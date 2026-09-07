# Interface / MATRIX Research Seeds Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Plant the first noncanonical Interface Theory ↔ MATRIX research-seed layer with explicit epistemic standing, exact source anchors, conservative translation status, and no changes to frozen canonical evidence.

**Architecture:** The implementation is documentation-only and lives under `docs/research_seeds/`. Each file has one responsibility: navigation/standing, cross-program correspondence, shared mathematical abstraction, repair-aware bridge, adaptive-internal-interface hypothesis, and conceptual provenance. The existing canonical Interface Theory artifacts and frozen gates remain byte-unchanged; all new material is explicitly downstream and noncanonical.

**Tech Stack:** Markdown, Git, existing repository validation scripts / GitHub Actions, exact source-commit anchoring.

**Spec:** `docs/superpowers/specs/2026-09-07-interface-matrix-research-seeds-design.md`

## Global Constraints

- Work only on branch `research/interface-matrix-seeds-2026-09-07`.
- Canonical Interface Theory base is `61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5`.
- MATRIX source anchor is `5bca7ec6508e9d7ca1008ba745748281139fcfac`.
- Do not modify `docs/CANONICAL_RECORD.md`, `docs/RESULT_LEDGER.md`, `docs/EVIDENCE_INDEX.md`, Gate 013, Gate 014, Protocol Foundations, the Adaptive Capacity Measurement Charter, or its frozen first-claim ceiling.
- Every new research-seed file has canonical standing `NONCANONICAL_RESEARCH_SEED`.
- Structural resemblance never earns `IDENTICAL`, `REFINEMENT`, or `PROJECTION` without an explicit mapping argument.
- Default cross-program translation standing for the first Interface Theory ↔ MATRIX bridge is `NO_TRANSLATION_EARNED`.
- Preserve the blind-repair caveat: identifiability is not necessary when one valid repair works uniformly over the entire uncertainty cell.
- Preserve source hierarchy: source result → derived observation → candidate schema / hypothesis. Do not write “Interface Theory + MATRIX proves a new theorem.”
- Conceptual provenance is `CONCEPTUAL_PROVENANCE_ONLY` and `NOT_EVIDENCE`.
- No new Interface Theory gate, MATRIX assay, CNI/NOOA runtime, transformer implementation, or empirical performance claim is authorized by this plan.

---

## File Structure

**Modify:**
- `docs/research_seeds/README.md` — directory boundary, three-axis standing model, navigation, promotion rule.

**Create:**
- `docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md` — typed cross-repo correspondence records.
- `docs/research_seeds/BLOCKWISE_ADEQUACY_POSET_V0.md` — candidate common mathematical schema only.
- `docs/research_seeds/REPAIR_AWARE_INTERFACE_BRIDGE_V0.md` — blind repair, diagnostic refinement, and the limit of static factorization.
- `docs/research_seeds/ADAPTIVE_INTERNAL_INTERFACES_V0.md` — architecture hypothesis and separated achievement levels.
- `docs/research_seeds/CONCEPTUAL_PROVENANCE_V0.md` — idea-generating lineage only.

**Verification only:**
- existing repository validation / integrity tooling;
- `git diff`, `git status`, and content searches for accidental promotion language.

---

### Task 1: Establish the isolated execution baseline

**Files:**
- Read: `docs/superpowers/specs/2026-09-07-interface-matrix-research-seeds-design.md`
- Read: `docs/research_seeds/README.md`
- Read: `docs/CANONICAL_RECORD.md`
- Read: `docs/RESULT_LEDGER.md`
- Read: `docs/EVIDENCE_INDEX.md`

**Interfaces:**
- Consumes: branch `research/interface-matrix-seeds-2026-09-07` and spec above.
- Produces: verified execution baseline with no unstaged changes and exact base ancestry.

- [ ] **Step 1: Create or enter an isolated worktree for the existing research branch**

Run from a clean clone:

```bash
git fetch origin
git worktree add ../interface-theory-seeds research/interface-matrix-seeds-2026-09-07
cd ../interface-theory-seeds
```

If the branch is already checked out elsewhere, create the worktree from the remote branch without moving the branch ref:

```bash
git worktree add --detach ../interface-theory-seeds origin/research/interface-matrix-seeds-2026-09-07
cd ../interface-theory-seeds
git switch -c research/interface-matrix-seeds-2026-09-07-work
```

Expected: isolated working directory based on the approved research-seed branch. Do not execute the detached fallback unless Git reports the branch is already checked out.

- [ ] **Step 2: Verify ancestry and working-tree cleanliness**

Run:

```bash
git status --short
git merge-base --is-ancestor 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5 HEAD
git log --oneline --decorate -5
```

Expected:

```text
# git status --short: no output
# merge-base command: exit 0
# log includes the approved design and pre-existing research-seed README commits
```

- [ ] **Step 3: Record baseline hashes for protected canonical files**

Run:

```bash
sha256sum \
  docs/CANONICAL_RECORD.md \
  docs/RESULT_LEDGER.md \
  docs/EVIDENCE_INDEX.md \
  ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md \
  FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md \
  > /tmp/interface-theory-protected-before.sha256
```

Then locate Gate 013/014 tracked files:

```bash
git ls-files '*gate_013*' '*gate_014*' | sort > /tmp/interface-theory-gates.txt
xargs -r sha256sum < /tmp/interface-theory-gates.txt > /tmp/interface-theory-gates-before.sha256
```

Expected: both files under `/tmp` contain hashes and no command errors.

- [ ] **Step 4: Read the spec and current seed README before editing**

Run:

```bash
sed -n '1,260p' docs/superpowers/specs/2026-09-07-interface-matrix-research-seeds-design.md
sed -n '1,220p' docs/research_seeds/README.md
```

Expected: the spec states the three-axis standing model and the README states the noncanonical boundary.

- [ ] **Step 5: Commit nothing for baseline setup**

Expected: Task 1 leaves the repository byte-identical.

---

### Task 2: Upgrade the research-seed README into the standing/navigation contract

**Files:**
- Modify: `docs/research_seeds/README.md`

**Interfaces:**
- Consumes: standing model from the approved spec.
- Produces: one directory-level contract that every later seed file can reference.

- [ ] **Step 1: Replace the flat standing list with three orthogonal standing axes**

The README must contain these exact categories:

```text
Evidence standing:
SOURCE_RESULT
DERIVED_MATHEMATICAL_OBSERVATION
CANDIDATE_SHARED_SCHEMA
EXPERIMENTAL_HYPOTHESIS
CONCEPTUAL_PROVENANCE_ONLY
NOT_EVIDENCE

Cross-program translation standing:
IDENTICAL
REFINEMENT
PROJECTION
ANALOGY
NO_TRANSLATION_EARNED

Canonical standing:
NONCANONICAL_RESEARCH_SEED
```

Also state explicitly:

```text
A file may be CANDIDATE_SHARED_SCHEMA + NO_TRANSLATION_EARNED + NONCANONICAL_RESEARCH_SEED.
```

- [ ] **Step 2: Add navigation for all five substantive seed files**

Add a table with columns:

```text
File | Role | Evidence standing | Translation standing | Canonical standing
```

Use these initial rows:

```text
CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md | typed cross-repo ledger | mixed per entry | mixed per entry, conservative default | NONCANONICAL_RESEARCH_SEED
BLOCKWISE_ADEQUACY_POSET_V0.md | candidate shared mathematical schema | CANDIDATE_SHARED_SCHEMA | NO_TRANSLATION_EARNED | NONCANONICAL_RESEARCH_SEED
REPAIR_AWARE_INTERFACE_BRIDGE_V0.md | candidate repair-aware bridge | CANDIDATE_SHARED_SCHEMA | NO_TRANSLATION_EARNED | NONCANONICAL_RESEARCH_SEED
ADAPTIVE_INTERNAL_INTERFACES_V0.md | architecture hypothesis | EXPERIMENTAL_HYPOTHESIS | NO_TRANSLATION_EARNED | NONCANONICAL_RESEARCH_SEED
CONCEPTUAL_PROVENANCE_V0.md | idea-generating lineage | CONCEPTUAL_PROVENANCE_ONLY / NOT_EVIDENCE | NO_TRANSLATION_EARNED | NONCANONICAL_RESEARCH_SEED
```

- [ ] **Step 3: Preserve and sharpen the no-promotion rules**

The README must retain these exact distinctions:

```text
similar notation != identical object
similar structure != refinement
finite correspondence != general law
successful architecture != target validation
provenance != causal attribution
```

Add:

```text
shared abstraction != source-result identity
source-side witness != cross-program translation proof
implementation success != mechanism attribution
```

- [ ] **Step 4: Verify README boundary language**

Run:

```bash
grep -nE 'NONCANONICAL_RESEARCH_SEED|NO_TRANSLATION_EARNED|similar structure != refinement|Promotion' docs/research_seeds/README.md
```

Expected: all four concepts are present.

- [ ] **Step 5: Commit the README contract update**

Run:

```bash
git add docs/research_seeds/README.md
git commit -m "docs: type research-seed standings"
```

Expected: one commit modifying only the README.

---

### Task 3: Create the typed cross-program correspondence ledger

**Files:**
- Create: `docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md`

**Interfaces:**
- Consumes: exact source commits and the README standing vocabulary.
- Produces: auditable correspondence entries whose unresolved mismatches are explicit.

- [ ] **Step 1: Create the ledger header and entry schema**

The file must begin with:

```text
Evidence standing: DERIVED_MATHEMATICAL_OBSERVATION / CANDIDATE_SHARED_SCHEMA as declared per entry
Translation standing: NO_TRANSLATION_EARNED unless an entry explicitly earns another status
Canonical standing: NONCANONICAL_RESEARCH_SEED
```

Pin sources:

```text
Interface Theory source anchor: 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5
MATRIX source anchor: 5bca7ec6508e9d7ca1008ba745748281139fcfac
```

Define each ledger entry with these fields:

```text
entry_id
source_program
source_commit
source_artifact
source_object
candidate_target_program
candidate_target_object
evidence_standing
translation_standing
conditions
preserved_distinctions
lost_or_unmapped_distinctions
unresolved_mismatch
evidence_or_witness
claim_ceiling
```

- [ ] **Step 2: Add entry CP-001 — factorization / target-homogeneous quotient ↔ representation safety**

Source-side content to preserve:

```math
L=\widehat L\circ O
```

and:

```math
\mathrm{Safe}_B(g\mid G)
\iff
\forall m\in\mathrm{im}(g),\ g^{-1}(m)\in\Phi_B(G).
```

Required mismatch statement:

```text
Interface Theory adequacy is functional target homogeneity under a declared observation interface.
MATRIX safety is bounded joint correctability of representation cells under system-relative diagnostics, policy, repair, cost, and budget semantics.
These are not the same scientific object.
```

Set translation standing:

```text
NO_TRANSLATION_EARNED
```

- [ ] **Step 3: Add entry CP-002 — incomparable minimum interfaces ↔ no coarsest safe representation**

Record source-side witness:

```text
Interface Theory Gate 014: three incomparable minimum informative interfaces in the frozen finite probe vocabulary.
```

Record MATRIX-side source statement:

```text
A coarsest safe representation need not exist when future experiments are available; several incomparable compressions may remain safe while their common coarsening is unsafe.
```

Required claim ceiling:

```text
Candidate shared order-theoretic pattern only. No claim that the two source results are instances of one proved cross-repo theorem.
```

Set translation standing:

```text
NO_TRANSLATION_EARNED
```

- [ ] **Step 4: Add entry CP-003 — adaptive protocol observation ↔ constructible diagnostics**

Record Interface Theory source object:

```math
P:(A\times Y)^*\to A\cup\{\texttt{stop}\},
\qquad O_P(f)=\operatorname{Exec}(P,f).
```

Record candidate MATRIX relation:

```text
Q_t = diagnostic procedures constructible from primitive affordances U_t.
```

Required unresolved mismatch:

```text
MATRIX additionally quantifies over repair validity, executable policy selection, grounded cost, remaining resources, and whole-set correction. Protocol-generated observability alone does not identify the corrective frontier.
```

- [ ] **Step 5: Add entry CP-004 — CNI/NOOA recursive-update surface ↔ adaptive-internal-interface hypothesis**

Anchor source artifact:

```text
docs/cni_nooa_candidate.md
```

Record only the source-side candidate loop:

```text
state -> proposed change -> execution -> consequence -> generator update
```

and:

```math
G_{t+1}=\Gamma(G_t,\Omega_t).
```

Required claim ceiling:

```text
CNI/NOOA is a candidate implementation substrate, not evidence for the internal-interface architecture hypothesis and not an earned mapping to it.
```

Translation standing:

```text
NO_TRANSLATION_EARNED
```

- [ ] **Step 6: Verify all ledger entries have anchors and conservative translation standing**

Run:

```bash
grep -n '61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5' docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md
grep -n '5bca7ec6508e9d7ca1008ba745748281139fcfac' docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md
grep -n 'NO_TRANSLATION_EARNED' docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md
```

Expected: both source anchors are present and every initial entry is conservatively typed.

- [ ] **Step 7: Commit the ledger**

Run:

```bash
git add docs/research_seeds/CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md
git commit -m "docs: add cross-program correspondence ledger"
```

---

### Task 4: Create the blockwise hereditary adequacy seed

**Files:**
- Create: `docs/research_seeds/BLOCKWISE_ADEQUACY_POSET_V0.md`

**Interfaces:**
- Consumes: CP-001 and CP-002 as source-motivated observations.
- Produces: one abstract mathematical schema whose source-specific instantiations remain explicitly separate.

- [ ] **Step 1: Write the standing block prominently at the top**

Use:

```text
Evidence standing: CANDIDATE_SHARED_SCHEMA
Translation standing: NO_TRANSLATION_EARNED
Canonical standing: NONCANONICAL_RESEARCH_SEED

WARNING: This file defines an abstract comparison schema. It does not establish that Interface Theory and MATRIX use the same scientific object, the same poset presentation, or an earned translation.
```

- [ ] **Step 2: Define the abstract blockwise adequacy schema**

Include:

```math
A(C)\land C'\subseteq C\Longrightarrow A(C').
```

and:

```math
\operatorname{Adeq}(P)
\iff
\forall C\in P,\ A(C).
```

Define refinement orientation explicitly so no later reader has to infer it:

```text
P \preceq Q means Q is at least as fine as P (every block of Q is contained in a block of P).
```

Then derive:

```math
\operatorname{Adeq}(P)\land P\preceq Q
\Longrightarrow
\operatorname{Adeq}(Q).
```

- [ ] **Step 3: State only the elementary order-theoretic consequences actually used**

For a finite declared search space, state:

```text
- adequate structures form an upward-closed subset under the chosen refinement orientation;
- minimal adequate elements form an antichain;
- upward closure does not imply a unique least adequate element;
- therefore a canonical least sufficient structure is not guaranteed by the abstract schema.
```

Do not call these consequences novel.

- [ ] **Step 4: Record Interface Theory as one candidate instantiation**

Use:

```math
A_L(C)\iff L\text{ is constant on }C.
```

Explain:

```text
Observation maps induce partitions of the declared system class. Factorization means each observational block is target-homogeneous. Gate 014 supplies a finite source-side example with multiple incomparable minimum probe interfaces in its frozen vocabulary.
```

- [ ] **Step 5: Record MATRIX as a separate candidate instantiation**

Use:

```math
A_{\Phi}(C)\iff C\in\Phi_B(G).
```

Explain:

```text
Representation maps induce uncertainty cells. MATRIX's finite corrective frontier is downward closed, so safety of every cell is preserved by refining the representation. MATRIX separately notes that a coarsest safe representation need not exist when future experiments are allowed.
```

- [ ] **Step 6: Add the explicit non-identity section**

Include all of:

```text
same hereditary shape != same semantics
same monotonicity != same adequacy predicate
same antichain phenomenon != same theorem
source-side witnesses != cross-program proof
```

- [ ] **Step 7: Verify warning and non-identity language**

Run:

```bash
grep -nE 'WARNING|NO_TRANSLATION_EARNED|same antichain phenomenon != same theorem|canonical least sufficient structure is not guaranteed' docs/research_seeds/BLOCKWISE_ADEQUACY_POSET_V0.md
```

Expected: all four are present.

- [ ] **Step 8: Commit the mathematical seed**

Run:

```bash
git add docs/research_seeds/BLOCKWISE_ADEQUACY_POSET_V0.md
git commit -m "docs: derive blockwise adequacy research seed"
```

---

### Task 5: Create the repair-aware interface bridge

**Files:**
- Create: `docs/research_seeds/REPAIR_AWARE_INTERFACE_BRIDGE_V0.md`

**Interfaces:**
- Consumes: Interface Theory identifiability as a source concept and MATRIX repair/frontier semantics as a separate source concept.
- Produces: one explicitly limited bridge for terminal/one-step repair plus a pointer back to the general adaptive frontier.

- [ ] **Step 1: Write the standing and caveat first**

Use:

```text
Evidence standing: CANDIDATE_SHARED_SCHEMA
Translation standing: NO_TRANSLATION_EARNED
Canonical standing: NONCANONICAL_RESEARCH_SEED

Core caveat:
Identification is required only when successful correction must condition on distinctions inside the current uncertainty set. If one valid repair works for all members, blind correction is possible without identification.
```

- [ ] **Step 2: Define the terminal repair relation special case**

Let:

```math
R(x)\subseteq A
```

be the set of valid terminal repairs/actions for state `x`.

State blind repair condition:

```math
\bigcap_{x\in S}R(x)\neq\varnothing.
```

Interpretation:

```text
There exists at least one repair valid for every state still possible in S; no further state discrimination is necessary for this terminal decision.
```

- [ ] **Step 3: Define observation-induced repair adequacy**

For observation/diagnostic map:

```math
O:S\to H,
```

with cells:

```math
C_h=O^{-1}(h),
```

state terminal sufficiency:

```math
\forall h,\qquad
\bigcap_{x\in C_h}R(x)\neq\varnothing.
```

Interpretation:

```text
The observation need not identify the exact state. It only has to refine uncertainty enough that each residual cell admits a common valid terminal repair.
```

- [ ] **Step 4: Explain the connection to functional factorization without equating them**

Include:

```text
If every state has a unique required repair label L(x), terminal repair adequacy reduces to target homogeneity on observation cells and can be represented by ordinary factorization. If repairs are set-valued, multiple states may remain safely conflated because their valid-repair sets overlap.
```

- [ ] **Step 5: Restore the general MATRIX boundary**

State explicitly:

```text
The intersection condition is not the general MATRIX frontier. In MATRIX, a policy may choose multiple diagnostics adaptively, consume resources, update its residual uncertainty, and then execute repair. General adequacy remains S in Phi_B(G), not the terminal intersection formula.
```

Include:

```math
S\in\Phi_B(G)
\iff
\exists\pi,\ \mathrm{cost}(\pi)\le B,\ \forall x\in S:\ \pi\text{ diagnoses and validly repairs }x.
```

- [ ] **Step 6: Add failure cases that prevent overtranslation**

Record:

```text
- factorization failure for an exact state label does not imply correction failure if blind repair exists;
- target identifiability does not imply executable policy availability;
- an observationally sufficient diagnostic may exceed the corrective budget;
- a static observation map may be insufficient while an adaptive diagnostic protocol succeeds;
- stored distinctions may be inaccessible to policy selection.
```

- [ ] **Step 7: Verify the blind-repair caveat and general-boundary wording**

Run:

```bash
grep -nE 'blind correction|not the general MATRIX frontier|NO_TRANSLATION_EARNED|valid-repair sets overlap' docs/research_seeds/REPAIR_AWARE_INTERFACE_BRIDGE_V0.md
```

Expected: all four are present.

- [ ] **Step 8: Commit the repair-aware bridge**

Run:

```bash
git add docs/research_seeds/REPAIR_AWARE_INTERFACE_BRIDGE_V0.md
git commit -m "docs: add repair-aware interface bridge seed"
```

---

### Task 6: Create the adaptive internal-interface architecture hypothesis

**Files:**
- Create: `docs/research_seeds/ADAPTIVE_INTERNAL_INTERFACES_V0.md`

**Interfaces:**
- Consumes: blockwise adequacy seed, repair-aware bridge, and CNI/NOOA only as candidate provenance/substrate context.
- Produces: a falsifiable architecture hypothesis with no implementation or performance claim.

- [ ] **Step 1: Write the standing block and hypothesis**

Use:

```text
Evidence standing: EXPERIMENTAL_HYPOTHESIS
Translation standing: NO_TRANSLATION_EARNED
Canonical standing: NONCANONICAL_RESEARCH_SEED
```

Hypothesis:

```text
An adaptive system may benefit from maintaining multiple incomparable sufficient internal interfaces rather than forcing one canonical representation.
```

Immediately add:

```text
This is not a claim that multiple interfaces are generally superior, that such an antichain will emerge in neural training, or that Interface Theory / MATRIX already validate this architecture.
```

- [ ] **Step 2: Define the internal communication object schematically**

Use:

```math
I_{A\to B}:H_A\to M_B.
```

State:

```text
I_{A->B} induces collisions on upstream states. For a declared downstream target or corrective contract, those collisions may be adequate or inadequate. The scientific question is target-relative, not whether the interface is globally information-preserving.
```

- [ ] **Step 3: Separate the three interface meanings**

Include this exact table:

```text
Internal computational interface | learned or fixed message/adapter between model components
Scientific observation/intervention interface | what an evaluator may observe or manipulate to identify a declared target
Corrective/environmental interface | affordances through which the deployed system can obtain evidence and execute correction
```

State:

```text
These interfaces may interact causally but are not interchangeable types.
```

- [ ] **Step 4: Separate the three achievement levels**

Use:

```text
A1: preserve competing state during one episode
A2: construct a temporary interaction interface between competing structures
A3: learn and retain a reusable interface across episodes
```

Then state:

```text
A1 does not imply A2. A2 does not imply A3. Each requires a separate assay and mechanism attribution.
```

- [ ] **Step 5: Record the antichain-inspired design possibility conservatively**

Use:

```math
\mathcal M_t=\{I_1,\ldots,I_k\}
```

only as schematic notation for a set of currently non-dominated interfaces under a declared adequacy/cost order.

State:

```text
The candidate design does not preserve every historical branch. It preserves multiple interfaces only while no declared replacement dominates them under the relevant target/corrective contract and resource model.
```

- [ ] **Step 6: Freeze the first experimental decomposition without designing the experiment**

Record only the future questions:

```text
E1: Does explicit preservation of alternatives improve later revision under matched memory and compute?
E2: Does a temporary learned interface add benefit beyond preserved alternatives alone?
E3: Does retaining an interface across episodes improve fresh-problem adaptation rather than memorize prior cases?
E4: Do any gains expand a corrective frontier or merely improve average task performance?
```

Do not specify a benchmark, model size, training schedule, or success threshold in this planting.

- [ ] **Step 7: Verify hypothesis/nonclaim separation**

Run:

```bash
grep -nE 'EXPERIMENTAL_HYPOTHESIS|A1 does not imply A2|not a claim that multiple interfaces are generally superior|NO_TRANSLATION_EARNED' docs/research_seeds/ADAPTIVE_INTERNAL_INTERFACES_V0.md
```

Expected: all required guardrails are present.

- [ ] **Step 8: Commit the architecture hypothesis**

Run:

```bash
git add docs/research_seeds/ADAPTIVE_INTERNAL_INTERFACES_V0.md
git commit -m "docs: plant adaptive internal-interface hypothesis"
```

---

### Task 7: Create the conceptual provenance record

**Files:**
- Create: `docs/research_seeds/CONCEPTUAL_PROVENANCE_V0.md`

**Interfaces:**
- Consumes: the conversational/intellectual lineage only.
- Produces: a provenance record that cannot be mistaken for evidence.

- [ ] **Step 1: Write the standing block**

Use:

```text
Evidence standing: CONCEPTUAL_PROVENANCE_ONLY / NOT_EVIDENCE
Translation standing: NO_TRANSLATION_EARNED
Canonical standing: NONCANONICAL_RESEARCH_SEED
```

- [ ] **Step 2: Record the provenance chain without claiming author intent**

Preserve the sequence:

```text
structural interpretation of the supplied artwork
-> inferred transformation grammar
-> speculative transformer/internal-interface translation
-> MATRIX comparison
-> Interface Theory loop-back
-> Kevin Kelly, Out of Control
-> Jean Baudrillard, Simulacres et Simulation
-> Jakub Pachocki / OpenAI, An Alien Mind
-> cross-model adversarial reduction and repair of the synthesis
```

For the artwork state:

```text
The artwork was used as a generative prompt for structural hypotheses. No claim is made that the artist intended the resulting computational or scientific interpretation.
```

- [ ] **Step 3: Record what each source contributed as question-generation only**

Use bounded descriptions:

```text
Artwork: recurring modules, local coordinate systems, interfaces, preserved separations, transformation-with-repetition.
Kelly: grown/adaptive organization, distributed control, change that changes itself.
Baudrillard: model/world feedback and self-validating representation loops as a cautionary conceptual lens.
Pachocki/OpenAI: grown neural systems, monitoring generalization, AI participation in AI research, and recursive-improvement control concerns.
Cross-model critique: pruned overclaims, preserved blind-repair caveat, separated temporary state/interfaces/persistent interfaces, and exposed the candidate shared-poset schema.
```

Precede the list with:

```text
None of these items supplies evidentiary support for Interface Theory, MATRIX, or the adaptive-internal-interface hypothesis.
```

- [ ] **Step 4: Add provenance-to-science firewall**

Include:

```text
idea source != evidence source
conceptual resonance != translation
historical influence != mechanism proof
author wording != program claim
```

- [ ] **Step 5: Verify all conceptual items are explicitly non-evidentiary**

Run:

```bash
grep -nE 'CONCEPTUAL_PROVENANCE_ONLY|NOT_EVIDENCE|No claim is made that the artist intended|None of these items supplies evidentiary support' docs/research_seeds/CONCEPTUAL_PROVENANCE_V0.md
```

Expected: all four guardrails are present.

- [ ] **Step 6: Commit the provenance record**

Run:

```bash
git add docs/research_seeds/CONCEPTUAL_PROVENANCE_V0.md
git commit -m "docs: record conceptual provenance for research seeds"
```

---

### Task 8: Final hostile verification and branch integrity gate

**Files:**
- Modify only if a verification failure requires correction: `docs/research_seeds/**`
- Do not modify protected canonical files.

**Interfaces:**
- Consumes: all seed files from Tasks 2–7.
- Produces: verified branch whose new claims remain within the approved noncanonical ceiling.

- [ ] **Step 1: Verify protected canonical files are byte-identical to Task 1 baseline**

Run:

```bash
sha256sum \
  docs/CANONICAL_RECORD.md \
  docs/RESULT_LEDGER.md \
  docs/EVIDENCE_INDEX.md \
  ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md \
  FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md \
  > /tmp/interface-theory-protected-after.sha256

diff -u /tmp/interface-theory-protected-before.sha256 /tmp/interface-theory-protected-after.sha256

xargs -r sha256sum < /tmp/interface-theory-gates.txt > /tmp/interface-theory-gates-after.sha256
diff -u /tmp/interface-theory-gates-before.sha256 /tmp/interface-theory-gates-after.sha256
```

Expected: both `diff` commands produce no output and exit 0.

- [ ] **Step 2: Verify branch scope**

Run:

```bash
git diff --name-only 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5...HEAD
```

Expected changed paths are limited to:

```text
docs/research_seeds/**
docs/superpowers/specs/2026-09-07-interface-matrix-research-seeds-design.md
docs/superpowers/plans/2026-09-07-interface-matrix-research-seeds.md
```

No canonical or experiment file may appear.

- [ ] **Step 3: Run the repository's existing validation/integrity command**

First discover the canonical command rather than guessing:

```bash
find . -maxdepth 3 -type f \( -name 'validate*.py' -o -name '*integrity*.py' -o -name 'pyproject.toml' -o -name 'Makefile' \) -print
```

Read `.github/workflows/*` and the discovered validation entrypoint. Run the same validation command the repository itself uses for canonical integrity. Do not invent a substitute validator.

Expected: PASS. If the validator rejects documentation-only additions because a canonical registry must enumerate every file, stop and report the conflict; do not alter canonical registries without a separate design decision.

- [ ] **Step 4: Search for accidental promotion language**

Run:

```bash
grep -RniE '\b(proves|establishes|is equivalent to|is the same as|validates MATRIX|validates Interface Theory)\b' docs/research_seeds || true
```

Review every hit manually.

Allowed examples:

```text
"does not establish"
"does not prove"
"not equivalent"
```

Disallowed examples include an unqualified statement that the shared schema proves equivalence or validates either source program.

- [ ] **Step 5: Search for standing completeness**

Run:

```bash
for f in docs/research_seeds/*.md; do
  echo "=== $f ==="
  grep -E 'Evidence standing|Translation standing|Canonical standing|Status:' "$f" || true
done
```

Expected: every substantive seed file exposes its standing; README exposes directory status/standing model.

- [ ] **Step 6: Verify source anchors and blind-repair caveat remain present**

Run:

```bash
grep -Rnl '61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5' docs/research_seeds
grep -Rnl '5bca7ec6508e9d7ca1008ba745748281139fcfac' docs/research_seeds
grep -n 'blind' docs/research_seeds/REPAIR_AWARE_INTERFACE_BRIDGE_V0.md
```

Expected: exact source anchors occur in the ledger and/or source sections; blind-repair language is explicit.

- [ ] **Step 7: Review the complete diff as a scientific claim audit**

Run:

```bash
git diff --stat 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5...HEAD
git diff --check 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5...HEAD
git diff 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5...HEAD -- docs/research_seeds
```

Review specifically for:

```text
source result being rewritten as a derived result
candidate schema being called an earned translation
blind repair being omitted
terminal repair condition replacing Phi_B
architecture hypothesis being presented as evidence
conceptual provenance being cited as support
```

Expected: none occur.

- [ ] **Step 8: If verification repairs were necessary, commit them separately**

Only if a prior step found a real defect:

```bash
git add docs/research_seeds
git commit -m "docs: tighten research-seed claim boundaries"
```

If no repairs were needed, do not create an empty commit.

- [ ] **Step 9: Confirm clean terminal state**

Run:

```bash
git status --short
git log --oneline --decorate 61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5..HEAD
```

Expected:

```text
# status: no output
# log: design/plan plus one reviewable commit per substantive planting task, and an optional final boundary-fix commit only if needed
```

---

## Plan Self-Review Record

**Spec coverage:**
- noncanonical layer boundary → Tasks 2 and 8;
- three-axis standing model → Task 2;
- typed correspondence ledger → Task 3;
- blockwise hereditary adequacy schema → Task 4;
- blind-repair caveat / general MATRIX boundary → Task 5;
- adaptive internal-interface hypothesis and type separation → Task 6;
- conceptual provenance only → Task 7;
- exact source anchoring → Tasks 3 and 8;
- canonical/gate byte-preservation → Tasks 1 and 8;
- hostile promotion-language audit → Task 8;
- no implementation / new assay / canonical promotion → Global Constraints and all tasks.

**Placeholder scan:** No `TBD`, `TODO`, “implement later,” or unspecified test steps remain.

**Type consistency:** The plan uses the same standing vocabulary, commit anchors, file names, and three interface types defined in the approved spec.
