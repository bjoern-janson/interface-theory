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

Each system has three candidate mechanisms arranged in a fixed directed
dependency graph. Every system shares the same baseline current performance.
The finite class has four members:

| Identifier | Selection policy | Influence topology |
|---|---|---|
| delete_independent | permanently delete a suppressed alternative | local influence only |
| delete_propagating | permanently delete a suppressed alternative | local evidence changes a downstream behavioral response |
| reversible_independent | retain a suppressed alternative so it can regain influence | local influence only |
| reversible_propagating | retain a suppressed alternative so it can regain influence | local evidence changes a downstream behavioral response |

Phase A supplies evidence favoring mechanism 1 and suppressing mechanism 2.
Phase B is a held-out reversal in which mechanism 2 becomes useful. A local
contradiction is separately applied to mechanism 1, and the externally visible
behavioral consequence at mechanism 3 is read.

The selection-policy flag, topology flag, authority weights, edge list, and
architecture label are excluded from the interface.

## Declared target \(L_{RS}\)

\[
L_{RS}(f)=\left(R_{\mathrm{reopen}}(f),K_{\mathrm{flow}}(f)\right).
\]

- \(R_{\mathrm{reopen}}\) is one exactly when a mechanism suppressed in phase
  A regains behavioral influence after the phase-B reversal.
- \(K_{\mathrm{flow}}\) is one exactly when a contradiction applied at node 1
  produces an externally visible downstream response at node 3; otherwise it
  is zero.

The target is a finite-class operational target. It does not define a general
authority variable or a universal notion of diversity preservation.

## Frozen interface ladder

The allowed behavioral readouts are:

| Readout | Experimental content |
|---|---|
| baseline | current performance before the intervention sequence |
| reversal_recovery | phase-B recovery after phase-A suppression and reversal |
| downstream_flow | node-3 behavioral response after a local contradiction at node 1 |

The frozen ladder is the baseline alone, baseline plus each individual probe,
and baseline plus both probes. A scalar readout is one interface resource.

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
