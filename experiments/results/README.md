# Frozen Gate Results

This directory contains gate-specific evidence artifacts. The authoritative
cross-gate summary is [docs/RESULT_LEDGER.md](../../docs/RESULT_LEDGER.md);
the governing factorization criterion and no-bypass hierarchy are in
[docs/CANONICAL_RECORD.md](../../docs/CANONICAL_RECORD.md); provenance and
reproducibility status are in [docs/EVIDENCE_INDEX.md](../../docs/EVIDENCE_INDEX.md).

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

- A result is canonical only when it agrees with the frozen ledger and the
  evidence index identifies its source artifact and reproducibility status.
- `SUMMARY_RECORD_ONLY` means the repository stores a frozen conclusion but
  not a complete raw candidate table or generation script. It is not an
  independently reproducible audit.
- `INVALIDATED_LEGACY` means the file is deliberately non-evidential. It
  remains only to prevent direct links and parsers from treating its prior
  self-certifying claims as valid.
- Estimator construction remains downstream of a successful factorization
  gate: \(L=\widehat L\circ O\) over the declared class.
