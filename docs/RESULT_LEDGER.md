# Frozen Interface-Theory Result Ledger

**Status:** authoritative summary of completed, class-scoped interface gates.

A result in this ledger establishes neither a universal metric nor a
mechanism effect. It establishes only whether a declared target is identifiable
under the stated class and interface family.

## Resource notation

\[
\mathcal C_I(\psi,F)=
(N_{\mathrm{scalar}},N_{\mathrm{readout}},N_{\mathrm{probe}},
T_{\mathrm{temporal}},R_{\mathrm{repeat}},\text{precision}).
\]

The temporal coordinate is class-specific: it may be an observation lag or a
pre-target phase span. Minimal interfaces can be non-unique, so these rows
give a representative member of the minimum antichain.

## Executed results

| Class | Representative minimum interface | Resource vector | Scoped result |
|---|---|---:|---|
| (F_0): closed deterministic nonlinear response class | ({e=-1}\times{r_1,r_2}) | ((2,2,1,0,1,\mathrm{exact})) | All lower-cost candidates fail; seven cost-two interfaces identify the declared target. |
| (F_H): (F_0) plus fixed latent state | ({-1,0,1}\times{r_\Sigma}) | ((3,1,3,0,1,\mathrm{exact})) | The inherited (F_0) interface fails; a unique cost-three aggregate-readout interface succeeds. |
| (F_D): (F_0) plus a fixed known one-step delay | ({e=-1}\times{r_1,r_2}\times{\lambda=1}) | ((2,2,1,1,1,\mathrm{exact})) | Immediate observation is temporally misaligned; lag-one observation restores the spatial distinction. |
| (F_S): (F_0) plus known stationary binary readout noise | ({e=-1}\times{r_1,r_2}), 92 repetitions per scalar | ((2,2,1,0,92,\mathrm{Bernoulli}\;\delta=0.05)) | Exact finite-sample decoding is unavailable; 92 repetitions per scalar give maximum target-decoding error 0.046459. |
| (F_{HD}): fixed latent state plus fixed one-step delay | ({-1,0,1}\times{r_\Sigma}\times{\lambda=1}) | ((3,1,3,1,1,\mathrm{exact})) | The lifted hidden-state interface is the unique minimum at lag one. No supra-compositional cost or lower-cost synergy appears in this ladder. |
| (F_N): closed known-linear-drift response class | ({t=0,1}\times{e=-1}\times{r_1,r_2}) | ((4,2,1,1,1,\mathrm{exact})) | One pre-target slice fails; two slices identify the held-out (t=2) coefficient vector. Among 150 interfaces, 26 identify; none below scalar cost four does. |

## Interpretation limits

- The (F_S) row concerns **readout noise**, not stochastic transition
  dynamics. It is an estimation-budget result after distribution-level
  identifiability is declared.
- The (F_N) row assumes a closed, known linear drift family. It says nothing
  about unknown, nonlinear, adversarial, or unbounded drift.
- The (F_{HD}) result is a separability result within one finite partial
  order; it is not an additive law of nature.
- No row opens estimator development without a separate frozen estimation
  protocol.

## Current decision

Theoretical pruning is complete for these declared classes. Measurement
development remains closed until a newly declared target passes a
factorization gate under a useful interface and system class.
