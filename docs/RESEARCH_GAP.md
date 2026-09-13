# Research gap — updated

## What is already established

Temporal memory in quantum dynamics is an established research area. Process-tensor / quantum-comb methods can characterize multitime processes, and experiments have demonstrated non-Markovian process characterization and control. There are also explicit criteria for distinguishing classical from quantum memory at the level of multitime process structure.

Therefore this repository does **not** claim to introduce the concept of quantum memory, non-Markovianity, process tensors, or history dependence.

## Narrow hypothesis worth testing

The narrower engineering/scientific question is whether a **low-cost history/echo protocol combined with adversarial held-out prediction** can act as a screening test before full process-tensor reconstruction.

```text
history/echo measurements
        -> fit nested classical memory models
        -> hold out longer/unseen histories
        -> measure predictive failure
        -> compare with constrained quantum environment models
```

A history-order statistic such as `A_H = 1/2 [R(AB) - R(BA)]` is explicitly treated as a diagnostic only. It is not a quantum-memory witness because classical hidden-state models can have noncommuting A/B updates and therefore produce order dependence too.

## Potential contribution

The project could become useful if it demonstrates a reproducible **predictive-complexity gap**: a compact quantum environment explains held-out multitime data while every tested classical hidden-state family requires substantially higher latent dimension/complexity or fails prediction.

Even then, the result must be stated relative to the tested model class. It would not imply that all classical explanations have been eliminated unless a rigorous completeness theorem is established.
