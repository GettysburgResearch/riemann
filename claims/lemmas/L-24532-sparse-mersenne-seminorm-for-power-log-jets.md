# L-24532 — Sparse Mersenne seminorm bounds for stopped power-log jets

Claim ID: `L-24532`  
Title: The bottom-plus-Mersenne functional is bounded on every analytic power-log channel and on the complete positive stopped-endpoint layer cake, even though the ambient square-root atomic boundary norm is macroscopic  
Status: **PROPOSED COMPLETE ELEMENTARY ESTIMATE**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `L-24531`; elementary differentiation and geometric series  
Scope: sparse scalar boundary estimates; no all-generation contraction is asserted

## 1. Sparse Mersenne seminorm

For a function `F` on the positive integers, extended by zero past an endpoint
`N`, define

\[
\boxed{
\mathfrak M_N(F)
 =|F(2)|
 +\sum_{\substack{P=2^r\\2P-1\le N}}
 P\,|F(2P-1)-F(2P)|.
}
\tag{L-24532.1}
\]

This is the absolute seminorm naturally dominating the sparse functional in
`L-24531.11`.  It samples one adjacent pair per binary scale, rather than every
arithmetic source node.

## 2. Unstopped power-log channels

Fix `s>=1/2` and an integer `a>=0`.  Put

\[
F_{s,a,N}(x)=x^{-s}\left(1+\log{N\over x}\right)^a
\qquad(2\le x\le N).
\tag{L-24532.2}
\]

On this interval,

\[
|F_{s,a,N}'(x)|
 \le C_{s,a}
 x^{-s-1}
 \left(1+\log{N\over x}\right)^a.
\tag{L-24532.3}
\]

For a dyadic `P` with `2P<=N`, the mean-value theorem gives

\[
\begin{aligned}
P|F_{s,a,N}(2P-1)-F_{s,a,N}(2P)|
&\le C_{s,a}
 P^{-s}
 \left(1+\log{N\over P}\right)^a.
\end{aligned}
\tag{L-24532.4}
\]

Since the `P` are powers of two,

\[
\sum_{P=2^r\le N/2}
 P^{-s}\left(1+\log{N\over P}\right)^a
 \le C_{s,a}(1+\log N)^a.
\tag{L-24532.5}
\]

Thus, away from the zero-extension jump,

\[
\boxed{
\mathfrak M_N(F_{s,a,N})
 \le C_{s,a}(1+\log N)^a
 +\mathcal J_N(F_{s,a,N}),
}
\tag{L-24532.6}
\]

where `mathcal J_N` denotes the possible terminal jump at `N=2P-1`.

## 3. Endpoint jumps are harmless after the actual layer weights

For the stopped critical resolution, the endpoint weight is

\[
\ell_N=\log{N+1\over N}\le {1\over N}.
\tag{L-24532.7}
\]

A terminal jump occurs only when

\[
N=2P-1
\]

for one dyadic `P`.  For the pure-power channel `a=0`, its weighted contribution
is

\[
\ell_{2P-1}P(2P-1)^{-s}
 \le C_sP^{-s}.
\tag{L-24532.8}
\]

Consequently

\[
\sum_{\substack{N<X\\N=2P-1}}
\ell_N\mathcal J_N(F_{s,0,N})
 \le C_s\sum_{P=2^r}P^{-s}<\infty.
\tag{L-24532.9}
\]

For `a>=1`, the unmodified logarithmic factor vanishes at its own stopped
endpoint; the same estimate, with a harmless polynomial logarithm for shifted
jets, follows directly.

Combining (L-24532.5), (L-24532.7), and harmonic summation gives

\[
\boxed{
\sum_{N=2}^{X-1}
\ell_N\mathfrak M_N(F_{s,a,N})
 \le C_{s,a}(1+\log X)^{a+1}.
}
\tag{L-24532.10}
\]

The estimate is elementary and uniform in the final endpoint `X`.

## 4. Finite shifts and finite differences

Let `|b|<=B` and let

\[
G(x)=(x+b)^{-s}
 \left(1+\log{N\over x+b}\right)^a
\]

on the range where `x+b>=1`.  The finitely many small exceptional values are
placed in a base table.  On the remaining range, the proof of
(L-24532.3)--(L-24532.10) is unchanged, with constants depending on
`s,a,B`.

Every fixed-order finite difference has the positive Peano representation

\[
\Delta_h^mG(x)
 =(-1)^m\int_{[0,h]^m}
 G^{(m)}(x+t_1+\cdots+t_m)
 \,dt_1\cdots dt_m.
\tag{L-24532.11}
\]

Taking absolute values after the one-variable Peano recombination and applying
(L-24532.3) at derivative order `m` yields

\[
\boxed{
\sum_{N<X}\ell_N
 \mathfrak M_N(\Delta_h^mG)
 \le C_{s,a,B,m,h}
 (1+\log X)^{a+1}.
}
\tag{L-24532.12}
\]

The same bound holds for a fixed finite Euler jet bank and its exact remainder,
provided the remainder is retained in its positive Hausdorff/Peano form before
absolute values are taken.

## 5. Contrast with the ambient atomic norm

The outer-anchor family of `R-24530` has

\[
\sum_m\sqrt m|\sigma(m)|\gg X.
\]

There is no contradiction with (L-24532.10).  The atomic norm pays every outer
anchor separately, whereas the sparse Mersenne seminorm tests only the bottom
coordinate and one adjacent pair at each binary scale.  The central carry
pairing of `L-24531` proves that this sparse functional, after its mandatory
Dyadic zeta filter, is the source-specific RH-bearing coordinate.

Therefore the appropriate continuation is not to improve the constant `24` in
the ambient commutator bound.  It is to propagate the finite analytic and
boundary jet banks directly in the completed dyadic Mersenne seminorm.

## 6. What this closes and what it does not

Closed here:

1. every individual power-log analytic channel has polylogarithmic sparse norm;
2. the complete positive stopped-endpoint layer cake has polylogarithmic sparse
   norm;
3. every fixed finite family of shifts, differences, and Peano jets has the
   same property;
4. endpoint jumps at Mersenne locations are summable with the actual layer
   weights.

Not closed here:

1. stability of this seminorm after all finite central-cascade generations;
2. cancellation between the two endpoints in the dyadic filter;
3. RH.
