# Frozen Gate Results

This directory contains gate-specific evidence artifacts. The authoritative cross-gate
summary is [docs/RESULT_LEDGER.md](../../docs/RESULT_LEDGER.md); the governing
factorization criterion and no-bypass hierarchy are in
[docs/CANONICAL_RECORD.md](../../docs/CANONICAL_RECORD.md).

## Reading a gate result

Keep execution and scientific outcomes separate:

```text
Execution status: PASSED
Identifiability result: IDENTIFIABLE | NON-IDENTIFIABLE | APPROXIMATELY IDENTIFIABLE
Decision: ADVANCE | STOP ESTIMATOR DEVELOPMENT | RECORD BOUNDARY
```

A scientifically negative result can therefore be a successfully executed gate.
Conversely, passing a finite-class interface gate does not validate a universal
metric, predictive construct, or engineering mechanism.

## Evidence policy

- A result is canonical only when it agrees with the frozen ledger and its linked
  executable evidence.
- `examples/` are illustrative or legacy unless explicitly rebuilt from the ledger.
- Estimator construction remains downstream of a successful factorization gate:
  `L = \widehat L \circ O` over the declared class.
