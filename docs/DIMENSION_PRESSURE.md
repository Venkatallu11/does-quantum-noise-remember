# Dimension-pressure experiment

## Question

Can a finite-dimensional **classical hidden-state process** reproduce the output of a coherent system-environment model across short histories and still predict longer, unseen histories?

This is deliberately adversarial. A history-order asymmetry by itself is not a quantum-memory witness because a classical hidden environment with noncommuting history updates can also generate `AB != BA`.

## Protocol

Target process: the two-qubit system/environment model in `dqnr.quantum_history`.

Training histories:

- all binary A/B strings of lengths 1, 2, 3, 4 (`30` histories)

Held-out test histories:

- all binary A/B strings of lengths 5, 6 (`96` histories)

Classical surrogate:

```text
x <- M_A x + a_A     for A
x <- M_B x + a_B     for B
p = sigmoid(b + w^T x)
```

The dimension `D` controls the number of latent classical degrees of freedom. We fit only on short histories and score prediction on longer histories that were never used in fitting.

## Results

| D | parameters | train MSE | test MSE | test MAE | test max error |
|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 8.05e-3 | 5.07e-2 | 0.195 | 0.445 |
| 2 | 15 | 1.68e-3 | 2.02e-2 | 0.108 | 0.456 |
| 3 | 28 | 5.91e-4 | 2.15e-1 | 0.388 | 0.920 |
| 4 | 45 | 7.79e-5 | 1.99e-1 | 0.332 | 0.960 |
| 6 | 91 | 3.61e-16 | 4.31e-2 | 0.156 | 0.686 |

These are exploratory fits with only two random optimizer starts per dimension. They are not publication-grade uncertainty estimates.

## Interpretation

The important observation is a separation between **interpolation** and **history extrapolation**. Increasing latent dimension can drive training error essentially to zero without guaranteeing accurate prediction of longer histories.

The D=2 model is currently the strongest short-model baseline in this sweep, but even it leaves substantial held-out error. D=6 nearly memorizes the training set and reduces, but does not eliminate, test error.

This does **not** establish quantum memory. A richer classical state, different parameterization, longer training histories, or a process-tensor construction may close the gap.

## Next falsification step

Repeat the sweep with:

1. training histories through length 5 and testing length 6-7;
2. multiple randomized train/test partitions rather than a fixed length split;
3. bounded/stable hidden-state maps to prevent pathological extrapolation;
4. delay, echo, and measurement-basis covariates;
5. an explicit quantum model fit with the same evaluation protocol;
6. model selection using held-out log likelihood and complexity penalties.

A claim of quantum memory becomes interesting only if increasingly expressive classical models fail on held-out multitime statistics while a physically constrained quantum environment predicts those statistics substantially better.
