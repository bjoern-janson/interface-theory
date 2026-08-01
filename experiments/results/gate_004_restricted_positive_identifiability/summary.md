# Gate 004 — Restricted Positive Identifiability

## Status

**PASSED**

Within the declared restricted evolution class, the target is identifiable from the declared interface.

This is the constructive counterpart to Gate 003.

Gate 003 established that:

\[
L\neq \widehat L\circ O
\]

for a finite interface that discarded target-relevant distinctions.

Gate 004 establishes that with a sufficiently matched interface:

\[
\boxed{
L=\widehat L\circ O
}
\]

can hold.

---

# Gate Declaration

## Gate

Test whether a declared future target can be recovered from a restricted interface over a known evolution family.

---

## Question

Does the observation operator preserve every direction relevant to the target?

The criterion is:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

or, in the linear setting:

\[
\ker(O)\subseteq\ker(L).
\]

---

## Failure Condition

The gate fails if there exists:

\[
\Delta f
\]

such that:

\[
O(\Delta f)=0
\]

but:

\[
L(\Delta f)\neq0.
\]

Such a direction is an unobserved target-relevant mode.

---

# Restricted System Class

The declared class is:

\[
F_{\mathrm{linear}}
\]

with evolution:

\[
\theta_t=\Phi(t)\alpha
\]

where:

- \(\alpha\) is the unknown coefficient vector;
- \(\Phi(t)\) is a known evolution basis.

The target is:

\[
L(\theta)=\phi(T)^T\alpha.
\]

Observations follow:

\[
Y=X_{\mathcal T}\alpha.
\]

---

# Identifiability Criterion

The target is identifiable when:

\[
\boxed{
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T})
}
\]

Equivalently:

\[
\boxed{
\ker(X_{\mathcal T})
\subseteq
\ker(\phi(T)^T)
}
\]

Meaning:

> Every evolution mode invisible to the interface must be irrelevant to the target.

---

# Result

The frozen interface satisfies the criterion.

The temporal design matrix is:

\[
X_{\mathcal T}
=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix}
\]

with:

\[
\operatorname{rank}(X_{\mathcal T})=2.
\]

The target vector satisfies:

\[
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T}).
\]

Therefore:

\[
\boxed{
L=\widehat L\circ O
}
\]

exists over the declared class.

---

# Example: Linear Drift Recovery

For:

\[
\theta_t=a+bt
\]

the target is:

\[
\theta_2=a+2b.
\]

Observing:

\[
\theta_0=a
\]

and:

\[
\theta_1=a+b
\]

allows recovery of:

\[
b=\theta_1-\theta_0
\]

and therefore:

\[
\theta_2
=
2\theta_1-\theta_0.
\]

The future target is identifiable without observing the future.

---

# Boundary Cases

## Failure: insufficient temporal rank

One observation:

\[
X=
\begin{bmatrix}
1&0
\end{bmatrix}
\]

cannot distinguish:

\[
(a,b)
\]

from:

\[
(a,b+\Delta).
\]

The hidden drift changes the future target.

Therefore:

\[
\phi(T)\notin\operatorname{rowspan}(X).
\]

---

## Failure: insufficient spatial observability

Even with enough time samples, an interface fails if it does not observe target-relevant components.

A hidden direction:

\[
\Delta\theta
\]

can satisfy:

\[
O(\Delta\theta)=0
\]

while:

\[
L(\Delta\theta)\neq0.
\]

---

# Important Refinement

Full system recovery is not required.

The condition is not:

\[
\operatorname{rank}(X)=\dim(\alpha).
\]

The condition is:

\[
\phi(T)\in\operatorname{rowspan}(X).
\]

A target may be identifiable even when the entire system is not.

This establishes the distinction:

\[
\boxed{
\text{parameter identifiability}
\neq
\text{target identifiability}
}
\]

---

# Relationship to Previous Gates

## Gate 001

Observation traces can collapse target-relevant distinctions.

Lesson:

\[
\text{arbitrary observation is insufficient}
\]

---

## Gate 002

Updater pathway signatures can remain insufficient.

Lesson:

\[
\text{visible mechanism traces do not guarantee target access}
\]

---

## Gate 003

Formalized the obstruction.

Lesson:

\[
\text{measurement requires factorization}
\]

---

## Gate 004

Provides the positive condition.

Lesson:

\[
\boxed{
\text{When the interface spans the target-relevant subspace, measurement becomes possible.}
}
\]

---

# Scientific Consequence

The program now has both sides of the theorem:

## Negative result

If:

\[
\exists f_a,f_b:
O(f_a)=O(f_b)
\land
L(f_a)\neq L(f_b)
\]

then measurement is impossible from that interface.

---

## Positive result

If:

\[
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T})
\]

then:

\[
L=\widehat L\circ O.
\]

---

# Scope

## Established

Within:

- known linear evolution families;
- noiseless observations;
- declared target functionals;
- declared interface operators.

---

## Not Established

This does not prove:

- nonlinear identifiability;
- unknown basis recovery;
- adversarial dynamics;
- stochastic finite-sample guarantees;
- open-ended adaptive systems.

---

# Gate Decision

\[
\boxed{
\text{PASSED}
}
\]

The interface is sufficient for the declared target in the declared class.

Authorized next steps:

1. derive explicit decoder \(\widehat L\);
2. introduce approximate/noisy observations;
3. measure interface complexity;
4. test minimal interface conditions.

---

# Final Statement

Gate 004 establishes the constructive principle:

\[
\boxed{
\text{A target is measurable exactly when the interface preserves every distinction that can change that target.}
}
\]

The problem is therefore not finding a better estimator first.

The problem is designing an interface through which the target can exist as an identifiable object.
