# Diagnostic Topology Collision V0

**Protocol status:** `FROZEN_PRE_EXECUTION_ASSAY`

**Evidence standing:** `DERIVED_MATHEMATICAL_OBSERVATION` for the finite causal construction and analytic contrast.

**Execution role:** `EXECUTABLE_CONFORMANCE_TEST_PENDING`

**Translation standing:** `NO_TRANSLATION_EARNED`

**Canonical standing:** `NONCANONICAL_RESEARCH_SEED`

**Pre-execution repair lineage:** the original V0 text was frozen at `1a5eeeef68db57db31823d43a4392c35e52cb1a5` and indexed at `27255e1a61cf8c95a660051f7d971c535a06b38c`. No V0 execution occurred before the formal repair recorded in the commit containing this revision. The original freeze remains preserved in Git history; this revision is the operative pre-execution refreeze.

## 1. Identity

```text
DIAGNOSTIC_TOPOLOGY_COLLISION_V0
=
controlled representation intervention
+
two solvable hidden worlds
+
disjoint bounded viable-policy classes
```

The construction asks exactly one causal question:

```math
\boxed{
\text{Can preserving a policy-relevant topology distinction change the controller's ability to select a bounded viable policy, and therefore repair success?}
}
```

The representation is manipulated directly. V0 does **not** test whether a system can learn what distinction to preserve.

```text
V0 manipulates representation;
it does not credit an architecture for representation learning.
```

No learned interface, persistent adaptation, reuse, held-out transfer, or general corrigibility claim is part of this construction.

## 2. Self-contained finite world

There are two diagnostic-topology worlds:

```math
G_\tau,\qquad \tau\in\{A,B\},
```

and one unresolved binary fault:

```math
f\in\{0,1\}.
```

Define the topology bit

```math
t(A)=0,\qquad t(B)=1.
```

The primitive executable action vocabulary is shared exactly:

```math
\mathcal U=\{q_A,q_B,r_0,r_1\}.
```

The valid terminal repairs are:

```math
R(0)=\{r_0\},\qquad R(1)=\{r_1\}.
```

Therefore:

```math
R(0)\cap R(1)=\varnothing.
```

No state-independent terminal repair succeeds while the fault remains unresolved.

## 3. Diagnostic topology

In world `G_A`:

```math
q_A\mapsto f,
\qquad
q_B\mapsto\bot.
```

In world `G_B`:

```math
q_B\mapsto f,
\qquad
q_A\mapsto\bot.
```

The symbol `\bot` means that the probe consumed its declared resource cost but produced no usable fault value.

The two worlds differ only in which diagnostic reveals `f`. They have the same action vocabulary, repair semantics, budget, fault family, and controller.

## 4. Resource contract

Freeze the episode budget to:

```math
B=2.
```

Every diagnostic action costs one unit:

```math
c(q_A)=c(q_B)=1,
```

and every repair costs one unit:

```math
c(r_0)=c(r_1)=1.
```

A correct diagnostic leaves:

```math
B=1
```

with the fault value known, so `r_f` is executable and valid.

A wrong diagnostic leaves:

```math
B=1
```

with residual uncertainty

```math
S=\{0,1\}.
```

At that point:

- choosing a repair cannot guarantee success because `R(0)\cap R(1)=\varnothing`;
- choosing another diagnostic consumes the final budget unit and leaves no budget for repair.

Therefore:

```math
\boxed{
q_{\rm wrong}
\longrightarrow
(S=\{0,1\},B=1)
\longrightarrow
\text{no bounded zero-error continuation}.
}
```

The failure after a wrong probe is a declared resource-and-repair consequence, not a semantic convention that the episode simply stops.

## 5. Viable-policy collision

Let `\Pi` be the class of deterministic, history-dependent policies that map each legal finite action-observation history to a legal next action or `stop`, subject to the frozen action vocabulary and budget.

Let

```math
\mathcal C_Q(G)\subseteq\Pi
```

denote the policies that guarantee valid zero-error repair in world `G` for both possible fault values under the frozen budget and action contract.

Two concrete policies witness nonemptiness:

```math
\pi_A:
q_A\ \text{first};\ 
\text{if }q_A\text{ returns }y\in\{0,1\},\text{ execute }r_y,
```

and:

```math
\pi_B:
q_B\ \text{first};\ 
\text{if }q_B\text{ returns }y\in\{0,1\},\text{ execute }r_y.
```

Hence:

```math
\pi_A\in\mathcal C_Q(G_A),
\qquad
\pi_B\in\mathcal C_Q(G_B),
```

so both viable-policy classes are nonempty.

The stronger and sufficient collision statement is about the required initial action, not singleton syntax.

For every viable policy in `G_A`:

```math
\boxed{
\forall\pi\in\mathcal C_Q(G_A),
\qquad
\pi(\epsilon)=q_A.
}
```

Why: starting with `q_B` leaves no bounded zero-error continuation by Section 4; starting with `r_0`, `r_1`, or `stop` cannot guarantee valid repair for both possible faults.

Similarly:

```math
\boxed{
\forall\pi\in\mathcal C_Q(G_B),
\qquad
\pi(\epsilon)=q_B.
}
```

A deterministic policy has one initial action. Since `q_A\neq q_B`, no policy can satisfy both requirements. Therefore:

```math
\boxed{
\mathcal C_Q(G_A)\neq\varnothing,
\qquad
\mathcal C_Q(G_B)\neq\varnothing,
\qquad
\mathcal C_Q(G_A)\cap\mathcal C_Q(G_B)=\varnothing.
}
```

This argument does not require claiming that either viable-policy class is a syntactic singleton. Policies may differ on histories unreachable in a given world without affecting the collision proof.

Both hidden worlds are individually solvable. The collision is therefore not created by an intrinsically infeasible branch.

## 6. Raw history and matched one-bit representation intervention

Each episode has raw history:

```math
h=(t,n),
```

where:

- `t=t(\tau)` is the topology-relevant historical cue;
- `n\in\{0,1\}` is a nuisance bit;
- `n` is independent of `\tau` and `f`;
- `f` is not encoded in `h`.

For matched comparison pairs, use the same `n` in `G_A` and `G_B`:

```math
h_A=(0,n),
\qquad
h_B=(1,n).
```

Both experimental conditions receive the same raw history object. The intervention changes only which one-bit distinction survives compression.

### Compression condition

```math
g_0(h)=n.
```

For a matched pair:

```math
g_0(h_A)=g_0(h_B)=n.
```

The controller-visible state therefore collapses the topology distinction.

### Preservation condition

```math
g_1(h)=t.
```

Hence:

```math
g_1(h_A)=0,
\qquad
g_1(h_B)=1.
```

Both encoders retain exactly one bit.

```text
same raw history
+
same representational capacity
+
same action vocabulary
+
same budget
+
same controller
+
different retained information
```

The topology cue is present in the raw history supplied to **both** conditions. No treatment-only topology label or fault value is injected.

```math
\boxed{
\text{preserved topology information}
\neq
\text{revealed fault information}.
}
```

## 7. Fixed controller

The controller is identical across representation conditions.

For retained bit `b\in\{0,1\}`:

```text
if b = 0: choose q_A
if b = 1: choose q_B
```

If the diagnostic returns `y\in\{0,1\}`, execute:

```text
r_y
```

If the diagnostic returns `\bot`, no bounded zero-error continuation exists under Section 4.

The controller is not trained separately in the two arms. The only intervention is `g_0` versus `g_1`.

Crucially, the representation intervention does **not** change `\mathcal C_Q(G_A)` or `\mathcal C_Q(G_B)`. Those viable-policy classes are determined by the hidden world and frozen action/resource contract. The intervention changes whether the controller-visible representation exposes enough topology information to select the required viable initial action.

```math
\boxed{
\text{policy existence}
\neq
\text{policy selectability from exposed information}.
}
```

## 8. Finite exhaustive evaluation

V0 is a deterministic finite construction with a pending executable conformance test, not a sampling study.

Exhaustively enumerate:

```math
\tau\in\{A,B\},
\qquad
f\in\{0,1\},
\qquad
n\in\{0,1\}.
```

There are exactly:

```math
2\times2\times2=8
```

episodes per representation condition.

Use the uniform finite average over these eight episodes as the reported success probability.

### Analytic compression result

Under `g_0`, the controller sees `n`, which is independent of topology.

It chooses the topology-correct diagnostic exactly when:

```math
n=t(\tau).
```

That holds in four of eight episodes. Therefore:

```math
\boxed{
P_{\rm success}(g_0)=\frac{4}{8}=\frac12.
}
```

Equivalently, under the balanced topology prior, no randomized policy depending only on the collapsed topology-independent state can exceed one-half success:

```math
\frac12p+\frac12(1-p)=\frac12.
```

### Analytic preservation result

Under `g_1`, the controller receives the topology bit and always selects the required viable initial diagnostic. The diagnostic reveals `f`, after which `r_f` is executed.

Therefore:

```math
\boxed{
P_{\rm success}(g_1)=\frac{8}{8}=1.
}
```

### Frozen analytic contrast

```math
\boxed{
\Delta P_{\rm success}
=
P_{\rm success}(g_1)-P_{\rm success}(g_0)
=
1-\frac12
=\frac12.
}
```

This `1/2` contrast is already a derived property of the frozen finite construction. It is not a scientific effect waiting to be discovered by execution.

The legal interpretation of a future run is:

```text
analytic finite witness established
        ->
executable conformance test
        ->
exact predicted finite behavior reproduced or implementation/protocol failure
```

Do not describe exact reproduction as empirical discovery or independent confirmation of the already-derived `1/2` effect.

## 9. Required result fields for any implementation

A future executable implementation must report at least:

```text
protocol_state
total_worlds
success_count_g0
success_count_g1
wrong_probe_count_g0
wrong_probe_count_g1
P_success_g0
P_success_g1
delta_P_success
viable_policy_initial_action_collision_verified
controller_selectability_effect_verified
raw_history_equal_across_conditions
representation_capacity_matched
controller_identity_matched
primitive_actions_matched
budget_matched
```

The frozen expected values are:

```text
total_worlds = 8
success_count_g0 = 4
success_count_g1 = 8
wrong_probe_count_g0 = 4
wrong_probe_count_g1 = 0
P_success_g0 = 0.5
P_success_g1 = 1.0
delta_P_success = 0.5
viable_policy_initial_action_collision_verified = true
controller_selectability_effect_verified = true
raw_history_equal_across_conditions = true
representation_capacity_matched = true
controller_identity_matched = true
primitive_actions_matched = true
budget_matched = true
```

Any mismatch is an implementation failure or protocol violation, not a surprising scientific result.

## 10. Causal interpretation if faithfully instantiated

The intended causal graph is:

```text
same raw history
        |
        v
controlled representation intervention: g0 vs g1
        |
        v
retained one-bit topology distinction
        |
        v
controller ability to select the world-viable initial diagnostic
        |
        v
fault observation or failure to observe fault
        |
        v
bounded repair success
```

The intervention does not create or destroy the viable policies of either hidden world. It changes whether the fixed controller can select the viable initial action from its exposed representation.

The strongest admitted V0 statement is:

```text
Under the frozen two-world contract, preserving a policy-relevant topology distinction causally changes the controller's ability to select a bounded viable diagnostic policy, and thereby repair success.
```

This statement is a property of the declared finite construction. A future faithful execution may establish implementation conformance to that construction; it does not upgrade the result into a general empirical mechanism claim.

## 11. Claim ceiling

V0 does **not** establish:

- representation learning;
- discovery of which distinction should be preserved;
- learned interface construction;
- temporary mediation between unresolved alternatives;
- persistent adaptation;
- reusable interface learning;
- held-out generalization;
- transfer;
- adaptive intelligence;
- recursive self-improvement;
- general corrigibility;
- a general Interface Theory result;
- a general MATRIX result;
- an earned translation between source programs.

In particular:

```math
\boxed{
V0:\quad
\text{representation distinction}
\longrightarrow
\text{viable-policy selection}
\longrightarrow
\text{bounded repair consequence}
}
```

and nothing stronger.

## 12. Downstream ladder

The conceptual downstream ladder remains separate:

```text
V0: representation distinction -> viable-policy selection -> bounded repair consequence
V1: unresolved alternatives -> temporary mediation
V2: temporary mediation -> persistent interface
V3: persistent interface -> held-out reuse
V4: reuse -> reopening / correction
```

Each rung adds a new causal responsibility and requires a separately frozen design and assay.

V0 supplies no evidence for any downstream rung.

## 13. Provenance boundary

The painting, generative-grammar discussion, transformer architecture hypothesis, Interface Theory, MATRIX, and prior model critique explain why this finite construction was sought.

They are not premises required to derive V0's finite viable-policy collision or analytic `1/2` contrast.

The scientific object in this file is the declared finite state/action/resource construction itself.

## 14. Pre-execution repair boundary

The formal repair in this revision changes no world, action, cost, budget, representation, controller, or analytic count. It repairs only the scientific typing of the already-declared construction:

```text
syntactic singleton viable-policy claim
    ->
nonempty viable-policy classes with incompatible required initial actions
```

and:

```text
policy availability
    ->
controller-visible viable-policy selectability
```

No V0 implementation or execution is authorized by this repair. The execution gate remains separately controlled.
