import json
from pathlib import Path
from dqnr.models import ExperimentConfig, VectorHiddenStateNoise
from dqnr.quantum_history import matched_quantum_order, sample_order

cfg = ExperimentConfig()
model = VectorHiddenStateNoise(rho=0.93, coupling=0.11)
rows = []
for history in (("AB",), ("BA",), ("AA",), ("BB",)):
    h = list(history[0])
    p = model.probability_for_history(h, cfg)
    rows.append({"history": history[0], "classical_probability": p})
q = matched_quantum_order(g=0.22)
shot = sample_order(q, repeats=20000, seed=123)
rows.append({"history": "QUANTUM_EXACT", "quantum": q.__dict__, "quantum_shot_estimate": shot})
out = Path(__file__).resolve().parents[1] / "docs" / "order_adversary.json"
out.write_text(json.dumps(rows, indent=2))
print(json.dumps(rows, indent=2))
