from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class EchoResult:
    ab: float
    ba: float
    aa: float
    bb: float
    antisymmetry: float
    symmetric_memory: float
    standardized: float


def matched_order_statistics(
    history: list[str],
    repeats: int = 4000,
    seed: int = 0,
    response_strength: float = 0.10,
    noise_floor: float = 0.20,
) -> EchoResult:
    """Estimate AB/BA response asymmetry under an order-sensitive diagnostic model.

    This is a diagnostic primitive, not a quantum-memory certificate. Classical
    adversaries are explicitly benchmarked elsewhere in the repository.
    """
    if sorted(history) != ["A", "B"]:
        raise ValueError("history must contain exactly ['A','B'] in either order")
    rng = np.random.default_rng(seed)
    def run(h):
        s = 0.0
        phase = 0.0
        for i, symbol in enumerate(h):
            u = 1.0 if symbol == "A" else -1.0
            phase += (i + 1) * (0.7 if symbol == "A" else -0.55)
            s = 0.91 * s + 0.18 * u + 0.05 * np.sin(phase)
        p = np.clip(0.5 + response_strength * s, 1e-4, 1 - 1e-4)
        y = rng.random(repeats) < p
        return float(np.mean(y))
    ab = run(["A", "B"])
    ba = run(["B", "A"])
    aa = run(["A", "A"])
    bb = run(["B", "B"])
    anti = 0.5 * (ab - ba)
    symmetric = 0.5 * ((ab + ba) - (aa + bb))
    se = np.sqrt(max((ab * (1 - ab) + ba * (1 - ba)) / (2 * repeats), 1e-12))
    return EchoResult(ab, ba, aa, bb, float(anti), float(symmetric), float(anti / se))
