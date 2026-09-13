from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class QuantumOrderResult:
    ab: float
    ba: float
    aa: float
    bb: float
    antisymmetry: float
    echo_antisymmetry: float

def _rx(theta: float) -> np.ndarray:
    c, s = np.cos(theta / 2), -1j * np.sin(theta / 2)
    return np.array([[c, s], [s, c]], dtype=complex)

def _rz(theta: float) -> np.ndarray:
    return np.array([[np.exp(-1j*theta/2), 0], [0, np.exp(1j*theta/2)]], dtype=complex)

def _kron(*ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out

def _interaction(g: float) -> np.ndarray:
    xx = _kron(np.array([[0,1],[1,0]], complex), np.array([[0,1],[1,0]], complex))
    return np.cos(g)*np.eye(4, dtype=complex) - 1j*np.sin(g)*xx

def _run(history: list[str], g: float, echo: bool = False) -> float:
    state = np.zeros(4, dtype=complex)
    state[0] = 1.0
    u = _interaction(g)
    gates = {"A": _kron(_rx(0.83), np.eye(2)), "B": _kron(_rz(-1.17), np.eye(2))}
    for symbol in history:
        state = u @ (gates[symbol] @ state)
    if echo:
        for symbol in reversed(history):
            state = u.conj().T @ (gates[symbol].conj().T @ state)
    rho = np.outer(state, state.conj()).reshape(2,2,2,2).trace(axis1=1, axis2=3)
    z = float(np.real(np.trace(np.array([[1,0],[0,-1]], complex) @ rho)))
    return float(np.clip((1 + z)/2, 0, 1))

def matched_quantum_order(g: float = 0.22) -> QuantumOrderResult:
    vals = {h:_run(list(h),g,False) for h in ("AB","BA","AA","BB")}
    anti = 0.5*(vals["AB"]-vals["BA"])
    echo_vals = {h:_run(list(h),g,True) for h in ("AB","BA")}
    return QuantumOrderResult(vals["AB"],vals["BA"],vals["AA"],vals["BB"],float(anti),float(0.5*(echo_vals["AB"]-echo_vals["BA"])))

def sample_order(result: QuantumOrderResult, repeats: int = 4000, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    out = {k:float(np.mean(rng.random(repeats) < getattr(result,k))) for k in ("ab","ba","aa","bb")}
    out["antisymmetry"] = 0.5*(out["ab"]-out["ba"])
    return out
