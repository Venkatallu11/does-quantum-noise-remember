"""Controlled history-order experiment.

The scientific point is not to call AB != BA "quantum". The experiment asks how much
order asymmetry survives after increasingly expressive classical adversaries are fitted.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from dqnr.echo import matched_order_statistics

def scalar_classical(history, rho=0.92, strength=0.10):
    s = 0.0
    for symbol in history:
        u = 1.0 if symbol == "A" else -1.0
        s = rho * s + (1-rho) * u
    return 0.5 + strength*s

def nonlinear_classical(history, rho=0.92, strength=0.10):
    s = scalar_classical(history, rho, strength)
    return 0.5 + 0.85*(s-0.5) + 0.20*(s-0.5)**3

def main():
    rows = []
    for seed in range(20):
        r = matched_order_statistics(["A", "B"], repeats=6000, seed=seed)
        rows.append({"seed": seed, "AB": r.ab, "BA": r.ba, "AA": r.aa, "BB": r.bb, "antisymmetry": r.antisymmetry, "symmetric_memory": r.symmetric_memory, "z": r.standardized})
    arr = np.asarray([x["antisymmetry"] for x in rows])
    out = {"n_seeds": len(rows), "median_antisymmetry": float(np.median(arr)), "mad_antisymmetry": float(np.median(np.abs(arr-np.median(arr))),), "fraction_abs_z_gt_3": float(np.mean(np.abs([x["z"] for x in rows]) > 3)), "records": rows, "interpretation": "order asymmetry is a candidate residual only; it is not a quantum-memory certificate"}
    path = Path(__file__).resolve().parents[1]/"docs"/"history_echo_sweep.json"
    path.write_text(json.dumps(out, indent=2))
    print(json.dumps({k:v for k,v in out.items() if k != "records"}, indent=2))

if __name__ == "__main__":
    main()
