# Roadmap

## Phase 1 — simulation

- Validate M0–M4 adversarial classical families.
- Add vector hidden-state classical models whose update matrices do not commute.
- Add explicit quantum-environment models (system + one/two bath qubits).
- Verify whether the order-antisymmetric statistic separates any model classes at all.

## Phase 2 — causal intervention

- Implement causal-break and state-repreparation protocols.
- Compare `AB`, `BA`, random permutation, and time-reversed histories.
- Add delay sweeps and dynamical-decoupling / echo controls.

## Phase 3 — quantum-circuit layer

- Qiskit Aer ideal/noise simulation.
- Hardware-agnostic circuit generator.
- Export circuits for IBM/IonQ style backends.
- Connect to the user's existing QEM auditing framework only after the synthetic tests are clean.

## Phase 4 — falsification

The project should be killed if an expressive classical hidden-state model reproduces all proposed signatures with no worse held-out performance.

A negative result is useful: it establishes that the proposed observable is not a practical quantum-memory discriminator.
