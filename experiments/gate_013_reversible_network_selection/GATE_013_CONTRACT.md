# Gate 013 — Reversible Selection and Network Propagation

**Gate:** Factorization  
**Status:** frozen Gate 1 contract  
**Question:** Can a joint, target-level distinction between reversible
selection and externally observable authority propagation be identified through
a finite behavioral intervention interface?

## Scope

This is the smallest joint Alexi/Jim class. It is not an adaptive-intelligence
architecture, a correctability estimator, or a downstream engineering result.
It contains neither noise, hidden state, delay, drift, learned graph rewiring,
nor a claim about real neural or organizational systems.

## Declared system class \(F_{RS}\)

The executable class is a Cartesian product of two binary labels, not a
simulated mechanism graph. Every record shares the same baseline value. The
finite class has four members:

| Identifier | Selection label | Influence-topology label |
|---|---|---|
| delete_independent | permanently delete a suppressed alternative | local influence only |
| delete_propagating | permanently delete a suppressed alternative | local evidence changes a downstream behavioral response |
| reversible_independent | retain a suppressed alternative so it can regain influence | local influence only |
| reversible_propagating | retain a suppressed alternative so it can regain influence | local evidence changes a downstream behavioral response |

The label names refer to a planned future dynamic experiment: phase-A
suppression, a post-suppression reversal phase included in the Gate 1
interface, and a contrasted local-to-downstream intervention. None of those
dynamics is simulated here. The generator contains no suppression, recurrence,
authority redistribution, graph edges, propagation, downstream cancellation,
or relearning.

The selection-policy flag, topology flag, authority weights, edge list, and
architecture label are excluded from the interface.

## Declared target \(L_{RS}\)

\[
L_{RS}(f)=\left(R_{\mathrm{reopen}}(f),K_{\mathrm{flow}}(f)\right).
\]

In this class, the components are aliases for the labels:

\[
R_{\mathrm{reopen}}=\mathbf 1[\text{selection label}=\text{reversible}],
\qquad
K_{\mathrm{flow}}=\mathbf 1[\text{topology label}=\text{propagating}].
\]

- \(R_{\mathrm{reopen}}\) is one exactly when a mechanism suppressed in phase
  A regains behavioral influence after the phase-B reversal.
- \(K_{\mathrm{flow}}\) is the stipulated binary downstream-response label.
  It is not yet an estimated causal effect from contrasted interventions.

The target is a finite-class operational target. It does not define a general
authority variable or a universal notion of diversity preservation.

## Frozen interface ladder

The allowed behavioral readouts are:

| Readout | Experimental content |
|---|---|
| baseline | current performance before the intervention sequence |
| reversal_recovery | phase-B recovery after phase-A suppression and reversal |
| downstream_flow | node-3 behavioral response after a local contradiction at node 1 |

The frozen ladder requires the constant baseline control in every active
protocol: baseline alone, baseline plus each individual probe, and baseline
plus both probes. A scalar readout is one protocol resource.

## Cost accounting

The minimum identifying member of the frozen mandatory-baseline ladder has
protocol cost three:

\[
C_{\mathrm{protocol}}^*=3.
\]

The baseline is constant over \(F_{RS}\) and contains no target information.
Removing that mandatory control leaves the target-relevant projection

\[
O_{\mathrm{informative}}=(\text{reversal recovery},\text{downstream flow}),
\qquad C_{\mathrm{target\text{-}relevant}}^*=2.
\]

The cost-three result is therefore a property of the frozen protocol ladder,
not a claim that three informative scalar readouts are necessary. The
cost-two statement is minimal only within the predeclared binary probe
coordinates. An unrestricted scalar could encode all four target values; such
encodings are outside this audit.

## Constructive scope

In this operational class, the readouts are direct aliases:

\[
O_R=R_{\mathrm{reopen}},
\qquad
O_K=K_{\mathrm{flow}}.
\]

Consequently,

\[
\widehat L(1,r,k)=(r,k).
\]

Factorization is constructively true by design once both probes are available.
The gate demonstrates reproducible interface composition, not discovery of a
nontrivial adaptive-system invariant. A scientifically stronger class must
allow policy labels and operational outcomes to dissociate.

## Pass/fail rule

The target passes Gate 1 under an interface \(O\) only if

\[
O(f_a)=O(f_b)\Longrightarrow L_{RS}(f_a)=L_{RS}(f_b)
\qquad\forall f_a,f_b\in F_{RS}.
\]

A counterexample stops the branch for that interface. The audit must preserve
the counterexample rather than add an estimator or change the target after
inspection.

## Predeclared expectations

- baseline fails: all four systems have the same current performance.
- baseline plus reversal recovery fails: it cannot distinguish independent
  from propagating topology at fixed reopenability.
- baseline plus downstream flow fails: it cannot distinguish deletion from
  reversible selection at fixed flow.
- the combined interface identifies the two-component target in this finite
  class.

The final item is a Gate 1 finding only. Estimation, held-out prediction, and
mechanism intervention remain closed even if factorization succeeds.

## Reproduction

    python experiments/gate_013_reversible_network_selection/run_gate_013.py \
      --write experiments/results/gate_013_reversible_network_selection/factorization_audit.json