# Factorization Criterion Theorem v0.1

**Status:** Foundational theorem  
**Parent theory:** Interface Theory v0.1  
**Scope:** General identifiability criterion

---

# 1. Statement

Let:

\[
F
\]

be a declared system class.

Let:

\[
O:F\rightarrow Y
\]

be an observation/interface map.

Let:

\[
L:F\rightarrow Z
\]

be a declared target.

Then the following statements are equivalent:

---

## (1) Target Identifiability

The target \(L\) is identifiable from the interface \(O\) over \(F\):

\[
\forall f_a,f_b\in F:
\]

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

---

## (2) Interface Equivalence Refines Target Equivalence

The observational equivalence relation is contained within the target equivalence relation:

\[
\boxed{
\sim_O\subseteq\sim_L
}
\]

Equivalently:

\[
[f]_O\subseteq[f]_L
\]

for all:

\[
f\in F
\]

---

## (3) Factorization Exists

There exists a function:

\[
\widehat L:O(F)\rightarrow Z
\]

such that:

\[
\boxed{
L=\widehat L\circ O
}
\]

or explicitly:

\[
\forall f\in F:
\]

\[
L(f)=\widehat L(O(f))
\]

---

# 2. Proof

## (1) implies (3)

Assume:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

Define:

\[
\widehat L(y)
\]

for:

\[
y\in O(F)
\]

by choosing any:

\[
f\in F
\]

such that:

\[
O(f)=y
\]

and setting:

\[
\widehat L(y)=L(f)
\]

This is well-defined because if:

\[
O(f_1)=O(f_2)
\]

then:

\[
L(f_1)=L(f_2)
\]

by identifiability.

Therefore:

\[
\widehat L(O(f))=L(f)
\]

and:

\[
L=\widehat L\circ O
\]

---

## (3) implies (1)

Assume:

\[
L=\widehat L\circ O
\]

Take:

\[
O(f_a)=O(f_b)
\]

Then:

\[
L(f_a)
=
\widehat L(O(f_a))
\]

and:

\[
L(f_b)
=
\widehat L(O(f_b))
\]

Since:

\[
O(f_a)=O(f_b)
\]

we obtain:

\[
L(f_a)=L(f_b)
\]

Therefore:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

---

Thus:

\[
\boxed{
\text{Identifiability}
\iff
\text{Factorization through the interface}
}
\]

---

# 3. Interpretation

The interface does not need to reveal the internal system.

It only needs to preserve every distinction relevant to the target.

The interface may discard information:

\[
F
\rightarrow
O(F)
\]

provided the discarded information is target-irrelevant.

The forbidden case is:

\[
\exists f_a,f_b:
\]

\[
O(f_a)=O(f_b)
\]

but:

\[
L(f_a)\neq L(f_b)
\]

because then the target cannot be recovered from observations.

---

# 4. Linear Special Case

Let:

\[
F=V
\]

be a vector space.

Let:

\[
O(x)=Ax
\]

and:

\[
L(x)=Bx
\]

where:

\[
A,B
\]

are linear operators.

The factorization condition becomes:

\[
B=\widehat B A
\]

for some linear map:

\[
\widehat B
\]

---

## Kernel Criterion

This is equivalent to:

\[
\boxed{
\ker(A)\subseteq\ker(B)
}
\]

---

## Proof

If:

\[
v\in\ker(A)
\]

then:

\[
Av=0
\]

and therefore:

\[
Bv=\widehat BAv
\]

so:

\[
Bv=0
\]

Hence:

\[
v\in\ker(B)
\]

Therefore:

\[
\ker(A)\subseteq\ker(B)
\]

---

Conversely, if:

\[
\ker(A)\subseteq\ker(B)
\]

then \(B\) is constant on every equivalence class induced by \(A\), allowing a map:

\[
\widehat B
\]

to exist on:

\[
A(F)
\]

such that:

\[
B=\widehat B A
\]

---

# 5. Nonlinear Local Form

For differentiable maps:

\[
O:F\rightarrow Y
\]

and:

\[
L:F\rightarrow Z
\]

a necessary local condition is:

\[
\boxed{
\ker(DO_f)
\subseteq
\ker(DL_f)
}
\]

for every:

\[
f\in F
\]

---

Interpretation:

Any infinitesimal system change invisible to the interface must also leave the target unchanged.

---

# 6. Stochastic Extension

For stochastic interfaces:

\[
O(f)
\equiv
P(Y|f)
\]

The criterion becomes:

\[
\boxed{
P(Y|f_a)=P(Y|f_b)
\Rightarrow
L(f_a)=L(f_b)
}
\]

The factorization is:

\[
L(f)=\widehat L(P(Y|f))
\]

---

Finite data affects estimation of:

\[
\widehat L
\]

but not the existence of the factorization itself.

Therefore:

\[
\boxed{
\text{identifiability precedes estimation}
}
\]

---

# 7. Approximate Factorization

Exact factorization may fail while approximate prediction remains possible.

Define:

\[
d_Y(O(f_a),O(f_b))
\leq\epsilon
\]

and:

\[
d_Z(L(f_a),L(f_b))
\leq\eta
\]

for all approximately equivalent systems.

Then:

\[
\boxed{
\epsilon\text{-equivalent observations imply }\eta\text{-bounded target ambiguity}
}
\]

---

# 8. Interface Refinement Consequence

Suppose:

\[
O_1\preceq O_2
\]

meaning \(O_2\) contains all information available to \(O_1\).

Then:

\[
L\text{ identifiable under }O_1
\Rightarrow
L\text{ identifiable under }O_2
\]

but:

\[
L\text{ identifiable under }O_2
\not\Rightarrow
L\text{ identifiable under }O_1
\]

---

# 9. Minimal Interface Consequence

The search problem is:

\[
\min_I C_I(I)
\]

subject to:

\[
L=\widehat L_I\circ O_I
\]

The solution set:

\[
\boxed{
\mathfrak I_{\min}(L,F)
}
\]

is the minimal interface antichain.

---

# 10. Research Consequence

The theorem imposes the ordering:

\[
\boxed{
\text{interface}
\rightarrow
\text{identifiability}
\rightarrow
\text{measurement}
\rightarrow
\text{prediction}
\rightarrow
\text{intervention}
}
\]

A target cannot justify an estimator until it has been shown to factor through the declared interface.

---

# 11. Relation to Adaptive Revision Targets

A proposed adaptive property:

\[
C_{\mathrm{rev}}
\]

must enter as:

\[
L=C_{\mathrm{rev}}
\]

with declared:

\[
(F,O)
\]

The scientific question is:

\[
\boxed{
\exists\widehat C_{\mathrm{rev}}
:
C_{\mathrm{rev}}
=
\widehat C_{\mathrm{rev}}\circ O?
}
\]

If yes:

measurement may proceed.

If no:

the failure is an interface limitation, not an estimator weakness.

---

# 12. Scope

This theorem establishes an organizing criterion.

It does not by itself establish:

- a universal adaptive intelligence metric;
- a universal correctability quantity;
- a privileged behavioral interface;
- a mechanism of adaptation;
- predictive superiority over existing measures.

Those require additional theorems and experiments.

---

# End of Theorem
