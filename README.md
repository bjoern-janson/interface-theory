# Interface Theory

A benchmark framework for studying **representation sufficiency, identifiability, and adaptive validity**.

---

## Core Question

> What information must an interface preserve for a system to remain predictive and causally competent?

Most machine learning systems are evaluated on whether they can produce correct outputs.

Interface Theory asks a different question:

> Does the system preserve the information required for correctness when the environment changes?

A representation is not evaluated only by current accuracy, but by whether it maintains access to distinctions that remain important under future conditions.

---

# Overview

The framework studies progressively harder environments where representations can fail.

Linear
|
v
Hidden State
|
v
Delay
|
v
Stochastic
|
v
Nonstationary
|
v
Adaptive

Each environment introduces a new failure mode.

---

# Core Formalism

A system contains:

- A latent state `x`
- An observation interface `O_I`
- A target variable `L`

The interface transforms the available information:

x → O_I(x) → prediction

A sufficient interface satisfies:

\[
P(L|x)=\hat{P}(L|O_I(x))
\]

Meaning:

The interface preserves everything needed to predict the target.

---

# Failure Condition

An interface fails when it merges states that require different predictions.

Formally:

\[
O_I(x_A)=O_I(x_B)
\]

but:

\[
P(L|x_A)\neq P(L|x_B)
\]

The interface created a false equivalence.

---

# Benchmark Environments

## 1. Linear Identifiability

Directory:

examples/F0_linear/

### Question

Can the interface preserve predictive information in simple deterministic systems?

### Failure mode

Representation collapse.

Two states become identical after compression despite requiring different outputs.

---

## 2. Hidden State Identifiability

Directory:

examples/hidden_state/

### Question

Can the interface recover information that is not directly observable?

### Failure mode

Latent variable omission.

The observation does not contain the complete state.

The system must infer hidden structure through history or belief.

---

## 3. Delay Identifiability

Directory:

examples/delay/

### Question

What happens when useful information arrives too late?

### Failure mode

Temporal misalignment.

The correct information exists, but not at the moment decisions must be made.

---

## 4. Stochastic Identifiability

Directory:

examples/stochastic/

### Question

Does the interface preserve uncertainty?

### Failure mode

Distribution collapse.

Two states may have similar observations but different probability distributions over future outcomes.

---

## 5. Nonstationary Identifiability

Directory:

examples/nonstationary/

### Question

Can a system recognize when its own assumptions become invalid?

### Failure mode

Validity collapse.

The environment changes:

P(x_next | x)

becomes:

P(x_next | x, z)

where `z` represents the active regime.

A previously correct model becomes obsolete.

---

# Repository Structure

.
├── examples/
│ ├── F0_linear/
│ ├── hidden_state/
│ ├── delay/
│ ├── stochastic/
│ └── nonstationary/
│
├── experiments/
│ └── results/
│
├── docs/
│ └── roadmap.md
│
└── README.md

---

# Experimental Gates

The benchmark is organized around validation gates.

gate_001 → linear identifiability
gate_002 → hidden state
gate_003 → temporal delay
gate_004 → stochastic uncertainty
gate_005+ → increasingly adaptive environments

Each gate contains:

- System definition
- Candidate interfaces
- Target variables
- Factorization checks
- Counterexamples
- Trace analysis
- Minimal interface search

---

# Interface Hierarchy

Different environments require different preserved information.

| Environment | Minimal Information |
|---|---|
| Linear | Relevant state variables |
| Hidden State | Latent state belief |
| Delay | Temporal alignment |
| Stochastic | Uncertainty structure |
| Nonstationary | Regime validity |

The required interface grows as the environment becomes more dynamic.

---

# Key Insight

A representation can be:

- accurate,
- compact,
- computationally efficient,

and still fail if it removes information needed for future adaptation.

The important question is not only:

> "Does this representation predict?"

but:

> "Does this representation preserve the ability to know when its predictions stop being valid?"

---

# Research Direction

Future phases investigate adaptive interfaces.

The next question:

> Can a system discover that its representation is insufficient and modify the representation itself?

This requires:

- representation expansion,
- hypothesis generation,
- self-monitoring,
- structural correction,
- long-horizon adaptation.

---

# Roadmap

See:

docs/roadmap.md

for the complete development path.

---

# Status

Current completed benchmarks:

- ✓ Linear identifiability
- ✓ Hidden state identifiability
- ✓ Delay identifiability
- ✓ Stochastic identifiability
- ✓ Nonstationary identifiability

Current research phase:

**Adaptive Interface Systems**

---

# License

Research prototype.

Use, modify, and extend for experimental investigation.
