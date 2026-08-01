# Instrumentation Requirements for Adaptive-Capacity Claims

## Scope and authority

This document extracts the minimum implementation-neutral capabilities an experimental instrument must provide to support claims admitted by `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md` and constrained by `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER_HOSTILE_AUDIT.md`.

It specifies what evidence must be observable, controllable, recorded, isolated, and preserved. It does not specify how an instrument is built, what system substrate it evaluates, which experiment is run, or which statistical estimator is used.

An **instrument** in this document means any experimental capability that produces and preserves the declared observations, interventions, records, and integrity evidence. It is not a learning architecture and need not be part of the evaluated system.

The requirements inherit the charter's scope rule:

\[
\text{admissible claim}
\Longrightarrow
\text{claim level supported by the available instrument evidence}.
\]

More detailed logs do not, by themselves, raise the causal claim level.

> **CNI / NOOA does not implement adaptive capacity.**

The only admissible future wording is:

> **CNI / NOOA may be evaluated as one candidate instrumentation layer for collecting evidence required by the Adaptive Capacity Measurement Charter.**

The same constraint applies to every other proposed architecture or instrumentation substrate.

## Claim-level ladder

| Level | Admissible claim | Minimum interpretation |
| --- | --- | --- |
| \(C_1\) | **Scoped future-adaptation profile difference** | Two declared branches or populations differ on a frozen multidimensional future-adaptation profile. No causal attribution to feedback or generator change is implied. |
| \(C_2\) | **Causal total feedback-branch effect** | Assignment to a declared feedback policy causes a change in the scoped future-adaptation profile relative to a valid comparator. The effect belongs to the complete branch. |
| \(C_3\) | **Update-pathway or transition-specific effect** | Enabling a declared update pathway, or imposing a declared transition, causally changes the profile under a coherent contrast. Logging a transition is not sufficient. |
| \(C_4\) | **Generator-mediated effect** | A declared generator transition mediates the feedback effect under a coherent mediator intervention or sufficient identifying assumptions, with competing pathways addressed. |

The levels are cumulative in evidentiary burden, not interchangeable labels:

\[
C_4\Rightarrow C_3\Rightarrow C_2\Rightarrow C_1
\]

only when the corresponding contrasts are nested and jointly well-defined. A study may support \(C_2\) while \(C_3\) or \(C_4\) is scientifically incoherent.

For each requirement below, **highest claim level supported** means the highest level to which that capability can contribute. It never means that the capability is independently sufficient for that claim.

## Universal and conditional capability classes

### Universal core

Every admissible claim requires the applicable core of:

- system and observation-boundary declaration;
- starting-state and lineage capture;
- exposure and leakage accounting;
- frozen perturbation and outcome scope;
- resource accounting;
- external evaluator separation;
- retention evidence under the declared contract;
- multidimensional outcome records;
- failures, missingness, time, and stopping-rule records;
- interface-identifiability evidence;
- frozen configuration and decision provenance;
- replication and uncertainty metadata;
- complete claim-scoping metadata.

### Conditional causal capabilities

- \(C_2\) additionally requires feedback assignment, feedback provenance, comparator integrity, treatment versions, and interference records.
- \(C_3\) additionally requires a coherent mechanism boundary, update identity and persistence records, and an intervention that isolates the update pathway or transition from parallel changes.
- \(C_4\) additionally requires mediator-specific intervention or sufficient causal identification, alternate-mediator isolation, and evidence about treatment-induced mediator–outcome confounding.

### Conditional construct-validity capabilities

Sequential perturbation, delayed retention, joint capability, access-cost, and repeated-shift records are required whenever the claim includes persistence, transfer, recovery, compositional retention, or later-shift adaptability. Otherwise they remain unavailable dimensions rather than universal proof obligations.

## Implementation-neutral capability requirements

### IR-01 — System and mechanism boundary declaration

**Classification:** universal core; generator-specific extension conditional for \(C_3\) and \(C_4\).

**Highest claim level supported:** \(C_4\).

The instrument must preserve a frozen, architecture-neutral declaration equivalent to

\[
(S_t,G_t,W_t,E_t),
\]

where the study distinguishes evaluated state, declared adaptive or generator mechanism, auxiliary or external memory and tools, and environment or evaluator state.

The declaration must record:

- which components can change;
- which components are held fixed, randomized, cloned, compared, or excluded;
- which components are observable and which remain hidden;
- known limitations created by hidden state;
- whether the boundary has the same meaning across treatment and controls;
- whether a transition, block, rollback, or transplant is semantically coherent.

Complete internal interpretability is not required. The boundary must only be clear enough to determine what each causal noun in the study refers to.

**Failure if absent:** \(C_1\) may survive only as a whole-system profile comparison if its system boundary remains clear. Generator- or pathway-specific claims are blocked; a claim that silently reallocates effects among \(S\), \(G\), and \(W\) is inadmissible.

### IR-02 — Starting-state and lineage capture

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must identify starting conditions and every evaluated descendant. It must be able to preserve or reference:

- checkpoint or initial-state identity;
- model, program, policy, and declared mechanism versions;
- initialization provenance;
- optimizer or other persistent update state where applicable;
- persistent memory, retrieval index, cache, and external-store state;
- tool and external-service configuration;
- prior training, pretraining, and exposure records;
- lineage from the starting state through modification and evaluation branches;
- paired or independent randomness and possible cross-branch interference.

The records must expose evidence relevant to distinguishing new adaptation from stored or latent competence. Behavioral success alone cannot guarantee that distinction.

**Failure if absent:** starting-state, current-competence, inherited-resource, and latent-policy explanations remain unresolved. Causal branches are not exchangeably comparable, and even a \(C_1\) profile difference may be attributable to baseline inequality.

### IR-03 — Feedback provenance

**Classification:** conditional; first required for \(C_2\).

**Highest claim level supported:** \(C_4\), as provenance only.

For causal feedback claims, the instrument must record a reproducible lineage:

```text
external event
        ↓
raw observed consequence
        ↓
evaluator transformation
        ↓
delivered feedback
        ↓
system exposure and observable routing
        ↓
update event and state writes
        ↓
persistence, rollback, or overwrite
        ↓
later adaptive behavior
        ↓
external outcome
```

Required records include the source, content or reproducible reference, timestamps or causal order, delivery channel, treatment version, exposure, associated update events, later branch identity, and persistent-state history.

\[
\boxed{
\text{Provenance is not mediation proof.}
}
\]

**Failure if absent:** chronology and branch membership cannot be reconstructed. \(C_2\) is blocked when feedback assignment or exposure cannot be verified; \(C_3\) and \(C_4\) remain blocked even when chronology is available but isolation is not.

### IR-04 — Exposure and leakage ledger

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must record exposure to:

- training, modification, validation, and evaluation environments;
- evaluation instances, seeds, configurations, templates, and families;
- perturbation-generation rules and family parameters;
- prompts, tools, caches, retrieval outputs, evaluator traces, and shared memory;
- prior benchmark or pretraining exposure;
- repeated confirmatory evaluation and cross-branch information flow.

Each held-out claim must be indexed by its novelty level, such as unseen instance, seed, configuration, perturbation family, or causal mechanism. The ledger must distinguish data used to produce, select, tune, accept, or evaluate a candidate change.

**Failure if absent:** memorization, family lookup, contamination, and researcher leakage cannot be excluded. The affected generalization claim is narrowed or blocked; `held out` becomes an unsupported label.

### IR-05 — Perturbation isolation and assignment

**Classification:** universal core for \(C_1\); causal assignment extension required for \(C_2\) through \(C_4\).

**Highest claim level supported:** \(C_4\).

The instrument must preserve:

- the frozen perturbation set or population and its version;
- reproducible sampling, family labels, severity labels, weights, and order;
- treatment and control assignment where causal claims are made;
- repeated and sequential perturbation histories;
- separation of modification data from confirmatory evaluation data;
- whether perturbations were externally assigned, system-generated, system-filtered, adaptively selected by researchers, or excluded after failure;
- whether perturbation and evaluator draws were treatment-independent;
- pairing or independence of perturbation randomness across branches.

**Failure if absent:** the target population, distributional scope, assignment mechanism, or selection process cannot be reconstructed. \(C_1\) loses its declared scope; \(C_2\) and higher lose causal assignment validity.

### IR-06 — Resource accounting

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must preserve the complete declared resource vector, including every applicable quantity among:

- computation and parallelism;
- interaction steps, observations, samples, and episodes;
- memory and persistent storage;
- model or program size;
- wall-clock time;
- communication bandwidth;
- tools, retrieval, and external services;
- offline search and update selection;
- reusable precomputation and inherited information;
- initialization information;
- energy or physical resources.

The ledger must distinguish resources **available**, **consumed**, and **inherited**, and must cover feedback production, modification search and selection, later adaptation, and evaluation.

No universal conversion among heterogeneous resources is assumed. The instrument must preserve unordered resource–outcome profiles when credible scalar comparison is unavailable.

**Failure if absent:** extra resources, prior computation, privileged initialization, or external scaffolding remain alternative explanations. A capacity ordering is blocked or relabeled as a resource-mediated difference.

### IR-07 — Update and mechanism-difference recording

**Classification:** conditional for \(C_3\) and \(C_4\); descriptive update records may be retained at lower levels without raising the claim.

**Highest claim level supported:** \(C_4\).

The instrument must be able to identify and version a declared mechanism before and after an update without assuming a substrate. Eligible representations may include parameter snapshots, program or graph differences, learned-library changes, operator changes, policy-generator changes, memory writes, or other study-declared differences.

It must record:

- pre-update and post-update identity;
- update time and source;
- the representation in which difference is asserted;
- persistence, rollback, overwrite, and descendant lineage;
- other simultaneous state writes;
- whether controls received comparable update opportunities.

A recorded difference establishes only

\[
G_{t+1}\neq G_t
\]

relative to the declared representation.

**Failure if absent:** a transition-specific contrast cannot be defined or reconstructed. Even when present, the record alone establishes neither benefit nor mediation.

### IR-08 — Counterfactual intervention and control support

**Classification:** conditional on causal claim and declared identification design; first applicable at \(C_2\).

**Highest claim level supported:** \(C_4\), as confound checks only.

When a study invokes any of the charter's six controls, the instrument must preserve for each:

- exact intervention and comparator behavior;
- treatment–control differences;
- induced resource and timing differences;
- whether the control is on- or off-distribution;
- whether it changes signal semantics, support, or coherence;
- whether disabling one path also disables other paths;
- whether the intervention creates an invalid or off-manifold system state;
- assigned and consumed resources, failures, and exclusions.

The supported controls are:

- no-update;
- shuffled-feedback;
- random-modification;
- internal-score;
- current-performance-matched;
- resource-matched.

If a literal control is invalid, the instrument must record the alternative identification strategy and the confound it addresses. The existence of all six records does not establish generator mediation.

**Failure if absent:** the rival explanation targeted by the missing or invalid control remains open. The claim ceiling is set by the remaining valid causal contrasts, not by the number of control names present.

### IR-09 — Conditional mediation instrumentation

**Classification:** conditional; required only for \(C_4\), with a subset required for transition-specific \(C_3\).

**Highest claim level supported:** \(C_4\).

When generator mediation is claimed, the instrument must support or document a scientifically coherent combination of:

- selective prevention of the declared generator transition;
- selective restoration or rollback;
- transplantation into a matched surrounding state when semantically coherent;
- matched testing of the changed mechanism;
- holding parallel state, memory, and external pathways fixed where possible;
- isolation and recording of alternate mediators;
- temporal-precedence checks;
- variables and treatment histories needed to assess mediator–outcome confounding, including treatment-induced confounding;
- consistency, overlap, interference, and compatibility limitations of the mediator intervention.

These operations may be impossible or meaningless for tightly coupled systems. Their unavailability is an evidence boundary, not an instruction to force an incoherent intervention.

**Failure if absent:** \(C_4\) is blocked. The admissible result may stop at \(C_2\), or at \(C_3\) when a pathway or transition contrast is independently coherent.

### IR-10 — External evaluator separation

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must distinguish external scoring from independent evaluation and record:

- who or what defines outcomes;
- evaluator code, data, configuration, and version;
- whether the system can observe evaluator identity, metadata, timing, or stopping rules;
- whether the system can influence sampling, perturbation generation, logging, exclusions, or outcome records;
- whether evaluation records and code are isolated from system writes;
- evaluator transformations between raw consequence and delivered feedback;
- known residual exploitation or coupling risks.

**Failure if absent:** self-evaluation, evaluator-gated behavior, reward hacking, and logging manipulation remain viable explanations. An external score alone cannot support an independent outcome claim.

### IR-11 — Longitudinal retention testing

**Classification:** universal support for the retention contract; detailed assays conditional on the declared retention target.

**Highest claim level supported:** \(C_4\).

The instrument must preserve a versioned protected set \(\mathcal R\), tolerances \(\epsilon_r\), and capability-specific histories. It must be able to record:

- retention-probe identity, schedule, baseline, and raw outcome;
- repeated and delayed probes where declared;
- joint and compositional probes where declared;
- access cost and latency;
- relearning or recovery trajectories;
- erase-then-relearn behavior;
- missing probes, failures, and degradation;
- whether retention is a constraint, primary dimension, or secondary diagnostic.

The records must distinguish retained performance, retained mechanism, rapid reacquisition, and inaccessible but nominally stored capability. They are not interchangeable observations.

**Failure if absent:** forgetting may be called improvement, erase-then-relearn may be called preservation, inaccessible capability may be counted as retained, or runs failing retention may disappear through survivor filtering.

### IR-12 — Sequential perturbation testing

**Classification:** conditional; required when the target includes persistence, later transfer, repeated shifts, or second-perturbation adaptability.

**Highest claim level supported:** \(C_4\).

For a sequential target, the instrument must preserve:

- ordered perturbation identifiers, assignment, and times;
- adaptation trajectories between shifts;
- mechanism and persistent-state versions after each shift;
- phase-specific and cumulative resource use;
- transfer, interference, recovery, and delayed collapse;
- whether later evaluation reuses information from earlier shifts;
- retention measurements at declared points in the sequence.

**Failure if absent:** the result is limited to a single adaptation event. No claim about persistent adaptability, accumulation, later-shift transfer, or preservation of future search is admissible.

### IR-13 — Multidimensional outcome recording

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must preserve raw or sufficiently detailed records for every declared outcome dimension before aggregation. These may include:

- adaptation latency and full adaptation trajectory;
- sample, compute, interaction, and other resource efficiency;
- terminal performance;
- perturbation breadth and coverage;
- reliability, recovery, and transfer;
- retention;
- second-shift performance;
- variance and sensitivity across units, seeds, or lineages;
- failure-tail severity and catastrophic-event frequency.

Any aggregation, dominance relation, constraint, priority, equivalence margin, or scalarization must remain an input from the frozen study contract. The instrument must retain the component records needed to audit it.

**Failure if absent:** tradeoffs can be hidden, specialization can masquerade as breadth, means can hide tail collapse, and a favorable scalar cannot be decomposed. A single capacity ranking is unsupported.

### IR-14 — Failure, censoring, and missingness capture

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must retain one auditable record for every scheduled unit or run, including:

- crashes and divergence;
- illegal or invalid updates;
- timeouts and aborted episodes;
- failed adaptations;
- missing retention probes;
- excluded units or seeds;
- unavailable evaluator outputs;
- resource overruns;
- censoring and attrition.

Each record must contain the assigned branch, failure time, preceding state reference, reason, declared inclusion or censoring treatment, analysis-stage denominator, and whether the failure is itself an outcome.

**Failure if absent:** survivor filtering, informative missingness, denominator drift, and post-treatment exclusion can reverse the observed result. `No output` cannot be distinguished from `no failure`.

### IR-15 — Temporal and stopping-rule capture

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

The instrument must preserve both the frozen intended schedule and the realized schedule, including:

- feedback and update times;
- checkpoints and adaptation windows;
- retention and delayed-evaluation windows;
- perturbation sequence;
- stopping rule, trigger, and actual stopping event;
- timing amendments and their outcome-access status;
- whether the evaluated system could observe or infer the schedule;
- post-horizon behavior when it was collected.

**Failure if absent:** optional stopping, transient-gain selection, stopping-time exploitation, delayed forgetting, and deferred collapse cannot be audited. Finite observations never establish indefinite persistence.

### IR-16 — Interface-identifiability evidence

**Classification:** universal gate.

**Highest claim level supported:** \(C_4\), when the evidence covers the observation and intervention regime needed at that level.

The instrument must preserve:

- a versioned manifest of the permitted observation and intervention interface \(O\);
- raw permitted observations;
- every transformation and summary applied to them;
- discarded fields and precision loss;
- inputs made available to a decoder or estimator;
- known observational collisions;
- exact or approximate equivalence tolerances;
- references to evidence offered for target identification over the declared class;
- the claim-level access envelope actually used.

The instrument does not prove factorization. It preserves the evidence needed to determine whether target-different systems remain observationally indistinguishable.

**Failure if absent:** the interface prerequisite cannot be audited. A target-changing observational collision blocks the corresponding claim, and unexplained summarization may have discarded the target-relevant distinction.

### IR-17 — Configuration freezing and integrity

**Classification:** universal governance requirement.

**Highest claim level supported:** \(C_4\).

The instrument must provide immutable or auditable versions of:

- system class and boundary;
- perturbation population;
- resource definitions;
- evaluation horizon and schedule;
- outcome profile and comparison rule;
- retention contract;
- observation interface;
- causal claim level and estimand;
- control definitions;
- estimator plan and uncertainty metadata;
- stopping, failure-handling, and reporting rules.

It must preserve version identifiers, hashes or equivalent integrity evidence, amendment history, exploratory/confirmatory separation, the data that motivated amendments, and detection of silent replacement.

**Failure if absent:** preregistration cannot be distinguished from outcome-driven revision, and the result cannot be tied to a stable contract.

### IR-18 — Researcher-decision audit trail

**Classification:** universal governance requirement.

**Highest claim level supported:** \(C_4\).

The instrument must record every decision capable of reversing or relabeling the result, including task and seed inclusion, unit definition, target population, perturbation and resource weighting, resource normalization, retention tolerances, horizon, control construction, outcome promotion, aggregation, exclusions, failure handling, and reporting emphasis.

Each decision record must preserve:

- actor or decision process;
- time;
- field affected;
- previous and new value;
- rationale;
- outcome-access state;
- associated data and configuration version.

**Failure if absent:** predeclared scientific judgment cannot be distinguished from post hoc sign selection.

### IR-19 — Uncertainty and replication support

**Classification:** universal capability; activation depends on the stochastic design.

**Highest claim level supported:** \(C_4\).

Without selecting an estimator, the instrument must support preservation of:

- experimental-unit, seed, and lineage identifiers;
- cluster membership, dependence, interference, and repeated-measure structure;
- pairing and assignment information;
- per-unit outcomes;
- exact sample and denominator counts at every stage;
- failed-run inclusion;
- multiplicity-family metadata;
- inputs needed for reproducible resampling or reanalysis;
- the frozen uncertainty procedure reference.

A deterministic exhaustive finite audit may not use sampling uncertainty, but its complete enumeration and exact counts must still be preserved.

**Failure if absent:** pseudoreplication, seed selection, dependence errors, multiplicity, denominator changes, and uncertainty claims cannot be audited.

### IR-20 — Claim-scoping metadata

**Classification:** universal.

**Highest claim level supported:** \(C_4\).

Every result must be inseparably indexed to its complete assay profile:

\[
\mathcal A=
(F,\mathcal D_{\mathrm{future}},B,H,V,\mathcal R,\epsilon,O)
\]

and to its causal claim level. Machine-readable result records must expose explicit fields equivalent to:

```text
system_class
perturbation_population
resource_vector
evaluation_horizon
outcome_profile
retention_set
retention_tolerances
observation_interface
causal_claim_level
```

The representation format is not fixed by this requirement.

**Failure if absent:** a result can be detached from the contract that gives it meaning and overgeneralized beyond its system class, perturbation scope, resources, horizon, target, retention contract, interface, or causal level.

## Counterfactual limits the instrument must expose

An admissible instrument record must not hide the following limits:

1. Observed branches do not reveal both potential outcomes for one realized unit.
2. A checkpoint clone does not guarantee equivalence when randomness, history, shared state, environments, or services diverge.
3. Before/after observation is not a causal counterfactual.
4. A negative control is a falsification contrast, not automatically the missing counterfactual.
5. A no-update intervention may disable an update bundle rather than \(G\) alone.
6. Random changes, rollbacks, and transplants may be invalid, off-support, or semantically incoherent.
7. Held-out perturbations establish a generalization scope, not causal exchangeability.
8. Passing all six controls does not close mediator backdoor paths or treatment-induced confounding.
9. Logging cannot verify cross-world mediation assumptions.
10. Finite observations cannot prove the absence of interference, evaluator exploitation, or target-relevant observational twins over an open class.

## Control-specific evidence ceilings

| Control | Instrument evidence that must be preserved | Strongest contribution | Failure condition |
| --- | --- | --- | --- |
| No-update | Exact gate or prevention intervention, matched handling, timing, state writes, resources, and every other path disabled by the intervention | \(C_3\) pathway-enabled effect when selective and coherent; otherwise a \(C_2\) branch contrast | The intervention disables a bundle, changes compute or timing, or creates an invalid state |
| Shuffled-feedback | Reproducible correspondence-breaking transformation plus timing, magnitude, marginals, autocorrelation, support, semantics, and resource differences | \(C_2\) correspondence-specific total effect relative to that negative control | Shuffle is incoherent, harmful, off-support, or changes information volume or semantics |
| Random-modification | Frozen transition distribution and matching on validity, locus, magnitude, sparsity, timing, search cost, and resources | \(C_3\) specificity relative to the declared alternative-transition distribution | Comparator is destructive, invalid, off-manifold, or selected as a straw alternative |
| Internal-score | Separate internal proxy record, tamper-evident external outcome, and whether the system consumes or can manipulate the proxy | \(C_1\) evaluator-gaming diagnostic | Proxy and external outcome share a mutable path, or score intervention changes behavior without being recorded |
| Current-performance-matched | Pre-treatment competence, matching variables and time, branch lineage, exclusions, and any post-treatment selection | \(C_1\) comparability and, with valid assignment, \(C_2\) exchangeability conditional on observed baselines | Matching is post-treatment, induces collider selection, or omits latent competence |
| Resource-matched | Available, consumed, and inherited end-to-end resource vectors across feedback, transition search, adaptation, and evaluation | Weakens a declared resource rival at any claim level | Precomputation, information, tools, storage, or parallelism is omitted, or arbitrary conversion hides a tradeoff |

Passing every row establishes no automatic claim level. Each control addresses a particular rival explanation under its own validity conditions.

## Traceability matrix

| Charter or audit obligation | Instrument capability required | Claim level enabled | Failure if absent | Universal or conditional |
| --- | --- | --- | --- | --- |
| **IR-01 — Causal objects; starting-state and estimand declarations; parallel-mediator audit** | Preserve the study-declared \(S/G/W/E\) role boundary, mutability, exclusions, hidden-state limits, and cross-branch stability | Through \(C_4\); fine generator boundary first required for \(C_3\) | Generator-specific language has no stable referent; effects can be relabeled across state classes | Universal core; generator extension conditional for \(C_3,C_4\) |
| **IR-02 — Starting state, experimental unit, provenance, latent-competence audit** | Identify starting states, versions, initialization, persistent stores, tools, prior exposure, randomness, interference, and descendant lineage | Through \(C_4\) | Baseline inequality, stored competence, interference, or pseudoreplication remains open | Universal |
| **IR-03 — Feedback declaration and immutable lineage; provenance-not-mediation audit** | Record raw event, consequence, transformation, delivery, exposure, writes, persistence, descendants, and outcomes | First required for \(C_2\); contributes through \(C_4\) | Feedback branch and chronology cannot be reconstructed; mediation still remains unproven even when present | Conditional for \(C_2\)–\(C_4\) |
| **IR-04 — Held-out population and exposure ledger; lookup and contamination attacks** | Preserve all development, selection, validation, evaluation, tool, cache, prompt, template, family, and benchmark exposures with novelty level | Through \(C_4\) as a scope prerequisite | Held-out status, new adaptation, and generalization scope are unverifiable | Universal for held-out claims |
| **IR-05 — Perturbation population, assignment, sequencing, and exclusion audit** | Version population, sampling, weights, labels, order, branch assignment, source, filtering, exclusions, and development/test separation | \(C_1\) scope; causal extension through \(C_4\) | Favorable selection, treatment-dependent support, or post hoc exclusion can explain the result | Universal core; assignment extension conditional for \(C_2\)–\(C_4\) |
| **IR-06 — Complete resource vector; effective-resource leakage audit** | Record available, consumed, and inherited resources across the full lifecycle without forced conversion | Through \(C_4\) as comparability evidence | Hidden precomputation, tools, information, time, or initialization can masquerade as capacity | Universal |
| **IR-07 — Generator transition and state-write record; change-is-not-benefit rule** | Version pre/post mechanism identity, update source/time, representation, persistence, overwrite, parallel writes, and control opportunity | \(C_3\), and mediator measurement for \(C_4\) | Transition/pathway contrast is unavailable; chronology alone cannot replace intervention | Conditional for \(C_3,C_4\) |
| **IR-08 — Six confound checks and their limitations; all-controls-passing counterexamples** | Preserve exact intervention, branch differences, resources, validity, support, semantics, pathway coupling, and failures for every invoked control | First applicable at \(C_2\); can contribute through \(C_4\) | The targeted rival remains open; invalid controls can create their own confound | Conditional on causal design |
| **IR-09 — Mediation assumptions and coherent intervention; parallel \(W\) audit** | Support selective prevention, restoration, coherent transplant or equivalent mediator contrast, alternate-mediator isolation, and confounder evidence | \(C_4\) | Generator mediation is unavailable; claim stops at a supported lower level | Conditional only for \(C_4\), with subsets for transition-specific \(C_3\) |
| **IR-10 — External outcome and evaluator independence boundary; sleeper attack** | Version evaluator and record visibility, manipulability, sampling, stopping, logging, exclusions, perturbation control, and outcome integrity | Through \(C_4\) as outcome-validity evidence | Self-report, evaluator gating, reward hacking, or record manipulation remains viable | Universal |
| **IR-11 — Retention contract; undeclared-loss and erase/relearn attacks** | Version \(\mathcal R,\epsilon_r\) and preserve probe identities, times, raw outcomes, access costs, recovery, missingness, and histories | Through \(C_4\) | Forgetting can be hidden, reacquisition confused with preservation, or failures filtered | Universal contract support; detailed assays conditional |
| **IR-12 — Subsequent transfer and repeated shifts; delayed-collapse audit** | Record perturbation order, between-shift adaptation, mechanism versions, cumulative resources, transfer, reuse, and delayed failures | Through \(C_4\) for sequential targets | Only a single-shift result is supported | Conditional on persistence, transfer, or repeated-shift claim |
| **IR-13 — Separate outcome dimensions; scalarization and tail-risk audit** | Preserve dimension-level trajectories, efficiencies, breadth, reliability, retention, transfer, variance, and tails before aggregation | Through \(C_4\) as target evidence | Tradeoffs, specialization, or tail collapse can be hidden by aggregation | Universal |
| **IR-14 — Failed-run policy; survivor-filtering audit** | Record every scheduled run, failure, timeout, invalid update, missing probe, exclusion, censoring decision, and denominator | Through \(C_4\) | Attrition and survivor filtering can reverse the result | Universal |
| **IR-15 — Horizon and schedule; stopping-time and temporal-reversal audit** | Preserve intended and actual schedules, checkpoints, windows, triggers, amendments, system visibility, and collected later behavior | Through \(C_4\) | Optional stopping, transient gains, delayed forgetting, and deferred collapse cannot be audited | Universal |
| **IR-16 — Interface prerequisite; observational-twin audit** | Preserve \(O\), raw observations, transformations, discarded information, estimator inputs, tolerances, collisions, and identification evidence | Universal gate through \(C_4\) | Target-changing observational equivalence blocks the corresponding claim | Universal |
| **IR-17 — Frozen declarations and amendments; post hoc revision audit** | Version and integrity-protect the full contract, claim level, controls, analysis plan, amendments, and motivating data | Through \(C_4\) | Moving targets and reuse of amendment-motivating data cannot be detected | Universal |
| **IR-18 — Researcher decisions; degrees-of-freedom audit** | Record actor, time, field, old/new value, rationale, outcome access, and data version for result-reversing decisions | Through \(C_4\) | Preregistered judgment cannot be distinguished from post hoc sign selection | Universal |
| **IR-19 — Replication and uncertainty; seed, dependence, and denominator audit** | Preserve units, seeds, lineages, clusters, pairing, assignment, per-unit outcomes, counts, failures, multiplicity, and reanalysis inputs | Through \(C_4\) | Pseudoreplication, cherry-picking, uncertainty, and denominator drift cannot be audited | Universal capability; stochastic use conditional |
| **IR-20 — Complete assay profile; scope-overreach audit** | Bind each result to \((F,\mathcal D,B,H,V,\mathcal R,\epsilon,O)\) and its causal level | Through \(C_4\) | Results can be detached from their scientific scope and overgeneralized | Universal |

## Minimum cumulative instrument profiles

These profiles describe the smallest capability boundary for each claim level. They do not require every conditional assay and do not prescribe an implementation.

### Minimum profile for \(C_1\): scoped future-adaptation profile difference

The instrument must provide:

1. a stable whole-system boundary and experimental-unit identity;
2. starting-state and descendant lineage records;
3. a frozen perturbation population, novelty level, exposure ledger, and sampling record;
4. complete available/consumed/inherited resource vectors;
5. tamper-evident external outcomes and evaluator-boundary records;
6. the declared adaptation trajectories, retention outcomes, dimensional profile, failures, missingness, and temporal schedule;
7. the permitted observation interface and evidence relevant to target identification;
8. frozen configuration, amendment, and researcher-decision histories;
9. unit, dependence, exact-count, and uncertainty metadata;
10. complete assay-profile indices.

Sequential-perturbation and detailed retention capabilities are activated only when those dimensions are part of the \(C_1\) target.

The maximum conclusion is:

> The declared future-adaptation profiles differ under the frozen assay.

Feedback assignment, no-update intervention, transition recording, and mediator isolation are not intrinsically required for \(C_1\).

### Additional profile for \(C_2\): causal total feedback-branch effect

In addition to \(C_1\), the instrument must provide:

1. assignment to a versioned feedback policy \(Z\) and a declared comparator;
2. matched, cloned, randomized, or otherwise exchangeable starting branches, with the supporting design recorded;
3. delivered treatment versions, feedback provenance, branch lineage, and every treatment-dependent state write;
4. treatment-independent perturbation and evaluator assignment, or exact records of any differences included in the treatment;
5. interference records for shared memory, tools, environments, communication, and evaluator state;
6. end-to-end branch resource accounting;
7. the valid comparator or control evidence required by the particular causal contrast.

The result includes every causal path inside the feedback branch, including generator change, ordinary learning, memory, tools, direct information transfer, and other state changes.

The maximum conclusion is:

> Assignment to the declared feedback policy caused a scoped difference in the complete future-adaptation branch.

### Additional profile for \(C_3\): update-pathway or transition-specific effect

In addition to \(C_2\), the instrument must provide:

1. a frozen pathway or transition boundary and exact pre/post identity;
2. a coherent selective intervention that enables, prevents, restores, replays, or applies the declared pathway or transition;
3. matched handling or sham evidence and complete records of induced compute, timing, opportunity, and state-write differences;
4. evidence that compared intervention states are valid and on-support for the declared starting states;
5. evidence that pathway gating does not silently disable alternate processes;
6. valid no-update evidence and, when specificity is claimed, an on-support alternative-transition comparator;
7. transition-selection provenance showing no confirmatory-outcome selection.

For a particular-transition claim, applying or restoring the transition must have coherent meaning in the matched surrounding state. If \(G\) cannot be separated from \(S\) or \(W\), that claim is unavailable even when a broader pathway-enabled branch effect remains possible.

The maximum conclusion is:

> Permitting the declared update pathway, or applying the declared transition, caused the scoped profile difference.

This is not yet a mediation claim about feedback.

### Additional profile for \(C_4\): generator-mediated effect

In addition to \(C_3\), the instrument must provide:

1. both a valid feedback assignment contrast and a well-defined mediator contrast for \(M=G_t\rightsquigarrow G_{t+1}\);
2. records and interventions sufficient to distinguish competing mediators \(W\), including memory, representations, policy, data, tools, stores, environment changes, and ordinary learning;
3. coherent generator blocking, restoration, transplant, or equivalent evidence required by the frozen mediation-identification assumptions;
4. temporal resolution sufficient to establish the declared order;
5. records for mediator–outcome confounders, including confounders caused by feedback assignment;
6. evidence about consistency, semantic compatibility, overlap, and interference for mediator interventions;
7. preserved direct \(Z\to Y\) and alternate \(Z\to W\to Y\) paths rather than an assumption that complete logging removed them;
8. the exact mediation estimand and assumption set.

The maximum conclusion is:

> The declared generator transition mediated the scoped total feedback effect under the frozen intervention design and assumptions.

If the mediator cannot be coherently manipulated or identified, the claim stops at \(C_2\) or \(C_3\), according to the available contrast.

## Claim ceilings and failure conditions

| Missing or invalid capability | Highest remaining admissible result |
| --- | --- |
| Missing assay indices, external outcome integrity, dimensional records, failure records, or interface-identifiability evidence | No admissible \(C_1\) adaptive-capacity-profile claim |
| Unknown or incomparable starting states/resources | Unmatched descriptive record only; comparative \(C_1\) is blocked |
| Unverifiable held-out or exposure boundary | Result narrowed to verified exposure scope, or inconclusive for novelty/generalization |
| Unknown assignment, invalid comparator, lack of exchangeability, or uncontrolled interference | \(C_1\) description may remain; \(C_2\) is blocked |
| Feedback chronology recorded but no pathway intervention | At most \(C_2\); \(C_3\) is blocked |
| Pathway intervention manipulates a bundle or creates an invalid/off-support state | At most the broader valid branch contrast; isolated \(C_3\) is blocked |
| Generator and surrounding state are nonseparable or transplant is incoherent | Transition-specific \(C_3\) and \(C_4\) are blocked |
| Competing mediator \(W\) always co-varies, mediator intervention is undefined, or treatment-induced confounding is unobserved | \(C_4\) is blocked; supported \(C_2\) or \(C_3\) may remain |
| Passing all six controls without mediator identification | No automatic upgrade; claim remains at the level identified by the actual contrasts |
| Incomplete resource ledger | Resource-adjusted capacity claim blocked or classified as resource-mediated/incomparable |
| Silent attrition, censoring, or denominator changes | Comparative and causal result blocked until the complete outcome population is visible |
| Missing horizon or stopping-rule integrity | Persistence and temporal comparison claims blocked; collected observations remain descriptive |
| Target-changing observational collision under \(O\) | Corresponding target claim is non-identifiable through that interface |
| Configuration or amendment history unavailable | Confirmatory status and preregistered claim are unavailable |

## Explicit non-goals

This requirements extraction does not:

- design CNI or NOOA;
- claim that CNI, NOOA, or any other architecture implements adaptive capacity;
- introduce CURM, EMI, RMC, or another substrate ontology;
- choose software components or classes;
- choose a learning architecture;
- select a benchmark, environment, perturbation population, or dataset;
- define an adaptive-capacity estimator;
- define a scalar capacity metric;
- define a universal conversion among resources;
- formulate a theorem or novelty claim;
- infer update-pathway effects from transition logs;
- infer generator mediation from chronology, provenance, or control count;
- repair or amend the measurement charter;
- revise the hostile audit;
- authorize implementation or instrumentation work.

## Minimum unresolved choices before candidate instruments can be compared

1. Which claim levels, \(C_1\) through \(C_4\), candidate instruments are required to support.
2. Which system-boundary and substrate classes the comparison covers.
3. The permitted observational and interventional access envelope.
4. Required temporal resolution, causal-order semantics, and clock synchronization.
5. Required capture fidelity, precision, and tolerance for observations and interface-collision evidence.
6. Which retention, joint-capability, access-cost, and sequential-assay capabilities are mandatory versus conditionally supported.
7. The resource categories, provenance boundary, and accounting resolution instruments must represent.
8. The failure, missingness, exclusion, censoring, and denominator event vocabulary.
9. The experimental-unit, seed, lineage, clustering, dependence, pairing, and interference metadata vocabulary.
10. The exposure and leakage identity scheme, novelty levels, and ledger granularity.
11. The evaluator-independence and outcome-integrity evidence candidate instruments must preserve.
12. The immutable configuration, integrity-evidence, amendment, and exploratory/confirmatory governance model.
13. The researcher-decision audit fields and operational meaning of confirmatory outcome access.
14. The interface-identifiability evidence, known-collision, summary-transformation, and discarded-data representation.
15. The machine-readable assay-profile and result-linkage fields used to compare record completeness.
