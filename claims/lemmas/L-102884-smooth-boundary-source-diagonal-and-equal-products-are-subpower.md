# L-102884 — Smooth-boundary source diagonals and equal products are subpower

Claim ID: `L-102884`  
Status: **PROVED EXACT SOURCE-ENERGY REDUCTION**  
Created: 2026-08-24  
Depends on: `L-102881`; `L-102831`; `L-102702`  
RH status: **not assumed**

Reinsert the largest-two owner factor into the derivative smooth boundary of `L-102881`.  One labelled occurrence has the form

\[
N=pq\,(de\ell k)^2
\]

and coefficient

\[
{\mu^{<q}(d)\mu^{<q}(e)\over
\sqrt{pq}\,de\ell k},
\]

with

\[
p>q,\qquad d,e\le U,\qquad \ell\ge q,\qquad P^+(k)\le\ell,
\]

and only support-active variables retained.

## 1. Free diagonal energy

Discarding all restrictions only enlarges the square sum. Therefore, on a horizon `Y`,

\[
\begin{aligned}
\mathcal E_{\rm bdry}^{\rm free}
&\le
\left(\sum_{p\le16Y}{1\over p}\right)^2
\left(\sum_{d\ge1}{1\over d^2}\right)^2
\left(\sum_{\ell\ge2}{1\over\ell^2}\right)
\left(\sum_{k\ge1}{1\over k^2}\right)\\
&\ll (\log\log(3Y))^2.
\end{aligned}
\]

Thus

\[
\boxed{
\mathcal E_{\rm bdry}^{\rm free}=Y^{o(1)}.
}
\tag{L-102884.1}
\]

The second labelled copy of `67` changes only the absolute constant.

## 2. Equal-product multiplicity

Suppose two boundary tuples give the same physical integer.  The squarefree kernel determines the unordered owner pair `{p,q}` exactly, apart from the already-separated repeated-`67` diagonal.  Once `p,q` are fixed, equality reduces to

\[
de\ell k=d'e'\ell'k'.
\]

The number of such representations of one core integer `c` is at most a fixed divisor-function power,

\[
\ll \tau_4(c)^2=c^{o(1)}.
\]

Factor-pair Cauchy and (L-102884.1) therefore give

\[
\boxed{
\text{complete equal-product boundary collapse}=Y^{o(1)}.
}
\tag{L-102884.2}

No separate boundary occupancy theorem is required for identical physical products.

## 3. Owner and phase compatibility

The new boundary prime `ell` is a literal greatest-prime owner.  Distinct-product cross terms may be assigned either to `ell` or to the largest discrepancy among the two semiprime owner pairs, with the assignment fixed before phases are inserted.  The additive phase identities and centered energy theorem `L-102882--L-102883` commute with the coefficientwise boundary decomposition.

## Exact remaining boundary operation

After (L-102884.1)--(L-102884.2), the derivative smooth boundary retains only

```text
KSCX102884:
  distinct-product, different-owner cross correlations of the smooth-boundary
  tuples in the fixed ratio-eight derivative observation.
```

This is the same physical operator type as the balanced stopped current, not an independent source-diagonal or equal-product obstruction.
