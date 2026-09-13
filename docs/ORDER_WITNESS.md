# Order/echo witness: what it can and cannot prove

## Question

For matched histories `AB` and `BA`, can the present probe retain an order-sensitive response after identical preparation?

Define `A_H = 1/2 [R(AB) - R(BA)]`.

A nonzero value is **not** a quantum-memory certificate. A classical hidden state with noncommuting update maps can also produce `A_H != 0`.

## Stronger control

The repository contains a vector hidden-state adversary whose classical hidden state is two-dimensional and whose `A` and `B` updates do not commute. This closes an important loophole in the original scalar colored-noise model.

## Quantum comparator

`dqnr.quantum_history` contains a minimal two-qubit system-environment model. The system receives noncommuting controls while the system and environment undergo coherent `X⊗X` coupling. The same `AB/BA/AA/BB` protocol is evaluated exactly and with finite-shot sampling.

This is a **comparator**, not evidence for an unexplained effect. Its purpose is to ask whether the proposed statistic is sensitive to genuine coherent system-environment memory and whether a classical adversary can reproduce the same observable family.

## Falsification rule

If the vector classical adversary can match the quantum comparator on the full pre-registered observable set, the order witness does not distinguish quantum memory. The correct result is that the witness is diagnostically useful but not quantum-specific.
