# L-32406 — Positive renewal equation for critical Haar shells

Claim ID: `L-32406`  
Title: Convolution of every critical Haar Möbius shell with the positive half-power kernel collapses exactly to a finite dyadic difference  
Status: **PROPOSED COMPLETE EXACT FINITE/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: `L-32403`, `L-32405`  
Scope: exact positive-kernel renewal identity; no sign, stability, or RH theorem

## 1. Critical normalization

For `k>=1`, retain

\[
\nu_{2,k}
=(\varepsilon-\sqrt2\,\delta_2)^{*k}*\mu
\]

and define the normalized coefficients

\[
 b_k(n)={\nu_{2,k}(n)\over\sqrt n},
 \qquad
 c(n)={1\over\sqrt n}.
\tag{L-32406.1}

Because the square root is completely multiplicative,

\[
 (b_k*c)(n)
 ={[(\nu_{2,k}*\mathbf1)(n)]\over\sqrt n}.
\]

Using `L-32405.5`, every coefficient `(-sqrt(2))^r delta_(2^r)` becomes simply `(-1)^r delta_(2^r)` after division by `sqrt(2^r)`. Therefore

\[
\boxed{
 b_k*c=(\varepsilon-\delta_2)^{*k}.
}
\tag{L-32406.2}

This identity contains no Möbius coefficient on the right.

## 2. Riesz convolution identity

Let

\[
 \mathcal H_{2,k}(X)
 =\sum_{n\le X}b_k(n)\log{X\over n}.
\tag{L-32406.3}

Then for every real `X>=1`, finite convolution gives

\[
\begin{aligned}
 \sum_{m\le X}{1\over\sqrt m}
 \mathcal H_{2,k}(X/m)
 &=\sum_{mn\le X}c(m)b_k(n)\log{X\over mn}\\
 &=\sum_{r=0}^{k}(-1)^r\binom kr
   \mathbf1_{X\ge2^r}\log{X\over2^r}.
\end{aligned}
\]

Hence

\[
\boxed{
 \sum_{m\le X}{\mathcal H_{2,k}(X/m)\over\sqrt m}
 =\mathcal G_k(X),
}
\tag{L-32406.4}

where

\[
\boxed{
 \mathcal G_k(X)
 =\sum_{r=0}^{k}(-1)^r\binom kr
 \mathbf1_{X\ge2^r}\log{X\over2^r}.
}
\tag{L-32406.5}

The kernel `1/sqrt(m)` is strictly positive.

## 3. First Haar shell

For `k=1` and `X>=2`,

\[
\boxed{
 \sum_{m\le X}{\mathcal H_{2,1}(X/m)\over\sqrt m}
 =\log2.
}
\tag{L-32406.6}

Thus the full critical Haar Möbius shell solves one explicit positive Volterra/renewal equation with constant forcing.

## 4. Higher Haar shells

For `k>=2` and `X>=2^k`, all indicators in (L-32406.5) equal one. The two binomial moment identities

\[
 \sum_{r=0}^{k}(-1)^r\binom kr=0,
\]

and

\[
 \sum_{r=0}^{k}(-1)^r\binom kr r=0
 \qquad(k\ge2)
\]

therefore give

\[
\boxed{
 \sum_{m\le X}{\mathcal H_{2,k}(X/m)\over\sqrt m}=0
 \qquad(X\ge2^k,\ k\ge2).
}
\tag{L-32406.7}

In particular the cubic source of `L-32405` is an exact null vector of a positive critical renewal operator outside its finite collar.

## 5. Logarithmic-coordinate form

Put

\[
 h_k(t)=e^{-t/2}\mathcal H_{2,k}(e^t).
\]

Multiplying (L-32406.4) by `e^(-t/2)` gives

\[
\boxed{
 \sum_{m\le e^t}{1\over m}
 h_k(t-\log m)
 =e^{-t/2}\mathcal G_k(e^t).
}
\tag{L-32406.8}

The left side is a causal positive harmonic-weight convolution. For `k>=2`, its forcing is compactly supported in `t<k log2`.

This is a potentially useful alternative to the signed eta propagation: the source is transferred into a positive renewal kernel at the price of a critical nullspace rather than a contraction.

## 6. What this does and does not give

The identity explains why source-blind strict contraction is structurally unavailable: higher Haar shells are nontrivial RH-sensitive states lying in the nullspace of a positive critical renewal operator after a finite collar.

A completion would need additional information—such as one-sidedness, variation control, a second independent positive renewal channel, or a source-specific finite boundary condition—to recover the state from this null equation.

No such uniqueness/coercivity theorem is asserted here.

## 7. Proof boundary

Established exactly, subject to review:

1. normalized convolution `b_k*c=(epsilon-delta_2)^k`;
2. the positive-kernel Riesz renewal identity;
3. constant forcing `log2` for `k=1`;
4. zero forcing after the finite collar for every `k>=2`;
5. the harmonic log-coordinate representation.

Not established:

1. uniqueness from the positive renewal equation;
2. a sign or subpower bound;
3. RH.
