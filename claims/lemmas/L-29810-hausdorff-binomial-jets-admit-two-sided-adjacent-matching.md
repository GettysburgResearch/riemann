# L-29810 — Hausdorff binomial jets admit a two-sided adjacent matching

Claim ID: `L-29810`  
Title: Every vector-valued finite difference of a Hausdorff moment sequence can be matched nonnegatively from its even source levels to its neighboring odd demand levels, with residual equal to the positive scalar finite difference  
Status: **PROPOSED COMPLETE EXACT FINITE TRANSPORT LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: finite weighted Hall/max-flow theorem; Taylor's formula with integral remainder  
Scope: exact coefficient/source matching for the Euler jet bank; balanced Pascal realization of both transport orientations is treated separately

## 1. Hausdorff jet weights

Let

\[
 a_n=\int_{[0,1]}y^n\,d\nu(y)
\tag{L-29810.1}
\]

for one finite positive measure `nu`. Fix integers `N>=0` and `m>=0`, and put

\[
 w_r={m\choose r}a_{N+r},
 \qquad 0\le r\le m.
\tag{L-29810.2}
\]

The vector-valued `m`th finite difference has node source

\[
 V_{N,m}=\sum_{r=0}^{m}(-1)^rw_re_{N+r}.
\tag{L-29810.3}
\]

Even `r` are positive source levels and odd `r` are negative demand levels.
The scalar residual is

\[
 \sum_r(-1)^rw_r=\Delta^ma_N\ge0.
\tag{L-29810.4}
\]

## 2. Adjacent matching theorem

There exist nonnegative numbers

\[
 t_0,\ldots,t_{m-1}\ge0
\]

and nonnegative residuals `rho_r>=0` on the even levels such that

\[
\boxed{
 w_r=t_{r-1}+t_r
 \qquad(r\text{ odd}),}
\tag{L-29810.5}
\]

\[
\boxed{
 w_r=\rho_r+t_{r-1}+t_r
 \qquad(r\text{ even}),}
\tag{L-29810.6}
\]

with the boundary convention `t_(-1)=t_m=0`.

Equivalently,

\[
\boxed{
 V_{N,m}
 =\sum_{r\ {m even}}\rho_re_{N+r}
  +\sum_{r=0}^{m-1}t_r\,arepsilon_r
    (e_{N+r}-e_{N+r+1}),}
\tag{L-29810.7}
\]

where

\[
 \varepsilon_r=(-1)^r.
\]

Thus every odd demand is paid by its two neighboring even source levels and no
positive source is overspent.

The total residual is exactly

\[
 \boxed{
 \sum_{r\ {m even}}\rho_r=\Delta^ma_N.}
\tag{L-29810.8}
\]

## 3. Weighted Hall reduction

Consider the path graph on `0,1,...,m`, with even vertices as supplies and odd
vertices as demands.  By finite weighted Hall/max-flow duality, equations
(L-29810.5)--(L-29810.6) hold if and only if every set of odd vertices has
weight no larger than its neighboring even vertices.

Every connected component of such a set is an interval of odd levels

\[
 a,a+2,\ldots,b
\]

with `a,b` odd. Neighbor sets of distinct components are disjoint. It is
therefore enough to prove

\[
\boxed{
 \sum_{\substack{a\le r\le b\\r\ {m odd}}}w_r
 \le
 \sum_{\substack{a-1\le r\le b+1\\0\le r\le m\\r\ {m even}}}w_r.}
\tag{L-29810.9}
\]

## 4. Pointwise binomial interval inequality

Because `w_r` is a positive integral, it suffices to prove (L-29810.9) for

\[
 w_r={m\choose r}y^{N+r},
 \qquad 0\le y\le1.
\]

The common factor `y^N` may be removed. Define

\[
 P_k(y)=\sum_{r=0}^{k}(-1)^r{m\choose r}y^r,
 \qquad P_{-1}=0.
\tag{L-29810.10}
\]

For `0<=k<m`, Taylor's formula for `(1-y)^m` gives

\[
\boxed{
 P_k(y)=(1-y)^m+(-1)^kA_k(y),}
\tag{L-29810.11}
\]

where

\[
 A_k(y)
 ={m!\over k!(m-k-1)!}
 \int_0^y(y-t)^k(1-t)^{m-k-1}dt
 \ge0.
\tag{L-29810.12}
\]

Let `l=a-1`, and let `u=min(b+1,m)`.  The desired supply-minus-demand is

\[
 P_u(y)-P_{l-1}(y).
\tag{L-29810.13}
\]

Here `l` is even and `l-1` is odd. If `u<m`, then `u` is even and

\[
 P_u-P_{l-1}=A_u+A_{l-1}\ge0.
\tag{L-29810.14}
\]

If `u=m`, then `P_m=(1-y)^m`, so the same difference is either
`A_(l-1)>=0` or `(1-y)^m>=0` when `l=0`.  If `l=0`, the lower partial sum is
absent and `P_u>=0` directly.

This proves every interval inequality (L-29810.9), hence the weighted Hall
condition and the adjacent matching theorem.

## 5. Integrated Hausdorff sources

The proof was pointwise in `y`, but no measurable selection is required.
Integrating the interval inequalities first gives the Hall inequalities for the
actual weights (L-29810.2), and finite max-flow then supplies one matching for
the integrated source.

The theorem is therefore stable under every nonnegative superposition used in
the stopped-power/Taylor/Peano source ledger.

## 6. Application to the corrected Euler bank

`L-29809` proves that the scalar coefficient sequences emitted from an
even-start interleaved Euler transform are Hausdorff moment sequences in the
paired index. For each finite order `m`, equation (L-29810.7) gives the complete
node-labeled source decomposition which was missing from scalar positivity.

The order-two control of `R-29804` is repaired at the coefficient level by
allowing the right even source to pay the preceding odd demand.

## 7. Remaining Pascal orientation theorem

Equation (L-29810.7) contains both orientations:

\[
 e_{2h}-e_{2h+1}
 \quad\text{and}\quad
 e_{2h+2}-e_{2h+1}.
\]

The first is the central-to-sibling carry dipole already used in `L-28302`.
A completed source-to-flow theorem must also realize the second orientation by
an exact nonnegative balanced Pascal gadget, or pair the two orientations in a
larger nonnegative cycle.

This is a finite local carry problem. It is no longer a coefficient-sign or
Hausdorff-matching problem.

## 8. Proof boundary

Proved here:

- every Hausdorff binomial jet satisfies all weighted Hall inequalities;
- a nonnegative two-sided adjacent matching exists;
- no odd source demand is left unpaid;
- residual positive mass equals the scalar finite difference;
- the theorem is stable under positive source superposition.

Open:

- nonnegative balanced Pascal realization of the right-to-left orientation;
- complete source-to-PR-272 DCD congruence;
- DCD;
- RH.
