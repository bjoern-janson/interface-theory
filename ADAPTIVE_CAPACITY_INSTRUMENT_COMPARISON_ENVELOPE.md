# Adaptive-Capacity Instrument Comparison Envelope

## Scope and authority

This document freezes the minimum shared access, representation, and recording conditions under which candidate instruments may later be compared for support of the frozen

\[
\boxed{C_1+C_2}
\]

adaptive-capacity claim profile.

It is a comparison-admissibility contract only. It does not select, rank, score, recommend, design, name, qualify, or evaluate any candidate instrument.

The governing question is:

> **Under what shared access and recording conditions can candidate instruments be compared for support of a \(C_1+C_2\) study?**

The artifact defines the playing field. It does not define or choose the players.

## Governing dependencies

This envelope is constrained by:

```text
ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md
ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER_HOSTILE_AUDIT.md
INSTRUMENTATION_REQUIREMENTS_ADAPTIVE_CAPACITY.md
FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md
```

It does not revise, expand, reinterpret, repair, or replace those artifacts.

It inherits:

\[
\boxed{
C_2:\text{ causal total feedback-branch effect}
}
\]

with:

\[
\boxed{
C_1:\text{ scoped future-adaptation profile difference}
}
\]

as its required descriptive basis.

It does not authorize:

\[
C_3:\text{ update-pathway or transition-specific effect}
\]

or:

\[
C_4:\text{ generator-mediated effect}.
\]

## Frozen comparison boundary

Candidate instruments may be compared only for their ability to support the frozen \(C_1+C_2\) claim profile.

The envelope concerns:

\[
\boxed{
\text{evidence coverage}
}
\]

not:

\[
\boxed{
\text{feature count}.
}
\]

\[
\boxed{
\text{instrument richness}\neq\text{claim adequacy}.
}
\]

A simpler instrument may satisfy the complete frozen profile. A richer instrument remains inadmissible for comparison if it lacks mandatory evidence such as assignment integrity, comparator integrity, resource provenance, evaluator integrity, exposure accounting, failure capture, audit completeness, or assay-profile linkage.

Additional internal visibility cannot compensate for missing \(C_1+C_2\) evidence and cannot raise the claim level.

## Comparison objective and dimensions

The only comparison objective is support for \(C_1+C_2\). The admissibility record may describe:

- required evidence coverage;
- evidence fidelity;
- intervention and assignment validity;
- compatibility with the frozen scope;
- audit completeness;
- known evidence gaps.

These dimensions remain separate. The envelope defines no universal ranking function, scalar score, winner-selection rule, or preferred-instrument recommendation.

## Exactly three comparison statuses

These are the only permitted comparison-level statuses.

### Admissible

The candidates can be compared under one shared envelope for the declared \(C_1+C_2\) purpose.

### Conditionally comparable

The candidates can be compared only within an explicitly narrowed system class, access envelope, evidence subset, or assay scope.

### Comparison blocked

The available boundaries, privileges, intervention semantics, evidence vocabularies, or records cannot support a scientifically meaningful comparison.

The statuses concern comparison validity. They are not grades, scores, rankings, or statements that an instrument is scientifically superior.

## Eight shared comparison envelopes

### 1. System Eligibility Envelope \(\mathcal E_S\)

**Purpose:** define the shared evaluated-system and treatment-branch scope.

#### Must be representable

- evaluated whole-system boundary;
- complete treatment-branch boundary;
- auxiliary and external components;
- tools and external services;
- persistent and inherited state or information;
- environment and evaluator relationships;
- experimental-unit definition;
- starting-state identity and descendant-lineage identity;
- declared system-class assumptions.
- which components are mutable, fixed, compared, excluded, or shared across branches;
- interference boundaries for shared buffers, stores, services, environments, evaluators, and communication.

The treatment-branch boundary includes every pathway whose behavior may differ because of assignment to the feedback policy. It does not require a universal decomposition into generator, ordinary state, memory, or mechanism classes.

#### May remain inaccessible

- complete internal semantics;
- full interpretability;
- architecture-specific mechanisms;
- arbitrary hidden implementation details;
- a universal \(S/G/W\) decomposition;
- generator-level state.

Raw hidden state may remain inaccessible when its existence, possible relevance, and resulting scope limitation are disclosed and bounded for the proposed comparison.

#### Mandatory evidence

- declared system class;
- whole-system and treatment-branch boundaries;
- included and excluded components;
- external dependencies;
- persistent-state assumptions;
- known inaccessible regions;
- comparison-relevant limitations;
- whether boundary semantics have the same meaning for every candidate.
- starting-state and lineage semantics;
- interference and shared-component boundaries.

#### Differences reported rather than normalized

- supported system classes;
- treatment-boundary assumptions;
- handling of tools, stores, services, and persistent state;
- experimental-unit definitions;
- hidden-state limitations.
- starting-state capture and lineage granularity;
- interference handling and external-service versioning.

#### Conditionally comparable when

- candidates overlap only on a declared subset of system classes;
- boundaries can be mapped only under explicit assumptions;
- support is limited to a restricted substrate class.

Any mapped or coarsened boundary must still preserve the complete \(C_2\) treatment branch.

#### Comparison blocked when

- candidates concern different system classes without a shared declared scope;
- system or treatment-branch boundaries cannot be mapped;
- one boundary silently includes components another excludes;
- the experimental unit has materially different meaning;
- hidden components that could reverse the interpretation cannot be bounded or disclosed.

#### Requirement status

**Universal:** whole-system boundary, treatment-branch boundary, unit identity, system class, inclusions, exclusions, external dependencies, and known access limits.

**System-class dependent:** the substrate-specific representation of those boundaries, persistent state, tools, services, and any deeper internal visibility.

### 2. Observational Access Envelope \(\mathcal E_O\)

**Purpose:** define the common observations sufficient for the frozen descriptive and whole-branch causal profile.

#### Must be representable

- external outcomes;
- every declared multidimensional profile dimension;
- retention outcomes;
- failures, exclusions, censoring, and missingness;
- resource, exposure, and leakage records;
- treatment and branch identity;
- treatment-dependent events required to verify exposure, branch membership, comparator validity, or the frozen assay;
- the observation interface;
- observation transformations, summaries, and discarded information.

Internal update events are required only when the declared \(C_2\) design uses them for branch reconstruction or comparator validity. They are not universally required observations.

#### May remain inaccessible

- arbitrary internal state;
- private mechanism semantics;
- generator state;
- architecture-specific variables;
- internal transitions irrelevant to \(C_1+C_2\);
- complete causal-pathway decomposition.

#### Mandatory evidence

- versioned observation-interface manifest;
- observable fields;
- transformations and summaries;
- precision, fidelity, and missingness limits;
- discarded information;
- known observational collisions;
- approximate-identifiability tolerances where applicable;
- candidate-specific access privileges.
- indexing by unit, branch, perturbation, horizon, schedule, and assay-profile version;
- scheduled-observation membership and exact denominators;
- evidence relevant to exact or approximate target identification over the declared class;
- whether identification evidence is a finite collision audit or a result covering an open class.

#### Differences reported rather than normalized

- observation privileges;
- fidelity and precision;
- timing resolution;
- summary transformations;
- access to persistent state or external dependencies;
- known collision classes.
- target-identification scope and tolerance;
- missing-field patterns;
- whether representation mappings preserve common evidence obligations exactly or approximately.

#### Conditionally comparable when

- candidates share a reduced common observation interface;
- richer observations remain optional rather than mandatory;
- the comparison is explicitly scoped to evidence available across candidates;
- different raw observation spaces map validly to the same mandatory evidence semantics.

The reduced interface must still identify the frozen \(C_1/C_2\) target within the declared tolerance.

#### Comparison blocked when

- observation spaces have no valid mapping to common mandatory evidence obligations;
- privileged observations are unaccounted for;
- mandatory \(C_1+C_2\) outcomes cannot be reconstructed;
- one interface discards target-relevant distinctions;
- known observational collisions invalidate the intended comparison.

#### Requirement status

**Universal:** external outcomes, declared dimensions, retention, failures, resources, exposure, branch identity, interface manifest, transformations, discarded evidence, and known collisions.

**System- or design-dependent:** internal transition visibility, precision, temporal granularity, and optional state access used by a particular \(C_2\) comparator.

### 3. Intervention and Assignment Envelope \(\mathcal E_I\)

**Purpose:** define the shared causal-assignment semantics for the \(C_2\) total feedback-branch estimand.

#### Must be representable

- feedback-policy and comparator assignment;
- assignment mechanism;
- treatment and comparator versions;
- branch membership;
- assigned treatment and realized exposure;
- crossover and noncompliance;
- interference;
- treatment-dependent external effects and resources;
- intervention semantics relevant to the complete branch contrast.
- assignment probabilities, strata, eligibility, or equivalent records needed by the declared design;
- pre-assignment balancing variables where relied upon;
- the distinction among raw consequence, evaluator transformation, delivered signal, and actual exposure;
- the exact assignment-versus-receipt estimand.

#### May remain inaccessible

- arbitrary internal interventions;
- selective generator manipulation;
- transition-specific manipulation;
- mediator intervention;
- generator rollback or transplantation;
- pathway isolation required only for \(C_3\) or \(C_4\).

The instrument need only represent and preserve the externally imposed assignment process. It need not implement assignment itself.

#### Mandatory evidence

- frozen assignment rule;
- comparator definition;
- policy and comparator versions;
- assignment and branch records;
- actual exposure, crossover, and noncompliance records;
- treatment-dependent perturbation or evaluator differences;
- interference records;
- branch-integrity evidence;
- comparator coherence and limitations;
- counterfactual-control evidence or valid alternative confound checks required by the declared \(C_2\) design.
- comparator support, coherence, timing, resource, state-write opportunity, and failure-mode differences;
- allocation authority, deviations from the frozen rule, and assumptions concerning consistency, overlap, exchangeability, and interference.

#### Differences reported rather than normalized

- randomized versus non-random assignment;
- cloned versus independent branches;
- assignment versus receipt estimands;
- comparator semantics;
- treatment versions;
- treatment-induced resources;
- intervention side effects;
- interference assumptions.
- allocation authority and rule deviations;
- consistency, overlap, and exchangeability assumptions.

#### Conditionally comparable when

- different identification designs support the same frozen \(C_2\) estimand under explicit assumptions;
- candidate support is restricted to particular assignment mechanisms;
- comparator semantics align only within a narrowed study class.

A no-update, replay, gating, or bundled intervention used as a comparator remains whole-branch \(C_2\) evidence under this profile.

#### Comparison blocked when

- assignment, treatment version, comparator version, or branch membership cannot be reconstructed;
- intervention meanings materially differ and cannot be mapped;
- comparator semantics cannot be aligned;
- interference invalidates the whole-branch contrast;
- one candidate requires a different causal estimand.
- a candidate supports only \(C_1\) for a comparison whose declared purpose requires \(C_2\).

#### Requirement status

**Universal for \(C_2\):** assignment, policy, comparator, branch, exposure, noncompliance, interference, and treatment-version evidence.

**Design-dependent:** randomization or matching form, specific controls, assignment-versus-receipt contrast, cloning, sham semantics, and limited interventions used only to validate a comparator. Such interventions do not authorize \(C_3\).

### 4. Temporal Resolution Envelope \(\mathcal E_T\)

**Purpose:** define the common causal-order and schedule evidence required by the frozen assay.

#### Must be representable

- treatment assignment;
- feedback delivery and actual exposure;
- treatment-dependent events required by the assay;
- perturbation delivery;
- adaptation and evaluation windows;
- retention windows;
- failures and stopping events;
- timing or schedule amendments;
- causal ordering required by \(C_2\).
- perturbation order and sequential treatment history when included in the frozen assay.

Internal update timing is required only when the declared \(C_2\) design uses it for branch reconstruction, comparator validity, or treatment definition.

#### May remain inaccessible

- exact internal computation timing when irrelevant to \(C_1+C_2\);
- instruction-level timing;
- pathway-specific temporal traces;
- mediator timing required only for \(C_3\) or \(C_4\).

#### Mandatory evidence

- timestamps or declared causal-order semantics;
- clock source or ordering basis;
- temporal resolution and synchronization limitations;
- adaptation, evaluation, delayed-evaluation, and retention windows;
- stopping rules;
- schedule visibility to the evaluated system.
- event, delivery, exposure, record, and evaluation times where they may differ;
- time-base or ordering authority, clock drift or uncertainty, cross-service synchronization, buffering, batching, and timestamp missingness.

#### Differences reported rather than normalized

- clock precision;
- event-order granularity;
- synchronization guarantees;
- buffering and batching;
- schedule visibility;
- missing or uncertain times.
- clock or ordering-source changes;
- whether timing information was treatment-dependent.

#### Conditionally comparable when

- a shared coarser ordering remains sufficient for \(C_2\);
- exact times differ while the required causal order remains identifiable;
- the comparison is narrowed to assays compatible with the shared resolution.

The shared order must preserve every timing relation required by the frozen \(C_2\) contrast, including horizons, stopping semantics, and retention schedules.

#### Comparison blocked when

- required causal ordering cannot be established;
- assignment, exposure, perturbation, and evaluation order cannot be reconstructed;
- stopping-time differences could reverse the interpretation;
- timing semantics cannot be mapped.

These failures block \(C_2\) comparison even when a descriptive \(C_1\) record survives.

#### Requirement status

**Universal:** schedule, stopping, treatment, perturbation, evaluation, failure, and required causal-order records.

**Design-dependent:** clock precision, synchronization, internal update timing, sequential windows, delayed probes, and resolution beyond the shared \(C_1+C_2\) contrast.

### 5. Resource Representation Envelope \(\mathcal E_B\)

**Purpose:** define the common resource vocabulary and lifecycle boundary without imposing a universal conversion.

#### Must be representable

Where relevant:

- available, consumed, and inherited resources;
- treatment-induced resources;
- computation and parallelism;
- memory and persistent storage;
- interaction, samples, observations, and episodes;
- wall-clock time;
- communication bandwidth;
- tools, external services, and retrieval;
- offline search and reusable precomputation;
- model or program size;
- initialization information;
- energy and other physical resources.

#### May remain inaccessible

- a universal resource conversion;
- a single scalar cost;
- architecture-neutral effective-resource equivalence;
- a universal efficiency ordering.

#### Mandatory evidence

- shared resource vocabulary, units, and definitions;
- lifecycle boundary;
- available/consumed/inherited distinction;
- treatment-induced resource records;
- accounting precision and missing categories;
- candidate-specific omissions;
- resource-comparability status.

#### Differences reported rather than normalized

- accounting resolution;
- omitted categories;
- treatment of inherited information;
- tools, retrieval, and precomputation;
- parallelism and storage;
- treatment-induced resource use;
- heterogeneous resource–outcome tradeoffs.

Treatment-induced resources remain inside the \(C_2\) total branch. Pre-existing or treatment-extraneous resource differences threaten comparability. Neither case is erased through normalization.

#### Conditionally comparable when

- comparison is limited to a shared subset of resource dimensions;
- residual resource differences remain explicit tradeoffs;
- no scalar normalization is imposed.

#### Comparison blocked when

- resource definitions cannot be mapped;
- omitted resources could reverse interpretation;
- lifecycle boundaries are incompatible;
- inherited or external resources are invisible;
- forced conversion hides an unresolved resource–outcome tradeoff.

#### Requirement status

**Universal:** vocabulary, lifecycle boundary, available/consumed/inherited distinction, treatment-induced resources, omissions, precision, and comparability status.

**System- or design-dependent:** applicable resource coordinates, units, physical measurements, and the shared subset on which comparison remains meaningful.

### 6. Exposure and Leakage Provenance Envelope \(\mathcal E_X\)

**Purpose:** define the shared exposure boundary and the exact novelty level supported by later comparison.

#### Must be representable

- training and pretraining exposure;
- modification and model-selection exposure;
- validation and confirmatory evaluation exposure;
- perturbation instances, configurations, templates, and families;
- prompts, tools, caches, retrieval outputs, and evaluator traces;
- benchmark exposure;
- cross-branch information flow.

#### May remain inaccessible

- historical exposure records that cannot affect the declared assay under explicit assumptions;
- unavailable historical detail when the resulting scope limitation is preserved.

#### Mandatory evidence

- exposure ledger and leakage boundary;
- novelty-level declarations;
- identity scheme for instances, seeds, configurations, templates, and families;
- known unknown exposure;
- repeated-evaluation records;
- development/confirmatory separation;
- ledger granularity and limitations.

#### Differences reported rather than normalized

- novelty level;
- historical completeness;
- family-identity semantics;
- retrieval and tool visibility;
- benchmark-contamination risk;
- cross-branch isolation.

#### Conditionally comparable when

- comparison is narrowed to a verified common novelty level;
- a stronger novelty claim is reduced to unseen instance, seed, or configuration;
- exposure uncertainty remains explicit in the scope.

#### Comparison blocked when

- exposure scopes cannot be reconciled;
- held-out status cannot be reconstructed;
- identity schemes are incompatible;
- contamination risk could reverse the interpretation;
- unavailable exposure history creates an unaccounted advantage.

#### Requirement status

**Universal:** exposure ledger, leakage boundary, novelty label, identity scheme, repeated evaluation, development/confirmatory separation, and known unknowns.

**System- or design-dependent:** relevant historical depth, family ontology, tool and retrieval exposure, and the strongest shared novelty level.

### 7. Evaluation Integrity Envelope \(\mathcal E_V\)

**Purpose:** define the common external-outcome and evaluator boundary.

#### Must be representable

- evaluator identity and version;
- scoring and outcome-generation processes;
- evaluator transformations of raw consequences;
- outcome storage and write access;
- exclusion and stopping rules;
- perturbation-sampling authority;
- evaluator visibility to the system;
- system influence over evaluator behavior;
- manipulation risks;
- evaluator treatment-dependence.

#### May remain inaccessible

- complete evaluator independence when the claim is explicitly scoped to the evaluator interaction;
- evaluator internals irrelevant to outcome integrity.

#### Mandatory evidence

- evaluator and outcome boundaries;
- outcome provenance;
- code or configuration identity;
- manipulation boundary;
- scoring transformations;
- sampling, stopping, exclusion, and censoring authority;
- system write access;
- treatment-dependent evaluator differences;
- known exploitation risks.

External scoring and independent evaluation are not synonyms.

#### Differences reported rather than normalized

- evaluator independence and visibility;
- manipulation exposure;
- scoring transformation;
- sampling and stopping authority;
- outcome-record isolation;
- treatment dependence.

#### Conditionally comparable when

- candidates share an explicitly scoped evaluator interaction;
- independence differs but outcome integrity remains auditable;
- residual limitations stay attached to the claim scope.

#### Comparison blocked when

- outcome integrity cannot be assessed consistently;
- outcome records can be altered without detection;
- evaluator versions cannot be aligned;
- treatment changes evaluator behavior in an unmodeled way;
- stopping, exclusion, or sampling cannot be reconstructed;
- nominally identical outcomes have materially different meanings.

#### Requirement status

**Universal:** evaluator identity, outcome integrity, version, transformation, manipulation boundary, sampling/stopping/exclusion authority, system access, and treatment dependence.

**System- or design-dependent:** degree of technical isolation, evaluator internals, residual visibility, and the evaluator-scoped limitations retained in the result.

### 8. Record Persistence and Auditability Envelope \(\mathcal E_R\)

**Purpose:** define the common evidence that must survive for audit, reconstruction, and reanalysis.

#### Must be representable

- configuration and assay-profile versions;
- feedback-policy and comparator versions;
- assignment and branch-lineage records;
- system, perturbation, resource, exposure, evaluator, and outcome records;
- retention, failure, censoring, and missingness records;
- stopping events;
- amendments and researcher decisions;
- result classifications and claim-level metadata.

#### May remain inaccessible

- implementation-specific records that do not affect \(C_1+C_2\);
- optional telemetry not needed for auditability.

#### Mandatory evidence

- immutable identifiers or equivalent integrity evidence;
- manifests, hashes, or auditable versions;
- amendment history;
- exploratory/confirmatory separation;
- outcome-access state for decisions;
- machine-readable assay linkage;
- unit, dependence, pairing, denominator, and exact-count records;
- uncertainty and multiplicity metadata;
- missing-data provenance;
- discarded-record declarations;
- record-retention duration and audit-access guarantees.

#### Differences reported rather than normalized

- integrity mechanisms;
- record completeness;
- retention guarantees;
- machine readability;
- lineage granularity;
- amendment handling;
- audit access;
- reproducibility limitations.

#### Conditionally comparable when

- records map into a common evidence vocabulary with declared loss;
- optional fields differ while all mandatory \(C_1+C_2\) evidence survives;
- comparison is limited to the shared auditable subset.

#### Comparison blocked when

- records cannot map to a shared assay-profile vocabulary;
- configuration identity, assignment, or branch lineage is unavailable;
- amendments cannot be reconstructed;
- failures, exclusions, missingness, or denominators are absent;
- results can be detached from their assay profiles;
- mandatory evidence cannot be independently audited.

#### Requirement status

**Universal:** identities, versions, assay linkage, assignment, lineage, outcomes, failures, amendments, decisions, denominators, integrity, retention, and access guarantees.

**System- or design-dependent:** implementation-specific telemetry, retention duration beyond the audit need, optional raw records, and loss accepted when mapping into the shared vocabulary.

## Universal versus conditional requirements

### Universal requirements

Every candidate comparison requires:

- frozen \(C_1+C_2\) claim-level declaration;
- complete assay-profile linkage;
- whole-system and treatment-branch boundaries;
- starting-state and lineage identity;
- external outcome integrity;
- perturbation and exposure scope;
- shared resource vocabulary and lifecycle boundary;
- assignment, comparator, treatment-version, branch, and interference records for \(C_2\);
- configuration identity;
- failure, missingness, censoring, and denominator capture;
- interface-identifiability and known-collision evidence;
- replication, pairing, dependence, exact-count, multiplicity, and uncertainty support;
- record persistence and audit access;
- claim-scoping metadata.

### Conditional requirements

The following activate only for particular system classes, assays, or \(C_2\) identification designs:

- deeper internal visibility;
- internal update timing;
- specific state access;
- limited interventions used to validate a comparator;
- particular control implementations;
- mechanism-specific observations that remain exploratory;
- joint-capability and access-cost probes;
- sequential perturbation support;
- specialized resource categories.

Conditional requirements do not become universal because one candidate happens to support them. Optional capability cannot compensate for missing universal capability. Limited intervention evidence used for a \(C_2\) comparator does not authorize \(C_3\) or \(C_4\).

## Common comparison-record categories

The shared comparison record must be able to represent these categories without fixing a serialization format:

```text
candidate_identifier
supported_system_classes
supported_claim_levels
system_boundary
treatment_branch_boundary
observation_envelope
intervention_envelope
temporal_envelope
resource_envelope
exposure_envelope
evaluation_envelope
record_envelope
mandatory_requirements_supported
conditional_requirements_supported
known_evidence_gaps
scope_restrictions
comparison_status
comparison_blockers
assay_profile_compatibility
configuration_version
```

`comparison_status` accepts exactly `Admissible`, `Conditionally comparable`, or `Comparison blocked`.

This document defines no field encoding, API, software class, database schema, scoring formula, or ranking rule.

## Comparison-blocking conditions

Candidate comparison remains blocked when:

1. system boundaries differ without a shared declared scope;
2. treatment-branch boundaries cannot be aligned;
3. observation privileges differ without explicit accounting;
4. mandatory evidence cannot map into a common interface;
5. intervention or assignment semantics materially differ;
6. causal ordering cannot be represented at sufficient resolution;
7. resource definitions or lifecycle boundaries are incompatible;
8. omitted resources could reverse interpretation;
9. exposure records or novelty levels cannot be aligned;
10. evaluator integrity uses incompatible standards;
11. outcome meanings materially differ;
12. configuration, lineage, amendment, failure, missingness, or denominator records are unavailable;
13. records cannot map to the common assay-profile categories;
14. candidates support different causal estimands rather than the same frozen \(C_2\) claim.

These are comparison failures. They are not automatically failures of an instrument outside the attempted shared envelope.

## Non-compensation rule

\[
\boxed{
\text{Optional capability cannot compensate for missing mandatory capability.}
}
\]

Consequently:

- richer internal telemetry cannot compensate for invalid assignment;
- generator visibility cannot compensate for missing resource provenance;
- finer timing cannot compensate for evaluator manipulation;
- larger records cannot compensate for missing exposure history;
- architecture-specific interpretability cannot compensate for absent failure capture.

## Permanent governance rules

\[
\boxed{
\text{No candidate instrument is named during comparison-envelope construction.}
}
\]

\[
\boxed{
\text{No requirement may be added solely because a preferred instrument supports it.}
}
\]

\[
\boxed{
\text{Comparison measures compliance with the frozen claim profile, not theoretical elegance.}
}
\]

\[
\boxed{
\text{Optional capability cannot compensate for missing mandatory capability.}
}
\]

\[
\boxed{
\text{A shared comparison envelope must be established before instrument differences are interpreted.}
}
\]

\[
\boxed{
\text{No comparison result may raise the frozen claim level beyond }C_2.
}
\]

## Stop boundary

This artifact stops after freezing comparison admissibility. It does not proceed to candidate qualification, comparison, scoring, ranking, recommendation, selection, architecture evaluation, experiment design, or implementation.

The governing sequence remains:

\[
\boxed{
C_1+C_2\text{ claim profile}
\longrightarrow
\text{comparison envelope}
\longrightarrow
\text{candidate qualification protocol}
\longrightarrow
\text{candidate qualification}
\longrightarrow
\text{comparison}
\longrightarrow
\text{selection}
\longrightarrow
\text{experiment design}
}
\]

## Explicit non-goals

This envelope does not:

- name any candidate instrument;
- compare, qualify, score, rank, recommend, or select instruments;
- define a winner-selection rule;
- design an instrument;
- define software architecture, runtime components, APIs, or storage systems;
- choose technologies;
- define a benchmark, environment, experiment, estimator, or metric;
- define a scalar comparison score;
- introduce new theory;
- expand the claim level;
- define preferred observation methods;
- authorize implementation.

## Minimum unresolved choices before candidate comparison

1. The supported system and substrate classes.
2. The shared whole-system and treatment-branch boundary semantics.
3. The permitted observation envelope.
4. The permitted intervention, comparator, and assignment envelope.
5. The required temporal resolution and causal-order semantics.
6. The required capture fidelity and identifiability tolerances.
7. The required resource vocabulary, lifecycle boundary, and accounting precision.
8. The required exposure identity scheme, novelty levels, and ledger granularity.
9. The required evaluator-integrity and outcome-provenance standard.
10. The required retention, joint-capability, failure, missingness, censoring, and denominator depth.
11. The required lineage, dependence, pairing, clustering, and interference evidence.
12. The required configuration integrity, amendment, exploratory/confirmatory, and decision-audit evidence.
13. The required interface-identifiability and known-collision evidence.
14. The required record-retention duration and audit-access guarantees.
15. The required machine-readable common comparison record categories.
