# Gate 008 — Hidden-State Interface Generalization v0.1

**Execution status:** executed  
**Identifiability result:** conditional positive after interface refinement  
**Decision:** record the class-scoped minimum; no estimator gate opens.

## Declared class and target

(F_H) adds one fixed latent revision state to the frozen nonlinear (F_0)
class. The target and 50-member behavioral interface ladder remain fixed.

## Result

The inherited (F_0) interface,

\[
\{e=-1\}\times\{r_1,r_2\},
\]

is non-identifying. The systems ((a,b,h)=(1,1,0)) and ((1,1,1)) have the
same allowed trace ((-1,1)) but different target values.

The unique minimum in the frozen ladder is

\[
I^*_{F_H}=\{-1,0,1\}\times\{r_\Sigma\}.
\]

| Quantity | Value |
|---|---:|
| Systems | 8 |
| Interfaces evaluated | 50 |
| Target-identifying interfaces | 13 |
| Minimum scalar cost | 3 |
| Minimum sufficient interfaces | 1 |
| Lower-cost candidates identifying | 0 |

## Scope

The result trades two readouts at one probe for one aggregate readout across
three probes. It does not show that hidden state generically requires an
additional readout channel, internal access, a future-response feature, or a
belief estimator.
