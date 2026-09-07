# Live-Alternative Diagnostic Mediation V1

Protocol state: FROZEN_PRE_EXECUTION_ASSAY  
Implementation state: IMPLEMENTED_NOT_EXECUTED  
Execution state: UNEXECUTED  
Scientific result: NONE  
Canonical standing: NONCANONICAL_RESEARCH_SEED  
Translation standing: NO_TRANSLATION_EARNED

`LIVE_ALTERNATIVE_DIAGNOSTIC_MEDIATION_V1` is an implementation of the approved finite pre-execution design for testing one narrow causal contrast:

```text
same retained alternatives + same marginal predictive signatures
        ->
C0: no joint relation computation
or
C1: temporary read-only joint comparison
        ->
diagnostic selection from the fixed menu {q0,q1}
```

The implementation does not test representation learning, diagnostic invention, persistent interfaces, interface learning, reuse, transfer, generalization, corrigibility, adaptive intelligence, or any earned Interface Theory ↔ MATRIX translation.

## Authority lineage

- Design: `docs/superpowers/specs/2026-09-07-live-alternative-diagnostic-mediation-v1-design.md`
- Plan: `docs/superpowers/plans/2026-09-07-live-alternative-diagnostic-mediation-v1.md`
- Frozen V0: `docs/research_seeds/DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md`

The mediator may compare the two marginal predictive signatures and propose a diagnostic. Only the external world supplies the observation that can resolve the live pair. The same downstream resolver and repair code are used after diagnostic selection in both conditions.

## Permitted implementation validation

```bash
python -m unittest discover -s experiments/research_seeds/live_alternative_diagnostic_mediation_v1 -p 'test_*.py' -v
python experiments/research_seeds/live_alternative_diagnostic_mediation_v1/run_v1.py --validate-contract
python scripts/validate_frozen_record.py
```

Passing unit tests or contract validation is **not** a V1 scientific result. The scientific execution mode is intentionally excluded from implementation validation.

Do not run `--execute` without separate explicit authorization to execute the frozen V1 assay. Until that authorization is given and the assay is actually executed, the legal terminal state remains:

```text
protocol_state = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTED_NOT_EXECUTED
execution_state = UNEXECUTED
scientific_result = NONE
```
