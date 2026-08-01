# Approximate Identifiability Theorem v0.1

**Status:** Interface Theory theorem  
**Parent theory:** Interface Theory v0.1  
**Depends on:** Factorization Criterion, Minimal Interface Theorem  
**Scope:** Approximate target recovery under imperfect interfaces

---

# 1. Purpose

Exact identifiability requires:

\[
L=\widehat L\circ O
\]

over the declared system class.

Real systems introduce:

- measurement noise,
- finite precision,
- stochastic observations,
- incomplete interventions,
- bounded model mismatch.

Approximate identifiability replaces exact equality with bounded target ambiguity.

The central question becomes:

> If two systems are indistinguishable up to interface error, how different can their targets be?

---

# 2. Definitions

## 2.1 Approximate Observation Equivalence

Let:

\[
O:F\rightarrow Y
\]

be an interface.

Let:

\[
d_Y
\]

be a metric over observation space.

Define:

\[
f_a\sim_O^\epsilon f_b
\]

when:

\[
\boxed{
d_Y(O(f_a),O(f_b))\leq\epsilon
}
\]

The interface cannot distinguish the systems beyond tolerance:

\[
\epsilon.
\]

---

## 2.2 Approximate Target Ambiguity

Let:

\[
L:F\rightarrow Z
\]

and:

\[
d_Z
\]

be a target-space metric.

Define:

\[
\boxed{
A_L(\epsilon,O,F)
=
\sup_{
f_a\sim_O^\epsilon f_b
}
d_Z(L(f_a),L(f_b))
}
\]

This is the maximum target uncertainty induced by the interface.

---

# 3. Exact Limit

Exact identifiability is recovered when:

\[
\epsilon=0
\]

and:

\[
A_L(0,O,F)=0
\]

because:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

---

# 4. Theorem Statement

Suppose:

\[
L=\widehat L\circ O
\]

and:

\[
\widehat L
\]

is Lipschitz continuous:

\[
d_Z(\widehat L(y_1),\widehat L(y_2))
\leq
K
d_Y(y_1,y_2)
\]

for constant:

\[
K\geq0.
\]

Then:

\[
\boxed{
A_L(\epsilon,O,F)
\leq
K\epsilon
}
\]

---

# 5. Proof

Take:

\[
f_a,f_b\in F
\]

such that:

\[
d_Y(O(f_a),O(f_b))\leq\epsilon
\]

Since:

\[
L=\widehat L\circ O
\]

we have:

\[
L(f_a)=\widehat L(O(f_a))
\]

and:

\[
L(f_b)=\widehat L(O(f_b))
\]

Therefore:

\[
d_Z(L(f_a),L(f_b))
=
d_Z(
\widehat L(O(f_a)),
\widehat L(O(f_b))
)
\]

By Lipschitz continuity:

\[
\leq
K d_Y(O(f_a),O(f_b))
\]

and:

\[
\leq K\epsilon
\]

Taking the supremum:

\[
\boxed{
A_L(\epsilon,O,F)\leq K\epsilon
}
\]

---

# 6. Linear Approximate Identifiability

Let:

\[
O(x)=Ax
\]

and:

\[
L(x)=Bx
\]

Suppose:

\[
B=\widehat BA
\]

with:

\[
\widehat B
\]

bounded:

\[
\|\widehat B\|\leq K
\]

Then:

\[
\boxed{
\|L(x_1)-L(x_2)\|
\leq
K
\|O(x_1)-O(x_2)\|
}
\]

---

# 7. Condition Number Bound

For linear reconstruction:

\[
O(x)=Ax
\]

suppose:

\[
A
\]

is invertible on the target-relevant subspace.

Then:

\[
\|\widehat x-x\|
\leq
\frac{\epsilon_O}
{\sigma_{\min}(A)}
\]

where:

\[
\sigma_{\min}(A)
\]

is the smallest singular value.

Thus:

\[
\boxed{
\text{identifiability depends on conditioning, not only rank}
}
\]

---

# 8. Interface Conditioning

Two interfaces may both satisfy:

\[
\ker(A)\subseteq\ker(B)
\]

yet have different practical performance.

Example:

Well-conditioned:

\[
\sigma_{\min}(A)=0.9
\]

Poorly conditioned:

\[
\sigma_{\min}(A)=0.001
\]

Both are theoretically identifiable.

Only the first is robust under noise.

---

# 9. Approximate Factorization

The practical objective becomes:

Find:

\[
\widehat L
\]

such that:

\[
\boxed{
d_Z(
L(f),
\widehat L(O(f))
)
\leq\eta
}
\]

for all:

\[
f\in F
\]

where:

\[
\eta
\]

is the approximation error.

---

# 10. Stochastic Extension

For stochastic observations:

\[
O(f)=P(Y|f)
\]

replace observation distance with distribution distance:

\[
d_{\mathcal P}
(
P(Y|f_a),
P(Y|f_b)
)
\]

Approximate identifiability requires:

\[
\boxed{
d_{\mathcal P}(O(f_a),O(f_b))
\leq\epsilon
\Rightarrow
d_Z(L(f_a),L(f_b))
\leq\eta
}
\]

---

# 11. Estimation Versus Identifiability

Approximate identifiability separates two questions:

## Structural question

Does a stable map exist?

\[
L\approx\widehat L\circ O
\]

---

## Statistical question

Can finite data estimate:

\[
\widehat L
\]

accurately?

---

Finite samples affect:

\[
\widehat L
\]

not:

\[
\text{existence of the mapping}
\]

---

# 12. Noise-Conditioned Sample Requirement

If observations satisfy:

\[
y=O(f)+\xi
\]

with noise variance:

\[
\sigma^2
\]

then repetition reduces estimation error:

\[
\epsilon_n
\propto
\frac{\sigma}{\sqrt n}
\]

and target uncertainty:

\[
\eta_n
\leq
K
\frac{\sigma}{\sqrt n}
\]

provided the interface remains identifiable.

---

# 13. Failure Modes

Approximate identifiability fails in three distinct ways.

---

## 13.1 Structural Non-Identifiability

\[
A_L(0,O,F)>0
\]

Even perfect measurements cannot recover the target.

---

## 13.2 Poor Conditioning

\[
A_L(0,O,F)=0
\]

but:

\[
K\rightarrow\infty
\]

Small measurement errors create large target uncertainty.

---

## 13.3 Finite Data Limitation

The interface is sufficient, but:

\[
n<n_{\mathrm{required}}
\]

for desired precision.

---

# 14. Consequence for Interface Search

Minimal interface cost is incomplete without stability.

The practical object becomes:

\[
\boxed{
I^*(L,F,\epsilon,\delta)
}
\]

where the interface must achieve:

- identifiability,
- bounded ambiguity,
- finite estimation cost.

---

# 15. Consequence for Adaptive Targets

For:

\[
L=C_{\mathrm{rev}}
\]

the correct progression is:

\[
\boxed{
\text{Can }C_{\mathrm{rev}}\text{ factor through an interface?}
}
\]

then:

\[
\boxed{
\text{How stable is that factorization under noise?}
}
\]

then:

\[
\boxed{
\text{Can finite data estimate it?}
}
\]

---

# 16. Scope

This theorem does not establish:

- a universal adaptive score;
- that approximate recovery is possible outside the declared class;
- that a stable interface exists;
- that the target is scientifically useful.

It establishes:

\[
\boxed{
\text{how identifiability degrades when interfaces are imperfect.}
}
\]

---

# End of Theorem
