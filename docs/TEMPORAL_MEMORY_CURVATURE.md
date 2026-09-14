# Temporal Memory Curvature: a testable hypothesis

## 1. From memory to geometry

Let `R(H)` denote an observable produced after a controlled history `H`. For two controllable operations `A` and `B`, define a closed history loop

```text
L_AB = A -> B -> A^-1 -> B^-1
```

and its opposite orientation

```text
L_BA = B -> A -> B^-1 -> A^-1.
```

The measured loop-orientation response is

```text
K_AB(g) = R(L_AB; g) - R(L_BA; g),
```

where `g` is a tunable system-environment coupling parameter.

The proposal is to treat `K_AB` as a **curvature-like response in history space**. It is not a new fundamental field or a claim about spacetime curvature.

## 2. Weak-coupling limit

For ordinary group commutators of small transformations, the Baker-Campbell-Hausdorff expansion gives a leading commutator term of second order:

```text
exp(gA) exp(gB) exp(-gA) exp(-gB)
    = exp(g^2 [A,B] + O(g^3)).
```

Our open-system loop is more general because each control pulse can also alter an unobserved environment state. The operational analogue is therefore defined from the measured response:

```text
C_AB = lim_{g -> 0} K_AB(g) / g^2,
```

when that limit exists.

`C_AB` is the proposed **temporal memory curvature coefficient** for the chosen preparation, controls, delay, and observable.

## 3. Why the coefficient matters

A single nonzero loop response is easy to fake with an expressive classical hidden state. The stronger object is the *whole response surface*:

```text
C_AB(delay, basis, preparation, reversal, ...)
```

A successful explanation must reproduce the surface, not just one point.

The project therefore tests three increasingly strong statements:

1. **History sensitivity:** `K_AB != 0`.
2. **Geometric scaling:** `K_AB ~ g^2 C_AB` over a controlled weak-coupling regime.
3. **Quantum structure:** the same response cannot be reproduced by the declared classical model class, and an independent quantumity witness becomes positive.

Only statement 3 could support a genuinely quantum interpretation.

## 4. Current numerical result

For the present two-qubit system+bath toy model, the exploratory weak-coupling fit over `g <= 0.10` gives

```text
power-law exponent = 1.9388
prefactor           = 0.5872
```

The result is close to the expected quadratic scaling, but the model is deliberately simple. This number is therefore a **research benchmark**, not a newly discovered exponent.

## 5. Stronger version: curvature tensor

Instead of one control pair, choose a basis of controls `{G_i}` and define pairwise coefficients

```text
C_ij = lim_{g -> 0} K_ij(g) / g^2.
```

The antisymmetric part

```text
Omega_ij = (C_ij - C_ji) / 2
```

is the candidate history-space curvature matrix.

With several measurement observables `M_a`, the experiment produces a response tensor

```text
Omega[a, i, j].
```

This creates a potentially useful object: a **temporal-memory curvature fingerprint**.

## 6. The hard question

Can two physically different memory mechanisms have the same low-order curvature tensor but different higher-order response?

That motivates a hierarchy:

```text
quadratic curvature
       ↓
 cubic / higher-order loop terms
       ↓
 delay dependence
       ↓
 cross-basis correlations
       ↓
 held-out history prediction
       ↓
 quantumity witness
```

This is where the project can go beyond a simple witness and become a spectroscopy framework.

## 7. Relation to current literature

Temporal memory and process tensors are already established. Recent work also gives operational quantum non-Markovianity tests, temporal-entanglement approaches, and process-tensor criteria tied to non-mixed-unitary behavior. The proposed curvature object is therefore presented as a **new research hypothesis and measurement architecture**, not as a claim that quantum memory itself is newly discovered.

The immediate literature anchors are:

- Di Pietra et al., *Temporal Entanglement and Witnesses of Non-Classicality* (2025): https://arxiv.org/abs/2506.15474
- Roy et al., *Semi-device-independent certification of quantum non-Markovianity using sequential random access codes* (2024): https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.012608
- Bäcker, Beyer & Strunz, *Quantum memory precludes mixed-unitary dynamics* (2026): https://journals.aps.org/prresearch/abstract/10.1103/dn6t-y9ky
- *Process Tensor Approaches to Non-Markovian Quantum Dynamics* (PRX, 2026): https://journals.aps.org/prx/abstract/10.1103/1ncg-11hz

## 8. Falsification rule

The curvature program fails as a physics claim if an increasingly expressive classical hidden-state family reproduces

- the full weak-coupling scaling,
- orientation reversal,
- delay dependence,
- multiple probe observables,
- and held-out histories

without requiring implausible or unbounded model complexity.

That failure would still leave a useful engineering result: a compact diagnostic of temporal noise structure.

A surviving residual does **not** automatically imply subquantum physics. Standard quantum open-system, process-tensor, and temporal-correlation models must be exhausted first.
