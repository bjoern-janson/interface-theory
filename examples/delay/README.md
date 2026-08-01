# Archived illustrative specification: delay

**Status:** noncanonical. This directory is retained as a design sketch and
must not be cited as the completed delay gate.

In a fixed known deterministic system, a delayed observation can identify the
current state by forward propagation. For example, if

\[
x_{t+1}=1.2x_t,
\qquad
y_t=x_{t-2},
\]

then (x_t=1.2^2y_t). A counterexample with equal (y_t) but arbitrary
different current states is outside that declared class.

The frozen delay result is recorded in
[docs/RESULT_LEDGER.md](../../docs/RESULT_LEDGER.md): within its specified
class, immediate observations fail and a one-step-later observation restores
the original cost-two spatial interface. It establishes temporal alignment,
not a delay sweep or an additive interface-cost law.

A replacement must specify whether transition dynamics, disturbances, and
initial histories are known to the interface.
