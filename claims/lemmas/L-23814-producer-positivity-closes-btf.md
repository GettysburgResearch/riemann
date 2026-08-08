# L-23814 — Producer positivity automatically closes the BTF rate

Claim ID: `L-23814`  
Title: A nonnegative binary–ternary producer has `O((log X)^2)` weighted variation by its exact balanced carry load  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE PROOF**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`, `L-23811`  
Scope: removes the weighted-variation estimate as an independent hinge

## 1. Averaged binary–ternary row

For a parent `n>=2`, let

\[
 a_2=\lfloor n/2\rfloor,
 \qquad b_2=n-a_2,
\]

and

\[
 a_3=\lceil n/3\rceil,
 \qquad b_3=n-a_3.
\]

Put

\[
 \bar\chi_n(q)
 =\frac12\chi_{n,a_2}(q)
  +\frac12\chi_{n,a_3}(q).
\tag{L-23814.1}
\]

Both declared splits are balanced.  In particular,

\[
 \max(a_2,b_2)\le\frac{n+1}{2},
 \qquad
 \max(a_3,b_3)\le\frac{2n+1}{3}.
\]

Therefore, for every integer

\[
 \left\lfloor\frac{2n+1}{3}\right\rfloor<q\le n,
\]

both children in both splits are strictly below `q`, while the parent is at
least `q`.  Hence

\[
\boxed{
 \bar\chi_n(q)=1
 \qquad
 \left(\left\lfloor\frac{2n+1}{3}\right\rfloor<q\le n\right).}
\tag{L-23814.2}
\]

Consequently there is an absolute `c_*>0` such that

\[
\boxed{
 \sum_{q=2}^{n}q^{-1/2}\bar\chi_n(q)
 \ge c_*\sqrt n}
\tag{L-23814.3}
\]

for every `n>=2`.  For example one may take any fixed constant smaller than

\[
 2\left(1-\sqrt{2/3}\right)
\]

after absorbing the finitely many small parents.

## 2. Exact target load

Let `A_X(n)` be the explicit producer of `L-23811`.  Its exact column identity
is

\[
\boxed{
 w_X(q)=\sum_{n=q}^{X}A_X(n)\bar\chi_n(q)
 \qquad(2\le q\le X),}
\tag{L-23814.4}
\]

where

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

Assume only the producer sign theorem

\[
\boxed{A_X(n)\ge0\qquad(2\le n\le X).}
\tag{L-23814.5}
\]

Multiply (L-23814.4) by `q^(-1/2)` and sum over the columns.  Positivity permits
interchange without cancellation, and (L-23814.3) gives

\[
 c_*\sum_{n=2}^{X}A_X(n)\sqrt n
 \le
 \sum_{q=2}^{X}q^{-1/2}w_X(q).
\tag{L-23814.6}
\]

The right side is elementary:

\[
 \sum_{q=2}^{X}q^{-1/2}w_X(q)
 =\sum_{q=2}^{X}\frac1q\log(X/q)
 =O((\log X)^2).
\tag{L-23814.7}
\]

Thus

\[
\boxed{
 \sum_{n=2}^{X}A_X(n)\sqrt n
 =O((\log X)^2).}
\tag{L-23814.8}
\]

Since the coefficients are nonnegative, this is exactly the absolute weighted
variation required by `BTF`:

\[
 \sum_{n=2}^{X}|A_X(n)|\sqrt n
 =O((\log X)^2)=X^{o(1)}.
\tag{L-23814.9}
\]

## 3. Consequences

Under (L-23814.5), the scalar half-moment of `L-23812` also satisfies

\[
 \mathfrak H_X=O((\log X)^2).
\tag{L-23814.10}
\]

More importantly, the conditional chain of `L-23811/T-23803` now needs no
separate analytic rate theorem:

```text
explicit producer positivity
-> exact balanced flow
-> O(log^2 X) weighted variation
-> sharp prime ramp
-> square-screw/Landau
-> RH.
```

The sole remaining theorem in this producer architecture is therefore the
finite cofinal sign assertion (L-23814.5).

## 4. Proof boundary

Proved here:

- the uniform terminal carry interval of every declared split;
- the exact weighted-load inequality;
- producer positivity implies `BTF` with an explicit polylogarithmic rate;
- the half-moment rate is automatic under positivity.

Not proved here:

- cofinal producer positivity;
- RH.
