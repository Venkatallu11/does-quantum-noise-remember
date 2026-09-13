# Next experiment

## Objective

Move from an order witness to a genuine model-discrimination experiment.

### Stage A — classical dimension pressure

Fit vector hidden-state models with increasing latent dimension to short histories and predict longer held-out histories.

### Stage B — richer history splits

Do not only split by history length. Randomly hold out history strings so that the test set probes interpolation across unseen temporal compositions.

### Stage C — physical constraints

Constrain the hidden-state maps to stable dynamics and compare against unconstrained fits. This prevents a classical adversary from winning merely through pathological extrapolation.

### Stage D — quantum comparator

Fit/validate an explicit system + environment model with coherent interaction. Give it the same training and held-out histories. Penalize parameter count/complexity so that the comparison is predictive rather than descriptive.

### Stage E — device protocol

Translate the strongest synthetic discriminator into:

```text
state preparation
-> A/B history block
-> optional delay
-> optional reversal/echo
-> probe
-> multi-basis measurement
```

Then interleave histories randomly in wall-clock time to decouple history order from calibration drift.

## Kill conditions

Stop the quantum-memory interpretation if any sufficiently expressive, stable classical hidden-state model predicts the held-out data within experimental uncertainty without a material complexity disadvantage.

Also stop if the apparent gap disappears under randomized compilation, state re-preparation, time interleaving, delay controls, or independent hardware replication.
