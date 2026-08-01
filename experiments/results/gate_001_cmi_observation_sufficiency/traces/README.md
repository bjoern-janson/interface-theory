# Gate 001 Trace Archive

## Purpose

This directory stores raw observation traces used in the CMI v0.1 observation sufficiency test.

The traces are evidence artifacts.

They are not estimators, scores, or target definitions.

---

## Trace hierarchy

The experiment compares two systems:

\[
A,\ B
\]

with:

\[
L(A)\neq L(B)
\]

while testing whether:

\[
O_I(A)=O_I(B)
\]

under the declared interface.

---

## Required trace contents

Each trace record contains:

```json
{
  "gate_id": "GATE-001",
  "system_id": "",
  "probe_type": "",
  "interface_version": "",
  "timestamp": "",
  "input": {},
  "observation": {},
  "metadata": {}
}
```
# Probe Categories

## Behavior

Passive and normal interaction trajectories.

**Question:**

> Can ordinary behavior expose the target distinction?

---

## Intervention

Controlled environmental or input perturbations.

**Question:**

> Does causal probing reveal the distinction?

---

## Recurrence

Repeated exposure and recovery behavior.

**Question:**

> Does temporal repetition reveal the distinction?

---

## Counterfactual

Alternative continuation branches.

**Question:**

> Does hypothetical variation reveal the distinction?

---

## Oracle Control

Privileged assay outside the declared interface.

**Purpose:**

> Confirm that the systems are genuinely different while maintaining the boundary that the tested interface cannot observe why.

---

# Interpretation Rule

The failure condition is:

```text
O_I(A) = O_I(B) ∧ L(A) ≠ L(B)
```

A trace match is therefore evidence of **interface insufficiency**, not evidence that the systems are identical.

---

# Immutability

Once generated:

- Traces are frozen.
- Derived metrics may reference them.
- Traces must not be modified to improve separability.
