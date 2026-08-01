# Gate 010 — Stochastic Identifiability v0.1

**Execution status:** executed  
**Identifiability result:** approximate finite-sample recovery under known
stationary readout noise  
**Decision:** record sample requirement; no estimator gate opens.

## Declared class

(F_S) holds the (F_0) spatial interface fixed and adds known stationary
Bernoulli readout noise. This is not a stochastic-transition-dynamics study.

## Result

At the distribution level the declared target remains identifiable. Finite
reset-and-replay observations require repetition for accurate decoding.

\[
R^*_{0.05}=92
\]

repetitions **per scalar observation** are the first audited budget meeting the
maximum target-decoding error threshold (delta=0.05).

| Quantity | Value |
|---|---:|
| Scalars in inherited interface | 2 |
| Repetitions per scalar | 92 |
| Total binary queries | 184 |
| Maximum target-decoding error | 0.046459 |

## Scope

Observation-distribution overlap is an estimation problem when the
distributions differ; it is not itself a structural factorization failure.
The result gives no curve beyond the frozen threshold audit and no claim about
unknown noise or stochastic transition dynamics.
