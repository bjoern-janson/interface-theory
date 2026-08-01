# Gate Registry

**Canonical cross-gate source:** [docs/RESULT_LEDGER.md](../docs/RESULT_LEDGER.md)  
**Evidence provenance:** [docs/EVIDENCE_INDEX.md](../docs/EVIDENCE_INDEX.md)  
**Method:** [docs/CANONICAL_RECORD.md](../docs/CANONICAL_RECORD.md)

A gate number does not authorize a downstream measurement or engineering
claim. Historical artifacts are permanent evidence, but only records marked
canonical in the evidence index establish a current frozen result.

## Historical pruning gates

| Gate | Result | Permanent consequence |
|---|---|---|
| Gate 001 — CMI v0.1 observation sufficiency | Non-identifying behavioral interface. | Stop the behavior-only estimator branch. |
| Gate 002 — CMI v0.2 updater pathway | Non-identifying pathway assay. | Stop the pathway-estimator branch. |
| Gate 003 — finite interface non-identifiability | Counterexample found. | Require a factorization gate before estimator construction. |
| Gate 004 — restricted positive identifiability | Positive result in a restricted linear class. | Target-relative recovery can be possible under declared access conditions. |
| Gate 006 — nonlinear target identifiability | Inherited interface is non-identifying. | Search for a declared minimal refinement rather than patching an estimator. |

## Current frozen interface gates

| Gate | Declared class | Scientific result | Decision |
|---|---|---|---|
| Gate 007 — nonlinear baseline search | \(F_0\) | Target identifiable in the declared nonlinear interface ladder; the frozen minimum is \(\{e=-1\}\times\{r_1,r_2\}\) at scalar cost two. Seven cost-two candidates identify; the separate target-aligned scalar belongs only to illustrative `examples/F0_linear/`. | Record scoped result |
| Gate 008 — hidden-state generalization | \(F_H\) | Inherited interface fails; a three-probe aggregate behavioral interface is the unique minimum in the frozen ladder. | Record boundary |
| Gate 009 — delay identifiability | \(F_D\) | Lag 0 fails; inherited spatial interface at lag 1 identifies the target. | Record boundary |
| Gate 010 — stochastic identifiability | \(F_S\) | Known stationary readout noise preserves structural identifiability; 92 repetitions per scalar observation meet the declared \(\delta=0.05\) error criterion. | Estimation budget only |
| Gate 011 — hidden-plus-delay composition | \(F_{HD}\) | Unique minimum has three scalar observations at lag one; no supra-compositional penalty or lower-cost synergy in the frozen class. | Record scoped composition |
| Gate 012 — nonstationary identifiability | \(F_N\) | Under known closed linear drift, two pre-target slices identify the \(t=2\) target; no interface below scalar cost four succeeds. | Record scoped result |

## Target-specific factorization pilot

| Gate | Declared class and target | Scientific result | Decision |
|---|---|---|---|
| Gate 013 — reversible selection and network propagation | \(F_{RS}\), \(L_{RS}=(R_{\mathrm{reopen}},K_{\mathrm{flow}})\) | In the complete four-member deterministic audit, current performance alone and either individual intervention probe are non-identifying. The combined behavioral interface has scalar cost three and identifies the declared two-component target. | Record Gate 1 only; estimation, predictive validity, and intervention remain closed. |

The complete contract, deterministic generator, and all counterexample witnesses
are committed under [Gate 013](gate_013_reversible_network_selection/README.md).
This is a deliberately finite operational target, not a result about general
authority dynamics, diversity preservation, or adaptive intelligence.

## Legacy Gate 005 and Gate 007 audit records

The old Gate 005 and Gate 007 machine-readable audit files are retained only as
**superseded summary records**. They lack a complete reproducible
partial-order enumeration and contain outdated “next gate” labels. They do
not establish the older claims of a unique refinement-minimal interface or 38
total sufficient interfaces. See [EVIDENCE_INDEX.md](../docs/EVIDENCE_INDEX.md).

## Gate rule

\[
\text{Factorization}
\rightarrow
\text{Estimation}
\rightarrow
\text{Predictive validity}
\rightarrow
\text{Intervention}.
\]

A failed factorization gate blocks estimator development for that declared
\((F,L,\mathfrak I)\) branch. A successful finite-class gate does not establish
predictive validity or mechanism efficacy.