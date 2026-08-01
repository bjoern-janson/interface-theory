# F0_linear — Target-Relative Linear Identifiability

**Status:** illustrative linear factorization example. The canonical completed-gate
record is maintained in [docs/RESULT_LEDGER.md](../../docs/RESULT_LEDGER.md).

## System and target

\[
x_{t+1}=Ax_t,
\qquad
A=
\begin{bmatrix}
1&0.2\\
0&0.9
\end{bmatrix}.
\]

The example target is the first coordinate after five transitions:

\[
L_T(x_0)=e_1^\top A^5x_0
=
\begin{bmatrix}
1&0.81902
\end{bmatrix}x_0.
\]

The target is a scalar linear functional. It does **not** require reconstruction
of the entire initial state.

## Factorization test

An interface (O) is sufficient for (L_T) if

\[
\exists\widehat L
\quad\text{such that}\quad
L_T=\widehat L\circ O.
\]

A counterexample is a pair (x_a,x_b) for which

\[
O(x_a)=O(x_b)
\quad\text{but}\quad
L_T(x_a)\ne L_T(x_b).
\]

## Declared candidate interfaces

| Interface | Observation | Result for (L_T) |
|---|---|---|
| Full state | (O(x)=x) | Sufficient |
| First coordinate | (O(x)=x_1) | Insufficient |
| Second coordinate | (O(x)=x_2) | Insufficient |
| Target-aligned scalar | (O(x)=[1,0.81902]x) | Sufficient |

The target-aligned scalar interface has (widehat L(y)=y). It shows why
minimality is target-relative: one scalar can identify this scalar target,
whereas full-state access remains necessary for targets such as complete
trajectory reconstruction.

The finite candidate menu is specified in interfaces.json. It is not a claim
about every conceivable interface cost or an execution record for the broader
frozen nonlinear (F_0) gate.

## Correct reference values

\[
A^5=
\begin{bmatrix}
1&0.81902\\
0&0.59049
\end{bmatrix}.
\]

Therefore,

\[
L_T([0,1]^\top)=0.81902,
\qquad
L_T([1,1]^\top)=1.81902.
\]

## Scope

This example illustrates the factorization criterion. It does not validate an
adaptive target, a correctability metric, or a mechanism. For the current
class-scoped evidence, consult the [frozen result ledger](../../docs/RESULT_LEDGER.md).
