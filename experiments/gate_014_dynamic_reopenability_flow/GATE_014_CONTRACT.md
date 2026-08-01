# Gate 014 — Cross-Context Dynamic Factorization

**Gate:** Factorization  
**Status:** frozen-before-execution Gate 1 contract  
**Protocol:** `CROSS_CONTEXT_DYNAMIC_FACTORIZATION_v0.1`  
**Question:** Do behavioral intervention assays at identification contexts
identify reopenability and signed authority flow in a disjoint target context
over a finite dynamic class?

## Scientific boundary

Gate 013 established direct operational projection composition by construction.
Gate 014 removes those aliases. Architecture labels, latent coefficients,
internal state, and target-assay outputs are unavailable to the interface.
Both the interface and target are generated independently from one shared set
of deterministic rational dynamics.

This remains a finite-class factorization test. A pass establishes finite
target-preserving compression only. It does not establish an estimator, a
simple or generalizable law, predictive validity, mechanism efficacy, or an
adaptive-intelligence architecture.

## Procedural independence

An exact finite contract mathematically entails an audit outcome. Therefore,
"the contract does not imply a verdict" is not a coherent requirement. The
frozen requirement is procedural:

- no parameter value, legal-combination rule, context, probe, class member,
  deduplication step, or target definition may be selected using observed
  equivalence classes or a desired verdict;
- the full legal parameter image is generated before observations or targets
  are partitioned;
- no class member is filtered using an observation, target, collision, or
  audit result;
- generator validity is decided before the factorization verdict;
- a failed interface is preserved rather than patched.

The expected minimum interfaces below are an analytic preregistration derived
from the shared affine response family. Execution audits every frozen subset
and may invalidate that expectation; the implementation is not to be changed
after the contract is frozen.

## Declared parameter space

Each parameter tuple is

\[
\theta=(S,u_R,c_R,G,u_K,c_K).
\]

The selection label and hidden reserve are:

| \(S\) | \(m_S\) | legal \(u_R\) |
|---|---:|---:|
| `delete` | \(0\) | \(0,\frac14\) |
| `reversible` | \(1\) | \(-\frac14,0\) |

For both labels,

\[
c_R\in\left\{-\frac18,0,\frac18\right\}.
\]

The topology label and declared primary-path coefficient are:

| \(G\) | \(p_G\) | legal \(u_K\) |
|---|---:|---:|
| `independent` | \(0\) | \(-1,0,1\) |
| `propagating` | \(1\) | \(-2,-1,0\) |

For both labels,

\[
c_K\in\{-1,0,1\}.
\]

There are no target bits, assay outcomes, collision flags, target-context-only
coefficients, or post-audit exclusions in \(\theta\). The exact Cartesian
image contains

\[
|\Theta_{014}|=12\times18=216
\]

parameter tuples. Full internal-trajectory signatures must also be unique, so
the declared system class must satisfy

\[
|F_{014}|=216.
\]

If this fails, execution is `INVALID_GENERATOR`, not a scientific verdict.

## Shared state and transition equations

All assays use fresh clones of the same post-suppression state. Context is a
numeric input

\[
c\in\{-1,0,+1\};
\]

the implementation may not branch on assay names or on whether a context is
used for identification or target evaluation.

### Reopenability subsystem

At the end of the suppression phase,

\[
A_0=0,\qquad M=m_S.
\]

The observable suppression and passive trajectories are fixed across all
systems; \(M\) is excluded from the interface. Under reversal input
\(u\in\{0,1\}\), define the shared rate

\[
v_R(c,u)=u\left(\frac18+\frac{M}{4}+u_R+c_Rc\right).
\]

For \(h=1,\ldots,5\),

\[
A_h(c,u)=\min\left(1,A_{h-1}(c,u)+v_R(c,u)\right),
\qquad
Y_h^{\mathrm{alt}}(c,u)=A_h(c,u).
\]

Every legal rate lies in \([0,\frac12]\). Identification and target assays
use paired \(u=0\) and \(u=1\) branches from identical cloned states.

### Authority-flow subsystem

Each assay uses paired local-evidence branches

\[
e\in\{0,1\}
\]

and fully enumerated exogenous common-cause contexts

\[
q\in\{-1,+1\}.
\]

All non-intervened coordinates and initial states are identical within each
contrast. Passive outputs satisfy

\[
Y_1=q,\qquad Y_3=q
\]

for every system, so observational association is present but contains no
target information.

For nodes \(j\in\{3,4\}\), let

\[
\nu_3=0,\qquad \nu_4=1.
\]

The primary and auxiliary states are

\[
P_1=p_Ge,
\]

\[
A_{j,1}=e\left[u_K+c_K(c+\nu_j)\right].
\]

At lag two,

\[
Y_j^{(e)}(2;c,q)=q+P_1+A_{j,1}.
\]

Advance the auxiliary path by

\[
A_{j,2}=A_{j,1}+c_Ke,
\]

and at lag three,

\[
Y_j^{(e)}(3;c,q)=q+P_1+A_{j,2}.
\]

The matched causal contrast is therefore

\[
\Delta_K(c,j,\tau)
=\frac12\sum_{q\in\{-1,+1\}}
\left[Y_j^{(1)}(\tau;c,q)-Y_j^{(0)}(\tau;c,q)\right].
\]

The common cause cancels exactly. No output function may read \(G\), \(p_G\),
\(u_K\), \(c_K\), or a stored target value directly; it must execute these
transitions.

## Disjoint identification and target domains

Identification uses numeric contexts

\[
\mathcal C_{\mathrm{ID}}=\{-1,0\}.
\]

The target uses only

\[
\mathcal C_{\mathrm{T}}=\{+1\}.
\]

Thus

\[
\mathcal C_{\mathrm{ID}}\cap\mathcal C_{\mathrm{T}}=\varnothing.
\]

No target-context output may appear in an identification probe.

## Declared target

The target reopenability assay uses context \(c=+1\), horizon

\[
H_R=5,
\]

threshold

\[
\theta_R=\frac45,
\]

and requires

\[
q_R=2
\]

consecutive threshold-attaining paired-branch contrasts. Let

\[
B_h^*=Y_h^{\mathrm{alt}}(+1,1)-Y_h^{\mathrm{alt}}(+1,0).
\]

Then

\[
R^*(f)=\mathbf 1\left[
\exists h\in\{1,2,3,4\}:
B_h^*\ge\frac45\land B_{h+1}^*\ge\frac45
\right].
\]

The signed flow target uses the disjoint assay

\[
(c,j,\tau)=(+1,4,3)
\]

and is

\[
K^*(f)=\Delta_K(+1,4,3).
\]

All arithmetic is exact. The scientific equality tolerance is zero.

The joint target is

\[
L_{014}(f)=\left(R^*(f),K^*(f)\right).
\]

It is computed only from target-assay trajectories. Target code may not call
an interface function or inspect labels, coefficients, identifiers, or
generator configuration.

## Nuisance constancy and label/outcome dissociation

The ordered nuisance vector contains baseline output, the complete observable
suppression trace, passive node traces for both values of \(q\), and all
unintervened outputs. It must equal one exact rational vector \(z_0\) for every
system. No empirical mutual-information estimate substitutes for this check.

The generated target audit must also establish by exact enumeration that:

- each fixed \(S\) realizes both \(R^*=0\) and \(R^*=1\);
- each value of \(R^*\) occurs under both selection labels;
- each fixed \(G\) realizes every signed \(K^*\) value;
- each signed \(K^*\) value occurs under both topology labels;
- each target component varies and the joint target is nonconstant.

Failure of any requirement is `INVALID_GENERATOR`.

## Frozen interface vocabulary and lattice

A mandatory constant passive control \(O_0\) is included in every protocol.
It contains no target information. The informative vocabulary contains six
vector probes:

| Probe | Exact assay |
|---|---|
| `R_NEG` | paired raw reopenability trajectories at \(c=-1\), \(h=1{:}5\) |
| `R_ZERO` | paired raw reopenability trajectories at \(c=0\), \(h=1{:}5\) |
| `K_BASE` | paired raw flow branches at \((-1,3,2)\), all \(q\) |
| `K_CONTEXT` | paired raw flow branches at \((0,3,2)\), all \(q\) |
| `K_NODE` | paired raw flow branches at \((-1,4,2)\), all \(q\) |
| `K_LAG` | paired raw flow branches at \((-1,3,3)\), all \(q\) |

The frozen lattice is every subset of these six probes, ordered first by probe
count and then lexicographically. There are exactly \(2^6=64\) interfaces.
Probe cost and raw scalar-coordinate cost must both be reported. Minimality is
only within this predeclared probe vocabulary; unrestricted encodings are not
tested.

Excluded access includes:

- target-context trajectories and target values;
- policy or topology labels;
- hidden reserve, mechanism identity, path states, or authority values;
- deletion, archive, relearning, or cancellation flags;
- coefficients, parameter tuples, dynamic signatures, or generator metadata;
- system identifiers and interface observations from other systems.

## Counterexample-first quotient audit

For every interface \(O\), construct exact equivalence classes

\[
f_a\sim_Of_b\iff O(f_a)=O(f_b).
\]

Interfaces are audited in frozen lattice order. For every quotient class,
record system identifiers, target values, architecture configurations, latent
configurations, full internal-dynamics-signature count, and target
homogeneity. For every heterogeneous class, retain a canonical
target-changing witness and the complete target-changing pair count.

Each interface record must report:

- quotient count and complete class-size histogram;
- singleton and collision-class counts;
- systems participating in collisions;
- pairwise collision count;
- heterogeneous-class and target-changing-pair counts;
- target-value coverage among collision classes;
- architecture, latent-configuration, and internal-dynamics diversity.

## Generator validity

Before assigning a scientific verdict, execution must validate:

- exactly 216 legal parameter tuples and 216 unique system identifiers;
- exactly 216 distinct full internal-trajectory signatures;
- total deterministic transitions using `fractions.Fraction` only;
- disjoint identification and target assay tuples;
- exact nuisance constancy;
- target nondegeneracy and label/outcome dissociation;
- activity of every parameter coordinate somewhere in the generated dynamics;
- no result-conditioned filtering or deduplication;
- canonical rational, system, context, node, lag, interface, witness, and JSON
  ordering.

Any failure returns

```text
INVALID_GENERATOR
```

and no factorization verdict.

## Decision taxonomy

For a valid generator, each interface receives exactly one verdict.

### Counterexample failure

```text
FAIL_COUNTEREXAMPLE
```

iff at least one quotient class contains multiple target values.

### Injective-interface pass

```text
PASS_INJECTIVE_INTERFACE
```

iff factorization holds and every quotient class is a singleton.

### Noninjective finite factor

```text
PASS_NONTRIVIAL_QUOTIENT
```

iff factorization holds and at least one quotient class contains multiple
systems. This establishes finite target-preserving compression only. It does
not rule out an arbitrary lookup table over interface fingerprints.

The optional subtype

```text
PASS_NONTRIVIAL_QUOTIENT_WITH_STRUCTURAL_DIVERSITY
```

requires dynamically inequivalent systems within the target-homogeneous
collision classes. Architecture or parameter-name differences alone do not
count.

Decision precedence is counterexample, then injective pass, then noninjective
pass and optional subtype.

## Preregistered analytic expectation

The shared affine context law implies the preregistered candidate antichain

\[
\begin{aligned}
I_C^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{context}}\},\\
I_N^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{node}}\},\\
I_L^*&=\{R_{-1},R_0,K_{-1},K_{\mathrm{lag}}\}.
\end{aligned}
\]

The expected cross-context maps are

\[
v_R(+1)=2v_R(0)-v_R(-1)
\]

and, writing \(k_-=\Delta_K(-1,3,2)\) and letting any refinement recover
\(a_K=p_G+u_K\),

\[
K^*=4a_K-3k_-.
\]

These are expectations, not stored target coordinates. The exhaustive audit
determines the recorded finite-class verdict and minimal antichain.

## Freeze and reproduction

The audit records the SHA-256 of this exact contract. Rational numbers are
serialized as reduced `[numerator, denominator]` pairs. JSON keys are sorted,
arrays follow the orders declared above, output uses LF newlines, and exactly
one final newline is written.

After this contract and its unchanged generator are committed as frozen but
unexecuted, reproduce with:

```text
python experiments/gate_014_dynamic_reopenability_flow/run_gate_014.py \
  --write experiments/results/gate_014_dynamic_reopenability_flow/factorization_audit.json
```

Gate 013 is immutable. Regardless of Gate 014's outcome, Gates 2–4 remain
closed.

