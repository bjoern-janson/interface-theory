from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from mediation import (
    compare_signatures,
    control_select_diagnostic,
    treatment_select_diagnostic,
)
from protocol import (
    BUDGET,
    DIAGNOSTIC_COST,
    DIAGNOSTICS,
    NULL_PAIR,
    POSITIVE_MODELS,
    POSITIVE_PAIRS,
    REPAIR_COST,
    Diagnostic,
    LatentModel,
    MediationStatus,
    marginal_view,
    world_observation,
)


class Condition(str, Enum):
    C0 = "C0"
    C1 = "C1"


class ProtocolViolation(RuntimeError):
    pass


@dataclass(frozen=True)
class EpisodeResult:
    condition: str
    pair: tuple[str, str]
    true_model: str
    diagnostic: str
    observation: int | None
    resolved_model: str | None
    repair: str | None
    budget_remaining: int
    discriminating: bool
    repair_success: bool
    failure: str | None


def resolve_pair(
    pair: tuple[LatentModel, LatentModel],
    diagnostic: Diagnostic,
    observation: int,
) -> tuple[LatentModel, ...]:
    coordinate = 0 if diagnostic is Diagnostic.Q0 else 1
    return tuple(
        model for model in pair if model.signature[coordinate] == observation
    )


def run_episode(
    condition: Condition,
    pair: tuple[LatentModel, LatentModel],
    true_model: LatentModel,
) -> EpisodeResult:
    left, right = pair
    if true_model not in pair:
        raise ProtocolViolation("true model is not a member of the live pair")

    left_view = marginal_view(left)
    right_view = marginal_view(right)
    if condition is Condition.C0:
        decision = control_select_diagnostic()
    else:
        decision = treatment_select_diagnostic(left_view, right_view)

    if decision is MediationStatus.OUT_OF_FROZEN_FAMILY:
        raise ProtocolViolation("live pair is outside the frozen V1 family")
    if decision is MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC:
        return EpisodeResult(
            condition.value,
            (left.key, right.key),
            true_model.key,
            decision.value,
            None,
            None,
            None,
            BUDGET,
            False,
            False,
            None,
        )

    budget = BUDGET - DIAGNOSTIC_COST
    observation = world_observation(true_model, decision)
    survivors = resolve_pair(pair, decision, observation)

    if len(survivors) != 1:
        return EpisodeResult(
            condition.value,
            (left.key, right.key),
            true_model.key,
            decision.value,
            observation,
            None,
            None,
            budget,
            False,
            False,
            "NO_BOUNDED_ZERO_ERROR_CONTINUATION",
        )

    resolved = survivors[0]
    if budget < REPAIR_COST:
        raise ProtocolViolation("resolved model but repair budget is unavailable")
    budget -= REPAIR_COST
    return EpisodeResult(
        condition.value,
        (left.key, right.key),
        true_model.key,
        decision.value,
        observation,
        resolved.key,
        resolved.repair,
        budget,
        True,
        resolved is true_model,
        None,
    )


def positive_episode_specs() -> tuple[
    tuple[tuple[LatentModel, LatentModel], LatentModel], ...
]:
    return tuple(
        (pair, true_model)
        for pair in POSITIVE_PAIRS
        for true_model in pair
    )


def aggregate_results(results) -> dict[str, int | float]:
    results = tuple(results)
    count = len(results)
    if count == 0:
        raise ProtocolViolation("cannot aggregate an empty result set")
    discriminating = sum(result.discriminating for result in results)
    repaired = sum(result.repair_success for result in results)
    return {
        "episode_count": count,
        "discriminating_count": discriminating,
        "repair_success_count": repaired,
        "P_disc": discriminating / count,
        "P_repair": repaired / count,
    }


def _edge_diagnostic(
    pair: tuple[LatentModel, LatentModel],
) -> Diagnostic:
    left, right = pair
    disagreement = compare_signatures(left.signature, right.signature)
    if disagreement == (1, 0):
        return Diagnostic.Q0
    if disagreement == (0, 1):
        return Diagnostic.Q1
    raise ProtocolViolation("positive edge does not have exactly one disagreement")


def validate_contract() -> dict[str, object]:
    if len(POSITIVE_PAIRS) != 4:
        raise ProtocolViolation("positive pair count changed")
    if len(positive_episode_specs()) != 8:
        raise ProtocolViolation("positive episode count changed")

    incidence = {model.key: set() for model in POSITIVE_MODELS}
    for pair in POSITIVE_PAIRS:
        if sum(a != b for a, b in zip(pair[0].signature, pair[1].signature)) != 1:
            raise ProtocolViolation("positive edge must differ on exactly one coordinate")
        diagnostic = _edge_diagnostic(pair)
        incidence[pair[0].key].add(diagnostic)
        incidence[pair[1].key].add(diagnostic)

    endpoint_nonidentifiability = all(
        value == {Diagnostic.Q0, Diagnostic.Q1}
        for value in incidence.values()
    )
    if not endpoint_nonidentifiability:
        raise ProtocolViolation("an endpoint determines the useful diagnostic")

    no_universal_diagnostic = all(
        not all(
            pair[0].signature[index] != pair[1].signature[index]
            for pair in POSITIVE_PAIRS
        )
        for index in (0, 1)
    )
    if not no_universal_diagnostic:
        raise ProtocolViolation("a universal positive-family diagnostic exists")

    pair_order_invariance = all(
        treatment_select_diagnostic(pair[0].signature, pair[1].signature)
        == treatment_select_diagnostic(pair[1].signature, pair[0].signature)
        for pair in POSITIVE_PAIRS
    )
    if not pair_order_invariance:
        raise ProtocolViolation("pair order changes mediator output")

    excluded_diagonals = (
        ((0, 0), (1, 1)),
        ((0, 1), (1, 0)),
    )
    if not all(
        treatment_select_diagnostic(left, right)
        is MediationStatus.OUT_OF_FROZEN_FAMILY
        for left, right in excluded_diagonals
    ):
        raise ProtocolViolation("square diagonal contract changed")

    null_left, null_right = NULL_PAIR
    null_vector = compare_signatures(
        marginal_view(null_left), marginal_view(null_right)
    )
    null_output = treatment_select_diagnostic(
        marginal_view(null_left), marginal_view(null_right)
    )
    if null_vector != (0, 0):
        raise ProtocolViolation("null disagreement vector changed")
    if null_output is not MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC:
        raise ProtocolViolation("null mediator output changed")

    if len({model.repair for model in POSITIVE_MODELS}) != len(POSITIVE_MODELS):
        raise ProtocolViolation("positive repairs are not unique")
    if null_left.repair == null_right.repair:
        raise ProtocolViolation("null repairs must differ")
    if set(DIAGNOSTICS) != {Diagnostic.Q0, Diagnostic.Q1}:
        raise ProtocolViolation("diagnostic menu changed")
    if (BUDGET, DIAGNOSTIC_COST, REPAIR_COST) != (2, 1, 1):
        raise ProtocolViolation("resource contract changed")

    snapshots = tuple(model.signature for model in POSITIVE_MODELS)
    for pair in POSITIVE_PAIRS:
        treatment_select_diagnostic(pair[0].signature, pair[1].signature)
    read_only = snapshots == tuple(model.signature for model in POSITIVE_MODELS)
    if not read_only:
        raise ProtocolViolation("mediator modified a live alternative")

    mediator_ephemeral = (
        treatment_select_diagnostic.__closure__ is None
        and not treatment_select_diagnostic.__dict__
    )
    if not mediator_ephemeral:
        raise ProtocolViolation("mediator carries persistent function state")

    joint_comparison_only_in_c1 = (
        control_select_diagnostic.__code__.co_argcount == 0
        and treatment_select_diagnostic.__code__.co_argcount == 2
    )
    if not joint_comparison_only_in_c1:
        raise ProtocolViolation("selector dependency contract changed")

    marginal_information_matched = all(
        marginal_view(model) == model.signature
        for model in (*POSITIVE_MODELS, *NULL_PAIR)
    )
    if not marginal_information_matched:
        raise ProtocolViolation("marginal view contract changed")

    return {
        "positive_pair_count": 4,
        "positive_episode_count_per_condition": 8,
        "endpoint_nonidentifiability_verified": endpoint_nonidentifiability,
        "no_universal_diagnostic_verified": no_universal_diagnostic,
        "pair_order_invariance_verified": pair_order_invariance,
        "marginal_information_matched": marginal_information_matched,
        "joint_comparison_only_in_C1": joint_comparison_only_in_c1,
        "read_only_mediator_verified": read_only,
        "mediator_ephemeral_verified": mediator_ephemeral,
        "shared_menu_verified": True,
        "budget_matched": True,
        "resolver_identity_matched": True,
        "null_disagreement_vector": list(null_vector),
        "null_mediator_output": null_output.value,
    }


def run_assay() -> dict[str, object]:
    c0_results = [
        run_episode(Condition.C0, pair, true_model)
        for pair, true_model in positive_episode_specs()
    ]
    c1_results = [
        run_episode(Condition.C1, pair, true_model)
        for pair, true_model in positive_episode_specs()
    ]
    c0 = aggregate_results(c0_results)
    c1 = aggregate_results(c1_results)
    contract = validate_contract()
    return {
        "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
        "execution_state": "EXECUTED",
        "positive_pair_count": contract["positive_pair_count"],
        "positive_episode_count_per_condition": contract[
            "positive_episode_count_per_condition"
        ],
        "c0_discriminating_count": c0["discriminating_count"],
        "c1_discriminating_count": c1["discriminating_count"],
        "c0_repair_success_count": c0["repair_success_count"],
        "c1_repair_success_count": c1["repair_success_count"],
        "P_disc_C0": c0["P_disc"],
        "P_disc_C1": c1["P_disc"],
        "delta_P_disc": c1["P_disc"] - c0["P_disc"],
        "P_repair_C0": c0["P_repair"],
        "P_repair_C1": c1["P_repair"],
        "delta_P_repair": c1["P_repair"] - c0["P_repair"],
        **{
            key: value
            for key, value in contract.items()
            if key not in {"positive_pair_count", "positive_episode_count_per_condition"}
        },
    }
