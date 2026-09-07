# Interface Theory / MATRIX Research-Seed Layer — Design

**Status:** design for a noncanonical research-seed layer. No canonical Interface Theory result, frozen gate, Adaptive Capacity claim profile, or MATRIX result is modified by this design.

**Branch:** `research/interface-matrix-seeds-2026-09-07`

**Canonical Interface Theory base:** `61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5`

**MATRIX source anchor:** `5bca7ec6508e9d7ca1008ba745748281139fcfac`

**Pre-existing branch state:** the branch already contains `docs/research_seeds/README.md` at commit `df4c5e642cc08ef8d5b3cc91d2a7946cbb5c0c3f`. That file establishes the intended noncanonical boundary. This design treats it as existing branch state and does not interpret its presence as canonical promotion.

## 1. Purpose

Preserve the useful cross-program observations developed around Interface Theory, MATRIX, corrective possibility, adaptive internal interfaces, and their conceptual provenance without changing the standing of any already-frozen result.

The layer is deliberately downstream of the canonical record:

```text
canonical Interface Theory / frozen evidence
        ↓
noncanonical cross-program research seeds
        ↓
possible later derivation, translation, or experiment
        ↓
separate promotion change only if earned
```

The first planting has three scientific jobs:

1. record a candidate shared order-theoretic schema between Interface Theory target-preserving interfaces and MATRIX representation safety;
2. state a repair-aware bridge that preserves the distinction between identifying a state and correcting it;
3. preserve an adaptive-internal-interface architecture hypothesis without treating it as evidence or implementation.

A fourth file records idea-generating provenance only.

## 2. Hard boundaries

This work must not modify or reinterpret:

- `docs/CANONICAL_RECORD.md`;
- `docs/RESULT_LEDGER.md`;
- `docs/EVIDENCE_INDEX.md`;
- Gate 013;
- Gate 014;
- Protocol Foundations;
- the frozen Adaptive Capacity Measurement Charter;
- the frozen `C_1` / `C_2` first claim ceiling;
- any MATRIX frozen kernel, assay, result, or claim ceiling.

No research-seed document may imply that a structural resemblance is an earned cross-program translation.

The following remain distinct:

```text
source result
!= derived mathematical observation
!= candidate shared schema
!= earned translation
!= experimental hypothesis
!= conceptual provenance
!= evidence
```

## 3. Standing model

The current `docs/research_seeds/README.md` uses one flat list of permitted labels. The implementation should refine this into three orthogonal fields so that epistemic standing, translation standing, and canonical standing cannot be conflated.

### 3.1 Evidence standing

Allowed values:

```text
SOURCE_RESULT
DERIVED_MATHEMATICAL_OBSERVATION
CANDIDATE_SHARED_SCHEMA
EXPERIMENTAL_HYPOTHESIS
CONCEPTUAL_PROVENANCE_ONLY
NOT_EVIDENCE
```

### 3.2 Cross-program translation standing

Use the MATRIX translation vocabulary where applicable:

```text
IDENTICAL
REFINEMENT
PROJECTION
ANALOGY
NO_TRANSLATION_EARNED
```

For the first Interface Theory ↔ MATRIX bridge, the default is:

```text
NO_TRANSLATION_EARNED
```

A candidate common abstraction may still be recorded while this remains the translation standing.

### 3.3 Canonical standing

Every file in this layer begins as:

```text
NONCANONICAL_RESEARCH_SEED
```

Promotion requires a separate reviewed change that names the missing argument or evidence and updates the appropriate canonical artifact. Promotion is never implied by age, repetition, citation, or successful implementation.

## 4. Files and responsibilities

The first planting should contain:

```text
docs/research_seeds/
├── README.md
├── CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md
├── BLOCKWISE_ADEQUACY_POSET_V0.md
├── REPAIR_AWARE_INTERFACE_BRIDGE_V0.md
├── ADAPTIVE_INTERNAL_INTERFACES_V0.md
└── CONCEPTUAL_PROVENANCE_V0.md
```

### 4.1 `README.md`

Role: boundary and navigation only.

It must:

- state that the directory is noncanonical;
- define the three-axis standing model above;
- identify authoritative frozen artifacts;
- link the seed files;
- state the promotion rule;
- avoid scientific claims beyond summarizing the standing of the seed records.

### 4.2 `CROSS_PROGRAM_CORRESPONDENCE_LEDGER.md`

Role: typed cross-repo ledger.

Each entry should record:

```text
entry_id
source_program
source_commit
source_object
candidate_target_object
source_evidence_standing
translation_standing
conditions
preserved_distinctions
lost_or_unmapped_distinctions
unresolved_mismatch
evidence_or_witness
claim_ceiling
```

Initial entries should include at least:

- Interface Theory factorization / target-homogeneous quotient ↔ MATRIX representation safety;
- Interface Theory minimal identifying interfaces ↔ MATRIX no-coarsest-safe-representation observation;
- Protocol-generated adaptive observation ↔ MATRIX diagnostic procedures, with explicit mismatch because MATRIX additionally includes repair, policy, cost, and frontier semantics;
- CNI/NOOA candidate recursive update surface ↔ adaptive internal-interface hypothesis, with `NO_TRANSLATION_EARNED` unless an exact mapping is separately established.

### 4.3 `BLOCKWISE_ADEQUACY_POSET_V0.md`

Role: derived mathematical seed only.

Define a common information-structure abstraction without rewriting either source program.

For a set `X`, let an information structure induce a partition `P` of `X`. Let `A(C)` be a predicate on blocks that is hereditary under subsets:

```math
A(C) \land C'\subseteq C \Longrightarrow A(C').
```

Define partition adequacy by:

```math
\operatorname{Adeq}(P)
\iff
\forall C\in P,\ A(C).
```

Under the refinement order, adequacy is monotone under refinement. Therefore minimal adequate elements, when they exist in a finite declared search space, form an antichain. A unique least adequate structure is not guaranteed by the abstract schema.

Record two candidate instantiations separately:

Interface Theory:

```math
A_L(C)
\iff
L\text{ is constant on }C.
```

MATRIX:

```math
A_{\Phi}(C)
\iff
C\in\Phi_B(G).
```

The record must explicitly state:

```text
shared abstract shape apparent
!= same scientific object
!= same poset presentation
!= earned translation
```

Gate 014's incomparable minimal probe interfaces and MATRIX's no-coarsest-safe-representation result are source-side witnesses motivating the comparison, not proof that the two repo results are identical.

### 4.4 `REPAIR_AWARE_INTERFACE_BRIDGE_V0.md`

Role: candidate bridge between target identifiability and corrective possibility.

The file must preserve the caveat:

```text
identification is required only when successful correction must condition on distinctions inside the current uncertainty set.
```

For a terminal or one-step repair relation `R(x)`, blind repair is possible on `S` when:

```math
\bigcap_{x\in S}R(x)\neq\varnothing.
```

If an observation or diagnostic induces cells `C`, that observation is sufficient for one-step repair when:

```math
\forall C,\quad
\bigcap_{x\in C}R(x)\neq\varnothing.
```

This is only a terminal special case. The general MATRIX object is adaptive and budgeted: a transcript leaves a residual uncertainty set plus remaining resources, and adequacy depends on the existence of a valid continuation policy. The bridge should therefore point back to `\Phi_B(G)` rather than replacing it with the intersection condition.

The file must not claim that Interface Theory factorization is necessary for all correction. A uniform policy can repair an entire uncertainty cell without distinguishing its members.

### 4.5 `ADAPTIVE_INTERNAL_INTERFACES_V0.md`

Role: architecture hypothesis only.

Candidate hypothesis:

```text
An adaptive system may benefit from maintaining multiple incomparable sufficient internal interfaces rather than forcing one canonical representation.
```

Model an internal communication map schematically as:

```math
I_{A\to B}:H_A\to M_B.
```

The map induces an information partition on upstream states. A downstream task may require that the induced collisions remain adequate for the relevant target or corrective contract.

The file must keep three achievements separate:

```text
preserving competing state during one episode
!= constructing a temporary interaction interface
!= learning and retaining a reusable interface across episodes
```

It should also distinguish:

```text
internal computational interface
!= scientific observation/intervention interface
!= corrective/environmental interface
```

No transformer implementation, benchmark, or performance claim belongs in this first planting.

### 4.6 `CONCEPTUAL_PROVENANCE_V0.md`

Role: preserve idea-generating lineage only.

It may record that the research path was sharpened through:

- structural interpretation of the supplied artwork;
- Kevin Kelly, *Out of Control*;
- Jean Baudrillard, *Simulacres et Simulation*;
- Jakub Pachocki / OpenAI, *An Alien Mind*;
- subsequent cross-model critique and reduction.

Every such item must be marked:

```text
CONCEPTUAL_PROVENANCE_ONLY
NOT_EVIDENCE
```

The file must not attribute the derived research ideas to the artist or authors as intended meanings unless a source explicitly establishes that intent.

## 5. Source anchoring

Every cross-program claim should be pinned to exact source versions.

Minimum anchors for this planting:

```text
Interface Theory:
61bef6c4eb9ee46cc38ac85a2f91874f9f8642a5

MATRIX:
5bca7ec6508e9d7ca1008ba745748281139fcfac
```

Where a claim depends on a specific artifact, name the artifact explicitly rather than citing only the repository root.

No later repository change may silently alter the meaning of an existing correspondence entry; a changed source requires a new or amended entry with provenance.

## 6. Data flow / epistemic flow

The intended flow is:

```text
frozen source result
        ↓
exact source object and commit
        ↓
derived structural observation
        ↓
candidate correspondence entry
        ↓
explicit translation standing
        ↓
research hypothesis, if any
        ↓
future proof / translation / experiment
        ↓
separate promotion decision
```

No arrow may be skipped by prose.

In particular:

```text
analogy -> canonical theory
```

and

```text
architecture success -> target validation
```

are forbidden shortcuts.

## 7. Verification

Before the first planting is presented for merge or further implementation, verify:

1. only `docs/research_seeds/**` and the design/plan artifacts are changed;
2. canonical Interface Theory files are byte-unchanged from base;
3. Gate 013 and Gate 014 artifacts are byte-unchanged from base;
4. Adaptive Capacity governance artifacts are byte-unchanged from base;
5. all cross-repo entries contain exact commit anchors;
6. all candidate translations default conservatively and no structural resemblance is labeled `IDENTICAL` or `REFINEMENT` without an explicit map;
7. all conceptual sources are marked non-evidentiary;
8. the repair-aware file explicitly preserves the blind-repair caveat;
9. the blockwise-adequacy file distinguishes an abstract mathematical schema from source-specific results;
10. repository integrity validation still passes, if the existing validator covers documentation-only additions without requiring canonical registration.

A textual hostile pass should search for accidental promotion language such as:

```text
proves
establishes
is equivalent to
is the same as
validates MATRIX
validates Interface Theory
```

and require each occurrence to be justified by the declared standing.

## 8. Error / ambiguity handling

If a correspondence cannot be typed cleanly, record:

```text
NO_TRANSLATION_EARNED
```

rather than inventing a broader abstraction.

If the shared-poset formulation requires assumptions not present in one source program, state the assumption and narrow the schema rather than editing the source program.

If a conceptual-provenance item cannot be sourced reliably, preserve only the fact that it inspired the discussion; do not attach scientific claims to it.

If an architecture hypothesis requires a new scientific noun, stop and identify the missing argument before adding the noun.

## 9. Promotion contract

Nothing in this first planting is promoted automatically.

A later promotion must identify which of the following occurred:

```text
proof earned
translation earned
finite witness earned
causal experiment earned
implementation evidence earned
```

and must preserve the original seed record as provenance.

The first planting does not authorize:

- a new Interface Theory gate;
- a new MATRIX assay;
- CNI/NOOA implementation;
- a transformer implementation;
- a general theory of adaptive interfaces;
- a claim that corrective capacity and identifiability are identical;
- a claim that the artwork encodes the scientific theory.

## 10. Acceptance criterion for this design

The design is successful if it creates a place where tonight's useful cross-program observations can be preserved with exact source anchors, explicit claim ceilings, and explicit unresolved mismatches, while the canonical Interface Theory record remains untouched.

Implementation begins only after this design is reviewed and approved.
