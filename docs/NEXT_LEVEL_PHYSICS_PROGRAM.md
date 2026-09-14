# Next-level physics program

## Working title

**Temporal Memory Geometry and Quantumity Spectroscopy**

## The central idea

Do not ask only whether the environment remembers the past. Ask how the observable response transforms when the control history is changed along closed paths.

The project treats a controlled history `H` as an input to an observable response `R(H)` and studies:

```text
order sensitivity
      ↓
closed-loop response
      ↓
weak-coupling expansion
      ↓
higher-order temporal geometry
      ↓
predictive complexity
      ↓
quantumity
```

## Hypothesis A — temporal curvature

For two controls `A,B`, define

```text
K_AB(g) = R(ABA^-1B^-1; g) - R(BAB^-1A^-1; g).
```

If a weak-coupling expansion exists,

```text
K_AB(g) = g^2 C_AB + g^3 D_AB + g^4 E_AB + ...
```

we can study the coefficients as a spectroscopy of the environment-mediated history response.

The first project result is only that the current toy system shows a near-quadratic small-coupling regime. The coefficients are not asserted to be fundamental invariants.

## Hypothesis B — higher-order memory contains new information

Two mechanisms may share the same second-order coefficient `C_AB` but differ in `D_AB`, `E_AB`, delay dependence, or cross-basis tensors.

Therefore test:

```text
second order
     vs
third/fourth order
     vs
delay-resolved response
     vs
cross-basis tensor
```

This creates a stronger fingerprint than one scalar witness.

## Hypothesis C — memory has a predictive complexity cost

A physical process should be judged by whether a compact model predicts unseen histories, not by whether a flexible model can interpolate training data.

Define a practical complexity curve

```text
C_cl(D) = held-out error of classical latent dimension D
C_q(d) = held-out error of quantum environment dimension d
```

Then study an empirical gap such as

```text
Delta(D,d) = C_cl(D) - C_q(d)
```

under equalized data volume, regularization, and parameter budget.

This is not a theorem of classical-vs-quantum computational complexity. It is an experimentally testable model-selection quantity.

## Hypothesis D — loop geometry can be used as a search primitive

Rather than reconstructing the entire process tensor everywhere, use curvature and delay scans to locate regimes where memory is structurally rich.

Proposed workflow:

```text
cheap loop scan
      ↓
locate strong / anomalous geometry
      ↓
classical adversarial compression
      ↓
held-out history test
      ↓
quantumity gate
      ↓
full process-tensor analysis only if necessary
```

This is potentially the practical contribution even if the final physics is completely standard.

## Hypothesis E — closed loops may reveal a memory holonomy-like effect

A speculative extension is to compare loops built from different paths connecting the same endpoint. If

```text
R(H1) != R(H2)
```

for histories with the same intended net control but different temporal ordering, then the process is path-sensitive in history space.

A family of such loop comparisons may be organized as a holonomy-like object. This is only an analogy to geometry; no spacetime interpretation should be made without an explicit derivation.

The scientific target is to determine whether this path dependence is:

1. fully explained by ordinary classical hidden state,
2. naturally explained by a quantum environment,
3. or associated with a stronger nonclassical witness.

## Hypothesis F — subquantum physics is a last-resort branch

The existing `subquantum-medium` work is not imported as an assumption into this project.

A hypothetical non-Born or subquantum mechanism would only become relevant after:

```text
ordinary drift
→ classical colored noise
→ classical hidden-state memory
→ standard quantum open-system memory
→ measurement / compilation artifacts
→ quantumity witnesses
```

have been tested and excluded.

A leftover residual by itself is never enough to claim subquantum physics.

## Next experimental matrix

### Coupling

```text
g = 0.01 ... 0.25
```

with dense sampling in the perturbative region and a separate strong-coupling region.

### Delay

Use logarithmically spaced delays plus matched zero-delay controls.

### Histories

Include:

```text
AB / BA
AA / BB
ABab / BAba
ABC... inverse loops
random permutations
long unseen strings
```

### Measurements

Use several observables, at minimum X/Y/Z on the system probe.

### Nuisance controls

Randomize wall-clock ordering, compilation seeds, reset order, and measurement basis order. Include causal breaks and state re-preparation.

### Replication

At minimum:

- independent random seeds;
- independent simulator implementation;
- second backend or physical platform before strong claims.

## Success criterion for a serious physics paper

A publishable physics result would need a coherent chain:

```text
reproducible temporal geometry
        +
classical adversaries fail on held-out data
        +
higher-order / delay structure is nontrivial
        +
independent quantumity witness succeeds
        +
artifact controls pass
        +
independent replication
```

The final paper should explicitly state the class of classical models ruled out, the statistical uncertainty, and the assumptions behind the quantumity witness.

## Kill criterion

The project should pivot to an engineering/diagnostic paper if a well-regularized classical hidden-state family reproduces the complete observable response surface with no meaningful predictive-complexity disadvantage.

That would still be valuable: a compact temporal-noise spectroscopy package for diagnosing correlated quantum-device noise.
