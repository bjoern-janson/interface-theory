#!/usr/bin/env python3
"""Integrity checks for the frozen Interface Theory record.

This validates repository consistency and regenerates the complete Gate 013
and Gate 014 audits. It does not regenerate the missing candidate-level audits
identified in docs/EVIDENCE_INDEX.md.
"""

from __future__ import annotations

import json
import hashlib
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
        "f014-cross-context-dynamic-factorization",
    }
    referenced_evidence_anchors = set(
        re.findall(r"EVIDENCE_INDEX\.md#([a-z0-9-]+)", ledger_text)
    )
    require(
        referenced_evidence_anchors == expected_evidence_anchors,
        "Ledger evidence links changed without updating the eight-anchor contract.",
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
        gate_013["minimum_protocol_scalar_readout_cost_in_frozen_ladder"] == 3
        and gate_013["minimum_informative_probe_cost_in_frozen_readout_set"] == 2
        and gate_013["all_evaluated_lower_protocol_cost_interfaces_in_frozen_ladder_failed"],
        "Gate 013 protocol/informative cost certificate changed.",
    )
    require(
        gate_013["target_relevant_projection"]["identifiable"]
        and not gate_013["target_relevant_projection"]["member_of_frozen_protocol_ladder"]
        and gate_013["target_relevant_projection"]["status"]
        == "DERIVED_COST_ACCOUNTING_ONLY",
        "Gate 013 informative projection scope changed.",
    )
    require(
        gate_013["constructive_factorization"]["map"] == "L_hat(1, r, k) = (r, k)"
        and gate_013["target"]["alias_formulas"]["reopenability"]
        == "1[selection_label = reversible]"
        and not gate_013["interface_policy"]["unrestricted_scalar_encodings_tested"],
        "Gate 013 constructive factorization or scope changed.",
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

    gate_014_path = ROOT / (
        "experiments/results/gate_014_dynamic_reopenability_flow/"
        "factorization_audit.json"
    )
    gate_014 = load(
        "experiments/results/gate_014_dynamic_reopenability_flow/"
        "factorization_audit.json"
    )
    require(gate_014["gate_id"] == "GATE-014", "Missing Gate 014 audit.")
    require(
        gate_014["execution_status"] == "EXECUTED"
        and gate_014["generator_validity"]["valid"],
        "Gate 014 generator validity changed.",
    )
    require(
        gate_014["scientific_decision"] == "PASS_NONTRIVIAL_QUOTIENT"
        and gate_014["decision_subtype"]
        == "PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY",
        "Gate 014 scoped factorization decision changed.",
    )
    require(
        gate_014["system_class"]["parameter_space_cardinality"] == 216
        and gate_014["system_class"]["dynamic_system_cardinality"] == 216
        and gate_014["interface_policy"]["interface_count"] == 64,
        "Gate 014 class or interface cardinality changed.",
    )
    require(
        gate_014["minimum_informative_probe_cost_in_frozen_vocabulary"] == 4
        and gate_014["minimum_protocol_probe_cost_with_mandatory_baseline"] == 5
        and gate_014["all_lower_probe_cost_interfaces_failed"]
        and gate_014["identifying_interface_count"] == 7,
        "Gate 014 probe-cost certificate changed.",
    )
    require(
        gate_014["assay_domains"]["disjoint"]
        and gate_014["assay_domains"]["identification_contexts"]
        == [[-1, 1], [0, 1]]
        and gate_014["assay_domains"]["target_contexts"] == [[1, 1]],
        "Gate 014 identification/target separation changed.",
    )

    expected_antichain = {
        frozenset(("K_BASE", "K_CONTEXT", "R_NEG", "R_ZERO")),
        frozenset(("K_BASE", "K_LAG", "R_NEG", "R_ZERO")),
        frozenset(("K_BASE", "K_NODE", "R_NEG", "R_ZERO")),
    }
    antichain = gate_014["minimum_identifying_antichain"]
    require(
        {frozenset(record["probes"]) for record in antichain}
        == expected_antichain,
        "Gate 014 minimum antichain changed.",
    )
    minimum_interface_ids = {record["interface_id"] for record in antichain}
    minimum_interfaces = {
        interface["interface_id"]: interface
        for interface in gate_014["interfaces"]
        if interface["interface_id"] in minimum_interface_ids
    }
    require(
        set(minimum_interfaces) == minimum_interface_ids,
        "Gate 014 minimum interfaces are missing from the complete audit.",
    )
    for record in antichain:
        quotient = record["quotient"]
        require(
            record["decision"] == "PASS_NONTRIVIAL_QUOTIENT"
            and record["decision_subtype"]
            == "PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY"
            and quotient["class_count"] == 54
            and quotient["singleton_class_count"] == 0
            and quotient["collision_class_count"] == 54
            and quotient["systems_in_collision_classes"] == 216
            and quotient["pairwise_collision_count"] == 324
            and quotient["heterogeneous_class_count"] == 0,
            "Gate 014 quotient certificate changed.",
        )
        for quotient_class in minimum_interfaces[record["interface_id"]][
            "observation_classes"
        ]:
            architecture_configurations = {
                tuple(configuration)
                for configuration in quotient_class["architecture_configurations"]
            }
            latent_configurations = {
                json.dumps(configuration, sort_keys=True)
                for configuration in quotient_class["latent_configurations"]
            }
            require(
                quotient_class["architecture_configuration_count"]
                == len(architecture_configurations)
                and quotient_class["architecture_configuration_count"] > 1,
                "Gate 014 minimum quotient lost architecture diversity.",
            )
            require(
                quotient_class["latent_configuration_count"]
                == len(latent_configurations)
                and quotient_class["latent_configuration_count"] > 1,
                "Gate 014 minimum quotient lost latent-configuration diversity.",
            )
            require(
                quotient_class["internal_dynamics_signature_count"] > 1,
                "Gate 014 minimum quotient lost internal-dynamics diversity.",
            )

    targets_by_system = {
        record["system_id"]: json.dumps(record["target"], sort_keys=True)
        for record in gate_014["system_class"]["systems"]
    }
    expected_systems = set(targets_by_system)
    require(len(expected_systems) == 216, "Gate 014 system table is incomplete.")
    for interface in gate_014["interfaces"]:
        observed_systems: list[str] = []
        heterogeneous_classes = 0
        changing_pairs = 0
        for quotient_class in interface["observation_classes"]:
            members = quotient_class["systems"]
            observed_systems.extend(members)
            class_targets = {targets_by_system[system] for system in members}
            require(
                quotient_class["target_homogeneous"] == (len(class_targets) == 1),
                f"Gate 014 class homogeneity mismatch: {interface['interface_id']}",
            )
            if len(class_targets) > 1:
                heterogeneous_classes += 1
                changing_pairs += quotient_class["target_changing_pair_count"]
                require(
                    quotient_class["canonical_counterexample"] is not None,
                    "Gate 014 heterogeneous class lacks a preserved witness.",
                )
        require(
            len(observed_systems) == 216
            and set(observed_systems) == expected_systems
            and len(set(observed_systems)) == 216,
            f"Gate 014 quotient is not a partition: {interface['interface_id']}",
        )
        require(
            interface["quotient"]["heterogeneous_class_count"]
            == heterogeneous_classes
            and interface["quotient"]["target_changing_pair_count"]
            == changing_pairs
            and interface["identifiable"] == (heterogeneous_classes == 0),
            f"Gate 014 quotient summary mismatch: {interface['interface_id']}",
        )
        expected_decision = (
            "FAIL_COUNTEREXAMPLE"
            if heterogeneous_classes
            else (
                "PASS_INJECTIVE_INTERFACE"
                if interface["quotient"]["singleton_class_count"] == 216
                else "PASS_NONTRIVIAL_QUOTIENT"
            )
        )
        require(
            interface["decision"] == expected_decision,
            f"Gate 014 decision mismatch: {interface['interface_id']}",
        )

    gate_014_contract = ROOT / (
        "experiments/gate_014_dynamic_reopenability_flow/GATE_014_CONTRACT.md"
    )
    require(
        hashlib.sha256(gate_014_contract.read_bytes()).hexdigest()
        == gate_014["contract_sha256"],
        "Gate 014 contract hash changed.",
    )
    gate_014_script = ROOT / (
        "experiments/gate_014_dynamic_reopenability_flow/run_gate_014.py"
    )
    regenerated_014 = subprocess.run(
        [sys.executable, str(gate_014_script)],
        check=True,
        capture_output=True,
    )
    require(
        regenerated_014.stdout == gate_014_path.read_bytes(),
        "Gate 014 committed audit is not byte-identical to its frozen generator.",
    )
    require(
        b"\r\n" not in gate_014_path.read_bytes()
        and gate_014_path.read_bytes().endswith(b"\n")
        and not gate_014_path.read_bytes().endswith(b"\n\n"),
        "Gate 014 audit is not canonical LF JSON with one final newline.",
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
    require(
        "Gate 014" in (ROOT / "experiments/gate_registry.md").read_text(encoding="utf-8"),
        "Gate 014 must remain in the registry.",
    )

    print(f"Validated {len(json_files)} JSON artifacts and canonical record invariants.")


if __name__ == "__main__":
    main()

