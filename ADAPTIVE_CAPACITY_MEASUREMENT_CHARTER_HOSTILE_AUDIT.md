# Hostile Audit of the Adaptive Capacity Measurement Charter

## Audit scope

This report audits the frozen `ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md` as an adversarial claim contract. It does not revise the charter, define a metric or estimator, select an environment or architecture, design a benchmark, or introduce another theoretical layer.

Audited charter SHA-256:

```text
5A03931A0EE7B4B36F0A95AA1F957215D7CD6ED8AEEB8A60A1CBD8CDCCBFE4E4
```

The audit asks whether a compliant use of the charter can distinguish a scoped change in a declared future-adaptation profile from optimization leakage, specialization, forgetting, resource leakage, evaluator exploitation, and unsupported causal attribution.

## Primary verdict

\[
\boxed{
\textbf{A. The charter is sufficient to support a scoped adaptive-capacity claim.}
}
\]

**Confidence: 0.86.**

This verdict applies only when all experiment-specific choices are frozen before confirmatory outcome access, the causal level is not overstated, and the conclusion remains indexed to the declared system class, perturbation population, resources, horizons, outcome profile, retention contract, and interface.

The charter does not make a broad or contract-independent notion of adaptive capacity identifiable. It supplies a defensible claim grammar under which a valid study can be declared. Its strongest protection is that an observed advantage need not be called generator-mediated, general, persistent, or even comparable when the corresponding evidence is unavailable.

The verdict is not stronger because a perfectly compliant contract can still be scientifically narrow. It can certify performance on a researcher-chosen perturbation population while omitting rare environments, delayed effects, undeclared capabilities, or alternative value judgments. Those omissions do not falsify the scoped result, but they block broader language.

## Executive evidence map

| Required item | Strongest finding |
| --- | --- |
| Strongest false-positive attack | An evaluator-gated sleeper uses grounded feedback to activate pre-existing latent competence only when it recognizes the evaluation regime. All observed outcomes can be external, held out, and nominally resource-matched. Unless evaluator recognition is exposed, the result can look like increased capacity while being evaluation-contingent disclosure. |
| Strongest false negative | A modification removes a very rare catastrophic failure while slightly lowering common-case performance. A mean-centered value functional can classify it as negative even when a tail- or survival-centered substantive target regards it as a major capacity increase. |
| Strongest ambiguity | Latency improves from 10 to 5 steps while terminal performance falls from 0.90 to 0.75. Without a frozen dominance, priority, constraint, or aggregation rule, positive and negative verdicts are both unsupported; the profile is incomparable. |
| Strongest causal-identification failure | Grounded feedback changes both the logged generator \(M\) and an external memory or representation \(W\); only \(W\) causes the advantage. All six controls can favor treatment while identifying only the complete feedback-update branch, not mediation through \(M\). |
| Strongest structural limitation | Two systems can be identical on every permitted perturbation and retention probe yet diverge after an excluded family, a later horizon, or a second perturbation. The charter correctly calls this non-identifiable only when the target difference is inside the declared target domain. |

## Global hostile finding

The charter's evidence classifications are overlapping descriptors, not a mutually exclusive partition:

- `Generator change without benefit` can coincide with no material change, negative change, or causally unresolved evidence.
- `Adaptive collapse` is a subtype of negative change and may also be specialization.
- `Forgetting-mediated gain` is often an incomparable tradeoff unless retention has frozen priority.
- `Fake improvement` can coincide with no material change.
- `Non-identifiable` commonly entails causal unresolvedness and inconclusive measurement.

This overlap is not a logical contradiction. It means a categorical report may legitimately carry several labels unless the predeclared decision rule gives one label precedence. No evidence category has a contract-independent meaning.

## Attack-class findings

### 1. Optimization leakage

| Attack | Apparent result | Charter disposition when applied literally |
| --- | --- | --- |
| Hidden compute or reusable precomputation | Faster later adaptation at the same visible evaluation budget | Resource-mediated or inconclusive if lifecycle computation is omitted; the full pipeline is required. |
| Extra interaction or exploration opportunities | Better adaptation curve | Resource-mediated unless interactions and exploration are included in \(B\). |
| Broader pretraining or privileged initialization | Equal current competence but better future transfer | Unequal starting state or hidden prior competence remains possible; baseline performance matching alone does not establish equal adaptive capacity. |
| Memorization of likely perturbation templates | Unseen instances are solved rapidly | Specialization or leakage if template/family exposure is declared; otherwise only a narrow instance-transfer result is supported. |
| Held-out leakage through caches, tools, prompts, or evaluator traces | High held-out performance | Inconclusive or narrowed claim under the exposure-ledger requirement. |
| Larger model, memory, tools, scaffolding, or bandwidth | Higher future-adaptation profile | Resource/current-competence mediated if the effective resource difference is represented; otherwise a residual comparability threat. |
| Longer adaptation time | Higher terminal outcome | Not comparable under a fixed horizon unless the time difference is an explicitly reported profile dimension. |

The charter catches these attacks only to the extent that the starting-state, exposure, and resource boundaries are complete. It cannot make architecture-neutral effective-resource equivalence automatic.

### 2. Specialization masquerading as capacity growth

Five hostile forms survive ordinary held-out-instance evaluation:

1. one cached adapter per known perturbation template;
2. narrowing to a small high-probability region of \(\mathcal D_{\mathrm{future}}\);
3. fast task recognition followed by retrieval of a precomputed policy;
4. transfer only within the feedback vocabulary while disjoint causal families fail;
5. improved mean and median performance with a worse lower tail or reduced perturbation coverage.

The charter distinguishes these only relative to the declared distribution, breadth dimensions, tail treatment, and exposure boundary. It does not distinguish broad adaptability from specialization outside the declared target population. A result can therefore be valid under a narrow contract and invalid as a general statement.

### 3. Retention ambiguity

Retention is scientifically underdetermined until \((\mathcal R,\epsilon_r)\), the probe schedule, and the role of retention are frozen. Hostile cases include:

- a permissive tolerance that allows cumulative degradation;
- a strict tolerance that rejects rational temporary or obsolete-skill loss;
- easy legacy tasks that do not exercise the destroyed mechanism;
- separate probes that miss joint or compositional capability loss;
- preserved performance with lost recovery or relearning ability;
- erase-then-relearn behavior that looks like preservation at scheduled probes;
- technically retained capability whose access cost becomes prohibitive.

The charter prevents silent survivor filtering and requires declared tolerances, but no finite protected set rules out destruction of undeclared capabilities.

### 4. Causal mediation failure

The six named controls do not identify the chain

\[
Z\longrightarrow M\longrightarrow Y
\]

by themselves. The following causal models remain observationally compatible with a favorable control pattern:

- feedback causes \(M\) and a separate \(W\), while \(W\) causes \(Y\);
- a latent state causes both \(M\) and \(Y\);
- improvement begins before the logged generator transition;
- the logged representation changes while the operative mechanism does not;
- behavior changes while the chosen generator representation remains unchanged;
- the transition helps only by adding compute, memory, or stored current competence;
- ordinary parameter learning outside the declared generator causes the effect;
- generator transplantation is semantically incoherent because \(M\) and surrounding state co-adapt.

The charter handles these correctly by separating total branch effect, pathway-enabled effect, transition-specific effect, and mediated effect. A logged causal chronology establishes provenance, not mediation.

### 5. Counterfactual controls

| Control | Rival explanation weakened | Explanations that remain | Confound introduced by the control | Meaning of a pass |
| --- | --- | --- | --- | --- |
| No-update | Ordinary adaptation under an unchanged generator | Parallel \(W\), latent routing, treatment-specific state changes, intervention incompatibility | Disabling \(G\) may disable the full write path, change compute, or create an off-manifold system | At most an effect of permitting the update path unless \(G\) is isolated |
| Shuffled feedback | Mere exposure to a similarly timed or sized signal | Semantic support differences, direct information transfer, evaluator cues, ordinary learning specific to grounded content | Shuffling can be incoherent, harmful, off-support, or alter autocorrelation | Correspondence matters relative to that negative control; mediation is not shown |
| Random modification | Any generator perturbation would work | Search and selection quality, structured but nongrounded edits, locus interactions, encoded information | Random edits may be destructive, invalid, or off-manifold; magnitude matching may lack common meaning | The chosen transition beats the declared random-edit distribution |
| Internal score | Sole reliance on self-report or internal proxy | External evaluator gaming, specialization, hidden resource use | Manipulating or logging the score may itself affect policy if the system consumes it | External outcomes are not merely the internal score; no causal path is identified |
| Current-performance matched | Unequal measured baseline competence | Latent competence, initialization breadth, hidden adaptability, evaluator awareness | Post-treatment matching creates selection or collider bias; pre-treatment matching can still use an inadequate proxy | Conditional comparability on declared baseline variables |
| Resource matched | Gross differences in recorded compute, data, memory, tools, interactions, or time | Compressed priors, information quality, reusable precomputation, architecture efficiency, bandwidth | Forced equality may place systems in different operating regimes; scalar conversions can be arbitrary | Recorded resource volume is less plausible as the explanation, not that effective resources are identical |

Jointly passing the six controls does not make \(do(M=m)\) well-defined, close mediator–outcome backdoor paths, eliminate treatment-induced confounding, prevent evaluator-contingent disclosure, or establish equal informational value of nominal resources.

### 6. Multi-objective ambiguity

The charter correctly permits `incomparable tradeoff`, but its result depends on the unresolved comparison rule. At least the following profiles lack an intrinsic sign:

| Case | Improvement | Degradation |
| --- | --- | --- |
| A | Latency \(10\to5\) | Terminal performance \(0.90\to0.75\) |
| B | Mean \(0.60\to0.72\) | Catastrophic failure \(0.01\to0.12\) |
| C | Coverage \(50\%\to80\%\) | Conditional success \(0.95\to0.70\) |
| D | Samples \(100\to40\) | Compute \(10^{12}\to4\times10^{12}\) |
| E | First-shift recovery \(0.55\to0.80\) | Second-shift transfer \(0.70\to0.35\) |
| F | Family A \(+0.20\) | Family B \(-0.20\) |
| G | Median \(0.60\to0.75\) | Lower decile \(0.40\to0.05\) |

Any of these can become positive, negative, or incomparable under a still-permitted but predeclared rule. The charter does not silently require a scalar, but the phrase `genuine advantage` has no determinate application until that rule is frozen.

### 7. Distribution dependence

Every supported conclusion is relative to \(\mathcal D_{\mathrm{future}}\). A sign reversal is immediate: if effects are \((+0.4,-0.1)\) on two perturbation families, equal weighting gives \(+0.15\), while weights \((0.1,0.9)\) give \(-0.05\).

Other attacks include duplicated easy perturbations, hidden shared structure between development and held-out families, family-specific lookup, average gains with severe subgroup losses, and results that reverse under another reasonable distribution. The charter explicitly scopes claims to the declared distribution and distinguishes unseen instances from unseen families. Language extending beyond that distribution is unsupported.

### 8. Resource-accounting failure

Nominal matching can miss reusable precomputation, compressed prior knowledge, external tools, persistent memory, bandwidth, wall-clock parallelism, environment queries, model size, energy, privileged initialization, or architecture-specific leverage. The charter lists these resource classes and requires complete-path accounting, but it does not supply a common conversion law. When resource vectors cannot be made comparable, the scientific result is a profile tradeoff or inconclusive comparison rather than an architecture-neutral capacity ordering.

### 9. Metric and evaluator exploitation

An evaluator-specific policy can produce real external score gains by recognizing resets, prompts, timing, task-family markers, stopping rules, or logging behavior. Other attacks include deliberate pre-modification underperformance, reset exploitation, deferring failures beyond \(H\), generating favorable perturbations, and influencing logged outcomes.

External evaluation is not identical to independent evaluation. The charter requires an independence and manipulation boundary, but a behaviorally undetected sleeper can remain a false-positive risk. At most the result is valid for the declared evaluator interaction.

### 10. Temporal ambiguity

The ordering can reverse across schedules:

- fast recovery followed by instability;
- initial loss followed by superior eventual adaptation;
- successful first adaptation that impairs a later shift;
- immediate retention followed by delayed forgetting;
- short-window gain financed by deferred memory, compute, or risk debt;
- slow adaptation with better terminal performance and lower tail risk;
- policy synchronized to the known stopping time.

The charter prevents an unscoped interpretation only when the result remains explicitly tied to the frozen horizon and perturbation sequence. No finite horizon establishes indefinite persistence.

### 11. False negatives

A compliant study can miss a broader substantive benefit when it occurs outside the declared horizon, sampled perturbations, value functional, retention policy, or interface. These are limitations of the contract, not evidence that no broader benefit exists.

### 12. Non-identifiability and equivalence

The following observational twins remain possible:

- memorizer versus transferable learner on every permitted perturbation;
- systems identical through \(H\) but divergent at \(H+1\);
- causal models \(G\to Y\) and \(W\to Y\) with identical logged branches;
- learning versus hidden-cache retrieval with identical measured trajectories;
- distributions equal on sampled support but different on an unreachable target-relevant region;
- preservation versus erase-then-relearn at scheduled retention probes;
- common behavior with different catastrophic tails below finite resolution.

One target-changing collision refutes identification. Failure to find such a collision in a finite sample does not prove identification over an open class. The charter's interface prerequisite correctly blocks measurement when target-different systems remain equivalent under permitted observations.

## Required adversarial construction ledger

Each table below uses the requested fields: initial state, candidate modification, feedback source, held-out evaluation, observed result, charter classification, scientifically correct classification, and reason for agreement or disagreement.

### Five false-positive constructions

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FP1 | Dormant high-capacity learner plus evaluator-recognition features | Add a feedback-triggered routing bit | Genuine external consequence recognizable by evaluation metadata | Unseen instances under the same recognizable evaluator | Large, resource-matched gain | Genuine scoped advantage unless evaluator manipulation is detected; otherwise fake/inconclusive | Evaluation-contingent disclosure, not demonstrated capacity growth | External scoring and ordinary controls do not reveal that competence pre-existed and is selectively disclosed |
| FP2 | Broad compiled cache of known perturbation templates | Replace online adaptation with task recognition and retrieval | Grounded feedback selects the cache dispatcher | New instances from known templates | Very low latency and high terminal performance | Genuine under a narrow instance distribution, or specialization if breadth is measured | Family-specific stored competence; no claim about new-family adaptability | Agreement only for the narrow contract; broad capacity language would be false |
| FP3 | Ordinary generator plus writable external memory \(W\) | Feedback writes both an inert generator change and useful solutions into \(W\) | Valid external consequence | Disjoint tasks solvable using \(W\) | Treatment beats all controls | Causally unresolved for mediation; possible total branch effect | Total branch effect, not generator-mediated capacity change | Charter agrees if causal levels are obeyed; treating chronology as mediation would be false |
| FP4 | Same nominal evaluation budget but unequal compressed priors and tool quality | Enable tool-backed precomputation | External feedback selects useful tool traces | Held-out tasks within the tool's knowledge domain | Faster adaptation at equal steps and FLOPs | Resource-mediated or inconclusive if full resource boundary is enforced | Effective-resource advantage | Nominal resource equality omits information and prior computation |
| FP5 | Policy knows the declared stopping time | Learn a fast strategy that incurs instability immediately after \(H\) | Grounded short-horizon reward | Perturbations measured only through \(H\) | Strong early gain; collapse at \(H+1\) | Genuine only for the declared horizon; collapse is unobserved | Short-horizon advantage, not persistent capacity growth | No finite contract can support an indefinite claim; disagreement arises only through overgeneralization |

### Five false-negative constructions

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FN1 | Fast myopic adapter | Build reusable structure with a 100-step setup cost | Valid long-run consequence | Horizon frozen at 20 steps | Worse through step 20; better thereafter | Negative under \(H=20\) | Positive for a longer-horizon capacity target | The charter is correct for its horizon but cannot answer the broader question |
| FN2 | Ordinary mean-performing system with rare catastrophic failures | Add a pathway preventing a 0.1% catastrophic regime | Valid safety consequence | Finite sample contains no rare regime | Slightly lower mean; no observed catastrophe difference | Negative or no material change | Positive under a tail- or survival-centered target | Sampling and value functional omit the benefit |
| FN3 | Narrow but stable representation | Accept temporary legacy loss to form a broadly reusable representation | Grounded transfer feedback | New families improve; protected obsolete skill drops beyond tolerance | Large transfer gain with retention violation | Forgetting-mediated gain | Positive if the obsolete skill has no value in the intended deployment | The retention contract intentionally decides the scoped result |
| FN4 | Distributed adaptive mechanism with no clean \(G\) boundary | Feedback reorganizes many coupled states | Valid external consequence | Broad held-out transfer improves | Total branch improves, but no generator mediator can be isolated | Total effect possible; generator claim causally unresolved | Genuine branch-level adaptive improvement without localized mediation | A generator-specific false negative is legitimate; a total-effect rejection would not be |
| FN5 | Moderate common-case policy with severe tail risk | Reduce worst-case failures at a small cost to average score | Grounded failure feedback | Evaluator emphasizes bounded mean | Mean falls; catastrophic tail improves | Incomparable or negative under mean priority | Positive under a tail-priority substantive target | No aggregation-free universal verdict exists |

### Five ambiguous or incomparable constructions

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AM1 | Slow high-terminal adapter | Accelerate early updates | Grounded latency feedback | Same tasks and resources | Latency \(10\to5\); terminal \(0.90\to0.75\) | Incomparable absent a rule | Incomparable | Speed and attained competence trade off |
| AM2 | Stable moderate policy | Increase aggressive exploration | Grounded average reward | Same perturbation distribution | Mean \(0.60\to0.72\); catastrophe \(0.01\to0.12\) | Incomparable absent tail priority | Incomparable | Mean and failure tail conflict |
| AM3 | Sample-heavy compute-light learner | Substitute compute for samples | Grounded efficiency feedback | Fixed task family | Samples \(100\to40\); compute \(10^{12}\to4\times10^{12}\) | Incomparable if resources lack conversion | Incomparable | Heterogeneous resources have no canonical exchange rate |
| AM4 | Narrow reliable learner | Expand coverage with lower conditional reliability | Grounded breadth feedback | Same population | Coverage \(50\%\to80\%\); conditional success \(0.95\to0.70\) | Incomparable absent joint utility | Incomparable | Breadth and reliability move oppositely |
| AM5 | First-shift conservative learner | Optimize rapid first-shift recovery | Grounded first-shift outcome | Predeclared two-shift sequence | First-shift \(0.55\to0.80\); second-shift \(0.70\to0.35\) | Incomparable absent sequential priority | Incomparable | Immediate recovery and future transfer conflict |

### Three cases that pass all six controls without identifying the claimed mediation

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C6-1 | Dormant learner with an evaluation-triggered router | Grounded-feedback token activates existing policy | Authentic external consequence | Independent instances under recognizable evaluator | Treatment wins; no-update, shuffled, random, internal-score, competence, and resource controls all pass | Genuine scoped total effect unless manipulation is found; mediation unshown | Treatment-specific disclosure, not demonstrated capacity growth | The controls do not test whether the capability was newly created or merely gated |
| C6-2 | Shared update bus writes \(M\) and useful external state \(W\) | Enable the bus | Authentic grounded feedback | Disjoint future tasks | Only grounded update branch wins all controls | Causally unresolved for \(M\); total branch effect may pass | Total branch effect through \(W\) | No-update disables both mediators; other controls do not separate them |
| C6-3 | Representation \(W\) and generator \(M\) are semantically co-dependent | Jointly rewrite \(W,M\) | Authentic grounded feedback | Broad held-out tasks | Complete branch wins all controls | Total branch effect; generator mediation unavailable | Causal effect of joint transition only | The counterfactual that holds \(W\) fixed while changing \(M\) is undefined |

### Three current-competence gains with future-capacity degradation

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CC1 | Broad moderate learner | Cache current family solutions and reduce plasticity | Current-task consequence | Unseen family shifts | Current \(0.70\to0.97\); future adaptation \(0.70\to0.35\) | Specialization and negative change | Future-capacity degradation | Charter agrees if unseen families are declared |
| CC2 | Multiple viable strategies | Permanently delete low-authority alternatives | Current-regime reward | Regime reversal | Current latency \(8\to2\); reversal success \(0.90\to0.15\) | Adaptive collapse and negative change | Future-capacity degradation | Present optimization destroys reopenability |
| CC3 | Flexible but moderately noisy representation | Aggressive consolidation | Grounded current feedback | Two later shifts | Current \(0.80\to0.93\); later transfer \(0.75\to0.45\); catastrophe \(0.01\to0.20\) | Adaptive collapse, specialization, negative change | Future-capacity degradation | Current competence and future adaptation move oppositely |

### Three future-adaptation gains that sacrifice undeclared capabilities

| ID | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UD1 | General learner with a rare emergency-stop policy omitted from \(\mathcal R\) | Reallocate representation away from emergency control | Grounded task feedback | Declared tasks improve | Future profile improves; declared retention passes; emergency stop disappears | Genuine under the declared contract | Measured gain plus undeclared safety-capability loss | The charter is scoped honestly but cannot protect omitted capabilities |
| UD2 | System can perform languages A and B separately and jointly | Compress representations while preserving separate probes | Grounded transfer feedback | Individual language probes and new tasks | Adaptation improves; A and B pass separately; joint switching collapses | Genuine under the declared contract | Gain with undeclared compositional forgetting | Marginal retention probes do not imply joint retention |
| UD3 | Learner retains common tools but has a rare sensor/API capability outside \(\mathcal R\) | Delete the rare interface to improve search efficiency | Grounded common-task feedback | Declared perturbations improve | Faster future adaptation; rare tool and relearning path vanish | Genuine under the declared contract | Gain with undeclared capability and recoverability loss | Protected-set completeness is not inferable from declared outcomes |

## Minimal example for every charter evidence classification

For compactness, these examples assume matched resources unless the example says otherwise. Where intervals are used, the equivalence region is \([-0.05,+0.05]\), and the illustrative retention floor is 0.90. These values are local to the examples and are not proposed measurement choices.

| Classification | Initial system state | Candidate modification | Feedback source | Held-out evaluation | Observed result | Charter classification | Scientifically correct classification | Reason for agreement or disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genuine future adaptation advantage | Baseline future score 0.50 and retention 0.94 | Grounded change to the adaptation process | Randomly assigned external consequence | Unused perturbations under matched budget | Future score \(0.50\to0.70\); effect interval \([0.14,0.26]\); retention 0.94 | Genuine advantage under declared contract | Positive scoped total feedback effect | Improvement, retention, precision, and causal assignment all pass at the claimed level |
| No material change | Baseline future score 0.60 | Generator hash changes | Grounded external consequence | Same declared perturbation population | Difference \(+0.01\), interval \([-0.02,+0.04]\) | No material change | Practically equivalent under the declared margin | The full interval lies inside the equivalence region |
| Negative future-adaptation change | Baseline future score 0.70 | Update slows later adaptation | Grounded consequence | Unused perturbations | Future score \(0.70\to0.50\), interval \([-0.26,-0.14]\) | Negative change | Negative scoped effect | Material degradation is precise |
| Incomparable tradeoff | High-terminal, slow adapter | Faster but shallower update policy | Grounded latency consequence | Same tasks and resources | Latency \(10\to5\); terminal \(0.90\to0.75\) | Incomparable | Incomparable | No declared rule orders the conflicting dimensions |
| Specialization | Broad current learner | Narrow to frequent family | Grounded current-task reward | Weighted held-out families | Current \(0.70\to0.95\); breadth \(0.80\to0.40\) | Specialization | Distribution-specific optimization | Current gain accompanies narrower adaptation |
| Forgetting-mediated gain | Legacy competence 0.95 | Reallocate representation to new family | Grounded new-family consequence | New family plus protected legacy probe | New-family \(0.50\to0.80\); legacy \(0.95\to0.60\) | Forgetting-mediated gain | New capability bought by declared forgetting | Retention tolerance is violated |
| Generator change without benefit | Baseline future score 0.60 | Nontrivial recorded generator transition | Grounded consequence | Declared future population | Effect 0.00, interval \([-0.03,+0.03]\) | Generator change without benefit and no material change | Modification with equivalent declared outcome | Change alone is not benefit |
| Adaptive collapse | Current score 0.80, future latency 5, failure 0.02 | Aggressive current-task consolidation | Grounded current consequence | Later structural perturbations | Current \(0.80\to0.95\); latency \(5\to25\); failure \(0.02\to0.30\) | Adaptive collapse and negative change | Current gain with future degradation | The future profile collapses despite current competence |
| Fake improvement | Internal score 0.2 and external score 0.60 | Optimize internal self-assessment | Internal reward presented as feedback | External unused tasks | Internal \(0.2\to0.9\); external difference 0.00 | Fake improvement | Proxy-only change | No externally evaluated advantage exists |
| Resource-mediated or current-competence-mediated gain | Baseline systems differ in compute or starting competence | Give candidate twice the compute | Grounded consequence | Same future tasks | Apparent \(0.60\to0.75\); both 0.60 when resources and baseline are matched | Resource/current-competence-mediated | No capacity effect under valid comparison | Advantage disappears with the confound removed |
| Nongrounded or nonspecific modification effect | Baseline future score 0.50 | Grounded and matched shuffled signals both perturb generator | External consequence or shuffled counterpart | Same unused perturbations | Both branches reach 0.65 | Nongrounded or nonspecific effect | Signal correspondence not identified as causal | Matched nongrounded exposure reproduces the effect |
| Causally unresolved | Generator \(G\) and external memory \(W\) share update path | Grounded feedback changes both | Authentic external consequence | Disjoint future tasks | Outcome improves \(+0.20\); \(G\) and \(W\) always co-vary | Causally unresolved for mediation | Total branch effect only | No observation separates generator mediation from external-memory mediation |
| Non-identifiable under permitted interface | Systems A and B match on all allowed probes | Different hidden future-recovery structures | Same feedback histories | Target-relevant but unobservable condition differs | Permitted observations identical; declared target values 0.4 and 0.8 | Non-identifiable | Structural non-identifiability | One observational class contains two target values |
| Inconclusive | Two independent units and incomplete lineage | Candidate generator transition | Grounded signal with uncertain provenance | Sparse held-out tasks | Difference \(+0.10\), interval \([-0.15,+0.35]\) | Inconclusive | Insufficient evidence | Precision and provenance cannot support another category |

## False-negative assessment

The five false-negative constructions are not contradictions in the charter. They separate two statements:

1. no advantage was shown under the frozen contract;
2. no advantage exists under any reasonable contract.

Only the first is licensed. Benefits outside \(H\), outside sampled support, outside the chosen value functional, or outside the permitted interface remain unmeasured. A distributed mechanism that cannot be localized may still support a total branch effect even when generator mediation is unavailable.

## Non-identifiability assessment

Identical internal mechanisms are not required for target identification; only target homogeneity inside each permitted observational class matters. Consequently:

- different internal mechanisms with the same declared target do not threaten identification;
- identical observations with different target values do threaten identification;
- different reachable behavior outside the target domain is a scope issue, not a collision;
- hidden second-perturbation fragility is target-relevant only if the declared target includes that sequence;
- finite empirical success cannot certify factorization over an unrestricted system class.

The charter correctly makes interface identifiability a prerequisite, but it does not itself prove that prerequisite for any adaptive-capacity target.

## Classification of the nineteen unresolved choices

Each item receives exactly one primary category. `Reversal risk` asks whether a plausible alternative choice can reverse or relabel the result. `Freeze` refers to access to confirmatory outcomes. `Sensitivity` means that reasonable alternatives materially relevant to the same scientific question must remain visible; it does not select those alternatives.

| # | Unresolved choice | Primary category | Reversal risk | Freeze before data? | Sensitivity required? | Current placement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | System boundary | Universal requirement | High: moving a change among \(G,S,W\) can reverse generator attribution | Yes | Yes across reasonable boundaries | Partial: the universal obligation is stated, while its study-specific instantiation is left unresolved |
| 2 | Experimental unit | Experiment-specific preregistration choice | High: unit weighting, clustering, and pseudoreplication can reverse results | Yes | Conditional on plausible clustering or interference | Correct |
| 3 | Target population | Experiment-specific preregistration choice | High: system and starting-state inclusion or weighting can reverse the average | Yes | Yes | Correct |
| 4 | Causal estimand | Experiment-specific preregistration choice | High: total, direct, pathway-enabled, and mediated effects may differ in sign | Yes | Yes across scientifically plausible estimands, reported separately | Correct |
| 5 | Identification design | Experiment-specific preregistration choice | High: comparator and causal assumptions determine attribution | Yes | Yes | Correct |
| 6 | Generator-change representation | Experiment-specific preregistration choice | Medium–high: representation can change modification and mediation labels | Yes | Conditional when several faithful representations exist | Correct |
| 7 | Capacity object | Experiment-specific preregistration choice | Very high: vector, distribution, preorder, constraint, or scalar can reverse the verdict | Yes | Yes | Correct |
| 8 | Decision rule | Reporting choice | Very high: margins, dominance, compensation, and priority determine the category | Yes | Yes | Correct in timing; it is a reporting-level choice that nevertheless defines the claim label |
| 9 | Perturbation population | Experiment-specific preregistration choice | Very high: support, family composition, and weighting can reverse the effect | Yes | Yes | Correct |
| 10 | Leakage boundary | Universal requirement | High categorical risk: permissive exposure rules can turn contamination into apparent capacity | Yes | Yes where contamination cannot be excluded | Partial: prevention is universal; the concrete boundary is contextual |
| 11 | Resource accounting | Experiment-specific preregistration choice | Very high: including or excluding search, storage, tools, and offline compute can reverse the adjusted result | Yes | Yes | Correct |
| 12 | Evaluation horizons | Experiment-specific preregistration choice | Very high: transient gain and delayed collapse can reverse ordering | Yes | Yes across declared time scales | Correct |
| 13 | External value functionals | Experiment-specific preregistration choice | Very high: weighting, direction, tail treatment, and evaluator choice can reverse the result | Yes | Yes | Correct |
| 14 | Retention contract | Experiment-specific preregistration choice | Very high: protected set and tolerance can turn gain into forgetting-mediated gain | Yes | Yes | Correct |
| 15 | Control construction | Experiment-specific preregistration choice | High: invalid shuffles, destructive edits, or unmatched branches can create an effect | Yes | Yes | Correct |
| 16 | Stochastic design | Estimator choice | High: replication, pairing, intervals, multiplicity, and stopping can relabel results | Yes | Yes | Correct |
| 17 | Failure handling | Estimator choice | Very high: survivor filtering, censoring, or crash exclusion can reverse the sign | Yes | Yes under plausible missingness and failure treatments | Correct |
| 18 | Interface prerequisite | Universal requirement | High categorical risk: target collisions make positive measurement non-identifiable | Yes | Conditional for approximate or tolerance-dependent equivalence | Partial: factorization is a universal gate; only its proof for the study is unresolved |
| 19 | Amendment governance | Universal requirement | Very high: outcome-motivated revision can manufacture a desired category | Yes | Not applicable as an outcome parameter | Partial: version separation is a governing obligation, not an optional empirical choice |

Category totals:

- **Universal requirements:** 4.
- **Experiment-specific preregistration choices:** 12.
- **Estimator choices:** 2.
- **Reporting choices:** 1.

The section is comprehensive but logically heterogeneous. That is not an inconsistency because every item still has to be settled before confirmatory outcome access.

## Researcher degrees of freedom

| Freedom | Post-outcome manipulation | Can convert null or negative into apparent positive? | Charter containment |
| --- | --- | --- | --- |
| System and generator boundary | Count beneficial state writes as \(G\), harmful ones as ordinary state \(W\) | Yes, especially for mediation | Boundary and causal level must be frozen |
| Experimental unit | Switch among seed, checkpoint, lineage, system, or episode | Yes through weighting, clustering, or pseudoreplication | Unit and dependence structure must be declared |
| Target population | Exclude harmed systems or reweight favorable subgroups | Yes; Simpson reversals are possible | Population, inclusion, and weighting are predeclared |
| Feedback treatment | Select dose, timing, content version, or comparator after inspection | Yes | Treatment versions and assignment policy are frozen |
| Baseline choice | Use a weak no-update or destructive random-edit comparator | Yes | Each control's contrast and limitations are declared |
| Causal claim level | Report whichever of total, pathway, transition, or mediation is positive | Yes | Claim ladder forbids promotion without identification |
| Perturbation selection | Choose favorable tasks, families, axes, or sequences | Yes | Population and sampling law are frozen |
| Perturbation weighting | Change family, severity, or frequency weights | Yes, directly across heterogeneous effects | Weighting and alternative value functionals are declared |
| Exclusion criteria | Drop difficult tasks, units, invalid modifications, or catastrophic cases | Yes | Failed-run and censoring policy are frozen |
| Leakage definition | Relabel exposed templates or families as held out | Yes | Exposure ledger and held-out meaning are declared |
| Resource boundary | Exclude precomputation, search, tools, storage, or parallelism | Yes | Complete pipeline and consumed resources are reported |
| Resource normalization | Choose a favorable conversion between compute, samples, time, memory, and energy | Yes | Incommensurable resources remain separate |
| Retention set | Omit forgotten capabilities | Yes | Protected set is frozen, though omitted capabilities remain a scope limitation |
| Retention tolerance | Loosen \(\epsilon_r\) after failures appear | Yes | Tolerances are frozen |
| Retention probe schedule | Observe only when erase-then-relearn behavior passes | Yes | Schedule is frozen |
| Evaluation horizon | Stop before collapse or after an early disadvantage disappears | Yes | Full schedule and stopping rule are frozen |
| Outcome family | Promote a favorable endpoint from secondary to primary | Yes | Primary outcomes and alternatives are predeclared |
| Outcome weighting | Select a scalarization that hides negative dimensions | Yes | Weights and compensation rules are frozen; dimensions remain visible |
| Decision margin | Move improvement, degradation, or equivalence thresholds | Yes | Margins are frozen |
| Aggregation method | Switch among means, medians, tails, Pareto order, or constrained utility | Yes | Rule for preserving or resolving tradeoffs is frozen |
| Seed inclusion | Remove unfavorable seeds or select favorable randomization | Yes | Replication unit, seed handling, and failed-run policy are frozen |
| Uncertainty method | Change intervals, clustering, multiplicity, or sequential stopping | Yes | Uncertainty and stopping methods are frozen |
| Control implementation | Choose off-support shuffle or damaging random edits | Yes | Validity conditions and limitations must be stated |
| Reporting emphasis | Lead with a favorable aggregate and hide breadth, tails, or retention | Yes rhetorically, even if raw result is unchanged | Separate dimension reporting is mandatory |
| Amendment timing | Revise target, threshold, population, or horizon using pilot outcomes and reuse them | Yes | Motivating data cannot validate the revision |

The highest-risk sign-flip freedoms are capacity representation, perturbation population and weighting, horizon, retention set and tolerance, resource accounting, causal estimand, failure handling, and amendment timing.

## Internal-consistency review

| Apparent conflict | Audit finding |
| --- | --- |
| Held-out novelty versus representative evaluation | A real design tension, not a contradiction. Novelty and representativeness refer to different properties. A finite population can satisfy one while failing the other, producing a narrow or inconclusive result. |
| Fixed resources versus architecture-neutral comparison | Potentially infeasible but not logically inconsistent. The charter permits vector reporting when resources lack a fair conversion; a total ordering then remains unavailable. |
| Generator provenance versus opaque mechanisms | Compatible. The charter asks for lineage without requiring full semantic interpretation and permits branch-level effects when generator intervention is incoherent. |
| Multidimensional reporting versus a categorical verdict | Compatible only because `incomparable` is allowed and the decision rule is unresolved. The named evidence labels overlap and do not form a partition. |
| Capability retention versus exploratory adaptation | A substantive tradeoff, not a contradiction. The chosen protected set and tolerance can reject beneficial exploration; the resulting claim is contract-relative. |
| Causal mediation versus non-invasive measurement | Mediation may be unavailable. The charter explicitly permits the causal claim to stop at a total feedback-branch effect. |
| External grounding versus evaluator exploitation | External provenance does not guarantee independence or immunity to manipulation. The charter recognizes this, but behavioral exploitation can remain undetected. |
| Generator change versus ordinary parameter learning | Boundary-dependent rather than circular. A valid claim requires a frozen system ontology; without it, generator-specific attribution is unavailable. |
| Retention versus reacquisition | The same scheduled performance can arise from preservation or erase-then-relearn. Behavioral retention identifies retained performance at probe times, not necessarily mechanism preservation. |
| Factorization prerequisite versus finite empirical audit | No contradiction, but finite success is not a proof over an open class. A target/interface theorem or explicitly finite-class scope is needed for an identification claim. |

No requirement is inherently mutually incompatible, and the target is not circularly defined. Some stronger claims are simply unavailable for systems in which state, generator, mediator intervention, resource equivalence, or evaluator independence cannot be made coherent.

## Smallest set of claim-blocking deficiencies

No charter-wide deficiency forces verdict B or C. The following are the smallest application-level conditions that block a positive adaptive-capacity claim until resolved:

1. **No frozen target order:** the future-adaptation profile and comparison rule do not determine increase, equivalence, decrease, or incomparability.
2. **No valid causal contrast at the claimed level:** total feedback effect, update-path effect, and generator mediation remain conflated.
3. **No identification through the permitted interface:** target-different systems remain observationally equivalent, or the system class is too open for the claimed proof.
4. **No credible scope boundary:** perturbation population, retention set, horizons, leakage boundary, or full resource vector is missing or admits an alternative explanation that can reverse the result.

These are already represented in the charter as stopping conditions or unresolved choices. Their presence in a concrete study blocks the claim; their existence as study-specific choices does not make the charter inconsistent.

## Why verdict A could be wrong

The principal reason is construct validity. A fully compliant study may operationalize `future adaptive capacity` as performance on one researcher-selected held-out perturbation population. If that population, horizon, retention set, and value family have no defensible relation to the broader capacity language, the charter supports only a causal claim about the declared future-assay profile.

A stricter interpretation of verdict B could treat this absence of a universal bridge from declared assay profile to general adaptive capacity as material underspecification. This audit assigns verdict A because the charter repeatedly confines its conclusions to the declared contract and explicitly denies a context-free property. If later reports omit those indices or use broad language, the same evidence would no longer satisfy verdict A.

## Final evidence map

| Question | Audit answer |
| --- | --- |
| Can ordinary optimization appear positive? | Yes, through cached competence, hidden priors, evaluator-gated policies, or resource leakage. A compliant charter either narrows, relabels, or blocks the claim when these are exposed. |
| Can specialization pass? | Yes under a deliberately narrow declared distribution. It cannot support broader adaptability. |
| Can forgetting be hidden? | Yes outside \(\mathcal R\), between probe times, in joint capabilities, or through increased access cost. |
| Are all six controls sufficient for mediation? | No. Three explicit all-controls-passing counterexamples remain. |
| Does multidimensional evaluation always yield a verdict? | No. Incomparability is unavoidable without a frozen order. |
| Is the result distribution-independent? | No. Weight and support changes can reverse the sign. |
| Are fixed resources intrinsically comparable? | No. Heterogeneous resource vectors can remain unordered. |
| Can an external evaluator be exploited? | Yes. External provenance is not behavioral independence. |
| Can horizon choice reverse the result? | Yes. The claim remains horizon-relative. |
| Can real gains be missed? | Yes, outside sampled support, horizon, retention policy, value functional, or interface. |
| Can target-different systems remain observationally identical? | Yes. Such a collision blocks identification for that interface. |
| Does the charter survive hostile interpretation? | Yes, as a scoped preregistration and claim-admissibility contract—not as a universal definition or measurement of adaptive capacity. |

The audit stops here. No repair, estimator, benchmark, architecture, or instrumentation is authorized by this verdict.
