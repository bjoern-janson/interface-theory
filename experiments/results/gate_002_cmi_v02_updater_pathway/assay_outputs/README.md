# Gate 002 — Assay Outputs

## Purpose

This directory contains the raw assay artifacts generated during:

**Gate 002 — CMI v0.2 Updater Pathway Sufficiency Test**

The purpose of these artifacts is to evaluate whether the declared updater-pathway interface preserves target-relevant distinctions.

These files are **interface evidence**, not estimator training data.

The gate question is:

\[
L=\widehat{L}\circ O_{CMI_{v0.2}} \; ?
\]

where:

- \(L\) is the declared future-adaptation target;
- \(O_{CMI_{v0.2}}\) is the frozen updater-pathway observation interface;
- \(\widehat{L}\) is a possible decoder from observations to target.

The gate succeeds only if all observational equivalence classes induced by the interface remain target-consistent.

---

# Directory Role

This folder records:

1. What the interface observes.
2. What the interface cannot distinguish.
3. Whether hidden target divergence remains after observation.
4. The boundary between identifiable and non-identifiable regimes.

The primary evidence structure is:

\[
\text{Observed interface}
\rightarrow
\text{Equivalence analysis}
\rightarrow
\text{Held-out target comparison}
\]

---

# Contents

## Core Assay Data

### `checkpoint_features.json`

Frozen updater-pathway features available before future continuation.

Contains:

- checkpoint observations;
- extracted pathway features;
- permitted interface variables;
- feature-freeze metadata.

These represent the complete information available to the candidate measurement.

---

### `replay_trajectories.json`

Replay traces generated under the allowed assay protocol.

Contains:

- replay conditions;
- observed pathway transitions;
- trajectory alignment;
- consistency checks.

Replay data is used only to characterize the interface.

---

### `updater_pathway_signatures.json`

Canonical representation of updater observations.

Used to define observational equivalence:

\[
O(A)=O(B)
\]

Two systems sharing a signature are treated as indistinguishable by the interface.

---

# Mimic Assays

## `mimic_assay/`

Contains adversarial constructions designed to test whether the interface captures target-relevant distinctions.

### `local_mimics.json`

Tests systems with superficial pathway similarity.

Question:

> Does the interface separate obvious updater differences?

---

### `strategic_mimics.json`

Tests systems designed to preserve measured features while changing future behavior.

Question:

> Can a system match observed updater signatures without matching future adaptation?

---

### `fragile_updater_mimic.json`

Primary failure witness.

Tests:

\[
O(A)=O(B)
\]

while:

\[
L(A)\neq L(B)
\]

A positive result here demonstrates interface insufficiency.

---

# Equivalence Analysis

## `equivalence_checks/`

Contains formal gate calculations.

### `observational_equivalence.json`

Records whether systems are identical under:

\[
O_{CMI_{v0.2}}
\]

---

### `target_divergence.json`

Records whether equivalent observations correspond to different future targets.

The decisive failure pattern is:

\[
O(A)=O(B)
\land
L(A)\neq L(B)
\]

which implies:

\[
L\neq\widehat L\circ O
\]

---

# Diagnostic Metrics

## `classifiers/`

Contains separability diagnostics.

These are not candidate estimators.

They answer:

> Does this interface contain enough information to distinguish known target classes?

They do not answer:

> Can we define a valid measurement of the target?

---

### `updater_feature_auc.json`

Reports classifier performance using updater-pathway features.

Interpretation:

- AUC above chance may indicate some distinctions are exposed.
- Chance-level performance indicates no accessible distinction.

---

### `held_out_prediction_metrics.json`

Reports prediction of future continuation outcomes.

Used only for the preregistered gate decision.

---

# Interpretation Rules

## Positive Result

A positive gate requires:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\]

for all systems in the declared class.

Meaning:

The target factors through the interface.

---

## Negative Result

A negative gate occurs when:

\[
\exists f_a,f_b:
O(f_a)=O(f_b)
\land
L(f_a)\neq L(f_b)
\]

Meaning:

The interface collapses target-relevant distinctions.

The correct response is:

- record the boundary;
- refine interface theory;
- do not tune an estimator.

---

# Scope

This assay does **not** establish:

- impossibility of measuring adaptive revision;
- impossibility of richer interfaces;
- validity of alternative targets;
- failure of updater-pathway analysis generally.

It establishes only:

> The frozen CMI v0.2 updater-pathway interface is insufficient for identifying the declared target within the tested system class.

---

# Gate Status

Result:

\[
\boxed{
\text{CMI v0.2 interface failed identifiability}
}
\]

Decision:

\[
\boxed{
\text{Estimator development blocked}
}
\]

Next permitted work:

\[
\text{interface theory}
\rightarrow
\text{new declared target}
\rightarrow
\text{new gate}
\]

No metric revision is authorized without a new identifiability argument.
