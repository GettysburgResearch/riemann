# L-29814 — Reverse Euler-jet debt is controlled by square-root source mass

Claim ID: `L-29814`  
Title: After the exact mode separation and two-sided Hausdorff matching, every finite Euler jet has an explicit reverse-commutator debt bounded independently of the jet order after its Euler coefficient is inserted; the exact remainder has zero reverse debt  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29809`, `L-29810`, `L-29812`, `L-29813`  
Scope: one even-start common-tail source and its positive superpositions; global boundary-source summability is isolated in Section 6

## 1. Smooth Hausdorff source

Use the mode separation of `L-29812`.  For the smooth mode, write

\[
 b_n=\int_{[0,1]}y^n\,d\nu(y).
\tag{L-29814.1}
\]

At even start `N` and finite-difference order `m`, the alternating vector jet
has weights

\[
 w_r={m\choose r}b_{N+r},
 \qquad 0\le r\le m.
\tag{L-29814.2}
\]

Let `t_r` be any nonnegative adjacent matching supplied by `L-29810`.
The reverse orientations are exactly the edges with odd `r`.

## 2. Total reverse matching mass

Every matching edge is incident to exactly one odd demand vertex. Therefore

\[
 \sum_{r=0}^{m-1}t_r
 =\sum_{\substack{0\le r\le m\\r\ {
text{ odd}}}}w_r.
\tag{L-29814.3}
\]

In particular, the reverse subset obeys

\[
 \sum_{\substack{0\le r<m\\r\ {
text{ odd}}}}t_r
 \le\sum_{r\ {
text{ odd}}}w_r.
\tag{L-29814.4}
\]

The odd binomial mass has the exact integral

\[
\begin{aligned}
\sum_{r\ {
text{ odd}}}w_r
={1\over2}\int y^N
 \left[(1+y)^m-(1-y)^m\right]d\nu(y).
\end{aligned}
\tag{L-29814.5}
\]

Since `0<=y<=1`,

\[
 \boxed{
 \sum_{r\ {
text{ odd}}}w_r
 \le2^{m-1}b_N
 \qquad(m\ge1).}
\tag{L-29814.6}
\]

## 3. Capacity of the reverse orientations

Realize each reverse adjacent dipole by the canonical commutator `E_(N+r)`.
By `L-29813`,

\[
 \mathcal N_\omega(E_{N+r})
 \le(4+2\sqrt2)\sqrt{N+r}.
\tag{L-29814.7}
\]

Hence the reverse debt of the unscaled `m`th jet is bounded by

\[
\begin{aligned}
\mathcal D_{N,m}^{\leftarrow}
&\le(4+2\sqrt2)\sqrt{N+m}
 \sum_{r\ {
text{ odd}}}t_r\\
&\le(4+2\sqrt2)2^{m-1}
 \sqrt{N+m}\,b_N.
\end{aligned}
\tag{L-29814.8}
\]

The finite Euler coefficient of this jet is `2^(-m-1)`. Therefore

\[
 \boxed{
 2^{-m-1}\mathcal D_{N,m}^{\leftarrow}
 \le{2+\sqrt2\over2}\sqrt{N+m}\,b_N.}
\tag{L-29814.9}
\]

The exponential binomial growth has canceled exactly against the Euler weight.
There is no loss increasing with `2^m`.

For fixed Euler order `M`, summing all finite jets gives

\[
\boxed{
\sum_{m=1}^{M-1}2^{-m-1}
 \mathcal D_{N,m}^{\leftarrow}
 \le{2+\sqrt2\over2}(M-1)
 \sqrt{N+M}\,b_N.}
\tag{L-29814.10}
\]

The order-zero jet contains no reverse orientation.

## 4. Exact remainder has zero reverse debt

Consider the exact `M`th Euler remainder of `L-29809`.  On the smooth mode,
its node coefficients are

\[
 (-1)^r c_r,
 \qquad
 c_r=\Delta^Mb_{N+r}.
\tag{L-29814.11}
\]

The sequence `c_r` is nonnegative and decreasing because it is Hausdorff.
Pair every even level with the following odd level:

\[
 c_{2h}e_{N+2h}-c_{2h+1}e_{N+2h+1}
 =(c_{2h}-c_{2h+1})e_{N+2h}
 +c_{2h+1}(e_{N+2h}-e_{N+2h+1}).
\tag{L-29814.12}
\]

Every dipole has the forward orientation and therefore the nonnegative Pascal
realization of `L-28302`.  The residual is nonnegative.

The parity mode of `L-29812` is coefficientwise nonnegative after the Euler
sign. Consequently

\[
 \boxed{
 \mathcal D_{N,M}^{\leftarrow,\rm remainder}=0.}
\tag{L-29814.13}
\]

The factor `2^(-M)` remains available for its positive residual source, but no
negative-capacity estimate is needed for the remainder itself.

## 5. Positive superpositions

Let a finite or absolutely convergent source bank be indexed by `lambda`, with
nonnegative outer coefficients `c_lambda`, even starts `N_lambda`, and smooth
mode values `b_(lambda,N_lambda)`.  Complete common-destination recombination
preserves the preceding estimates. Define its square-root source mass

\[
 \boxed{
 \mathfrak B_M
 =\sum_\lambda c_\lambda
  \sqrt{N_\lambda+M}\,
  b_{\lambda,N_\lambda}.}
\tag{L-29814.14}
\]

Then the complete reverse debt from all finite jets satisfies

\[
 \boxed{
 \mathcal D_{\rm jets}^{\leftarrow}
 \le{2+\sqrt2\over2}(M-1)\mathfrak B_M,}
\tag{L-29814.15}
\]

and every exact Euler remainder has zero reverse debt.

This estimate is source-additive and uses the same capacity metric as PR #272.

## 6. Exact remaining scalar

The vector sign, matching, and local commutator problems are now closed.  To
obtain DCD from the corrected boundary cascade it is enough to prove, for one
fixed `M`, that the complete emitted source bank satisfies

\[
 \boxed{
 \mathfrak B_M(X)=O(\log^A(2X))}
\tag{L-29814.16}
\]

through all half-scale generations, with every unmatched odd-start term and
bottom charge retained in the existing collar.

This is a square-root-weighted source-mass estimate, not a generic kernel
positivity statement.  PR #286 `L-28402.10` claims a polylogarithmic
first-generation capacity ledger; a completed proof must identify its declared
capacity norm with or above (L-29814.14) and propagate it under the exact
Duhamel source map.

## 7. Proof boundary

Proved here:

- exact odd-binomial matching mass;
- explicit reverse capacity bound for every finite jet;
- cancellation of the exponential jet-order factor;
- zero reverse debt for the exact Euler remainder;
- additive reduction to the square-root source mass `mathfrak B_M`.

Open:

- all-generation bound (L-29814.16);
- exact binding to the lower-flow odd leakage;
- DCD;
- RH.
