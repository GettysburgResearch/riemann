# L-93013 — Every same-prime-tower term in the Q4 Goldbach energy is already at PIG scale

Claim ID: `L-93013`  
Status: **PROPOSED COMPLETE UNCONDITIONAL REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: PR #386 `L-90703`; PR #362 `T-90404`; `T-93010`; the elementary Chebyshev bound  
Scope: the hard compact-Q4 endpoint row and its exact weighted-Goldbach/max-kernel expansion; no estimate for distinct-prime correlations and no RH conclusion

## 1. Five arithmetic channels

For \(r=0,1,2,3\), put

\[
 \Phi_r(a)=4a-r,
 \qquad
 u_r(a)=\Lambda(4a-r),
 \qquad
 \kappa_r=1.
\tag{L-93013.1}
\]

For the contracted channel put

\[
 \Phi_4(a)=a,
 \qquad
 u_4(a)=\Lambda(a),
 \qquad
 \kappa_4=-4.
\tag{L-93013.2}
\]

Then the exact block-prime increment of `L-90703` is

\[
 \boxed{
 b(a)=\sum_{r=0}^{4}\kappa_ru_r(a).
 }
\tag{L-93013.3}
\]

The absolute channel weight is

\[
 \sum_{r=0}^{4}|\kappa_r|=8.
\tag{L-93013.4}
\]

## 2. The two exact quadratic kernels

For an endpoint \(n\), define

\[
 W_+(a,b)
 =(n+1-a-b)\mathbf1_{a,b\ge1,\ a+b\le n},
\tag{L-93013.5}
\]

and

\[
 W_{\max}(a,b)
 =(n-\max(a,b))\mathbf1_{1\le a,b<n}.
\tag{L-93013.6}
\]

Both kernels are nonnegative and bounded by \(n\). The two quadratic terms of
`L-90703.20` are

\[
 R_+(n)=\sum_{a,b}W_+(a,b)b(a)b(b),
\tag{L-93013.7}
\]

\[
 R_{\max}(n)=\sum_{a,b}W_{\max}(a,b)b(a)b(b).
\tag{L-93013.8}
\]

Expanding (L-93013.3) retains every cross term:

\[
 R_W(n)
 =\sum_{r,s=0}^{4}\kappa_r\kappa_s
   \sum_{a,b}W(a,b)u_r(a)u_s(b).
\tag{L-93013.9}
\]

## 3. Prime-tower partition

Whenever \(\Lambda(m)\ne0\), write

\[
 \operatorname{base}(m)=p
 \quad\text{if }m=p^k.
\]

Split (L-93013.9) into

\[
 R_W^{\mathrm{same}}(n)
\]

where

\[
 \operatorname{base}(\Phi_r(a))
 =\operatorname{base}(\Phi_s(b)),
\tag{L-93013.10}
\]

and the complementary term

\[
 R_W^{\mathrm{cross}}(n),
\tag{L-93013.11}
\]

where the two von-Mangoldt factors lie on distinct prime towers. Then exactly

\[
 \boxed{
 R_W=R_W^{\mathrm{same}}+R_W^{\mathrm{cross}}.
 }
\tag{L-93013.12}
\]

The same-prime part includes:

- equal prime powers;
- different powers of the same prime;
- coincidences between a residue-block channel and the contracted channel;
- every power-of-two interaction present in the five hard channels.

The explicit four-adic gauge is handled separately in Section 6.

Thus “diagonal” means a complete prime tower, not merely equality of the two
integer arguments.

## 4. Uniform same-prime bound

Fix a prime \(p\) and a channel \(r\). Put

\[
 A_{p,r}
 =\sum_{\substack{a\\\Phi_r(a)=p^k\le4n}}
   \Lambda(p^k).
\tag{L-93013.13}
\]

The channel only selects a subset of the powers of \(p\), so

\[
 A_{p,r}
 \le\sum_{p^k\le4n}\log p
 \le\log(4n).
\tag{L-93013.14}
\]

Using \(0\le W\le n\),

\[
\begin{aligned}
 |R_W^{\mathrm{same}}(n)|
 &\le n\sum_p
   \left(\sum_{r=0}^{4}|\kappa_r|A_{p,r}\right)^2\\
 &\le64n\,\pi(4n)\log^2(4n)\\
 &\le\boxed{256n^2\log^2(4n)}.
\end{aligned}
\tag{L-93013.15}
\]

Only the trivial bound \(\pi(4n)\le4n\) is used. Therefore, for both kernels,

\[
 |R_+^{\mathrm{same}}(n)|
 +|R_{\max}^{\mathrm{same}}(n)|
 \le512n^2\log^2(4n).
\tag{L-93013.16}
\]

This is already at PIG scale after division by \(n^2\).

## 5. Exact distinct-prime normal form

Retain the coupled linear terms of `L-90703`:

\[
 C_n=\mathcal B(n)-4\log4,
 \qquad
 R_1(n)=\sum_{m=1}^{n-1}(n-m)b(m).
\]

The hard row energy is

\[
 \mathcal E_n
 =(n-1)C_n^2-4C_nR_1(n)
  +2R_{\max}(n)+2R_+(n).
\tag{L-93013.17}
\]

Define the distinct-prime remainder without separating the large linear
cancellations:

\[
 \boxed{
 \mathcal E_n^{\ne p}
 =(n-1)C_n^2-4C_nR_1(n)
  +2R_{\max}^{\mathrm{cross}}(n)
  +2R_+^{\mathrm{cross}}(n).
 }
\tag{L-93013.18}
\]

Then (L-93013.16) gives

\[
 \boxed{
 |\mathcal E_n-\mathcal E_n^{\ne p}|
 \le1024n^2\log^2(4n).
 }
\tag{L-93013.19}
\]

Consequently

\[
 \frac{\mathcal E_n}{n^2}\ll\log^A n
\]

for some fixed \(A\) if and only if

\[
 \frac{|\mathcal E_n^{\ne p}|}{n^2}\ll\log^{A'} n
\]

for some fixed \(A'\). The remaining quadratic terms pair von-Mangoldt factors
from **different primes**. All self-correlation of one Euler factor, including
its complete prime-power tower, is removed unconditionally.

## 6. Actual compact innovation and endpoint completion

The artificial cyclic endpoint used in `L-90703` changes the physical row
energy by the explicit endpoint square \(C_n^2\). The Chebyshev bound gives
\(C_n=O(n)\), so this costs only \(O(n^2)\).

The actual compact innovation differs from the hard row by the delayed bare
gauge of `T-90404`, which is \(O(\log n)\) pointwise. If \(G\) denotes that
gauge, then

\[
 \|Q+G\|_2^2\le2\|Q\|_2^2+2\|G\|_2^2
\]

and the reverse inequality holds with \(Q\) and \(Q+G\) interchanged. Since

\[
 \|G\|_2^2=O(n\log^2 n),
\]

the actual endpoint PIG of `T-93010` is polylogarithmic exactly when the
same-prime-stripped quantity (L-93013.18) is polylogarithmic.

## 7. Interpretation

The random-Euler benchmark becomes transparent in this coordinate: independent
prime signs kill the distinct-prime part in expectation, while the surviving
same-prime towers obey (L-93013.15). Deterministic PIG is therefore not blocked
by prime powers, diagonal Goldbach terms, or the power-of-two gauge. Its exact
remaining arithmetic content is coherent correlation between different Euler
factors, with the large \(C_n,R_1\) cancellation retained.

This narrows the next legitimate estimate to:

> control the signed distinct-prime max-kernel plus weighted-Goldbach
> correlation in (L-93013.18), without taking absolute values before its exact
> linear and reflected cancellations.

No such estimate is proved here.

## 8. Proof boundary

Established unconditionally:

1. exact five-channel expansion;
2. exact same-prime/distinct-prime partition for both Q4 kernels;
3. complete same-prime-tower bound \(O(n^2\log^2 n)\);
4. exact distinct-prime energy normal form;
5. equivalence with hard-row and actual endpoint PIG after endpoint/gauge costs;
6. removal of every one-prime Euler self-correlation from the RH-bearing gate.

Open:

1. the distinct-prime signed correlation estimate;
2. endpoint PIG;
3. RH.
