# F0_linear — Canonical Linear Interface Identifiability Example

## Overview

`F0_linear` is the foundational example for Interface Theory.

It defines the smallest nontrivial dynamical system where:

- hidden state exists;
- observations may discard information;
- targets depend on future evolution;
- factorization can be verified exactly.

The purpose is not to demonstrate advanced dynamics.

The purpose is to establish the core principle:

\[
\boxed{
\text{A target is identifiable only if the interface preserves every distinction the target requires.}
}
\]

---

# System Definition

The system evolves according to:

\[
x_{t+1}=Ax_t
\]

where:

\[
x_t\in\mathbb{R}^2
\]

and:

\[
A=
\begin{bmatrix}
1&0.2\\
0&0.9
\end{bmatrix}
\]

The observation interface is:

\[
y_t=Cx_t
\]

where \(C\) determines what information is accessible.

---

# Target

The benchmark target is:

\[
L_T(x_0)=x_5^{(1)}
\]

Meaning:

> Given an observation interface, can the system's future first state coordinate be determined?

The question is not whether the full internal state can be reconstructed.

The question is whether the target can be computed from available observations.

---

# Factorization Criterion

An interface \(O\) is sufficient when:

\[
\exists \widehat L:
L=\widehat L\circ O
\]

Equivalent test:

\[
O(x_a)=O(x_b)
\Rightarrow
L(x_a)=L(x_b)
\]

A failed interface produces:

\[
O(x_a)=O(x_b)
\]

but:

\[
L(x_a)\neq L(x_b)
\]

meaning the interface merged states that the target must distinguish.

---

# Included Interfaces

## 1. Full State Interface

\[
C=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]

Observation:

\[
O(x)=x
\]

Result:

factorization: verified
status: sufficient

Reason:

The complete state determines the future trajectory.

---

## 2. Position-Only Interface

\[
C=
\begin{bmatrix}
1&0
\end{bmatrix}
\]

Observation:

\[
O(x)=x_1
\]

Two states:

\[
x_a=
\begin{bmatrix}
1\\
0
\end{bmatrix}
\]

\[
x_b=
\begin{bmatrix}
1\\
1
\end{bmatrix}
\]

produce:

\[
O(x_a)=O(x_b)
\]

but evolve differently:

\[
L(x_a)\neq L(x_b)
\]

Result:

factorization: rejected
status: insufficient

---

## 3. Hidden-Dimension Interface

\[
C=
\begin{bmatrix}
0&1
\end{bmatrix}
\]

The interface observes only the second dimension.

The first dimension directly affects the target.

Result:

factorization: rejected
status: insufficient

---

# Counterexample Principle

Every failed interface has the same structure:

## Observation collision

\[
O(x_a)=O(x_b)
\]

## Target divergence

\[
L(x_a)\neq L(x_b)
\]

The collision demonstrates that information necessary for the target has been removed.

---

# Minimal Interface Search

The search evaluates candidate observation matrices.

Objective:

\[
\min C(O)
\]

subject to:

\[
L=\widehat L\circ O
\]

For this system:

minimum sufficient dimension: 2
minimum sufficient interface: full state

The result is specific to this target and dynamics.

A different target may require less information.

---

# Files

F0_linear/
├── README.md
├── system.json
├── interfaces.json
├── targets.json
├── factorization_check.json
├── counterexamples.json
├── minimal_interface_search.json
└── traces/
├── system_A.json
├── system_B.json
└── equivalence_classes.json

---

# Role in Interface Theory

`F0_linear` establishes the baseline before introducing:

- nonlinear dynamics;
- stochastic observations;
- hidden-state generalization;
- temporal delays;
- nonstationary systems;
- adaptive interfaces.

The progression is:

F0_linear
|
├── F1_nonlinear
|
├── F2_hidden_state
|
├── F3_stochastic
|
├── F4_delay
|
├── F5_nonstationary
|
└── F6_adaptive_interface

---

# Scientific Interpretation

The benchmark validates:

\[
\boxed{
\text{Computation cannot recover distinctions that the interface has eliminated.}
}
\]

The limiting factor is not solver power.

The limiting factor is whether the observation boundary preserves the information required by the target.

`F0_linear` is the smallest environment where that boundary can be measured exactly.
