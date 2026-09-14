# Master research state — 2026-09-14

## 1. What the project is now

The project began as **Does Quantum Noise Remember?** and is now a falsifiable research program for studying temporal structure in quantum-device noise.

The central question is no longer simply whether noise has memory. Temporal memory and non-Markovian dynamics are already established research topics, and process-tensor methods can characterize multitime dynamics. The project instead asks a harder model-discrimination question:

> Can a compact, experimentally practical set of history, reversal, and closed-loop measurements reveal temporal structure that is difficult for progressively richer classical hidden-state models to reproduce on completely unseen histories?

Only after a classical adversary is stressed should the surviving residual be passed to a **quantumity gate**.

---

## 2. Research ladder

The current adversarial ladder is:

- **M0** — stationary / Markov noise
- **M1** — deterministic drift
- **M2** — scalar colored or latent classical noise
- **M3** — finite-memory channels
- **M4** — vector hidden-state classical environments
- **M5** — nonlinear history-dependent classical models
- **Q** — explicit coherent system + environment models
- **Q+** — an independent quantumity witness, rather than memory alone
- **Residual** — held-out behavior not explained by the declared model family

A result can move upward only when lower models fail on data they did not see during fitting.

---

## 3. What has already been falsified

### 3.1 AB/BA asymmetry is not quantum-specific

The basic history-order statistic is

```text
A_H = 1/2 [R(AB) - R(BA)]
```

An explicit two-dimensional classical hidden environment with noncommuting A/B updates produces order dependence. Therefore `AB != BA` cannot be used as a quantum-memory certificate.

The current benchmark also contains a two-qubit coherent system+bath comparator. The exact toy model produces a clear order asymmetry, but this is only a controlled reference model.

### 3.2 Fitting short histories is not enough

A four-dimensional classical hidden-state model can fit short quantum-generated histories extremely closely while performing much worse on longer unseen histories.

Current exploratory dimension-pressure result:

| latent dimension | parameters | train MSE | held-out MSE |
|---:|---:|---:|---:|
| 1 | 6 | 8.05e-3 | 5.07e-2 |
| 2 | 15 | 1.68e-3 | 2.02e-2 |
| 3 | 28 | 5.91e-4 | 2.15e-1 |
| 4 | 45 | 7.79e-5 | 1.99e-1 |
| 6 | 91 | 3.61e-16 | 4.31e-2 |

This is evidence for a **predictive-complexity test**, not evidence that the underlying process is quantum.

The next step is to make these comparisons more statistically rigorous with repeated seeds, complexity penalties, stable dynamics constraints, random held-out histories, and confidence intervals.

---

## 4. The next-level physics direction: temporal memory geometry

The project now studies closed control loops instead of only single order swaps.

For two controls `A` and `B`, consider

```text
L_AB = A -> B -> A^-1 -> B^-1
L_BA = B -> A -> B^-1 -> A^-1
```

and measure

```text
K_AB(g) = R(L_AB; g) - R(L_BA; g).
```

Here `g` is a tunable system-environment coupling parameter in the toy model.

The working hypothesis is that `K_AB` can be treated as a **curvature-like response in history/control space**. This is a measurement construct, not a claim about spacetime curvature or a new fundamental field.

A single loop residual is not quantum-specific. The purpose of the loop is to create a larger family of constraints: orientation, reversal, coupling scaling, delay dependence, measurement basis, and predictive generalization.

---

## 5. Weak-coupling scaling result

The current two-qubit system+bath toy model gives the following exploratory loop scan:

| g | forward | reverse | closure/orientation defect |
|---:|---:|---:|---:|
| 0.02 | 0.830104 | 0.829517 | 0.0002937 |
| 0.03 | 0.825309 | 0.823995 | 0.0006573 |
| 0.04 | 0.818633 | 0.816313 | 0.0011599 |
| 0.06 | 0.799791 | 0.794682 | 0.0025545 |
| 0.08 | 0.773987 | 0.765177 | 0.0044054 |
| 0.10 | 0.741779 | 0.728550 | 0.0066147 |
| 0.12 | 0.703861 | 0.685738 | 0.0090614 |
| 0.16 | 0.614239 | 0.586062 | 0.0140885 |
| 0.22 | 0.460030 | 0.421054 | 0.0194882 |
| 0.30 | 0.261503 | 0.230146 | 0.0156785 |
| 0.40 | 0.104673 | 0.139473 | -0.0173997 |

A log-log fit over `g <= 0.10` gives an exploratory exponent of approximately

```text
1.9388
```

with prefactor approximately `0.5872`.

A near-quadratic response is compatible with a commutator-like weak-coupling effect, but this is **not a new physical law** and **not a quantum-memory certificate**. The strong-coupling region becomes non-monotonic, which is itself a useful feature to investigate because environmental backaction changes the simple perturbative regime.

---

## 6. Curvature fingerprint

For a set of controls `{X,Y,Z}`, define pairwise loop coefficients and the antisymmetric component

```text
Omega_ij = (C_ij - C_ji)/2.
```

At `g = 0.04`, the exploratory toy-model estimate is

```text
Omega ≈
[[ 0.000000, -0.449802,  0.827629],
 [ 0.449802,  0.000000,  0.708109],
 [-0.827629, -0.708109,  0.000000]]
```

with Frobenius norm of the measured finite-g antisymmetric matrix approximately `0.0026665`.

The interesting object is not one scalar. It is the response surface/tensor

```text
Omega[a, i, j]
```

across measurement observable, controls, delay, preparation, reversal, and coupling.

This motivates the phrase **temporal-memory curvature fingerprint**.

Again: this is a proposed spectroscopy object, not an established fundamental quantity.

---

## 7. The physics question we should attack next

The strongest version of the idea is:

> Can two physically different memory mechanisms share the same low-order temporal curvature while becoming distinguishable through higher-order loop terms, delay dependence, cross-basis response, or held-out multitime prediction?

This creates a hierarchy:

```text
second-order loop curvature
        ↓
third/fourth-order loop coefficients
        ↓
delay dependence
        ↓
cross-basis response tensor
        ↓
random held-out history prediction
        ↓
quantum-memory / nonclassicality witness
```

The intended contribution is therefore not “we discovered memory.” It is a possible **temporal-memory spectroscopy and model-discrimination framework**.

---

## 8. Quantumity gate

A genuinely quantum interpretation must be separated from generic non-Markovianity.

Useful existing routes include:

1. **Semi-device-independent quantum non-Markovianity.** Sequential QRAC-type protocols have been proposed in which classical-memory processes do not achieve the same sequential quantum advantage as a quantum-memory environment.
2. **Temporal nonclassicality / temporal Bell witnesses.** A qubit probe can, under stated assumptions, witness non-classicality through temporal Bell-type violations.
3. **Non-mixed-unitary process witnesses.** September 2026 work links quantum memory to non-mixed-unitary behavior and develops semidefinite-program witnesses using process-tensor structure.
4. **Process tensors and tensor-network simulation.** Recent 2026 work emphasizes process tensors as a practical framework for structured non-Markovian dynamics.

The project should use these as **independent quantumity gates**, not replace them with the curvature statistic.

---

## 9. Falsification rules

The stronger physics claim must be abandoned if a sufficiently expressive, stable, physically constrained classical model reproduces:

- history-order response,
- loop orientation,
- weak-coupling scaling,
- delay dependence,
- cross-basis response,
- reversal/echo behavior,
- and held-out histories

within experimental uncertainty without a material complexity disadvantage.

A surviving residual is still not automatically subquantum physics. Before invoking any nonstandard interpretation, the analysis must exhaust ordinary quantum open-system mechanisms, quantum-memory witnesses, process-tensor descriptions, calibration artifacts, compilation effects, and measurement loopholes.

---

## 10. Experimental translation

The eventual device protocol should look like:

```text
state preparation
      ↓
A/B history block
      ↓
optional delay
      ↓
optional reversal / echo
      ↓
probe
      ↓
X/Y/Z measurement basis
```

History strings should be randomly interleaved in wall-clock order so history type is not confounded with time drift.

The same data should be analyzed by every lower model before the quantumity gate is attempted.

---

## 11. Current status

**Established by this project:**

- classical hidden-state memory can mimic AB/BA order asymmetry;
- held-out prediction is a stronger discriminator than training fit;
- a simple coherent system+bath model produces measurable closed-loop response;
- the weak-coupling loop response is approximately quadratic in the current toy model;
- a multi-control curvature-like response tensor can be estimated.

**Not established:**

- that the curvature is uniquely quantum;
- that a real hardware device exhibits the predicted effect;
- that classical models cannot reproduce the full response surface;
- that the project has discovered a new law of physics;
- that any residual is subquantum or beyond quantum mechanics.

The project is ready for the next stage: **high-statistics adversarial classical fitting + higher-order loop spectroscopy + an independent quantumity witness.**
