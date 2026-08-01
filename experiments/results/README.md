# Experiment Results Archive v0.1

**Status:** Immutable execution archive  
**Parent:** Interface Theory v0.1

---

# Purpose

This directory contains executed experiment outputs.

Results are archival artifacts, not theory definitions.

The separation is:

\[
\text{theory}
\rightarrow
\text{protocol}
\rightarrow
\text{execution}
\rightarrow
\text{result}
\]

---

# Rules

## 1. Results are immutable

Once a gate is executed:

- outputs are preserved;
- failures are not overwritten;
- later interpretations belong in new documents.

---

## 2. Every result must map to a registered gate

Required metadata:

```json
{
  "gate_id": "",
  "protocol_version": "",
  "system_class": "",
  "target": "",
  "interface_family": "",
  "status": "",
  "decision": ""
}
# Result Status

Allowed values:

| Status | Meaning |
|--------|---------|
| **PASS** | Preregistered condition satisfied |
| **FAIL** | Preregistered failure condition reached |
| **BOUNDED** | Partial characterization only |
| **INVALID** | Protocol violation |
| **REPEATED** | Independently reproduced |

---

# Interpretation Boundary

Results may establish:

- Identifiability
- Non-identifiability
- Interface requirements
- Sample requirements
- Counterexamples
- Lower bounds

Results may **not** establish without later gates:

- Universal adaptive metrics
- Intelligence measures
- Engineering superiority
- Causal improvement mechanisms

---

# Current Highest Valid Layer

**Interface Theory**

The archive currently supports:

```text
(F, O, L)
      ↓
Factorization analysis
      ↓
Interface requirements
```

It does **not** support:

```text
Metric
   ↓
Capability score
```

---

# Reproducibility Requirement

Each result directory should contain:

- Frozen protocol reference
- Configuration
- Raw output
- Derived summary
- Validation tests
- Decision

---

# No Repair Rule

Failed gates are preserved as scientific results.

A failure does **not** authorize:

- Hidden parameter changes
- Interface changes
- Estimator tuning
- Benchmark redesign

Those require a new preregistered gate.
