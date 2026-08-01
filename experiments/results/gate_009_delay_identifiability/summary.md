# Gate 009 — Delay Identifiability v0.1

**Execution status:** executed  
**Identifiability result:** conditional positive at lag one  
**Decision:** record temporal alignment as a separate interface resource.

## Declared class

(F_D) is the frozen (F_0) response class with a known fixed one-step delay:
lag-zero responses are zero and the ordinary (F_0) response appears at lag
one.

## Result

The inherited immediate interface is non-identifying. The original spatial
minimum regains identifiability when sampled one step later:

\[
I^*_{F_D}=\{e=-1\}\times\{r_1,r_2\}\times\{\lambda=1\}.
\]

| Quantity | Value |
|---|---:|
| Timed interfaces evaluated | 100 |
| Target-identifying interfaces | 26 |
| Minimum scalar cost | 2 |
| Required observation lag | 1 |
| Lower scalar-cost candidates identifying | 0 |

## Scope

This is not a delay sweep, an additive cost law, or a claim about arbitrary
delayed dynamics. It isolates temporal misalignment in one declared fixed-delay
class.
