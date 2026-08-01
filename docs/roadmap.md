# Interface Theory Roadmap

**Protocol:** gate-driven, class-scoped research program.

## Purpose

Interface Theory asks a prerequisite question for any proposed adaptive
property:

> Given a declared system class (F), target (L), and allowed
> observation/intervention interface (O), does (L) factor through (O)?

The answer must be established before constructing a metric, evaluating a
mechanism, or claiming an engineering benefit.

See the [canonical record](CANONICAL_RECORD.md) and
[frozen result ledger](RESULT_LEDGER.md) for the present evidence.

## Authorized pipeline

\[
\text{target declaration}
\longrightarrow
\text{factorization}
\longrightarrow
\text{estimation}
\longrightarrow
\text{predictive validity}
\longrightarrow
\text{intervention}.
\]

### Gate 1 — Factorization

Declare:

\[
(F,\;O,\;L,\;\mathfrak I,\;\preceq).
\]

Here (mathfrak I) is the allowed interface family and (preceq) its
access order. Prove or refute:

\[
\exists\widehat L:O(F)\to\mathcal T
\quad\text{such that}\quad
L=\widehat L\circ O.
\]

A constructive failure witness has the form:

\[
O(f_a)=O(f_b)
\quad\text{and}\quad
L(f_a)\ne L(f_b).
\]

If factorization fails, record the boundary or search only the predeclared
interface-refinement family. Do not start estimator development.

### Gate 2 — Estimation

Only after Gate 1 succeeds, declare an estimator (widehat L_n), its
sampling model, uncertainty criterion, and finite budget. Distinguish:

- structural non-identifiability;
- approximate identifiability;
- finite-sample estimation error;
- model misspecification.

A stochastic interface is treated distributionally. Repetition may reduce
estimation error; it does not make an unidentifiable target identifiable.

### Gate 3 — Predictive validity

Freeze the target operationalization and compare preregistered held-out
predictors:

\[
p_0(Y_{\mathrm{future}}\mid B)
\quad\text{versus}\quad
p_1(Y_{\mathrm{future}}\mid B,L).
\]

A score improvement is required on held-out environments. The null is that
the target adds no incremental predictive information beyond (B).

### Gate 4 — Intervention

Candidate mechanisms may be tested only after a target survives the earlier
gates. The question is whether an intervention changes the validated target
and downstream outcome under matched constraints.

Mechanisms do not define targets, interfaces, or evidence of factorization.

## Current frontier

The frozen ledger establishes conditional results for deterministic nonlinear
responses, fixed latent state, known delay, known stationary readout noise,
their controlled composition, and known linear drift. Gate 013 additionally
records a complete finite audit for four labeled operational records in
\(F_{RS}\). Direct target/readout aliases make the two informative probes
jointly identifying; this is reproducible interface composition by construction,
not a simulated authority-network result. It authorizes a separate frozen
**estimation** protocol only as a noisy two-bit decoding study.

Gate 014 records the separate dynamic expansion. Its 216-system rational class
dissociates architecture labels from operational outcomes and separates
identification contexts \(-1,0\) from target context \(+1\). Every interface
below informative probe cost four fails. Three incomparable cost-four
interfaces produce noninjective, target-homogeneous quotients with internal
dynamics diversity. This establishes exact finite target-preserving
compression under the frozen shared response law.

That result does not show that reversible selection or network propagation is
beneficial. Nor does a noninjective quotient rule out a lookup table over the
remaining finite interface fingerprints. Gates 2–4 remain closed until a new
protocol separately declares finite-sample estimation, held-out predictive
validity, or a causal mechanism comparison. Gate 013 and Gate 014 may not be
modified to make a downstream study pass. New unrelated theoretical work
likewise requires its own contract, such as a temporal-rank theorem or a
restricted unknown-drift class.

## Not authorized by the current evidence

The present record does not support claims about:

- a universal correctability metric;
- substrate-independent intelligence;
- open-ended self-improvement;
- representation expansion as a necessary mechanism;
- adaptive change detectors under arbitrary regime shifts;
- architecture performance as confirmation of an Interface Theory target.

Those are future target- or mechanism-specific questions, not current
conclusions.

