import itertools
import json
from pathlib import Path
import numpy as np
from dqnr.loop_geometry import sweep
from dqnr.adversary import classical_response, fit_to_quantum
from dqnr.quantum_history import _run

ROOT = Path(__file__).resolve().parents[1]
rows = sweep()


def histories(ns):
    return tuple(''.join(x) for n in ns for x in itertools.product('AB', repeat=n))


train = histories((1, 2, 3, 4))
test = histories((5, 6))
fit = fit_to_quantum(train, dimension=4, seeds=3)
quantum_test = np.asarray([_run(list(h), 0.22, False) for h in test])
pred_test = np.asarray([classical_response(h, fit.params, 4) for h in test])

result = {
    "loop_geometry": rows,
    "classical_adversary": {
        "dimension": 4,
        "train_mse": float(np.mean((fit.prediction - fit.target) ** 2)),
        "heldout_mse": float(np.mean((pred_test - quantum_test) ** 2)),
        "heldout_mae": float(np.mean(np.abs(pred_test - quantum_test))),
    },
    "interpretation": (
        "The loop observable is a diagnostic of history sensitivity, not a quantum certificate. "
        "The adversarial comparison asks whether finite classical hidden state remains predictive on unseen histories."
    ),
}
(ROOT / "docs" / "loop_geometry.json").write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
