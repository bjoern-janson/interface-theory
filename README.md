# Interface Theory

A class-scoped framework for determining when a declared property of an
adaptive system is measurable through a declared observation/intervention
interface.

**Current status:** theoretical pruning is complete for the frozen classes in
the [result ledger](docs/RESULT_LEDGER.md). No universal adaptive metric,
correctability scalar, or mechanism claim has been validated.

## Core criterion

Let (F) be a declared system class, (O:F\to O(F)) an
observational-interventional interface, and (L:F\to\mathcal T) a declared
target. The target is identifiable from the interface exactly when

\[
\exists\,\widehat L:O(F)\to\mathcal T
\quad\text{such that}\quad
L=\widehat L\circ O.
\]

Equivalently,

\[
O(f_a)=O(f_b)\Rightarrow L(f_a)=L(f_b)
\qquad\forall f_a,f_b\in F.
\]

An interface fails when it leaves an admissible target-changing distinction
unobserved. No estimator can repair information that never enters the
interface.

## No-bypass research hierarchy

| Gate | Question | A failure means |
|---|---|---|
| Factorization | Does (L) factor through (O) over (F)? | The target is not identifiable under this interface. |
| Estimation | Can finite data estimate \(\widehat L\) with declared uncertainty? | The target may be identifiable in principle but not measurable under the available budget. |
| Predictive validity | Does the recovered target improve held-out prediction beyond preregistered baselines? | The target is measurable but currently redundant. |
| Intervention | Can a candidate mechanism causally change the validated target? | The mechanism is not effective for that target. |

A later-stage result never repairs an earlier-stage failure.

## Canonical evidence

- [Canonical record](docs/CANONICAL_RECORD.md) — definitions, scope, and
  evidence policy.
- [Frozen result ledger](docs/RESULT_LEDGER.md) — class-scoped positive and
  negative interface results.
- [Roadmap](docs/roadmap.md) — authorized next work.

The frozen ledger separates spatial access, temporal alignment, statistical
repetition, latent structure, composition, and known drift. These are
interface requirements, not ingredients of intelligence.

## Examples

The materials in `examples/` are **illustrative or legacy specifications**
unless they explicitly link to a matching frozen-ledger entry and executable
evidence. They must not be cited as completed results merely because they
contain a proposed benchmark, factorization audit, or expected outcome.

Candidate architectures, memory systems, representation expansion, posterior
beliefs, and change detectors are not interfaces by default. They become
candidate mechanisms only after their raw information access and target have
been separately declared.

## Repository structure

```text
docs/
  CANONICAL_RECORD.md
  RESULT_LEDGER.md
  roadmap.md
examples/
  illustrative and legacy specifications
experiments/
  executable evidence and result artifacts
```

## License

This project is licensed under the [MIT License](LICENSE).
