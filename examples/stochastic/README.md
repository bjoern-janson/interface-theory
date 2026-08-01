# Stochastic Interface Identifiability Example

## Overview

This example evaluates whether an interface preserves enough information to identify target properties when the underlying system contains stochastic dynamics and noisy observations.

Unlike deterministic examples where failure occurs because two states map to the same observation:

O(x_a) = O(x_b)

the stochastic case evaluates distributional ambiguity:

P(O | x_a) = P(O | x_b)

while

P(L | x_a) != P(L | x_b)

The central question is:

> Can an interface preserve target-relevant distinctions when observations are probabilistic rather than exact?

---

## System

The example uses a stochastic dynamical system:

x_{t+1} = f(x_t) + ε_t

with noisy observations:

y_t = h(x_t) + η_t

where:

- `x_t` is the latent system state
- `ε_t` is process noise
- `η_t` is observation noise
- `y_t` is the available interface signal

The observer does not access the true state directly.

---

## Purpose

This benchmark tests:

1. **Stochastic identifiability**

Can an interface distinguish states whose observation distributions overlap?

2. **Distribution preservation**

Does the interface retain information about the target distribution?

3. **Sampling requirements**

How many observations are required before the target becomes identifiable?

4. **Uncertainty calibration**

Does the interface represent uncertainty rather than collapsing ambiguous states?

---

## Core Formalism

An interface is sufficient for target `L` if:

P(L | x) = P(L | O_I(x))

or equivalently:

O_I(x_a) = O_I(x_b)
=>
P(L | x_a) = P(L | x_b)

For stochastic systems this becomes a distributional factorization requirement.

---

## Directory Structure

examples/stochastic/

├── README.md
├── system.json
├── interfaces.json
├── targets.json
├── minimal_interface_search.json
├── factorization_check.json
├── counterexamples.json

└── traces/
├── stochastic_process_A.json
├── stochastic_process_B.json
├── observation_stream.json
└── probabilistic_equivalence_classes.json

---

## Benchmark Environment

The canonical system contains:

### Latent state

x_t

The true internal state of the system.

### Transition noise

ε_t ~ N(0, σ_x)

Randomness introduced during state evolution.

### Observation noise

η_t ~ N(0, σ_y)

Randomness introduced during measurement.

### Observation interface

y_t = x_t + η_t

The observer receives noisy evidence rather than direct state access.

---

## Candidate Interfaces

The benchmark compares progressively richer interfaces:

### I_observation

Raw noisy observations only.

O(x_t)=y_t

Expected behavior:

- sufficient for low-noise targets
- fails under overlapping distributions

---

### I_history_window

Temporal observation history.

O(x_t)=
(y_{t-k},...,y_t)

Expected behavior:

- reduces uncertainty
- improves posterior estimation

---

### I_distribution_estimator

Observation history plus uncertainty modeling.

O(x_t)=
(P(x_t | y_{0:t}))

Expected behavior:

- preserves belief state
- supports probabilistic targets

---

### I_intervention

Active probing of the stochastic system.

O(x_t,u_t)

Expected behavior:

- improves causal identifiability
- separates correlated stochastic processes

---

## Counterexample Principle

A stochastic counterexample exists when:

P(O | x_A) ≈ P(O | x_B)

but

P(L | x_A) ≠ P(L | x_B)

Meaning:

Two latent processes appear identical through the interface while requiring different predictions.

---

## Relationship To Other Examples

### Linear Example

Failure:

same observation
different target

Cause:

representation collapse.

---

### Hidden State Example

Failure:

unobserved latent dimensions

Cause:

inaccessible state.

---

### Delay Example

Failure:

correct information at wrong time

Cause:

temporal misalignment.

---

### Stochastic Example

Failure:

overlapping observation distributions

Cause:

uncertainty collapse.

---

## Expected Results

The benchmark should demonstrate:

1. Raw observations are not always sufficient.

2. More samples can increase identifiability.

3. A belief representation can outperform point estimates.

4. Active interfaces can resolve uncertainty that passive observation cannot.

5. Minimal sufficient interfaces depend on the target and uncertainty structure.

---

## Validation Criteria

A successful run verifies:

- stochastic dynamics are generated correctly
- observation distributions are measured correctly
- equivalence classes are distribution-based
- target divergence is detected
- minimal interfaces are identified

---

## Interpretation

The stochastic benchmark extends interface theory from:

> "Can the observer see the state?"

to:

> "Does the observer retain enough uncertainty structure to make correct distinctions?"

The key boundary is not missing information alone.

It is whether the interface preserves the probability structure required by the target.
