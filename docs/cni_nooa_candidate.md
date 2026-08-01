# CNI / NOOA Candidate Integration Plan

## Status

CNI / NOOA is a candidate implementation substrate.

It is not currently:

* a verified adaptive-intelligence architecture;
* a proof of residual agency;
* a formal definition of nontransitivity;
* evidence that (C_{\mathrm{improve}}) increases;
* a closure of the framework’s open obligations.

Its present value is narrower:

[
\boxed{
\text{CNI / NOOA provides an executable surface on which proposed invariants can be represented, violated, tested, and audited.}
}
]

## Current research stack

```text
Established adaptive testing and diagnosis theory
        ↓
Protocol Foundations
        ↓
Interface and target preservation
        ↓
Recursive generator-modification audit
        ↓
CNI / NOOA candidate implementation substrate
        ↓
Externally grounded falsification
```

CNI must remain downstream of the current hostile audit.

It should not determine the theory’s primitives or be treated as evidence for theoretical novelty.

---

# Phase 1 — Preserve the proposal without adopting it

Create:

```text
docs/cni_nooa_candidate.md
```

The document should:

* credit and preserve Jim’s proposal;
* distinguish Jim’s CNI interpretation from the underlying NOOA implementation framework;
* map proposed classes and methods to candidate adaptive mechanisms;
* identify executable hypotheses;
* list every unverified assumption;
* distinguish software contracts from externally validated invariants;
* state that no existing frozen result is changed.

Use the status:

> Candidate implementation architecture. Unvalidated and non-canonical.

Use the central claim:

> CNI provides a candidate executable substrate for testing residual-agency and recursive-adaptation hypotheses.

Do not claim:

> CNI closes the open obligations.

Do not add CNI to the canonical theory stack, evidence ledger, or frozen gate registry.

---

# Phase 2 — Wait for the recursive generator-modification audit

The audit must first determine whether the higher-order structure

[
G_{t+1}=\Gamma(G_t,\Omega_t)
]

is already contained in meta-learning, adaptive control, evolutionary computation, self-modifying systems, or neighboring fields.

CNI should then be interpreted according to the audit result.

## If verdict A: already contained

Treat CNI as an engineering realization of established higher-order adaptive mechanisms.

No theoretical elevation is warranted.

## If verdict B: structural remainder survives

Treat CNI as one candidate substrate for testing that remainder.

Do not assume CNI uniquely implements it.

## If verdict C: object underspecified

Do not build the runtime yet.

First determine the minimum missing operational definitions.

---

# Phase 3 — Build the smallest CNI runtime

Only after evaluating the audit, construct a minimal runtime:

```text
cni_runtime/
    controller.py
    network.py
    intelligence.py
    fabric.py
    contracts.py
    tests/
```

## Minimal responsibilities

### Controller

```text
state
propose_change()
record_consequence()
```

### Network

```text
route_change()
apply_transition()
record_provenance()
```

### Intelligence

```text
generate_candidate()
evaluate_observation()
revise_generator()
```

### Fabric

```text
hold shared execution state
apply accepted changes
preserve audit traces
reject explicitly defined violations
```

### Contracts

```text
validate declared types
check operational predicates
raise explicit failures
```

The initial runtime should implement only:

[
\text{state}
\rightarrow
\text{proposed change}
\rightarrow
\text{execution}
\rightarrow
\text{consequence}
\rightarrow
\text{generator update}.
]

It should not attempt to implement the full conceptual architecture.

---

# Explicit exclusions

Do not initially implement:

## EMI correspondence

```text
Controller ↔ Energy
Network ↔ Matter
Intelligence ↔ Information
```

This remains an analogy until it produces defined mappings and distinct predictions.

## KAM, Diophantine, parity, or Majorana protection

These terms must not become fields or class names unless equations specify:

* the represented mathematical object;
* its causal role;
* the protected quantity;
* the assumptions required;
* the measurable failure condition.

## Undefined nontransitivity

Do not implement:

```python
assert nontransitive()
```

until the relation, carrier set, temporal semantics, and violation witness are operationally defined.

## Self-reported improvement

Do not treat:

```python
after.c_improve > before.c_improve
```

as evidence of improvement.

That establishes only that an internal variable changed.

---

# Phase 4 — Connect the runtime to external falsification

The first meaningful experiment should ask:

> Can consequence feedback modify the mechanism that generates future adaptations, and does that modification improve performance under held-out environmental changes?

Compare at least:

```text
System A: fixed optimizer
System B: generator-modifying CNI runtime
System C: internally consistent pseudo-CNI disconnected from consequences
```

Hold constant:

* environment;
* compute budget;
* observation access;
* action budget;
* initial mechanism family;
* evaluation protocol.

Measure:

* recovery after regime change;
* adaptation latency;
* held-out generalization;
* retention of useful mechanisms;
* resistance to internally inflated improvement scores;
* changes in reachable future mechanisms;
* externally measured future viability.

The central intervention is not whether the system changes behavior:

[
\Delta P\neq0.
]

It is whether consequences alter the machinery producing future changes:

[
\boxed{
G_{t+1}=\Gamma(G_t,\Omega_t)
}
]

and whether that alteration produces externally validated improvement:

[
\boxed{
C_{\mathrm{improve},t+1}

>

C_{\mathrm{improve},t}.
}
]

---

# Scientific interpretation

CNI may provide:

* visible state;
* executable update paths;
* explicit failure surfaces;
* provenance records;
* restartable experiments;
* testable mechanism boundaries.

It cannot, by itself, establish:

* measurement validity;
* reality coupling;
* residual agency;
* improved future viability;
* nontransitivity;
* theoretical novelty.

The complete chain must remain:

[
\boxed{
\text{candidate invariant}
\rightarrow
\text{operational target}
\rightarrow
\text{protocol-generated observation}
\rightarrow
\text{valid interface}
\rightarrow
\text{runtime mechanism}
\rightarrow
\text{external falsification}.
}
]

## Decision rule

CNI deserves theoretical elevation only if experiments show that a precisely defined CNI mechanism produces a reproducible effect that:

1. cannot be explained by ordinary policy optimization;
2. depends causally on consequence-grounded generator modification;
3. survives held-out environments and adversarial controls;
4. corresponds to an operationally valid adaptive target.

Until then:

[
\boxed{
\text{CNI / NOOA = candidate implementation scaffold.}
}
]
