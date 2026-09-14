# Literature audit — 2026-09-14

## Why the novelty claim must stay narrow

Quantum memory and non-Markovian dynamics are established subjects. Process-tensor tomography, quantum combs, and tensor-network approaches already provide general frameworks for multitime dynamics. The project therefore cannot claim novelty merely from asking whether quantum noise has memory.

## Current frontier relevant to this project

### 1. Quantum memory has explicit quantumity criteria

Bäcker, Beyer & Strunz, **Quantum memory precludes mixed-unitary dynamics**, Physical Review Research 8, 033288 (published 8 September 2026), connects quantum memory in non-Markovian dynamics to non-mixed-unitary structure and gives a hierarchy of semidefinite-program witnesses using process-tensor language. It also demonstrates detection with incomplete channel tomography.

https://journals.aps.org/prresearch/abstract/10.1103/dn6t-y9ky

This is a direct reason our curvature observable must not be presented as a replacement for established quantumity criteria.

### 2. Process tensors are now a mature practical language

Keeling, Stoudenmire, Bañuls & Reichman, **Process Tensor Approaches to Non-Markovian Quantum Dynamics**, Physical Review X 16, 020502 (2026), reviews process tensors and efficient tensor-network representations for structured non-Markovian dynamics.

https://journals.aps.org/prx/abstract/10.1103/1ncg-11hz

The project's value therefore has to be a low-cost *screening/spectroscopy layer* that can precede complete process reconstruction.

### 3. Quantum memory can be probed without full process tomography

Roy et al., **Semi-device-independent certification of quantum non-Markovianity using sequential random access codes**, Physical Review A 110, 012608 (2024), shows that sequential communication statistics can distinguish quantum-memory environments from Markovian and classical-memory processes under the protocol assumptions.

https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.012608

This suggests a future independent quantumity gate for our project.

### 4. Temporal nonclassicality is another route

Di Pietra et al., **Temporal Entanglement and Witnesses of Non-Classicality** (2025), develops a qubit-probe protocol in which temporal Bell-inequality violation can witness non-classicality under a general conservation-law assumption, with proof-of-principle NMR emulations.

https://arxiv.org/abs/2506.15474

Again, the implication for our project is architectural: use history/curvature to *find interesting regimes*, then use an independent temporal-nonclassicality witness.

### 5. Two-time temporal-correlation sensing is already emerging experimentally

A September 2026 Physical Review Letters paper, **Two-Tooth Bosonic Quantum Comb for Temporal-Correlation Sensing**, uses a two-tooth quantum comb as a temporal interferometer for environmental two-time correlations and studies nonmonotonic memory response versus delay.

https://journals.aps.org/prl/abstract/10.1103/6738-xcgc

This is particularly relevant to our delay-sweep direction. Our proposed temporal-memory geometry must therefore be distinguished by its adversarial model-selection and predictive-complexity component, not by temporal correlation sensing alone.

### 6. Classical explanations remain a hard boundary

Bäcker, Beyer & Strunz, **Local Disclosure of Quantum Memory in Non-Markovian Dynamics** (PRL 2024), explicitly frames the difficulty of deciding whether non-Markovian memory has a genuinely quantum origin or can be modeled classically.

https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.060402

This reinforces the project's adversarial classical ladder.

## What is still potentially interesting

The narrow hypothesis is:

> A low-cost closed-loop/history protocol may expose a predictive-complexity signature of temporal memory that can be used to select experiments and candidate regimes before invoking full process-tensor reconstruction or dedicated quantum-memory certification.

The proposed temporal-memory curvature is therefore an **instrument/analysis object**, not a claim that a new form of memory has been discovered.

## What would make the work genuinely strong

A compelling result would require all of the following:

1. The loop/curvature response is reproducible under blinded randomized history ordering.
2. The response has a stable weak-coupling expansion over a clearly identified perturbative range.
3. Higher-order coefficients contain information not already present in second-order curvature.
4. A progressively richer classical hidden-state family is evaluated on held-out histories and held-out loop compositions.
5. The effect survives nuisance controls and independent compilation/backend choices.
6. An independent quantumity witness becomes positive in the same regime.
7. Replication occurs in a second physical implementation or independently developed simulator.

Only this full chain would justify moving from “interesting temporal structure” toward a serious physics claim.
