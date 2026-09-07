# Diagnostic Topology Collision V0 Conformance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an executable conformance implementation of the already-refrozen `DIAGNOSTIC_TOPOLOGY_COLLISION_V0` finite construction without changing its world, policy, representation, resource, controller, analytic-count, or claim semantics.

**Architecture:** Implement the frozen object as a small standard-library Python package under `experiments/research_seeds/diagnostic_topology_collision_v0/`. Separate world/resource semantics, representation/controller semantics, viable-initial-action analysis, and exhaustive execution so static contract validation can run during implementation without performing the scientific conformance run. Expose execution only behind an explicit `--execute --write <path>` gate; implementation and CI must use `--validate-contract` only.

**Tech Stack:** Python 3.12 standard library, `unittest`, GitHub Actions.

**Spec:** `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`

## Global Constraints

- Operative pre-execution refreeze commit: `c650943031831aaa50379dd5dd79515bf681c0f3`.
- Frozen DTC-V0 spec Git blob: `447e5db3f15476406910a32e1d36c0e2364e1344`.
- Frozen pre-execution repair-authority addendum Git blob: `303031bdec77dfffb4a5d6c9bdd2d033f30314ac`.
- The implementation branch must descend from the commit containing this plan and therefore retain `c650943031831aaa50379dd5dd79515bf681c0f3` in ancestry.
- Recommended implementation branch: `impl/diagnostic-topology-collision-v0-conformance`.
- Use an isolated worktree at execution time.
- Do not modify `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md` during implementation.
- Do not modify `docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md` during implementation.
- Do not modify canonical Interface Theory artifacts, frozen Gate 013/014 artifacts, MATRIX artifacts, or any canonical/evidence ledger.
- Do not alter the frozen worlds, diagnostics, repairs, costs, budget, histories, encoders, controller mapping, episode family, analytic counts, or claim ceiling to accommodate implementation behavior.
- The executable may reveal a conformance failure; it may not redefine the frozen analytic object to make the implementation pass.
- Frozen worlds: `G_A`, `G_B`; fault set: `{0,1}`.
- Frozen diagnostic map: in `G_A`, `q_A -> f`, `q_B -> bottom`; in `G_B`, `q_B -> f`, `q_A -> bottom`.
- Frozen repairs: `R(0)={r_0}`, `R(1)={r_1}`; no state-independent repair exists while fault remains unresolved.
- Frozen budget: `B=2`; diagnostic cost `1`; repair cost `1`.
- Frozen raw history: `h=(t,n)` with `t(A)=0`, `t(B)=1`, nuisance `n in {0,1}`, and no fault value in history.
- Frozen encoders: `g_0(h)=n`; `g_1(h)=t`; both expose one bit.
- Frozen controller: retained bit `0 -> q_A`; retained bit `1 -> q_B`; diagnostic value `y in {0,1} -> r_y`.
- Viable-policy result must be represented as nonempty policy classes with incompatible required initial actions, not as syntactic singleton policy sets.
- The representation intervention changes controller-visible viable-policy selectability; it does not change the underlying viable-policy classes.
- Frozen exhaustive family: `tau in {A,B}`, `f in {0,1}`, `n in {0,1}` = exactly `8` episodes per representation condition.
- Frozen analytic values: `success_count_g0=4`, `success_count_g1=8`, `wrong_probe_count_g0=4`, `wrong_probe_count_g1=0`, `P_success_g0=0.5`, `P_success_g1=1.0`, `delta_P_success=0.5`.
- Implementation-phase unit tests may exercise individual components and representative episodes, but must not invoke the full exhaustive `run_conformance()` entry point or write a scientific result artifact.
- During implementation, never invoke the CLI with `--execute`.
- During implementation, do not create `experiments/research_seeds/diagnostic_topology_collision_v0/results/` and do not create any DTC-V0 result JSON.
- Terminal implementation state before execution authorization must be exactly:

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state      = UNEXECUTED
scientific_result    = NONE
```

---

## File Structure

Create exactly this implementation surface:

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

Do **not** create a `results/` directory during implementation.

Responsibilities:

- `protocol.py`: frozen world/action/resource semantics only.
- `representation.py`: raw history, `g_0`, `g_1`, and fixed controller only.
- `viability.py`: finite proof-by-enumeration of the required viable initial action in each world; no singleton-policy claim.
- `conformance.py`: representative episode execution helpers, static contract validation, and the full exhaustive `run_conformance()` function. The full function exists but is not invoked during implementation.
- `run_v0.py`: hard CLI separation between static validation and explicitly authorized execution.
- `README.md`: provenance, frozen source identity, implementation/execution state, and command discipline.
- `.github/workflows/validate-dtc-v0-implementation.yml`: source-binding checks, unit tests, static contract validation, and no-result-artifact guard. It must not run `--execute`.

---

### Task 1: Freeze World, Action, Repair, and Resource Semantics in Code

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/protocol.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_protocol.py`

**Interfaces:**
- Produces: `Topology`, `Diagnostic`, `Repair`, `Action`, `FAULTS`, `TOPOLOGY_BIT`, `ACTIONS`, `BUDGET`, `DIAGNOSTIC_COST`, `REPAIR_COST`, `probe()`, `valid_repair()`.
- Later tasks must import these definitions rather than redefining the finite world.

- [ ] **Step 1: Write the failing protocol tests**

Create `test_protocol.py`:

```python
import unittest

from protocol import (
    ACTIONS,
    BUDGET,
    DIAGNOSTIC_COST,
    FAULTS,
    REPAIR_COST,
    TOPOLOGY_BIT,
    Diagnostic,
    Repair,
    Topology,
    probe,
    valid_repair,
)


class ProtocolTests(unittest.TestCase):
    def test_frozen_resource_contract(self):
        self.assertEqual(BUDGET, 2)
        self.assertEqual(DIAGNOSTIC_COST, 1)
        self.assertEqual(REPAIR_COST, 1)
        self.assertEqual(FAULTS, (0, 1))

    def test_topology_bits_are_frozen(self):
        self.assertEqual(TOPOLOGY_BIT[Topology.A], 0)
        self.assertEqual(TOPOLOGY_BIT[Topology.B], 1)

    def test_shared_action_vocabulary_is_exact(self):
        self.assertEqual(
            ACTIONS,
            (
                Diagnostic.QA,
                Diagnostic.QB,
                Repair.R0,
                Repair.R1,
                "stop",
            ),
        )

    def test_ga_diagnostic_topology(self):
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 0), 0)
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 1), 1)
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 0))
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 1))

    def test_gb_diagnostic_topology(self):
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 0), 0)
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 1), 1)
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 0))
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 1))

    def test_repairs_are_fault_specific(self):
        self.assertTrue(valid_repair(0, Repair.R0))
        self.assertTrue(valid_repair(1, Repair.R1))
        self.assertFalse(valid_repair(0, Repair.R1))
        self.assertFalse(valid_repair(1, Repair.R0))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the protocol tests and verify RED**

Run:

```bash
cd experiments/research_seeds/diagnostic_topology_collision_v0
python -m unittest test_protocol.py -v
```

Expected: import failure because `protocol.py` does not yet exist.

- [ ] **Step 3: Implement the minimal frozen protocol**

Create `protocol.py`:

```python
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
    Diagnostic.QA,
    Diagnostic.QB,
    Repair.R0,
    Repair.R1,
    "stop",
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

`None` is the executable representation of the frozen `bottom` observation. Do not attach additional semantics to it.

- [ ] **Step 4: Run the protocol tests and verify GREEN**

Run:

```bash
python -m unittest test_protocol.py -v
```

Expected: `6` tests pass.

- [ ] **Step 5: Commit Task 1**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/protocol.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_protocol.py
git commit -m "test: encode DTC V0 frozen world contract"
```

---

### Task 2: Encode the Matched One-Bit Representation Intervention and Fixed Controller

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/representation.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_representation.py`

**Interfaces:**
- Consumes: `Topology`, `TOPOLOGY_BIT`, `Diagnostic` from `protocol.py`.
- Produces: `RawHistory`, `make_history()`, `g0()`, `g1()`, `select_diagnostic()`.

- [ ] **Step 1: Write the failing representation tests**

Create `test_representation.py`:

```python
import unittest

from protocol import Diagnostic, Topology
from representation import RawHistory, g0, g1, make_history, select_diagnostic


class RepresentationTests(unittest.TestCase):
    def test_same_raw_history_object_can_feed_both_encoders(self):
        history = make_history(Topology.A, 1)
        self.assertEqual(history, RawHistory(topology_bit=0, nuisance=1))
        self.assertEqual(g0(history), 1)
        self.assertEqual(g1(history), 0)

    def test_g0_collapses_matched_topology_pair(self):
        for nuisance in (0, 1):
            h_a = make_history(Topology.A, nuisance)
            h_b = make_history(Topology.B, nuisance)
            self.assertEqual(g0(h_a), g0(h_b))

    def test_g1_preserves_topology_bit(self):
        for nuisance in (0, 1):
            self.assertEqual(g1(make_history(Topology.A, nuisance)), 0)
            self.assertEqual(g1(make_history(Topology.B, nuisance)), 1)

    def test_both_encoders_emit_exactly_one_binary_value(self):
        for topology in (Topology.A, Topology.B):
            for nuisance in (0, 1):
                history = make_history(topology, nuisance)
                self.assertIn(g0(history), (0, 1))
                self.assertIn(g1(history), (0, 1))

    def test_fixed_controller_mapping(self):
        self.assertIs(select_diagnostic(0), Diagnostic.QA)
        self.assertIs(select_diagnostic(1), Diagnostic.QB)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the representation tests and verify RED**

Run:

```bash
python -m unittest test_representation.py -v
```

Expected: import failure because `representation.py` does not exist.

- [ ] **Step 3: Implement the minimal representation/controller module**

Create `representation.py`:

```python
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
    return RawHistory(topology_bit=TOPOLOGY_BIT[topology], nuisance=nuisance)


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

Do not add fault information, topology labels, model IDs, or condition-specific controller code.

- [ ] **Step 4: Run the representation tests and verify GREEN**

Run:

```bash
python -m unittest test_representation.py -v
```

Expected: `5` tests pass.

- [ ] **Step 5: Commit Task 2**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/representation.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_representation.py
git commit -m "test: encode DTC V0 representation intervention"
```

---

### Task 3: Verify Viable-Policy Collision Through Required Initial Actions

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/viability.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_viability.py`

**Interfaces:**
- Consumes: world/action/resource primitives from `protocol.py`.
- Produces: `initial_action_supports_zero_error()`, `viable_initial_actions()`.
- This module verifies the repaired claim `all viable policies in G_A start q_A` and `all viable policies in G_B start q_B` without enumerating or claiming singleton policy syntax.

- [ ] **Step 1: Write the failing viability tests**

Create `test_viability.py`:

```python
import unittest

from protocol import Diagnostic, Repair, Topology
from viability import initial_action_supports_zero_error, viable_initial_actions


class ViabilityTests(unittest.TestCase):
    def test_ga_has_exactly_one_zero_error_viable_initial_action(self):
        self.assertEqual(
            viable_initial_actions(Topology.A),
            frozenset({Diagnostic.QA}),
        )

    def test_gb_has_exactly_one_zero_error_viable_initial_action(self):
        self.assertEqual(
            viable_initial_actions(Topology.B),
            frozenset({Diagnostic.QB}),
        )

    def test_wrong_probe_has_no_bounded_zero_error_continuation(self):
        self.assertFalse(
            initial_action_supports_zero_error(Topology.A, Diagnostic.QB)
        )
        self.assertFalse(
            initial_action_supports_zero_error(Topology.B, Diagnostic.QA)
        )

    def test_terminal_repair_or_stop_cannot_guarantee_both_faults(self):
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

- [ ] **Step 2: Run the viability tests and verify RED**

Run:

```bash
python -m unittest test_viability.py -v
```

Expected: import failure because `viability.py` does not exist.

- [ ] **Step 3: Implement the bounded initial-action analysis**

Create `viability.py`:

```python
from __future__ import annotations

from collections import defaultdict

from protocol import (
    ACTIONS,
    DIAGNOSTIC_COST,
    FAULTS,
    REPAIR_COST,
    Action,
    Diagnostic,
    Repair,
    Topology,
    probe,
    valid_repair,
)


def _group_faults_by_observation(
    topology: Topology,
    diagnostic: Diagnostic,
) -> dict[int | None, tuple[int, ...]]:
    grouped: dict[int | None, list[int]] = defaultdict(list)
    for fault in FAULTS:
        grouped[probe(topology, diagnostic, fault)].append(fault)
    return {observation: tuple(faults) for observation, faults in grouped.items()}


def _one_repair_handles_all(faults: tuple[int, ...]) -> bool:
    return any(
        all(valid_repair(fault, repair) for fault in faults)
        for repair in (Repair.R0, Repair.R1)
    )


def initial_action_supports_zero_error(topology: Topology, action: Action) -> bool:
    if isinstance(action, Diagnostic):
        remaining_budget = 2 - DIAGNOSTIC_COST
        if remaining_budget < REPAIR_COST:
            return False
        groups = _group_faults_by_observation(topology, action)
        return all(_one_repair_handles_all(faults) for faults in groups.values())

    if isinstance(action, Repair):
        return all(valid_repair(fault, action) for fault in FAULTS)

    if action == "stop":
        return False

    raise ValueError(f"unknown action: {action!r}")


def viable_initial_actions(topology: Topology) -> frozenset[Action]:
    return frozenset(
        action
        for action in ACTIONS
        if initial_action_supports_zero_error(topology, action)
    )
```

This is a finite initial-action viability check. It does not assert that the entire viable-policy class contains only one syntactic policy.

- [ ] **Step 4: Run the viability tests and verify GREEN**

Run:

```bash
python -m unittest test_viability.py -v
```

Expected: `5` tests pass.

- [ ] **Step 5: Commit Task 3**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/viability.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_viability.py
git commit -m "test: verify DTC V0 viable initial-action collision"
```

---

### Task 4: Build Episode Semantics, Static Contract Validation, and the Dormant Exhaustive Runner

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/conformance.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_conformance.py`

**Interfaces:**
- Consumes: all frozen modules from Tasks 1-3.
- Produces: `Condition`, `EpisodeSpec`, `EpisodeResult`, `episode_specs()`, `run_episode()`, `validate_contract()`, `run_conformance()`.
- `validate_contract()` must not call `run_conformance()`.
- Unit tests must not call `run_conformance()` during implementation.

- [ ] **Step 1: Write the failing conformance-component tests**

Create `test_conformance.py`:

```python
import unittest

from conformance import (
    Condition,
    EpisodeSpec,
    episode_specs,
    run_episode,
    validate_contract,
)
from protocol import Diagnostic, Topology


class ConformanceComponentTests(unittest.TestCase):
    def test_episode_family_has_exactly_eight_specs(self):
        specs = episode_specs()
        self.assertEqual(len(specs), 8)
        self.assertEqual(
            {(spec.topology, spec.fault, spec.nuisance) for spec in specs},
            {
                (topology, fault, nuisance)
                for topology in (Topology.A, Topology.B)
                for fault in (0, 1)
                for nuisance in (0, 1)
            },
        )

    def test_g1_representative_episode_selects_world_viable_probe_and_repairs(self):
        result = run_episode(
            Condition.G1,
            EpisodeSpec(Topology.B, fault=1, nuisance=0),
        )
        self.assertIs(result.diagnostic, Diagnostic.QB)
        self.assertEqual(result.observation, 1)
        self.assertTrue(result.repair_success)
        self.assertEqual(result.budget_remaining, 0)

    def test_g0_representative_wrong_probe_exposes_no_bounded_continuation(self):
        result = run_episode(
            Condition.G0,
            EpisodeSpec(Topology.B, fault=0, nuisance=0),
        )
        self.assertIs(result.diagnostic, Diagnostic.QA)
        self.assertIsNone(result.observation)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")
        self.assertEqual(result.budget_remaining, 1)

    def test_static_contract_validator_reports_frozen_prerequisites_only(self):
        contract = validate_contract()
        self.assertEqual(contract["positive_episode_count_per_condition"], 8)
        self.assertTrue(contract["viable_policy_initial_action_collision_verified"])
        self.assertTrue(contract["representation_capacity_matched"])
        self.assertTrue(contract["controller_identity_matched"])
        self.assertTrue(contract["primitive_actions_matched"])
        self.assertTrue(contract["budget_matched"])
        self.assertTrue(contract["raw_history_contract_verified"])
        self.assertTrue(contract["controller_selectability_contract_verified"])


if __name__ == "__main__":
    unittest.main()
```

These tests deliberately cover only representative episodes. They do not invoke the exhaustive `run_conformance()` function and do not produce aggregate scientific-result counts.

- [ ] **Step 2: Run the component tests and verify RED**

Run:

```bash
python -m unittest test_conformance.py -v
```

Expected: import failure because `conformance.py` does not exist.

- [ ] **Step 3: Implement episode semantics and static contract validation**

Create `conformance.py` with these exact public types and functions:

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from protocol import (
    ACTIONS,
    BUDGET,
    DIAGNOSTIC_COST,
    FAULTS,
    REPAIR_COST,
    Diagnostic,
    Repair,
    Topology,
    probe,
    valid_repair,
)
from representation import g0, g1, make_history, select_diagnostic
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
    retained_bit: int
    diagnostic: Diagnostic
    observation: int | None
    repair: Repair | None
    budget_remaining: int
    wrong_probe: bool
    repair_success: bool
    failure: str | None


EXPECTED_RESULT = {
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


def run_episode(condition: Condition, spec: EpisodeSpec) -> EpisodeResult:
    raw_history = make_history(spec.topology, spec.nuisance)
    retained_bit = g0(raw_history) if condition is Condition.G0 else g1(raw_history)
    diagnostic = select_diagnostic(retained_bit)
    required = _required_diagnostic(spec.topology)
    wrong_probe = diagnostic is not required
    budget = BUDGET - DIAGNOSTIC_COST
    observation = probe(spec.topology, diagnostic, spec.fault)

    if observation is None:
        return EpisodeResult(
            condition,
            spec.topology,
            spec.fault,
            spec.nuisance,
            retained_bit,
            diagnostic,
            None,
            None,
            budget,
            wrong_probe,
            False,
            "NO_BOUNDED_ZERO_ERROR_CONTINUATION",
        )

    repair = Repair.R0 if observation == 0 else Repair.R1
    if budget < REPAIR_COST:
        raise ConformanceFailure("fault resolved but repair budget unavailable")
    budget -= REPAIR_COST
    success = valid_repair(spec.fault, repair)
    return EpisodeResult(
        condition,
        spec.topology,
        spec.fault,
        spec.nuisance,
        retained_bit,
        diagnostic,
        observation,
        repair,
        budget,
        wrong_probe,
        success,
        None if success else "INVALID_REPAIR",
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
    if ACTIONS != (
        Diagnostic.QA,
        Diagnostic.QB,
        Repair.R0,
        Repair.R1,
        "stop",
    ):
        raise ConformanceFailure("primitive action vocabulary changed")
    if (BUDGET, DIAGNOSTIC_COST, REPAIR_COST) != (2, 1, 1):
        raise ConformanceFailure("resource contract changed")

    raw_history_contract = all(
        make_history(topology, nuisance).topology_bit
        == (0 if topology is Topology.A else 1)
        for topology in (Topology.A, Topology.B)
        for nuisance in (0, 1)
    )
    if not raw_history_contract:
        raise ConformanceFailure("raw history contract changed")

    controller_selectability = (
        select_diagnostic(g1(make_history(Topology.A, 0))) is Diagnostic.QA
        and select_diagnostic(g1(make_history(Topology.B, 0))) is Diagnostic.QB
        and g0(make_history(Topology.A, 0)) == g0(make_history(Topology.B, 0))
        and g0(make_history(Topology.A, 1)) == g0(make_history(Topology.B, 1))
    )
    if not controller_selectability:
        raise ConformanceFailure("controller-selectability contract changed")

    return {
        "positive_episode_count_per_condition": 8,
        "viable_policy_initial_action_collision_verified": True,
        "representation_capacity_matched": True,
        "controller_identity_matched": True,
        "primitive_actions_matched": True,
        "budget_matched": True,
        "raw_history_contract_verified": True,
        "controller_selectability_contract_verified": True,
    }
```

Then append the dormant exhaustive runner below. Do not invoke it during implementation:

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
    specs = episode_specs()
    g0_results = tuple(run_episode(Condition.G0, spec) for spec in specs)
    g1_results = tuple(run_episode(Condition.G1, spec) for spec in specs)
    g0_summary = _aggregate(g0_results)
    g1_summary = _aggregate(g1_results)
    observed = {
        "total_worlds": len(specs),
        "success_count_g0": g0_summary["success_count"],
        "success_count_g1": g1_summary["success_count"],
        "wrong_probe_count_g0": g0_summary["wrong_probe_count"],
        "wrong_probe_count_g1": g1_summary["wrong_probe_count"],
        "P_success_g0": g0_summary["P_success"],
        "P_success_g1": g1_summary["P_success"],
        "delta_P_success": g1_summary["P_success"] - g0_summary["P_success"],
    }
    if observed != EXPECTED_RESULT:
        raise ConformanceFailure(
            f"implementation does not conform to frozen analytic object: {observed!r}"
        )
    return {
        "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
        "implementation_state": "IMPLEMENTED",
        "execution_state": "EXECUTED_CONFORMANCE",
        "scientific_result": "ANALYTIC_OBJECT_REPRODUCED_BY_EXECUTABLE_CONFORMANCE",
        **observed,
        **validate_contract(),
    }
```

The critical behavior is fail-closed: any mismatch raises `ConformanceFailure`; no expected value may be updated from observed implementation behavior.

- [ ] **Step 4: Run only the component tests and verify GREEN**

Run:

```bash
python -m unittest test_conformance.py -v
```

Expected: `4` tests pass.

Do **not** run `run_conformance()` in this task.

- [ ] **Step 5: Commit Task 4**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/conformance.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_conformance.py
git commit -m "feat: add dormant DTC V0 conformance runner"
```

---

### Task 5: Add an Explicit Validation-vs-Execution CLI Gate

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/run_v0.py`
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/test_cli.py`

**Interfaces:**
- Consumes: `validate_contract()` and `run_conformance()` from `conformance.py`.
- Produces: CLI modes `--validate-contract` and `--execute`.
- `--execute` requires `--write`; `--write` is rejected with validation mode.
- The implementation workflow will call validation mode only.

- [ ] **Step 1: Write the failing CLI tests**

Create `test_cli.py`:

```python
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "run_v0.py"


class CliTests(unittest.TestCase):
    def test_validate_contract_reports_unexecuted_state_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "result.json"
            proc = subprocess.run(
                [sys.executable, str(RUNNER), "--validate-contract"],
                check=True,
                capture_output=True,
                text=True,
                cwd=ROOT,
            )
            payload = json.loads(proc.stdout)
            self.assertEqual(payload["execution_state"], "UNEXECUTED")
            self.assertEqual(payload["scientific_result"], "NONE")
            self.assertFalse(target.exists())

    def test_validate_contract_rejects_write_path(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--validate-contract", "--write", "x.json"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--write is valid only with --execute", proc.stderr)

    def test_execute_requires_explicit_write_path(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--execute"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--execute requires --write", proc.stderr)


if __name__ == "__main__":
    unittest.main()
```

These tests must not invoke a successful `--execute` path.

- [ ] **Step 2: Run the CLI tests and verify RED**

Run:

```bash
python -m unittest test_cli.py -v
```

Expected: failure because `run_v0.py` does not exist.

- [ ] **Step 3: Implement the gated CLI**

Create `run_v0.py`:

```python
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

The presence of the execution code is not execution authorization. No successful `--execute` command is legal during this plan.

- [ ] **Step 4: Run the CLI tests and verify GREEN**

Run:

```bash
python -m unittest test_cli.py -v
```

Expected: `3` tests pass.

Then run static validation only:

```bash
python run_v0.py --validate-contract
```

Expected JSON includes:

```json
{
  "execution_state": "UNEXECUTED",
  "implementation_state": "VALIDATED_NOT_EXECUTED",
  "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
  "scientific_result": "NONE"
}
```

with an additional `contract_validation` object.

- [ ] **Step 5: Commit Task 5**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/run_v0.py \
        experiments/research_seeds/diagnostic_topology_collision_v0/test_cli.py
git commit -m "feat: gate DTC V0 conformance execution"
```

---

### Task 6: Bind Implementation to the Refrozen Source and Add No-Execution CI

**Files:**
- Create: `experiments/research_seeds/diagnostic_topology_collision_v0/README.md`
- Create: `.github/workflows/validate-dtc-v0-implementation.yml`

**Interfaces:**
- README records exact refreeze/source identity and terminal scientific standing.
- CI proves the spec/addendum files are byte-identical in Git-object identity to the operative refreeze, runs all unit tests, runs static validation only, and fails if an implementation-time results directory exists.

- [ ] **Step 1: Create the implementation README in pre-terminal form**

Create `README.md` with exactly this standing block near the top:

```markdown
# Diagnostic Topology Collision V0 — Executable Conformance Implementation

Source scientific object: `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`

Operative pre-execution refreeze commit: `c650943031831aaa50379dd5dd79515bf681c0f3`

Frozen source blob: `447e5db3f15476406910a32e1d36c0e2364e1344`

Repair-authority addendum blob: `303031bdec77dfffb4a5d6c9bdd2d033f30314ac`

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTATION_IN_PROGRESS
execution_state      = UNEXECUTED
scientific_result    = NONE
```

This directory implements an already-derived finite construction. It does not redesign the benchmark and does not create a new empirical hypothesis.

The implementation must fail if executable behavior diverges from the frozen analytic values. The frozen values must never be edited to match implementation output.

During implementation, the only legal runner command is:

```bash
python run_v0.py --validate-contract
```

The `--execute --write ...` path exists for a later separately authorized conformance run and must not be invoked during implementation.

No `results/` directory or result JSON belongs in this implementation state.
```

Append a short file-role table for `protocol.py`, `representation.py`, `viability.py`, `conformance.py`, and `run_v0.py`, plus the claim boundary:

```text
analytic finite witness established
        -> executable implementation
        -> [future explicit execution authorization required]
        -> exact reproduction OR conformance failure
```

- [ ] **Step 2: Create the no-execution workflow**

Create `.github/workflows/validate-dtc-v0-implementation.yml`:

```yaml
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
      - name: Bind implementation to refrozen DTC source
        shell: bash
        run: |
          test "$(git hash-object docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md)" = "447e5db3f15476406910a32e1d36c0e2364e1344"
          test "$(git hash-object docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md)" = "303031bdec77dfffb4a5d6c9bdd2d033f30314ac"
      - name: Run implementation unit tests only
        run: |
          cd experiments/research_seeds/diagnostic_topology_collision_v0
          python -m unittest discover -p 'test_*.py' -v
      - name: Validate static contract without execution
        run: |
          cd experiments/research_seeds/diagnostic_topology_collision_v0
          python run_v0.py --validate-contract > /tmp/dtc_v0_contract.json
          python - <<'PY'
          import json
          payload = json.load(open('/tmp/dtc_v0_contract.json', encoding='utf-8'))
          assert payload['protocol_state'] == 'FROZEN_PRE_EXECUTION_ASSAY'
          assert payload['execution_state'] == 'UNEXECUTED'
          assert payload['scientific_result'] == 'NONE'
          PY
      - name: Refuse implementation-time result artifacts
        shell: bash
        run: |
          test ! -e experiments/research_seeds/diagnostic_topology_collision_v0/results
```

Do not add a workflow step invoking `--execute`.

- [ ] **Step 3: Run all implementation tests locally**

Run:

```bash
cd experiments/research_seeds/diagnostic_topology_collision_v0
python -m unittest discover -p 'test_*.py' -v
python run_v0.py --validate-contract > /tmp/dtc_v0_contract.json
python - <<'PY'
import json
payload = json.load(open('/tmp/dtc_v0_contract.json', encoding='utf-8'))
assert payload['protocol_state'] == 'FROZEN_PRE_EXECUTION_ASSAY'
assert payload['execution_state'] == 'UNEXECUTED'
assert payload['scientific_result'] == 'NONE'
PY
cd ../../../..
test "$(git hash-object docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md)" = "447e5db3f15476406910a32e1d36c0e2364e1344"
test "$(git hash-object docs/superpowers/specs/2026-09-07-diagnostic-topology-collision-v0-preexecution-repair.md)" = "303031bdec77dfffb4a5d6c9bdd2d033f30314ac"
test ! -e experiments/research_seeds/diagnostic_topology_collision_v0/results
```

Expected: all unit tests pass; validation assertions pass; both source-object hash checks pass; no results directory exists.

- [ ] **Step 4: Run the repository's pre-existing frozen-record validator unchanged**

Run:

```bash
python scripts/validate_frozen_record.py
```

Expected: exit code `0`.

Do not modify the validator to accommodate DTC implementation behavior.

- [ ] **Step 5: Commit Task 6**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/README.md \
        .github/workflows/validate-dtc-v0-implementation.yml
git commit -m "ci: validate DTC V0 implementation without execution"
```

---

### Task 7: Close Implementation at `IMPLEMENTED_NOT_EXECUTED`

**Files:**
- Modify: `experiments/research_seeds/diagnostic_topology_collision_v0/README.md`

**Interfaces:**
- Changes documentation standing only after all implementation checks are green.
- Does not run the exhaustive conformance function and does not produce a result artifact.

- [ ] **Step 1: Replace only the implementation-state line in README**

Change:

```text
implementation_state = IMPLEMENTATION_IN_PROGRESS
```

to:

```text
implementation_state = IMPLEMENTED_NOT_EXECUTED
```

The complete terminal block must read:

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state      = UNEXECUTED
scientific_result    = NONE
```

- [ ] **Step 2: Run the complete implementation verification suite fresh**

Run:

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

Expected:

- all DTC-V0 unit tests pass;
- static contract validation succeeds with `execution_state=UNEXECUTED` and `scientific_result=NONE`;
- frozen-record validator exits `0`;
- both source-object Git blob identities remain exact;
- no results directory exists;
- `git status --short` shows only the intentional README state change before commit.

- [ ] **Step 3: Verify the exhaustive execution path was never invoked in implementation history**

Run:

```bash
git diff c650943031831aaa50379dd5dd79515bf681c0f3..HEAD -- \
  experiments/research_seeds/diagnostic_topology_collision_v0 \
  .github/workflows/validate-dtc-v0-implementation.yml \
  docs/superpowers/plans/2026-09-07-diagnostic-topology-collision-v0-conformance.md
```

Review specifically for:

```text
no committed results directory
no committed result JSON
no CI invocation of --execute
no source-spec mutation
no expected-value rewrite derived from observed output
```

If any of those are present, stop and repair the implementation boundary before closing.

- [ ] **Step 4: Commit the terminal implementation state**

```bash
git add experiments/research_seeds/diagnostic_topology_collision_v0/README.md
git commit -m "docs: bind DTC V0 implementation to unexecuted state"
```

- [ ] **Step 5: Wait for both CI lanes on the exact terminal commit**

Required green evidence before calling implementation complete:

```text
Validate DTC V0 implementation without conformance execution = SUCCESS
Validate frozen record                                      = SUCCESS
```

Do not infer success from a previous commit's workflow run.

---

## Implementation Completion Boundary

At the end of this plan, the only authorized conclusion is:

```text
The executable implementation conforms statically to the refrozen DTC-V0 specification and is ready for a separately authorized exhaustive conformance run.
```

The plan does **not** authorize saying:

```text
DTC-V0 executed
DTC-V0 empirically confirmed
DTC-V0 discovered delta=0.5
representation generally improves correction
Interface Theory and MATRIX are translated
V1 is supported by V0 execution
```

A later execution authorization must name the exact implementation commit to be run, must preserve the frozen source-object blob identities above, and must treat any deviation from the analytic `4/8`, `8/8`, `0.5` contract as implementation/protocol failure rather than evidence for a revised benchmark.
