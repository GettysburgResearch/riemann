# PIG continuation: randomized benchmark and exact major-mode reduction

Author: `gpt56-pro`  
Date: 2026-08-11  
Branch: `research/gpt56-pro/90410-pig-fourier-rademacher`  
Base: PR #362 head `31c57c56c00c0a062a49a126d4e5a68ff28e9fe8`  
Status: **new exact PIG-side reductions; RH unproved**

## Executive result

This pass did not prove deterministic PIG. It produced two substantial exact
reductions.

First, the Q4 innovation is solved in the independently randomized Euler
model:

\[
\mathbb E_\varepsilon\mathcal I_\varepsilon(J)
\ll(1+J)^2.
\]

Second, the actual deterministic carry-position Gram has an exact
inverse-discrete-Laplacian form. Elementary coefficient energy closes every
additive residue class outside a square-root neighborhood of zero. The complete
unresolved positive mass is reduced to

\[
\text{one mean mode}
+
O(\sqrt N)\text{ low additive modes}.
\]

The mean has an explicit zero-safe reciprocal-zeta Mellin transform and is
itself RH-bearing.

## Why the random theorem matters

The random theorem demonstrates that no local size obstruction remains in the
Q4 source. Each squarefree core contributes one orthogonal Walsh character and
the complete expected energy is exactly the diagonal sum of its fiber
amplitudes. The deterministic difficulty is therefore coherent multiplicative
phase alignment.

This is not a comparison theorem. The actual Möbius point is one extreme point
of the sign cube. `R-90410` gives an exact endpoint-4 counterexample: the
Möbius energy is larger than both the all-positive energy and the random mean.
Thus the random theorem cannot be specialized by extremality.

## Exact Fourier coordinate

For \(c=\mathbf1*f\), the complete field satisfies

\[
\widehat Q(k)
=
\frac1{\pi k}\sum_{m<N}c(m)\sin(2\pi km/N),
\]

and

\[
\|Q\|_2^2
=
|\widehat Q(0)|^2
+
\frac1{N^2}\sum_{a=1}^{N-1}
\frac{|S_a|^2}{\sin^2(\pi a/N)}.
\]

The denominator is the Green function of the discrete circle Laplacian. The
only singular locations are \(a=0,N\).

For the innovation prefix,

\[
c_\circ(m)
=
\Lambda(m)-4\mathbf1_{4\mid m}\Lambda(m/4)
+3\log4\sum_{r\ge1}\mathbf1_{m=4^r},
\]

so

\[
\sum_{m\le N}|c_\circ(m)|^2\ll N\log N.
\]

Finite Fourier Parseval then gives

\[
\mathcal E_{\rm bulk}(N)
\ll N\log N
\]

outside \(d_N(a)<\sqrt N\).

## Exact mean scalar

The mean is

\[
M_\circ(X)=\sum_{m\le X}c_\circ(m)(2m/X-1)
\]

and

\[
\int_1^\infty M_\circ(X)X^{-z-1}dX
=
\frac{z-1}{z(z+1)}
\left[
(1-4^{1-z})\left(-\frac{\zeta'}{\zeta}(z)\right)
+3\log4\frac{4^{-z}}{1-4^{-z}}
\right].
\]

Every nontrivial open-strip zero survives. Thus the mean cannot be discarded as
a collar or neutral coordinate.

## Correct relation to the reviewed Q4 graph

PR #371 correctly demotes the claim that the complete `PIG => RH` block
assembly has already been proved. The present packet does not rely on that
claim. It supplies exact arithmetic facts about the PIG field itself.

Before any global RH composition, the integration-wave obligations remain:
one metric, exact source substitution, valid reservoir transfer, exact
pushforward measure, all collars and terminal states, and a pole-energy adapter.

## Recommended next theorem

Prove the major-mode estimate

\[
|\widehat Q(0)|^2
+
\frac1{N^2}
\sum_{0<d_N(a)<\sqrt N}
\frac{|S_a|^2}{\sin^2(\pi a/N)}
\ll N\log^B N.
\]

This is the honest deterministic frontier. The mean suggests an endpoint
annular attack; the nonzero residues suggest a genuinely growing
prime-resonant alias or finite-compression architecture. Fixed banks and generic
large-sieve bounds cannot close it.

## Exact boundary

```text
randomized Euler PIG in expectation       proposed complete exact
carry Fourier/inverse-Laplacian identity  proposed complete exact
innovation prefix coefficient formula     proposed complete exact
bulk additive residues at PIG scale       proposed complete unconditional
mean zero-safe Mellin scalar               proposed complete exact
major-mode deterministic estimate          open / RH-bearing
global repaired PIG -> RH adapter           open / review obligation
Riemann Hypothesis                          unproved
```
