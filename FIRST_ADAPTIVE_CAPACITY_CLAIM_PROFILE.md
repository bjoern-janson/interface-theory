# First Adaptive-Capacity Claim Profile

## Status and purpose

This document freezes the strongest scientific claim level authorized for the first adaptive-capacity study. It is a claim-selection artifact only.

It is governed by:

- `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md`;
- `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER_HOSTILE_AUDIT.md`;
- `INSTRUMENTATION_REQUIREMENTS_ADAPTIVE_CAPACITY.md`.

It does not select an architecture, instrument, benchmark, environment, estimator, intervention design, or experiment.

Its purpose is to prevent observational evidence, provenance, internal visibility, mechanism changes, or instrument richness from being used to support a stronger causal statement than the frozen profile permits.

## Frozen first claim level

The strongest authorized claim is:

\[
\boxed{
C_2:
\text{causal total feedback-branch effect}
}
\]

Its required descriptive outcome basis is:

\[
\boxed{
C_1:
\text{scoped future-adaptation profile difference}
}
\]

The following levels are outside this profile:

\[
\boxed{
C_3:
\text{update-pathway or transition-specific effect}
}
\]

\[
\boxed{
C_4:
\text{generator-mediated effect}
}
\]

This document does not authorize a future attempt to support \(C_3\) or \(C_4\). Either level requires a separately frozen claim-profile artifact before candidate-instrument selection or experiment design.

## Claim hierarchy

The complete hierarchy remains:

\[
\begin{aligned}
C_1 &: \text{scoped future-adaptation profile difference},\\
C_2 &: \text{causal total feedback-branch effect},\\
C_3 &: \text{update-pathway or transition-specific effect},\\
C_4 &: \text{generator-mediated effect}.
\end{aligned}
\]

The implication

\[
C_4\Rightarrow C_3\Rightarrow C_2\Rightarrow C_1
\]

holds only when the interventions, causal contrasts, scope declarations, and identifiability conditions required at every level are independently satisfied.

Additional state access, logging, telemetry, architectural detail, or internal visibility does not raise the claim level.

## Frozen primary claim language

When a materially nonzero \(C_2\) contrast is identified, the admissible primary claim is:

> **Assignment to a declared externally grounded feedback policy causally changes the system's future-adaptation profile under a frozen assay profile, relative to a declared comparator.**

This is a whole-branch causal claim. The treatment effect may include paths through:

- ordinary learning;
- representations;
- memory;
- update selection;
- tools;
- policy changes;
- generator changes;
- persistent system state;
- any other treatment-dependent pathway inside the declared branch.

The primary claim attributes the effect only to assignment to the complete feedback policy relative to its comparator. It does not attribute the effect to a particular pathway, state transition, mechanism, or generator modification.

\(C_2\) is a causal estimand and identification level, not a guarantee of a positive or nonzero result. When a valid \(C_2\) analysis establishes practical equivalence, the admissible language is:

> **Assignment to the declared externally grounded feedback policy produced no material change in the system's future-adaptation profile under the frozen assay, relative to the declared comparator.**

A negative or incomparable effect vector may likewise retain \(C_2\) when the whole-branch causal contrast remains identified.

If the causal requirements for \(C_2\) fail but a valid scoped comparison remains, the language must be downgraded to:

> **A difference in the declared future-adaptation profiles was observed under the frozen assay.**

The downgraded statement is \(C_1\) and contains no causal verb.

## Frozen assay scope

Every conclusion is indexed to:

\[
\mathcal A=
(F,\mathcal D_{\mathrm{future}},B,H,V,\mathcal R,\epsilon,O),
\]

where:

- \(F\) is the declared system class;
- \(\mathcal D_{\mathrm{future}}\) is the declared perturbation population;
- \(B\) is the declared heterogeneous resource vector;
- \(H\) is the declared evaluation horizon and schedule;
- \(V\) is the declared multidimensional outcome profile and frozen comparison rule;
- \(\mathcal R\) is the declared retention set;
- \(\epsilon\) contains the declared retention tolerances;
- \(O\) is the permitted observation interface.

The claim does not generalize beyond these indices. In particular, the unindexed phrase

> adaptive capacity increased

is inadmissible.

The result must preserve whether evaluation concerns unseen instances, seeds, configurations, perturbation families, or causal mechanisms. `Held out` is not a scope by itself.

## Included evidence boundary

### Required \(C_1\) descriptive basis

The first study must record the scoped future-adaptation profile that serves as the outcome basis for \(C_2\). Every declared dimension remains separately visible before application of a frozen comparison rule.

Applicable dimensions may include:

- adaptation latency and adaptation-curve shape;
- sample efficiency;
- compute and interaction efficiency;
- terminal performance;
- perturbation breadth and coverage;
- reliability and recovery;
- retention;
- subsequent transfer and later-shift behavior;
- variance across declared units or seeds;
- failure tails and catastrophic failures.

The \(C_1\) evidence boundary requires:

- a stable whole-system and experimental-unit boundary;
- starting-state and descendant lineage records;
- perturbation identities, scope, order, and sampling records;
- exposure and leakage records;
- complete available, consumed, and inherited resource vectors;
- external outcome and evaluator-boundary records;
- multidimensional outcomes, retention, failures, missingness, and timing;
- observation-interface and identifiability evidence;
- frozen configuration and researcher-decision provenance;
- exact unit, denominator, dependence, and uncertainty metadata;
- complete assay-scope indices.

This evidence supports only a descriptive difference unless the additional \(C_2\) conditions hold.

### Required \(C_2\) causal evidence

The primary claim additionally requires:

- assignment to a declared and versioned externally grounded feedback policy;
- a frozen, scientifically coherent comparator;
- a valid whole-branch causal contrast;
- matched, cloned, randomized, or otherwise exchangeable starting branches, with the supporting design recorded;
- complete feedback-policy, treatment-exposure, and comparator provenance;
- treatment and control assignment records;
- perturbation-assignment integrity and treatment-independent outcome sampling, or explicit inclusion of differences in the treatment definition;
- exposure and leakage accounting across development, modification, selection, and confirmatory evaluation;
- comparability or explicit modeling of pre-assignment, baseline, and inherited resource differences;
- complete recording of treatment-induced resource use as part of the total feedback branch;
- external evaluator and outcome-record integrity;
- interference records for shared memory, tools, environments, evaluators, communication, and external services;
- complete failure, exclusion, censoring, attrition, and denominator records;
- frozen assay, decision, amendment, and governance metadata.

The causal result belongs to the complete treatment branch. It includes every internal and external path changed by the feedback policy unless the treatment definition explicitly excludes that path.

Resources caused by feedback assignment are mediators inside this total branch; they do not invalidate the \(C_2\) assignment effect. They do prevent a resource-independent or matched-resource adaptive-capacity interpretation unless a separately declared contrast supports it. Pre-existing, uncontrolled, or treatment-extraneous resource differences remain comparability threats.

## Causal meaning of externally grounded feedback

For this profile, `externally grounded feedback` requires a declared assignment policy and a raw consequence that is not solely controlled by the evaluated system. The records must distinguish:

- assigned feedback policy;
- raw external event or consequence;
- evaluator transformation;
- delivered signal;
- actual exposure;
- complete treatment-dependent branch.

The realized consequence may depend on earlier system behavior and must not be substituted for the assigned treatment without a corresponding causal design.

External provenance does not guarantee evaluator independence, immunity to manipulation, or mechanism mediation.

`Externally grounded` describes the assigned policy and provenance of its consequences. A \(C_2\) comparison against an arbitrary coherent comparator identifies only that policy contrast. A stronger statement that **correspondence to external consequences** caused the effect requires a comparator that specifically varies correspondence while preserving the other declared treatment features.

Imperfect receipt or compliance does not automatically destroy an assignment effect. When assignment is the frozen estimand, treatment versions, branch membership, noncompliance, and crossover must be recorded; a causal claim about receipt or exposure requires its own valid contrast.

## Explicit \(C_3\) exclusion

The first study must not claim that a particular update pathway, mechanism, or state transition caused the future-adaptation result.

The following are insufficient to support \(C_3\):

- chronological ordering;
- causal trace or provenance logs;
- pre/post state differences;
- parameter differences;
- memory differences;
- program, code, or graph differences;
- architecture visibility;
- pathway names;
- correlation between a recorded update and later outcomes;
- update persistence;
- disabling an intervention bundle whose components are not isolated;
- an off-support rollback, replay, or random modification;
- a transition selected using confirmatory outcomes.

The statement

> the declared update pathway caused the future-adaptation difference

is outside this profile.

Exploratory pathway evidence may be collected. It must remain segregated from the confirmatory conclusion and cannot raise the claim ceiling.

## Explicit \(C_4\) exclusion

The first study must not claim that a generator transition mediated the feedback effect.

None of the following is sufficient:

\[
G_{t+1}\neq G_t,
\]

\[
\Omega_t\longrightarrow G_{t+1},
\]

\[
G_{t+1}\longrightarrow V_{\mathrm{future}},
\]

or any logged chronology combining them.

Generator mediation belongs to a separate claim profile because it requires additional conditions concerning:

- a coherent selective mediator intervention;
- alternate mediators;
- parallel state, memory, tool, and environment pathways;
- mediator–outcome confounding;
- treatment-induced confounding;
- semantic compatibility of blocking, rollback, restoration, or transplantation;
- overlap, consistency, and interference;
- interface identifiability at the mediation level.

No such claim is authorized here. Complete lineage, detailed internal access, or all six charter controls do not change that exclusion.

## Required result metadata

Every admissible result must expose machine-readable or equivalently auditable fields for:

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
feedback_policy
comparator
configuration_version
assignment_mechanism
treatment_version
branch_lineage
interference_status
evaluator_version
resource_comparability_status
result_classification
```

The frozen causal level is:

```text
C2_TOTAL_FEEDBACK_BRANCH_EFFECT
```

unless the result is downgraded. A result detached from the complete assay profile, comparator, feedback policy, or configuration version cannot support the primary claim.

## Candidate-instrument evaluation boundary

Candidate instruments may be compared only against requirements necessary for:

\[
\boxed{C_1+C_2}
\]

The required scope includes:

- assay-profile integrity;
- whole-system boundary declaration;
- starting-state and lineage comparability;
- feedback-policy and comparator assignment;
- counterfactual-control evidence or valid alternative confound checks required by the declared \(C_2\) design;
- feedback provenance;
- exposure and leakage accounting;
- perturbation isolation, assignment, ordering, and exclusions;
- complete resource accounting;
- external evaluator separation and outcome integrity;
- multidimensional outcome recording;
- retention measurement under the frozen contract;
- failure, missingness, censoring, and denominator capture;
- temporal and stopping-rule integrity;
- interference records;
- configuration and amendment integrity;
- researcher-decision provenance;
- interface-identifiability evidence at the \(C_1/C_2\) level;
- replication, pairing, dependence, exact-count, multiplicity, and uncertainty support;
- complete claim-scoping metadata.

This profile must not require:

- selective generator intervention;
- generator transplantation, rollback, or restoration;
- mediator isolation;
- a universal \(S/G/W\) decomposition;
- transition-specific causal identification;
- \(C_3\) or \(C_4\) instrumentation capabilities.

A candidate instrument may expose additional information. That information neither changes the comparison requirements nor raises the frozen claim level.

Selective generator intervention is not a universal \(C_2\) requirement. A particular \(C_2\) design may nevertheless invoke no-update, random-modification, or another confound check that requires a limited intervention capability. Such capability is evaluated only for the validity of that branch comparator and cannot be interpreted as \(C_3\) evidence.

## Result classifications and downgrade rules

### Admissible \(C_2\) result

A \(C_2\) result is admissible only when:

- feedback assignment, treatment version, branch membership, and the exposure information required by the frozen assignment estimand are valid;
- the comparator is coherent for the declared contrast;
- the whole-branch causal contrast is identifiable;
- starting-state comparability or exchangeability is supported;
- perturbation handling and exposure boundaries are auditable;
- pre-assignment and treatment-extraneous resources do not provide an undeclared explanation;
- treatment-induced resource changes are preserved as part of the total branch and remain visible in the profile;
- evaluator and outcome integrity are preserved;
- interference is absent, controlled, or included in the treatment definition;
- the multidimensional outcome has a frozen decision rule;
- retention, failures, exclusions, and missingness are interpretable;
- assay and configuration integrity remain intact.

The classification may be positive, no material change, negative, specialization, forgetting-mediated, adaptive collapse, incomparable, or another charter-authorized descriptor. \(C_2\) identifies the branch contrast, not a universal capacity ordering.

Claim level and outcome classification are orthogonal. A precisely equivalent, negative, mixed, resource-mediated, or incomparable causal effect may retain `C2_TOTAL_FEEDBACK_BRANCH_EFFECT` when the assignment contrast is valid. Descriptive labels may be cumulative rather than mutually exclusive.

### Downgrade to \(C_1\)

The result must be downgraded to a descriptive \(C_1\) comparison when any causal requirement fails but a valid scoped profile comparison remains, including when:

- causal assignment is absent or insufficient;
- comparator validity is unresolved;
- exchangeability or starting-state comparability is unsupported;
- assignment, treatment version, branch membership, or crossover cannot be reconstructed for the frozen estimand;
- interference prevents branch-level attribution;
- assignment, comparator, branch, or outcome provenance required for the whole-branch contrast cannot be reconstructed;
- perturbation or evaluator assignment depends on treatment in an unmodeled way.

The surviving statement may describe only the observed profile difference under the frozen assay. It must not use causal language.

Variation in realized exposure or noncompliance does not force this downgrade when assignment is the frozen estimand and assignment, treatment versions, branch membership, and outcomes remain validly recorded.

### Resource-confounded or resource-incomparable comparison

When pre-existing, uncontrolled, or treatment-extraneous resource differences plausibly explain the comparison, the admissible conclusion is limited to:

> **A descriptive future-adaptation profile difference was observed under unequal or noncomparable resource conditions.**

It is classified as:

\[
\boxed{
\text{resource-confounded or resource-incomparable difference}
}
\]

It is not evidence of an adaptive-capacity advantage.

When the assigned feedback policy itself causes additional computation, memory, tool use, or other resource consumption, those resources are part of the \(C_2\) total branch. The admissible classification is **resource-mediated total feedback-branch effect**. It may retain \(C_2\), but it does not establish a resource-independent or matched-resource adaptive-capacity advantage. If its resource–outcome profile lacks a frozen ordering, it is also incomparable.

### Incomparable result

A result is incomparable when:

- some declared outcome dimensions improve while others degrade;
- the frozen comparison rule supplies no ordering;
- heterogeneous resource–outcome profiles remain unordered;
- retention, breadth, latency, reliability, transfer, or tail dimensions conflict without declared priority.

\[
\boxed{
\text{incomparable}\neq\text{inconclusive}
}
\]

An incomparable result can be completely measured and scientifically valid. It supports no positive or negative total ordering.

When its branch contrast is causally identified, an incomparable effect retains `C2_TOTAL_FEEDBACK_BRANCH_EFFECT`. `Incomparable` describes the absence of an outcome ordering, not failure of causal identification.

### Inconclusive result

A result is inconclusive at its intended claim level when the evidence is insufficient for that level. The result is downgraded rather than discarded whenever a valid weaker claim survives.

\(C_2\) is inconclusive, while \(C_1\) may remain available, when:

- evaluator sampling, stopping, or versions compromise the causal branch comparison but still permit a descriptive record;
- causal precision is insufficient while the observed profiles remain reconstructable;
- leakage or configuration uncertainty blocks the intended causal or confirmatory interpretation without erasing the observed profile;
- the comparator, assignment, or interference conditions fail while starting states and outcomes remain descriptively comparable.

The result is inconclusive even at \(C_1\) when:

- perturbation scope cannot be reconstructed;
- leakage cannot be assessed;
- outcome integrity is compromised so that the observed profile itself is untrustworthy;
- retention evidence is missing or uninterpretable;
- failures, exclusions, or denominators cannot be reconstructed;
- precision is insufficient for every frozen descriptive classification, including equivalence and direction;
- interface identifiability is unsupported;
- configuration integrity is unavailable to the extent that the assay producing the observations cannot be reconstructed;
- no valid \(C_1\) comparison survives failure of the causal contrast.

Inconclusive is an evidentiary failure, not a multidimensional tradeoff.

Evaluator independence and external scoring are distinct. A stable, tamper-evident but non-independent evaluator can support a profile explicitly scoped to that evaluator interaction, and may support \(C_2\) if evaluator behavior is treatment-independent under the branch contrast. It cannot support a broader claim of evaluator-independent validity.

### No automatic upgrade

No result can be raised beyond \(C_2\) by:

- richer internal logging;
- additional state visibility;
- parameter or code access;
- larger state descriptions;
- architectural complexity;
- self-reported mechanism labels;
- internal estimates of improvement;
- causal narratives generated by the evaluated system;
- post hoc pathway analysis;
- the presence of CNI, NOOA, or any other named architecture.

## Governance constraints

\[
\boxed{
\text{No architecture enters until the claim level is frozen.}
}
\]

\[
\boxed{
\text{No claim level is raised because an architecture exposes more variables.}
}
\]

\[
\boxed{
\text{A stronger instrument cannot silently produce a stronger claim.}
}
\]

\[
\boxed{
\text{Exploratory internal evidence cannot enter the confirmatory claim without a new frozen claim profile.}
}
\]

Instrumentation determines which evidence can be collected. It does not determine which variables are scientifically fundamental.

Architecture remains subordinate to the frozen claim contract.

## Stop boundary

This document freezes only the claim ceiling and the evidence boundary. It does not authorize instrument comparison, instrument recommendation, scorecard construction, instrument selection, experiment design, or implementation.

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

This claim profile does not:

- design CNI or NOOA;
- evaluate CURM, EMI, or RMC;
- compare, select, rank, or recommend candidate instruments;
- create an instrument scorecard;
- define software components or choose an implementation;
- choose an environment, perturbation population, dataset, or benchmark;
- define an experiment, estimator, or analysis method;
- introduce a new theory;
- define a universal adaptive-capacity property;
- define a scalar \(C_{\mathrm{improve}}\);
- support an update-pathway or transition-specific effect;
- support generator mediation;
- amend the measurement charter, hostile audit, or instrumentation requirements;
- authorize implementation.

## Minimum unresolved choices before instrument comparison

1. The system and substrate classes candidate instruments must support.
2. The permitted observational access envelope for \(C_1\) and \(C_2\).
3. The permitted feedback-policy intervention, comparator, and assignment envelope.
4. The required temporal resolution, causal-order semantics, and schedule visibility records.
5. The required capture fidelity, precision, and approximate-identifiability tolerances.
6. The required exposure-ledger identities, novelty levels, and granularity.
7. The required resource categories and accounting precision for available, consumed, and inherited resources.
8. The required perturbation population, assignment, ordering, exclusion, and treatment-dependence records.
9. The required evaluator-isolation, manipulation-boundary, and outcome-integrity evidence.
10. The required retention, joint-capability, access-cost, failure, missingness, censoring, and denominator records.
11. The required starting-state, lineage, clustering, pairing, dependence, and interference evidence.
12. The required configuration integrity, amendment history, exploratory/confirmatory separation, and researcher-decision audit evidence.
13. The required interface-identifiability and known-collision evidence at the \(C_1/C_2\) level.
14. The machine-readable assay-profile, feedback-policy, comparator, claim-level, and configuration-linkage schema.
