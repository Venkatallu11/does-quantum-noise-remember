from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .quantum_history import _rx, _rz, _interaction, _kron

X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

@dataclass(frozen=True)
class LoopResult:
    forward: float
    reverse: float
    closure_defect: float
    orientation_defect: float
    loop_phase_proxy: float


def _run_extended(sequence: str, g: float = 0.22) -> float:
    """Two-qubit system+bath evolution with A/B and their formal inverses a/b."""
    state = np.zeros(4, dtype=complex)
    state[0] = 1.0
    ui = _interaction(g)
    gates = {
        "A": _kron(_rx(0.83), I2),
        "B": _kron(_rz(-1.17), I2),
        "a": _kron(_rx(-0.83), I2),
        "b": _kron(_rz(1.17), I2),
    }
    for symbol in sequence:
        state = ui @ (gates[symbol] @ state)
    rho = np.outer(state, state.conj()).reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
    z = float(np.real(np.trace(Z @ rho)))
    return float(np.clip((1 + z) / 2, 0, 1))


def loop_geometry(g: float = 0.22) -> LoopResult:
    # Group-commutator-like loops. Lowercase symbols are inverse controls.
    fwd = _run_extended("ABab", g)
    rev = _run_extended("BAba", g)
    defect = 0.5 * abs(fwd - rev)
    orientation = 0.5 * (fwd - rev)
    phase = float(orientation * (1 - 2 * defect))
    return LoopResult(fwd, rev, defect, orientation, phase)


def sweep(couplings=(0.04, 0.08, 0.12, 0.16, 0.22, 0.30, 0.40)) -> list[dict]:
    rows = []
    for g in couplings:
        r = loop_geometry(g)
        rows.append({
            "g": g,
            "forward": r.forward,
            "reverse": r.reverse,
            "closure_defect": r.closure_defect,
            "orientation_defect": r.orientation_defect,
            "loop_phase_proxy": r.loop_phase_proxy,
        })
    return rows
