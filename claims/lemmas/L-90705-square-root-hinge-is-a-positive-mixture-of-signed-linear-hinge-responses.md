# L-90705 — The square-root CHS coefficient is a positive mixture of signed linear-hinge responses

Claim ID: `L-90705`  
Status: **PROPOSED COMPLETE EXACT FINITE DECOMPOSITION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the finite average-carry inverse; `R-90704`  
Scope: exact reformulation of CHS; no positivity theorem and no RH conclusion

## 1. Linear-hinge basis of the decreasing-convex cone

Fix an endpoint \(T\ge3\), and define

\[
h_T(q)=q^{-1/2}-T^{-1/2}
\qquad(2\le q\le T),
\tag{L-90705.1}
\]

with \(h_T(T+1)=0\). For \(2\le K\le T-1\), put

\[
H_K(q)=(K+1-q)_+.
\tag{L-90705.2}
\]

Let

\[
\omega_{T,K}
=h_T(K)-2h_T(K+1)+h_T(K+2),
\tag{L-90705.3}
\]

where the last value uses \(h_T(T+1)=0\). Thus

\[
\omega_{T,K}
=K^{-1/2}-2(K+1)^{-1/2}+(K+2)^{-1/2}>0
\quad(K\le T-2),
\tag{L-90705.4}
\]

and

\[
\omega_{T,T-1}=(T-1)^{-1/2}-T^{-1/2}>0.
\tag{L-90705.5}
\]

Double summation of discrete differences gives the exact positive representation

\[
\boxed{
h_T(q)=\sum_{K=2}^{T-1}\omega_{T,K}H_K(q).}
\tag{L-90705.6}
\]

This is simply the extreme-ray decomposition of a decreasing discretely convex target.

## 2. Response kernel

Let \(a_K(n)\) be the exact finite average-carry inverse coefficient of the linear hinge \(H_K\), i.e.

\[
H_K(q)=\sum_{n=q}^{K}a_K(n)\beta_{nq},
\qquad2\le q\le K.
\tag{L-90705.7}
\]

Let \(c_T(n)\) be the inverse coefficient of \(h_T\). Linearity and triangular support yield

\[
\boxed{
c_T(n)=\sum_{K=n}^{T-1}\omega_{T,K}a_K(n).}
\tag{L-90705.8}
\]

Thus Critical Hinge Saturation is exactly the weighted cancellation theorem

\[
\boxed{
\sum_{K=n}^{T-1}\omega_{T,K}a_K(n)\ge0
\qquad(2\le n<T).
}
\tag{L-90705.9}
\]

The weights are explicit, positive and asymptotic to

\[
\omega_{T,K}=\frac34K^{-5/2}+O(K^{-7/2})
\tag{L-90705.10}
\]

away from the endpoint.

## 3. Why generic convexity is not enough

The response kernel \(a_K(n)\) is signed. `R-90704` gives the exact witness

\[
\boxed{a_{60}(11)=-\frac2{55}.}
\tag{L-90705.11}
\]

Therefore one may not infer CHS from:

```text
square-root hinge is decreasing and convex;
average-carry inversion preserves that whole cone.
```

The second statement is false. The square-root theorem, if true, comes from the **specific decay and distribution of the weights** \(\omega_{T,K}\) against the oscillatory response kernel \(a_K(n)\).

## 4. New production target

A viable proof may establish any of the following stronger sufficient statements:

1. a weighted partial-sum bound
   \[
   \sum_{K=n}^{M}\omega_{T,K}a_K(n)\ge-arepsilon_{n,M}
   \]
   whose remaining positive tail pays \(\varepsilon_{n,M}\);
2. an Abel/renewal representation of \(K\mapsto a_K(n)\) whose cumulative response is nonnegative against the completely monotone weight \(K^{-5/2}\);
3. a finite-state decomposition of the negative response intervals into lower-scale positive packets.

The response sequence is arithmetic-free and can be studied independently of primes. This is a sharper target than residual monotonicity, which `R-90701` already refutes.

## 5. Proof boundary

```text
positive linear-hinge decomposition of h_T       exact
CHS coefficient as weighted response sum         exact
linear-hinge response kernel is signed           exact
specific square-root weighted cancellation       open / RH-bearing
CHS and RH                                        unproved
```
