# Temporal Memory Geometry: a next-level research direction

## The proposed leap

The project should stop treating a nonzero `AB - BA` response as the endpoint. Instead, treat controlled histories as **paths through a memory state space** and study the response to closed history loops.

A basic loop is

```text
A -> B -> A^-1 -> B^-1
```

where `A^-1` and `B^-1` undo the intended system control. The system is then interrogated for a residual. Define a loop-closure defect

```text
K_AB = R(ABA^-1B^-1) - R(BAB^-1A^-1).
```

This is analogous to a group-commutator response: it probes the order sensitivity of the process rather than merely asking whether history exists.

## Why this is interesting

Ordinary temporal correlation, drift, and finite classical hidden-state memory can all produce `AB != BA`. Our own simulations already demonstrate that explicitly. A closed-loop protocol gives a larger family of constraints: orientation, reversal, coupling scaling, delay dependence, and cross-basis response must all be explained together.

The key scientific rule remains adversarial:

> A loop residual is evidence of history sensitivity, not evidence of quantum memory.

A classical multidimensional hidden state can have noncommuting update maps and therefore produce loop responses too.

## The proposed three-gate program

### Gate 1 — History geometry

Measure a family of loop observables across coupling, delay, orientation, basis, and echo/reversal conditions.

### Gate 2 — Classical compression test

Fit progressively richer classical hidden-state models. Train on one set of histories and evaluate on completely unseen histories and loop families. Track predictive error per latent dimension.

### Gate 3 — Quantumity test

Only a residual that survives the classical model ladder should be passed to a quantumity analysis. Two especially relevant existing directions are:

1. **Temporal Bell / temporal-entanglement tests.** A 2025 work gives a qubit-probe protocol linking temporal Bell-inequality violation to non-classicality under a conservation-law assumption and reports proof-of-principle NMR emulations. [Di Pietra et al., 2025](https://arxiv.org/abs/2506.15474)
2. **Non-mixed-unitary memory witnesses.** A September 2026 Physical Review Research paper connects quantum memory to non-mixed-unitary structure and gives a hierarchy of semidefinite-program witnesses in the process-tensor language, including incomplete-tomography examples. [Bäcker, Beyer & Strunz, 2026](https://journals.aps.org/prresearch/abstract/10.1103/dn6t-y9ky)

This is important because generic non-Markovianity is not enough. Modern work already provides process-tensor descriptions of memory and operational routes to certify quantum non-Markovianity. [Process Tensor Approaches to Non-Markovian Quantum Dynamics, PRX 2026](https://journals.aps.org/prx/abstract/10.1103/1ncg-11hz); [Roy et al., 2024](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.012608)

## Current simulation result

The first loop scan with the two-qubit system+bath toy model gives:

| g | forward loop | reverse loop | closure defect |
|---:|---:|---:|---:|
| 0.04 | 0.818633 | 0.816313 | 0.001160 |
| 0.08 | 0.773987 | 0.765177 | 0.004405 |
| 0.12 | 0.703861 | 0.685738 | 0.009061 |
| 0.16 | 0.614239 | 0.586062 | 0.014089 |
| 0.22 | 0.460030 | 0.421054 | 0.019489 |
| 0.30 | 0.261503 | 0.230146 | 0.015679 |
| 0.40 | 0.104673 | 0.139473 | 0.017400 |

For the smallest couplings the exploratory log-log fit gives an exponent of about `1.94`, compatible with a leading commutator-like response. This is **not** evidence of a new law: it is only a numerical signature that motivates further controlled scaling tests.

## The falsification ladder

A future real-device claim should require all of the following:

1. The loop signal survives randomized interleaving and calibration controls.
2. A scalar colored-noise model fails on held-out histories.
3. A vector hidden-state model fails on held-out longer histories.
4. Increasing classical latent dimension does not cheaply remove the residual.
5. The effect survives independent compilation and backend changes.
6. A quantumity witness, not merely a memory witness, becomes positive.
7. A second device or an independent simulator family reproduces the effect.

If any lower layer succeeds, the stronger interpretation is rejected.

## What could become genuinely new

The most interesting possible result is not simply a new memory witness. It would be a **memory-complexity phase diagram** showing how much classical hidden-state capacity is required to reproduce a given family of temporal loops, compared with the smallest quantum-environment model that reproduces them.

That would turn the project into a quantitative question:

> How much physical memory is required to reproduce a temporal process, and what changes when the memory is genuinely quantum?

That question can connect open-system physics, quantum information, causal modeling, and experimental quantum-device diagnostics without assuming any nonstandard physics in advance.

## Status

This is a research hypothesis and experimental design, not a claim of discovered new physics. The present toy calculations establish that loop geometry is measurable in the chosen model and that our classical adversarial benchmark remains a necessary part of the analysis.
