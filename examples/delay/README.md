# delay — Temporal Interface Identifiability Example

## Overview

`delay` evaluates whether an interface can preserve target-relevant information when observations arrive after a temporal offset.

Unlike `hidden_state`, where information is unavailable because it is latent, `delay` studies systems where information exists but arrives too late for immediate use.

The core question:

\[
\boxed{
\text{Can a system act correctly when causal evidence is delayed?}
}
\]

---

# Motivation

Many real systems operate under delayed feedback:

- sensors have latency;
- environments reveal consequences after action;
- learning signals arrive after decisions;
- biological systems integrate delayed information;
- distributed systems synchronize asynchronously.

A system may have access to the correct information eventually, but still fail if the interface cannot compensate for the delay.

`delay` tests whether an interface preserves enough temporal structure for correct inference.

---

# System Model

The true state evolves:

\[
x_{t+1}=Ax_t
\]

The observer receives:

\[
y_t=x_{t-\tau}
\]

where:

- \(x_t\) = current system state;
- \(y_t\) = delayed observation;
- \(\tau\) = delay length.

The target depends on:

\[
L(x_t)
\]

The observer must infer the present from the past.

---

# Delay Boundary

A delayed interface creates a temporal information boundary:

True system:

t0 ---- t1 ---- t2 ---- t3 ---- t4
A B C D E

Observed stream (τ = 2):

          A      B      C      D      E
          ^
          arrives later

The information is not destroyed.

It is displaced.

---

# Factorization Criterion

An interface is sufficient when:

\[
\exists \widehat{L}: L=\widehat{L}\circ O
\]

Equivalent:

\[
O(x_a)=O(x_b)
\Rightarrow
L(x_a)=L(x_b)
\]

Failure occurs when delayed observations collapse states that require different current decisions.

---

# Example Failure

Two systems:

\[
x_a(t)=A
\]

\[
x_b(t)=B
\]

may produce identical delayed observations:

\[
y_t^a=y_t^b
\]

while:

\[
x_a(t)\neq x_b(t)
\]

Therefore:

\[
L(x_a)\neq L(x_b)
\]

The interface contains correct information, but not at the correct time.

---

# Interfaces

## 1. Instantaneous Delayed Observation

I_delayed_observation

Receives:

\[
y_t=x_{t-\tau}
\]

Properties:

- minimal bandwidth;
- no compensation;
- cannot directly identify current state.

Expected:

insufficient

for current-state targets.

---

## 2. Delay-Aware Interface

I_delay_compensated

Receives:

\[
(y_t,\tau)
\]

The observer knows how old the information is.

Can reconstruct:

\[
x_{t-\tau}
\]

but requires system dynamics to infer:

\[
x_t
\]

Expected:

conditionally sufficient

---

## 3. History Window Interface

I_history_window

Receives:

\[
(y_{t-k},...,y_t)
\]

History may compensate for delay by providing temporal context.

Expected:

sufficient when k >= τ

and dynamics are identifiable.

---

## 4. Predictive Model Interface

I_predictive_model

Receives:

- delayed observations;
- transition model;
- state estimator.

Uses:

\[
\hat{x}_t=A^\tau y_t
\]

Expected:

sufficient

when the model is correct.

---

# Benchmark Files

delay/
├── README.md
├── system.json
├── interfaces.json
├── targets.json
├── minimal_interface_search.json
├── factorization_check.json
├── counterexamples.json
└── traces/
├── delayed_signal_A.json
├── delayed_signal_B.json
├── observation_stream.json
└── temporal_equivalence_classes.json

---

# Relationship to Previous Examples

| Example | Core ambiguity |
|---|---|
| `F0_linear` | missing state dimensions |
| `hidden_state` | latent causal variables |
| `delay` | displaced temporal information |

`hidden_state` asks:

> Is the information hidden?

`delay` asks:

> Is the information arriving too late?

---

# Scientific Objective

`delay` measures the difference between:

\[
\text{information absence}
\]

and:

\[
\text{information latency}
\]

A system does not necessarily fail because it lacks information.

It may fail because its interface cannot transform delayed evidence into present-time action.

---

# Expected Findings

The benchmark should establish:

1. Delayed observation alone is insufficient for present-state targets.

2. Knowing the delay improves identifiability but does not always solve prediction.

3. Temporal history can recover lost alignment.

4. Predictive models can compensate for delay when the transition structure is known.

5. Interface quality depends on matching information arrival time with decision time.

---

# Role in Interface Theory

`delay` introduces the temporal dimension of causal accessibility.

It extends interface analysis from:

\[
\text{what information exists}
\]

to:

\[
\text{when information becomes available}
\]

---

# Final Statement

\[
\boxed{
\text{Information that arrives too late behaves like missing information unless the interface can compensate for time.}
}
\]

`delay` measures whether an interface preserves causal relevance across temporal boundaries.
