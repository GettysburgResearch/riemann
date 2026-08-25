# L-103071 — BCI is one normal-ordered analytic square behind a positive spectral factor

Claim ID: `L-103071`  
Status: **PROVED EXACT SPECTRAL NORMAL FORM**  
Created: 2026-08-26  
Depends on: `L-103070`; PR #751 at `98af0db6ec7f77d6333a77a3dac53c4698852f43`, especially `L-106133--L-106135`, `T-106150`  
RH status: **unproved**

The current parent frontier `BCI102990` has the exact one-half-source form of
PR #751. This lemma removes the remaining kernel and detector phase from that
representation.

## 1. Exact half-source square imported at a frozen head

For the canonical equal-pair Boolean source, PR #751 proves

\[
 \mathfrak B_U^{\rm eq}
 =\int_0^1(1-\theta)
   \mathfrak G_{U,\theta}\star
   \mathfrak G_{U,\theta}\,d\theta,
\tag{L-103071.1}
\]

where `star` is disjoint-support Boolean convolution and every atom of
`mathfrak G_(U,theta)` has the unique physical form `n=p a^2`.

Let

\[
 F_{U,\theta}(X)=\mathcal O_A[\mathfrak G_{U,\theta}](X)
\]

and use the ordinary completion

\[
 \mathcal J_U
 =\int_0^1(1-\theta)
   (F_{U,\theta}*_MF_{U,\theta})\,d\theta.
\tag{L-103071.2}
\]

The difference between (L-103071.2) and the exact Wick convolution consists
only of shared-label prime powers of exponent `2`, `3`, or `4`; their fixed
observation is already closed in `T-102990`.

The live derivative observation is therefore

\[
 H_K^{\rm live}
 =\mathcal D_{\rm out}\mathcal J_U+H_{\rm closed},
\qquad
 \int_1^Y|H_{\rm closed}(X)|{dX\over X}=Y^{o(1)},
\tag{L-103071.3}
\]

with

\[
 P(D):=\mathcal D_{\rm out}
 ={1\over2}D(D-1)(5D+3/2)(2D-1).
\tag{L-103071.4}
\]

## 2. Critical conjugation

Put `x=log X` and write

\[
 f_{U,\theta}(u)=F_{U,\theta}(e^u)
 =\sum_n c_{U,\theta}(n)a(u-\log n).
\]

Define

\[
 S_{U,\theta}(t)
 =\sum_n c_{U,\theta}(n)n^{-1/4-it},
\]

and the normal-ordered analytic-square amplitude

\[
\boxed{
 \mathscr Q_U(t)
 =\int_0^1(1-\theta)S_{U,\theta}(t)^2\,d\theta.
}
\tag{L-103071.5}
\]

No complex conjugation occurs.

Let

\[
 j_U(x)=\mathcal J_U(e^x).
\]

By `L-103070`, if `g_(U,theta)(u)=e^{-u/4}f_(U,theta)(u)`, then

\[
 \widehat g_{U,\theta}(t)
 =e^{-itL}r_A(t)S_{U,\theta}(t),
 \qquad L=\log2,
\]

where `r_A(t)>0`. Since

\[
 e^{-x/4}(f*_Mf)(e^x)=g*g(x),
\]

finite Fubini gives

\[
\boxed{
 \widehat{e^{-x/4}j_U(x)}(t)
 =e^{-2itL}r_A(t)^2\mathscr Q_U(t).
}
\tag{L-103071.6}
\]

Conjugating the differential operator yields

\[
 e^{-x/4}P(D)j_U
 =P(D+1/4)\bigl(e^{-x/4}j_U\bigr).
\]

Therefore

\[
\boxed{
 \widehat{e^{-x/4}P(D)j_U}(t)
 =P(1/4+it)e^{-2itL}r_A(t)^2\mathscr Q_U(t).
}
\tag{L-103071.7}
\]

This is an exact identity of compactly supported distributions; an Abel
factor may be inserted and removed if an ordinary integral representative is
desired.

## 3. The detector phase is uniformly tiny

A direct expansion gives

\[
\boxed{
 P(1/4+it)
 =q(t)+ir(t),
}
\tag{L-103071.8}
\]

where

\[
 q(t)=5t^4+{19\over8}t^2+{33\over256}>0,
\qquad
 r(t)=t^3+{t\over16}.
\tag{L-103071.9}
\]

For `t>=0`,

\[
 {5\over32}q(t)-r(t)
 ={(16t^2+1)(400t^2-512t+165)\over8192}>0,
\]

because the second quadratic has discriminant `-1856`. By symmetry,

\[
\boxed{
 {|r(t)|\over q(t)}<{5\over32}
 \quad(t\in\mathbb R).
}
\tag{L-103071.10}
\]

Thus

\[
\boxed{
 |\arg P(1/4+it)|<\arctan(5/32)<0.155.
}
\tag{L-103071.11}
\]

The common kernel contributes the strictly positive factor `r_A(t)^2`; the
fixed detector contributes a positive-real factor whose phase is less than
nine degrees. Every remaining nontrivial phase and every possible adverse
orientation lies in the literal source quantity `mathscr Q_U(t)` and the
Fourier character `e^(itx)`.

## 4. Exact equivalence of the live gates

Modulo the inherited closed contraction field, equations (L-103071.3) and
(L-103071.7) identify the three current formulations:

```text
BCI102990:
  canonical coprime two-sided Boolean physical orientation;

REFSIG106150:
  positive differential variation of the reflection-odd half-field energy;

ASPH103080:
  subpower logarithmic negative mass of the inverse Fourier distribution in
  L-103071.7 after the frozen carrier/source recombinations.
```

At the exact/polylogarithmic transfer scope,

\[
\boxed{
 \mathrm{ASPH}_{103080}
 \Longleftrightarrow
 \mathrm{REFSIG}_{106150}
 \Longleftrightarrow
 \mathrm{BCI}_{102990}.
}
\tag{L-103071.12}
\]

Any one implies RH through the frozen parent Mellin--Landau consumer.

## 5. Meaning

The endpoint kernel, the dyadic common mother, the differential multiplier,
the owner gauge, and shared-label contractions have all been removed as
possible causes of the final sign problem. The sole conclusion-bearing object
is one Boolean-normal-ordered analytic square of the actual one-owner
half-source.

This theorem is a normalization and equivalence result. It does not prove
`ASPH103080`; the impossibility of replacing the analytic square by a modulus
square or an amplitude estimate is `R-103010`.
