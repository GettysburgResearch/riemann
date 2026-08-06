# T-9501 — Semicircle totient endpoint: exact pole criterion and Jordan bridge

Claim ID: `T-9501`  
Title: The semicircle-weighted totient error detects every off-line zero and realizes the Jordan endpoint  
Status: `PROPOSED PARTIAL — CONVERSE EXACT; RH-TO-BOUND TRANSFER OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Last updated: 2026-08-07  
Dependencies: standard analytic continuation of `zeta`; Mellin inversion; `L-9506`; correction `R-9502`  
Scope: global one-way RH criterion and exact operator/arithmetic bridge  
Related counterexample candidates: none

## Finite arithmetic observable

For real `x>1`, define

\[
\boxed{
\mathcal V(x)=
\frac2x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \sqrt{1-\frac{n^2}{x^2}}}
\tag{T-9501.1}
\]

and

\[
\mathcal E(x)=\mathcal V(x)-\frac3\pi.
\tag{T-9501.2}
\]

The following implication is exact:

\[
\boxed{
\mathcal E(x)=O_\varepsilon(x^{-3/2+\varepsilon})
\text{ for every }\varepsilon>0
\quad\Longrightarrow\quad
\mathrm{RH}.}
\tag{T-9501.3}
\]

The converse is not claimed in this file. The initial absolute-contour proof
shortcut was incomplete; see `R-9502`. The rigorous proof-facing equivalence is
`T-9502`, using the quartic weight `(1-u^2)^2`.

## Exact Mellin transform

Put

\[
k(u)=2\sqrt{1-u^2}\,\mathbf1_{(0,1)}(u).
\tag{T-9501.4}
\]

Then

\[
\boxed{
\widehat k(z)=
\int_0^1k(u)u^{z-1}du
=B(z/2,3/2)
=\frac{\Gamma(z/2)\Gamma(3/2)}
       {\Gamma((z+3)/2)}.}
\tag{T-9501.5}
\]

Since

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^{z+1}}
=\frac{\zeta(z)}{\zeta(z+1)}
\qquad(\Re z>1),
\]

Mellin inversion gives

\[
\boxed{
\mathcal V(x)=
\frac1{2\pi i}\int_{(c)}
 \widehat k(z)
 \frac{\zeta(z)}{\zeta(z+1)}
 x^{z-1}dz,
\qquad c>1.}
\tag{T-9501.6}
\]

The pole at `z=1` contributes

\[
\frac{\widehat k(1)}{\zeta(2)}
=\frac{\pi/2}{\pi^2/6}
=\frac3\pi.
\tag{T-9501.7}
\]

At `z=0`, the pole of `Gamma(z/2)` is canceled by the zero of
`1/zeta(z+1)`.

Every nontrivial zero `rho` produces a genuine pole

\[
\boxed{z=\rho-1.}
\tag{T-9501.8}
\]

There is no cancellation:

1. `zeta(rho-1)` is nonzero because `rho-1` is nonreal with real part in
   `(-1,0)`;
2. `widehat k(rho-1)` is nonzero because gamma has no zeros and the reciprocal
   denominator-gamma zeros occur only at negative odd real integers.

## Proof of the one-way RH criterion

For `Re z>1`, direct Mellin integration yields

\[
\boxed{
\widehat k(z)\frac{\zeta(z)}{\zeta(z+1)}
-\frac{3/\pi}{z-1}
=\int_1^\infty\mathcal E(x)x^{-z}dx.}
\tag{T-9501.9}
\]

If the bound in (T-9501.3) holds for every `epsilon>0`, the right side is
analytic throughout

\[
\Re z>-\frac12.
\]

A zero `rho` with `Re rho>1/2` would create the uncanceled pole `rho-1` in that
half-plane, contradiction. The functional equation supplies the reflected
half. Hence RH holds.

More generally, any bound

\[
\mathcal E(x)=O_\varepsilon(x^{-3/2+\theta+\varepsilon})
\]

excludes zeros with

\[
\Re\rho>\frac12+\theta.
\]

Thus the rightmost shifted-zero pole gives a rigorous lower obstruction to every
possible semicircle error exponent.

## Why the reverse direction remains open here

On the putative shifted line

\[
\Re z=-\frac12+\varepsilon,
\]

one has

\[
\widehat k(z)=O(|t|^{-3/2}),
\]

while the functional equation gives

\[
|\zeta(-1/2+\varepsilon+it)|
\asymp |t|^{1-\varepsilon}
|\zeta(3/2-\varepsilon-it)|.
\]

Therefore the absolute integrand is only approximately

\[
|t|^{-1/2-\varepsilon+o(1)},
\]

which is not integrable for small `epsilon`. A valid RH-to-bound proof would
require an oscillatory stationary-phase or Bessel--Möbius theorem. No such
complete theorem is claimed here.

`T-9502` avoids this issue: its quartic Mellin kernel decays like `|t|^-3`, and
`L-9508` transfers the classical Mertens bound directly.

## Exact Jordan/Volterra endpoint bridge

The endpoint `s=1` of `L-9506` has

\[
F_1(n)=\frac{\varphi(n)}n,
\qquad
n_1(t)=2e^{-t}\sqrt{1-e^{-2t}},
\qquad
c_1=\frac6{\pi^2}.
\tag{T-9501.10}
\]

Its centered regular density satisfies

\[
\boxed{
Y_1(\log x)
=\mathcal V(x)
-\frac6{\pi^2}\left[
 \frac\pi2-\arcsin\frac1x
 -\frac1x\sqrt{1-\frac1{x^2}}
 \right].}
\tag{T-9501.11}
\]

Subtracting the positive pole-density term gives

\[
\boxed{
\begin{aligned}
Y_1(\log x)-\frac{12}{\pi^2x}
={}&\mathcal E(x)\\
&+\frac6{\pi^2}\left[
 \arcsin\frac1x
 +\frac1x\sqrt{1-\frac1{x^2}}
 -\frac2x
 \right].
\end{aligned}}
\tag{T-9501.12}
\]

The bracket is `O(x^-3)`. Therefore the Jordan/Volterra centered endpoint and
the semicircle finite arithmetic error have the same shifted-zero pole
obstruction and differ only by an elementary faster-decaying term.

## Proof-producing interface

At fixed integer or rational `x`, a directed certificate requires only exact
totients, outward square-root intervals, exact rational factors, and a directed
interval for `3/pi`.

No finite ladder proves a global exponent.

## Status boundary

What is complete at `PROPOSED` status:

1. the finite observable;
2. its Mellin transform and main residue;
3. noncancellation at every shifted nontrivial zero;
4. the implication from the RH-scale bound to RH;
5. the exact Jordan/Volterra endpoint identity.

What remains open in this file:

\[
\mathrm{RH}
\quad\Longrightarrow\quad
\mathcal E(x)=O_\varepsilon(x^{-3/2+\varepsilon}).
\]

Use `T-9502` for the complete proof-facing equivalence.

## Independent-review targets

1. Recompute the Mellin transform and residue.
2. Audit every noncancellation statement.
3. Verify the Mellin-transform converse.
4. Reconstruct the exact endpoint bridge.
5. Keep this partial criterion separate from the complete quartic transfer.
