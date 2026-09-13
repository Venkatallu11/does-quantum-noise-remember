# Research design

## Falsifiable question

Does a quantum-device error carry information about the **recent history of the device** that cannot be predicted from the present state, known drift, readout bias, and an explicitly modeled finite-memory environment?

## Three separations

### 1. State dependence vs history dependence
Re-prepare the same nominal quantum state after every history sequence. If the effect survives state re-preparation, it is not simply the current state's accumulated unitary error.

### 2. Device drift vs memory
Randomize the order of histories across time. Fit measured instrumental drift independently. A real history effect must predict held-out history blocks, not merely correlate with clock time.

### 3. Markov memory vs out-of-family memory
Fit finite-memory channels with increasing memory depth. The interesting result is not “depth 4 wins.” It is a stable held-out residual or information criterion gap after the model family is stress-tested.

## Proposed experimental matrix

`history × delay × basis × depth × reversal × re-preparation × backend`

Primary contrasts:

- same present state / different history
- forward circuit / inverse circuit
- short delay / long delay
- fresh preparation / reused preparation
- randomized compiling on / off

## Discovery criterion

A statistically significant history coefficient is **necessary but not sufficient**.

A candidate memory effect becomes interesting only when all are true:

1. replicated across independent runs,
2. survives held-out prediction,
3. survives measured drift and readout nuisance models,
4. survives a finite-memory quantum-channel baseline,
5. changes predictably under reversal or delay,
6. is reproduced under an independent measurement basis,
7. has a pre-registered analysis path.

Even then, the correct conclusion is **out-of-family memory under tested models**, not “new physics proven.”
