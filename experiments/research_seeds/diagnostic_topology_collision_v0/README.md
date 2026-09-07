# Diagnostic Topology Collision V0 — Executable Conformance Implementation

Operative pre-execution refreeze commit: `c650943031831aaa50379dd5dd79515bf681c0f3`

Frozen source blob: `447e5db3f15476406910a32e1d36c0e2364e1344`

Repair-authority addendum blob: `303031bdec77dfffb4a5d6c9bdd2d033f30314ac`

```text
protocol_state       = FROZEN_PRE_EXECUTION_ASSAY
implementation_state = IMPLEMENTATION_IN_PROGRESS
execution_state      = UNEXECUTED
scientific_result    = NONE
```

This implementation instantiates an already-derived finite construction. It may expose conformance failure; it may not change the frozen expected object to accommodate implementation output.

The only legal implementation-phase runner command is:

```bash
python run_v0.py --validate-contract
```

The successful `--execute --write ...` path requires a later explicit authorization.

## Module boundaries

- `protocol.py` — frozen world, action, repair, and resource semantics.
- `representation.py` — raw history, matched one-bit encoders, and the fixed controller.
- `viability.py` — required viable initial-action analysis; no singleton-policy claim.
- `conformance.py` — representative episode semantics, static validation, and the dormant exhaustive conformance runner.
- `run_v0.py` — hard validation-versus-execution CLI gate.

## Lineage

```text
analytic finite witness
    -> executable implementation
    -> separate execution authorization required
    -> exact conformance reproduction OR conformance failure
```

Implementation must preserve the distinction:

```text
policy existence != policy selectability from exposed information
```

The representation intervention may change controller-visible selection of the world-viable initial diagnostic; it may not change the world's viable-policy classes.
