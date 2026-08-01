#!/usr/bin/env python3
"""Integrity checks for the frozen Interface Theory record.

This validates repository consistency and regenerates the complete Gate 013
audit. It does not regenerate the missing candidate-level audits identified in
docs/EVIDENCE_INDEX.md.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(relative: str) -> dict:
    with (ROOT / relative).open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    json_files = list(ROOT.rglob("*.json"))
    require(json_files, "Expected JSON evidence artifacts.")
    for path in json_files:
        try:
            with path.open(encoding="utf-8") as handle:
                json.load(handle)
        except json.JSONDecodeError as error:
            raise AssertionError(
                f"Invalid JSON: {path.relative_to(ROOT)}: {error}"
            ) from error

    f0 = load("examples/F0_linear/factorization_check.json")
    aligned = next(
        interface for interface in f0["interfaces"]
        if interface["interface_id"] == "I_target_aligned_projection"
    )
    require(aligned["C"] == [[1, 0.81902]], "F0 target-aligned projection changed.")
    require(
        f0["minimality_check"]["result"]["minimum_dimension_found"] == 1,
        "F0 scalar target lower bound changed.",
    )
    hidden = next(
        interface for interface in f0["interfaces"]
        if interface["interface_id"] == "I_hidden_dimension"
    )
    require(
        hidden["counterexample"]["future_targets"] == {"L_A": 0.81902, "L_B": 1.81902},
        "F0 rollout values are inconsistent with e1^T A^5 = [1, 0.81902].",
    )

    legacy_dirs = (
        "examples/delay",
        "examples/hidden_state",
        "examples/stochastic",
        "examples/nonstationary",
    )
    for directory in legacy_dirs:
        for path in (ROOT / directory).rglob("*.json"):
            record = json.loads(path.read_text(encoding="utf-8"))
            require(
                record.get("canonical_status") == "INVALIDATED_LEGACY",
                f"Legacy file must be invalidated: {path.relative_to(ROOT)}",
            )
            require(
                "status" not in record and "interface_boundaries_verified" not in record,
                f"Legacy self-certification remains: {path.relative_to(ROOT)}",
            )

    summary_paths = (
        "experiments/results/gate_008_hidden_state_generalization/hidden_state_pairs.json",
        "experiments/results/gate_008_hidden_state_generalization/interface_search.json",
        "experiments/results/gate_009_delay_identifiability/lag_results.json",
        "experiments/results/gate_009_delay_identifiability/temporal_audit.json",
        "experiments/results/gate_010_stochastic_identifiability/confidence_results.json",
        "experiments/results/gate_010_stochastic_identifiability/repetition_curve.json",
        "experiments/results/gate_011_hd_composition/composition_search.json",
        "experiments/results/gate_012_nonstationary_identifiability/drift_counterexamples.json",
        "experiments/results/gate_012_nonstationary_identifiability/temporal_design_results.json",
    )
    for relative in summary_paths:
        record = load(relative)
        require(record.get("evidence_class") == "FROZEN_SUMMARY_RECORD", relative)
        require(
            record.get("reproducibility", {}).get("status") == "SUMMARY_RECORD_ONLY",
            relative,
        )

    stochastic = load(
        "experiments/results/gate_010_stochastic_identifiability/confidence_results.json"
    )
    require(stochastic.get("error_tolerance") == 0.05, "Incorrect stochastic tolerance.")
    require("confidence_threshold" not in stochastic, "Ambiguous confidence field remains.")

    ledger_text = (ROOT / "docs/RESULT_LEDGER.md").read_text(encoding="utf-8")
    evidence_text = (ROOT / "docs/EVIDENCE_INDEX.md").read_text(encoding="utf-8")
    expected_evidence_anchors = {
        "f0-nonlinear-baseline",
        "fh-hidden-state",
        "fd-delay",
        "fs-stochastic-readout-noise",
        "fhd-hidden-state--delay",
        "fn-known-linear-drift",
        "frs-reversible-network-selection",
    }
    referenced_evidence_anchors = set(
        re.findall(r"EVIDENCE_INDEX\.md#([a-z0-9-]+)", ledger_text)
    )
    require(
        referenced_evidence_anchors == expected_evidence_anchors,
        "Ledger evidence links changed without updating the seven-anchor contract.",
    )
    for anchor in expected_evidence_anchors:
        require(
            f'<a id="{anchor}"></a>' in evidence_text,
            f"Missing evidence anchor: {anchor}",
        )

    gate_013 = load(
        "experiments/results/gate_013_reversible_network_selection/factorization_audit.json"
    )
    require(gate_013["gate_id"] == "GATE-013", "Missing Gate 013 audit.")
    require(
        gate_013["identifiability_result"] == "IDENTIFIABLE_IN_DECLARED_FINITE_CLASS",
        "Gate 013 identifiability result changed.",
    )
    require(
        gate_013["minimum_scalar_readout_cost"] == 3
        and gate_013["all_lower_cost_interfaces_failed"],
        "Gate 013 minimum-interface certificate changed.",
    )
    audit_script = ROOT / "experiments/gate_013_reversible_network_selection/run_gate_013.py"
    generated = subprocess.run(
        [sys.executable, str(audit_script)],
        check=True,
        capture_output=True,
        text=True,
    )
    require(
        json.loads(generated.stdout) == gate_013,
        "Gate 013 committed audit does not match its deterministic generator.",
    )

    for relative, text in {
        "README.md": "L=\\widehat L\\circ O",
        "docs/CANONICAL_RECORD.md": "target-relevant experimental information",
        "docs/RESULT_LEDGER.md": "EVIDENCE_INDEX.md",
        "docs/EVIDENCE_INDEX.md": "FROZEN_SUMMARY_RECORD",
        "experiments/gate_registry.md": "Historical pruning gates",
    }.items():
        require(text in (ROOT / relative).read_text(encoding="utf-8"), relative)

    require(
        "Gate 013" in (ROOT / "experiments/gate_registry.md").read_text(encoding="utf-8"),
        "Gate 013 must remain in the registry.",
    )

    print(f"Validated {len(json_files)} JSON artifacts and canonical record invariants.")


if __name__ == "__main__":
    main()