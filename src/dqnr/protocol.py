from __future__ import annotations
import numpy as np
from .models import ExperimentConfig, BaseNoise

def generate_sequence(model: BaseNoise, cfg: ExperimentConfig, seed: int = 0):
    rng = np.random.default_rng(seed)
    old_state = np.random.get_state()
    np.random.seed(seed)
    try:
        model.reset()
        y = np.empty(cfg.n_shots, dtype=float)
        for t in range(cfg.n_shots):
            probe = 1 if (t % 2 == 0) else -1
            history = y[max(0, t - 12):t].copy()
            p = model.probability(t, history, cfg)
            p = np.clip(p + 0.015 * probe, 0.001, 0.999)
            y[t] = float(rng.random() < p)
        return y
    finally:
        np.random.set_state(old_state)

def summarize_history_contrast(y: np.ndarray, lag: int = 1) -> dict:
    if lag >= len(y):
        raise ValueError("lag must be smaller than sequence length")
    prev = y[:-lag]
    curr = y[lag:]
    same = curr[prev == 1]
    diff = curr[prev == 0]
    if len(same) == 0 or len(diff) == 0:
        raise ValueError("both history classes need observations")
    delta = float(np.mean(same) - np.mean(diff))
    se = float(np.sqrt(np.var(same, ddof=1) / len(same) + np.var(diff, ddof=1) / len(diff)))
    z = delta / se if se > 0 else np.inf
    return {"delta": delta, "se": se, "z": float(z), "n_same": len(same), "n_diff": len(diff)}
