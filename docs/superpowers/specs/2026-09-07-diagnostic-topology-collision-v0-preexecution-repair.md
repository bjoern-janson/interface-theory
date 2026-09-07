# Diagnostic Topology Collision V0 — Pre-Execution Formal Repair Authority Addendum

**Status:** process/provenance addendum only.

**Scientific standing:** `NOT_EVIDENCE`

**Canonical standing:** no canonical Interface Theory artifact is modified or promoted by this addendum.

## 1. Purpose

This addendum records why `DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md` was reopened and refrozen **before any execution**.

It authorizes only a bounded documentation-level formal repair of the existing finite construction. It does not authorize implementation, execution, interpretation beyond the repaired claim ceiling, V1 work, canonical promotion, or any Interface Theory ↔ MATRIX translation.

## 2. Prior lineage

The original cross-program seed planting was completed before DTC-V0 was introduced.

The subsequent DTC sequence was:

```text
first planting completed
        ->
repair-aware bridge exposed the need for a finite nonempty/disjoint viable-policy witness
        ->
DTC-V0 finite construction frozen at 1a5eeeef68db57db31823d43a4392c35e52cb1a5
        ->
DTC-V0 indexed at 27255e1a61cf8c95a660051f7d971c535a06b38c
        ->
pre-execution formal review found two typing defects
        ->
this bounded repair/refreeze
```

No DTC-V0 implementation or execution occurred between the original freeze and this refreeze.

## 3. Defect A — syntactic singleton viable-policy claim

The original text asserted:

```math
\mathcal C_Q(G_A)=\{\pi_A\},
\qquad
\mathcal C_Q(G_B)=\{\pi_B\}.
```

That equality was stronger than the declared policy language warranted. A total policy can agree with `\pi_A` or `\pi_B` on every history reachable in the relevant world while differing on unreachable histories.

The repaired statement is therefore:

```math
\forall\pi\in\mathcal C_Q(G_A),\quad \pi(\epsilon)=q_A,
```

and:

```math
\forall\pi\in\mathcal C_Q(G_B),\quad \pi(\epsilon)=q_B.
```

Concrete policies `\pi_A` and `\pi_B` witness nonemptiness. Because one deterministic policy cannot have both distinct initial actions, the required result still follows:

```math
\mathcal C_Q(G_A)\neq\varnothing,
\qquad
\mathcal C_Q(G_B)\neq\varnothing,
\qquad
\mathcal C_Q(G_A)\cap\mathcal C_Q(G_B)=\varnothing.
```

No quotient over unreachable behavior is required.

## 4. Defect B — wrong causal noun

The original text said the representation intervention changed bounded corrective **policy availability**.

But the viable-policy classes are fixed by the hidden world plus the declared action, repair, cost, and budget contract before `g_0` and `g_1` are applied.

The intervention instead changes:

```math
\boxed{
\text{whether the controller-visible representation exposes enough topology information to select the required viable policy.}
}
```

The repaired distinction is:

```math
\boxed{
\text{policy existence}
\neq
\text{policy selectability from exposed information}.
}
```

Accordingly, the strongest V0 causal line becomes:

```text
representation distinction
    -> viable-policy selection
    -> bounded repair consequence
```

not a claim that `g_1` creates policies that did not otherwise exist.

## 5. Execution standing

The finite counts and contrast are analytically determined by the construction:

```math
P_{\rm success}(g_0)=\frac12,
\qquad
P_{\rm success}(g_1)=1,
\qquad
\Delta P_{\rm success}=\frac12.
```

Therefore a future executable run can establish only conformance of an implementation to the frozen finite construction.

The legal interpretation is:

```text
analytic finite witness established
        ->
executable conformance test
        ->
exact predicted finite behavior reproduced
```

or else implementation/protocol failure.

Do not describe exact reproduction as empirical discovery or independent confirmation of the already-derived effect.

## 6. Authorized changes in this refreeze

Exactly these changes are authorized:

```text
1. define the viable-policy class sufficiently to avoid singleton overclaim;
2. prove nonempty/disjoint viability through incompatible required initial actions;
3. replace policy-availability language with controller-visible viable-policy selectability;
4. retype the finite object as a DERIVED_MATHEMATICAL_OBSERVATION with executable conformance pending;
5. update the research-seed README so navigation and claim language match the repaired object;
6. record this process/provenance addendum.
```

No world, diagnostic, fault, repair, cost, budget, raw history, encoder, controller, analytic count, or downstream claim ceiling is otherwise changed.

## 7. Explicit non-authorization

This addendum does **not** authorize:

```text
DTC-V0 implementation
DTC-V0 execution
scientific-result recording
canonical Interface Theory updates
MATRIX updates
Interface Theory ↔ MATRIX translation
V1 execution or promotion
persistent-interface claims
corrigibility claims
```

A separate explicit authorization is required before any DTC-V0 executable conformance run.

## 8. Refreeze identity

The commit containing this addendum together with the repaired `DIAGNOSTIC_TOPOLOGY_COLLISION_V0.md` and aligned research-seed README is the operative pre-execution V0 refreeze.

The original freeze at `1a5eeeef68db57db31823d43a4392c35e52cb1a5` remains part of the immutable Git history and should be cited when reconstructing how the formal typing changed before execution.
