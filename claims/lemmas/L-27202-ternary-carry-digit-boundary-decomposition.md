# L-27202 — Ternary carry, the positive base-three comb, and the exact rounding boundary

Claim ID: `L-27202`  
Title: The deterministic ternary split is the positive continuum `1/3–2/3` carry kernel minus one explicit divisibility boundary charge, with a base-three digit-sum endpoint ledger  
Status: **PROPOSED EXACT FINITE LEMMA PENDING REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27201`; general positive `p`-adic digit comb `L-23013` on PR #236  
Scope: exact floor algebra

## 1. Continuum ternary carry

For integers `2<=q<=n`, define

\[
C_{1/3}(n,q)
=
\left\lfloor\frac nq\right\rfloor
-
\left\lfloor\frac{n}{3q}\right\rfloor
-
\left\lfloor\frac{2n}{3q}\right\rfloor.
\tag{L-27202.1}
\]

This is the atomized carry associated with the exact real split
`n/3+2n/3` before integer endpoint rounding.

Let

\[
\chi_3(n,q)
=
\left\lfloor\frac nq\right\rfloor
-
\left\lfloor\frac{\lceil n/3\rceil}{q}\right\rfloor
-
\left\lfloor\frac{\lfloor2n/3\rfloor}{q}\right\rfloor.
\tag{L-27202.2}
\]

## 2. Exact rounding identity

For every `n,q`,

\[
\boxed{
\chi_3(n,q)
=C_{1/3}(n,q)
-
\mathbf1_{3\nmid n}
\mathbf1_{q\mid\lceil n/3\rceil}.
}
\tag{L-27202.3}
\]

Indeed, for `n=3m` there is no rounding. For `n=3m+1` or `3m+2`, the
`2n/3` floor is unchanged while replacing `n/3` by `ceil(n/3)=m+1`
subtracts exactly `1_(q|m+1)`.

Thus the deterministic carry row is not a generic positive kernel. Its complete
failure from the positive continuum row is one explicit divisibility boundary.

## 3. Source-level decomposition

Let `A_X(n)` be any ternary flow coefficients. Put

\[
E_X(m)=A_X(3m-2)+A_X(3m-1).
\tag{L-27202.4}
\]

Summing (L-27202.3) gives

\[
\boxed{
\sum_{n=q}^{X}A_X(n)C_{1/3}(n,q)
=
\sum_{n=q}^{X}A_X(n)\chi_3(n,q)
+
\sum_{m\le(X+2)/3:\,q\mid m}E_X(m).
}
\tag{L-27202.5}
\]

If `A_X>=0`, then `E_X>=0`. The continuum ternary carry therefore overcovers
the exact finite target by one nonnegative divisibility ledger. No boundary row
is hidden.

For the logarithmic target and the producer of `L-27201`, equation
(L-27201.7) turns this into

\[
\boxed{
\sum_{n=q}^{X}A_X(n)C_{1/3}(n,q)
=w_X(q)+\sum_{q\mid m}E_X(m).
}
\tag{L-27202.6}
\]

## 4. Base-three digit endpoint

Legendre's identity gives

\[
\sum_{m=1}^{N}v_3(m)=\frac{N-s_3(N)}2,
\]

where `s_3(N)` is the sum of the base-three digits of `N`. Therefore

\[
\boxed{
\sum_{m=1}^{N}\bigl(1-2v_3(m)\bigr)=s_3(N)\ge0.
}
\tag{L-27202.7}
\]

This is the ternary analogue of the binary endpoint identity retained on
PR #272.

## 5. Exact connection to the positive digit comb

The general `p`-adic kernel of `L-23013`, specialized to `p=3`, is

\[
P_3(t)=e^{-t/2}r_3(\lfloor e^t\rfloor)\ge0,
\]

with jump sequence

\[
1-3\mathbf1_{3\mid n}
\]

and Euler-aligned Möbius source

\[
b_3(n)=\mu(n)-\mathbf1_{3\mid n}\mu(n/3).
\]

Equations (L-27202.3)--(L-27202.7) identify the precise finite endpoint charge
that must be matched before this positive ternary comb can be used as a
coercive source theorem.

## 6. Proof boundary

Closed exactly:

- continuum/discrete ternary carry identity;
- complete divisibility correction;
- nonnegative correction when the ternary flow is nonnegative;
- base-three digit endpoint identity;
- the source link to the positive `P_3` comb.

Open:

- domination or recursive absorption of the divisibility boundary;
- inner ternary-flow positivity;
- RH.
