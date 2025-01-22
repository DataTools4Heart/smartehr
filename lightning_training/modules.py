import torch
import torch.nn as nn
import lightning.pytorch as L
from pycox.models.loss import nll_pmf
from lightning_training.metrics import SurvMetrics
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

from peft import LoraConfig
import peft
import bitsandbytes as bnb

class SurvivalAnalysisModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float):
        super().__init__()
        self.model = model
        self.lr = lr
        self.surv_metrics = SurvMetrics(evaluation_times=[i for i in range(1, self.model.time_intervals)])

    def training_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True)
        return loss

    def validation_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True)
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def test_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def on_validation_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        for t, ci in results["ci"].items():
            self.log(f"ci_{t}", ci, rank_zero_only=True, sync_dist=True)
        for t, roc in results["roc_auc"].items():
            self.log(f"roc_auc_{t}", roc, rank_zero_only=True, sync_dist=True)

    def on_test_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        print(results)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        return optimizer


class SurvivalAnalysisModuleLLM(SurvivalAnalysisModule):
    def __init__(self, model: nn.Module, lr: float):
        #self.time_intervals = time_intervals
        super().__init__(model=model,lr=lr)
        #self.model.config.use_cache = False
        self.peft_config = LoraConfig(
                            lora_alpha=4, lora_dropout=0.1, r=16,
                            bias="none", #task_type="CAUSAL_LM",
                            target_modules=[
                                "q_proj",
                                'k_proj',
                                'v_proj',
                                'fc1',
                                'fc2'])
                
        self.model = peft.get_peft_model(self.model, self.peft_config)
        #self.model.config.use_cache = False

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.lr)
        return optimizer
