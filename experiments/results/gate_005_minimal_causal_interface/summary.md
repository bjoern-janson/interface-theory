# Gate 005 — Minimal Causal Interface

## Status

**PASSED**

A minimal sufficient interface was identified within the declared interface family.

The result moves the program from:

\[
\text{Is the target identifiable?}
\]

to:

\[
\text{What is the smallest interface that makes the target identifiable?}
\]

---

# Gate Declaration

## Objective

Given:

- a declared system class \(F\);
- a declared target functional \(L\);
- an admissible interface family \(\mathfrak I\);

find:

\[
I^*
\in
\mathfrak I
\]

such that:

\[
L=\widehat L\circ O_{I^*}
\]

and no strictly smaller interface satisfies this condition.

---

# Formal Criterion

The target is identifiable through interface \(I\) when:

\[
O_I(f_a)=O_I(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

for all:

\[
f_a,f_b\in F.
\]

In the linear case:

\[
\ker(O_I)\subseteq\ker(L)
\]

or equivalently:

\[
L\in\operatorname{rowspan}(O_I).
\]

---

# Interface Search

## Search Space

The interface lattice varied:

- intervention choice;
- behavioral readout channels;
- temporal observation window.

Total candidates evaluated:

\[
150
\]

interfaces.

Each interface was tested by:

1. generating observational equivalence classes;
2. checking target purity;
3. verifying factorization existence.

---

# Result

A sufficient interface was found:

\[
\boxed{
I^*
=
\{e=-1\}
\times
\{r_1,r_2\}
}
\]

with scalar observation cost:

\[
\boxed{
C_I^*=2
}
\]

---

# Minimality

All lower-cost interfaces failed.

For every:

\[
I\prec I^*
\]

there exists:

\[
f_a,f_b\in F
\]

such that:

\[
O_I(f_a)=O_I(f_b)
\]

while:

\[
L(f_a)\neq L(f_b).
\]

Therefore:

\[
\boxed{
I^*
\text{ is minimal within the declared lattice.}
}
\]

---

# Rank Audit

The minimum interface satisfies:

\[
\operatorname{rank}(O_{I^*})
=
\operatorname{rank}(L\text{-relevant space})
\]

and contains no target-relevant null directions.

Equivalently:

\[
\ker(O_{I^*})
\subseteq
\ker(L).
\]

The interface spans the complete target-relevant subspace without requiring full system reconstruction.

---

# Important Distinction

The result does **not** show that:

\[
I^*
\]

is universally minimal.

It shows:

\[
\boxed{
\text{Within the declared class and interface family, this is the minimum sufficient interface.}
}
\]

A different:

- target;
- system class;
- interface family;

may produce a different minimum.

---

# Relationship to Previous Gates

## Gate 001 — Observation Sufficiency

Finding:

\[
\text{passive traces can erase target information}
\]

Established the need for interface design.

---

## Gate 002 — Updater Pathway

Finding:

\[
\text{mechanism-visible traces can still fail}
\]

Established that richer observations are not automatically sufficient.

---

## Gate 003 — Finite Interface Non-Identifiability

Formalized:

\[
L\neq\widehat L\circ O
\]

as the decisive obstruction.

---

## Gate 004 — Restricted Positive Identifiability

Established:

\[
\phi(T)\in\operatorname{rowspan}(X_{\mathcal T})
\]

as a constructive sufficient condition in restricted classes.

---

## Gate 005

Adds:

\[
\boxed{
\text{the smallest interface required for factorization}
}
\]

---

# Scientific Interpretation

The object being measured is not a scalar property extracted from arbitrary traces.

The primary object is:

\[
\boxed{
\mathfrak I_{\min}(L,F)
}
\]

the set of minimal interfaces through which a target becomes identifiable.

This shifts the research question from:

> "What metric measures the property?"

to:

> "What information must an experiment preserve for the property to exist as an observable quantity?"

---

# Consequence for Future Metrics

A future quantity such as:

\[
C_{\mathrm{rev}}
\]

must enter as a declared target:

\[
L=C_{\mathrm{rev}}
\]

not as an assumption.

The correct sequence remains:

\[
\boxed{
(F,L)
\rightarrow
\mathfrak I_{\min}
\rightarrow
\widehat L
\rightarrow
\text{prediction}
\rightarrow
\text{intervention}
}
\]

---

# Scope

## Established

Within:

- the frozen system class;
- the declared target;
- the finite interface lattice;

a minimum sufficient causal interface exists and was identified.

---

## Not Established

This does not establish:

- a universal causal interface;
- a universal intelligence metric;
- arbitrary adaptive system measurement;
- nonlinear global guarantees;
- noisy finite-sample guarantees.

---

# Final Gate Statement

\[
\boxed{
\text{Before measuring a property, identify the minimum interface through which that property can become observable.}
}
\]

Gate 005 establishes the first finite-class construction of that interface frontier.
