# Adaptive Capacity Qualification Record Template

Blank record template for one candidate version evaluated under one frozen qualification-protocol version, one frozen comparison-envelope version, one declared scope, and one immutable evidence snapshot.

Qualification is distinct from later stages:

```text
qualification != comparison != selection
```

The candidate is evaluated against the frozen envelope. The envelope is not revised to admit the candidate. The claim ceiling remains (C_1+C_2).

## Record

```yaml
qualification_record_id: ""

candidate_version:
  identifier: ""
  composite_manifest_hash: ""

qualification_protocol_version:
  identifier: ""
  content_hash: ""

comparison_envelope_version:
  identifier: ""
  content_hash: ""

evidence_snapshot:
  identifier: ""
  manifest:
    artifact_identifiers_and_hashes: []
    provenance: ""
    capture_cutoff: ""
    inclusion_cutoff: ""
    collection_time: ""
    validation_time: ""
    missingness_and_corrections: ""
    source_availability: ""
    retention_or_audit_access_limits: ""
  freshness_rule: ""
  freshness_result_at_decision: ""

declared_scope:
  requested_scope: ""
  requested_system_class: ""
  claim_and_target: "C1+C2"
  assay_and_perturbation_population: ""
  access_envelope: ""
  temporal_schedule: ""
  resource_and_exposure_boundaries: ""
  evaluator_and_comparator_semantics: ""
  tolerances: ""
  exclusions: ""
  authorized_fallback_scopes: []
  prohibited_narrowing_dimensions: []

qualification_status: "<Qualified | Conditionally qualified | Not qualified>"

mandatory_requirements_status:
  - requirement_id: ""
    scope: ""
    applicability_state: "ACTIVATED"
    activation_rationale: ""
    evidence_state: "<SATISFIED | UNSATISFIED>"
    evidence_snapshot_reference: ""
    representation_or_mapping: ""
    information_loss_or_tolerance: ""
    rationale: ""
    scope_consequence_of_failure: ""

conditional_requirements_status:
  - requirement_id: ""
    scope: ""
    applicability_state: "<ACTIVATED | NOT_ACTIVATED>"
    activation_rationale: ""
    evidence_state: "<SATISFIED | UNSATISFIED>"
    evidence_snapshot_reference: ""
    representation_or_mapping: ""
    information_loss_or_tolerance: ""
    rationale: ""
    scope_consequence_of_failure: ""

known_evidence_gaps: []

comparison_blockers:
  - scope: ""
    blocker: ""
    status: "<PRESENT | ABSENT>"
    evidence_snapshot_reference: ""
    rationale: ""

authorized_fallback_scope_results:
  - scope: ""
    pass_result: "<PASS | FAIL>"
    passing_fallback_scopes: []

qualified_scope: ""

scope_restrictions: []

deferred_relational_comparability_conditions: []

requalification_conditions: []

lifecycle_metadata:
  qualification_date: ""
  decision_timestamp: ""
  assessor_identity: ""
  supersedes_record_id: ""
  lifecycle_events: []
```

## Deterministic status trace

```yaml
status_assignment_trace:
  requested_scope: ""
  authorized_fallback_scope_set: []
  requirement_instances: []
  activated_requirement_set: []
  binary_requirement_results: []
  candidate_to_envelope_blocker_results: []
  passing_scopes: []
  assignment_rule: ""
```

## Status values

Use exactly one of:

```text
Qualified
Conditionally qualified
Not qualified
```

These are admission states only. This record does not compare candidates, rank candidates, select candidates, score candidates, or revise the comparison envelope.
