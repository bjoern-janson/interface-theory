# Gate 012 — Nonstationary Revision-Rule Identifiability v0.1

**Execution status:** executed  
**Identifiability result:** conditional finite-horizon positive result under
known linear drift  
**Decision:** record temporal-design requirement; no measurement gate opens.

## Declared class and target

For (t\in\{0,1,2\}),

\[
f_t(e)=\left((a_0+v_at)e,(b_0+v_bt)e^2\right),
\qquad a_0,b_0,v_a,v_b\in\left\{0,\tfrac12\right\}.
\]

The held-out target is the coefficient vector (psi=(a_2,b_2)). Candidate
interfaces may observe only pre-target phases (t=0,1).

## Result

One pre-target slice fails. The preregistered two-slice interface succeeds:

\[
I^*_{F_N}=\{t=0,1\}\times\{e=-1\}\times\{r_1,r_2\}.
\]

| Quantity | Value |
|---|---:|
| Systems | 16 |
| Phase/spatial interfaces evaluated | 150 |
| Target-identifying interfaces | 26 |
| Minimum scalar cost | 4 |
| Minimum sufficient interfaces | 7 |
| Lower-cost candidates identifying | 0 |

The temporal condition is that the observed temporal design spans the known
linear drift family. A snapshot identifies position but not drift direction.

## Scope

This is not a study of HMM regimes, change detectors, adaptive windows,
event-triggered sampling, phase transitions, or unknown/adversarial drift.
Those require separately declared system classes and Gate 1 factorization
tests.
