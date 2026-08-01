# Gate 014 — Cross-Context Dynamic Factorization

**Execution status:** EXECUTED  
**Scientific decision:** `PASS_NONTRIVIAL_QUOTIENT`  
**Decision subtype:** `PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY`  
**Downstream gates:** CLOSED

Gate 014 exhaustively audits cross-context factorization over 216 deterministic
rational dynamic systems. Identification assays use contexts \(-1,0\); the
target is defined only by independent assays at context \(+1\). Architecture
labels, latent coefficients, internal state, target-assay outputs, and target
values are excluded from the interface.

The frozen generator passed all pre-audit validity checks:

- 216 legal parameter tuples and 216 distinct internal-dynamics signatures;
- exact nuisance constancy;
- disjoint identification and target domains;
- nondegenerate targets with architecture-label/outcome dissociation;
- no target-, observation-, or collision-conditioned filtering.

All \(2^6=64\) subsets of the six-probe vocabulary were audited. Every
interface below informative probe cost four has a preserved factorization
counterexample. The minimum identifying antichain has three incomparable
members:

\[
\begin{aligned}
I_C^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{context}}\},\\
I_N^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{node}}\},\\
I_L^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{lag}}\}.
\end{aligned}
\]

Each minimum interface induces 54 target-homogeneous quotient classes of size
four:

\[
N_Q=54,\qquad N_{\mathrm{singleton}}=0,
\qquad N_{\mathrm{collision}}=54.
\]

All 216 systems participate in collisions. Each class contains dynamically
inequivalent hidden-reserve/compensation and primary/auxiliary-path
decompositions while preserving the target.

The mandatory constant passive control raises protocol probe cost from four to
five. Raw scalar-coordinate cost is 29 for each minimum protocol. These costs
are minimal only within the frozen probe vocabulary; unrestricted encodings
were not tested.

The complete canonical audit is in
[the result JSON](../results/gate_014_dynamic_reopenability_flow/factorization_audit.json).
The unchanged generator reproduces it byte-for-byte.

## Exact interpretation

This result establishes finite target-preserving compression through disjoint
dynamic assays in the declared class. It is stronger than Gate 013's direct
projection control, but it does not rule out an arbitrary finite lookup table
over interface fingerprints. It establishes no estimator, cross-class
generalization, predictive validity, reversible-selection benefit,
authority-network benefit, or adaptive-intelligence architecture. Gates 2–4
remain closed.

