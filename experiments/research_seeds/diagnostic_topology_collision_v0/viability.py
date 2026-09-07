from __future__ import annotations

from collections import defaultdict

from protocol import (
    ACTIONS, BUDGET, DIAGNOSTIC_COST, FAULTS, REPAIR_COST,
    Action, Diagnostic, Repair, Topology, probe, valid_repair,
)


def _groups_after_probe(topology: Topology, diagnostic: Diagnostic):
    grouped: dict[int | None, list[int]] = defaultdict(list)
    for fault in FAULTS:
        grouped[probe(topology, diagnostic, fault)].append(fault)
    return tuple(tuple(faults) for faults in grouped.values())


def _one_repair_handles_all(faults: tuple[int, ...]) -> bool:
    return any(
        all(valid_repair(fault, repair) for fault in faults)
        for repair in (Repair.R0, Repair.R1)
    )


def initial_action_supports_zero_error(topology: Topology, action: Action) -> bool:
    if isinstance(action, Diagnostic):
        remaining = BUDGET - DIAGNOSTIC_COST
        if remaining < REPAIR_COST:
            return False
        return all(_one_repair_handles_all(group) for group in _groups_after_probe(topology, action))
    if isinstance(action, Repair):
        return all(valid_repair(fault, action) for fault in FAULTS)
    if action == "stop":
        return False
    raise ValueError(f"unknown action: {action!r}")


def viable_initial_actions(topology: Topology) -> frozenset[Action]:
    return frozenset(
        action for action in ACTIONS
        if initial_action_supports_zero_error(topology, action)
    )
