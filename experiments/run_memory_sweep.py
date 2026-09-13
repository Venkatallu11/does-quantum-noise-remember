import json
import numpy as np
from pathlib import Path
from dqnr.models import ExperimentConfig, MarkovNoise, DriftNoise, FiniteMemoryNoise, LatentEnvironmentNoise, NonlinearHistoryNoise
from dqnr.protocol import generate_sequence, summarize_history_contrast
from dqnr.inference import compare_models, history_residual

OUT = Path(__file__).resolve().parents[1] / "docs" / "first_sweep.json"

cases = [
    (MarkovNoise(), ExperimentConfig()),
    (DriftNoise(), ExperimentConfig(drift=0.04)),
    (FiniteMemoryNoise(), ExperimentConfig()),
    (LatentEnvironmentNoise(rho=0.985), ExperimentConfig(latent_sigma=0.01)),
    (NonlinearHistoryNoise(), ExperimentConfig(nonlinear=0.25)),
]

results = []
for i, (model, cfg) in enumerate(cases):
    y = generate_sequence(model, cfg, seed=100 + i)
    results.append({
        "model": model.name,
        "history": summarize_history_contrast(y, lag=1),
        "residual": (lambda rr: {"mean": rr["mean"], "rms": rr["rms"], "beta": rr["beta"].tolist(), "residual": rr["residual"].tolist()})(history_residual(y, depth=4)),
        "comparison": compare_models(y, max_depth=6),
    })

OUT.write_text(json.dumps(results, indent=2))
print(f"wrote {OUT}")
for r in results:
    print(r["model"], r["history"], "best_test_loglik_depth", max(r["comparison"], key=lambda x: x["test_loglik"])["depth"])
