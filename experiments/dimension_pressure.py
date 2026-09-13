import itertools, json
from pathlib import Path
import numpy as np
from dqnr.adversary import fit_to_quantum, classical_response
from dqnr.quantum_history import _run

def histories(ns):
    return tuple(''.join(x) for n in ns for x in itertools.product('AB', repeat=n))

train = histories((1,2,3,4))
test = histories((5,6))
all_rows = []
for d in (1,2,3,4,6):
    fit = fit_to_quantum(train, dimension=d, seeds=2)
    target_test = np.asarray([_run(list(h), 0.22, False) for h in test])
    pred_test = np.asarray([classical_response(h, fit.params, d) for h in test])
    row = {
        'dimension': d,
        'parameters': int(fit.params.size),
        'train_mse': float(np.mean((fit.prediction-fit.target)**2)),
        'train_max_abs': float(np.max(np.abs(fit.prediction-fit.target))),
        'test_mse': float(np.mean((pred_test-target_test)**2)),
        'test_mae': float(np.mean(np.abs(pred_test-target_test))),
        'test_max_abs': float(np.max(np.abs(pred_test-target_test))),
    }
    all_rows.append(row)
    print(json.dumps(row))

out = Path(__file__).resolve().parents[1] / 'docs' / 'dimension_pressure.json'
out.write_text(json.dumps({'train_histories': len(train), 'test_histories': len(test), 'results': all_rows}, indent=2))
