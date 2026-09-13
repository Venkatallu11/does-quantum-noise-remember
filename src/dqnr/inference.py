from __future__ import annotations
import numpy as np
from scipy.special import expit
from scipy.optimize import minimize

def _design(y: np.ndarray, depth: int):
    y = np.asarray(y, dtype=float)
    n = len(y)
    if depth < 0 or depth >= n:
        raise ValueError("depth must satisfy 0 <= depth < len(y)")
    rows, target = [], []
    for t in range(depth, n):
        time = t / max(n - 1, 1)
        if depth == 0:
            row = [1.0, time]
        else:
            h = y[t-depth:t][::-1]
            lags = np.arange(1, depth + 1, dtype=float)
            row = [1.0, time, *h, *(h * lags)]
        rows.append(row)
        target.append(y[t])
    return np.asarray(rows, dtype=float), np.asarray(target, dtype=float)

def _fit(X, y):
    def loss(beta):
        z = X @ beta
        return float(np.sum(np.logaddexp(0, z) - y * z) + 1e-3 * np.sum(beta[1:] ** 2))
    res = minimize(loss, np.zeros(X.shape[1]), method="L-BFGS-B")
    if not res.success:
        raise RuntimeError(f"logistic fit failed: {res.message}")
    return res.x

def _score(X, y, beta):
    p = expit(X @ beta)
    return float(np.sum(y * np.log(np.clip(p, 1e-9, 1)) + (1-y) * np.log(np.clip(1-p, 1e-9, 1))))

def compare_models(y: np.ndarray, max_depth: int = 6, holdout: float = 0.25):
    y = np.asarray(y, dtype=float)
    if not 0 < holdout < 0.8:
        raise ValueError("holdout must be between 0 and 0.8")
    results = []
    for depth in range(max_depth + 1):
        X, target = _design(y, depth)
        cut = max(1, int(len(X) * (1 - holdout)))
        beta = _fit(X[:cut], target[:cut])
        results.append({
            "depth": depth,
            "n_parameters": int(X.shape[1]),
            "train_loglik": _score(X[:cut], target[:cut], beta),
            "test_loglik": _score(X[cut:], target[cut:], beta) if cut < len(X) else np.nan,
            "n_test": max(len(X) - cut, 0),
        })
    return results

def history_residual(y: np.ndarray, depth: int = 4):
    X, target = _design(np.asarray(y, float), depth)
    beta = _fit(X, target)
    p = expit(X @ beta)
    residual = target - p
    return {
        "residual": residual,
        "mean": float(np.mean(residual)),
        "rms": float(np.sqrt(np.mean(residual**2))),
        "beta": beta,
    }
