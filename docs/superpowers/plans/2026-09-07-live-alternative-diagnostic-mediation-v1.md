# Live-Alternative Diagnostic Mediation V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the frozen `LIVE_ALTERNATIVE_DIAGNOSTIC_MEDIATION_V1` finite assay machinery without executing the scientific assay, while preserving the design’s causal separation between isolated marginal access and temporary joint relation computation.

**Architecture:** The implementation is a small, deterministic Python 3.12 research-assay package under `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/`. World definitions and frozen constants live in `protocol.py`; the causal intervention lives in `mediation.py`; episode composition, resource accounting, validation, and result aggregation live in `assay.py`; `run_v1.py` exposes two explicitly separated modes: structural validation and scientific execution. Unit tests and CI exercise only component behavior and `--validate-contract`; they must never invoke the full frozen V1 execution path during implementation.

**Tech Stack:** Python 3.12 standard library only (`dataclasses`, `enum`, `argparse`, `json`, `unittest`, `subprocess`, `pathlib`), Git, existing `scripts/validate_frozen_record.py`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md`

## Global Constraints

- The approved design commit is `1f646397d76b04c96afa22815bc78957b561c81b` on `design/live-alternative-diagnostic-mediation-v1`.
- At execution time, create `impl/live-alternative-diagnostic-mediation-v1` from the exact approved plan commit; do not implement directly on the parent research branch.
- `LIVE_ALTERNATIVE_DIAGNOSTIC_MEDIATION_V1` remains `NONCANONICAL_RESEARCH_SEED` with `NO_TRANSLATION_EARNED`.
- Before scientific execution, evidence standing remains `EXPERIMENTAL_HYPOTHESIS` plus finite analytic consequences of the frozen design; there is no empirical V1 result.
- V1 adds exactly one causal responsibility beyond V0: `temporary relation between retained alternatives -> information-producing action`.
- Both conditions already retain the same live alternatives and the same per-alternative predictive signatures. V1 receives no credit for preservation.
- Shared diagnostic menu is exactly `q0`, `q1`; no diagnostic invention or composition is allowed.
- Positive model signatures are exactly `M00=(0,0)`, `M01=(0,1)`, `M10=(1,0)`, `M11=(1,1)`.
- Positive live pairs are exactly the four square edges; square diagonals are outside the frozen family.
- Each positive pair has exactly one discriminating diagnostic, and no endpoint alone determines which diagnostic is useful over all pairs containing that endpoint.
- C0 diagnostic selection is pair-blind and fixed to `q0`; C0 contains no pre-action node with both marginal streams as causal parents.
- C1 may compute only an intervention-local, read-only, permutation-symmetric comparison of the two marginal signatures.
- C1 comparator output contract is exact: `(1,0)->q0`, `(0,1)->q1`, `(0,0)->NO_DISCRIMINATING_DIAGNOSTIC`, `(1,1)->OUT_OF_FROZEN_FAMILY`.
- The mediator may not modify either alternative before external evidence, may not persist state, and may not update parameters.
- Only the external world supplies evidence about which live alternative is true.
- Every positive latent model has a unique terminal repair. Total budget is exactly `B=2`; every diagnostic costs `1`; every repair costs `1`.
- Under the frozen controller/resolver contract, a non-discriminating positive-family probe leaves no bounded zero-error continuation.
- Positive-family analytic values are frozen by design: `P_disc(C0)=0.5`, `P_disc(C1)=1.0`, `P_repair(C0)=0.5`, `P_repair(C1)=1.0`.
- Null pair is exactly two distinct latent worlds with identical signature `(0,0)` and distinct repairs; C1 must return `NO_DISCRIMINATING_DIAGNOSTIC` before acting.
- Implementation validation must not be interpreted as assay execution or as empirical evidence.
- Do not invoke the scientific execution mode during implementation. In particular, do not run `run_v1.py --execute ...`.
- Do not create or commit a V1 result JSON, result summary, result ledger entry, evidence-index entry, or gate-registry entry during implementation.
- Do not modify `docs/CANONICAL_RECORD.md`, `docs/RESULT_LEDGER.md`, `docs/EVIDENCE_INDEX.md`, `docs/protocol_foundations.md`, `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md`, `FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md`, Gate 013, Gate 014, or `scripts/validate_frozen_record.py`.
- Do not convert V1 into Gate 015. It remains a noncanonical research-seed assay.
- Use no third-party Python dependency.

---

## File Structure

**Create:**
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py` — frozen models, signatures, repairs, positive-pair family, null pair, budget/action constants, marginal projection, external world response.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py` — C0 pair-blind selector, C1 XOR comparison, exact comparator output contract. This module must not import latent-model registries or pair labels.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py` — condition enum, episode execution, external-evidence resolver, resource accounting, static-contract validation, positive enumeration, aggregation, and the full assay function that remains uninvoked during implementation.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py` — CLI with mutually exclusive `--validate-contract` and `--execute`; `--execute` requires an explicit write path.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py` — square, endpoint non-identifiability, pair family, repair, and null-contract tests.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py` — C0/C1 dependency, XOR, symmetry, null abstention, and out-of-family tests.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py` — representative episode/resource/resolution tests plus synthetic aggregation tests; no full frozen V1 execution.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py` — verifies validation mode cannot call the assay and execution mode requires explicit authorization flags.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md` — status, authority boundary, validation commands, and explicit `UNEXECUTED` state.
- `.github/workflows/validate-v1-implementation.yml` — implementation-only CI that runs unit tests and `--validate-contract`, never `--execute`.

**Do not create during implementation:**
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/results/`
- any `result.json`
- any scientific `summary.md`
- any canonical ledger/index update

---

### Task 1: Establish an isolated implementation baseline

**Files:**
- Read: `docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md`
- Read: `docs/superpowers/plans/2026-09-07-live-alternative-diagnostic-mediation-v1.md`
- Read: `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`
- Read: `scripts/validate_frozen_record.py`
- Read: `.github/workflows/validate-frozen-record.yml`

**Interfaces:**
- Consumes: exact approved plan commit and design spec.
- Produces: clean isolated implementation branch plus before-hashes for protected artifacts.

- [ ] **Step 1: Create an isolated worktree from the exact approved plan commit**

After this plan is committed, replace `<PLAN_COMMIT>` below with that exact SHA and run:

```bash
git fetch origin
git worktree add -b impl/live-alternative-diagnostic-mediation-v1 \
  ../interface-theory-v1 <PLAN_COMMIT>
cd ../interface-theory-v1
```

Expected: new branch `impl/live-alternative-diagnostic-mediation-v1` starts exactly from the committed plan and design lineage.

- [ ] **Step 2: Verify ancestry and cleanliness**

Run:

```bash
git status --short
git merge-base --is-ancestor 1f646397d76b04c96afa22815bc78957b561c81b HEAD
git log --oneline --decorate -5
```

Expected:

```text
# git status --short: no output
# merge-base: exit 0
# log contains the V1 design commit and V1 implementation-plan commit
```

- [ ] **Step 3: Record protected-file hashes**

Run:

```bash
sha256sum \
  docs/CANONICAL_RECORD.md \
  docs/RESULT_LEDGER.md \
  docs/EVIDENCE_INDEX.md \
  docs/protocol_foundations.md \
  ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md \
  FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md \
  scripts/validate_frozen_record.py \
  .github/workflows/validate-frozen-record.yml \
  > /tmp/v1-protected-before.sha256

git ls-files '*gate_013*' '*gate_014*' | sort > /tmp/v1-gates.txt
xargs -r sha256sum < /tmp/v1-gates.txt > /tmp/v1-gates-before.sha256
```

Expected: both hash files are created without errors.

- [ ] **Step 4: Verify no V1 implementation/result path already exists**

Run:

```bash
test ! -e experiments/research_seeds/live_alternative_diagnostic_mediation_v1
```

Expected: exit `0`.

- [ ] **Step 5: Commit nothing**

Task 1 must leave repository bytes unchanged.

---

### Task 2: Encode the frozen square, repair vocabulary, and null family

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py`

**Interfaces:**
- Produces: `Signature`, `Diagnostic`, `MediationStatus`, `LatentModel`, `POSITIVE_MODELS`, `POSITIVE_PAIRS`, `NULL_PAIR`, `BUDGET`, `DIAGNOSTIC_COST`, `REPAIR_COST`, `marginal_view()`, `world_observation()`.
- Consumed later by: `mediation.py`, `assay.py`.

- [ ] **Step 1: Write the failing protocol tests**

Create `test_protocol.py` with these tests:

```python
import unittest

from protocol import (
    BUDGET,
    DIAGNOSTIC_COST,
    NULL_PAIR,
    POSITIVE_MODELS,
    POSITIVE_PAIRS,
    REPAIR_COST,
    Diagnostic,
    marginal_view,
)


class ProtocolTests(unittest.TestCase):
    def test_square_signatures_are_exact(self):
        self.assertEqual(
            {model.key: marginal_view(model) for model in POSITIVE_MODELS},
            {
                "M00": (0, 0),
                "M01": (0, 1),
                "M10": (1, 0),
                "M11": (1, 1),
            },
        )

    def test_positive_family_is_exactly_four_square_edges(self):
        edges = {frozenset((left.key, right.key)) for left, right in POSITIVE_PAIRS}
        self.assertEqual(
            edges,
            {
                frozenset(("M00", "M10")),
                frozenset(("M01", "M11")),
                frozenset(("M00", "M01")),
                frozenset(("M10", "M11")),
            },
        )
        self.assertNotIn(frozenset(("M00", "M11")), edges)
        self.assertNotIn(frozenset(("M01", "M10")), edges)

    def test_every_positive_edge_differs_on_exactly_one_coordinate(self):
        for left, right in POSITIVE_PAIRS:
            diffs = sum(a != b for a, b in zip(left.signature, right.signature))
            self.assertEqual(diffs, 1)

    def test_each_endpoint_occurs_in_one_q0_edge_and_one_q1_edge(self):
        incidence = {model.key: set() for model in POSITIVE_MODELS}
        for left, right in POSITIVE_PAIRS:
            differing = [index for index in (0, 1) if left.signature[index] != right.signature[index]]
            diagnostic = Diagnostic.Q0 if differing == [0] else Diagnostic.Q1
            incidence[left.key].add(diagnostic)
            incidence[right.key].add(diagnostic)
        for diagnostics in incidence.values():
            self.assertEqual(diagnostics, {Diagnostic.Q0, Diagnostic.Q1})

    def test_repairs_are_unique_and_budget_is_exact(self):
        self.assertEqual(len({model.repair for model in POSITIVE_MODELS}), 4)
        self.assertEqual(BUDGET, 2)
        self.assertEqual(DIAGNOSTIC_COST, 1)
        self.assertEqual(REPAIR_COST, 1)

    def test_null_pair_has_identical_signature_and_distinct_repairs(self):
        left, right = NULL_PAIR
        self.assertEqual(left.signature, (0, 0))
        self.assertEqual(right.signature, (0, 0))
        self.assertNotEqual(left.repair, right.repair)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the protocol tests and verify RED**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_protocol.py' -v
```

Expected: import failure because `protocol.py` does not exist.

- [ ] **Step 3: Implement the minimal frozen protocol objects**

Create `protocol.py` with this structure:

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

Signature: TypeAlias = tuple[int, int]


class Diagnostic(str, Enum):
    Q0 = "q0"
    Q1 = "q1"


class MediationStatus(str, Enum):
    NO_DISCRIMINATING_DIAGNOSTIC = "NO_DISCRIMINATING_DIAGNOSTIC"
    OUT_OF_FROZEN_FAMILY = "OUT_OF_FROZEN_FAMILY"


@dataclass(frozen=True)
class LatentModel:
    key: str
    signature: Signature
    repair: str


M00 = LatentModel("M00", (0, 0), "r00")
M01 = LatentModel("M01", (0, 1), "r01")
M10 = LatentModel("M10", (1, 0), "r10")
M11 = LatentModel("M11", (1, 1), "r11")

POSITIVE_MODELS = (M00, M01, M10, M11)
POSITIVE_PAIRS = (
    (M00, M10),
    (M01, M11),
    (M00, M01),
    (M10, M11),
)

N0 = LatentModel("N0", (0, 0), "rN0")
N1 = LatentModel("N1", (0, 0), "rN1")
NULL_PAIR = (N0, N1)

DIAGNOSTICS = (Diagnostic.Q0, Diagnostic.Q1)
BUDGET = 2
DIAGNOSTIC_COST = 1
REPAIR_COST = 1


def marginal_view(model: LatentModel) -> Signature:
    return model.signature


def world_observation(model: LatentModel, diagnostic: Diagnostic) -> int:
    index = 0 if diagnostic is Diagnostic.Q0 else 1
    return model.signature[index]
```

Do not add model IDs, pair IDs, or pair classes to `Signature`.

- [ ] **Step 4: Run the protocol tests and verify GREEN**

Run the same unittest command.

Expected: all protocol tests pass.

- [ ] **Step 5: Commit Task 2**

Run:

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py \
        experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py
git commit -m "feat: encode frozen V1 model square"
```

---

### Task 3: Implement the strict C0/C1 mediation boundary

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py`

**Interfaces:**
- Consumes: only `Diagnostic`, `MediationStatus`, and `Signature` from `protocol.py`.
- Produces: `compare_signatures(left, right)`, `control_select_diagnostic()`, `treatment_select_diagnostic(left, right)`.
- Hard boundary: `mediation.py` must not import `LatentModel`, `POSITIVE_MODELS`, `POSITIVE_PAIRS`, `NULL_PAIR`, model keys, or repair mappings.

- [ ] **Step 1: Write the failing mediation tests**

Create `test_mediation.py`:

```python
import inspect
import unittest

import mediation
from mediation import (
    compare_signatures,
    control_select_diagnostic,
    treatment_select_diagnostic,
)
from protocol import Diagnostic, MediationStatus


class MediationTests(unittest.TestCase):
    def test_xor_comparison_is_permutation_symmetric(self):
        self.assertEqual(compare_signatures((0, 0), (1, 0)), (1, 0))
        self.assertEqual(compare_signatures((1, 0), (0, 0)), (1, 0))
        self.assertEqual(compare_signatures((0, 1), (0, 0)), (0, 1))

    def test_treatment_selects_unique_disagreement_coordinate(self):
        self.assertEqual(treatment_select_diagnostic((0, 0), (1, 0)), Diagnostic.Q0)
        self.assertEqual(treatment_select_diagnostic((0, 0), (0, 1)), Diagnostic.Q1)

    def test_treatment_abstains_on_no_disagreement(self):
        self.assertEqual(
            treatment_select_diagnostic((0, 0), (0, 0)),
            MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC,
        )

    def test_treatment_rejects_double_disagreement_as_out_of_family(self):
        self.assertEqual(
            treatment_select_diagnostic((0, 0), (1, 1)),
            MediationStatus.OUT_OF_FROZEN_FAMILY,
        )

    def test_control_selector_is_pair_blind(self):
        self.assertEqual(list(inspect.signature(control_select_diagnostic).parameters), [])
        self.assertEqual(control_select_diagnostic(), Diagnostic.Q0)

    def test_treatment_selector_accepts_only_two_marginal_signatures(self):
        self.assertEqual(
            list(inspect.signature(treatment_select_diagnostic).parameters),
            ["left", "right"],
        )

    def test_mediation_module_has_no_latent_registry_imports(self):
        forbidden = {
            "LatentModel",
            "POSITIVE_MODELS",
            "POSITIVE_PAIRS",
            "NULL_PAIR",
            "M00",
            "M01",
            "M10",
            "M11",
        }
        self.assertTrue(forbidden.isdisjoint(mediation.__dict__))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the mediation tests and verify RED**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_mediation.py' -v
```

Expected: import failure because `mediation.py` does not exist.

- [ ] **Step 3: Implement the pure temporary comparator and selectors**

Create `mediation.py`:

```python
from __future__ import annotations

from protocol import Diagnostic, MediationStatus, Signature

MediationOutput = Diagnostic | MediationStatus


def compare_signatures(left: Signature, right: Signature) -> Signature:
    return left[0] ^ right[0], left[1] ^ right[1]


def control_select_diagnostic() -> Diagnostic:
    return Diagnostic.Q0


def treatment_select_diagnostic(
    left: Signature,
    right: Signature,
) -> MediationOutput:
    disagreement = compare_signatures(left, right)
    if disagreement == (1, 0):
        return Diagnostic.Q0
    if disagreement == (0, 1):
        return Diagnostic.Q1
    if disagreement == (0, 0):
        return MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC
    return MediationStatus.OUT_OF_FROZEN_FAMILY
```

Keep the module stateless. Do not create a mediator object, cache, learned parameter, or cross-episode global.

- [ ] **Step 4: Run protocol + mediation tests**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_*.py' -v
```

Expected: all current tests pass.

- [ ] **Step 5: Commit Task 3**

Run:

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py \
        experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py
git commit -m "feat: add ephemeral V1 comparison channel"
```

---

### Task 4: Implement external evidence, resolution, budget, and representative episodes

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py`

**Interfaces:**
- Consumes: protocol constants/models plus `control_select_diagnostic()` and `treatment_select_diagnostic()`.
- Produces: `Condition`, `EpisodeResult`, `ProtocolViolation`, `run_episode()`, `positive_episode_specs()`, `aggregate_results()`, `validate_contract()`, `run_assay()`.
- Scientific boundary: component tests may run representative episodes, but must not call `run_assay()` over the complete frozen V1 family.

- [ ] **Step 1: Write failing representative episode tests**

Create `test_assay.py` with:

```python
import unittest

from assay import (
    Condition,
    EpisodeResult,
    aggregate_results,
    positive_episode_specs,
    run_episode,
    validate_contract,
)
from protocol import M00, M01, M10, NULL_PAIR, Diagnostic, MediationStatus


class AssayTests(unittest.TestCase):
    def test_control_succeeds_when_fixed_q0_discriminates(self):
        result = run_episode(Condition.C0, (M00, M10), M10)
        self.assertEqual(result.diagnostic, Diagnostic.Q0.value)
        self.assertEqual(result.observation, 1)
        self.assertEqual(result.resolved_model, "M10")
        self.assertEqual(result.repair, "r10")
        self.assertEqual(result.budget_remaining, 0)
        self.assertTrue(result.discriminating)
        self.assertTrue(result.repair_success)

    def test_control_fails_bounded_zero_error_after_nondiscriminating_q0(self):
        result = run_episode(Condition.C0, (M00, M01), M01)
        self.assertEqual(result.diagnostic, Diagnostic.Q0.value)
        self.assertEqual(result.observation, 0)
        self.assertIsNone(result.resolved_model)
        self.assertIsNone(result.repair)
        self.assertEqual(result.budget_remaining, 1)
        self.assertFalse(result.discriminating)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")

    def test_treatment_uses_relation_then_world_evidence_to_resolve(self):
        result = run_episode(Condition.C1, (M00, M01), M01)
        self.assertEqual(result.diagnostic, Diagnostic.Q1.value)
        self.assertEqual(result.observation, 1)
        self.assertEqual(result.resolved_model, "M01")
        self.assertEqual(result.repair, "r01")
        self.assertEqual(result.budget_remaining, 0)
        self.assertTrue(result.repair_success)

    def test_treatment_is_pair_order_invariant(self):
        forward = run_episode(Condition.C1, (M00, M01), M01)
        reverse = run_episode(Condition.C1, (M01, M00), M01)
        self.assertEqual(forward.diagnostic, reverse.diagnostic)
        self.assertEqual(forward.resolved_model, reverse.resolved_model)
        self.assertEqual(forward.repair_success, reverse.repair_success)

    def test_null_treatment_abstains_before_world_action(self):
        left, right = NULL_PAIR
        result = run_episode(Condition.C1, (left, right), left)
        self.assertEqual(
            result.diagnostic,
            MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC.value,
        )
        self.assertIsNone(result.observation)
        self.assertEqual(result.budget_remaining, 2)
        self.assertIsNone(result.resolved_model)
        self.assertIsNone(result.repair)

    def test_positive_episode_spec_count_is_exact_without_executing_them(self):
        self.assertEqual(len(positive_episode_specs()), 8)

    def test_aggregation_math_uses_supplied_results_only(self):
        fake = [
            EpisodeResult("C0", ("A", "B"), "A", "q0", 0, "A", "rA", 0, True, True, None),
            EpisodeResult("C0", ("C", "D"), "C", "q0", 0, None, None, 1, False, False, "NO_BOUNDED_ZERO_ERROR_CONTINUATION"),
        ]
        aggregate = aggregate_results(fake)
        self.assertEqual(aggregate["episode_count"], 2)
        self.assertEqual(aggregate["discriminating_count"], 1)
        self.assertEqual(aggregate["repair_success_count"], 1)
        self.assertEqual(aggregate["P_disc"], 0.5)
        self.assertEqual(aggregate["P_repair"], 0.5)

    def test_static_contract_validation_passes_without_running_full_assay(self):
        record = validate_contract()
        self.assertTrue(record["endpoint_nonidentifiability_verified"])
        self.assertTrue(record["no_universal_diagnostic_verified"])
        self.assertTrue(record["pair_order_invariance_verified"])
        self.assertTrue(record["shared_menu_verified"])
        self.assertEqual(record["null_disagreement_vector"], [0, 0])
        self.assertEqual(
            record["null_mediator_output"],
            "NO_DISCRIMINATING_DIAGNOSTIC",
        )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run `test_assay.py` and verify RED**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_assay.py' -v
```

Expected: import failure because `assay.py` does not exist.

- [ ] **Step 3: Implement condition/result types and episode execution**

`assay.py` must define these exact public types:

```python
from dataclasses import dataclass
from enum import Enum


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
```

Implement `run_episode()` so that:

```python
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

    if isinstance(decision, MediationStatus):
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
    coordinate = 0 if decision is Diagnostic.Q0 else 1
    survivors = [
        model for model in pair
        if model.signature[coordinate] == observation
    ]

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
```

Do not let either selector receive `left.key`, `right.key`, pair labels, or repair names.

- [ ] **Step 4: Implement frozen enumeration, static contract validation, and aggregation**

Implement:

```python
def positive_episode_specs():
    return tuple(
        (pair, true_model)
        for pair in POSITIVE_PAIRS
        for true_model in pair
    )


def aggregate_results(results):
    results = tuple(results)
    count = len(results)
    discriminating = sum(result.discriminating for result in results)
    repaired = sum(result.repair_success for result in results)
    return {
        "episode_count": count,
        "discriminating_count": discriminating,
        "repair_success_count": repaired,
        "P_disc": discriminating / count,
        "P_repair": repaired / count,
    }
```

`validate_contract()` must check all frozen structural invariants without invoking `run_assay()`:

```text
positive_pair_count == 4
positive_episode_count_per_condition == 8
every positive pair differs on exactly one coordinate
each endpoint appears in one q0-edge and one q1-edge
no single diagnostic separates all four positive pairs
C1 output is invariant to pair order
null disagreement vector == [0,0]
null output == NO_DISCRIMINATING_DIAGNOSTIC
square diagonals map to OUT_OF_FROZEN_FAMILY
all positive repairs are unique
null repairs differ
BUDGET == 2
diagnostic and repair costs == 1
```

Return booleans using the field names from design section 18 where applicable.

- [ ] **Step 5: Define but do not invoke the full assay function**

Add:

```python
def run_assay() -> dict:
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
    null_left, null_right = NULL_PAIR
    null_output = treatment_select_diagnostic(
        marginal_view(null_left), marginal_view(null_right)
    )
    return {
        "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
        "execution_state": "EXECUTED",
        "positive_pair_count": 4,
        "positive_episode_count_per_condition": 8,
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
        **contract,
        "null_disagreement_vector": [0, 0],
        "null_mediator_output": null_output.value,
    }
```

Do not add a unit test that calls `run_assay()` over the frozen V1 positive family during implementation. The function exists for a separately authorized scientific execution step.

- [ ] **Step 6: Run all component tests**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_*.py' -v
```

Expected: all tests pass; no test invokes `run_assay()`.

- [ ] **Step 7: Commit Task 4**

Run:

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py \
        experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py
git commit -m "feat: add bounded V1 episode machinery"
```

---

### Task 5: Add an execution-gated CLI without running the assay

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py`

**Interfaces:**
- `--validate-contract`: allowed during implementation; prints structural validation plus `execution_state=UNEXECUTED`.
- `--execute --write <path>`: scientific execution path; must not be invoked during implementation.
- No default mode may call `run_assay()`.

- [ ] **Step 1: Write failing CLI safety tests**

Create `test_cli.py`:

```python
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_v1


class CliTests(unittest.TestCase):
    def test_validate_contract_does_not_call_full_assay(self):
        stdout = io.StringIO()
        with patch.object(run_v1, "run_assay", side_effect=AssertionError("assay executed")):
            with contextlib.redirect_stdout(stdout):
                code = run_v1.main(["--validate-contract"])
        self.assertEqual(code, 0)
        payload = json.loads(stdout.getvalue())
        self.assertEqual(payload["execution_state"], "UNEXECUTED")
        self.assertEqual(payload["scientific_result"], "NONE")

    def test_execute_requires_explicit_write_path_before_assay_call(self):
        with patch.object(run_v1, "run_assay", side_effect=AssertionError("assay executed")):
            with self.assertRaises(SystemExit):
                run_v1.main(["--execute"])

    def test_write_is_rejected_without_execute(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "result.json"
            with self.assertRaises(SystemExit):
                run_v1.main(["--validate-contract", "--write", str(target)])
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run CLI tests and verify RED**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_cli.py' -v
```

Expected: import failure because `run_v1.py` does not exist.

- [ ] **Step 3: Implement the mutually exclusive CLI modes**

Create `run_v1.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from assay import run_assay, validate_contract


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    mode = value.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-contract", action="store_true")
    mode.add_argument("--execute", action="store_true")
    value.add_argument("--write", type=Path)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)

    if args.validate_contract:
        if args.write is not None:
            parser().error("--write is valid only with --execute")
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
        parser().error("--execute requires --write")

    result = run_assay()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.write.parent.mkdir(parents=True, exist_ok=True)
    args.write.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

The explicit `execution_state="EXECUTED"` exists only inside the result returned by `run_assay()` after the `--execute --write` gate is crossed.

- [ ] **Step 4: Run all unit tests and structural validation only**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_*.py' -v

python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py \
  --validate-contract
```

Expected:

```text
all tests pass
execution_state = UNEXECUTED
scientific_result = NONE
```

Do not run the CLI with `--execute`.

- [ ] **Step 5: Commit Task 5**

Run:

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py \
        experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py
git commit -m "feat: gate V1 scientific execution"
```

---

### Task 6: Document the implementation boundary and add non-executing CI

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md`
- Create: `.github/workflows/validate-v1-implementation.yml`

**Interfaces:**
- README distinguishes implementation validation from scientific execution.
- CI runs unit tests and `--validate-contract` only.
- Existing `.github/workflows/validate-frozen-record.yml` remains byte-unchanged.

- [ ] **Step 1: Create the local implementation README**

The README must begin with exactly these state lines:

```text
Protocol state: FROZEN_PRE_EXECUTION_ASSAY
Implementation state: IMPLEMENTED_NOT_EXECUTED
Execution state: UNEXECUTED
Scientific result: NONE
Canonical standing: NONCANONICAL_RESEARCH_SEED
Translation standing: NO_TRANSLATION_EARNED
```

Then link:

```text
Design: docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md
Plan: docs/superpowers/plans/2026-09-07-live-alternative-diagnostic-mediation-v1.md
Frozen V0: docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md
```

Document the allowed implementation-validation commands:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_*.py' -v

python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py \
  --validate-contract

python scripts/validate_frozen_record.py
```

Add an explicit warning:

```text
The scientific execution mode is intentionally not part of implementation validation.
Do not run --execute without a separate explicit authorization to execute the frozen V1 assay.
Passing unit tests or contract validation is not a V1 scientific result.
```

- [ ] **Step 2: Create a V1-specific implementation CI workflow**

Create `.github/workflows/validate-v1-implementation.yml`:

```yaml
name: Validate V1 implementation without assay execution

on:
  push:
    paths:
      - "experiments/research_seeds/live_alternative_diagnostic_mediation_v1/**"
      - ".github/workflows/validate-v1-implementation.yml"
  pull_request:
    paths:
      - "experiments/research_seeds/live_alternative_diagnostic_mediation_v1/**"
      - ".github/workflows/validate-v1-implementation.yml"

permissions:
  contents: read

jobs:
  validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: >-
          python -m unittest discover
          -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1
          -p 'test_*.py' -v
      - run: >-
          python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py
          --validate-contract
```

Do not add `--execute`, a result path, or a result-upload step.

- [ ] **Step 3: Verify the workflow cannot trigger scientific execution**

Run:

```bash
if grep -n -- '--execute' .github/workflows/validate-v1-implementation.yml; then
  echo 'ERROR: V1 CI contains scientific execution command' >&2
  exit 1
fi

grep -n -- '--validate-contract' .github/workflows/validate-v1-implementation.yml
```

Expected: first command finds nothing; second finds exactly the validation command.

- [ ] **Step 4: Run all allowed validation commands**

Run the three commands documented in the README.

Expected: unit tests pass, contract validation says `UNEXECUTED`, frozen-record validation exits `0`.

- [ ] **Step 5: Commit Task 6**

Run:

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md \
        .github/workflows/validate-v1-implementation.yml
git commit -m "docs: bind V1 implementation to unexecuted state"
```

---

### Task 7: Final implementation verification without scientific execution

**Files:**
- Verification only.
- No result artifact may be created.

**Interfaces:**
- Consumes all implementation tasks.
- Produces an implementation checkpoint whose legal terminal state is `IMPLEMENTED_NOT_EXECUTED / UNEXECUTED / NONE`.

- [ ] **Step 1: Run the complete unit suite**

Run:

```bash
python -m unittest discover \
  -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -p 'test_*.py' -v
```

Expected: `0` failures and `0` errors.

- [ ] **Step 2: Run structural contract validation only**

Run:

```bash
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py \
  --validate-contract \
  > /tmp/v1-contract-validation.json

python - <<'PY'
import json
from pathlib import Path
record = json.loads(Path('/tmp/v1-contract-validation.json').read_text())
assert record['protocol_state'] == 'FROZEN_PRE_EXECUTION_ASSAY'
assert record['execution_state'] == 'UNEXECUTED'
assert record['scientific_result'] == 'NONE'
contract = record['contract_validation']
assert contract['endpoint_nonidentifiability_verified'] is True
assert contract['no_universal_diagnostic_verified'] is True
assert contract['pair_order_invariance_verified'] is True
assert contract['null_disagreement_vector'] == [0, 0]
assert contract['null_mediator_output'] == 'NO_DISCRIMINATING_DIAGNOSTIC'
print('V1 implementation contract validation: PASS / UNEXECUTED')
PY
```

Expected: final printed line exactly identifies `UNEXECUTED` state.

- [ ] **Step 3: Re-run frozen canonical repository validation**

Run:

```bash
python scripts/validate_frozen_record.py
```

Expected: exit `0`.

- [ ] **Step 4: Verify protected files and existing frozen gates are byte-unchanged**

Run:

```bash
sha256sum -c /tmp/v1-protected-before.sha256
xargs -r sha256sum < /tmp/v1-gates.txt > /tmp/v1-gates-after.sha256
diff -u /tmp/v1-gates-before.sha256 /tmp/v1-gates-after.sha256
```

Expected: every protected hash reports `OK`; gate diff has no output.

- [ ] **Step 5: Verify no scientific result artifact exists**

Run:

```bash
test ! -d experiments/research_seeds/live_alternative_diagnostic_mediation_v1/results
! find experiments/research_seeds/live_alternative_diagnostic_mediation_v1 \
  -type f \( -name 'result.json' -o -name 'summary.md' \) -print -quit | grep -q .
```

Expected: both commands exit `0`.

- [ ] **Step 6: Verify no forbidden canonical file changed**

Run:

```bash
git diff --name-only <PLAN_COMMIT>...HEAD | sort
```

Expected changed paths are restricted to:

```text
.github/workflows/validate-v1-implementation.yml
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py
experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py
```

If any canonical ledger, evidence index, existing gate, existing validator, or `experiments/results/` path appears, stop and repair the implementation before proceeding.

- [ ] **Step 7: Verify branch state and commit history**

Run:

```bash
git status --short
git log --oneline --decorate <PLAN_COMMIT>..HEAD
```

Expected: clean working tree and a small sequence of task-scoped implementation commits.

- [ ] **Step 8: STOP before scientific execution**

Do not run:

```bash
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py \
  --execute \
  --write experiments/research_seeds/live_alternative_diagnostic_mediation_v1/results/result.json
```

The legal terminal implementation state is exactly:

```text
protocol_state = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state = UNEXECUTED
scientific_result = NONE
```

A separate explicit user authorization is required before the frozen V1 scientific assay may be executed.

---

## Execution Handoff Boundary

The implementation plan deliberately separates three things:

```text
implementation validation
!=
scientific assay execution
!=
scientific interpretation / promotion
```

Completing Tasks 1–7 may establish only that the implementation appears to instantiate the approved finite design and that the scientific execution path remains unrun. It does not create a V1 empirical result and does not authorize V2.
