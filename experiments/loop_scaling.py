import json
from pathlib import Path
import numpy as np
from dqnr.loop_geometry import sweep

ROOT = Path(__file__).resolve().parents[1]
rows = sweep((0.02, 0.03, 0.04, 0.06, 0.08, 0.10, 0.12, 0.16, 0.22, 0.30, 0.40))
small = [(r['g'], abs(r['orientation_defect'])) for r in rows if r['g'] <= 0.10 and r['orientation_defect'] != 0]
x = np.log([v[0] for v in small])
y = np.log([v[1] for v in small])
exponent, log_prefactor = np.polyfit(x, y, 1)
result = {
    'rows': rows,
    'small_g_power_law_exponent': float(exponent),
    'small_g_prefactor': float(np.exp(log_prefactor)),
    'interpretation': 'Exploratory scaling only. A near-quadratic small-g law is consistent with commutator-like response, but is not a quantum-memory certificate.'
}
(ROOT / 'docs' / 'loop_scaling.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
