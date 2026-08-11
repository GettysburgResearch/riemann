# L-91003 — Even-depth Brun projectors for the phase-locked Möbius renewal

Claim ID: `L-91003`  
Title: Every probability mixture of even renewal depths produces an exact Möbius-free lower certificate; nonnegativity of one scale-adapted projector prevents the first negative phase-locked charge  
Status: **PROPOSED COMPLETE EXACT RENEWAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: `L-90430`; elementary polynomial division in a causal positive convolution algebra  
Scope: exact first-counterexample machinery; no proof that the resulting projector is nonnegative for the zeta source

## 1. Abstract positive-delay renewal

Let `K` be a positive causal delay operator: if `f(x)>=0` for every `x<X`, then

\[
(K^r f)(X)\ge0
\tag{L-91003.1}
\]

for every integer `r>=1`, provided every delay in `K` is strict.

Suppose

\[
\boxed{(I+K)D=G.}
\tag{L-91003.2}
\]

In the phase-locked route, `K` is the positive divisor-delay convolution by

\[
h=\mathbf1-\varepsilon,
\tag{L-91003.3}
\]

`D=-\mathcal C_*` is the desired nonnegative charge, and `G` is the explicit filtered forcing.

## 2. One even-depth projector

For an even integer `r>=2`, define

\[
Q_r(z)=1-z+z^2-\cdots-z^{r-1}
=\frac{1-z^r}{1+z}.
\tag{L-91003.4}
\]

Multiplying (L-91003.2) by `Q_r(K)` gives

\[
\boxed{
D=Q_r(K)G+K^rD.
}
\tag{L-91003.5}
\]

If `X` is a first point at which `D(X)<0`, then every strict delayed value entering `K^rD(X)` is nonnegative. Therefore

\[
K^rD(X)\ge0
\tag{L-91003.6}
\]

and (L-91003.5) forces

\[
\boxed{Q_r(K)G(X)<0.}
\tag{L-91003.7}
\]

Consequently, if for every candidate first-crossing scale one can choose an even `r` with

\[
Q_r(K)G(X)\ge0,
\tag{L-91003.8}
\]

then `D` never becomes negative.

## 3. Probability mixtures of even depths

Let `omega_r>=0` be finitely supported on even positive integers and satisfy

\[
\sum_r\omega_r=1.
\tag{L-91003.9}
\]

Put

\[
R(z)=\sum_r\omega_r z^r.
\tag{L-91003.10}
\]

Since every `r` is even,

\[
R(-1)=1,
\]

so

\[
\boxed{
Q(z)=\frac{1-R(z)}{1+z}
=\sum_r\omega_rQ_r(z)
}
\tag{L-91003.11}
\]

is a polynomial. Averaging (L-91003.5) gives the exact identity

\[
\boxed{
D=Q(K)G+R(K)D.
}
\tag{L-91003.12}
\]

At a first negative point,

\[
R(K)D(X)\ge0,
\tag{L-91003.13}
\]

and hence

\[
\boxed{Q(K)G(X)<0.}
\tag{L-91003.14}
\]

Thus any scale-dependent even-depth probability law may be used as a proof-producing Brun projector. One is not restricted to a single truncation depth.

## 4. Möbius-free source of the certificate

Work in the arithmetic convolution algebra and put

\[
h=\mathbf1-\varepsilon,
\qquad
\mu=(\varepsilon+h)^{-1}.
\tag{L-91003.15}
\]

Let `ell` be the finite phase-locked dyadic source and let

\[
b_*=\ell*\mu.
\tag{L-91003.16}
\]

The desired charge has source

\[
d=\varepsilon-b_*.
\tag{L-91003.17}
\]

Then

\[
(\varepsilon+h)*d
=\mathbf1-\ell.
\tag{L-91003.18}
\]

Hence the forcing source in (L-91003.2) is the finite/Möbius-free sequence

\[
\boxed{g=\mathbf1-\ell.}
\tag{L-91003.19}
\]

The depth-`r` certificate has source

\[
\boxed{
s_r=Q_r(h)*(\mathbf1-\ell).
}
\tag{L-91003.20}
\]

For even `r`, this factors as

\[
\boxed{
Q_r(h)
=(\varepsilon-h)
 *(\varepsilon+h^{*2}+h^{*4}+\cdots+h^{*(r-2)}).
}
\tag{L-91003.21}
\]

No Möbius coefficient occurs in (L-91003.20)--(L-91003.21). For a mixed projector the source is simply

\[
\boxed{
s_Q=Q(h)*(\mathbf1-\ell).}
\tag{L-91003.22}
\]

This is the key change of proof coordinate: the reciprocal-zeta oscillation is pushed entirely into the nonnegative first-crossing remainder `R(K)D`.

## 5. Cofinal diagonal target

Every strict divisor delay has multiplicative size at least two. Therefore a natural scale-adapted choice is an even depth `r=r(X)` satisfying

\[
2^r\le X<4\,2^r.
\tag{L-91003.23}
\]

At such a depth, the first-crossing remainder samples only the near-minimal factorisation diagonal. `L-91004` proves that this diagonal has only polynomial combinatorial complexity in `r` and exponentially small Riesz weight.

The radical closure target is therefore:

> **Diagonal Brun Positivity (`DBP`).** For every sufficiently large `X`, choose an even `r` satisfying (L-91003.23), or an even-depth probability law supported in an `O(1)` neighbourhood of that `r`, such that
> \[
> \boxed{Q(K)G(X)\ge0.}
> \tag{L-91003.24}
> \]

DBP rules out a first negative `D`, gives `D>=0` cofinally, hence `mathcal C_*<=0` cofinally, and the zero-safe Landau consumer yields RH.

DBP is not proved here.

## 6. Why mixtures matter

A single monomial remainder `K^r` is only one approximation to the inverse `(I+K)^{-1}`. Equation (L-91003.11) permits Fejer-, geometric-, Poisson-, or optimisation-derived probability laws over even depths while preserving:

```text
exact inverse identity;
positive first-crossing remainder;
finite Möbius-free certificate;
strict scale delay.
```

This creates a genuine design degree of freedom absent from the earlier fixed-depth truncations.

## 7. Proof boundary

Closed exactly here:

1. the even-depth identity;
2. the first-counterexample sign orientation;
3. arbitrary probability mixtures of even depths;
4. the finite Möbius-free projector source;
5. the scale-adapted diagonal formulation;
6. `DBP -> eventual phase-locked sign -> RH`.

Open:

1. DBP for one explicit sequence of depth laws;
2. a sum-of-squares, injection, or total-positivity proof of the projector sign;
3. RH.