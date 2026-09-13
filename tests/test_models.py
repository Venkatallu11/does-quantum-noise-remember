import numpy as np
from dqnr.models import ExperimentConfig, MarkovNoise, FiniteMemoryNoise, VectorHiddenStateNoise
from dqnr.protocol import generate_sequence, summarize_history_contrast
from dqnr.quantum_history import matched_quantum_order

def test_markov_sequence_is_binary():
    y = generate_sequence(MarkovNoise(), ExperimentConfig(n_shots=500), seed=2)
    assert set(np.unique(y)).issubset({0.0, 1.0})
    assert len(y) == 500

def test_history_contrast_runs():
    y = generate_sequence(FiniteMemoryNoise(), ExperimentConfig(n_shots=1000), seed=3)
    s = summarize_history_contrast(y)
    assert np.isfinite(s["delta"])
    assert s["n_same"] + s["n_diff"] == 999

def test_vector_hidden_state_is_order_sensitive():
    m = VectorHiddenStateNoise()
    cfg = ExperimentConfig()
    ab = m.probability_for_history(list("AB"), cfg)
    ba = m.probability_for_history(list("BA"), cfg)
    assert abs(ab - ba) > 1e-6

def test_quantum_history_comparator_runs():
    r = matched_quantum_order()
    assert 0.0 <= r.ab <= 1.0
    assert 0.0 <= r.ba <= 1.0
