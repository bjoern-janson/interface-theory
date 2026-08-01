# Gate 001 — CMI Observation Sufficiency v0.1

**Status:** FAIL  
**Decision:** STOP_ESTIMATOR_BRANCH  
**Protocol:** CMI v0.1 Observation Sufficiency Test

---

## Question

Can the declared adaptive target be identified from the frozen CMI v0.1 behavioral interface?

The gate tested whether the observation interface preserved all target-relevant distinctions required for a future adaptation target.

Formally:

\[
A \sim_I B \Rightarrow L(A)=L(B)
\]

must hold for the interface to be sufficient.

---

## Frozen Interface

The tested interface allowed:

- behavioral traces;
- intervention responses;
- recurrence probes;
- counterfactual probes.

The following were excluded:

- updater pathway access;
- weights;
- gradients;
- private implementation state;
- development labels.

The interface was evaluated as a behavioral measurement interface only.

---

## Result

The matched adversarial pair produced:

\[
O_I(A)=O_I(B)
\]

while:

\[
L(A)\neq L(B)
\]

Therefore:

\[
A\sim_I B
\not\Rightarrow
L(A)=L(B)
\]

The target does not factor through the CMI v0.1 observation map.

---

## Probe Results

| Probe | Result | AUC |
|---|---|---:|
| Behavioral trace | Failed | 0.50 |
| Intervention response | Failed | 0.50 |
| Recurrence behavior | Failed | 0.50 |
| Counterfactual behavior | Failed | 0.50 |

Every permitted behavioral channel was non-identifying.

---

## Boundary Control

A separate controlled updater-pathway assay achieved:

\[
AUC=1.00
\]

However, this assay used information explicitly outside the CMI v0.1 interface.

Therefore it demonstrates only:

- the systems differ;
- the distinction exists;
- the behavioral interface does not expose it.

It does not validate an estimator.

---

## Interpretation

This result establishes:

\[
\boxed{
\text{CMI v0.1 behavioral observations are insufficient for universal target identification in the tested class.}
}
\]

It does **not** establish:

- that the adaptive target is impossible to measure;
- that internal access is required;
- that no richer behavioral interface can succeed;
- that the underlying construct is invalid.

The failure is interface-specific.

---

## Consequence

The estimator branch is closed.

The correct response is:

\[
\text{interface analysis}
\rightarrow
\text{new identifiability question}
\]

not:

\[
\text{failed estimator}
\rightarrow
\text{metric tuning}
\]

No CMI v0.2 or v0.3 repair is authorized by this gate.

---

## Research Lesson

The failure identified the governing constraint:

\[
\boxed{
\text{A measurement cannot recover distinctions removed by its observation interface.}
}
\]

Future work must first establish that a declared target factors through a declared interface before attempting estimation.

---

## Validation

- Tests passed: 26
- Protocol compliance: confirmed
- Estimator development: not authorized
