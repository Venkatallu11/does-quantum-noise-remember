# Does Quantum Noise Remember?

**A falsifiable research program for detecting temporal memory in quantum noise without confusing it with ordinary drift, readout bias, calibration artifacts, or expressive classical hidden-state models.**

This repository does **not** assume quantum noise has memory and does **not** interpret a memory-like residual as new physics. The first objective is harder:

> Can a controlled experiment produce a statistically reproducible history-dependent residual that survives deliberately adversarial conventional models on held-out histories?

## Core question

We compare matched histories such as:

```text
RESET -> A -> B -> PROBE
RESET -> B -> A -> PROBE
```

and reversal/echo variants. The candidate order statistic is

```text
A_H = 1/2 [R(AB) - R(BA)]
```

with AA/BB controls, delays, causal breaks, state re-preparation, randomized ordering, and multiple measurement bases.

A nonzero `A_H` is **not** a quantum-memory certificate. Classical hidden-state systems can also have noncommuting updates and therefore show AB/BA asymmetry.

## Memory/adversary ladder

- **M0** stationary / Markov noise
- **M1** deterministic drift
- **M2** scalar colored / latent classical noise
- **M3** finite-memory channels
- **M4** vector hidden-state classical environments
- **M5** nonlinear history-dependent classical models
- **Q** explicit coherent system-environment model
- **Residual** behavior not predicted by the declared model family on held-out histories

A model moves upward only when lower classes fail on data they did not see during fitting.

## Current key finding

The raw history-order witness is **not quantum-specific**. An explicitly constructed two-dimensional classical hidden environment with noncommuting A/B updates also produces AB/BA asymmetry.

The more promising discriminator is **predictive complexity**: fit a classical hidden-state model on short histories, then test it on longer, completely unseen histories. A model that memorizes training histories but fails on unseen histories has not explained the underlying process.

See:

- `docs/RESEARCH_GAP.md`
- `docs/ORDER_WITNESS.md`
- `docs/DIMENSION_PRESSURE.md`
- `docs/PAPER_CLAIM.md`
- `docs/ROADMAP.md`

## Status

**Active research prototype.** The simulations establish methodology and falsification logic, not experimental discovery or evidence for nonstandard physics.

## License

MIT
