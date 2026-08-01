# Nonstationary Interface Identifiability Example

## Overview

This example evaluates whether an interface remains sufficient when the underlying system changes over time.

Previous benchmarks assume a stable generator:

P(x_{t+1}|x_t)=constant

The nonstationary benchmark removes this assumption.

The system evolves under changing dynamics:

x_{t+1}=f_t(x_t)+ε_t

and potentially changing observations:

y_t=h_t(x_t)+η_t

The central question is:

> Can an interface detect and adapt to changes in the causal structure of the environment?

---

## Motivation

A stationary interface may appear sufficient while the environment remains unchanged.

However, when the generating process shifts:

f_t != f_{t+k}

previously valid representations can become misleading.

The failure is not missing information.

The failure is that old information is no longer reliable under the new regime.

---

## Core Principle

A sufficient interface must preserve target-relevant distinctions across time.

For stationary systems:

P(L|x)=P_hat(L|O_I(x))

For nonstationary systems:

P(L_t|x_t, z_t)

P_hat(L_t|O_I(x_t), z_t)

where:

- `z_t` is the latent regime or environment state
- `f_t` is the active transition function
- `h_t` is the active observation function

---

## Failure Condition

A nonstationary interface fails when:

O_I(x_t)=O_I(x_{t+k})

but:

P(L_t|x_t) != P(L_{t+k}|x_{t+k})

Meaning:

The interface treats two situations as equivalent even though the environment requires different responses.

---

## Directory Structure

examples/nonstationary/

├── README.md
├── system.json
├── interfaces.json
├── targets.json
├── minimal_interface_search.json
├── factorization_check.json
├── counterexamples.json

└── traces/
├── regime_shift_A.json
├── regime_shift_B.json
├── observation_stream.json
└── temporal_equivalence_classes.json

---

## Benchmark Environment

The system contains:

### Latent state

x_t

The true internal state.

---

### Dynamic regime

z_t

A hidden variable controlling the active dynamics.

Example:

z_0 = stable_growth
z_1 = decay
z_2 = inversion

---

### Transition dynamics

x_{t+1}=f_{z_t}(x_t)+ε_t

Example regimes:

### Regime A: Growth

x_{t+1}=1.1x_t+ε_t

### Regime B: Stabilization

x_{t+1}=0.8x_t+ε_t

### Regime C: Inversion

x_{t+1}=-0.5x_t+ε_t

---

### Observation model

y_t=h_{z_t}(x_t)+η_t

The observation process may also drift.

---

# Candidate Interfaces

## I_observation

Raw current observation.

O_I(x_t)=y_t

Strength:

- minimal complexity

Failure:

- cannot determine whether the world changed

---

## I_history_window

Recent observation history.

O_I(x_t)=
(y_{t-k},...,y_t)

Strength:

- detects local patterns

Failure:

- long histories may contain obsolete information

---

## I_stationary_model

Fixed learned model.

P(x_{t+1}|x_t)

Strength:

- efficient under stable environments

Failure:

- assumptions become invalid after regime changes

---

## I_change_detector

Tracks evidence for distribution shifts.

O_I(x_t)=
P(z_t|y_{0:t})

Strength:

- identifies regime transitions

Failure:

- requires sufficient evidence

---

## I_adaptive_belief

Maintains uncertainty over both state and regime.

O_I(x_t)=
P(x_t,z_t|y_{0:t})

Strength:

- preserves uncertainty about changing structure

Expected behavior:

- strongest interface under nonstationarity

---

# Targets

The benchmark evaluates:

## State Estimation

Can the system estimate:

P(x_t|y_{0:t})

after environmental changes?

---

## Regime Identification

Can it infer:

P(z_t|y_{0:t})

?

---

## Future Prediction

Can it predict:

P(x_{t+k}|y_{0:t})

when the transition function may change?

---

## Adaptation Latency

How quickly does the interface recover after a regime shift?

Metric:

τ_adapt

where:

- low value = rapid adaptation
- high value = persistent outdated assumptions

---

# Counterexample Classes

## Hidden Regime Shift

Two observations appear identical:

y_A = y_B

but the active dynamics differ:

f_A != f_B

---

## Historical Contamination

Old data dominates:

P_old(L|O_I)

while the environment requires:

P_current(L|O_I)

---

## False Stability

The system assumes:

f_t=f_{t+1}

when:

f_t!=f_{t+1}

---

## Delayed Adaptation

The system detects change only after failure occurs.

---

# Relationship To Previous Examples

## Linear

Failure:

same representation
different target

Cause:

representation collapse.

---

## Hidden State

Failure:

important variables inaccessible

Cause:

state omission.

---

## Delay

Failure:

correct information at wrong time

Cause:

temporal misalignment.

---

## Stochastic

Failure:

same observation distribution
different target distribution

Cause:

uncertainty collapse.

---

## Nonstationary

Failure:

previously valid model
becomes invalid after change

Cause:

adaptation failure.

---

# Expected Results

The benchmark should demonstrate:

1. Stationary models perform well before shifts.

2. Performance collapses after unmodeled changes.

3. Short histories adapt faster but may be noisy.

4. Long histories provide stability but suffer from stale information.

5. Adaptive interfaces preserve regime uncertainty and recover faster.

---

# Validation Criteria

A successful run verifies:

- regime changes are generated correctly
- interfaces detect or fail to detect transitions
- adaptation latency is measurable
- stale assumptions produce identifiable failures
- minimal adaptive interfaces are discovered

---

# Interpretation

The nonstationary benchmark extends interface theory from:

> "Does the interface contain enough information?"

to:

> "Does the interface contain information that remains valid as the world changes?"

A sufficient adaptive interface must preserve not only state information, but information about when its own assumptions stop being valid.
