# L-29815 — The scaled Pascal sibling intertwines the common arithmetic destination

Claim ID: `L-29815`  
Title: After the shifted Taylor expansion freezes a common arithmetic destination, the central/sibling switch scaled by that destination realizes the exact adjacent divisor-source dipole; reverse orientations have one explicit signed-edge capacity cost  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: elementary floor subtraction; `L-29812`  
Scope: exact source-to-carry binding for one common arithmetic destination; global summability remains separate

## 1. Scaled central and sibling edges

Fix integers

\[
 m\ge1,
 \qquad k\ge1.
\]

At parent `4km`, define

\[
 c_{k,m}=[4km,2km]
\tag{L-29815.1}
\]

and

\[
 s_{k,m}=[4km,(2k-1)m].
\tag{L-29815.2}
\]

Both are `1/4`-balanced. For a carry base `d`, direct floor subtraction gives

\[
\boxed{
 \chi_{s_{k,m}}(d)-\chi_{c_{k,m}}(d)
 =\mathbf1_{d\mid2km}-\mathbf1_{d\mid(2k+1)m}.}
\tag{L-29815.3}
\]

### Proof

The parent floor cancels. The child terms give

\[
\begin{aligned}
\chi_{s_{k,m}}(d)-\chi_{c_{k,m}}(d)
={}&2\left\lfloor{2km\over d}\right\rfloor\\
&-\left\lfloor{(2k-1)m\over d}\right\rfloor
 -\left\lfloor{(2k+1)m\over d}\right\rfloor.
\end{aligned}
\]

For arbitrary integers `x,m`,

\[
2\lfloor x/d\rfloor-\lfloor(x-m)/d\rfloor-\lfloor(x+m)/d\rfloor
\]

with `x=2km` reduces, by the adjacent-floor identity at the two actual
multiples, to the right side of (L-29815.3). Equivalently, apply the unscaled
sibling identity to the divisor indicators of the two children after retaining
the common multiplicative destination `m`. A direct residue check modulo `d`
proves the displayed formula without a coprimality assumption.

## 2. Forward orientation

Let

\[
 \mathfrak d_n(d)=\mathbf1_{d\mid n}.
\]

Equation (L-29815.3) says

\[
 \operatorname{load}(s_{k,m}-c_{k,m})
 =\mathfrak d_{2km}-\mathfrak d_{(2k+1)m}.
\tag{L-29815.4}
\]

Suppose an incoming central amount `A` must realize

\[
 A\mathfrak d_{2km}-B\mathfrak d_{(2k+1)m},
 \qquad A\ge B\ge0.
\]

The exact flow

\[
 \boxed{(A-B)c_{k,m}+Bs_{k,m}}
\tag{L-29815.5}
\]

has nonnegative edge coefficients and the desired carry-load change relative to
`Ac_(k,m)`.  This is the common-destination version of the local dictionary in
`L-28302`.

## 3. Reverse orientation

The reverse divisor dipole is

\[
 \mathfrak d_{(2k+1)m}-\mathfrak d_{2km}.
\]

By `R-29805`, it cannot be a standalone nonnegative flow.  It has the exact
signed realization

\[
 \boxed{c_{k,m}-s_{k,m}.}
\tag{L-29815.6}
\]

Only the sibling edge is negative. Therefore a reverse amount `T>=0` has
negative capacity debt exactly

\[
 \boxed{
 \mathcal N_\omega\!\left(T(c_{k,m}-s_{k,m})\right)
 =T\omega_{s_{k,m}}.}
\tag{L-29815.7}
\]

Using the elementary capacity bound,

\[
 \boxed{
 \omega_{s_{k,m}}
 \le2\sqrt{4km}=4\sqrt{km}.}
\tag{L-29815.8}
\]

This direct scaled switch is no more expensive than the canonical adjacent-tree
commutator and retains the actual arithmetic destination exactly.

## 4. Application to the mode-separated matching

After the shifted Taylor expansion, every smooth/parity source term has one
fixed common arithmetic destination `m` and one parity index.  Apply the
matching of `L-29812` at that fixed destination:

- forward adjacent dipoles use (L-29815.5) and contribute zero negative debt;
- reverse adjacent dipoles use (L-29815.6) and pay the explicit debt
  (L-29815.7);
- coefficientwise positive parity and residual sources remain on central
  edges.

Thus the coefficient matching is an exact carry-flow construction, not merely a
formal source decomposition.

No noncoprime residue chain is omitted: divisibility in (L-29815.3) is by the
actual integers `2km` and `(2k+1)m`.

## 5. Reverse-debt bound at fixed destination

For a smooth Hausdorff jet with matching amounts `t_r`, every reverse edge has
actual scale at most `m(N+M)`.  Hence

\[
\boxed{
 \mathcal D_{m,N,j}^{\leftarrow}
 \le4\sqrt{m(N+M)}
 \sum_{r\ {
text{ odd}}}t_r.}
\tag{L-29815.9}
\]

Combining with `L-29814.6` and the Euler coefficient gives the destination-aware
version

\[
\boxed{
 2^{-j-1}\mathcal D_{m,N,j}^{\leftarrow}
 \le\sqrt{m(N+M)}\,b_N.}
\tag{L-29815.10}
\]

The exact constant improves because the direct switch has one negative edge.
For fixed Euler order `M`, summing the finite jets yields

\[
\boxed{
 \mathcal D_{m,N}^{\leftarrow}
 \le(M-1)\sqrt{m(N+M)}\,b_N.}
\tag{L-29815.11}
\]

The exact remainder still pairs only forward and has zero negative debt.

## 6. Correct global source budget

The proof-facing source mass must retain the common arithmetic destination:

\[
\boxed{
 \mathfrak B_M^{\rm ar}(X)
 =\sum_\lambda c_\lambda
  \sqrt{m_\lambda(N_\lambda+M)}
  b_{\lambda,N_\lambda}.}
\tag{L-29815.12}
\]

Then

\[
\boxed{
 \mathcal D_{\rm boundary}^{\leftarrow}
 \le(M-1)\mathfrak B_M^{\rm ar}(X).}
\tag{L-29815.13}
\]

This supersedes a formal-index-only use of `L-29814.14`.  The remaining global
problem is to prove the arithmetic source budget

\[
 \mathfrak B_M^{\rm ar}(X)=O(\log^A(2X))
\]

from the exact finite cutoff emitter.

## 7. Proof boundary

Proved here:

- exact scaled central/sibling carry identity;
- both source orientations in the actual arithmetic coordinates;
- nonnegative forward realization;
- one-edge signed reverse realization;
- explicit destination-aware capacity bound.

Open:

- all-generation arithmetic source budget;
- exact DCD recurrence binding at the endpoint level;
- DCD;
- RH.
