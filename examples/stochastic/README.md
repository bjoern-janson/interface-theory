# Archived illustrative specification: stochasticity

**Status:** noncanonical. This directory is retained as a design sketch and
must not be cited as the completed stochastic gate.

For a stochastic interface, the structural factorization test compares induced
observation distributions or kernels:

\[
P_O(\cdot\mid f_a)=P_O(\cdot\mid f_b)
\Rightarrow L(f_a)=L(f_b).
\]

Overlapping but unequal distributions create finite-sample estimation error;
they do not by themselves prove structural non-identifiability. Posterior
beliefs and distribution estimators are downstream derived objects unless
their raw information access is declared as part of (O).

The frozen result is in [docs/RESULT_LEDGER.md](../../docs/RESULT_LEDGER.md):
under known stationary binary readout noise, 92 repetitions per scalar are
required to reach maximum target-decoding error 0.046459 at
(delta=0.05). This is readout-noise sample complexity, not a stochastic
transition-dynamics result.
