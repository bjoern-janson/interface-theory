# hidden_state — Latent State Interface Identifiability Example

## Overview

`hidden_state` extends the `F0_linear` benchmark from direct state observation to systems where the target-relevant state is partially hidden behind an observation boundary.

The purpose is to test whether an interface can recover sufficient information about latent causal variables without directly observing the full system state.

The core question:

\[
\boxed{
\text{Can a system identify what matters when the relevant state is hidden?}
}
\]

---

# Motivation

`F0_linear` established:

\[
O(x_a)=O(x_b)
\Rightarrow
L(x_a)=L(x_b)
\]

as the requirement for interface sufficiency.

However, that benchmark assumes the hidden dimension is simply omitted.

Real systems are different:

- latent variables influence future observations;
- hidden structure can be inferred through dynamics;
- history may compensate for missing instantaneous access;
- interventions may reveal otherwise inaccessible variables.

`hidden_state` evaluates these cases.

---

# System Model

The true system state is:

\[
z_t=
\begin{bmatrix}
x_t\\
h_t
\end{bmatrix}
\]

where:

- \(x_t\) = observable component;
- \(h_t\) = hidden causal component.

The system evolves:

\[
z_{t+1}=Az_t
\]

The observer receives:

\[
y_t=O(z_t)
\]

The target depends on the full latent state:

\[
L(z_T)
\]

---

# Example Dynamics

Canonical system:

\[
A=
\begin{bmatrix}
1.0&0.5\\
0&0.95
\end{bmatrix}
\]

The hidden variable affects future observations:

\[
h_t \rightarrow x_{t+1}
\]

Therefore, two states can produce identical current observations while diverging later.

---

# Interface Question

The benchmark compares interfaces:

## 1. Instantaneous Observation

\[
O(z_t)=x_t
\]

The observer sees only the current visible state.

Expected:

insufficient

when multiple hidden states produce the same observation.

---

## 2. Temporal Observation

\[
O(z_t)=
(y_{t-k},...,y_t)
\]

The observer receives history.

Expected:

possibly sufficient

if hidden state leaves a recoverable signature in the trajectory.

---

## 3. Intervention Interface

The observer can apply controlled inputs:

\[
do(u_t)
\]

and observe the resulting response.

Expected:

stronger identifiability

because interventions can separate hidden causal states.

---

# Factorization Criterion

An interface is sufficient when:

\[
\exists \widehat L:
L=\widehat L\circ O
\]

Equivalent:

\[
O(z_a)=O(z_b)
\Rightarrow
L(z_a)=L(z_b)
\]

Failure occurs when:

\[
O(z_a)=O(z_b)
\]

but:

\[
L(z_a)\neq L(z_b)
\]

---

# Example Failure Mode

Two latent states:

\[
z_a=
\begin{bmatrix}
1\\
0
\end{bmatrix}
\]

\[
z_b=
\begin{bmatrix}
1\\
1
\end{bmatrix}
\]

Current observation:

\[
O(z_a)=O(z_b)=1
\]

but future trajectories differ:

\[
L(z_a)\neq L(z_b)
\]

The interface collapsed target-distinct causal states.

---

# Benchmark Files

hidden_state/
├── README.md
├── system.json
├── interfaces.json
├── targets.json
├── minimal_interface_search.json
├── factorization_check.json
├── counterexamples.json
└── traces/
├── hidden_state_A.json
├── hidden_state_B.json
├── observation_history.json
└── belief_equivalence_classes.json

---

# Relationship to F0_linear

| Property | F0_linear | hidden_state |
|---|---|---|
| Hidden variable | omitted coordinate | latent causal state |
| Observation | direct projection | partial measurement |
| Recovery | state access problem | inference problem |
| History | optional | potentially necessary |
| Intervention | not required | potentially required |

---

# Scientific Objective

`hidden_state` tests the boundary between:

\[
\text{unobserved}
\]

and:

\[
\text{unidentifiable}
\]

A hidden variable is not automatically inaccessible.

It becomes inaccessible only when the available interface fails to preserve a causal pathway from the hidden state to the target.

---

# Expected Findings

The benchmark should establish:

1. Instantaneous observations can fail even in deterministic systems.

2. Temporal interfaces can recover hidden variables when dynamics encode sufficient information.

3. Interventions can reduce ambiguity when passive observation cannot.

4. Interface sufficiency depends on the available causal channel, not direct visibility.

---

# Role in Interface Theory

`hidden_state` provides the transition from:

\[
\text{information preservation}
\]

to:

\[
\text{causal inference under limited access}
\]

It is the foundation for later benchmarks involving:

- stochastic latent systems;
- delayed observations;
- nonstationary hidden structure;
- adaptive interfaces.

---

# Final Statement

\[
\boxed{
\text{A variable does not need to be observed directly to be identifiable; it needs a preserved causal pathway to the target.}
}
\]

`hidden_state` measures whether an interface preserves that pathway.
