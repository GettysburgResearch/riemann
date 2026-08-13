# Uniform four-state regeneration attack

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Status: **new exact state algebra; source-typed recursive assembly remains under review**

The PR #405 counterexample rules out propagating the positive two-state
completion. The replacement is a Doeblin split of the exact arithmetic
four-state transition:

\[
D_p=\frac{1-p^{-1/2}}{50}I_4+R_p,
\qquad R_p\ge0.
\]

The recursive term is a canonical copy of the incoming arithmetic source with
coefficient below `1/50`. The complementary term has SHARP channel parameter

\[
\frac43\left(1+\frac{50}{49\sqrt p}\right)\in(4/3,3/2),
\]

so the uniform no-upward Hall and exact-row producer applies at the state-algebra
level. This removes parameter drift and does not use the refuted `N_p` cascade.

Under a genuinely measure-valued least-prime subpartition, residual source mass
would contract geometrically and the reset recurrence would strengthen to

\[
\mathfrak L_X\le\frac1{50}\mathfrak L_{K_X}+O(1).
\]

The sole remaining firewall is the typing of that source inequality. Every
paired interior, activation frontier, finite Boolean source, Schur packet and
contracted child must appear exactly once in

\[
\sum_b z_b\preceq z_{\rm in}.
\]

Scalar least-prime uniqueness is insufficient. The matrix algebra after this
gate is exact; the gate itself remains RH-bearing until reconstructed directly
from the source/carry definitions.
