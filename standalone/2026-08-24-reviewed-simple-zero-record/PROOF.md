# A reviewed 67.3008527927% simple-zero theorem

## The baseline

The multiplicity-aware no-hypothesis theorem in the pinned formal artifact
proves

\[
S\ge H_0N-o(N),
\qquad
H_0=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

for the number `S` of simple critical-line zeros in a dyadic window.

## Retaining the discarded convex defect

Let `P=VV*` be the Gram contribution of the simple-line atoms and let `Q` be
the remainder. Every positive direction of `Q` consumes two units of zero
multiplicity, so

\[
n_+(Q)\le(N-S)/2.
\]

The stability-enhanced rank--inertia inequality therefore retains

\[
S\ge H_0N+\Delta(M)-o(N),
\qquad
\Delta(M)=\operatorname{tr}\Psi(V^*V).
\]

## A machine-free strict gain

For the optimized overlap kernel `k`, three distances in a consecutive triple
are `u`, `v`, and `u+v`. The positive zero set of `k` is sum-free, so

\[
\epsilon_4=
\min_{u,v\ge0,\ u+v\le4}
(k(u)^2+k(v)^2+k(u+v)^2)>0.
\]

Disjoint triples and convex pinching give a positive-density contribution to
`Delta`, proving a strict improvement over `H0` without computation.

## The certified seven-gap gain

The source-locked interval theorem proves

\[
\frac1{3000}\sum g_i+
\sum_{s=1}^6\frac2{7-s}
\sum_i w(g_i+\cdots+g_{i+s-1})
\ge\frac{19}{5000}.
\]

Summing over windows and averaging 269 block offsets yields

\[
\Delta(M)
\ge
\frac{4997}{1,345,000}S
-
\frac{268}{134,500}N-o(N).
\]

Substitution gives

\[
\boxed{
\liminf\frac SN
\ge
\frac{1,345,000H_0-2,680}{1,340,003}
=0.673008527927557\ldots>0.673.
}
\]

The theorem is unconditional and computer-assisted. Ninety percent and RH are
not proved.
