from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from protocol import (
    ACTIONS, BUDGET, DIAGNOSTIC_COST, FAULTS, REPAIR_COST,
    Diagnostic, Repair, Topology, probe, valid_repair,
)
from representation import RawHistory, g0, g1, make_history, select_diagnostic
from viability import viable_initial_actions


class Condition(str, Enum):
    G0 = "g0"
    G1 = "g1"


class ConformanceFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class EpisodeSpec:
    topology: Topology
    fault: int
    nuisance: int


@dataclass(frozen=True)
class EpisodeResult:
    condition: Condition
    topology: Topology
    fault: int
    nuisance: int
    raw_history: RawHistory
    retained_bit: int
    diagnostic: Diagnostic
    observation: int | None
    repair: Repair | None
    budget_remaining: int
    wrong_probe: bool
    repair_success: bool
    failure: str | None


EXPECTED_COUNTS = {
    "total_worlds": 8,
    "success_count_g0": 4,
    "success_count_g1": 8,
    "wrong_probe_count_g0": 4,
    "wrong_probe_count_g1": 0,
    "P_success_g0": 0.5,
    "P_success_g1": 1.0,
    "delta_P_success": 0.5,
}


def episode_specs() -> tuple[EpisodeSpec, ...]:
    return tuple(
        EpisodeSpec(topology, fault, nuisance)
        for topology in (Topology.A, Topology.B)
        for fault in FAULTS
        for nuisance in (0, 1)
    )


def _required_diagnostic(topology: Topology) -> Diagnostic:
    viable = viable_initial_actions(topology)
    if viable == frozenset({Diagnostic.QA}):
        return Diagnostic.QA
    if viable == frozenset({Diagnostic.QB}):
        return Diagnostic.QB
    raise ConformanceFailure("frozen viable initial-action structure changed")


def run_episode(
    condition: Condition,
    spec: EpisodeSpec,
    raw_history: RawHistory,
) -> EpisodeResult:
    if raw_history != make_history(spec.topology, spec.nuisance):
        raise ConformanceFailure("raw history does not match frozen episode spec")
    retained_bit = g0(raw_history) if condition is Condition.G0 else g1(raw_history)
    diagnostic = select_diagnostic(retained_bit)
    required = _required_diagnostic(spec.topology)
    wrong_probe = diagnostic is not required
    budget = BUDGET - DIAGNOSTIC_COST
    observation = probe(spec.topology, diagnostic, spec.fault)

    if observation is None:
        return EpisodeResult(
            condition, spec.topology, spec.fault, spec.nuisance, raw_history,
            retained_bit, diagnostic, None, None, budget, wrong_probe, False,
            "NO_BOUNDED_ZERO_ERROR_CONTINUATION",
        )

    repair = Repair.R0 if observation == 0 else Repair.R1
    if budget < REPAIR_COST:
        raise ConformanceFailure("fault resolved but repair budget unavailable")
    budget -= REPAIR_COST
    success = valid_repair(spec.fault, repair)
    return EpisodeResult(
        condition, spec.topology, spec.fault, spec.nuisance, raw_history,
        retained_bit, diagnostic, observation, repair, budget, wrong_probe,
        success, None if success else "INVALID_REPAIR",
    )


def validate_contract() -> dict[str, object]:
    specs = episode_specs()
    viable_a = viable_initial_actions(Topology.A)
    viable_b = viable_initial_actions(Topology.B)
    collision = (
        viable_a == frozenset({Diagnostic.QA})
        and viable_b == frozenset({Diagnostic.QB})
        and viable_a.isdisjoint(viable_b)
    )
    if not collision:
        raise ConformanceFailure("viable initial-action collision changed")
    if len(specs) != 8:
        raise ConformanceFailure("episode family changed")
    if ACTIONS != (Diagnostic.QA, Diagnostic.QB, Repair.R0, Repair.R1, "stop"):
        raise ConformanceFailure("primitive action vocabulary changed")
    if (BUDGET, DIAGNOSTIC_COST, REPAIR_COST) != (2, 1, 1):
        raise ConformanceFailure("resource contract changed")

    histories = tuple(
        make_history(topology, nuisance)
        for topology in (Topology.A, Topology.B)
        for nuisance in (0, 1)
    )
    g0_values = {g0(history) for history in histories}
    g1_values = {g1(history) for history in histories}
    capacity_matched = g0_values == g1_values == {0, 1}
    if not capacity_matched:
        raise ConformanceFailure("one-bit representation capacity changed")

    g1_always_selects_viable = all(
        select_diagnostic(g1(make_history(topology, nuisance)))
        is _required_diagnostic(topology)
        for topology in (Topology.A, Topology.B)
        for nuisance in (0, 1)
    )
    g0_collapses_matched_topology = all(
        g0(make_history(Topology.A, nuisance))
        == g0(make_history(Topology.B, nuisance))
        for nuisance in (0, 1)
    )
    selectability_structure = g1_always_selects_viable and g0_collapses_matched_topology
    if not selectability_structure:
        raise ConformanceFailure("controller-selectability structure changed")

    return {
        "positive_episode_count_per_condition": 8,
        "viable_policy_initial_action_collision_verified": True,
        "representation_capacity_matched": True,
        "controller_identity_matched": True,
        "primitive_actions_matched": True,
        "budget_matched": True,
        "controller_selectability_structure_verified": True,
    }


def _aggregate(results: tuple[EpisodeResult, ...]) -> dict[str, int | float]:
    successes = sum(result.repair_success for result in results)
    wrong_probes = sum(result.wrong_probe for result in results)
    return {
        "success_count": successes,
        "wrong_probe_count": wrong_probes,
        "P_success": successes / len(results),
    }


def run_conformance() -> dict[str, object]:
    paired_results = []
    for spec in episode_specs():
        shared_history = make_history(spec.topology, spec.nuisance)
        g0_result = run_episode(Condition.G0, spec, shared_history)
        g1_result = run_episode(Condition.G1, spec, shared_history)
        paired_results.append((g0_result, g1_result))

    g0_results = tuple(pair[0] for pair in paired_results)
    g1_results = tuple(pair[1] for pair in paired_results)
    raw_history_equal = all(
        left.raw_history is right.raw_history
        for left, right in paired_results
    )
    controller_selectability_effect = all(
        result.diagnostic is _required_diagnostic(result.topology)
        for result in g1_results
    ) and sum(
        result.diagnostic is _required_diagnostic(result.topology)
        for result in g0_results
    ) == 4

    g0_summary = _aggregate(g0_results)
    g1_summary = _aggregate(g1_results)
    observed = {
        "total_worlds": len(episode_specs()),
        "success_count_g0": g0_summary["success_count"],
        "success_count_g1": g1_summary["success_count"],
        "wrong_probe_count_g0": g0_summary["wrong_probe_count"],
        "wrong_probe_count_g1": g1_summary["wrong_probe_count"],
        "P_success_g0": g0_summary["P_success"],
        "P_success_g1": g1_summary["P_success"],
        "delta_P_success": g1_summary["P_success"] - g0_summary["P_success"],
    }
    if observed != EXPECTED_COUNTS:
        raise ConformanceFailure(
            f"implementation diverges from frozen analytic object: {observed!r}"
        )
    if not raw_history_equal:
        raise ConformanceFailure("conditions did not receive the same raw history object")
    if not controller_selectability_effect:
        raise ConformanceFailure("controller-selectability effect did not conform")

    contract = validate_contract()
    return {
        "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
        "implementation_state": "IMPLEMENTED",
        "execution_state": "EXECUTED_CONFORMANCE",
        "scientific_result": "ANALYTIC_OBJECT_REPRODUCED_BY_EXECUTABLE_CONFORMANCE",
        **observed,
        "viable_policy_initial_action_collision_verified": contract[
            "viable_policy_initial_action_collision_verified"
        ],
        "controller_selectability_effect_verified": True,
        "raw_history_equal_across_conditions": True,
        "representation_capacity_matched": contract["representation_capacity_matched"],
        "controller_identity_matched": contract["controller_identity_matched"],
        "primitive_actions_matched": contract["primitive_actions_matched"],
        "budget_matched": contract["budget_matched"],
    }
