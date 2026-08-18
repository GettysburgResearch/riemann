# L-98014 — The target root is a Volterra monotonicity functional of the reciprocal Mertens sum

Claim ID: `L-98014`  
Status: **PROVED EXACT ABEL-SUMMATION IDENTITY**  
Created: 2026-08-18  
RH status: **not assumed**

Put

\[
A(x)=\sum_{n\le x}{\mu(n)\over n},
\qquad
B(x)=\sum_{n\le x}{\mu(n)\over\sqrt n}.
\]

The target root of `T-98012` is

\[
\mathcal T_x=4\sqrt x\,A(x)-3B(x).
\tag{L-98014.1}
\]

Abel summation with `a_n=mu(n)/n` and `f(t)=sqrt(t)` gives exactly

\[
B(x)=\sqrt x\,A(x)-{1\over2}\int_1^x{A(t)\over\sqrt t}\,dt.
\tag{L-98014.2}
\]

Therefore

\[
\boxed{
\mathcal T_x
=\sqrt x\,A(x)
+{3\over2}\int_1^x{A(t)\over\sqrt t}\,dt.
}
\tag{L-98014.3}
\]

Define the Volterra storage

\[
\mathcal H(x)
=x^{3/2}\int_1^x{A(t)\over\sqrt t}\,dt.
\tag{L-98014.4}
\]

On every open integer cell, and in the distributional/Stieltjes sense globally,

\[
\boxed{
\mathcal T_x
=x^{-1/2}{d\over dx}\mathcal H(x).
}
\tag{L-98014.5}
\]

Thus

\[
\boxed{
\mathrm{TRP67}
\iff
\mathcal H(x)\text{ is eventually nondecreasing}.
}
\tag{L-98014.6}
\]

## Exact finite-cell form

On `N<x<N+1`, `A(x)=A(N)` is constant. Hence

\[
\mathcal T_x
=\sqrt x\,A(N)+{3\over2}I_N,
\qquad
I_N=\int_1^N{A(t)\over\sqrt t}\,dt
+2A(N)(\sqrt x-\sqrt N).
\]

Equivalently, `mathcal T_x` is affine in `sqrt(x)` on each cell. Its minimum on a cell is therefore attained at one endpoint, determined by the sign of `A(N)`. A complete finite verification needs only outward-directed endpoint values; there is no interior nonlinear minimization.

## Research consequence

A proof of `TRP67` may now be sought as a storage theorem rather than as a direct cancellation of two unrelated sums:

```text
state:       reciprocal Mertens prefix A(N);
storage:     integral_1^N A(t)t^(-1/2)dt;
observation: sqrt(N)A(N)+(3/2)storage;
transition:  one exact Mobius jump at N+1.
```

A source-blind bound `|A|` cannot prove the sign. A successful argument must correlate the current reciprocal-Möbius jump with the accumulated Volterra storage.
