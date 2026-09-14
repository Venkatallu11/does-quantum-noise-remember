import json
from pathlib import Path
import numpy as np
from dqnr.quantum_history import _rx, _rz, _interaction, _kron

I2 = np.eye(2, dtype=complex)


def _ry(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], complex)


def response(seq, g=0.04):
    state = np.zeros(4, complex)
    state[0] = 1
    ui = _interaction(g)
    controls = {
        'X': _kron(_rx(0.73), I2),
        'Y': _kron(_ry(-0.61), I2),
        'Z': _kron(_rz(0.89), I2),
        'x': _kron(_rx(-0.73), I2),
        'y': _kron(_ry(0.61), I2),
        'z': _kron(_rz(-0.89), I2),
    }
    for s in seq:
        state = ui @ (controls[s] @ state)
    rho = np.outer(state, state.conj()).reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
    Z = np.array([[1, 0], [0, -1]], complex)
    return float(np.real(np.trace(Z @ rho)))


labels = ['X', 'Y', 'Z']
g = 0.04
K = np.zeros((3, 3))
for i, a in enumerate(labels):
    for j, b in enumerate(labels):
        if i == j:
            continue
        f = response(a + b + a.lower() + b.lower(), g)
        r = response(b + a + b.lower() + a.lower(), g)
        K[i, j] = 0.5 * (f - r)
Omega = 0.5 * (K - K.T)
C_est = Omega / (g * g)
result = {
    'g': g,
    'controls': labels,
    'K': K.tolist(),
    'Omega': Omega.tolist(),
    'curvature_estimate': C_est.tolist(),
    'frobenius_norm': float(np.linalg.norm(Omega)),
    'interpretation': 'Exploratory curvature tensor for a fixed two-qubit toy model; not a quantum witness.'
}
Path(Path(__file__).resolve().parents[1] / 'docs' / 'curvature_tensor.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
