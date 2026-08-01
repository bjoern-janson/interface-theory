#!/usr/bin/env python3
"""Exhaustive factorization audit for Gate 013.

Gate 013 is deliberately small. It tests whether a declared joint target for
reversible selection and observable authority propagation factors through a
declared behavioral intervention interface. It does not estimate a general
correctability variable, compare architectures, or open predictive validation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class System:
    """A finite authority-regulated three-mechanism system.

    The selection field determines whether a suppressed candidate is retained
    and can regain influence after a regime reversal. The topology field
    determines whether a contradiction at node 1 changes node 3's externally
    observed response. The policy flags are not in the allowed interface.
    """

    system_id: str
    selection: str  # delete | reversible
    topology: str  # independent | propagating


SYSTEMS = (
    System("delete_independent", "delete", "independent"),
    System("delete_propagating", "delete", "propagating"),
    System("reversible_independent", "reversible", "independent"),
    System("reversible_propagating", "reversible", "propagating"),
)


def target(system: System) -> tuple[int, int]:
    """Return (reopenability, authority_flow)."""

    return (
        int(system.selection == "reversible"),
        int(system.topology == "propagating"),
    )


def baseline_readout(_: System) -> int:
    """Current performance before the intervention sequence; equal by design."""

    return 1


def reversal_recovery_readout(system: System) -> int:
    """Held-out phase-B recovery after phase-A suppression and reversal."""

    return target(system)[0]


def downstream_flow_readout(system: System) -> int:
    """Effect at node 3 of do(evidence at node 1 = contradiction)."""

    return target(system)[1]


READOUTS: dict[str, Callable[[System], int]] = {
    "baseline": baseline_readout,
    "reversal_recovery": reversal_recovery_readout,
    "downstream_flow": downstream_flow_readout,
}


def observation(system: System, readouts: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(READOUTS[name](system) for name in readouts)


def audit_interface(readouts: tuple[str, ...]) -> dict:
    partitions: dict[tuple[int, ...], list[System]] = {}
    for system in SYSTEMS:
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
    identifying = [record for record in results if record["identifiable"]]
    minimum_cost = min(record["scalar_readout_cost"] for record in identifying)
    minima = [
        record["readouts"]
        for record in identifying
        if record["scalar_readout_cost"] == minimum_cost
    ]

    return {
        "gate_id": "GATE-013",
        "protocol_version": "REVERSIBLE_NETWORK_SELECTION_v0.1",
        "execution_status": "EXECUTED",
        "identifiability_result": "IDENTIFIABLE_IN_DECLARED_FINITE_CLASS",
        "system_class": {
            "name": "F_RS",
            "members": [system.system_id for system in SYSTEMS],
            "assumptions": [
                "Three candidate mechanisms with fixed directed dependency semantics.",
                "Deterministic phase-A suppression followed by a held-out phase-B regime reversal.",
                "No hidden state, noise, drift, rewiring, or learning beyond declared policies.",
            ],
        },
        "target": {
            "name": "L_RS",
            "components": ["reopenability", "authority_flow"],
            "definition": "(R_reopen, K_flow) as declared in the Gate 013 contract.",
        },
        "interface_policy": {
            "allowed_readouts": list(READOUTS),
            "excluded_access": [
                "selection-policy flag",
                "topology-policy flag",
                "authority weights",
                "edge list",
                "architecture label",
            ],
        },
        "interfaces": results,
        "minimum_scalar_readout_cost": minimum_cost,
        "minimum_identifying_interfaces": minima,
        "all_lower_cost_interfaces_failed": all(
            not record["identifiable"]
            for record in results
            if record["scalar_readout_cost"] < minimum_cost
        ),
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
