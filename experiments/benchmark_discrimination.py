import json
from pathlib import Path
import numpy as np
from dqnr.models import ExperimentConfig, MarkovNoise, DriftNoise, FiniteMemoryNoise, LatentEnvironmentNoise, NonlinearHistoryNoise
from dqnr.protocol import generate_sequence
from dqnr.inference import compare_models

CASES = [
    ("M0_markov", MarkovNoise(), ExperimentConfig()),
    ("M1_drift", DriftNoise(), ExperimentConfig(drift=0.04)),
    ("M3_finite_memory", FiniteMemoryNoise(), ExperimentConfig()),
    ("M2_latent_environment", LatentEnvironmentNoise(rho=0.985), ExperimentConfig(latent_sigma=0.01)),
    ("M5_out_of_family", NonlinearHistoryNoise(), ExperimentConfig(nonlinear=0.25)),
]
rows = []
for name, model, cfg in CASES:
    best_depths, deltas = [], []
    for seed in range(10):
        y = generate_sequence(model, cfg, seed=10_000 + seed)
        scores = compare_models(y, max_depth=6)
        best = max(scores, key=lambda r: r["test_loglik"])
        best_depths.append(best["depth"])
        deltas.append(scores[-1]["test_loglik"] - scores[0]["test_loglik"])
    rows.append({
        "truth": name,
        "best_depths": best_depths,
        "median_best_depth": float(np.median(best_depths)),
        "fraction_memory_depth_ge_1": float(np.mean(np.asarray(best_depths) >= 1)),
        "median_test_loglik_gain_depth6_vs_depth0": float(np.median(deltas)),
    })
out = Path(__file__).resolve().parents[1] / "docs" / "discrimination_benchmark.json"
out.write_text(json.dumps(rows, indent=2))
for row in rows:
    print(row)
print(f"wrote {out}")
