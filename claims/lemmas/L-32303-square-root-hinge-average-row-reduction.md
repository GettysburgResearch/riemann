# L-32303 — Square-root hinge saturation reduces to one triangular average-row sign theorem

Claim ID: `L-32303`  
Title: Positivity of the triangular inverse of the average-carry matrix on square-root hinges gives an explicit nonnegative carry flow and closes the critical target by positive superposition  
Status: **PROPOSED COMPLETE REDUCTION / COFINAL SIGN THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #295 `L-29203`; exact average-carry identity; Legendre/Kummer consumer on the carry route  
Scope: elementary finite carry formulation

## 1. Average carry matrix

For integers `2<=q<=n`, define

\[
\boxed{
\beta_{nq}
=\frac{\lfloor n/q\rfloor\,[q-1-(n\bmod q)]}{n+1}.
}
\tag{L-32303.1}
\]

Equivalently,

\[
\boxed{
\beta_{nq}
=\frac1{n+1}\sum_{j=0}^n
\left(
\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}q\right\rfloor
\right).
}
\tag{L-32303.2}
\]

Thus row `n` is the carry-load vector of the nonnegative flow which puts mass `1/(n+1)` on every split `[n,j]`, `0<=j<=n`.  The diagonal entry is

\[
\beta_{nn}=\frac{n-1}{n+1}>0.
\tag{L-32303.3}
\]

Hence the upper triangular matrix is invertible at every finite endpoint.

## 2. Square-root hinge target

For `T>=3`, define

\[
\boxed{
h_T(q)=q^{-1/2}-T^{-1/2},
\qquad2\le q\le T.
}
\tag{L-32303.4}
\]

Let `c_T(T)=0` and define uniquely by backward substitution

\[
\boxed{
h_T(q)=\sum_{n=q}^{T}c_T(n)\beta_{nq}.
}
\tag{L-32303.5}
\]

The load-bearing finite theorem is:

> **SHARP — Square-root Hinge Average-Row Positivity.**  For every `T>=3` and every `2<=n<=T`,
> \[
> \boxed{c_T(n)\ge0.}
> \tag{SHARP}
> \]

`c_T(T)=0` is forced because `h_T(T)=0`.

## 3. SHARP gives an explicit nonnegative split flow

Assume SHARP.  Put mass

\[
\frac{c_T(n)}{n+1}
\]

on every split `[n,j]`, `0<=j<=n`.  All coefficients are nonnegative.  By (L-32303.2), its carry load in column `q` is exactly

\[
\sum_{n=q}^{T}c_T(n)\beta_{nq}=h_T(q).
\]

Therefore SHARP supplies a complete nonnegative finite carry saturation of every square-root hinge.  No Pascal-cycle optimization, source inversion, endpoint norm, or asymptotic theorem is required.

## 4. SHARP closes the logarithmic target

PR #295 `L-29203` proves the exact positive hinge decomposition

\[
\boxed{
w_X(q)
=\sum_{T=3}^{X}\lambda_{X,T}h_T(q),
\qquad
\lambda_{X,T}\ge0.
}
\tag{L-32303.6}
\]

Superposing the SHARP flows with coefficients `lambda_(X,T)` gives a nonnegative exact carry saturation of

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

Thus SHARP implies the Carry Saturation statement used in the elementary entropy route.  The existing Legendre/Kummer and entropy ledger then yields the sharp complete prime-power ramp; the reviewed square-screw/Landau consumer gives RH.

Hence the complete conditional chain is

\[
\boxed{
\mathrm{SHARP}
\Longrightarrow
\text{exact nonnegative critical carry saturation}
\Longrightarrow
\text{sharp prime ramp}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-32303.7}
\]

This is a much smaller finite theorem than positivity of the logarithmic triangular inverse itself.

## 5. Exact adjoint formula for production

For an arbitrary target `w(2),...,w(T)`, define its multiples-Möbius state

\[
u_m=\sum_{k\le T/m}\mu(k)w(mk),
\qquad 1\le m\le T.
\tag{L-32303.8}
\]

The triangular inverse has the exact closed form

\[
\boxed{
 c(j)=
 \frac{
 (j+1)[j u_j-(j-2)u_{j+1}]
 +2\sum_{m=j+2}^{T}u_m
 }{j(j-1)}.
}
\tag{L-32303.9}
\]

For the hinge target, this is

\[
u_m
=m^{-1/2}\sum_{k\le T/m}\frac{\mu(k)}{\sqrt k}
-T^{-1/2}\sum_{k\le T/m}\mu(k).
\tag{L-32303.10}
\]

Equation (L-32303.9) permits an `O(T log T)` exact directed sign checker.  It also makes the arithmetic burden explicit: SHARP retains correlated Möbius cancellation and is not an automatic consequence of target convexity.

## 6. Computational theorem nomination

The attached checker uses integer-directed rational enclosures for every `1/sqrt(n)` and exact integer Möbius arithmetic.  At each nominated endpoint it computes interval enclosures for every `u_m`, every tail sum in (L-32303.9), and every numerator of `c_T(j)`.

The retained nomination checks

```text
T = 100,
    1,000,
    10,000,
    100,000,
    1,000,000.
```

Every coefficient `c_T(j)`, `2<=j<T`, has a strictly positive lower endpoint; `c_T(T)=0` is exact.  These are finite directed certificates only.  They do not prove SHARP for all `T`.

## 7. Why this is the preferred elementary frontier

The previous logarithmic carry inverse contains all quotient layers at once and its pointwise positivity is difficult to organize.  The hinge target has four structural advantages:

1. it vanishes exactly at its endpoint;
2. it is free of the logarithmic Jordan factor;
3. it has exact factor-two self-similarity;
4. positive hinge superposition recovers the critical target with no loss.

Therefore a proof of SHARP would be a short finite-arithmetic completion of the carry route rather than an asymptotic estimate of a larger signed packet.

## 8. Proof boundary

Closed exactly:

1. the average-carry matrix identity;
2. uniqueness of the hinge inverse;
3. SHARP-to-nonnegative-flow implication;
4. positive superposition to the full critical target;
5. the exact adjoint/Möbius formula used by the checker.

Open:

1. SHARP for every endpoint;
2. RH.
