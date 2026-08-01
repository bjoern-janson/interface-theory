#!/usr/bin/env python3
"""Exhaustive factorization audit for Gate 013.

Gate 013 is deliberately small. It tests whether a declared joint target for
reversible selection and observable authority propagation factors through a
declared behavioral intervention interface. It does not estimate a general
correctability variable, compare architectures, or open predictive validation.
The identifying readouts are exact operational projections of the target, so
the result is a reproducible interface-composition proof by construction.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class OperationalRecord:
    """One member of the two-label operational Cartesian product.

    This is not a simulated mechanism graph. The labels directly determine the
    declared target bits and are excluded from the allowed interface.
    """

    system_id: str
    selection_label: str  # delete | reversible
    topology_label: str  # independent | propagating


RECORDS = (
    OperationalRecord("delete_independent", "delete", "independent"),
    OperationalRecord("delete_propagating", "delete", "propagating"),
    OperationalRecord("reversible_independent", "reversible", "independent"),
    OperationalRecord("reversible_propagating", "reversible", "propagating"),
)


def target(system: OperationalRecord) -> tuple[int, int]:
    """Return (reopenability, authority_flow)."""

    return (
        int(system.selection_label == "reversible"),
        int(system.topology_label == "propagating"),
    )


def baseline_readout(_: System) -> int:
    """Current performance before the intervention sequence; equal by design."""

    return 1


def reversal_recovery_readout(system: OperationalRecord) -> int:
    """Post-suppression phase-B recovery after a reversal intervention."""

    return target(system)[0]


def downstream_flow_readout(system: OperationalRecord) -> int:
    """Effect at node 3 of do(evidence at node 1 = contradiction)."""

    return target(system)[1]


READOUTS: dict[str, Callable[[OperationalRecord], int]] = {
    "baseline": baseline_readout,
    "reversal_recovery": reversal_recovery_readout,
    "downstream_flow": downstream_flow_readout,
}


def observation(system: OperationalRecord, readouts: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(READOUTS[name](system) for name in readouts)


def audit_interface(readouts: tuple[str, ...]) -> dict:
    partitions: dict[tuple[int, ...], list[OperationalRecord]] = {}
    for system in RECORDS:
        partitions.setdefault(observation(system, readouts), []).append(system)

    witnesses = []
    for obs, systems in sorted(partitions.items()):
        for left, right in combinations(systems, 2):
            if target(left) != target(right):
                witnesses.append(
                    {
                        "observation": list(obs),
                        "system_a": left.system_id,
                        "system_b": right.system_id,
                        "target_a": list(target(left)),
                        "target_b": list(target(right)),
                    }
                )

    return {
        "readouts": list(readouts),
        "scalar_readout_cost": len(readouts),
        "identifiable": not witnesses,
        "observation_classes": [
            {
                "observation": list(obs),
                "systems": [system.system_id for system in systems],
                "targets": [list(target(system)) for system in systems],
            }
            for obs, systems in sorted(partitions.items())
        ],
        "counterexample_witnesses": witnesses,
    }


def run_audit() -> dict:
    # The finite ladder is frozen: passive baseline, each individual probe, and
    # the combined behavioral intervention interface. Policy flags, weights,
    # graph internals, and architecture labels are intentionally absent.
    ladder = (
        ("baseline",),
        ("baseline", "reversal_recovery"),
        ("baseline", "downstream_flow"),
        ("baseline", "reversal_recovery", "downstream_flow"),
    )
    results = [audit_interface(readouts) for readouts in ladder]
    informative_projection = audit_interface(
        ("reversal_recovery", "downstream_flow")
    )
    identifying = [record for record in results if record["identifiable"]]
    minimum_cost = min(record["scalar_readout_cost"] for record in identifying)
    minima = [
        record["readouts"]
        for record in identifying
        if record["scalar_readout_cost"] == minimum_cost
    ]

    return {
        "gate_id": "GATE-013",
        "protocol_version": "OPERATIONAL_REOPENABILITY_FLOW_v0.1",
        "execution_status": "EXECUTED",
        "identifiability_result": "IDENTIFIABLE_IN_DECLARED_FINITE_CLASS",
        "system_class": {
            "name": "F_RS",
            "members": [system.system_id for system in RECORDS],
            "assumptions": [
                "Four labeled operational records forming a two-by-two Cartesian product.",
                "No suppression, recurrence, authority redistribution, graph edge, propagation, or relearning dynamics are simulated.",
                "The labels directly determine the target bits and are excluded from the allowed interface.",
            ],
        },
        "target": {
            "name": "L_RS",
            "components": ["reopenability", "authority_flow"],
            "definition": "(R_reopen, K_flow) as declared in the Gate 013 contract.",
            "alias_formulas": {
                "reopenability": "1[selection_label = reversible]",
                "authority_flow": "1[topology_label = propagating]",
            },
        },
        "interface_policy": {
            "allowed_readouts": list(READOUTS),
            "projection_formulas": {
                "reversal_recovery": "O_R = R_reopen",
                "downstream_flow": "O_K = K_flow",
            },
            "frozen_ladder_requires_baseline_control": True,
            "unrestricted_scalar_encodings_tested": False,
            "excluded_access": [
                "selection-policy flag",
                "topology-policy flag",
                "authority weights",
                "edge list",
                "architecture label",
            ],
        },
        "interfaces": results,
        "target_relevant_projection": {
            **informative_projection,
            "status": "DERIVED_COST_ACCOUNTING_ONLY",
            "member_of_frozen_protocol_ladder": False,
        },
        "minimum_protocol_scalar_readout_cost_in_frozen_ladder": minimum_cost,
        "minimum_informative_probe_cost_in_frozen_readout_set": informative_projection[
            "scalar_readout_cost"
        ],
        "mandatory_protocol_controls": ["baseline"],
        "minimum_identifying_interfaces": minima,
        "all_evaluated_lower_protocol_cost_interfaces_in_frozen_ladder_failed": all(
            not record["identifiable"]
            for record in results
            if record["scalar_readout_cost"] < minimum_cost
        ),
        "constructive_factorization": {
            "map": "L_hat(1, r, k) = (r, k)",
            "scope": "Direct label and readout aliases establish operational interface composition by design; not discovery of an adaptive-system invariant.",
            "cost_scope": "The cost-two informative minimum is only over the two predeclared binary probe coordinates; unrestricted scalar encodings were not tested.",
        },
        "decision": "RECORD_GATE_1_ONLY; estimation, predictive validity, and mechanism claims remain closed.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        type=Path,
        help="Optional path for the complete deterministic audit JSON.",
    )
    args = parser.parse_args()
    result = run_audit()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()