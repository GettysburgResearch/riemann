# L-32402 — Uniform zeta powers create a strict Selberg–Kummer row reserve

Claim ID: `L-32402`  
Title: For every integer power `M>1`, the generalized Selberg forcing of `zeta^M` is strictly dominated by its Kummer square on every nontrivial binomial carry row  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #297 `L-29002`; generalized Selberg coefficient identity  
Scope: one complete carry row; no assertion that the extra reserve survives reflected polarization

## 1. Ordinary row notation

For a binomial carry row `(n,j)`, put

\[
 F=\sum_q\Lambda(q)\chi_{n,q}(j)=\log\binom nj,
\tag{L-32402.1}
\]

\[
 A=\sum_d\Lambda(d)\log d\,\chi_{n,d}(j),
\qquad
 B=\sum_d(\Lambda*\Lambda)(d)\chi_{n,d}(j).
\tag{L-32402.2}
\]

`L-29002` proves

\[
\boxed{
 Q:=F^2-A-B\ge0.
}
\tag{L-32402.3}
\]

For a nontrivial split `1<=j<=n-1`, one also has

\[
\boxed{A>0.}
\tag{L-32402.4}
\]

Indeed `binom(n,j)>1`, so some prime `p` divides it. Kummer's formula gives

\[
 v_p\binom nj=\sum_{r\ge1}\chi_{n,p^r}(j)>0.
\]

Thus at least one power `p^r` has carry one, and its contribution

\[
 \Lambda(p^r)\log(p^r)=r(\log p)^2
\]

is strictly positive.

## 2. Generalized primes for `zeta^M`

Fix an integer `M>=1` and let

\[
 \mathcal A_M(s)=\zeta(s)^M.
\]

Its generalized von Mangoldt sequence is exactly

\[
\boxed{
 \Lambda_M=M\Lambda.
}
\tag{L-32402.5}
\]

The generalized Selberg identity therefore has forcing

\[
\boxed{
 \mathcal C_M
 =M\Lambda\log+M^2\Lambda*\Lambda.
}
\tag{L-32402.6}
\]

On the same carry row, its generalized Kummer profile is

\[
 F_M=MF
\tag{L-32402.7}
\]

and its forcing profile is

\[
 S_M=MA+M^2B.
\tag{L-32402.8}
\]

## 3. Exact reserve decomposition

Subtracting (L-32402.8) from the square of (L-32402.7),

\[
\begin{aligned}
 F_M^2-S_M
 &=M^2F^2-MA-M^2B\\
 &=M^2(F^2-A-B)+M(M-1)A.
\end{aligned}
\]

Hence

\[
\boxed{
 F_M^2-S_M
 =M^2Q+M(M-1)A.
}
\tag{L-32402.9}
\]

Both terms on the right are nonnegative. Therefore

\[
\boxed{
 S_M\le F_M^2
}
\tag{L-32402.10}
\]

on every carry row.

More importantly, if `M>1` and `1<=j<=n-1`, then (L-32402.4) gives

\[
\boxed{
 F_M^2-S_M>0.
}
\tag{L-32402.11}
\]

Thus the endpoint-neighbor null rows of the ordinary theorem are no longer null for the generalized `zeta^M` Selberg row.

For example at `j=1`, where the ordinary reserve vanishes,

\[
 F_M^2-S_M=M(M-1)A>0.
\]

## 4. Quantitative form

Equation (L-32402.9) immediately gives the source-independent lower bound

\[
\boxed{
 F_M^2-S_M\ge M(M-1)A.
}
\tag{L-32402.12}
\]

On any row for which a prime power `p^r` carries,

\[
 F_M^2-S_M
 \ge M(M-1)r(\log p)^2.
\]

The theorem therefore supplies an explicit strict reserve on the exact unit-child rows selected by the two-contact source of `L-32401`.

## 5. Why this theorem matters and what it does not prove

The ordinary Selberg–Kummer reserve has exactly the same null set as the two-contact source:

```text
ordinary row reserve zero   <=>   endpoint neighbor;
two-contact source nonzero  <=>   endpoint neighbor.
```

Uniform zeta powers break that coincidence at row level. This is a genuine structural advance.

However, reflected Hermitian polarization has its own algebra. `R-32401` shows that the additional `M(M-1)A` term cancels from the standard reflected subtraction after the individual identities are normalized. Thus (L-32402.11) is not by itself a proof of the physical coupled source matrix or RH.

## 6. Proof boundary

Closed exactly:

- generalized primes and Selberg forcing for `zeta^M`;
- the reserve identity (L-32402.9);
- strict positivity for every nontrivial row when `M>1`;
- strict endpoint reserve.

Open:

- a polarization which retains a useful portion of this linear reserve in the physical Hermitian block;
- a source-complete root-coordinate estimate;
- RH.
