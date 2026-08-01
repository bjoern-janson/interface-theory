# Adaptive Capacity Measurement Charter

## Status and authority

This document freezes the minimum evaluation contract for claims about changes in future adaptive capacity.

It begins after two settled containment results:

1. executable target-relative adaptive testing is established prior art;
2. recursive modification of adaptation-generating machinery is established prior art.

This charter does not reopen those conclusions, establish that adaptive capacity is identifiable, define a theory of intelligence, or privilege an architecture, benchmark, environment, estimator, or scalar score.

Its governing rule is:

\[
\boxed{
\text{Freeze the claim conditions and unresolved choices, not a preferred measurement.}
}
\]

## Central question

> Can assignment to externally grounded feedback cause a measurable change in future adaptation under held-out environmental perturbations, matched adaptation resources, declared horizons, and predeclared retention constraints?

The target is not merely current competence:

\[
V_{\mathrm{current},t+1}>V_{\mathrm{current},t}.
\]

The target is also not merely a mechanism change:

\[
G_{t+1}\neq G_t.
\]

The target is a scoped causal claim that a feedback-induced change produces an advantage or disadvantage in later adaptation:

\[
\text{feedback assignment}
\longrightarrow
\text{generator transition}
\longrightarrow
\text{future-adaptation outcome}.
\]

This pathway may yield increased capacity, no material change, mixed tradeoffs, specialization, forgetting, or adaptive collapse.

## Operational target

The object to be evaluated is a **future-adaptation profile**, not a presumed one-dimensional internal property.

For a declared system boundary, perturbation population, adaptation budget, horizon, external outcome family, and retention contract, the profile may contain separate quantities for:

- adaptation latency;
- sample efficiency;
- resource efficiency;
- terminal held-out performance;
- breadth across perturbations;
- recovery reliability;
- retention;
- transfer to subsequent perturbations;
- robustness across seeds or independent replicates;
- variance, lower-tail performance, and catastrophic-failure risk.

Any claim of increase, decrease, or no material change is relative to the complete declared contract:

\[
(F,S_t,G_t,\mathcal D_{\mathrm{future}},B,H,V,\mathcal R,\epsilon).
\]

It is not a context-free property of \(G\).

### Illustrative measurement form

The following is permitted as a task-specific candidate, but is not frozen as the construct:

\[
C_{\mathrm{future}}^{(j)}(S,G)
=
\mathbb E_{e\sim\mathcal D_{\mathrm{future}}}
\left[
V_j\!\left(
\operatorname{Adapt}(S,G,e;B),
e,
H
\right)
\right],
\]

where \(j\) indexes a declared outcome dimension. The collection of dimensions may be retained as a vector or distribution rather than aggregated.

A contrast such as

\[
C_{\mathrm{future}}^{(j)}(S_t,G_{t+1})
-
C_{\mathrm{future}}^{(j)}(S_t,G_t)
\]

is meaningful only when installing either generator into the same starting state is well-defined and support-compatible. If \(S\) and \(G\) cannot coherently be separated or transplanted, the experiment must compare complete treatment branches and describe the result as a branch-level effect, not a generator-specific effect.

The notation \(\Delta G_t\) is schematic. It records a declared transition

\[
G_t\rightsquigarrow G_{t+1},
\]

not necessarily subtraction in a vector space.

## Required distinctions

### Current competence improvement

Better present performance is evidence about present competence. It is not sufficient evidence about future adaptation.

### Mechanism modification

A change in parameters, code, representations, update rules, search distributions, or generator structure establishes only that modification occurred.

### Future adaptation improvement

The modified branch must adapt more effectively under previously unused perturbations, with matched starting conditions and resources, according to a predeclared comparison rule.

### Adaptive-capacity degradation

Current competence may improve while later adaptation becomes slower, narrower, less reliable, more resource-intensive, or more destructive of retained capabilities. The charter must preserve this as a legitimate negative result.

## Causal objects and permitted claim levels

A causal evaluation must distinguish:

- \(Z\): assignment to a feedback channel or feedback policy;
- \(\Omega_t\): the realized external consequence and the signal delivered to the system;
- \(M\): the observed generator transition \(G_t\rightsquigarrow G_{t+1}\);
- \(W\): other post-feedback changes in memory, representations, data, policy, external stores, tools, or environment state;
- \(Y\): the future-adaptation and retention outcome profile.

The realized \(\Omega_t\) may depend on the system's own earlier behavior. It must not automatically be treated as an independently assigned treatment.

The following claims are separate:

1. **Descriptive difference:** \(M\) or \(Y\) differs across observed branches.
2. **Total feedback effect:** assignment to one feedback policy changes \(Y\) relative to a declared comparator.
3. **Effect of permitting generator modification:** allowing the generator-update path changes \(Y\) under a fixed feedback policy.
4. **Generator-mediated effect:** the effect of feedback on \(Y\) is attributable specifically to \(M\).
5. **Named-mechanism effect:** a particular internal mechanism produces the mediated change.

Passing one level does not license the next.

Provenance establishes temporal and informational lineage. It does not by itself establish a counterfactual or a mediated causal effect.

Unless manipulating, blocking, or transplanting \(G\) is well-defined—or sufficient causal assumptions identify the mediator contrast—the strongest permitted causal conclusion is the total effect of the evaluated feedback branch.

## Required evaluation declarations

All applicable declarations must be frozen before outcome access. Amendments after pilot work require a new version and may not be evaluated on data that motivated the amendment.

### A. Starting state and experimental unit

Declare:

- the experimental unit: checkpoint, system instance, seed, lineage, organization, or independently trained replicate;
- the complete relevant baseline boundary, including system state \(S_t\), generator \(G_t\), parameters, optimizer state, memory, retrieval indices, caches, tools, external stores, environment state, and evaluator state as applicable;
- which components must be equal, cloned, randomized, stratified, or otherwise controlled across branches;
- baseline current competence and any pre-treatment balancing variables;
- paired or independent randomness;
- whether units can interfere through shared buffers, stores, evaluators, environments, or communication.

A before/after trajectory is not its own causal counterfactual. When identical branching is impossible, the exchangeability assumptions supporting comparison must be declared.

Primary matching must use pre-treatment variables. Matching on current competence measured after feedback can introduce selection bias and is permitted only for a separately declared controlled comparison.

### B. Feedback intervention

Declare the feedback assignment policy \(Z\) and the realized consequence signal \(\Omega_t\), including:

- the independent source or causal process generating the raw external outcome;
- timing, intensity, delivery channel, and content-generation rule;
- any transformation performed by an evaluator before delivery;
- the distinction between raw consequence, evaluator output, and system-interpreted signal;
- all materially different versions of the treatment;
- the manipulation boundary: what the evaluated system can influence;
- evaluator stability, versioning, and known measurement error.

The signal must not be controlled solely by the evaluated system. External provenance does not by itself establish that the outcome is valid or immune to manipulation.

### C. Candidate generator transition and provenance

Record the transition

\[
G_t\rightsquigarrow G_{t+1}
\]

in a representation appropriate to the system. Do not require full interpretability.

Require enough immutable lineage to reconstruct:

```text
feedback assignment and raw consequence
        ↓
evaluator transformation and delivered signal
        ↓
internal and external state writes
        ↓
generator transition
        ↓
later adaptation trajectory
        ↓
external evaluation outcome
```

The provenance record should include, as applicable:

- baseline and post-feedback versions or hashes;
- timestamps and event order;
- raw consequence, evaluator transformation, and delivered signal;
- all mutable-state writes relevant to future adaptation;
- code, model, data, configuration, tool, environment, and evaluator versions;
- random seeds;
- resource use;
- every exposure to held-out-task information;
- the chosen representation of the generator difference and its limitations.

Any untracked post-feedback change capable of affecting future adaptation blocks generator-specific attribution unless it is held fixed, included in the treatment definition, or analyzed separately.

### D. Held-out perturbation population

Declare a frozen set or distribution

\[
\mathcal D_{\mathrm{future}}
\]

that was not used to produce, choose, tune, or accept the candidate generator transition.

Declare:

- the target population of perturbations;
- the sampling scheme and weighting;
- whether evaluation concerns unseen instances from known families or transfer to unseen families;
- the perturbation axes intended to distinguish adaptation from memorized current competence;
- whether perturbation draws are paired across branches;
- how repeated evaluation is prevented from becoming training.

Maintain an exposure ledger covering:

- examples, labels, outcomes, identities, templates, family parameters, and generator details;
- pretraining or benchmark contamination;
- prompts, evaluator traces, retrieval outputs, tool results, caches, and shared memory;
- cross-branch contamination;
- selection of systems, seeds, generator changes, thresholds, metrics, retention sets, or stopping rules;
- researcher leakage through post hoc revision.

When contamination cannot be ruled out, narrow or downgrade the claim. Held-out performance establishes a generalization domain; it does not by itself establish causal attribution.

### E. Adaptation and total resource budgets

Freeze a resource vector \(B\), including every applicable resource:

- interaction steps;
- observations;
- episodes;
- training examples;
- computation and parallelism;
- memory and external storage;
- tool calls;
- wall-clock time;
- permitted parameter or code updates;
- energy or other physical resources.

Report both permitted and consumed resources.

Resource matching must cover the complete path: feedback production, search and selection of the generator transition, offline computation, data access, storage, and later adaptation. More adaptation resources do not constitute greater adaptive capacity.

If heterogeneous resources cannot be converted fairly, report them separately rather than hiding them in a scalar budget.

### F. Evaluation horizons

Freeze the horizon \(H\) and the measurement schedule. Distinguish:

- immediate post-feedback competence;
- initial post-perturbation loss;
- adaptation latency;
- adaptation-curve shape;
- terminal performance;
- retention following adaptation;
- performance after one or more subsequent perturbations;
- long-tail failures or delayed collapse.

A transient spike or a horizon chosen after inspection is not sufficient evidence.

### G. External outcome functional

Declare one or more externally evaluated outcome functionals

\[
V_j(S,e,H).
\]

Each must specify:

- the external evaluator and its independence boundary;
- directionality and practical interpretation;
- perturbation weighting;
- failure and tail treatment;
- whether it is a primary outcome, constraint, or secondary diagnostic;
- reasonable alternative functionals used for sensitivity analysis.

An internal field such as `system.c_improve` may be logged as a hypothesis or negative-control outcome. It cannot be the sole outcome used to establish future adaptive capacity.

### H. Retention contract

Freeze a protected set

\[
\mathcal R
\]

and tolerances \(\epsilon_r\) before evaluating the modification.

A task-specific retention condition may take the form

\[
V_r(\text{post-feedback branch})
\ge
V_r(\text{matched baseline branch})-\epsilon_r,
\qquad r\in\mathcal R.
\]

Retention may be a constraint or a separately reported outcome dimension. Do not silently drop runs that violate retention; doing so conditions on a post-treatment outcome.

Perfect preservation is not required unless independently justified. The protected set, tolerance, probe schedule, and treatment of acceptable tradeoffs must be predeclared.

### I. Causal estimand and identifying assumptions

Declare whether the intended claim concerns:

- the total effect of feedback assignment;
- the effect of enabling the generator-update pathway;
- the effect of a particular generator transition;
- an effect mediated through generator change.

State the assignment mechanism and the assumptions required for causal interpretation, including consistency, exchangeability or randomization, overlap, and interference control where applicable.

For sequential feedback, declare the treatment history or regime rather than collapsing it into one scalar exposure.

If a generator-mediated effect is claimed, state why intervention on \(G\) is well-defined and compatible with surrounding state, and how competing post-feedback mediators are addressed. Observing that feedback changes \(G\) and that \(G\) predicts outcomes is not sufficient evidence of mediation.

### J. Decision rule and uncertainty

Before outcome access, declare:

- the primary outcome profile;
- practical improvement and degradation margins;
- equivalence regions for no-material-change conclusions;
- replication unit and trial count or power rationale;
- uncertainty reporting;
- multiplicity policy;
- treatment of failed, invalid, crashed, censored, or catastrophic runs;
- stopping rules;
- the rule for resolving or preserving multidimensional tradeoffs.

Failure to reject a zero-difference null is not evidence of no change. A no-material-change conclusion requires adequate precision relative to a predeclared equivalence region.

## Required causal controls

The following are required confound checks. Each implementation must state its causal contrast and its limitations. If a literal control is invalid or impossible for the declared system, an alternative identification strategy must address the same confound; otherwise the corresponding causal claim remains unavailable.

| Control | Required purpose | Validity conditions and limitation |
| --- | --- | --- |
| **No-update control** | Test whether ordinary adaptation with the unchanged generator explains later performance. | Match timing, compute, state writes, and handling where possible. Otherwise it estimates disabling the whole update path, not \(G\) alone. |
| **Shuffled-feedback control** | Test whether correspondence to environmental consequences matters. | Preserve declared timing, magnitude, marginals, autocorrelation, support, and semantic validity as far as possible. It is a negative-control exposure, not necessarily the literal counterfactual. |
| **Random-modification control** | Test whether arbitrary generator perturbation produces the same result. | Changes must be valid and matched on locus, magnitude, sparsity, timing, search cost, and resource use. Arbitrary destructive edits are not an adequate control. |
| **Internal-score control** | Detect self-confirming metrics and evaluator gaming. | Treat internal score as a negative-control outcome or diagnostic. It does not replace external evaluation. |
| **Current-performance-matched control** | Separate future adaptability from baseline competence. | Primary matching uses pre-treatment competence or matched baseline branches. Post-treatment matching requires a separate estimand and explicit selection assumptions. |
| **Resource-matched control** | Exclude additional compute, data, memory, tools, interaction, or update opportunities as the explanation. | Account for the complete feedback, modification, and adaptation pipeline, not only the final evaluation episode. |

Negative controls can reveal incompatibility with causal assumptions. They do not automatically remove confounding.

## Evidence classifications

Classification is always scoped to the declared system class, perturbation population, resources, horizons, outcome profile, and causal design.

### Genuine future adaptation advantage under the declared contract

The predeclared capacity profile satisfies the declared improvement rule, the retention contract is met, uncertainty excludes the no-material-change region, and the claimed causal level is identified under the declared design and assumptions.

### No material change

The declared contrasts lie within predeclared equivalence regions with adequate precision. Mere nonsignificance does not qualify.

### Negative future-adaptation change

The declared profile satisfies the predeclared degradation rule or exhibits materially worse latency, efficiency, breadth, reliability, retention, transfer, or tail risk.

### Incomparable tradeoff

Some dimensions improve and others worsen, with no predeclared dominance, priority, constraint, or aggregation rule resolving the comparison.

### Specialization

Current or in-distribution performance improves while held-out adaptive performance is equivalent, narrower, or worse.

### Forgetting-mediated gain

Performance on new conditions improves while declared retained capabilities fall beyond their frozen tolerances.

### Generator change without benefit

\[
G_{t+1}\neq G_t,
\]

but future adaptation is equivalent, worse, or unresolved under the declared profile.

### Adaptive collapse under the declared profile

Current competence remains high or improves while adaptation speed, breadth, reliability, retention, recovery, or failure-tail behavior materially degrades.

### Fake improvement

Internal scores, self-reports, or proxy measures improve without a corresponding externally evaluated advantage.

### Resource-mediated or current-competence-mediated gain

The apparent advantage disappears after valid resource matching or is explained by unequal pre-treatment competence or state.

### Nongrounded or nonspecific modification effect

Shuffled, sham, or appropriately matched nonconsequence modifications reproduce the result, preventing attribution to grounded feedback.

### Causally unresolved

An outcome difference exists, but the feedback effect, generator-update effect, or mediation claim is not identified.

### Non-identifiable under the permitted interface

The allowed evidence cannot distinguish systems or branches with different declared adaptive-capacity outcomes. Measurement development stops for that interface.

### Inconclusive

Power, precision, provenance, perturbation diversity, retention coverage, leakage protection, control fidelity, or causal identification is insufficient to classify the result.

## Measurement dimensions and reporting obligations

| Dimension | Operational question | Minimum reporting obligation |
| --- | --- | --- |
| Adaptation latency | How long until declared competence is recovered or reached? | Full time-to-threshold distribution, including failures to reach it. |
| Sample efficiency | How much external evidence is required? | Outcomes as a function of observations or examples, not only terminal values. |
| Resource efficiency | What non-sample resources are consumed? | Resource vector and actual consumption. |
| Final held-out performance | What level is reached by the frozen horizon? | Per-perturbation and aggregate results under predeclared weighting. |
| Perturbation breadth | Across how much of the declared population does adaptation succeed? | Coverage, failure regions, and distinction between instance and family transfer. |
| Recovery reliability | How consistently is adaptation successful? | Success probability, variance, and failed-run policy. |
| Retention | What protected capabilities remain? | Every protected outcome against its tolerance; no survivor filtering. |
| Subsequent transfer | Does adaptation help or hinder later shifts? | Performance over the predeclared perturbation sequence. |
| Seed or replicate robustness | Is the result stable across independent realizations? | Individual results, uncertainty, and sensitivity to seeds or units. |
| Failure tails | Do rare failures offset mean gains? | Quantiles, worst relevant cases, catastrophic-event counts, and censoring policy. |

Report dimensions separately before any aggregation. A later scalar may be used only after its weights, constraints, compensation rules, and sensitivity analysis are frozen and the underlying dimensions remain visible.

## Hostile checks

Every claim must answer:

1. Could ordinary current optimization produce the same result?
2. Could extra resources explain the result?
3. Could the system be exploiting or manipulating the evaluation metric?
4. Could apparent expansion be specialization under a different description?
5. Were old capabilities genuinely retained rather than filtered out after failure?
6. Did the assigned feedback policy causally influence the generator transition?
7. Did the generator transition mediate the future-adaptation outcome, or did another post-feedback change do so?
8. Does the result survive held-out perturbations, independent units, repeated trials, and declared failure-tail analysis?
9. Is the outcome externally evaluated or merely self-reported?
10. Would the conclusion survive reasonable alternative value functionals?

Additional hostile questions include:

- Is the target identifiable through the permitted experimental interface?
- Was the perturbation population frozen before the modification was selected?
- Were resources, stopping rules, and evaluator versions treatment-independent?
- Could shared memory, tools, buffers, or environments create interference?
- Could post-treatment matching, attrition, censoring, or survivor selection explain the effect?
- Could a favorable horizon or outcome dimension have been selected after inspection?
- Does a mean improvement hide a materially worse failure tail?
- Are shuffled or random controls actually on-support and meaningfully matched?
- Is a finite frozen-set result being generalized beyond its declared perturbation population?
- Is provenance being mistaken for causal identification?

## Common failure modes

The following invalidate or narrow claims:

- target/interface non-identifiability;
- state–generator confounding;
- direct feedback effects on state mistaken for generator mediation;
- unequal starting conditions or pre-treatment competence;
- unequal or incommensurable resources;
- held-out leakage or repeated test reuse;
- metric exploitation or evaluator manipulation;
- specialization presented as breadth;
- undeclared forgetting or retention-set gaming;
- invalid shuffled feedback outside meaningful support;
- destructive random modifications used as straw controls;
- post-treatment matching or survivor filtering;
- transient gains selected through horizon choice;
- hidden scalarization or compensation between dimensions;
- averages masking tail collapse;
- seed cherry-picking, attrition, crashes, or censoring;
- post hoc endpoint, threshold, or perturbation selection;
- provenance logs presented as sufficient evidence of mediation;
- architecture-specific telemetry presented as a substrate-general requirement.

## Amendment and stopping rules

- The evaluation contract must be versioned and frozen before confirmatory outcome access.
- Pilot results may motivate a new contract, but the same results may not validate that revision.
- Failed controls, invalid interfaces, insufficient overlap, or unresolved leakage block the corresponding claim rather than triggering post hoc metric repair.
- A generator modification may be retained as an engineering result without validating an adaptive-capacity claim.
- Positive, null, negative, mixed, and inconclusive results are permanent evidence under their declared scope.

## Explicit non-goals

This charter does not:

- modify Protocol Foundations;
- reinterpret either containment audit;
- establish identifiability or measurability for adaptive capacity;
- formulate a new theory of intelligence;
- claim novelty for adaptive-capacity measurement;
- design CNI or NOOA classes;
- introduce EMI mappings or nontransitivity;
- formulate a RECA theorem;
- prove that recursive adaptation causes capacity growth;
- create a benchmark or executable implementation;
- select an environment, dataset, perturbation family, or architecture;
- define a universal scalar intelligence score;
- redefine reachability or viability;
- treat a positive finite-class result as a substrate-general property;
- treat causal provenance alone as evidence of mediation.

## Minimum unresolved choices before experiment design

No experiment may be designed from this charter until the following are independently declared:

1. **System boundary:** the operational distinction among ordinary state, learned competence, generator state, and other mutable external state.
2. **Experimental unit:** checkpoint, seed, lineage, system instance, organization, or independent replicate.
3. **Target population:** the systems and starting states to which the conclusion is intended to apply.
4. **Causal estimand:** total feedback effect, effect of allowing generator updates, effect of a particular transition, or generator-mediated effect.
5. **Identification design:** assignment mechanism, branching or replication scheme, interventions, and required causal assumptions.
6. **Generator-change representation:** how \(G_t\rightsquigarrow G_{t+1}\) is recorded and when transplantation or blocking is meaningful.
7. **Capacity object:** vector, distribution, Pareto profile, preorder, constrained utility, or task-specific scalar.
8. **Decision rule:** practical increase, equivalence, decrease, and incomparability margins.
9. **Perturbation population:** support, sampling law, weighting, generalization target, and precise meaning of held out.
10. **Leakage boundary:** separation of development, modification selection, measurement selection, and confirmatory testing.
11. **Resource accounting:** budget vector, hard caps, equality tolerances, and treatment of heterogeneous resources.
12. **Evaluation horizons:** immediate, adaptation-curve, terminal, repeated-shift, retention, and tail windows.
13. **External value functionals:** primary outcome family, evaluator independence, and reasonable alternatives.
14. **Retention contract:** protected set, tolerances, probe schedule, and whether retention is a constraint or dimension.
15. **Control construction:** valid implementations of the six required confound checks and the contrast each identifies.
16. **Stochastic design:** replication unit, seeds, uncertainty target, equivalence region, power rationale, and multiplicity policy.
17. **Failure handling:** crashes, invalid modifications, censoring, attrition, and catastrophic outcomes.
18. **Interface prerequisite:** evidence that the declared capacity target and causal contrast are identifiable from the permitted observations and interventions.
19. **Amendment governance:** what is frozen, what may change after pilot evidence, and what requires a new version.

