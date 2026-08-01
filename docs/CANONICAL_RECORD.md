# Canonical Record: Interface Theory

**Status:** canonical conceptual and evidential index.

This repository distinguishes frozen results from illustrative benchmark designs.
Only this record, the linked result ledger, and the evidence index may be cited
as completed Interface Theory evidence.

## Core object

For a declared system class \(F\), experimental interface
\(O:F\to O(F)\), and target \(L:F\to\mathcal T\), the target is
identifiable from the interface exactly when a map

\[
\widehat L:O(F)\to\mathcal T
\]

exists such that

\[
L=\widehat L\circ O.
\]

Equivalently,

\[
O(f_a)=O(f_b)\Rightarrow L(f_a)=L(f_b)
\qquad\forall f_a,f_b\in F.
\]

The restriction to \(O(F)\) is intentional. No extension to unrealizable
observations is claimed.

For a linear class, this specializes to

\[
\ker(O)\subseteq\ker(L).
\]

For stochastic interfaces, \(O(f)\) denotes the induced observation
distribution or stochastic kernel. Finite samples concern estimation of an
existing \(\widehat L\); they do not establish factorization.

## No-bypass hierarchy

\[
\text{factorization}
\longrightarrow
\text{estimation}
\longrightarrow
\text{predictive validity}
\longrightarrow
\text{causal intervention}.
\]

1. **Factorization:** Does \(\widehat L\) exist for the declared
   \((F,O,L)\)?
2. **Estimation:** Can finite data estimate \(\widehat L\) with declared
   uncertainty?
3. **Predictive validity:** Does the recovered target add held-out predictive
   value beyond preregistered baselines?
4. **Intervention:** Can a candidate mechanism causally alter the validated
   target?

A later-stage success cannot repair an earlier-stage failure.

## Evidence policy

- The [result ledger](RESULT_LEDGER.md) is the authoritative cross-gate
  summary; the [evidence index](EVIDENCE_INDEX.md) states the provenance and
  reproducibility level of every row.
- A summary record is not a complete raw audit. Missing raw audits or
  generators are recorded explicitly rather than inferred from a passing
  narrative.
- The `examples/` directory contains legacy or illustrative specifications
  unless an example explicitly links to a frozen ledger entry and matching
  executable evidence.
- Architectures, memories, representation-expansion mechanisms, and change
  detectors are candidate interventions. They do not define a target or prove
  it measurable.
- Correctability, robustness, transfer, viability, and calibration are
  candidate targets \(L\), not privileged primitives.

## Current conclusion

The project does **not** establish a universal intelligence metric, a
substrate-independent correctability scalar, or a superior adaptive
architecture. It establishes a class-scoped program for determining the
target-relevant experimental information required before a proposed adaptive
target can be identified, estimated, tested for predictive value, and
manipulated.

See [RESULT_LEDGER.md](RESULT_LEDGER.md) for frozen interface results,
[EVIDENCE_INDEX.md](EVIDENCE_INDEX.md) for the evidence trail, and
[roadmap.md](roadmap.md) for authorized next work.
