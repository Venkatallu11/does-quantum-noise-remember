from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.optimize import least_squares
from scipy.special import expit
from .quantum_history import _run

@dataclass(frozen=True)
class ClassicalFit:
    loss: float
    histories: tuple[str, ...]
    target: np.ndarray
    prediction: np.ndarray
    params: np.ndarray
    dimension: int

def _decode(theta, d):
    k = d * d
    A = theta[0:k].reshape(d, d)
    B = theta[k:2*k].reshape(d, d)
    i = 2*k
    a = theta[i:i+d]; i += d
    b = theta[i:i+d]; i += d
    w = theta[i:i+d]; i += d
    bias = theta[i]
    return A, B, a, b, w, bias

def classical_response(history: str, theta: np.ndarray, dimension: int = 2) -> float:
    A, B, a, b, w, bias = _decode(theta, dimension)
    x = np.zeros(dimension)
    for symbol in history:
        if symbol == "A":
            x = A @ x + a
        elif symbol == "B":
            x = B @ x + b
        else:
            raise ValueError("history symbols must be A/B")
    return float(expit(bias + w @ x))

def fit_to_quantum(train_histories: tuple[str, ...], g: float = 0.22, dimension: int = 4, seeds: int = 48) -> ClassicalFit:
    target = np.asarray([_run(list(h), g, echo=False) for h in train_histories], float)
    npar = 2 * dimension * dimension + 3 * dimension + 1
    best = None
    rng = np.random.default_rng(20260912 + dimension)
    for _ in range(seeds):
        x0 = rng.normal(scale=0.15, size=npar)
        def residual(theta):
            pred = np.asarray([classical_response(h, theta, dimension) for h in train_histories])
            return pred - target
        result = least_squares(residual, x0, max_nfev=1200)
        loss = float(np.mean(residual(result.x) ** 2))
        if best is None or loss < best.loss:
            pred = np.asarray([classical_response(h, result.x, dimension) for h in train_histories])
            best = ClassicalFit(loss, train_histories, target, pred, result.x, dimension)
    assert best is not None
    return best
