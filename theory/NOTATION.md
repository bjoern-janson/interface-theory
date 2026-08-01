# Interface Theory Notation v0.1

**Status:** Foundational notation reference  
**Version:** 0.1  
**Parent document:** `INTERFACE_THEORY_V0_1.md`

---

# 1. Core Objects

The primary objects of Interface Theory are:

\[
(F,O,L)
\]

where:

| Symbol | Meaning |
|---|---|
| \(F\) | Declared system class |
| \(O\) | Observation / intervention interface |
| \(L\) | Declared target property |

The central question:

\[
\boxed{
\text{Does }L\text{ factor through }O\text{ on }F?
}
\]

---

# 2. System Class

\[
F
\]

The admissible system family.

Individual systems:

\[
f\in F
\]

A system may contain:

- internal state,
- transition rules,
- update mechanisms,
- stochastic variables,
- temporal dynamics.

The internal representation of \(f\) is not assumed observable.

---

# 3. Target Map

\[
L:F\rightarrow Z
\]

Maps systems to a target space.

Examples:

\[
L(f)=\text{future recovery}
\]

\[
L(f)=\text{adaptation reliability}
\]

\[
L(f)=\text{long-horizon viability}
\]

The target is declared before measurement design.

---

# 4. Observation Interface

General interface:

\[
O:F\rightarrow Y
\]

Observation output:

\[
y=O(f)
\]

where:

\[
y\in Y
\]

The interface may include:

\[
O=
(
O_{\mathrm{behavior}},
O_{\mathrm{intervention}},
O_{\mathrm{temporal}},
O_{\mathrm{repeat}}
)
\]

---

# 5. Intervention Notation

An intervention:

\[
do(i)
\]

where:

\[
i\in\mathcal I
\]

is an allowed perturbation.

The resulting observation:

\[
O(f,i)
\]

or:

\[
P(Y|do(i),f)
\]

for stochastic systems.

---

# 6. Observation Distribution

For stochastic interfaces:

\[
O(f)
\equiv
P_O(Y|f)
\]

Equality of observations means distributional equality:

\[
P_O(Y|f_a)
=
P_O(Y|f_b)
\]

not merely identical samples.

---

# 7. Interface Equivalence Relation

Defined by:

\[
f_a\sim_O f_b
\]

iff:

\[
O(f_a)=O(f_b)
\]

The interface equivalence class:

\[
[f]_O
\]

is:

\[
[f]_O=
\{g\in F:O(g)=O(f)\}
\]

---

# 8. Target Equivalence Relation

Defined by:

\[
f_a\sim_L f_b
\]

iff:

\[
L(f_a)=L(f_b)
\]

Target equivalence class:

\[
[f]_L
\]

---

# 9. Identifiability Condition

Primary criterion:

\[
\boxed{
f_a\sim_O f_b
\Rightarrow
f_a\sim_L f_b
}
\]

Equivalent form:

\[
\boxed{
[f]_O\subseteq[f]_L
}
\]

---

# 10. Factorization

Identifiability is equivalent to:

\[
\boxed{
L=\widehat L\circ O
}
\]

where:

\[
\widehat L:O(F)\rightarrow Z
\]

maps observations to target values.

The factorization only needs to exist on:

\[
O(F)
\]

the attainable observation set.

---

# 11. Observation Space

\[
O(F)
\]

is the image of the system class:

\[
O(F)=
\{O(f):f\in F\}
\]

---

# 12. Linear Interface Form

Linear observation:

\[
O(x)=Ax
\]

Target:

\[
L(x)=Bx
\]

where:

\[
A:Y\leftarrow X
\]

is the observation operator.

---

# 13. Kernel Criterion

Linear identifiability:

\[
\boxed{
\ker(A)\subseteq\ker(B)
}
\]

Interpretation:

Invisible directions must be target irrelevant.

Failure:

\[
\exists v:
Av=0,\quad Bv\neq0
\]

---

# 14. Nonlinear Local Form

For differentiable systems:

Observation differential:

\[
DO_f
\]

Target differential:

\[
DL_f
\]

Local condition:

\[
\boxed{
\ker(DO_f)\subseteq\ker(DL_f)
}
\]

---

# 15. Interface Refinement

Interface ordering:

\[
I_1\preceq I_2
\]

means:

\[
I_2
\]

contains at least the information available in:

\[
I_1.
\]

Examples:

\[
\text{more probes}
\]

\[
\text{more readouts}
\]

\[
\text{longer temporal window}
\]

\[
\text{higher repetition count}
\]

---

# 16. Minimal Interface

Minimal interface:

\[
I^*
\]

satisfies:

\[
L\text{ identifiable under }I^*
\]

and:

\[
\forall I\prec I^*,
\quad
L\text{ not identifiable}.
\]

---

# 17. Minimal Interface Antichain

All minimal interfaces:

\[
\boxed{
\mathfrak I_{\min}(L,F)
}
\]

may contain multiple incomparable solutions:

\[
I_1^*\not\preceq I_2^*
\]

and:

\[
I_2^*\not\preceq I_1^*
\]

---

# 18. Interface Cost

General cost:

\[
C_I(I)
\]

Possible components:

\[
C_I=
(
n_p,
d_o,
T,
n_r,
\epsilon,
\delta
)
\]

where:

| Symbol | Meaning |
|-|-|
| \(n_p\) | number of probes |
| \(d_o\) | observed dimensions |
| \(T\) | temporal coverage |
| \(n_r\) | repetitions |
| \(\epsilon\) | error tolerance |
| \(\delta\) | confidence failure probability |

---

# 19. Temporal Interface

Temporal observation set:

\[
\mathcal T_I
=
\{t_1,\ldots,t_n\}
\]

Evolution model:

\[
\theta_t
=
X_t\beta
\]

Temporal design matrix:

\[
X_{\mathcal T}
\]

Target identifiability requires target-relevant components satisfy:

\[
\phi(T)
\in
\operatorname{rowspan}(X_{\mathcal T})
\]

---

# 20. Hidden Temporal Modes

A temporal design fails when:

\[
\exists g:
g(t_i)=0
\]

for all observed times, but:

\[
g(T)\neq0
\]

Such a mode creates:

\[
O(f_a)=O(f_b)
\]

while:

\[
L(f_a)\neq L(f_b)
\]

---

# 21. Approximate Equivalence

Observation tolerance:

\[
d_Y(O(f_a),O(f_b))\leq\epsilon
\]

defines:

\[
f_a\sim_O^\epsilon f_b
\]

Approximate target ambiguity:

\[
d_Z(L(f_a),L(f_b))
\leq\eta
\]

---

# 22. Stochastic Identifiability

Observation distributions:

\[
P_O(Y|f)
\]

Identifiability:

\[
P_O(Y|f_a)
=
P_O(Y|f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

---

# 23. Measurement Separation

The hierarchy:

\[
\boxed{
\text{Target}
\rightarrow
\text{Interface}
\rightarrow
\text{Identifiability}
\rightarrow
\text{Estimator}
\rightarrow
\text{Prediction}
\rightarrow
\text{Intervention}
}
\]

---

# 24. Causal Revision Target Notation

A proposed adaptive property:

\[
C_{\mathrm{rev}}
\]

is treated as a candidate target:

\[
C_{\mathrm{rev}}:F\rightarrow Z
\]

not as a primitive measurement.

The indexed form is:

\[
C_{\mathrm{rev}}^{F,I}
\]

meaning:

- system class dependent,
- interface dependent.

---

# 25. Canonical Question

Interface Theory asks:

\[
\boxed{
\text{Given }(F,O,L),
\text{ does there exist }
\widehat L
\text{ such that }
L=\widehat L\circ O?
}
\]

Everything downstream depends on this answer.

---

# End of Notation
