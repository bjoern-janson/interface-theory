#!/usr/bin/env python3
"""Exact exhaustive audit for Gate 014 cross-context factorization.

This script uses only deterministic rational arithmetic. It generates the full
frozen class before computing any interface partitions or target values, runs
generator-validity checks, audits all 64 subsets of the six-probe vocabulary,
and emits canonical JSON with one terminal Gate 1 decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, Sequence


PROTOCOL_VERSION = "CROSS_CONTEXT_DYNAMIC_FACTORIZATION_v0.1"
CONTRACT_PATH = Path(__file__).with_name("GATE_014_CONTRACT.md")
CONTEXTS = (Fraction(-1), Fraction(0), Fraction(1))
ID_CONTEXTS = (Fraction(-1), Fraction(0))
TARGET_CONTEXTS = (Fraction(1),)
COMMON_CAUSES = (Fraction(-1), Fraction(1))
REVERSAL_BRANCHES = (0, 1)
EVIDENCE_BRANCHES = (0, 1)
NODES = (3, 4)
LAGS = (2, 3)
HORIZON_R = 5
THRESHOLD_R = Fraction(4, 5)
CONSECUTIVE_R = 2

SELECTIONS = ("delete", "reversible")
TOPOLOGIES = ("independent", "propagating")
C_R_VALUES = (Fraction(-1, 8), Fraction(0), Fraction(1, 8))
C_K_VALUES = (Fraction(-1), Fraction(0), Fraction(1))

# Lexicographic order is the canonical interface and observation order.
PROBE_ORDER = (
    "K_BASE",
    "K_CONTEXT",
    "K_LAG",
    "K_NODE",
    "R_NEG",
    "R_ZERO",
)

FLOW_PROBES = {
    "K_BASE": (Fraction(-1), 3, 2),
    "K_CONTEXT": (Fraction(0), 3, 2),
    "K_LAG": (Fraction(-1), 3, 3),
    "K_NODE": (Fraction(-1), 4, 2),
}


@dataclass(frozen=True)
class DynamicSystem:
    system_id: str
    selection: str
    u_r: Fraction
    c_r: Fraction
    topology: str
    u_k: Fraction
    c_k: Fraction

    @property
    def hidden_reserve(self) -> Fraction:
        return Fraction(int(self.selection == "reversible"))

    @property
    def primary_path(self) -> Fraction:
        return Fraction(int(self.topology == "propagating"))

    @property
    def latent_key(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return (self.u_r, self.c_r, self.u_k, self.c_k)


def ftoken(value: Fraction) -> str:
    sign = "m" if value < 0 else "p"
    value = abs(value)
    return f"{sign}{value.numerator}d{value.denominator}"


def system_identifier(
    selection: str,
    u_r: Fraction,
    c_r: Fraction,
    topology: str,
    u_k: Fraction,
    c_k: Fraction,
) -> str:
    return "__".join(
        (
            f"S-{selection}",
            f"uR-{ftoken(u_r)}",
            f"cR-{ftoken(c_r)}",
            f"G-{topology}",
            f"uK-{ftoken(u_k)}",
            f"cK-{ftoken(c_k)}",
        )
    )


def legal_u_r(selection: str) -> tuple[Fraction, ...]:
    if selection == "delete":
        return (Fraction(0), Fraction(1, 4))
    if selection == "reversible":
        return (Fraction(-1, 4), Fraction(0))
    raise ValueError(selection)


def legal_u_k(topology: str) -> tuple[Fraction, ...]:
    if topology == "independent":
        return (Fraction(-1), Fraction(0), Fraction(1))
    if topology == "propagating":
        return (Fraction(-2), Fraction(-1), Fraction(0))
    raise ValueError(topology)


def generate_systems() -> tuple[DynamicSystem, ...]:
    systems: list[DynamicSystem] = []
    for selection in SELECTIONS:
        for u_r in legal_u_r(selection):
            for c_r in C_R_VALUES:
                for topology in TOPOLOGIES:
                    for u_k in legal_u_k(topology):
                        for c_k in C_K_VALUES:
                            systems.append(
                                DynamicSystem(
                                    system_id=system_identifier(
                                        selection, u_r, c_r, topology, u_k, c_k
                                    ),
                                    selection=selection,
                                    u_r=u_r,
                                    c_r=c_r,
                                    topology=topology,
                                    u_k=u_k,
                                    c_k=c_k,
                                )
                            )
    return tuple(sorted(systems, key=lambda system: system.system_id))


SYSTEMS = generate_systems()


def reopen_rate(system: DynamicSystem, context: Fraction, reversal: int) -> Fraction:
    return Fraction(reversal) * (
        Fraction(1, 8)
        + system.hidden_reserve / 4
        + system.u_r
        + system.c_r * context
    )


def reopen_trajectory(
    system: DynamicSystem, context: Fraction, reversal: int
) -> tuple[Fraction, ...]:
    authority = Fraction(0)
    rate = reopen_rate(system, context, reversal)
    values: list[Fraction] = []
    for _ in range(HORIZON_R):
        authority = min(Fraction(1), authority + rate)
        values.append(authority)
    return tuple(values)


def flow_states(
    system: DynamicSystem,
    context: Fraction,
    node: int,
    evidence: int,
) -> tuple[Fraction, Fraction, Fraction]:
    if node not in NODES:
        raise ValueError(node)
    node_offset = Fraction(int(node == 4))
    primary = system.primary_path * evidence
    auxiliary_1 = Fraction(evidence) * (
        system.u_k + system.c_k * (context + node_offset)
    )
    auxiliary_2 = auxiliary_1 + system.c_k * evidence
    return primary, auxiliary_1, auxiliary_2


def flow_output(
    system: DynamicSystem,
    context: Fraction,
    node: int,
    lag: int,
    common_cause: Fraction,
    evidence: int,
) -> Fraction:
    if lag not in LAGS:
        raise ValueError(lag)
    primary, auxiliary_1, auxiliary_2 = flow_states(
        system, context, node, evidence
    )
    auxiliary = auxiliary_1 if lag == 2 else auxiliary_2
    return common_cause + primary + auxiliary


def flow_contrast(
    system: DynamicSystem, context: Fraction, node: int, lag: int
) -> Fraction:
    contrasts = []
    for common_cause in COMMON_CAUSES:
        contrasts.append(
            flow_output(system, context, node, lag, common_cause, 1)
            - flow_output(system, context, node, lag, common_cause, 0)
        )
    return sum(contrasts, Fraction(0)) / len(contrasts)


def reopen_target(system: DynamicSystem) -> int:
    active = reopen_trajectory(system, Fraction(1), 1)
    control = reopen_trajectory(system, Fraction(1), 0)
    contrast = tuple(left - right for left, right in zip(active, control))
    return int(
        any(
            all(value >= THRESHOLD_R for value in contrast[start : start + CONSECUTIVE_R])
            for start in range(HORIZON_R - CONSECUTIVE_R + 1)
        )
    )


def flow_target(system: DynamicSystem) -> Fraction:
    return flow_contrast(system, Fraction(1), 4, 3)


def target(system: DynamicSystem) -> tuple[int, Fraction]:
    # This function deliberately simulates only target-context assays. It does
    # not call observation(), probe_values(), or inspect architecture labels.
    return reopen_target(system), flow_target(system)


def nuisance_vector(system: DynamicSystem) -> tuple[Fraction, ...]:
    # Baseline, observable suppression trace, passive node-1/node-3 traces for
    # q=-1,+1, and unintervened active-assay outputs. Hidden state is excluded.
    values = [Fraction(0)]
    values.extend(Fraction(0) for _ in range(3))
    for common_cause in COMMON_CAUSES:
        values.extend((common_cause, common_cause))
    for context in CONTEXTS:
        for common_cause in COMMON_CAUSES:
            values.append(flow_output(system, context, 3, 2, common_cause, 0))
    return tuple(values)


def probe_values(system: DynamicSystem, probe: str) -> tuple[Fraction, ...]:
    # Interface code executes identification assays only. No target context,
    # target function, label, coefficient, or internal state is exposed.
    if probe == "R_NEG":
        context = Fraction(-1)
        return tuple(
            value
            for reversal in REVERSAL_BRANCHES
            for value in reopen_trajectory(system, context, reversal)
        )
    if probe == "R_ZERO":
        context = Fraction(0)
        return tuple(
            value
            for reversal in REVERSAL_BRANCHES
            for value in reopen_trajectory(system, context, reversal)
        )
    if probe in FLOW_PROBES:
        context, node, lag = FLOW_PROBES[probe]
        return tuple(
            flow_output(system, context, node, lag, common_cause, evidence)
            for common_cause in COMMON_CAUSES
            for evidence in EVIDENCE_BRANCHES
        )
    raise KeyError(probe)


def observation(system: DynamicSystem, probes: tuple[str, ...]) -> tuple[Fraction, ...]:
    values = [Fraction(0)]  # mandatory constant passive protocol control
    for probe in probes:
        values.extend(probe_values(system, probe))
    return tuple(values)


def dynamic_signature(system: DynamicSystem) -> tuple[Fraction, ...]:
    # Numeric internal-state signature over every declared context and branch.
    # Labels and parameter names are not included.
    values = [system.hidden_reserve, system.primary_path]
    for context in CONTEXTS:
        for reversal in REVERSAL_BRANCHES:
            values.append(reopen_rate(system, context, reversal))
            values.extend(reopen_trajectory(system, context, reversal))
    for context in CONTEXTS:
        for node in NODES:
            for evidence in EVIDENCE_BRANCHES:
                values.extend(flow_states(system, context, node, evidence))
                for common_cause in COMMON_CAUSES:
                    for lag in LAGS:
                        values.append(
                            flow_output(
                                system,
                                context,
                                node,
                                lag,
                                common_cause,
                                evidence,
                            )
                        )
    return tuple(values)


def pair(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def encode_fractions(values: Iterable[Fraction | int]) -> list[list[int]]:
    return [pair(value) for value in values]


def encode_target(value: tuple[int, Fraction]) -> list[object]:
    return [value[0], pair(value[1])]


def signature_hash(values: Sequence[Fraction]) -> str:
    canonical = json.dumps(encode_fractions(values), separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def parameter_record(system: DynamicSystem) -> dict:
    return {
        "selection": system.selection,
        "hidden_reserve": pair(system.hidden_reserve),
        "u_r": pair(system.u_r),
        "c_r": pair(system.c_r),
        "topology": system.topology,
        "primary_path": pair(system.primary_path),
        "u_k": pair(system.u_k),
        "c_k": pair(system.c_k),
    }


def target_key(value: tuple[int, Fraction]) -> tuple[int, int, int]:
    return value[0], value[1].numerator, value[1].denominator


def system_target_table() -> list[dict]:
    return [
        {
            "system_id": system.system_id,
            "parameters": parameter_record(system),
            "target": encode_target(target(system)),
            "dynamic_signature_sha256": signature_hash(dynamic_signature(system)),
        }
        for system in SYSTEMS
    ]


def exact_balance_table() -> list[dict]:
    counts: Counter[tuple[str, str, tuple[int, int, int]]] = Counter()
    for system in SYSTEMS:
        counts[(system.selection, system.topology, target_key(target(system)))] += 1
    records = []
    for (selection, topology, encoded), count in sorted(counts.items()):
        records.append(
            {
                "selection": selection,
                "topology": topology,
                "target": [encoded[0], [encoded[1], encoded[2]]],
                "count": count,
            }
        )
    return records


def generator_validity() -> dict:
    errors: list[str] = []
    ids = [system.system_id for system in SYSTEMS]
    signatures = [dynamic_signature(system) for system in SYSTEMS]
    nuisances = [nuisance_vector(system) for system in SYSTEMS]
    targets = [target(system) for system in SYSTEMS]

    if len(SYSTEMS) != 216:
        errors.append(f"expected 216 systems, found {len(SYSTEMS)}")
    if len(set(ids)) != len(ids):
        errors.append("system identifiers are not unique")
    if len(set(signatures)) != len(signatures):
        errors.append("parameter tuples do not map to 216 distinct dynamic signatures")
    if len(set(nuisances)) != 1:
        errors.append("superficial nuisance vector is not exactly constant")
    if set(ID_CONTEXTS) & set(TARGET_CONTEXTS):
        errors.append("identification and target contexts overlap")

    r_values = {value[0] for value in targets}
    k_values = {value[1] for value in targets}
    if r_values != {0, 1}:
        errors.append("reopenability target is degenerate")
    if len(k_values) != 9:
        errors.append(f"expected nine signed flow targets, found {len(k_values)}")
    if len(set(targets)) != 18:
        errors.append("joint target support is not the declared 18 values")

    for selection in SELECTIONS:
        observed = {target(system)[0] for system in SYSTEMS if system.selection == selection}
        if observed != {0, 1}:
            errors.append(f"selection label {selection} determines reopenability")
    for r_value in (0, 1):
        observed = {system.selection for system in SYSTEMS if target(system)[0] == r_value}
        if observed != set(SELECTIONS):
            errors.append(f"reopenability {r_value} determines selection label")
    for topology in TOPOLOGIES:
        observed = {target(system)[1] for system in SYSTEMS if system.topology == topology}
        if observed != k_values:
            errors.append(f"topology label {topology} restricts signed flow support")
    for k_value in k_values:
        observed = {system.topology for system in SYSTEMS if target(system)[1] == k_value}
        if observed != set(TOPOLOGIES):
            errors.append(f"signed flow {k_value} determines topology label")

    coordinate_activity = {
        "selection_hidden_reserve": len({system.hidden_reserve for system in SYSTEMS}) > 1,
        "u_r_reversal_rate": len({
            Fraction(1, 8) + system.hidden_reserve / 4 + system.u_r
            for system in SYSTEMS
        }) > 1,
        "c_r_context_slope": len({system.c_r for system in SYSTEMS}) > 1,
        "topology_primary_path": len({system.primary_path for system in SYSTEMS}) > 1,
        "u_k_auxiliary_intercept": len({system.u_k for system in SYSTEMS}) > 1,
        "c_k_context_node_lag_slope": len({system.c_k for system in SYSTEMS}) > 1,
    }
    if not all(coordinate_activity.values()):
        errors.append("at least one declared parameter coordinate is dynamically inactive")

    return {
        "valid": not errors,
        "errors": errors,
        "theta_cardinality": len(SYSTEMS),
        "dynamic_system_cardinality": len(set(signatures)),
        "external_target_support_size": len(set(targets)),
        "reopenability_support": sorted(r_values),
        "signed_flow_support": [pair(value) for value in sorted(k_values)],
        "nuisance_signature": encode_fractions(nuisances[0]) if nuisances else [],
        "nuisance_constant": len(set(nuisances)) == 1,
        "context_domains_disjoint": not (set(ID_CONTEXTS) & set(TARGET_CONTEXTS)),
        "coordinate_activity": coordinate_activity,
        "architecture_target_counts": exact_balance_table(),
        "generation_policy": {
            "full_legal_parameter_image_generated": True,
            "target_conditioned_filtering": False,
            "observation_conditioned_filtering": False,
            "collision_conditioned_filtering": False,
            "post_generation_deduplication": False,
        },
    }


def class_record(
    observation_value: tuple[Fraction, ...], systems: list[DynamicSystem]
) -> tuple[dict, int, int]:
    systems = sorted(systems, key=lambda system: system.system_id)
    target_values = [target(system) for system in systems]
    unique_targets = sorted(set(target_values), key=target_key)
    architectures = sorted({(system.selection, system.topology) for system in systems})
    latents = sorted(
        {system.latent_key for system in systems},
        key=lambda values: tuple((value.numerator, value.denominator) for value in values),
    )
    dynamic_count = len({dynamic_signature(system) for system in systems})

    heterogeneous_pairs = []
    pair_count = 0
    for left, right in combinations(systems, 2):
        if target(left) != target(right):
            pair_count += 1
            if not heterogeneous_pairs:
                heterogeneous_pairs.append(
                    {
                        "system_a": left.system_id,
                        "system_b": right.system_id,
                        "target_a": encode_target(target(left)),
                        "target_b": encode_target(target(right)),
                    }
                )

    record = {
        "observation": encode_fractions(observation_value),
        "systems": [system.system_id for system in systems],
        "targets": [encode_target(value) for value in unique_targets],
        "target_homogeneous": len(unique_targets) == 1,
        "architecture_configurations": [list(value) for value in architectures],
        "architecture_configuration_count": len(architectures),
        "latent_configurations": [encode_fractions(value) for value in latents],
        "latent_configuration_count": len(latents),
        "internal_dynamics_signature_count": dynamic_count,
        "canonical_counterexample": heterogeneous_pairs[0] if heterogeneous_pairs else None,
        "target_changing_pair_count": pair_count,
    }
    return record, pair_count, len(unique_targets)


def audit_interface(probes: tuple[str, ...]) -> dict:
    partitions: dict[tuple[Fraction, ...], list[DynamicSystem]] = {}
    for system in SYSTEMS:
        partitions.setdefault(observation(system, probes), []).append(system)

    classes = []
    heterogeneous_count = 0
    target_changing_pairs = 0
    collision_target_values: set[tuple[int, Fraction]] = set()
    class_sizes = []
    systems_in_collisions = 0
    pairwise_collisions = 0
    for obs, members in sorted(partitions.items(), key=lambda item: item[0]):
        record, changed_pairs, target_count = class_record(obs, members)
        classes.append(record)
        size = len(members)
        class_sizes.append(size)
        if size > 1:
            systems_in_collisions += size
            pairwise_collisions += size * (size - 1) // 2
            collision_target_values.update(target(system) for system in members)
        if target_count > 1:
            heterogeneous_count += 1
            target_changing_pairs += changed_pairs

    singleton_count = sum(size == 1 for size in class_sizes)
    collision_count = sum(size > 1 for size in class_sizes)
    identifiable = heterogeneous_count == 0
    if not identifiable:
        decision = "FAIL_COUNTEREXAMPLE"
    elif singleton_count == len(SYSTEMS):
        decision = "PASS_INJECTIVE_INTERFACE"
    else:
        decision = "PASS_NONTRIVIAL_QUOTIENT"

    all_target_values = set(target(system) for system in SYSTEMS)
    collision_records = [record for record in classes if len(record["systems"]) > 1]
    structural_subtype = bool(collision_records) and all(
        record["internal_dynamics_signature_count"] > 1
        for record in collision_records
    ) and collision_target_values == all_target_values

    histogram = Counter(class_sizes)
    scalar_cost = 1 + sum(len(probe_values(SYSTEMS[0], probe)) for probe in probes)
    return {
        "interface_id": "BASELINE" + ("+" + "+".join(probes) if probes else ""),
        "probes": list(probes),
        "informative_probe_cost": len(probes),
        "protocol_probe_cost": len(probes) + 1,
        "raw_scalar_coordinate_cost": scalar_cost,
        "identifiable": identifiable,
        "decision": decision,
        "decision_subtype": (
            "PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY"
            if decision == "PASS_NONTRIVIAL_QUOTIENT" and structural_subtype
            else None
        ),
        "quotient": {
            "class_count": len(classes),
            "class_size_histogram": {str(size): histogram[size] for size in sorted(histogram)},
            "singleton_class_count": singleton_count,
            "collision_class_count": collision_count,
            "systems_in_collision_classes": systems_in_collisions,
            "pairwise_collision_count": pairwise_collisions,
            "compression_ratio": pair(Fraction(len(classes), len(SYSTEMS))),
            "singleton_fraction": pair(Fraction(singleton_count, len(SYSTEMS))),
            "heterogeneous_class_count": heterogeneous_count,
            "target_changing_pair_count": target_changing_pairs,
            "collision_target_value_coverage": [
                encode_target(value) for value in sorted(collision_target_values, key=target_key)
            ],
            "all_target_values_covered_by_collisions": collision_target_values
            == all_target_values,
        },
        "observation_classes": classes,
    }


def interface_lattice() -> tuple[tuple[str, ...], ...]:
    return tuple(
        subset
        for cost in range(len(PROBE_ORDER) + 1)
        for subset in combinations(PROBE_ORDER, cost)
    )


def subset_minimal_identifying(results: list[dict]) -> list[dict]:
    identifying = [record for record in results if record["identifiable"]]
    minimal = []
    for record in identifying:
        probes = set(record["probes"])
        if not any(
            set(other["probes"]) < probes
            for other in identifying
        ):
            minimal.append(record)
    return sorted(minimal, key=lambda record: (len(record["probes"]), record["probes"]))


def terminal_decision(minimal: list[dict]) -> tuple[str, str | None]:
    if not minimal:
        return "FAIL_COUNTEREXAMPLE", None
    if any(record["decision"] == "PASS_NONTRIVIAL_QUOTIENT" for record in minimal):
        subtype = (
            "PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY"
            if all(
                record["decision_subtype"]
                == "PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY"
                for record in minimal
            )
            else None
        )
        return "PASS_NONTRIVIAL_QUOTIENT", subtype
    return "PASS_INJECTIVE_INTERFACE", None


def contract_sha256() -> str:
    return hashlib.sha256(CONTRACT_PATH.read_bytes()).hexdigest()


def run_audit() -> dict:
    validity = generator_validity()
    base = {
        "gate_id": "GATE-014",
        "protocol_version": PROTOCOL_VERSION,
        "contract_sha256": contract_sha256(),
        "execution_status": "EXECUTED" if validity["valid"] else "INVALID_GENERATOR",
        "generator_validity": validity,
        "scientific_scope": (
            "Exact finite-class cross-context factorization and target-preserving compression only; "
            "no estimator, generalizable law, predictive validity, mechanism efficacy, or architecture claim."
        ),
    }
    if not validity["valid"]:
        return {
            **base,
            "scientific_decision": None,
            "decision_subtype": None,
            "interfaces": [],
            "minimum_identifying_antichain": [],
        }

    results = [audit_interface(probes) for probes in interface_lattice()]
    minimal = subset_minimal_identifying(results)
    decision, subtype = terminal_decision(minimal)
    identifying = [record for record in results if record["identifiable"]]
    minimum_probe_cost = (
        min(record["informative_probe_cost"] for record in identifying)
        if identifying
        else None
    )
    lower_failed = all(
        not record["identifiable"]
        for record in results
        if minimum_probe_cost is not None
        and record["informative_probe_cost"] < minimum_probe_cost
    )

    return {
        **base,
        "system_class": {
            "name": "F_014",
            "parameter_space_cardinality": len(SYSTEMS),
            "dynamic_system_cardinality": len(
                {dynamic_signature(system) for system in SYSTEMS}
            ),
            "systems": system_target_table(),
        },
        "assay_domains": {
            "identification_contexts": encode_fractions(ID_CONTEXTS),
            "target_contexts": encode_fractions(TARGET_CONTEXTS),
            "disjoint": not (set(ID_CONTEXTS) & set(TARGET_CONTEXTS)),
            "common_cause_contexts": encode_fractions(COMMON_CAUSES),
            "target_flow_assay": {
                "context": pair(1),
                "node": 4,
                "lag": 3,
            },
        },
        "target": {
            "name": "L_014",
            "components": ["R_star", "K_star"],
            "reopenability_horizon": HORIZON_R,
            "reopenability_threshold": pair(THRESHOLD_R),
            "reopenability_consecutive_steps": CONSECUTIVE_R,
            "flow_equality_tolerance": pair(0),
            "target_support": [
                encode_target(value)
                for value in sorted({target(system) for system in SYSTEMS}, key=target_key)
            ],
        },
        "interface_policy": {
            "mandatory_controls": ["PASSIVE_BASELINE"],
            "probe_order": list(PROBE_ORDER),
            "interface_count": len(results),
            "all_subsets_audited": True,
            "unrestricted_encodings_tested": False,
            "excluded_access": [
                "target-context trajectories",
                "target values",
                "selection and topology labels",
                "hidden reserve and internal path states",
                "parameter coefficients and generator metadata",
                "system identifiers",
            ],
        },
        "interfaces": results,
        "identifying_interface_count": len(identifying),
        "minimum_informative_probe_cost_in_frozen_vocabulary": minimum_probe_cost,
        "minimum_protocol_probe_cost_with_mandatory_baseline": (
            minimum_probe_cost + 1 if minimum_probe_cost is not None else None
        ),
        "all_lower_probe_cost_interfaces_failed": lower_failed,
        "minimum_identifying_antichain": [
            {
                "interface_id": record["interface_id"],
                "probes": record["probes"],
                "informative_probe_cost": record["informative_probe_cost"],
                "protocol_probe_cost": record["protocol_probe_cost"],
                "raw_scalar_coordinate_cost": record["raw_scalar_coordinate_cost"],
                "decision": record["decision"],
                "decision_subtype": record["decision_subtype"],
                "quotient": record["quotient"],
            }
            for record in minimal
        ],
        "scientific_decision": decision,
        "decision_subtype": subtype,
        "decision_scope": (
            "A noninjective pass establishes finite target-preserving compression. "
            "The induced map may still be an arbitrary finite lookup over interface fingerprints. "
            "Gates 2 through 4 remain closed."
        ),
    }


def canonical_json(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        type=Path,
        help="Optional path for the complete canonical audit JSON.",
    )
    args = parser.parse_args()
    rendered = canonical_json(run_audit())
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_bytes(rendered)
    print(rendered.decode("utf-8"), end="")


if __name__ == "__main__":
    main()

