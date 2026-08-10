# R-90406 — A generic `ell^2`/wavelet estimate cannot prove the Positive Innovation Gate

Claim ID: `R-90406`  
Status: **PROPOSED COMPLETE ASYMPTOTIC FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `T-90404`, `L-90405`  
Scope: operator-norm obstruction for arbitrary coefficient sequences; it does not rule out arithmetic estimates using the special structure of von Mangoldt

## 1. The finite-difference operator

For a finite coefficient sequence `a=(a_m)` put

\[
A(x)=\sum_{m\le x}a_m.
\]

For `n=j+k` define the aligned radix-four innovation operator

\[
\boxed{
(\mathcal T_na)(j)
=A(4n)-A(4j)-A(4k)
 -4\bigl(A(n)-A(j)-A(k)\bigr).
}
\tag{R-90406.1}
\]

This is the linear part of the compact Chebyshev innovation in `T-90404`; the fixed constant and delayed bare gauge are irrelevant to its operator norm.

Fix `0<eta<1/2` and retain only

\[
\eta n\le j\le(1-\eta)n.
\]

Regard `T_n` as a map from `ell^2({1,...,4n})` to the balanced output rows with counting measure.

## 2. A power-mode test vector

Fix

\[
\frac12<\beta<1
\]

and take

\[
\boxed{a_m=m^{\beta-1}.}
\tag{R-90406.2}
\]

Euler summation gives, uniformly for `x>=1`,

\[
A(x)=\frac{x^\beta}{\beta}+C_\beta+O_\beta(x^{\beta-1}).
\tag{R-90406.3}
\]

Insert (R-90406.3) in (R-90406.1), write `theta=j/n`, and use `k=(1-theta)n`. The constant and error terms are `O_beta(1)`, while the homogeneous main term is

\[
\boxed{
(\mathcal T_na)(j)
=\frac{4^\beta-4}{\beta}
 n^\beta
 \bigl[1-\theta^\beta-(1-\theta)^\beta\bigr]
 +O_\beta(1).
}
\tag{R-90406.4}
\]

For `beta<1`, strict concavity gives

\[
\theta^\beta+(1-\theta)^\beta>1
\qquad(0<\theta<1).
\]

Also `4^beta-4<0`. Hence on the fixed balanced interval there is a constant `c_(beta,eta)>0` such that, for all sufficiently large `n`,

\[
\boxed{
|(\mathcal T_na)(j)|
\ge c_{\beta,\eta}n^\beta
}
\tag{R-90406.5}
\]

for every retained `j`.

## 3. Operator norm is linear in the parent scale

There are `(1-2eta)n+O(1)` balanced rows. Therefore

\[
\|\mathcal T_na\|_2^2
\gg_{\beta,\eta}n^{2\beta+1}.
\tag{R-90406.6}
\]

On the input side,

\[
\|a\|_2^2
=\sum_{m\le4n}m^{2\beta-2}
\asymp_\beta n^{2\beta-1}
\tag{R-90406.7}
\]

because `2beta-2>-1`. Hence

\[
\boxed{
\|\mathcal T_n\|_{\ell^2\to\ell^2}
\gg_{\beta,\eta}n.
}
\tag{R-90406.8}
\]

The matching upper bound `O(n)` follows already from the cumulative-sum matrix, so the generic operator scale is exactly linear.

## 4. Why Parseval/large-sieve input is insufficient

The elementary coefficient energy of von Mangoldt is

\[
\sum_{m\le4n}|\Lambda(m)-1|^2\ll n\log n.
\]

Combining only this fact with the generic operator norm (R-90406.8) yields at best

\[
\sum_j|\mathcal T_n(\Lambda-1)(j)|^2
\ll n^3\log n.
\]

After the PIG normalization by `n^2`, this is `O(n log n)`, exponentially too large in logarithmic block scale. A desired `polylog(n)` estimate would require an arithmetic saving of essentially one full factor of `n` beyond generic Hilbert-space boundedness.

The power mode (R-90406.2) also explains the exponent: its normalized balanced energy is

\[
\frac1{n^2}\sum_j|\mathcal T_na(j)|^2
\asymp n^{2\beta-1},
\tag{R-90406.9}
\]

exactly the growth produced by a spectral mode with real part `beta>1/2`.

## 5. Consequence

A proof of PIG cannot come from:

1. Bessel/Parseval alone;
2. the unweighted second moment `sum Lambda(n)^2` alone;
3. a generic wavelet-frame bound for the finite-difference operator;
4. Cauchy--Schwarz applied before using prime correlations.

It must exploit arithmetic cancellation tailored to the low-frequency power modes which (R-90406.4) retains. This is consistent with `L-90405`: the filter is deliberately zero-safe, so it cannot be a uniformly bounded high-pass transform on every `beta>1/2` mode.

## 6. Scope firewall

This is an operator-class no-go, not a counterexample to PIG for the actual von Mangoldt sequence. It leaves open:

- source-specific reflected identities;
- nontrivial prime correlations;
- configuration-sensitive finite-compression certificates;
- RH.
