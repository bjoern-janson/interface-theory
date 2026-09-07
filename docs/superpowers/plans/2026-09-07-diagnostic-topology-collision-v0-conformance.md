# Diagnostic Topology Collision V0 Conformance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an executable conformance implementation of the already-refrozen `DIAGNOSTIC_TOPOLOGY_COLLISION_V0` finite construction without changing its mathematical or causal meaning.

**Architecture:** Implement the frozen object as a small Python 3.12 standard-library package under `experiments/research_seeds/diagnostic_topology_collision_v0/`. Keep world/resource semantics, representation/controller semantics, viable-initial-action analysis, and exhaustive conformance execution separate so implementation validation can run without performing the exhaustive conformance run. Expose the exhaustive run only behind an explicit `--execute --write <path>` gate.

**Tech Stack:** Python 3.12 standard library, `unittest`, GitHub Actions.

**Spec:** `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`

## Global Constraints

- Operative pre-execution refreeze commit: `c650943031831aaa50379dd5dd79515bf681c0f3`.
- Frozen DTC-V0 spec Git blob: `447e5db3f15476406910a32e1d36c0e2364e1344`.
- Frozen repair-authority addendum Git blob: `303031bdec77dfffb4a5d6c9bdd2d033f30314ac`.
- The implementation branch must descend from the commit containing this plan and retain `c650943031831aaa50379dd5dd79515bf681c0f3` in ancestry.
- Recommended implementation branch: `impl/diagnostic-topology-collision-v0-conformance`.
- Create an isolated worktree at execution time.
- Do not modify either frozen source file named above during implementation.
- Do not modify canonical Interface Theory artifacts, Gate 013/014 artifacts, MATRIX artifacts, or canonical/evidence ledgers.
- The executable may expose a conformance failure; it may not redefine the frozen analytic object to make the implementation pass.
- Frozen worlds: `G_A`, `G_B`; fault set `{0,1}`.
- Frozen diagnostic topology: `G_A: q_A -> f, q_B -> bottom`; `G_B: q_B -> f, q_A -> bottom`.
- Frozen repairs: `R(0)={r_0}`, `R(1)={r_1}`.
- Frozen resource contract: `B=2`, diagnostic cost `1`, repair cost `1`.
- Frozen raw history: `h=(t,n)`, `t(A)=0`, `t(B)=1`, `n in {0,1}`, fault absent from history.
- Frozen encoders: `g_0(h)=n`, `g_1(h)=t`; each exposes one bit.
- Frozen controller: bit `0 -> q_A`, bit `1 -> q_B`; observed fault value `y -> r_y`.
- Viable-policy collision must be implemented as nonempty policy classes with incompatible required initial actions, never as syntactic singleton policy sets.
- The representation intervention changes viable-policy **selectability from exposed information**; it does not change policy existence or the world's viable-policy classes.
- Frozen family: `tau in {A,B}`, `f in {0,1}`, `n in {0,1}` = exactly `8` episodes per representation condition.
- Frozen analytic values: `success_count_g0=4`, `success_count_g1=8`, `wrong_probe_count_g0=4`, `wrong_probe_count_g1=0`, `P_success_g0=0.5`, `P_success_g1=1.0`, `delta_P_success=0.5`.
- Required future result fields remain exactly those named by the refrozen spec: `protocol_state`, `total_worlds`, `success_count_g0`, `success_count_g1`, `wrong_probe_count_g0`, `wrong_probe_count_g1`, `P_success_g0`, `P_success_g1`, `delta_P_success`, `viable_policy_initial_action_collision_verified`, `controller_selectability_effect_verified`, `raw_history_equal_across_conditions`, `representation_capacity_matched`, `controller_identity_matched`, `primitive_actions_matched`, `budget_matched`.
- Implementation-phase tests may exercise components and representative episodes, but must not call the full exhaustive `run_conformance()` entry point.
- During implementation, never invoke `run_v0.py --execute`.
- During implementation, do not create `experiments/research_seeds/diagnostic_topology_collision_v0/results/` and do not create a DTC-V0 result JSON.
- Terminal implementation state before separate execution authorization must be:

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state      = UNEXECUTED
scientific_result    = NONE
```

---

## File Structure

Create exactly:

```text
experiments/research_seeds/diagnostic_topology_collision_v0/
    README.md
    protocol.py
    representation.py
    viability.py
    conformance.py
    run_v0.py
    test_protocol.py
    test_representation.py
    test_viability.py
    test_conformance.py
    test_cli.py

.github/workflows/validate-dtc-v0-implementation.yml
```

No `results/` directory exists at implementation completion.

---

### Task 1: Encode the Frozen World and Resource Contract

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/protocol.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_protocol.py`

**Interfaces:**
- Produces: `Topology`, `Diagnostic`, `Repair`, `Action`, `FAULTS`, `TOPOLOGY_BIT`, `ACTIONS`, `BUDGET`, `DIAGNOSTIC_COST`, `REPAIR_COST`, `probe()`, `valid_repair()`.

- [ ] **Step 1: Write the failing protocol tests**

```python
# test_protocol.py
import unittest

from protocol import (
    ACTIONS, BUDGET, DIAGNOSTIC_COST, FAULTS, REPAIR_COST, TOPOLOGY_BIT,
    Diagnostic, Repair, Topology, probe, valid_repair,
)


class ProtocolTests(unittest.TestCase):
    def test_frozen_resources_and_actions(self):
        self.assertEqual((BUDGET, DIAGNOSTIC_COST, REPAIR_COST), (2, 1, 1))
        self.assertEqual(FAULTS, (0, 1))
        self.assertEqual(TOPOLOGY_BIT, {Topology.A: 0, Topology.B: 1})
        self.assertEqual(
            ACTIONS,
            (Diagnostic.QA, Diagnostic.QB, Repair.R0, Repair.R1, "stop"),
        )

    def test_ga_topology(self):
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 0), 0)
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 1), 1)
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 0))
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 1))

    def test_gb_topology(self):
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 0), 0)
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 1), 1)
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 0))
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 1))

    def test_fault_specific_repairs(self):
        self.assertTrue(valid_repair(0, Repair.R0))
        self.assertTrue(valid_repair(1, Repair.R1))
        self.assertFalse(valid_repair(0, Repair.R1))
        self.assertFalse(valid_repair(1, Repair.R0))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Verify RED**

```bash
cd experiments/research_seeds/diagnostic_topology_collision_v0
python -m unittest test_protocol.py -v
```

Expected: import failure because `protocol.py` does not exist.

- [ ] **Step 3: Implement the minimal protocol**

```python
# protocol.py
from __future__ import annotations

from enum import Enum
from typing import TypeAlias


class Topology(str, Enum):
    A = "A"
    B = "B"


class Diagnostic(str, Enum):
    QA = "q_A"
    QB = "q_B"


class Repair(str, Enum):
    R0 = "r_0"
    R1 = "r_1"


Action: TypeAlias = Diagnostic | Repair | str
FAULTS = (0, 1)
TOPOLOGY_BIT = {Topology.A: 0, Topology.B: 1}
ACTIONS: tuple[Action, ...] = (
    Diagnostic.QA, Diagnostic.QB, Repair.R0, Repair.R1, "stop"
)
BUDGET = 2
DIAGNOSTIC_COST = 1
REPAIR_COST = 1


def probe(topology: Topology, diagnostic: Diagnostic, fault: int) -> int | None:
    if fault not in FAULTS:
        raise ValueError("fault must be 0 or 1")
    if topology is Topology.A:
        return fault if diagnostic is Diagnostic.QA else None
    return fault if diagnostic is Diagnostic.QB else None


def valid_repair(fault: int, repair: Repair) -> bool:
    if fault not in FAULTS:
        raise ValueError("fault must be 0 or 1")
    return (fault == 0 and repair is Repair.R0) or (
        fault == 1 and repair is Repair.R1
    )
```

`None` is only the executable spelling of the frozen `bottom` diagnostic outcome.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest test_protocol.py -v
```

Expected: all protocol tests pass.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/protocol.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_protocol.py
git commit -m "test: encode DTC V0 frozen world contract"
```

---

### Task 2: Encode Raw History, One-Bit Encoders, and the Fixed Controller

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/representation.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_representation.py`

**Interfaces:**
- Consumes: `Topology`, `TOPOLOGY_BIT`, `Diagnostic`.
- Produces: `RawHistory`, `make_history()`, `g0()`, `g1()`, `select_diagnostic()`.

- [ ] **Step 1: Write the failing tests**

```python
# test_representation.py
import unittest

from protocol import Diagnostic, Topology
from representation import RawHistory, g0, g1, make_history, select_diagnostic


class RepresentationTests(unittest.TestCase):
    def test_same_history_can_feed_both_encoders(self):
        history = make_history(Topology.A, 1)
        self.assertEqual(history, RawHistory(topology_bit=0, nuisance=1))
        self.assertEqual(g0(history), 1)
        self.assertEqual(g1(history), 0)

    def test_g0_collapses_topology_for_matched_nuisance(self):
        for nuisance in (0, 1):
            self.assertEqual(
                g0(make_history(Topology.A, nuisance)),
                g0(make_history(Topology.B, nuisance)),
            )

    def test_g1_preserves_topology_for_both_nuisance_values(self):
        for nuisance in (0, 1):
            self.assertEqual(g1(make_history(Topology.A, nuisance)), 0)
            self.assertEqual(g1(make_history(Topology.B, nuisance)), 1)

    def test_both_encoders_are_binary(self):
        for topology in (Topology.A, Topology.B):
            for nuisance in (0, 1):
                history = make_history(topology, nuisance)
                self.assertIn(g0(history), (0, 1))
                self.assertIn(g1(history), (0, 1))

    def test_controller_is_fixed(self):
        self.assertIs(select_diagnostic(0), Diagnostic.QA)
        self.assertIs(select_diagnostic(1), Diagnostic.QB)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Verify RED**

```bash
python -m unittest test_representation.py -v
```

Expected: import failure because `representation.py` does not exist.

- [ ] **Step 3: Implement the minimal representation module**

```python
# representation.py
from __future__ import annotations

from dataclasses import dataclass

from protocol import Diagnostic, TOPOLOGY_BIT, Topology


@dataclass(frozen=True)
class RawHistory:
    topology_bit: int
    nuisance: int


def make_history(topology: Topology, nuisance: int) -> RawHistory:
    if nuisance not in (0, 1):
        raise ValueError("nuisance must be 0 or 1")
    return RawHistory(TOPOLOGY_BIT[topology], nuisance)


def g0(history: RawHistory) -> int:
    return history.nuisance


def g1(history: RawHistory) -> int:
    return history.topology_bit


def select_diagnostic(retained_bit: int) -> Diagnostic:
    if retained_bit == 0:
        return Diagnostic.QA
    if retained_bit == 1:
        return Diagnostic.QB
    raise ValueError("retained bit must be 0 or 1")
```

No condition-specific controller and no fault/topology oracle may be added.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest test_representation.py -v
```

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/representation.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_representation.py
git commit -m "test: encode DTC V0 representation intervention"
```

---

### Task 3: Verify Viable-Policy Collision by Required Initial Action

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/viability.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_viability.py`

**Interfaces:**
- Produces: `initial_action_supports_zero_error()`, `viable_initial_actions()`.
- This module verifies the repaired viable-policy claim without enumerating syntactic policies.

- [ ] **Step 1: Write the failing tests**

```python
# test_viability.py
import unittest

from protocol import Diagnostic, Repair, Topology
from viability import initial_action_supports_zero_error, viable_initial_actions


class ViabilityTests(unittest.TestCase):
    def test_ga_requires_q_a_initially(self):
        self.assertEqual(viable_initial_actions(Topology.A), frozenset({Diagnostic.QA}))

    def test_gb_requires_q_b_initially(self):
        self.assertEqual(viable_initial_actions(Topology.B), frozenset({Diagnostic.QB}))

    def test_wrong_probe_has_no_bounded_zero_error_continuation(self):
        self.assertFalse(initial_action_supports_zero_error(Topology.A, Diagnostic.QB))
        self.assertFalse(initial_action_supports_zero_error(Topology.B, Diagnostic.QA))

    def test_repairs_and_stop_cannot_guarantee_both_faults_initially(self):
        for topology in (Topology.A, Topology.B):
            self.assertFalse(initial_action_supports_zero_error(topology, Repair.R0))
            self.assertFalse(initial_action_supports_zero_error(topology, Repair.R1))
            self.assertFalse(initial_action_supports_zero_error(topology, "stop"))

    def test_viable_initial_action_sets_are_nonempty_and_disjoint(self):
        a = viable_initial_actions(Topology.A)
        b = viable_initial_actions(Topology.B)
        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(a.isdisjoint(b))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Verify RED**

```bash
python -m unittest test_viability.py -v
```

- [ ] **Step 3: Implement bounded initial-action analysis**

```python
# viability.py
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
```

This proves only the required initial-action property. Policies may differ on unreachable histories.

- [ ] **Step 4: Verify GREEN**

```bash
python -m unittest test_viability.py -v
```

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/viability.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_viability.py
git commit -m "test: verify DTC V0 viable initial-action collision"
```

---

### Task 4: Add Representative Episode Semantics and a Dormant Exhaustive Runner

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/conformance.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_conformance.py`

**Interfaces:**
- Produces: `Condition`, `EpisodeSpec`, `EpisodeResult`, `episode_specs()`, `run_episode()`, `validate_contract()`, `run_conformance()`.
- `run_episode()` takes an explicit `RawHistory` so the exhaustive runner can pass the **same object** to `g0` and `g1` for each matched episode.
- `validate_contract()` must not call `run_conformance()`.
- Implementation tests must not call `run_conformance()`.

- [ ] **Step 1: Write failing component tests**

```python
# test_conformance.py
import unittest

from conformance import Condition, EpisodeSpec, episode_specs, run_episode, validate_contract
from protocol import Diagnostic, Topology
from representation import make_history


class ConformanceComponentTests(unittest.TestCase):
    def test_episode_family_is_exact(self):
        specs = episode_specs()
        self.assertEqual(len(specs), 8)
        self.assertEqual(
            {(s.topology, s.fault, s.nuisance) for s in specs},
            {
                (topology, fault, nuisance)
                for topology in (Topology.A, Topology.B)
                for fault in (0, 1)
                for nuisance in (0, 1)
            },
        )

    def test_g1_representative_episode_repairs(self):
        spec = EpisodeSpec(Topology.B, fault=1, nuisance=0)
        history = make_history(spec.topology, spec.nuisance)
        result = run_episode(Condition.G1, spec, history)
        self.assertIs(result.diagnostic, Diagnostic.QB)
        self.assertEqual(result.observation, 1)
        self.assertTrue(result.repair_success)
        self.assertEqual(result.budget_remaining, 0)

    def test_g0_representative_wrong_probe_fails_bounded_continuation(self):
        spec = EpisodeSpec(Topology.B, fault=0, nuisance=0)
        history = make_history(spec.topology, spec.nuisance)
        result = run_episode(Condition.G0, spec, history)
        self.assertIs(result.diagnostic, Diagnostic.QA)
        self.assertIsNone(result.observation)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")
        self.assertEqual(result.budget_remaining, 1)

    def test_static_validator_checks_refrozen_structure(self):
        contract = validate_contract()
        self.assertEqual(contract["positive_episode_count_per_condition"], 8)
        self.assertTrue(contract["viable_policy_initial_action_collision_verified"])
        self.assertTrue(contract["representation_capacity_matched"])
        self.assertTrue(contract["controller_identity_matched"])
        self.assertTrue(contract["primitive_actions_matched"])
        self.assertTrue(contract["budget_matched"])
        self.assertTrue(contract["controller_selectability_structure_verified"])


if __name__ == "__main__":
    unittest.main()
```

These tests are software validation, not the exhaustive conformance run.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest test_conformance.py -v
```

- [ ] **Step 3: Implement episode semantics and static validation**

Create `conformance.py` beginning with:

```python
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
```

Append static contract validation:

```python
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
```

Then append the exhaustive function, but do not invoke it during this plan:

```python
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
```

The returned execution record includes every required field from the refrozen spec. Any analytic-count or invariant mismatch raises instead of rewriting `EXPECTED_COUNTS`.

- [ ] **Step 4: Verify GREEN without exhaustive execution**

```bash
python -m unittest test_conformance.py -v
```

Do not call `run_conformance()`.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/conformance.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_conformance.py
git commit -m "feat: add dormant DTC V0 conformance runner"
```

---

### Task 5: Add a Hard Validation-vs-Execution CLI Gate

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/run_v0.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_cli.py`

**Interfaces:**
- `--validate-contract`: static validation only, no write path, `UNEXECUTED`.
- `--execute`: requires `--write`; legal only after separate explicit authorization.

- [ ] **Step 1: Write failing CLI tests**

```python
# test_cli.py
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "run_v0.py"


class CliTests(unittest.TestCase):
    def test_validate_contract_reports_unexecuted_state(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--validate-contract"],
            check=True, capture_output=True, text=True, cwd=ROOT,
        )
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["protocol_state"], "FROZEN_PRE_EXECUTION_ASSAY")
        self.assertEqual(payload["execution_state"], "UNEXECUTED")
        self.assertEqual(payload["scientific_result"], "NONE")

    def test_validate_rejects_write(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--validate-contract", "--write", "x.json"],
            capture_output=True, text=True, cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--write is valid only with --execute", proc.stderr)

    def test_execute_requires_write(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--execute"],
            capture_output=True, text=True, cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--execute requires --write", proc.stderr)


if __name__ == "__main__":
    unittest.main()
```

No test invokes a successful execution path.

- [ ] **Step 2: Verify RED**

```bash
python -m unittest test_cli.py -v
```

- [ ] **Step 3: Implement the gated runner**

```python
# run_v0.py
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from conformance import run_conformance, validate_contract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-contract", action="store_true")
    mode.add_argument("--execute", action="store_true")
    parser.add_argument("--write", type=Path)
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.validate_contract:
        if args.write is not None:
            parser.error("--write is valid only with --execute")
        payload = {
            "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
            "implementation_state": "VALIDATED_NOT_EXECUTED",
            "execution_state": "UNEXECUTED",
            "scientific_result": "NONE",
            "contract_validation": validate_contract(),
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    if args.write is None:
        parser.error("--execute requires --write")
    result = run_conformance()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.write.parent.mkdir(parents=True, exist_ok=True)
    args.write.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Verify GREEN and static validation only**

```bash
python -m unittest test_cli.py -v
python run_v0.py --validate-contract
```

Expected validation payload includes `execution_state=UNEXECUTED` and `scientific_result=NONE`.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/run_v0.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_cli.py
git commit -m "feat: gate DTC V0 conformance execution"
```

---

### Task 6: Bind the Implementation to the Refreeze and Add No-Execution CI

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/README.md`
- Create: `.github/workflows/validate-dtc-v0-implementation.yml`

**Interfaces:**
- README records source identity and implementation/execution standing.
- CI checks both source Git blobs, runs unit tests and static validation, preserves the existing frozen-record validator, and refuses result artifacts.

- [ ] **Step 1: Create the README with implementation-in-progress standing**

The README must contain:

```markdown
# Diagnostic Topology Collision V0 — Executable Conformance Implementation

Operative pre-execution refreeze commit: `c650943031831aaa50379dd5dd79515bf681c0f3`

Frozen source blob: `447e5db3f15476406910a32e1d36c0e2364e1344`

Repair-authority addendum blob: `303031bdec77dfffb4a5d6c9bdd2d033f30314ac`

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTATION_IN_PROGRESS
execution_state      = UNEXECUTED
scientific_result    = NONE
```

This implementation instantiates an already-derived finite construction. It may expose conformance failure; it may not change the frozen expected object to accommodate implementation output.

The only legal implementation-phase runner command is:

```bash
python run_v0.py --validate-contract
```

The successful `--execute --write ...` path requires a later explicit authorization.
```

Also document the five Python modules and this lineage:

```text
analytic finite witness
    -> executable implementation
    -> separate execution authorization required
    -> exact conformance reproduction OR conformance failure
```

- [ ] **Step 2: Add the implementation-only workflow**

```yaml
# .github/workflows/validate-dtc-v0-implementation.yml
name: Validate DTC V0 implementation without conformance execution

on:
  push:
    paths:
      - "experiments/research_seeds/diagnostic_topology_collision_v0/**"
      - "docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md"
      - "docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md"
      - "docs/superpowers/plans/2026-09-07-diagnostic-topology-collision-v0-conformance.md"
      - ".github/workflows/validate-dtc-v0-implementation.yml"
  pull_request:
    paths:
      - "experiments/research_seeds/diagnostic_topology_collision_v0/**"
      - "docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md"
      - "docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md"
      - "docs/superpowers/plans/2026-09-07-diagnostic-topology-collision-v0-conformance.md"
      - ".github/workflows/validate-dtc-v0-implementation.yml"

permissions:
  contents: read

jobs:
  validate-without-execution:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Bind implementation to refrozen source
        shell: bash
        run: |
          test "$(git hash-object docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md)" = "447e5db3f15476406910a32e1d36c0e2364e1344"
          test "$(git hash-object docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md)" = "303031bdec77dfffb4a5d6c9bdd2d033f30314ac"
      - name: Run unit tests only
        run: |
          cd experiments/research_seeds/diagnostic_topology_collision_v0
          python -m unittest discover -p 'test_*.py' -v
      - name: Validate static contract only
        run: |
          cd experiments/research_seeds/diagnostic_topology_collision_v0
          python run_v0.py --validate-contract > /tmp/dtc_v0_contract.json
          python - <<'PY'
          import json
          with open('/tmp/dtc_v0_contract.json', encoding='utf-8') as handle:
              payload = json.load(handle)
          assert payload['protocol_state'] == 'FROZEN_PRE_EXECUTION_ASSAY'
          assert payload['execution_state'] == 'UNEXECUTED'
          assert payload['scientific_result'] == 'NONE'
          PY
      - name: Refuse implementation-time result artifacts
        shell: bash
        run: test ! -e experiments/research_seeds/diagnostic_topology_collision_v0/results
```

Do not add any workflow invocation of `--execute`.

- [ ] **Step 3: Run all implementation checks locally**

```bash
cd experiments/research_seeds/diagnostic_topology_collision_v0
python -m unittest discover -p 'test_*.py' -v
python run_v0.py --validate-contract > /tmp/dtc_v0_contract.json
cd ../../../..
test "$(git hash-object docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md)" = "447e5db3f15476406910a32e1d36c0e2364e1344"
test "$(git hash-object docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md)" = "303031bdec77dfffb4a5d6c9bdd2d033f30314ac"
test ! -e experiments/research_seeds/diagnostic_topology_collision_v0/results
python scripts/validate_frozen_record.py
```

Expected: all unit tests pass, static validation succeeds, both source-object hashes match, no results directory exists, and the pre-existing frozen-record validator exits `0` unchanged.

- [ ] **Step 4: Commit**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/README.md \
        .github/workflows/validate-dtc-v0-implementation.yml
git commit -m "ci: validate DTC V0 implementation without execution"
```

---

### Task 7: Close at `IMPLEMENTED_NOT_EXECUTED`

**Files:**
- Modify: `experiments/research_seeds/diagnostic_topology_collision_v0/README.md`

**Interfaces:**
- Documentation-state transition only after fresh green implementation validation.

- [ ] **Step 1: Change only the implementation-state line**

Replace:

```text
implementation_state = IMPLEMENTATION_IN_PROGRESS
```

with:

```text
implementation_state = IMPLEMENTED_NOT_EXECUTED
```

The complete block remains:

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state      = UNEXECUTED
scientific_result    = NONE
```

- [ ] **Step 2: Run fresh terminal verification**

```bash
cd experiments/research_seeds/diagnostic_topology_collision_v0
python -m unittest discover -p 'test_*.py' -v
python run_v0.py --validate-contract > /tmp/dtc_v0_contract.json
cd ../../../..
python scripts/validate_frozen_record.py
test "$(git hash-object docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md)" = "447e5db3f15476406910a32e1d36c0e2364e1344"
test "$(git hash-object docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md)" = "303031bdec77dfffb4a5d6c9bdd2d033f30314ac"
test ! -e experiments/research_seeds/diagnostic_topology_collision_v0/results
git status --short
```

Expected: all tests and validators green; both frozen source identities exact; no result artifact exists; only the intentional README state change remains uncommitted.

- [ ] **Step 3: Audit the implementation diff before closure**

```bash
git diff c650943031831aaa50379dd5dd79515bf681c0f3..HEAD -- \
  experiments/research_seeds/diagnostic_topology_collision_v0 \
  .github/workflows/validate-dtc-v0-implementation.yml
```

Confirm from the diff:

```text
no committed results directory
no committed result JSON
no CI execution call
no frozen source-spec mutation
no expected-value rewrite derived from implementation output
```

If any condition fails, implementation completion is blocked.

- [ ] **Step 4: Commit terminal implementation standing**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/README.md
git commit -m "docs: bind DTC V0 implementation to unexecuted state"
```

- [ ] **Step 5: Require fresh CI on that exact terminal commit**

Before claiming implementation completion, require:

```text
Validate DTC V0 implementation without conformance execution = SUCCESS
Validate frozen record                                      = SUCCESS
```

A green run from an earlier commit does not qualify.

---

## Implementation Completion Boundary

At completion of this plan, the strongest authorized statement is:

```text
The executable implementation is statically bound to the refrozen DTC-V0 object and is implemented but unexecuted. A separately authorized exhaustive conformance run may reproduce the already-derived finite behavior or expose implementation/protocol failure.
```

This plan does not authorize an assay result, empirical-confirmation language, canonical promotion, Interface Theory/MATRIX translation, V1 evidence, or any general representation/corrigibility claim.

Any later execution authorization must name the exact implementation commit being executed, preserve both frozen source-object blob identities, and treat deviation from `4/8`, `8/8`, and `delta=0.5` as conformance failure rather than permission to revise the benchmark after seeing implementation behavior.
