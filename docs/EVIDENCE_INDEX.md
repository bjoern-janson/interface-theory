# Evidence Index

**Status:** provenance and reproducibility index for the frozen result ledger.

This file separates a frozen conclusion from a complete independently
reproducible audit. Every result below has a stable source **blob SHA** at the
time this index was created. A blob SHA identifies the exact source content; it
is not a substitute for a full candidate-level audit or an executable
generator.

## Evidence status vocabulary

- **FROZEN_SUMMARY_RECORD** — a scoped conclusion and its source artifact are
  retained, but the repository does not contain a complete raw audit table or
  generation script.
- **COMPLETE_REPRODUCIBLE_AUDIT** — a complete finite candidate audit and a deterministic generator are committed; the integrity check regenerates and compares the audit.
- **INVALIDATED_LEGACY** — a former design sketch has been replaced by a
  tombstone. It is non-evidential even if its Git history contains a passing
  or verified field.
- **SUPERSEDED_SUMMARY_ONLY** — a historical summary lacked adequate raw
  evidence or had outdated scope/count claims. It is retained only for
  navigation and negative history.

## Frozen result provenance

| Ledger row | Gate declaration / primary source | Source blob SHA | Evidence status and declared audit information |
|---|---|---|---|
| F0 nonlinear baseline | [source](../experiments/results/gate_007_minimal_interface_search/summary.md) | `5b59300492e4ffff8d4afc3b115e33a9f4b508f7` | **FROZEN_SUMMARY_RECORD.** Seven cost-two identifying candidates in the frozen record; complete candidate-level audit is not committed. Raw candidate table: not committed. Generator: not committed. |
| FH hidden state | [source](../experiments/results/gate_008_hidden_state_generalization/interface_search.json) | `62bc8d88fd8e650437ff7e65dfe0101248973b3d` | **FROZEN_SUMMARY_RECORD.** 50 candidates; 13 identifying; unique cost-three minimum. Summary record only. Raw candidate table: not committed. Generator: not committed. |
| FD delay | [source](../experiments/results/gate_009_delay_identifiability/temporal_audit.json) | `2e5e5ac054548925f4f7d6724f51adf36faa3e42` | **FROZEN_SUMMARY_RECORD.** 100 candidates; 26 identifying; lag-one cost-two minimum. Summary record only. Raw candidate table: not committed. Generator: not committed. |
| FS stochastic readout noise | [source](../experiments/results/gate_010_stochastic_identifiability/confidence_results.json) | `60accc59a9fb31554c11188deb0e7a3699ac6035` | **FROZEN_SUMMARY_RECORD.** 92 repetitions per scalar; 184 binary queries; maximum decoding error 0.046459. Summary record only. Raw candidate table: not committed. Generator: not committed. |
| FHD hidden state plus delay | [source](../experiments/results/gate_011_hd_composition/composition_search.json) | `da90ee5d7f68c6840e44e7925727917851733659` | **FROZEN_SUMMARY_RECORD.** 100 candidates; 13 identifying; unique cost-three minimum at lag one. Summary record only. Raw candidate table: not committed. Generator: not committed. |
| FN known linear drift | [source](../experiments/results/gate_012_nonstationary_identifiability/temporal_design_results.json) | `6f6217d44ec18785688c39cf3707c78a97f6f640` | **FROZEN_SUMMARY_RECORD.** 150 candidates; 26 identifying; seven minimum-cost candidates at scalar cost four. Summary record only. Raw candidate table: not committed. Generator: not committed. |
| FRS operational reopenability/flow composition | [audit](../experiments/results/gate_013_reversible_network_selection/factorization_audit.json) and [generator](../experiments/gate_013_reversible_network_selection/run_gate_013.py) | audit `6a86d4f7c4b2bd06f73c83e44f42d8814020e240`; generator `2759d15f1af37a0c60e22c875fb0f79e2ef4a77a` | **COMPLETE_REPRODUCIBLE_AUDIT.** Four labeled records and all four frozen protocol interfaces are enumerated. The validator regenerates the direct-alias audit. Protocol cost is three; derived informative cost is two only within the declared binary readout vocabulary. |

## Stable evidence anchors

<a id="f0-nonlinear-baseline"></a>
### F0 nonlinear baseline

Frozen ledger row for the closed deterministic nonlinear response class.

<a id="fh-hidden-state"></a>
### FH hidden state

Frozen ledger row for the fixed latent-state extension.

<a id="fd-delay"></a>
### FD delay

Frozen ledger row for the fixed known one-step-delay extension.

<a id="fs-stochastic-readout-noise"></a>
### FS stochastic readout noise

Frozen ledger row for known stationary binary readout noise.

<a id="fhd-hidden-state--delay"></a>
### FHD hidden state + delay

Frozen ledger row for the combined fixed latent-state and one-step-delay class.

<a id="fn-known-linear-drift"></a>
### FN known linear drift

Frozen ledger row for the closed known-linear-drift class.

<a id="frs-reversible-network-selection"></a>
### FRS reversible network selection

Complete reproducible finite-class audit for operational reopenability/flow
interface composition by direct label/readout aliases.

## Corrections and limitations

- The nonlinear \(F_0\) ledger result is distinct from the illustrative
  target-aligned scalar projection under
  [examples/F0_linear](../examples/F0_linear/README.md).
- The old Gate 005 and Gate 007 audit JSONs are
  **SUPERSEDED_SUMMARY_ONLY**; they do not support the former claims of one
  refinement-minimal interface or 38 total sufficient interfaces.
- The archived delay, hidden-state, stochastic, and nonstationary example JSON
  files are **INVALIDATED_LEGACY** tombstones. Their former self-certifying
  fields were removed.
- The GitHub Actions integrity workflow validates repository consistency and
  regenerates the Gate 013 complete audit. It does not regenerate the missing
  candidate-level audits for the earlier summary-only records.

## Required before independent replication claims

A future replication-quality update must add, for each remaining
summary-only frozen result:

1. the complete candidate table or equivalence-class audit;
2. the generating command or deterministic script;
3. a pinned source commit or release tag;
4. executable validation output linked from the source of record.

Until then, the ledger records scoped frozen conclusions, not fully
independently reproducible experiments.