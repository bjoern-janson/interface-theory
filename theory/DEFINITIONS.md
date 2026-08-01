# Interface Theory Definitions v0.1

**Status:** Foundational definitions  
**Version:** 0.1  
**Parent document:** `INTERFACE_THEORY_V0_1.md`

---

# 1. System Class

A **system class** is the declared set of admissible systems:

\[
F
\]

where each element:

\[
f\in F
\]

represents a possible system consistent with the assumptions of the analysis.

A system class may specify:

- state structure,
- transition rules,
- observation model,
- intervention dynamics,
- stochastic assumptions,
- temporal evolution constraints.

All identifiability statements are relative to a declared \(F\).

---

# 2. Target

A **target** is a property assigned to each system:

\[
L:F\rightarrow Z
\]

where:

- \(F\) is the system class,
- \(Z\) is the target space.

Examples:

\[
L(f)=\text{future performance}
\]

\[
L(f)=\text{adaptation outcome}
\]

\[
L(f)=\text{revision reliability}
\]

A target is not assumed observable.

---

# 3. Observation Interface

An **observation interface** defines available information:

\[
O:F\rightarrow Y
\]

where:

- \(Y\) is the observation space.

The interface may include:

- passive observations,
- intervention responses,
- temporal traces,
- repeated measurements,
- behavioral outputs.

The interface is part of the experimental specification.

---

# 4. Intervention Interface

An **intervention interface** defines controlled system perturbations.

A general intervention interface is:

\[
I
\]

with induced observation mapping:

\[
O_I:F\rightarrow Y_I
\]

The interface includes both:

- what interventions are permitted,
- what resulting observations are available.

---

# 5. Attainable Observation Set

The attainable observation set is:

\[
O(F)=\{O(f):f\in F\}
\]

A target factorization only requires a mapping on this set:

\[
\widehat L:O(F)\rightarrow Z
\]

not necessarily on all possible observations.

---

# 6. Interface Equivalence

Two systems are equivalent under interface \(O\) when:

\[
f_a\sim_O f_b
\]

if and only if:

\[
O(f_a)=O(f_b)
\]

The interface partitions the system class into equivalence classes:

\[
[f]_O
\]

where:

\[
[f]_O=\{g\in F:O(g)=O(f)\}
\]

---

# 7. Target Equivalence

Two systems are equivalent with respect to target \(L\) when:

\[
f_a\sim_L f_b
\]

if:

\[
L(f_a)=L(f_b)
\]

The target partitions the system class into:

\[
[f]_L
\]

---

# 8. Identifiability

A target \(L\) is identifiable under interface \(O\) over \(F\) when:

\[
f_a\sim_O f_b
\Rightarrow
f_a\sim_L f_b
\]

Equivalently:

\[
[f]_O\subseteq[f]_L
\]

for every:

\[
f\in F.
\]

The interface-induced equivalence classes must refine the target equivalence classes.

---

# 9. Non-Identifiability

A target is non-identifiable under \(O\) if:

\[
\exists f_a,f_b\in F
\]

such that:

\[
O(f_a)=O(f_b)
\]

and:

\[
L(f_a)\neq L(f_b).
\]

Such a pair is an **observationally equivalent counterexample**.

---

# 10. Factorization

A target factors through an interface when:

\[
L=\widehat L\circ O
\]

for some:

\[
\widehat L:O(F)\rightarrow Z.
\]

Factorization exists if and only if the target is identifiable under the interface.

---

# 11. Linear Operators

For linear systems:

Observation:

\[
O(x)=Ax
\]

Target:

\[
L(x)=Bx
\]

where:

- \(A\) is the observation operator,
- \(B\) is the target operator.

---

# 12. Kernel Criterion

The linear identifiability condition is:

\[
\ker(A)\subseteq\ker(B)
\]

Meaning:

every system difference invisible to the interface must also be irrelevant to the target.

Failure occurs when:

\[
\exists v:
Av=0
\]

but:

\[
Bv\neq0.
\]

---

# 13. Local Nonlinear Identifiability

For differentiable nonlinear systems:

\[
O:F\rightarrow Y
\]

and:

\[
L:F\rightarrow Z
\]

local identifiability at \(f\) requires:

\[
\ker(DO_f)\subseteq\ker(DL_f)
\]

where:

- \(DO_f\) is the interface Jacobian,
- \(DL_f\) is the target Jacobian.

---

# 14. Minimal Interface

An interface \(I^*\) is minimal for target \(L\) over \(F\) when:

1. \(L\) is identifiable under \(I^*\);

and:

2. every strictly weaker interface fails:

\[
\forall I\prec I^*,
\quad
L\text{ is not identifiable under }I.
\]

---

# 15. Interface Refinement

Interface \(I_2\) refines interface \(I_1\):

\[
I_1\preceq I_2
\]

when \(I_2\) provides at least the information available from \(I_1\).

Examples:

Additional refinement may include:

- more probes,
- additional readouts,
- longer temporal coverage,
- increased repetition,
- higher precision.

---

# 16. Minimal Interface Set

A target may have multiple incomparable minimal interfaces.

The minimal interface set is:

\[
\mathfrak I_{\min}(L,F)
=
\{I:
I\text{ identifiable and no weaker interface is identifiable}\}
\]

This set is generally an antichain under refinement.

---

# 17. Interface Cost

An interface cost function:

\[
C_I(I)
\]

assigns a resource requirement.

Possible components:

\[
C_I=
(
N_{\mathrm{probe}},
d_{\mathrm{readout}},
T,
N_{\mathrm{repeat}},
\epsilon,
\delta
)
\]

Cost ordering is declared by the experiment.

A minimum-cost interface is:

\[
I^*
=
\arg\min_I C_I(I)
\]

subject to identifiability.

---

# 18. Approximate Identifiability

Under observation tolerance:

\[
d_Y(O(f_a),O(f_b))\leq\epsilon
\]

define approximate equivalence:

\[
f_a\sim_O^\epsilon f_b
\]

A target is approximately identifiable when:

\[
d_Z(L(f_a),L(f_b))\leq\eta
\]

for all approximately equivalent systems.

---

# 19. Stochastic Interface

For stochastic systems:

\[
O(f)
\]

is an induced observation distribution:

\[
P_O(\cdot|f)
\]

Identifiability becomes:

\[
P_O(\cdot|f_a)=P_O(\cdot|f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

Finite samples concern estimation of the factorized mapping, not existence of the mapping itself.

---

# 20. Temporal Interface

A temporal interface specifies observation times:

\[
\mathcal T_I=\{t_1,\ldots,t_n\}
\]

For evolving targets, temporal identifiability depends on whether these observations span the degrees of freedom governing target evolution.

For linear evolution:

\[
\theta_t=X_t\beta
\]

temporal identifiability requires target-relevant components of:

\[
\beta
\]

to lie in the span of the temporal design matrix.

---

# 21. Interface Ledger

For each system class \(F\) and target \(L\), record:

\[
(F,L,I,C_I,\text{result})
\]

where result is one of:

- identifiable,
- non-identifiable,
- approximately identifiable,
- unresolved.

---

# 22. Gate Declaration

Every experiment must specify:

\[
(F,O,L,\text{allowed refinements},\text{failure condition})
\]

before execution.

No estimator or mechanism evaluation proceeds without passing the identifiability gate.

---

# 23. Research Hierarchy

The fixed hierarchy is:

\[
\boxed{
\text{Factorization}
\rightarrow
\text{Estimation}
\rightarrow
\text{Prediction}
\rightarrow
\text{Intervention}
}
\]

Failure at an earlier stage cannot be repaired by a later stage.

---

# End State

Interface Theory studies the relationship:

\[
(F,I,L)
\]

and asks:

> What information structure is required for a declared property of a declared system class to become identifiable?
