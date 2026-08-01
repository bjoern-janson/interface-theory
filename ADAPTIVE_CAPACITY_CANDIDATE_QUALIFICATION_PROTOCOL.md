# Adaptive-Capacity Candidate Qualification Protocol

## Scope and purpose

This document defines the procedure for determining whether one named candidate instrument satisfies the frozen comparison envelope sufficiently to enter a later comparison.

It is a qualification-admissibility protocol only. It does not qualify a candidate, compare candidates, rank candidates, score candidates, select candidates, recommend candidates, modify the comparison envelope, or design an experiment.

The governing question is:

\[
\boxed{
\text{Does a named candidate satisfy enough of the frozen envelope to enter comparison?}
}
\]

It does not answer:

\[
\boxed{
\text{Is this candidate better than another candidate?}
}
\]

Qualification determines admission. Comparison determines differences among admitted candidates. Selection occurs only after comparison.

## Governing dependencies

This protocol is constrained by:

```text
ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER.md
ADAPTIVE_CAPACITY_MEASUREMENT_CHARTER_HOSTILE_AUDIT.md
INSTRUMENTATION_REQUIREMENTS_ADAPTIVE_CAPACITY.md
FIRST_ADAPTIVE_CAPACITY_CLAIM_PROFILE.md
ADAPTIVE_CAPACITY_INSTRUMENT_COMPARISON_ENVELOPE.md
```

It does not revise, expand, reinterpret, repair, or replace those artifacts.

The inherited claim boundary is:

\[
\boxed{C_1+C_2}
\]

where:

\[
\boxed{
C_2:\text{ causal total feedback-branch effect}
}
\]

and:

\[
\boxed{
C_1:\text{ scoped future-adaptation profile difference}.
}
\]

Qualification cannot authorize \(C_3\) or \(C_4\), irrespective of candidate access, telemetry, intervention capability, or internal visibility.

## Qualification boundary

\[
\boxed{
\text{qualification}\neq\text{comparison}
}
\]

\[
\boxed{
\text{comparison}\neq\text{selection}
}
\]

One candidate version is evaluated against one frozen comparison-envelope version, within one declared scope, using one frozen evidence snapshot and one protocol version.

\[
\boxed{
\text{candidate admissibility is determined by envelope compliance, not candidate capability claims.}
}
\]

The candidate is evaluated against the envelope. The envelope is not revised, relaxed, extended, or reinterpreted to admit the candidate.

## Qualification scope

Qualification checks only:

- mandatory envelope coverage;
- conditional requirements activated by the declared scope and identification design;
- known evidence gaps;
- explicit scope restrictions;
- comparison blockers.

The protocol contains no scores, weights, tiers, feature counts, rankings, preference functions, architecture preferences, repair proposals, experiment designs, or selection criteria.

Optional capability is recorded only when necessary to explain applicability or a known gap. It supplies no compensating credit.

## Qualification commencement conditions

A qualification pass begins only after all of the following are frozen:

- an auditable candidate version \(c\);
- a qualification-protocol version \(p\);
- an instantiated comparison-envelope version \(e\);
- a requested scope \(s_0\);
- the envelope-authorized strict fallback scopes, if any;
- an immutable evidence snapshot \(d\);
- an objective evidence-freshness rule.

The comparison envelope must already settle the reference semantics needed to evaluate one candidate: the claim level, system and assay boundaries, access assumptions, resource vocabulary, evidence schema, evaluator standard, and candidate-to-envelope mapping obligations. Qualification cannot settle those choices for the envelope.

If any commencement input is absent, or if the envelope still requires a scientific choice before a candidate can be evaluated, the qualification relation has not been instantiated. The pass does not begin and no qualification status is assigned. This is not a fourth status and is not evidence against the candidate.

The evidence-freshness rule is fixed by the envelope or this protocol before evaluation. It must be either `NO_AGE_EXPIRY` or a declared validity rule with an exact `valid_through` time or objective review event. Age alone never makes evidence stale unless that frozen rule says it does. Evidence is stale only when, as of the decision timestamp, a declared validity boundary has passed or an enumerated event has occurred: candidate or dependency drift, integrity failure, audit-access loss, source withdrawal, or a frozen expiry. The applied rule and outcome are part of the evidence trace.

Qualification evaluates only **candidate-to-envelope** obligations and blockers. Compatibility between two candidates, or among a set of candidates, remains a later comparison-stage question. A condition that cannot be evaluated without choosing another candidate is recorded as a deferred relational comparability condition; it does not become a candidate defect or affect the single-candidate qualification status.

## Exactly three qualification statuses

These are the only qualification statuses.

### Qualified

The candidate satisfies the frozen comparison envelope for the complete declared purpose and requires no scope narrowing.

### Conditionally qualified

The candidate satisfies the frozen comparison envelope only within an explicitly declared and recorded narrower scope.

### Not qualified

The candidate does not satisfy the frozen comparison envelope for the declared purpose or any permitted predeclared narrower scope.

These statuses are admission states. They are not grades, scores, tiers, rankings, or indicators of scientific superiority.

## Deterministic status semantics

### Requirement truth values

Each universal and activated conditional requirement receives exactly one evidence state:

```text
SATISFIED
UNSATISFIED
```

Unknown, undocumented, unavailable, stale, unverifiable, or ambiguously mapped support is assigned `UNSATISFIED`. No third provisional truth value enters status assignment.

The qualification record may separately explain why a requirement is unsatisfied.

Every conditional requirement also receives one applicability state:

```text
ACTIVATED
NOT_ACTIVATED
```

An applicability judgment that is unknown, undocumented, or unverifiable is treated as `ACTIVATED`; absent verified support, its evidence state is `UNSATISFIED`. `NOT_ACTIVATED` requires affirmative evidence from the frozen scope and envelope.

### Conditional activation

A conditional requirement is activated only by the frozen:

- system class;
- assay scope;
- \(C_2\) identification design;
- access assumptions;
- comparator or control semantics.

It is not activated merely because the candidate happens to support it. Candidate richness cannot enlarge the requirement set or the claim ceiling.

### Scope semantics

Before evidence evaluation, the record freezes:

- the requested scope \(s_0\); and
- a finite set \(\mathcal N_e(s_0)\) of envelope-authorized, nonempty, scientifically substantive strict fallback scopes.

Every fallback scope must preserve the same \(C_1+C_2\) claim type. A fallback cannot reduce the claim to \(C_1\), change the target, change the envelope, or select favorable runs, outcomes, failures, or evidence records. The dimensions along which narrowing is allowed must be declared by the envelope before the evidence snapshot is inspected.

Universal obligations remain universal in every fallback scope. Their scope-indexed evidence may change only because an envelope-authorized system, assay, or access domain is absent from that narrower scope; the obligation itself cannot be waived. Every excluded domain and every resulting loss of generality remains attached to the record.

If multiple incomparable fallback scopes pass, the record preserves all inclusion-maximal passing scopes. It does not choose a favorable scope after inspection.

A candidate-to-envelope blocker outside a permitted fallback scope does not block qualification within that fallback. Any candidate-to-envelope blocker remaining inside it does.

### Scope-indexed pass predicate

For a frozen envelope \(e\), protocol \(p\), candidate \(c\), and evidence snapshot \(d\), let:

- \(U_e(s)\) be the universal requirement instances for scope \(s\);
- \(A_e(s)\) be the conditional requirement instances activated for \(s\);
- \(\operatorname{Sat}_d(r)\) mean that requirement \(r\) is verified as `SATISFIED` by \(d\);
- \(B_e(c,s,d)\) be the candidate-to-envelope blockers remaining in \(s\).

Define:

\[
\operatorname{Pass}_{p}(c,e,s,d)
\iff
\left[
\forall r\in U_e(s)\cup A_e(s),\ \operatorname{Sat}_d(r)
\right]
\land
B_e(c,s,d)=\varnothing.
\]

Conflicting or internally inconsistent evidence is unverifiable and therefore does not satisfy \(\operatorname{Sat}_d\).

### Status rules

A candidate is **Qualified if and only if**:

\[
\operatorname{Pass}_{p}(c,e,s_0,d).
\]

No narrower scope is used or reported as the basis of admission.

A candidate is **Conditionally qualified if and only if**:

\[
\neg\operatorname{Pass}_{p}(c,e,s_0,d)
\]

and:

\[
\exists s\in\mathcal N_e(s_0):
\operatorname{Pass}_{p}(c,e,s,d).
\]

Every inclusion-maximal passing fallback, restriction, excluded domain, and resulting loss of scope is attached to the qualification record. Conditional qualification cannot waive a universal obligation or hide missing mandatory evidence inside an admitted fallback scope.

A candidate is **Not qualified if and only if**:

\[
\neg\operatorname{Pass}_{p}(c,e,s_0,d)
\]

and:

\[
\nexists s\in\mathcal N_e(s_0):
\operatorname{Pass}_{p}(c,e,s,d).
\]

This includes a relevant universal or activated-conditional failure, unavailable or unverifiable mandatory evidence, a candidate-to-envelope blocker in every permitted scope, a requirement for envelope revision, or support for only \(C_1\) where \(C_1+C_2\) is required.

The rules form a disjoint and exhaustive partition after the commencement conditions are met. Full requested-scope passage has precedence; otherwise the existence of a passing predeclared fallback determines conditional qualification; otherwise the candidate is not qualified.

## Deterministic qualification procedure

The admission procedure is:

1. **Identify candidate version.** Freeze an auditable composite manifest covering the candidate code, configuration, dependencies, services, and access mode.
2. **Identify protocol version.** Record the qualification-protocol version and content hash governing this pass.
3. **Identify comparison-envelope version.** Record the exact frozen envelope version and content hash.
4. **Check commencement conditions.** Confirm that the envelope is instantiated for one-candidate evaluation. If not, stop without assigning a status.
5. **Freeze requested and fallback scopes.** Record the requested scope \(s_0\), every envelope-authorized fallback in \(\mathcal N_e(s_0)\), and all prohibited narrowing dimensions before evidence review.
6. **Identify evidence snapshot.** Freeze a content-addressed manifest of the evidence set, artifact identifiers and hashes, provenance, capture and inclusion cutoffs, collection and validation times, missingness and corrections, retention or audit-access limits, and the objective evidence-freshness rule.
7. **Enumerate universal requirements.** Derive them from the frozen envelope, without reference to optional candidate features.
8. **Determine conditional applicability.** For every conditional, assign `ACTIVATED` or `NOT_ACTIVATED` from the frozen system class, assay, access assumptions, comparator, and \(C_2\) design; record the rationale.
9. **Evaluate requirements for each scope.** Assign `SATISFIED` or `UNSATISFIED` to every universal and activated conditional requirement with an evidence reference and rationale.
10. **Identify evidence gaps.** Record unknown, stale, conflicting, undocumented, unavailable, unverifiable, or lossy evidence and the requirements affected.
11. **Evaluate candidate-to-envelope blockers.** Record each unary blocker as present or absent in each scope. Record inherently pairwise or set-level conditions separately as deferred relational comparability conditions.
12. **Evaluate the requested scope first.** Compute \(\operatorname{Pass}_{p}(c,e,s_0,d)\).
13. **Evaluate only predeclared fallbacks if needed.** If the requested scope fails, evaluate every scope in \(\mathcal N_e(s_0)\) and retain all inclusion-maximal passing scopes.
14. **Apply the status partition mechanically.** Assign exactly one of the three qualification statuses.
15. **Record restrictions and limitations.** Preserve every passing fallback, exclusion, gap, assumption, candidate-to-envelope blocker, deferred relational condition, and requalification trigger.
16. **Freeze the qualification record.** Bind it to the five versioned inputs, evidence manifest, requirement-level trace, and deterministic assignment rule.

The procedure produces no score, total, percentage, ordinal tier, ranking, preference, or repair instruction.

## Qualification evidence requirements

### Universal envelope coverage

Qualification must evaluate all universal obligations of the frozen envelope, including:

- frozen \(C_1+C_2\) claim-level declaration;
- system and treatment-branch boundaries;
- starting-state and descendant lineage identity;
- observation-interface and target-identifiability evidence;
- assignment, policy, comparator, treatment-version, branch, exposure, noncompliance, and interference records;
- temporal order and stopping-rule integrity;
- resource vocabulary, lifecycle boundary, and available/consumed/inherited records;
- exposure, leakage, and novelty records;
- evaluator and outcome integrity;
- retention, multidimensional outcomes, failures, missingness, censoring, and denominators;
- replication, pairing, dependence, exact counts, multiplicity, and uncertainty support;
- record persistence, configuration integrity, amendment history, decision provenance, and assay-profile linkage.

### Activated conditional envelope coverage

Conditional requirements are evaluated only when activated by the frozen system class, assay scope, \(C_2\) design, access assumptions, comparator, or control semantics. They may include:

- deeper internal visibility required for branch reconstruction;
- internal event timing required by treatment or comparator definitions;
- limited state access;
- a particular comparator or confound check;
- joint-capability, sequential-perturbation, or access-cost records;
- specialized resource categories.

Limited intervention or internal evidence used to validate a \(C_2\) comparator remains \(C_2\) evidence. It cannot be interpreted as pathway-specific or generator-mediated evidence.

## Evidence mapping rules

Evidence must map to common envelope obligations, not necessarily to identical raw fields or substrate-specific variables.

For every requirement, the record must preserve:

- requirement identifier or unambiguous envelope reference;
- applicability basis;
- evidence state;
- evidence-snapshot reference;
- representation or mapping used;
- known information loss or tolerance;
- rationale;
- scope consequence of failure.

A lossy mapping is sufficient only when the frozen envelope permits it and the loss does not discard mandatory \(C_1+C_2\) evidence or create a target-changing observational collision.

Candidate self-description is not evidence unless independently auditable under the envelope.

## Qualification record

Qualification is specific to:

- one candidate composite manifest;
- one qualification-protocol version;
- one comparison-envelope version;
- one requested scope and its predeclared fallback set;
- one immutable evidence snapshot.

The record must include:

```text
candidate_version
qualification_protocol_version
comparison_envelope_version
evidence_snapshot_identifier
declared_scope
qualification_date
qualification_status
requalification_trigger
mandatory_requirements_status
conditional_requirements_status
known_evidence_gaps
scope_restrictions
comparison_blockers
```

The following supplementary fields are also mandatory for an executable record:

```text
qualification_record_id
candidate_manifest_hash
qualification_protocol_hash
comparison_envelope_hash
evidence_snapshot_manifest
evidence_freshness_rule
requested_scope
authorized_fallback_scopes
passing_fallback_scopes
qualified_scope
deferred_relational_comparability_conditions
requalification_conditions
decision_timestamp
assessor_identity
supersedes_record_id
```

`declared_scope` is a structured object containing the requested system class, \(C_1+C_2\) claim and target, assay and perturbation population, access envelope, temporal schedule, resource and exposure boundaries, evaluator and comparator semantics, tolerances, exclusions, and the predeclared fallback set. `qualified_scope` equals the requested scope for `Qualified`, contains all inclusion-maximal passing fallback scopes for `Conditionally qualified`, and is empty for `Not qualified`.

`mandatory_requirements_status` and `conditional_requirements_status` are itemized evidence maps, not counts or percentages. Every item records its requirement identifier, scope, applicability state where relevant, activation rationale, binary evidence state, evidence citation, mapping, loss or tolerance, and failure consequence.

`comparison_blockers` contains only candidate-to-envelope blockers that can be evaluated against the frozen reference semantics. Pairwise and set-level conditions are stored in `deferred_relational_comparability_conditions` and do not affect qualification status.

`evidence_snapshot_manifest` is immutable or content-addressed and records included artifact identifiers and hashes, provenance, capture and inclusion cutoffs, collection and validation times, missingness, corrections, source availability, retention limits, the frozen evidence-freshness rule and its decision-time result, and the candidate, envelope, and protocol manifests against which it was evaluated.

`qualification_date` is the decision date, distinct from the evidence capture cutoff, validation time, retention deadline, and any later requalification event. The inherited field name `requalification_trigger` is an alias for `requalification_conditions`: an immutable issuance-time list of objective conditions that would require a future pass. Actual later events are never written into or used to mutate the qualification record.

The record must also preserve the deterministic status-assignment trace: requested scope, authorized fallback set, requirement instances, activated-requirement set, binary requirement results, candidate-to-envelope blocker results, passing scopes, and the rule that produced the status. This trace introduces no score.

## Qualification relation

Qualification is not an enduring property of a candidate.

\[
\boxed{
\text{qualification is a versioned relation between protocol, candidate, evidence, scope, and envelope.}
}
\]

For a fixed qualification-protocol version \(p\), the qualification relation is:

\[
\boxed{
Q_p(c,e,s,d)
\in
\{
\text{Qualified},
\text{Conditionally qualified},
\text{Not qualified}
\},
}
\]

where:

- \(c\) is the candidate version;
- \(e\) is the frozen comparison-envelope version;
- \(s\) is the structured requested scope and predeclared fallback set;
- \(d\) is the frozen evidence snapshot.

When \(p\) is fixed by the surrounding record, \(Q(c,e,s,d)\) is shorthand for \(Q_p(c,e,s,d)\). Qualification is therefore bound to five frozen coordinates even though the inherited four-argument notation may be used as shorthand.

## Requalification and version invalidation

### Immutable requalification conditions

A qualification does not transfer across a change in any frozen coordinate. At issuance, `requalification_conditions` freezes the following objective trigger taxonomy:

- candidate code, configuration, dependency, model, service, or access-mode revision;
- qualification-protocol revision;
- comparison-envelope amendment;
- system, assay, target, access, temporal, resource, exposure, evaluator, comparator, assignment, treatment-version, or causal-estimand scope change;
- observation-field, transformation, discarded-data, evidence-mapping, or tolerance change;
- evidence-snapshot addition, correction, withdrawal, objective expiry, integrity failure, or loss of audit access;
- a newly discovered collision, leakage path, requirement failure, or candidate-to-envelope blocker;
- a change in conditional applicability.

The frozen evidence-freshness rule decides whether an age or review event constitutes objective expiry. A claimed nonmaterial change must be documented separately with its rationale and authorizing decision; it cannot silently inherit qualification.

### Append-only lifecycle catalog

A qualification decision and its evidence remain immutable for the original \((p,c,e,s,d)\) tuple. Actual later events are written only to an append-only lifecycle catalog with:

```text
event_id
qualification_record_id
event_type
event_time
reason
affected_coordinate
replacement_record_id
authorizing_identity
```

`event_type` may be `NONMATERIAL_CHANGE_REVIEW`, `SUPERSEDED`, or `WITHDRAWN`. `SUPERSEDED` and `WITHDRAWN` are terminal catalog events, and at most one may apply to a qualification record. `SUPERSEDED` requires `replacement_record_id`; `WITHDRAWN` uses an empty replacement field.

Catalog applicability is derived deterministically:

- `CURRENT` when no terminal event exists;
- `SUPERSEDED` when a `SUPERSEDED` event exists;
- `WITHDRAWN` when a `WITHDRAWN` event exists.

Crossing a frozen `valid_through` boundary constitutes a `WITHDRAWN` event at that exact time by rule. Catalog queries derive that withdrawal directly from the evidence manifest even if materialization of the event row is delayed.

These are catalog applicability labels, not qualification statuses. A later event never mutates the qualification tuple, snapshot, status, requirement trace, or restrictions. Any renewed claim requires a new qualification pass and record.

## Non-modification rule

\[
\boxed{
\text{The candidate is evaluated against the envelope.}
}
\]

\[
\boxed{
\text{The envelope is not modified to admit the candidate.}
}
\]

Any requested requirement change belongs to a separately governed envelope-revision process. It cannot occur inside qualification, and the evidence motivating the request cannot validate the revised envelope.

Qualification supplies no repair proposal for an unqualified candidate.

## Governance constraints

\[
\boxed{
\text{Qualification does not compare candidates.}
}
\]

\[
\boxed{
\text{Qualification does not rank candidates.}
}
\]

\[
\boxed{
\text{Qualification does not select candidates.}
}
\]

\[
\boxed{
\text{Qualification cannot increase the claim ceiling beyond }C_2.
}
\]

\[
\boxed{
\text{Optional capability cannot compensate for missing mandatory capability.}
}
\]

Additional capabilities may be recorded as out-of-scope facts only. They cannot change requirement activation, offset an unsatisfied requirement, break a tie, or modify qualification status.

## Stop boundary

This artifact stops after defining qualification admissibility. It does not proceed to candidate qualification, candidate comparison, selection, experiment design, or implementation.

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

The artifact defines admission. It does not decide preference.

## Explicit non-goals

This protocol does not:

- qualify a candidate;
- compare candidates;
- score, rank, recommend, or select candidates;
- define winners, tiers, weights, or preferences;
- revise the comparison envelope;
- propose repairs;
- define experiments, benchmarks, estimators, or metrics;
- define software architecture or implementation;
- introduce new theory;
- expand the claim level;
- authorize candidate-specific action beyond a future qualification pass.
