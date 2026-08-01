# Frozen Interface-Theory Result Ledger

**Status:** authoritative summary of completed, class-scoped interface gates.

A result in this ledger establishes neither a universal metric nor a
mechanism effect. It establishes only whether a declared target is identifiable
under the stated class and interface family. Every row links to its provenance
and explicitly records whether a complete raw audit is available.

## Resource notation

\[
\mathcal C_I(\psi,F)=
(N_{\mathrm{scalar}},N_{\mathrm{readout}},N_{\mathrm{probe}},
T_{\mathrm{temporal}},R_{\mathrm{repeat}},\text{precision}).
\]

The temporal coordinate is class-specific: it may be an observation lag or a
pre-target phase span. Minimal interfaces can be non-unique, so a row names a
representative member of the minimum antichain unless the evidence index says
otherwise.

## Executed results

| Class | Representative minimum interface | Resource vector | Scoped result | Evidence |
|---|---|---:|---|---|
| \(F_0\): closed deterministic nonlinear response class | \(\{e=-1\}\times\{r_1,r_2\}\) | \((2,2,1,0,1,\mathrm{exact})\) | Seven cost-two candidates identify the declared target in the frozen audit. The older “one refinement-minimal / 38 total sufficient” figures are noncanonical summary-only artifacts pending a complete partial-order audit. | [F0 record](EVIDENCE_INDEX.md#f0-nonlinear-baseline) |
| \(F_H\): \(F_0\) plus fixed latent state | \(\{-1,0,1\}\times\{r_\Sigma\}\) | \((3,1,3,0,1,\mathrm{exact})\) | The inherited \(F_0\) interface fails; a unique cost-three aggregate-readout interface succeeds in the frozen ladder. | [FH record](EVIDENCE_INDEX.md#fh-hidden-state) |
| \(F_D\): \(F_0\) plus a fixed known one-step delay | \(\{e=-1\}\times\{r_1,r_2\}\times\{\lambda=1\}\) | \((2,2,1,1,1,\mathrm{exact})\) | Immediate observation is temporally misaligned; lag-one observation restores the spatial distinction. | [FD record](EVIDENCE_INDEX.md#fd-delay) |
| \(F_S\): \(F_0\) plus known stationary binary readout noise | \(\{e=-1\}\times\{r_1,r_2\}\), 92 repetitions per scalar | \((2,2,1,0,92,\mathrm{Bernoulli};\delta=0.05)\) | Exact finite-sample decoding is unavailable; 92 repetitions per scalar give maximum target-decoding error 0.046459. | [FS record](EVIDENCE_INDEX.md#fs-stochastic-readout-noise) |
| \(F_{HD}\): fixed latent state plus fixed one-step delay | \(\{-1,0,1\}\times\{r_\Sigma\}\times\{\lambda=1\}\) | \((3,1,3,1,1,\mathrm{exact})\) | The lifted hidden-state interface is the unique minimum at lag one. No supra-compositional cost or lower-cost synergy appears in this ladder. | [FHD record](EVIDENCE_INDEX.md#fhd-hidden-state--delay) |
| \(F_N\): closed known-linear-drift response class | \(\{t=0,1\}\times\{e=-1\}\times\{r_1,r_2\}\) | \((4,2,1,1,1,\mathrm{exact})\) | One pre-target slice fails; two slices identify the held-out \(t=2\) coefficient vector. Among 150 interfaces, 26 identify; none below scalar cost four does. | [FN record](EVIDENCE_INDEX.md#fn-known-linear-drift) |
| \(F_{RS}\): four-record operational label class | \(\{\text{baseline},\text{reversal recovery},\text{downstream flow}\}\) | \(C_{\mathrm{protocol}}=3;\ C_{\mathrm{informative}}=2\) within the declared readout vocabulary | Each individual probe is insufficient for the joint target. The combined protocol factors by direct label/readout aliases. The complete finite audit and deterministic generator are committed. | [FRS record](EVIDENCE_INDEX.md#frs-reversible-network-selection) |
| \(F_{014}\): 216-system cross-context rational dynamic class | Identification contexts \(c\in\{-1,0\}\); target context \(c=+1\). A representative minimum is \(\{R_{-1},R_0,K_{-1},K_{\mathrm{context}}\}\). | \(C_{\mathrm{protocol}}=5\) probes including the mandatory constant baseline; \(C_{\mathrm{informative}}=4\) probes and 29 raw scalar coordinates within the frozen vocabulary. | Every lower-cost interface fails. Three incomparable cost-four interfaces induce 54 target-homogeneous classes of size four, with all 216 dynamically inequivalent systems in collisions. | [F014 record](EVIDENCE_INDEX.md#f014-cross-context-dynamic-factorization) |

## Interpretation limits

- The \(F_S\) row concerns **readout noise**, not stochastic transition
  dynamics. It is an estimation-budget result after distribution-level
  identifiability is declared.
- The \(F_N\) row assumes a closed, known linear drift family. It says nothing
  about unknown, nonlinear, adversarial, or unbounded drift.
- The \(F_{HD}\) result is a separability result within one finite partial
  order; it is not an additive law of nature.
- The \(F_0\) count of seven identifies a minimum **cost** tier. It does not,
  without a complete committed refinement relation, establish a unique
  refinement-minimal interface or a total sufficient-interface count.
- The \(F_{RS}\) row contains four labeled operational records, not simulated
  suppression, recurrence, graph, redistribution, or propagation dynamics.
  Protocol cost three includes a mandatory constant baseline. Informative cost
  two is minimal only over the two predeclared binary probes; unrestricted
  scalar encodings are outside the audit.
- The \(F_{014}\) result is an exact finite target-preserving compression
  result under a shared affine context law. A noninjective quotient prevents
  lookup by complete system identity, but the induced target map may still be
  an arbitrary lookup over finite interface fingerprints. It establishes no
  estimator, cross-class generalization, predictive validity, or mechanism
  efficacy. Probe and scalar costs are scoped to the frozen vocabulary.
- No row opens estimator development without a separate frozen estimation
  protocol.

## Current decision

Theoretical pruning is complete for the original interface classes. Gate 013
remains the direct-projection control. Gate 014 establishes only scoped
cross-context finite factorization over \(F_{014}\); Gates 2–4 remain closed.
Any estimation, prediction, or mechanism study requires a separately frozen
protocol and cannot modify either completed Gate 1 record.

