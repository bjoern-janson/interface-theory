# Live-Alternative Diagnostic Mediation V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the frozen `LIVE_ALTERNATIVE_DIAGNOSTIC_MEDIATION_V1` finite-assay machinery without executing the scientific assay, while preserving the causal contrast between isolated marginal access and temporary joint relation computation.

**Architecture:** Add a small deterministic Python 3.12 package under `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/`. `protocol.py` owns the frozen world/model objects; `mediation.py` owns the only C0/C1 causal difference; `assay.py` owns common external evidence, resolution, budgeting, validation, and the separately gated full assay; `run_v1.py` separates structural validation from scientific execution. Unit tests and CI exercise components and `--validate-contract` only. They must not invoke the full frozen V1 execution path.

**Tech Stack:** Python 3.12 standard library only (`dataclasses`, `enum`, `argparse`, `json`, `unittest`, `pathlib`), Git, existing `scripts/validate_frozen_record.py`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md`

## Global Constraints

- Approved design commit: `1f646397d76b04c96afa22815bc78957b561c81b` on `design/live-alternative-diagnostic-mediation-v1`.
- At implementation start, resolve and record the then-current head of `origin/design/live-alternative-diagnostic-mediation-v1` as `PLAN_BASE`; require the approved design commit to be its ancestor; create `impl/live-alternative-diagnostic-mediation-v1` from that exact resolved commit.
- `LIVE_ALTERNATIVE_DIAGNOSTIC_MEDIATION_V1` remains `NONCANONICAL_RESEARCH_SEED` and `NO_TRANSLATION_EARNED`.
- Before scientific execution there is no empirical V1 result. Implementation validation is not assay execution.
- V1 receives no credit for preserving alternatives. C0 and C1 already contain the same live alternatives and the same marginal predictive signatures.
- Diagnostic menu is exactly `{q0,q1}`. No diagnostic invention or composition is permitted.
- Positive signatures are exactly `M00=(0,0)`, `M01=(0,1)`, `M10=(1,0)`, `M11=(1,1)`.
- Positive live pairs are exactly the four square edges. Square diagonals are outside the frozen family.
- Each positive pair has exactly one discriminating diagnostic. Each endpoint occurs in one `q0` edge and one `q1` edge, so no endpoint alone determines the useful diagnostic over the positive family.
- C0 is pair-blind and precommitted to `q0`. No C0 pre-action node may receive both marginal streams as causal parents.
- C1's only extra pre-action operation is deterministic, read-only, permutation-symmetric comparison of the two signatures.
- Comparator contract is exact: `(1,0)->q0`, `(0,1)->q1`, `(0,0)->NO_DISCRIMINATING_DIAGNOSTIC`, `(1,1)->OUT_OF_FROZEN_FAMILY`.
- `OUT_OF_FROZEN_FAMILY` is a protocol violation if presented to episode execution; it is not an ordinary episode outcome.
- The mediator cannot modify alternatives, update parameters, retain state, or persist across episodes.
- Only the external world provides evidence about which live alternative is true. The mediator never selects the true model directly.
- Every positive latent model has a unique terminal repair. `B=2`; each diagnostic costs `1`; each repair costs `1`.
- Under the frozen controller/resolver contract, a non-discriminating positive-family probe leaves no bounded zero-error continuation.
- Frozen analytic values are design consequences, not implementation discoveries: `P_disc(C0)=0.5`, `P_disc(C1)=1.0`, `P_repair(C0)=0.5`, `P_repair(C1)=1.0`.
- Null pair consists of distinct `N0,N1` with identical signature `(0,0)` and distinct repairs. C1 must return `NO_DISCRIMINATING_DIAGNOSTIC` before world action.
- Do not invoke `run_v1.py --execute` during implementation.
- Do not create or commit a V1 results directory, `result.json`, scientific summary, result-ledger entry, evidence-index entry, or gate-registry entry during implementation.
- Do not modify `docs/CANONICAL_RECORD.md`, `docs/RESULT_LEDGER.md`, `docs/EVIDENCE_INDEX.md`, `docs/protocol_foundations.md`, `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md`, `FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md`, Gate 013, Gate 014, `scripts/validate_frozen_record.py`, or `.github/workflows/validate-frozen-record.yml`.
- Do not turn V1 into Gate 015.
- Use no third-party Python dependency.

---

## File Structure

**Create:**
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py` — frozen models, signatures, positive-pair family, null pair, repairs, costs, marginal projection, world response.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py` — C0 selector and C1 XOR comparator; no latent-model registry imports.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py` — episode type, common resolver, resource accounting, contract validator, pure aggregator, separately gated full assay.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py` — mutually exclusive `--validate-contract` and `--execute`; execution requires `--write`.
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py`
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py`
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py`
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py`
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md`
- `.github/workflows/validate-v1-implementation.yml`

**Do not create:**
- `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/results/`
- any V1 `result.json`
- any V1 scientific `summary.md`

---

### Task 1: Establish the isolated implementation baseline

**Files:**
- Read: `docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md`
- Read: this plan
- Read: `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`
- Read: `scripts/validate_frozen_record.py`
- Read: `.github/workflows/validate-frozen-record.yml`

**Interfaces:**
- Consumes: approved design lineage and current committed implementation plan.
- Produces: clean implementation worktree plus exact `PLAN_BASE` and protected-file hashes.

- [ ] **Step 1: Resolve the committed plan head and create an isolated worktree**

Run from a clean clone:

```bash
git fetch origin
PLAN_BASE=$(git rev-parse origin/design/live-alternative-diagnostic-mediation-v1)
git merge-base --is-ancestor 1f646397d76b04c96afa22815bc78957b561c81b "$PLAN_BASE"
git show "$PLAN_BASE":docs/superpowers/plans/2026-09-07-live-alternative-diagnostic-mediation-v1.md >/dev/null
printf '%s\n' "$PLAN_BASE" > /tmp/v1-plan-base.txt
git worktree add -b impl/live-alternative-diagnostic-mediation-v1 ../interface-theory-v1 "$PLAN_BASE"
cd ../interface-theory-v1
```

Expected: all commands exit `0`; implementation branch begins exactly at the resolved committed plan head.

- [ ] **Step 2: Verify ancestry and cleanliness**

Run:

```bash
git status --short
git merge-base --is-ancestor 1f646397d76b04c96afa22815bc78957b561c81b HEAD
test "$(git rev-parse HEAD)" = "$(cat /tmp/v1-plan-base.txt)"
git log --oneline --decorate -6
```

Expected: no status output; both ancestry/equality checks exit `0`.

- [ ] **Step 3: Record hashes for protected artifacts**

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

Expected: both hash manifests exist and are nonempty.

- [ ] **Step 4: Verify no implementation/result path exists yet**

Run:

```bash
test ! -e experiments/research_seeds/live_alternative_diagnostic_mediation_v1
```

Expected: exit `0`.

- [ ] **Step 5: Commit nothing**

Task 1 leaves repository bytes unchanged.

---

### Task 2: Encode the frozen square, repairs, and null pair

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py`

**Interfaces:**
- Produces: `Signature`, `Diagnostic`, `MediationStatus`, `LatentModel`, `M00`, `M01`, `M10`, `M11`, `POSITIVE_MODELS`, `POSITIVE_PAIRS`, `NULL_PAIR`, `BUDGET`, `DIAGNOSTIC_COST`, `REPAIR_COST`, `marginal_view()`, `world_observation()`.

- [ ] **Step 1: Write the RED protocol tests**

Create `test_protocol.py`:

```python
import unittest

from protocol import (
    BUDGET, DIAGNOSTIC_COST, NULL_PAIR, POSITIVE_MODELS, POSITIVE_PAIRS,
    REPAIR_COST, Diagnostic, marginal_view,
)


class ProtocolTests(unittest.TestCase):
    def test_square_signatures_are_exact(self):
        self.assertEqual(
            {m.key: marginal_view(m) for m in POSITIVE_MODELS},
            {"M00": (0, 0), "M01": (0, 1), "M10": (1, 0), "M11": (1, 1)},
        )

    def test_positive_family_is_exactly_the_four_square_edges(self):
        edges = {frozenset((a.key, b.key)) for a, b in POSITIVE_PAIRS}
        self.assertEqual(edges, {
            frozenset(("M00", "M10")), frozenset(("M01", "M11")),
            frozenset(("M00", "M01")), frozenset(("M10", "M11")),
        })
        self.assertNotIn(frozenset(("M00", "M11")), edges)
        self.assertNotIn(frozenset(("M01", "M10")), edges)

    def test_each_positive_edge_differs_on_exactly_one_coordinate(self):
        for left, right in POSITIVE_PAIRS:
            self.assertEqual(sum(a != b for a, b in zip(left.signature, right.signature)), 1)

    def test_each_endpoint_occurs_in_one_q0_and_one_q1_edge(self):
        incidence = {m.key: set() for m in POSITIVE_MODELS}
        for left, right in POSITIVE_PAIRS:
            diffs = [i for i in (0, 1) if left.signature[i] != right.signature[i]]
            diagnostic = Diagnostic.Q0 if diffs == [0] else Diagnostic.Q1
            incidence[left.key].add(diagnostic)
            incidence[right.key].add(diagnostic)
        for value in incidence.values():
            self.assertEqual(value, {Diagnostic.Q0, Diagnostic.Q1})

    def test_repairs_and_budget_are_exact(self):
        self.assertEqual(len({m.repair for m in POSITIVE_MODELS}), 4)
        self.assertEqual((BUDGET, DIAGNOSTIC_COST, REPAIR_COST), (2, 1, 1))

    def test_null_pair_has_same_signature_but_distinct_repairs(self):
        left, right = NULL_PAIR
        self.assertEqual(left.signature, right.signature)
        self.assertEqual(left.signature, (0, 0))
        self.assertNotEqual(left.repair, right.repair)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_protocol.py' -v
```

Expected: import failure because `protocol.py` does not exist.

- [ ] **Step 3: Implement the minimal protocol**

Create `protocol.py`:

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
POSITIVE_PAIRS = ((M00, M10), (M01, M11), (M00, M01), (M10, M11))
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
    return model.signature[0 if diagnostic is Diagnostic.Q0 else 1]
```

`Signature` must contain only the two prediction bits; never add IDs, pair labels, hashes, repairs, or metadata.

- [ ] **Step 4: Run GREEN**

Run the Task 2 unittest command again. Expected: all Task 2 tests pass.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/protocol.py experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_protocol.py
git commit -m "feat: encode frozen V1 model square"
```

---

### Task 3: Implement the strict C0/C1 mediation boundary

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py`

**Interfaces:**
- Consumes only: `Diagnostic`, `MediationStatus`, `Signature`.
- Produces: `compare_signatures(left,right)`, `control_select_diagnostic()`, `treatment_select_diagnostic(left,right)`.
- `mediation.py` must not import `LatentModel`, model registries, model keys, pair tables, or repair mappings.

- [ ] **Step 1: Write RED mediation tests**

Create `test_mediation.py`:

```python
import inspect
import unittest
import mediation
from mediation import compare_signatures, control_select_diagnostic, treatment_select_diagnostic
from protocol import Diagnostic, MediationStatus

class MediationTests(unittest.TestCase):
    def test_xor_is_permutation_symmetric(self):
        self.assertEqual(compare_signatures((0,0),(1,0)), (1,0))
        self.assertEqual(compare_signatures((1,0),(0,0)), (1,0))
        self.assertEqual(compare_signatures((0,1),(0,0)), (0,1))

    def test_treatment_selects_the_unique_disagreement(self):
        self.assertEqual(treatment_select_diagnostic((0,0),(1,0)), Diagnostic.Q0)
        self.assertEqual(treatment_select_diagnostic((0,0),(0,1)), Diagnostic.Q1)

    def test_treatment_abstains_on_zero_disagreement(self):
        self.assertEqual(treatment_select_diagnostic((0,0),(0,0)), MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC)

    def test_double_disagreement_is_outside_family(self):
        self.assertEqual(treatment_select_diagnostic((0,0),(1,1)), MediationStatus.OUT_OF_FROZEN_FAMILY)

    def test_c0_selector_is_pair_blind(self):
        self.assertEqual(list(inspect.signature(control_select_diagnostic).parameters), [])
        self.assertEqual(control_select_diagnostic(), Diagnostic.Q0)

    def test_treatment_accepts_only_two_marginal_signatures(self):
        self.assertEqual(list(inspect.signature(treatment_select_diagnostic).parameters), ["left", "right"])

    def test_mediation_module_has_no_latent_registry_symbols(self):
        forbidden = {"LatentModel","POSITIVE_MODELS","POSITIVE_PAIRS","NULL_PAIR","M00","M01","M10","M11"}
        self.assertTrue(forbidden.isdisjoint(mediation.__dict__))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_mediation.py' -v
```

Expected: import failure because `mediation.py` does not exist.

- [ ] **Step 3: Implement the stateless comparator**

Create `mediation.py`:

```python
from __future__ import annotations
from protocol import Diagnostic, MediationStatus, Signature

MediationOutput = Diagnostic | MediationStatus

def compare_signatures(left: Signature, right: Signature) -> Signature:
    return left[0] ^ right[0], left[1] ^ right[1]

def control_select_diagnostic() -> Diagnostic:
    return Diagnostic.Q0

def treatment_select_diagnostic(left: Signature, right: Signature) -> MediationOutput:
    disagreement = compare_signatures(left, right)
    if disagreement == (1, 0):
        return Diagnostic.Q0
    if disagreement == (0, 1):
        return Diagnostic.Q1
    if disagreement == (0, 0):
        return MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC
    return MediationStatus.OUT_OF_FROZEN_FAMILY
```

No cache, object state, parameter, learned weight, or cross-episode global is permitted.

- [ ] **Step 4: Run all current tests**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
```

Expected: all current tests pass.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/mediation.py experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_mediation.py
git commit -m "feat: add ephemeral V1 comparison channel"
```

---

### Task 4: Implement external evidence, common resolution, budget, and representative episodes

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py`

**Interfaces:**
- Produces: `Condition`, `ProtocolViolation`, `EpisodeResult`, `resolve_pair()`, `run_episode()`, `positive_episode_specs()`, `aggregate_results()`, `validate_contract()`, `run_assay()`.
- C0 and C1 must converge on the same `resolve_pair()` and repair code after diagnostic choice.
- Component tests may run representative episodes. They must not call `run_assay()` over the complete frozen family.

- [ ] **Step 1: Write RED assay tests**

Create `test_assay.py`:

```python
import unittest
from assay import Condition, EpisodeResult, ProtocolViolation, aggregate_results, positive_episode_specs, run_episode, validate_contract
from protocol import M00, M01, M10, M11, NULL_PAIR, Diagnostic, MediationStatus

class AssayTests(unittest.TestCase):
    def test_c0_succeeds_when_fixed_q0_discriminates(self):
        result = run_episode(Condition.C0, (M00,M10), M10)
        self.assertEqual((result.diagnostic,result.observation,result.resolved_model,result.repair,result.budget_remaining), ("q0",1,"M10","r10",0))
        self.assertTrue(result.discriminating)
        self.assertTrue(result.repair_success)

    def test_c0_has_no_bounded_zero_error_continuation_after_nondiscriminating_q0(self):
        result = run_episode(Condition.C0, (M00,M01), M01)
        self.assertEqual(result.diagnostic, "q0")
        self.assertEqual(result.observation, 0)
        self.assertIsNone(result.resolved_model)
        self.assertIsNone(result.repair)
        self.assertEqual(result.budget_remaining, 1)
        self.assertFalse(result.discriminating)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")

    def test_c1_relation_selects_q1_then_world_evidence_resolves(self):
        result = run_episode(Condition.C1, (M00,M01), M01)
        self.assertEqual((result.diagnostic,result.observation,result.resolved_model,result.repair,result.budget_remaining), ("q1",1,"M01","r01",0))
        self.assertTrue(result.repair_success)

    def test_c1_is_pair_order_invariant(self):
        forward = run_episode(Condition.C1, (M00,M01), M01)
        reverse = run_episode(Condition.C1, (M01,M00), M01)
        self.assertEqual((forward.diagnostic,forward.resolved_model,forward.repair_success), (reverse.diagnostic,reverse.resolved_model,reverse.repair_success))

    def test_null_abstains_before_world_action(self):
        left, right = NULL_PAIR
        result = run_episode(Condition.C1, (left,right), left)
        self.assertEqual(result.diagnostic, MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC.value)
        self.assertIsNone(result.observation)
        self.assertEqual(result.budget_remaining, 2)

    def test_square_diagonal_is_protocol_violation_not_episode_outcome(self):
        with self.assertRaises(ProtocolViolation):
            run_episode(Condition.C1, (M00,M11), M00)

    def test_true_world_must_belong_to_live_pair(self):
        with self.assertRaises(ProtocolViolation):
            run_episode(Condition.C1, (M00,M01), M10)

    def test_positive_episode_specs_only_enumerate_count(self):
        self.assertEqual(len(positive_episode_specs()), 8)

    def test_aggregation_uses_only_supplied_synthetic_results(self):
        fake = [
            EpisodeResult("C0",("A","B"),"A","q0",0,"A","rA",0,True,True,None),
            EpisodeResult("C0",("C","D"),"C","q0",0,None,None,1,False,False,"NO_BOUNDED_ZERO_ERROR_CONTINUATION"),
        ]
        aggregate = aggregate_results(fake)
        self.assertEqual(aggregate, {"episode_count":2,"discriminating_count":1,"repair_success_count":1,"P_disc":0.5,"P_repair":0.5})

    def test_static_contract_fields_are_exact(self):
        record = validate_contract()
        expected_true = {
            "endpoint_nonidentifiability_verified",
            "no_universal_diagnostic_verified",
            "pair_order_invariance_verified",
            "marginal_information_matched",
            "joint_comparison_only_in_C1",
            "read_only_mediator_verified",
            "mediator_ephemeral_verified",
            "shared_menu_verified",
            "budget_matched",
            "resolver_identity_matched",
        }
        for field in expected_true:
            self.assertIs(record[field], True, field)
        self.assertEqual(record["positive_pair_count"], 4)
        self.assertEqual(record["positive_episode_count_per_condition"], 8)
        self.assertEqual(record["null_disagreement_vector"], [0,0])
        self.assertEqual(record["null_mediator_output"], "NO_DISCRIMINATING_DIAGNOSTIC")

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_assay.py' -v
```

Expected: import failure because `assay.py` does not exist.

- [ ] **Step 3: Implement exact public types and common resolver**

In `assay.py` define:

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
    pair: tuple[str,str]
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

Add one common resolver used by both arms:

```python
def resolve_pair(pair, diagnostic, observation):
    coordinate = 0 if diagnostic is Diagnostic.Q0 else 1
    return tuple(model for model in pair if model.signature[coordinate] == observation)
```

- [ ] **Step 4: Implement `run_episode()` with strict status handling**

The key branch must be exactly:

```python
left_view = marginal_view(left)
right_view = marginal_view(right)
if condition is Condition.C0:
    decision = control_select_diagnostic()
else:
    decision = treatment_select_diagnostic(left_view, right_view)

if decision is MediationStatus.OUT_OF_FROZEN_FAMILY:
    raise ProtocolViolation("live pair is outside the frozen V1 family")
if decision is MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC:
    return EpisodeResult(condition.value,(left.key,right.key),true_model.key,decision.value,None,None,None,BUDGET,False,False,None)
```

Then, and only then, execute the declared diagnostic through `world_observation()`, subtract `DIAGNOSTIC_COST`, pass the observation to the shared `resolve_pair()`, and:

```python
if len(survivors) != 1:
    return EpisodeResult(
        condition.value,(left.key,right.key),true_model.key,decision.value,
        observation,None,None,budget,False,False,
        "NO_BOUNDED_ZERO_ERROR_CONTINUATION",
    )
```

For a unique survivor, subtract `REPAIR_COST`, use that survivor's repair, and set `repair_success = (resolved is true_model)`. Neither selector may receive keys, repair strings, or pair labels.

- [ ] **Step 5: Implement frozen enumeration, pure aggregation, and exact static validation fields**

`positive_episode_specs()` must return exactly:

```python
return tuple((pair,true_model) for pair in POSITIVE_PAIRS for true_model in pair)
```

`aggregate_results(results)` must report exactly:

```text
episode_count
discriminating_count
repair_success_count
P_disc
P_repair
```

`validate_contract()` must compute/check the square and return at least these exact fields:

```text
positive_pair_count = 4
positive_episode_count_per_condition = 8
endpoint_nonidentifiability_verified = true
no_universal_diagnostic_verified = true
pair_order_invariance_verified = true
marginal_information_matched = true
joint_comparison_only_in_C1 = true
read_only_mediator_verified = true
mediator_ephemeral_verified = true
shared_menu_verified = true
budget_matched = true
resolver_identity_matched = true
null_disagreement_vector = [0,0]
null_mediator_output = NO_DISCRIMINATING_DIAGNOSTIC
```

The validator must additionally assert that both excluded diagonals return `OUT_OF_FROZEN_FAMILY`, all positive repairs are unique, null repairs differ, each positive edge differs on exactly one coordinate, and each endpoint is incident to one q0 and one q1 edge. It must not call `run_assay()`.

`resolver_identity_matched` is justified operationally by the single `resolve_pair()` function called downstream of both C0 and C1 diagnostic selection; do not implement condition-specific resolvers.

- [ ] **Step 6: Define the full assay but do not invoke it**

`run_assay()` may enumerate all eight positive episode specs under C0 and C1, aggregate them, attach `validate_contract()` fields, and emit the design-required result keys. It must set `execution_state="EXECUTED"` only when this function is actually called through the execution gate. No unit test in this plan may call `run_assay()`.

- [ ] **Step 7: Run all component tests**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
```

Expected: all tests pass; no test invokes `run_assay()`.

- [ ] **Step 8: Commit**

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/assay.py experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_assay.py
git commit -m "feat: add bounded V1 episode machinery"
```

---

### Task 5: Add an execution-gated CLI without running the assay

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py`
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py`

**Interfaces:**
- `--validate-contract`: permitted during implementation; never calls `run_assay()`.
- `--execute --write PATH`: scientific execution path; not invoked in this plan.

- [ ] **Step 1: Write RED CLI safety tests**

Create `test_cli.py`:

```python
import contextlib, io, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import run_v1

class CliTests(unittest.TestCase):
    def test_validate_contract_cannot_execute_assay(self):
        stdout = io.StringIO()
        with patch.object(run_v1,"run_assay",side_effect=AssertionError("assay executed")):
            with contextlib.redirect_stdout(stdout):
                code = run_v1.main(["--validate-contract"])
        payload = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(payload["execution_state"], "UNEXECUTED")
        self.assertEqual(payload["scientific_result"], "NONE")

    def test_execute_without_write_stops_before_assay(self):
        with patch.object(run_v1,"run_assay",side_effect=AssertionError("assay executed")):
            with self.assertRaises(SystemExit):
                run_v1.main(["--execute"])

    def test_write_without_execute_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/"result.json"
            with self.assertRaises(SystemExit):
                run_v1.main(["--validate-contract","--write",str(target)])
            self.assertFalse(target.exists())

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_cli.py' -v
```

Expected: import failure because `run_v1.py` does not exist.

- [ ] **Step 3: Implement the CLI gate**

Create `run_v1.py` with this exact control structure:

```python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from assay import run_assay, validate_contract

def build_parser():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-contract", action="store_true")
    mode.add_argument("--execute", action="store_true")
    parser.add_argument("--write", type=Path)
    return parser

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.validate_contract:
        if args.write is not None:
            parser.error("--write is valid only with --execute")
        print(json.dumps({
            "protocol_state":"FROZEN_PRE_EXECUTION_ASSAY",
            "implementation_state":"VALIDATED_NOT_EXECUTED",
            "execution_state":"UNEXECUTED",
            "scientific_result":"NONE",
            "contract_validation":validate_contract(),
        }, indent=2, sort_keys=True))
        return 0
    if args.write is None:
        parser.error("--execute requires --write")
    result = run_assay()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.write.parent.mkdir(parents=True, exist_ok=True)
    args.write.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run unit tests and validation mode only**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py --validate-contract
```

Expected: tests pass; printed state is `UNEXECUTED` with `scientific_result=NONE`. Do not invoke `--execute`.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py experiments/research_seeds/live_alternative_diagnostic_mediation_v1/test_cli.py
git commit -m "feat: gate V1 scientific execution"
```

---

### Task 6: Document the unexecuted implementation state and add non-executing CI

**Files:**
- Create: `experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md`
- Create: `.github/workflows/validate-v1-implementation.yml`

**Interfaces:**
- CI runs unit tests and `--validate-contract` only.
- Existing frozen-record workflow remains byte-unchanged.

- [ ] **Step 1: Create the implementation README**

Begin with:

```text
Protocol state: FROZEN_PRE_EXECUTION_ASSAY
Implementation state: IMPLEMENTED_NOT_EXECUTED
Execution state: UNEXECUTED
Scientific result: NONE
Canonical standing: NONCANONICAL_RESEARCH_SEED
Translation standing: NO_TRANSLATION_EARNED
```

Link the design, this plan, and `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`. Document exactly these permitted implementation-validation commands:

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py --validate-contract
python scripts/validate_frozen_record.py
```

State explicitly: passing tests/contract validation is not a V1 scientific result, and `--execute` requires separate explicit authorization.

- [ ] **Step 2: Add implementation-only CI**

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

- [ ] **Step 3: Verify CI contains no execution path**

```bash
if grep -n -- '--execute' .github/workflows/validate-v1-implementation.yml; then
  echo 'ERROR: V1 CI contains scientific execution command' >&2
  exit 1
fi
grep -n -- '--validate-contract' .github/workflows/validate-v1-implementation.yml
```

Expected: first command finds nothing; second finds the validation command.

- [ ] **Step 4: Run all three permitted validation commands**

Expected: unit tests pass; validation remains `UNEXECUTED`; existing frozen-record validator exits `0`.

- [ ] **Step 5: Commit**

```bash
git add experiments/research_seeds/live_alternative_diagnostic_mediation_v1/README.md .github/workflows/validate-v1-implementation.yml
git commit -m "docs: bind V1 implementation to unexecuted state"
```

---

### Task 7: Final implementation verification without scientific execution

**Files:** verification only.

**Interfaces:** legal terminal state is `IMPLEMENTED_NOT_EXECUTED / UNEXECUTED / NONE`.

- [ ] **Step 1: Run the complete unit suite**

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
```

Expected: zero failures and zero errors.

- [ ] **Step 2: Run structural validation and assert terminal state**

```bash
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py --validate-contract > /tmp/v1-contract-validation.json
python - <<'PY'
import json
from pathlib import Path
record = json.loads(Path('/tmp/v1-contract-validation.json').read_text())
assert record['protocol_state'] == 'FROZEN_PRE_EXECUTION_ASSAY'
assert record['execution_state'] == 'UNEXECUTED'
assert record['scientific_result'] == 'NONE'
contract = record['contract_validation']
for field in (
    'endpoint_nonidentifiability_verified','no_universal_diagnostic_verified',
    'pair_order_invariance_verified','marginal_information_matched',
    'joint_comparison_only_in_C1','read_only_mediator_verified',
    'mediator_ephemeral_verified','shared_menu_verified','budget_matched',
    'resolver_identity_matched',
):
    assert contract[field] is True, field
assert contract['null_disagreement_vector'] == [0,0]
assert contract['null_mediator_output'] == 'NO_DISCRIMINATING_DIAGNOSTIC'
print('V1 implementation contract validation: PASS / UNEXECUTED')
PY
```

- [ ] **Step 3: Re-run canonical frozen-record validation**

```bash
python scripts/validate_frozen_record.py
```

Expected: exit `0`.

- [ ] **Step 4: Verify protected artifacts and gates are byte-unchanged**

```bash
sha256sum -c /tmp/v1-protected-before.sha256
xargs -r sha256sum < /tmp/v1-gates.txt > /tmp/v1-gates-after.sha256
diff -u /tmp/v1-gates-before.sha256 /tmp/v1-gates-after.sha256
```

Expected: all protected files `OK`; gate diff has no output.

- [ ] **Step 5: Verify no scientific result artifact exists**

```bash
test ! -d experiments/research_seeds/live_alternative_diagnostic_mediation_v1/results
! find experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -type f \( -name 'result.json' -o -name 'summary.md' \) -print -quit | grep -q .
```

Expected: both commands exit `0`.

- [ ] **Step 6: Verify changed paths are implementation-only**

```bash
PLAN_BASE=$(cat /tmp/v1-plan-base.txt)
git diff --name-only "$PLAN_BASE"...HEAD | sort
```

Expected paths are restricted exactly to:

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

If a canonical ledger/index, existing gate, existing validator, or `experiments/results/` path appears, stop and repair before proceeding.

- [ ] **Step 7: Verify clean branch state and task-scoped history**

```bash
PLAN_BASE=$(cat /tmp/v1-plan-base.txt)
git status --short
git log --oneline --decorate "$PLAN_BASE"..HEAD
```

Expected: clean tree and task-scoped implementation commits only.

- [ ] **Step 8: STOP before scientific execution**

Do not run the scientific execution mode. Legal terminal state is exactly:

```text
protocol_state = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state = UNEXECUTED
scientific_result = NONE
```

A separate explicit user authorization is required before executing frozen V1.

---

## Execution Handoff Boundary

```text
implementation validation
!= scientific assay execution
!= scientific interpretation / promotion
```

Completing Tasks 1–7 may establish only that the implementation instantiates the approved finite design and that the scientific execution path remains unrun. It does not create a V1 empirical result and does not authorize V2.
