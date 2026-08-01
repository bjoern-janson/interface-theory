# Gate 006 — Nonlinear Target Identifiability

## Status

**FAILED (Interface Insufficiency Confirmed)**

The declared nonlinear interface does not identify the target over the declared nonlinear system class.

This result extends the factorization framework beyond linear rank conditions.

The failure is not:

- a failure of optimization;
- a failure of estimator capacity;
- proof that nonlinear targets are impossible.

It is a failure of the observation interface to preserve target-relevant distinctions.

---

# Gate Declaration

## Objective

Determine whether:

\[
L=\widehat L\circ O
\]

exists over a nonlinear system class:

\[
F_{NL}.
\]

Equivalently:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

for all:

\[
f_a,f_b\in F_{NL}.
\]

---

# Why Linear Rank Is Insufficient

Previous gates used linear conditions:

\[
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T})
\]

or:

\[
\ker(O)\subseteq\ker(L).
\]

These remain valid only for linear operators or locally linearized neighborhoods.

For general nonlinear classes, the correct criterion is:

\[
\boxed{
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
}
\]

The question is whether observation equivalence classes are target-pure.

---

# Result

The frozen nonlinear interface contains observationally equivalent systems with different target values.

A counterexample exists:

\[
O(f_A)=O(f_B)
\]

while:

\[
L(f_A)\neq L(f_B).
\]

Therefore:

\[
\boxed{
L\neq\widehat L\circ O
}
\]

over the declared nonlinear class.

---

# Counterexample Pattern

Two nonlinear systems:

\[
f_A,f_B
\]

produce identical interface observations:

\[
O(f_A)=O(f_B)
\]

but diverge under the target:

\[
L(f_A)=1.0
\]

\[
L(f_B)=0.0.
\]

The interface collapses a distinction that changes the target.

---

# Failure Modes Identified

## 1. Hidden nonlinear modes

Different mechanisms produce identical observed trajectories.

Failure:

\[
\text{same observation}
\neq
\text{same target}
\]

---

## 2. Local-global mismatch

Two systems may share local behavior:

\[
DO_{f_A}=DO_{f_B}
\]

while differing globally.

Local derivative information does not guarantee global identifiability.

---

## 3. Nonlinear temporal aliasing

Different evolution laws can agree over observed history:

\[
O_{0:T}(f_A)=O_{0:T}(f_B)
\]

while diverging at future time:

\[
L(f_A)\neq L(f_B).
\]

---

# Boundary Audit

The gate explicitly rejects four invalid conclusions.

---

## Invalid conclusion 1

> Linear rank sufficiency automatically extends to nonlinear systems.

Rejected.

Nonlinear equivalence classes can contain target-divergent systems even when local rank conditions appear adequate.

---

## Invalid conclusion 2

> Failure of one nonlinear interface proves nonlinear targets cannot be measured.

Rejected.

A richer interface may restore:

\[
L=\widehat L\circ O.
\]

---

## Invalid conclusion 3

> Local Jacobian sufficiency proves global identifiability.

Rejected.

Local tangent information does not capture all nonlinear behavior.

---

## Invalid conclusion 4

> Local Jacobian failure proves global impossibility.

Rejected.

Nonlocal observations may still separate systems.

---

# Relationship to Previous Gates

## Gate 001 — Observation Sufficiency

Established:

\[
\text{arbitrary traces may erase target information}
\]

---

## Gate 002 — Updater Pathway

Established:

\[
\text{visible update behavior may still be insufficient}
\]

---

## Gate 003 — Finite Interface Non-Identifiability

Formalized:

\[
L\neq\widehat L\circ O
\]

as the central obstruction.

---

## Gate 004 — Restricted Positive Identifiability

Established positive linear conditions:

\[
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T})
\]

---

## Gate 005 — Minimal Causal Interface

Established the search problem:

\[
\mathfrak I_{\min}(L,F)
\]

---

## Gate 006

Extends the program boundary:

\[
\boxed{
\text{Nonlinear systems require equivalence-class factorization, not only rank analysis.}
}
\]

---

# Scientific Consequence

The theory now has a unified criterion.

For any declared class:

\[
F
\]

interface:

\[
O
\]

and target:

\[
L,
\]

the question is:

\[
\boxed{
\text{Does the target factor through the interface?}
}
\]

If yes:

\[
L=\widehat L\circ O.
\]

If no:

\[
\exists f_a,f_b:
O(f_a)=O(f_b),
\quad
L(f_a)\neq L(f_b).
\]

---

# Scope

## Established

Within the declared nonlinear class:

- the tested interface is insufficient;
- nonlinear rank shortcuts are invalid;
- factorization remains the correct organizing criterion.

---

## Not Established

This does not establish:

- universal nonlinear non-identifiability;
- impossibility of nonlinear interface refinement;
- impossibility of approximate prediction;
- impossibility of causal intervention.

---

# Next Authorized Steps

The correct next experiments are:

1. **Nonlinear interface refinement**

Search:

\[
\mathfrak I_{\min}(L,F_{NL})
\]

---

2. **Approximate nonlinear factorization**

Measure:

\[
A_L(O)
\]

as bounded residual target ambiguity.

---

3. **Local-to-global conditions**

Determine when local observability extends to global identifiability.

---

# Final Gate Statement

\[
\boxed{
\text{In nonlinear systems, measurement is possible only when the interface makes observational equivalence imply target equivalence.}
}
\]

Gate 006 establishes the boundary: rank conditions explain linear observability, but factorization governs identifiability in general.
