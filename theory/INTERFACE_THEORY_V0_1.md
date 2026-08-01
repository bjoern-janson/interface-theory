# Interface Theory v0.1

**Status:** Foundational theory document  
**Version:** 0.1  
**Scope:** Identifiability of declared targets under declared observation and intervention interfaces.

---

# Abstract

Interface Theory studies the conditions under which a property of a system can be identified from available observations and interventions.

The central claim is not that every system property is measurable, but that measurement requires an interface whose information structure preserves all distinctions relevant to the declared target.

Given:

- a system class \(F\),
- an interface \(O\),
- a target property \(L\),

the primary question is:

> Does the interface contain sufficient causal information to determine the target over the declared system class?

If yes, the target is identifiable under the interface. If no, no estimator, benchmark, or measurement procedure operating through that interface can universally recover the target.

Interface Theory therefore places identifiability before estimation.

---

# 1. Core Objects

## 1.1 System Class

A system class defines the set of admissible systems:

\[
F=\{f_1,f_2,\ldots\}
\]

The class determines what distinctions are possible.

Identifiability claims are always relative to a declared class.

A property may be identifiable over a restricted class and impossible over a broader one.

---

## 1.2 Target

A target is a declared property of systems:

\[
L:F\rightarrow Z
\]

Examples:

- future behavior,
- recovery capability,
- transfer performance,
- stability,
- adaptive revision properties.

The target is not assumed measurable.

Its identifiability must be established.

---

## 1.3 Interface

An interface defines what information about a system is available.

\[
O:F\rightarrow Y
\]

The interface may include:

- observations,
- interventions,
- temporal sampling,
- repeated trials,
- behavioral readouts.

The interface is part of the scientific claim.

There is no context-free measurement.

---

# 2. Identifiability

A target \(L\) is identifiable under interface \(O\) over \(F\) when:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

for all:

\[
f_a,f_b\in F.
\]

Equivalently:

Systems indistinguishable under the interface must be indistinguishable with respect to the target.

If there exist:

\[
O(f_a)=O(f_b)
\]

but:

\[
L(f_a)\neq L(f_b),
\]

then the target is not identifiable under that interface.

No estimator can repair this failure.

---

# 3. Factorization Criterion

The central organizing criterion is:

\[
L=\widehat{L}\circ O
\]

on the attainable observation set:

\[
O(F).
\]

A target is identifiable if and only if there exists a function:

\[
\widehat L
\]

that maps interface observations to the target.

The interface must preserve all target-relevant information.

In other words:

\[
\text{system}
\rightarrow
\text{interface}
\rightarrow
\text{target}
\]

must form a valid factorization.

---

# 4. Linear Form

For linear systems:

\[
O(x)=Ax
\]

and:

\[
L(x)=Bx,
\]

identifiability requires:

\[
\ker(A)\subseteq\ker(B).
\]

Any direction invisible to the interface must also be irrelevant to the target.

Failure occurs when:

\[
\exists v:
Av=0
\]

while:

\[
Bv\neq0.
\]

The interface hides a target-relevant degree of freedom.

---

# 5. Minimal Interfaces

An interface is sufficient when it identifies the target.

A minimal interface is a sufficient interface such that no strictly weaker interface remains sufficient.

Let:

\[
I_1\preceq I_2
\]

represent interface refinement.

Then:

\[
I^*
\]

is minimal when:

\[
L\text{ identifiable under }I^*
\]

and:

\[
\forall I\prec I^*,
\quad
L\text{ is not identifiable under }I.
\]

There may exist multiple incomparable minimal interfaces:

\[
\mathfrak I_{\min}(L,F)
=
\{I:
I\text{ sufficient and minimal}\}.
\]

The object of interest is therefore often an interface antichain, not a single measurement.

---

# 6. Interface Resources

Interface complexity is not a single quantity.

Different system properties require different causal resources.

Relevant dimensions include:

\[
C_I=
(
N_{\mathrm{probe}},
d_{\mathrm{readout}},
\mathcal T_I,
N_{\mathrm{repeat}},
\epsilon,
\delta
)
\]

where:

- \(N_{\mathrm{probe}}\): number of interventions,
- \(d_{\mathrm{readout}}\): observable dimensions,
- \(\mathcal T_I\): temporal design,
- \(N_{\mathrm{repeat}}\): repetition budget,
- \(\epsilon\): approximation tolerance,
- \(\delta\): confidence requirement.

---

# 7. Failure Modes

Different sources of ambiguity require different interface refinements.

## Spatial ambiguity

Different systems produce identical observations because probes do not expose relevant directions.

Required resource:

\[
\text{probe/readout expansion}
\]

---

## Temporal delay

The relevant consequence occurs after observation.

Required resource:

\[
\text{observation offset}
\]

---

## Statistical uncertainty

The target is identifiable in distribution but requires finite samples.

Required resource:

\[
\text{repetition budget}
\]

---

## Nonstationary evolution

The target changes over time.

Required resource:

\[
\text{temporal design rank}
\]

The interface must observe enough of the evolution law to determine the future target.

---

# 8. Approximate Identifiability

Exact identification may be impossible under realistic conditions.

Approximate identifiability asks whether remaining ambiguity can be bounded.

Let:

\[
A_L(I,F)
\]

represent the maximum target difference between systems indistinguishable under interface tolerance.

Exact identifiability:

\[
A_L(I,F)=0
\]

Approximate identifiability:

\[
A_L(I,F)\leq\eta.
\]

Noise and finite samples affect estimation accuracy, not necessarily the existence of a valid factorization.

---

# 9. Research Hierarchy

Interface Theory imposes a strict ordering:

\[
\boxed{
\text{Target declaration}
\rightarrow
\text{Interface identifiability}
\rightarrow
\text{Measurement}
\rightarrow
\text{Prediction}
\rightarrow
\text{Intervention}
}
\]

A later stage cannot repair failure at an earlier stage.

Examples:

- A better estimator cannot solve non-identifiability.
- A better benchmark cannot solve insufficient causal access.
- A better architecture cannot validate an undefined target.

---

# 10. Adaptive Intelligence Application

Adaptive intelligence provides one motivating application.

A candidate target such as:

\[
C_{\mathrm{rev}}
\]

should be treated as:

\[
L:F\rightarrow Z
\]

rather than a primitive quantity.

The correct sequence is:

1. Define the adaptive target.
2. Define the system class.
3. Determine whether the target is identifiable.
4. Find the minimal interface.
5. Construct measurements.
6. Test predictive and causal value.

Correctability is therefore not assumed to be measurable.

It must first survive interface analysis.

---

# 11. Current Research Question

The central question of Interface Theory is:

\[
\boxed{
\text{What is the minimal causal interface required to identify a declared property over a declared system class?}
}
\]

The answer is expected to depend on:

\[
(F,L,I)
\]

rather than existing as a universal measurement independent of context.

---

# 12. Scope Limitations

Interface Theory does not currently claim:

- a universal intelligence metric;
- a universal correctability metric;
- substrate-independent adaptive quantities;
- that every useful property is identifiable;
- that minimal interfaces are practical engineering solutions.

It provides a framework for determining when such claims are scientifically possible.

---

# Summary

The foundational principle is:

\[
\boxed{
\text{A property can only be measured through an interface that preserves the distinctions relevant to that property.}
}
\]

Measurement begins with identifiability.

Not the other way around.
