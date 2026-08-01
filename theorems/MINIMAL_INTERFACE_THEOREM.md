# Minimal Interface Theorem v0.1

**Status:** Interface Theory theorem  
**Parent theory:** Interface Theory v0.1  
**Depends on:** Factorization Criterion Theorem  
**Scope:** Minimal sufficient interfaces within a declared interface family

---

# 1. Purpose

The Factorization Criterion establishes whether an interface is sufficient:

\[
L=\widehat L\circ O
\]

The Minimal Interface Theorem addresses the next question:

> Among allowed interfaces, what is the smallest information interface that preserves identifiability?

The object of interest is not a universal measurement, but the minimum causal-observational resource required for a declared target.

---

# 2. Definitions

## 2.1 Interface Family

Let:

\[
\mathfrak I
\]

be a declared set of admissible interfaces.

Each interface:

\[
I\in\mathfrak I
\]

induces an observation map:

\[
O_I:F\rightarrow Y_I
\]

---

## 2.2 Interface Ordering

Define:

\[
I_1\preceq I_2
\]

when \(I_2\) contains at least the information available through \(I_1\).

Equivalently, there exists a map:

\[
h:Y_{I_2}\rightarrow Y_{I_1}
\]

such that:

\[
O_{I_1}=h\circ O_{I_2}
\]

Therefore:

\[
I_2
\]

is a refinement of:

\[
I_1.
\]

---

## 2.3 Interface Cost

Let:

\[
C_I:\mathfrak I\rightarrow\mathbb R^+
\]

assign an experimental cost.

Possible components:

\[
C_I=
(
n_{\mathrm{probe}},
d_{\mathrm{readout}},
T_{\mathrm{window}},
n_{\mathrm{repeat}},
\epsilon,
\delta
)
\]

Cost is declared before interface search.

---

# 3. Minimal Sufficient Interface

An interface:

\[
I^*
\]

is minimal sufficient for target:

\[
L
\]

over system class:

\[
F
\]

if:

## Sufficiency

\[
\boxed{
L=\widehat L_{I^*}\circ O_{I^*}
}
\]

---

## Minimality

For every strict refinement reduction:

\[
J\prec I^*
\]

we have:

\[
\boxed{
L\neq\widehat L_J\circ O_J
}
\]

---

# 4. Theorem Statement

Given:

- system class \(F\),
- target \(L:F\rightarrow Z\),
- interface family \(\mathfrak I\),

the set of minimal sufficient interfaces is:

\[
\boxed{
\mathfrak I_{\min}(L,F)
=
\{
I\in\mathfrak I:
L\text{ identifiable under }I
\land
\nexists J\prec I:
L\text{ identifiable under }J
\}
}
\]

---

# 5. Existence Theorem

If:

1. \(\mathfrak I\) is finite, and
2. at least one interface satisfies:

\[
L=\widehat L_I\circ O_I
\]

then:

\[
\boxed{
\mathfrak I_{\min}(L,F)\neq\emptyset
}
\]

---

# Proof

Because:

\[
\mathfrak I
\]

is finite, consider the subset:

\[
S=
\{I\in\mathfrak I:
L=\widehat L_I\circ O_I
\}
\]

By assumption:

\[
S\neq\emptyset
\]

Every finite partially ordered set contains at least one minimal element.

Therefore:

\[
\exists I^*\in S
\]

such that no:

\[
J\prec I^*
\]

exists within:

\[
S.
\]

Hence:

\[
I^*\in\mathfrak I_{\min}(L,F)
\]

---

# 6. Interface Antichain Result

Minimal interfaces are not necessarily unique.

There may exist:

\[
I_1^*,I_2^*\in\mathfrak I_{\min}
\]

where:

\[
I_1^*\not\preceq I_2^*
\]

and:

\[
I_2^*\not\preceq I_1^*
\]

Therefore:

\[
\boxed{
\mathfrak I_{\min}(L,F)
}
\]

is generally an antichain.

---

# 7. Interpretation

A target may be identifiable through multiple independent causal routes.

Example:

Interface A:

\[
\text{many spatial probes}
\]

Interface B:

\[
\text{fewer probes + temporal observations}
\]

Both may preserve:

\[
L
\]

without either containing the other.

The correct scientific object is therefore not always:

\[
I^*
\]

but:

\[
\boxed{
\mathfrak I_{\min}(L,F)
}
\]

---

# 8. Linear Special Case

Let:

\[
O_I(x)=A_Ix
\]

and:

\[
L(x)=Bx
\]

Identifiability requires:

\[
\ker(A_I)\subseteq\ker(B)
\]

A minimal interface satisfies:

\[
\ker(A_I)\subseteq\ker(B)
\]

while for every lower-cost:

\[
J\prec I
\]

we have:

\[
\ker(A_J)\not\subseteq\ker(B)
\]

---

# 9. Lower Bound Interpretation

The minimum interface cost:

\[
C_I^*
\]

is:

\[
\boxed{
C_I^*(L,F)
=
\min_{I\in\mathfrak I}
C_I(I)
\quad
\text{s.t.}
\quad
L=\widehat L_I\circ O_I
}
\]

This is a target-relative causal access lower bound.

---

# 10. Spatial, Temporal, and Statistical Dimensions

Interface cost may decompose:

\[
C_I^*
=
(
C_{\mathrm{space}},
C_{\mathrm{time}},
C_{\mathrm{repeat}},
C_{\mathrm{precision}}
)
\]

Different system complications increase different components.

Examples:

| Obstruction | Resource Increase |
|---|---|
| Hidden state | probe/readout diversity |
| Delay | observation offset |
| Noise | repetitions |
| Nonstationarity | temporal design rank |

---

# 11. Target-Relative Nature

Minimality is always relative to:

\[
(F,L,\mathfrak I)
\]

Changing any component changes the result.

A stronger system class may require:

\[
I_2^*\succ I_1^*
\]

A weaker target may require:

\[
I_2^*\prec I_1^*
\]

Therefore:

\[
\boxed{
\text{There is no target-free minimal interface.}
}
\]

---

# 12. Consequence for Measurement Design

The correct order is:

\[
\boxed{
\text{Define target}
\rightarrow
\text{define class}
\rightarrow
\text{search interface}
\rightarrow
\text{prove minimal sufficiency}
\rightarrow
\text{construct estimator}
}
\]

Estimator design before this step risks measuring interface artifacts rather than the target.

---

# 13. Relation to Adaptive Revision

For:

\[
L=C_{\mathrm{rev}}
\]

the question becomes:

\[
\boxed{
\mathfrak I_{\min}(C_{\mathrm{rev}},F)
=?
}
\]

Only after this object exists can a measurement attempt claim to estimate revision capacity.

---

# 14. Scope Limits

This theorem does not establish:

- existence of a universal adaptive property;
- that minimal interfaces are computationally easy to find;
- that the minimum interface generalizes outside \(F\);
- that a minimal interface produces a useful estimator under finite data.

It establishes only:

\[
\boxed{
\text{the formal object of minimum information required for target identification.}
}
\]

---

# End of Theorem
