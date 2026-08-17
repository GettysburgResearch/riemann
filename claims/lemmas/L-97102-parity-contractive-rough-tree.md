# L-97102 — Strict parity-contractive factor-67 induction

**Status:** proposed complete source-tree theorem from the exact causal identity and `L-97100`–`L-97101`.  
**RH:** not assumed.

Let `H_x` be the total unsigned mass of recursive children whose scale remains at least `67`. The exact factor-67 coefficients and monotonicity of the positive source mass give

\[
H_x<\frac18M(x).
\]

The complete current satisfies

\[
\frac1{40}(M(x)-H_x)\le f(C_x)\le\frac16(M(x)-H_x).
\]

Every recursive child is parity-swapped. Assuming inductively

\[
0\le f(P_y)\le\frac16m(P_y),
\]

the exact parent identity is

\[
f(P_x)=f(C_x)-\sum_i\alpha_if(P_{x/p_i}).
\]

Consequently

\[
\begin{aligned}
f(P_x)
&\ge\frac1{40}(M(x)-H_x)-\frac16H_x\\
&>\frac7{320}M(x)-\frac1{48}M(x)
=\boxed{\frac1{960}M(x)>0}.
\end{aligned}
\]

The upper bound `f(P_x)<=M(x)/6` follows from the current upper bound and subtraction of nonnegative recursive terms. Rank decreases by a factor at least `67`, while all low children are recombined exactly, so the induction is finite.

Therefore

\[
\boxed{\mathcal A_X\ge0\qquad(X\ge1).}
\]

This is the proposed arithmetic producer. A failure of the complete `P_61` bias theorem, mass monotonicity, first-owner disjointness, or low-child recombination rejects the result.
