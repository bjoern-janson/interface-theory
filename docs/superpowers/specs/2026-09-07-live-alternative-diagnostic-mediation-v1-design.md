# Live-Alternative Diagnostic Mediation V1 — Design

**Status:** approved design for a noncanonical, pre-execution research assay. No implementation or scientific execution is authorized by this document.

**Design branch:** `design/live-alternative-diagnostic-mediation-v1`

**Parent research branch:** `research/interface-matrix-seeds-2026-09-07`

**Parent branch anchor:** `27255e1a61cf8c95a660051f7d971c535a06b38c`

**Frozen V0 assay:** `DIAGNOSTIC_TOPOLOGY_COLLISION_V0` at commit `1a5eeeef68db57db31823d43a4392c35e52cb1a5`

**Canonical standing:** `NONCANONICAL_RESEARCH_SEED`

**Translation standing:** `NO_TRANSLATION_EARNED`

**Evidence standing before execution:** `EXPERIMENTAL_HYPOTHESIS` plus finite analytic consequences of the declared design. No empirical V1 result exists yet.

## 1. Purpose

V1 adds exactly one causal responsibility beyond V0.

V0 established the design target:

```text
representation distinction -> policy consequence
```

V1 asks whether a relation between already-retained unresolved alternatives can be converted into an information-producing action:

```text
relation between retained alternatives -> temporary mediation -> diagnostic action
```

The assay must not credit V1 for preserving alternatives. Both conditions already retain the same alternatives and the same per-alternative predictive information.

The new causal object is a temporary, intervention-local, read-only cross-alternative comparison.

```text
V1 does not test representation learning.
V1 does not test interface learning.
V1 does not test persistence.
V1 does not test reuse.
```

## 2. Central causal identity

The intended V1 causal chain is:

```text
two unresolved live alternatives
        |
        v
identical marginal predictive signatures
        |
        v
C0: no joint relation computation
or
C1: temporary read-only comparison
        |
        v
diagnostic selection from a fixed shared menu
        |
        v
external-world observation
        |
        v
resolution of the live pair
        |
        v
bounded terminal repair
```

The strongest design target is:

```math
\boxed{
\text{relation between retained alternatives}
\longrightarrow
\text{information-producing action}
}
```

No stronger architectural or learning claim is part of V1.

## 3. Non-negotiable invariants

The assay must satisfy all of the following.

1. Both alternatives remain live before external evidence.
2. The diagnostic menu is fixed and shared across conditions.
3. The informative diagnostic is pair-dependent; no universal diagnostic solves every positive pair.
4. The mediator cannot modify either alternative before external evidence.
5. No pair identity, model identity, creation order, memory address, hash, or other identity side channel is available to diagnostic selection.
6. The live pair is treated as unordered; mediation is permutation invariant.
7. C0 and C1 contain identical per-alternative predictive information.
8. Only C1 contains a pre-action computational node with both alternatives as causal parents.
9. A live pair with no available discriminating diagnostic must yield `NO_DISCRIMINATING_DIAGNOSTIC` in the mediation condition.
10. The useful diagnostic must not be inferable from either endpoint alone in the positive family.
11. No parameter update, persistent interface state, or cross-episode memory is created by mediation.
12. Execution, if later authorized, must be exhaustive over the frozen finite family rather than treated as a sampling study.

These are structural requirements, not implementation suggestions.

## 4. Shared diagnostic menu

The declared diagnostic action set is:

```math
\mathcal U_{\rm diag}=\{q_0,q_1\}.
```

No condition may synthesize a diagnostic outside this set.

```math
q^\star\in\mathcal U_{\rm diag}
```

is allowed, while

```math
q^\star\notin\mathcal U_{\rm diag}
```

is a protocol violation.

V1 therefore tests diagnostic **selection**, not diagnostic invention or composition.

## 5. Positive model family: the four-model square

Define four predictive models:

```math
\mathcal M^+
=
\{M_{00},M_{01},M_{10},M_{11}\}.
```

Their predictive signatures over the shared diagnostic menu are:

```math
S(M_{ab})=(a,b),
\qquad a,b\in\{0,1\},
```

so:

```math
\begin{aligned}
S(M_{00})&=(0,0),\\
S(M_{01})&=(0,1),\\
S(M_{10})&=(1,0),\\
S(M_{11})&=(1,1).
\end{aligned}
```

Equivalently:

```math
M_{ab}(q_0)=a,
\qquad
M_{ab}(q_1)=b.
```

The four positive live pairs are the four edges of the square:

```math
\begin{aligned}
E_0
&=
\big\{
\{M_{00},M_{10}\},
\{M_{01},M_{11}\}
\big\},\\[1mm]
E_1
&=
\big\{
\{M_{00},M_{01}\},
\{M_{10},M_{11}\}
\big\}.
\end{aligned}
```

Pairs in `E_0` disagree only on `q_0`.

Pairs in `E_1` disagree only on `q_1`.

The square diagonals

```text
{M00, M11}
{M01, M10}
```

are outside the V1 positive family because they disagree on both diagnostics and would destroy uniqueness of the required diagnostic.

## 6. Unique pair-dependent diagnostic

For each positive live pair `P={M_i,M_j}`, define the disagreement vector:

```math
d_{ij}
=
S(M_i)\oplus S(M_j),
```

where `\oplus` is componentwise XOR.

For every positive pair:

```math
d_{ij}\in\{(1,0),(0,1)\}.
```

Therefore the unique discriminating diagnostic is:

```math
\begin{aligned}
d_{ij}=(1,0)&\Rightarrow q^\star=q_0,\\
d_{ij}=(0,1)&\Rightarrow q^\star=q_1.
\end{aligned}
```

Formally:

```math
\forall P\in E_0\cup E_1,
\qquad
\exists!\,q^\star\in\mathcal U_{\rm diag}
:\
M_i(q^\star)\neq M_j(q^\star).
```

No diagnostic is universally informative across the positive family:

```math
\forall q\in\mathcal U_{\rm diag},
\qquad
\exists P\in E_0\cup E_1
:\
M_i(q)=M_j(q).
```

## 7. Endpoint non-identifiability of the useful diagnostic

The central square property is stronger than pair dependence alone.

Each model participates in one `q_0`-diagnostic pair and one `q_1`-diagnostic pair:

```text
M00: with M10 -> q0; with M01 -> q1
M01: with M11 -> q0; with M00 -> q1
M10: with M00 -> q0; with M11 -> q1
M11: with M01 -> q0; with M10 -> q1
```

Hence no individual endpoint determines the useful diagnostic.

There is no function of a single positive-family model signature that returns the correct diagnostic for every pair containing that model:

```math
\boxed{
q^\star=f(S_i,S_j),
\qquad
q^\star\neq f_i(S_i),
\qquad
q^\star\neq f_j(S_j)
}
```

for any endpoint-only functions that are required to succeed over the entire positive family.

The useful diagnostic is therefore information about the **relation** between the two live alternatives, not information carried by either endpoint alone.

## 8. Canonicalized marginal interface

Each alternative exposes only its predictive signature:

```math
S(M_i)=\big(M_i(q_0),M_i(q_1)\big).
```

No representation supplied to either condition may include:

```text
model ID
pair ID
pair class
creation order
memory address
object hash
hidden topology label
precomputed disagreement class
ordering-dependent metadata
```

The live pair is semantically unordered.

Any serialized or in-memory representation used later must canonicalize away irrelevant identity metadata and must be tested for permutation symmetry.

The scientific contrast is:

```text
same alternatives
+
same marginal predictive content
+
same diagnostic menu
+
same budget
+
same downstream resolver
+
different availability of joint relation computation
```

## 9. Control condition C0: isolated marginals, no joint causal parent

C0 retains both alternatives and their signatures, but the pre-action architecture contains no node that receives both marginal streams.

Schematic graph:

```text
S_i -> R_i

S_j -> R_j

q <- Pi_0
```

The isolated marginal readers may exist for matched storage, inspection, and audit, but neither reader may causally influence a pair-dependent diagnostic selector before action.

For the frozen reference implementation, `\Pi_0` is precommitted to:

```text
q0
```

before the live pair is instantiated.

This deterministic choice is arbitrary with respect to the symmetric square. A precommitted `q1` produces the same aggregate result. More generally, any pair-independent mixture over `q0` and `q1` has the same one-half positive-family diagnostic success under the uniform edge family.

C0 is intentionally strict. Allowing an arbitrary pre-action function

```math
F(S_i,S_j)
```

would itself introduce a joint mediator under another name and would invalidate the causal contrast.

## 10. Treatment condition C1: intervention-local comparison

C1 adds exactly one new pre-action causal structure:

```text
S_i ----> I_episode <---- S_j
                |
                v
               q*
```

Define:

```math
I_{ij}^{(\mathrm{episode})}
=
\operatorname{Compare}(S_i,S_j)
=
S_i\oplus S_j.
```

The comparator is:

- deterministic;
- stateless across episodes;
- read-only with respect to both alternatives;
- permutation symmetric;
- restricted to selecting from the frozen diagnostic menu;
- destroyed at episode termination.

Before external evidence:

```text
READ alternatives       yes
COMPARE alternatives    yes
SELECT diagnostic       yes
REWRITE alternatives    no
PERSIST comparison      no
UPDATE parameters       no
```

Formally:

```math
I_{ij}^{(\mathrm{episode})}(S_i,S_j)
=
I_{ij}^{(\mathrm{episode})}(S_j,S_i).
```

At episode termination:

```math
\boxed{
I_{ij}^{(\mathrm{episode})}\longrightarrow\varnothing
}
```

No persistent artifact from this comparison is available in the next episode.

## 11. Comparator output contract

The comparator's allowed outputs are determined by the disagreement vector.

```math
\begin{array}{rcl}
(1,0) &\Rightarrow& q_0,\\
(0,1) &\Rightarrow& q_1,\\
(0,0) &\Rightarrow& \texttt{NO\_DISCRIMINATING\_DIAGNOSTIC},\\
(1,1) &\Rightarrow& \texttt{OUT\_OF\_FROZEN\_FAMILY}.
\end{array}
```

The `(1,1)` case must not silently choose a diagnostic. It corresponds to excluded square diagonals or another protocol violation and is outside the frozen V1 family.

The mediator never outputs which alternative is true.

Its authorized role is only to select an information-producing action, or to certify that the frozen menu contains no discriminating diagnostic.

## 12. External evidence authority boundary

For a positive live pair

```math
P=\{M_i,M_j\},
```

exactly one member is instantiated as the true latent world:

```math
M_\tau\in P.
```

The mediator proposes a diagnostic:

```math
q^\star\in\mathcal U_{\rm diag}.
```

The external world then returns:

```math
\boxed{
o_{\rm world}=M_\tau(q^\star)
}
```

Because the positive pair disagrees on `q^\star`, the external observation resolves the live pair.

The authority sequence is therefore:

```text
mediator proposes intervention
        ->
world supplies observation
        ->
resolver updates which alternative remains viable
        ->
downstream controller executes repair
```

The mediator itself never promotes an alternative to truth and never collapses the live pair before external evidence.

## 13. Terminal repair contract

Assign every positive latent model a unique valid terminal repair:

```math
\mathcal U_{\rm repair}
=
\{r_{00},r_{01},r_{10},r_{11}\},
```

with:

```math
R(M_{ab})=\{r_{ab}\}.
```

Hence for any distinct live pair:

```math
R(M_i)\cap R(M_j)=\varnothing.
```

After a discriminating observation resolves `M_\tau`, the shared downstream resolver executes:

```math
r_\tau.
```

C0 and C1 use the same resolver and repair vocabulary.

## 14. Resource contract

Freeze total episode budget to:

```math
B=2.
```

Every diagnostic costs one unit:

```math
c(q_0)=c(q_1)=1,
```

and every terminal repair costs one unit:

```math
c(r)=1
```

for every declared repair.

A discriminating diagnostic yields:

```text
B = 1
+
live pair resolved
```

so the unique valid terminal repair remains executable.

A non-discriminating diagnostic yields:

```text
B = 1
+
live pair unresolved
```

and therefore no bounded zero-error continuation exists:

- immediately repairing cannot guarantee validity because the live alternatives require distinct repairs;
- running the other diagnostic consumes the last budget unit and leaves no budget for terminal repair.

Thus, under the frozen controller/resolver contract:

```math
\boxed{
q_{\rm nondisc}
\longrightarrow
(P=\{M_i,M_j\},B=1)
\longrightarrow
\text{no bounded zero-error continuation}.
}
```

This resource consequence is what connects diagnostic selection to bounded corrective outcome.

## 15. Positive finite assay

The positive family contains exactly four unordered live pairs.

Each pair is evaluated twice, once with each member instantiated as the true latent world:

```math
4\ \text{pairs}\times 2\ \text{true members}=8\ \text{positive episodes per condition}.
```

Use the uniform finite average over those eight episodes.

### 15.1 C0 analytic diagnostic result

The frozen C0 selector always emits `q0`.

`q0` is discriminating on the two `E_0` pairs and non-discriminating on the two `E_1` pairs.

Therefore:

```math
\boxed{
P_{\rm disc}(C_0)=\frac{4}{8}=\frac12.
}
```

The same aggregate result holds for a precommitted `q1` and for any pair-independent random mixture over the two diagnostics under the balanced positive family.

### 15.2 C1 analytic diagnostic result

The comparator returns the unique discriminating diagnostic for every positive edge.

Therefore:

```math
\boxed{
P_{\rm disc}(C_1)=\frac{8}{8}=1.
}
```

Hence:

```math
\boxed{
\Delta P_{\rm disc}=\frac12.
}
```

### 15.3 Repair consequence under the frozen controller/resolver contract

A correct diagnostic preserves exactly enough budget for external resolution plus the unique repair.

A non-discriminating diagnostic leaves no bounded zero-error continuation.

Therefore, under the stated C0/C1 controller and resolver contract:

```math
\boxed{
P_{\rm repair}(C_0)=\frac12,
\qquad
P_{\rm repair}(C_1)=1,
\qquad
\Delta P_{\rm repair}=\frac12.
}
```

These are analytic benchmark values implied by the frozen finite construction. They are not empirical surprises to be estimated after execution.

Any later executable assay would test whether the implementation faithfully instantiates this declared structure.

## 16. Null family: no available discriminating diagnostic

Introduce two additional latent worlds:

```math
N_0,
\qquad
N_1,
```

with identical predictive signatures over the frozen diagnostic menu:

```math
S(N_0)=S(N_1)=(0,0).
```

Give them distinct terminal repairs:

```math
R(N_0)=\{r_{N0}\},
\qquad
R(N_1)=\{r_{N1}\},
\qquad
r_{N0}\neq r_{N1}.
```

Then:

```math
\forall q\in\mathcal U_{\rm diag},
\qquad
N_0(q)=N_1(q).
```

The treatment comparator computes:

```math
d_{N0,N1}=(0,0)
```

and must return:

```text
NO_DISCRIMINATING_DIAGNOSTIC
```

The null target is **epistemic abstention**, not successful repair of an intentionally irresolvable pair.

The null verifies that the mediation mechanism does not fabricate useful disagreement or emit a probe merely because a probe is available.

The null family is not used to inflate the positive-family C0-vs-C1 repair contrast. Unless a separate null-control objective is preregistered later, its required scientific check is the C1 abstention behavior above.

The strongest local null interpretation is:

```text
within the frozen V1 family,
when the declared diagnostic menu exposes no pairwise discriminating intervention,
the temporary mediator reports that no such intervention is available.
```

Do not generalize this into a theorem that disagreement is useful if and only if it exists.

## 17. Anti-shortcut requirements

Any future implementation must include explicit checks that:

```text
no model ID reaches diagnostic selection
no pair ID reaches diagnostic selection
no endpoint alone determines the correct diagnostic over the positive family
pair order does not change mediator output
C0 contains no hidden joint function of S_i and S_j
C1's only extra pre-action dependency is the temporary joint comparison
no persistent mediator state crosses episode boundaries
no diagnostic outside {q0,q1} can be emitted
no positive episode contains a (0,0) or (1,1) disagreement vector
no null episode emits q0 or q1 in C1
```

A violation is a protocol failure, not a scientific result.

## 18. Required future result fields

If an implementation is later authorized, its result object should report at least:

```text
protocol_state
execution_state
positive_pair_count
positive_episode_count_per_condition
c0_discriminating_count
c1_discriminating_count
c0_repair_success_count
c1_repair_success_count
P_disc_C0
P_disc_C1
delta_P_disc
P_repair_C0
P_repair_C1
delta_P_repair
endpoint_nonidentifiability_verified
no_universal_diagnostic_verified
pair_order_invariance_verified
marginal_information_matched
joint_comparison_only_in_C1
read_only_mediator_verified
mediator_ephemeral_verified
shared_menu_verified
budget_matched
resolver_identity_matched
null_disagreement_vector
null_mediator_output
```

Expected positive-family values under the frozen design are:

```text
positive_pair_count = 4
positive_episode_count_per_condition = 8
c0_discriminating_count = 4
c1_discriminating_count = 8
c0_repair_success_count = 4
c1_repair_success_count = 8
P_disc_C0 = 0.5
P_disc_C1 = 1.0
delta_P_disc = 0.5
P_repair_C0 = 0.5
P_repair_C1 = 1.0
delta_P_repair = 0.5
endpoint_nonidentifiability_verified = true
no_universal_diagnostic_verified = true
pair_order_invariance_verified = true
marginal_information_matched = true
joint_comparison_only_in_C1 = true
read_only_mediator_verified = true
mediator_ephemeral_verified = true
shared_menu_verified = true
budget_matched = true
resolver_identity_matched = true
null_disagreement_vector = [0,0]
null_mediator_output = NO_DISCRIMINATING_DIAGNOSTIC
```

A mismatch in these predetermined finite values is an implementation or protocol failure unless a separately reviewed design change occurs before execution.

## 19. Claim ceiling

If a future implementation faithfully instantiates the frozen design, the strongest admitted V1 claim is:

```text
Within the frozen finite family,
temporary joint comparison of retained unresolved alternatives
can improve selection of an available discriminating intervention
and thereby preserve a bounded zero-error repair path
under the stated controller, resolver, and resource contract.
```

V1 does **not** establish:

```text
representation learning
discovery of which alternatives to retain
diagnostic invention
diagnostic composition
persistent interface state
interface learning
parameter adaptation
cross-episode reuse
held-out generalization
transfer
corrigibility
adaptive intelligence
recursive self-improvement
neural necessity of typed or separated streams
a general Interface Theory result
a general MATRIX result
an earned Interface Theory <-> MATRIX translation
```

The causal credit line is exactly:

```math
\boxed{
V1:\quad
\text{temporary relation between retained alternatives}
\longrightarrow
\text{information-producing action}
}
```

and nothing stronger.

## 20. Relationship to V0 and later rungs

The intended cumulative ladder remains:

```text
V0: representation distinction -> policy consequence
V1: relation between retained alternatives -> information-producing action
V2: temporary relation -> persistent learned interface
V3: persistent interface -> held-out reuse
V4: reuse -> reopening / correction
```

V1 assumes the live alternatives are already retained. It does not receive credit for that prerequisite.

V1's temporary comparator is constructed for the episode and then destroyed. It supplies no evidence for V2.

## 21. Engineering provenance boundary

The painting, generative-grammar discussion, transformer architecture discussion, state/prediction separation literature, Interface Theory, MATRIX, and prior cross-model critique are motivation and engineering/conceptual provenance for seeking this construction.

They are not premises required to derive the square's finite relation structure, analytic one-half contrast, resource consequence, or null abstention contract.

In particular, the state/prediction separation paper discussed during design supplies an engineering motif of separate streams plus constrained read access. V1 does not inherit that paper's scientific claims, and that paper does not validate unresolved-alternative mediation.

The scientific object in this design is the declared finite causal graph and resource contract above.

## 22. Implementation boundary

This document authorizes no implementation or execution.

The next legal process step after user approval of this committed design is to write an implementation plan.

The plan must preserve:

```text
four-model square
four positive unordered edges
two-diagnostic shared menu
endpoint non-identifiability
pair-order invariance
no identity leakage
C0 pair-blind fixed selector
C1 ephemeral read-only XOR comparison
external evidence authority boundary
B = 2 resource shell
unique terminal repairs
positive exhaustive 8-episode-per-condition evaluation
null abstention case
claim ceiling
```

No assay should be run in the same step as writing this design.
