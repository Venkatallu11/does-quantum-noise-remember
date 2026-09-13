from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class ExperimentConfig:
    n_shots: int = 4000
    p0: float = 0.12
    amplitude: float = 0.06
    memory: int = 4
    drift: float = 0.0
    latent_sigma: float = 0.0
    nonlinear: float = 0.0

class BaseNoise:
    name = "base"
    def reset(self):
        pass
    def probability(self, t: int, history: np.ndarray, cfg: ExperimentConfig) -> float:
        raise NotImplementedError

class MarkovNoise(BaseNoise):
    name = "M0_markov"
    def probability(self, t, history, cfg):
        return np.clip(cfg.p0 + cfg.amplitude, 0.0, 1.0)

class DriftNoise(BaseNoise):
    name = "M1_drift"
    def probability(self, t, history, cfg):
        x = 2.0 * t / max(cfg.n_shots - 1, 1) - 1.0
        return np.clip(cfg.p0 + cfg.amplitude + cfg.drift * x, 0.0, 1.0)

class FiniteMemoryNoise(BaseNoise):
    name = "M3_finite_memory"
    def probability(self, t, history, cfg):
        if len(history) == 0:
            h = 0.0
        else:
            w = np.exp(-np.arange(len(history)) / max(cfg.memory, 1))
            h = np.sum(w * (history[::-1] - 0.5)) / np.sum(w)
        return np.clip(cfg.p0 + cfg.amplitude + 0.12 * h, 0.0, 1.0)

class LatentEnvironmentNoise(BaseNoise):
    name = "M2_latent_environment"
    def __init__(self, rho: float = 0.97):
        self.rho = rho
        self.x = 0.0
    def reset(self):
        self.x = 0.0
    def probability(self, t, history, cfg):
        if t:
            self.x = self.rho * self.x + np.random.normal(scale=cfg.latent_sigma)
        return np.clip(cfg.p0 + cfg.amplitude + self.x, 0.0, 1.0)

class RenewalNoise(BaseNoise):
    name = "M4_renewal"
    def __init__(self, relax: float = 8.0):
        self.relax = relax
    def probability(self, t, history, cfg):
        if not len(history):
            age = self.relax
        else:
            age = 0
            for x in history[::-1]:
                if x < 0:
                    break
                age += 1
        return np.clip(cfg.p0 + cfg.amplitude * np.exp(-age / self.relax), 0.0, 1.0)

class NonlinearHistoryNoise(BaseNoise):
    name = "M5_out_of_family"
    def probability(self, t, history, cfg):
        if not len(history):
            h = 0.0
        else:
            recent = history[-min(6, len(history)):]
            h = float(np.mean((recent - 0.5) ** 3))
        return np.clip(cfg.p0 + cfg.amplitude + 1.8 * cfg.nonlinear * h, 0.0, 1.0)

class VectorHiddenStateNoise(BaseNoise):
    """Classical vector hidden-state adversary.

    The hidden state is multidimensional and its A/B updates need not commute.
    This model is intentionally stronger than a scalar colored-noise model: it can
    generate order effects without invoking a quantum environment.
    """
    name = "M6_vector_hidden_state"

    def __init__(self, rho: float = 0.93, coupling: float = 0.11):
        self.rho = float(rho)
        self.coupling = float(coupling)
        self.x = np.zeros(2, dtype=float)

    def reset(self):
        self.x = np.zeros(2, dtype=float)

    def push_symbol(self, symbol: str):
        # Non-commuting 2x2 linear updates.
        if symbol == "A":
            M = np.array([[self.rho, self.coupling], [0.0, self.rho]], float)
            b = np.array([0.16, 0.02])
        elif symbol == "B":
            M = np.array([[self.rho, 0.0], [-self.coupling, self.rho]], float)
            b = np.array([-0.11, 0.15])
        else:
            raise ValueError("symbol must be A or B")
        self.x = M @ self.x + b

    def probability_for_history(self, history: list[str], cfg: ExperimentConfig) -> float:
        x = np.zeros(2, dtype=float)
        old = self.x.copy()
        self.x = x
        for symbol in history:
            self.push_symbol(symbol)
        val = cfg.p0 + cfg.amplitude + 0.18 * self.x[0] + 0.10 * self.x[1]
        self.x = old
        return float(np.clip(val, 0.001, 0.999))

    def probability(self, t, history, cfg):
        # Sequence mode is kept for compatibility with generate_sequence.
        return self.probability_for_history(["A" if v > 0.5 else "B" for v in history[-8:]], cfg)
