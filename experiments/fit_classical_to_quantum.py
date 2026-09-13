import itertools
import json
from pathlib import Path
import numpy as np
from dqnr.adversary import fit_to_quantum, classical_response
from dqnr.quantum_history import _run

train = tuple(''.join(x) for n in (1,2,3,4) for x in itertools.product('AB', repeat=n))
test = tuple(''.join(x) for n in (5,6) for x in itertools.product('AB', repeat=n))
fit = fit_to_quantum(train, dimension=4, seeds=6)
train_pred = fit.prediction
all_test_target = np.asarray([_run(list(h), 0.22, False) for h in test])
test_pred = np.asarray([classical_response(h, fit.params, 4) for h in test])
summary = {
    'dimension': 4,
    'train_n': len(train),
    'test_n': len(test),
    'train_mse': float(np.mean((train_pred-fit.target)**2)),
    'train_max_abs_residual': float(np.max(np.abs(train_pred-fit.target))),
    'test_mse': float(np.mean((test_pred-all_test_target)**2)),
    'test_max_abs_residual': float(np.max(np.abs(test_pred-all_test_target))),
    'test_mean_abs_residual': float(np.mean(np.abs(test_pred-all_test_target))),
}
out = Path(__file__).resolve().parents[1] / 'docs' / 'classical_fit_quantum.json'
out.write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
