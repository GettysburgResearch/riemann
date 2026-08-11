# Q4 continuation: PIG is a singular cosine energy and weighted Goldbach correlation

**Date:** 2026-08-11  
**Status:** exact finite normal form proposed for independent review  
**RH:** unproved

## Result

Put

\[
\mathcal B(x)=\psi(4x)-4\psi(x),
\qquad
b(m)=\sum_{r=0}^3\Lambda(4m-r)-4\Lambda(m).
\]

The own compact innovation on `n=j+k` is

\[
Q_n(j)=\mathcal B(n)-\mathcal B(j)-\mathcal B(n-j)-4\log4.
\]

The complete uniform row energy has two exact normal forms.

### Fourier form

After one artificial cyclic endpoint completion,

\[
\sum_{j=1}^{n-1}|Q_n(j)|^2
=\frac1n\left[Z_n^2+4\sum_{\ell=1}^{n-1}
 (\Re\widehat{\mathcal B}_n(\ell))^2\right]-C_n^2,
\]

with

\[
\widehat{\mathcal B}_n(\ell)
=\frac{T_n(\ell)-\mathcal B(n)}{1-e^{-2\pi i\ell/n}},
\qquad
T_n(\ell)=\sum_{m\le n}b(m)e^{-2\pi i\ell m/n}.
\]

Thus PIG asks for cancellation in a singular low-frequency cosine-antiderivative norm of the radix-four block-prime source.

### Physical form

The same energy is

\[
(n-1)C^2-4CR_1+2R_{\max}+2R_+,
\]

where

\[
R_+=\sum_{a+b\le n}(n+1-a-b)b(a)b(b)
\]

is a weighted additive convolution. Expanding `b` gives explicit Goldbach-type correlations among the four radix-four residue blocks and the contracted von-Mangoldt source.

## Exact no-go

For the test increment `b(m)=sin(2*pi*m/n)`, the reflected cumulative row satisfies

\[
\frac{\|Q_n\|_2}{\|b\|_2}
=\sqrt3\cot(\pi/n)\sim\frac{\sqrt3}{\pi}n.
\]

So source-blind Parseval or the ordinary `Lambda^2` estimate necessarily loses one complete factor of `n`. A closure theorem must exploit the exact radix-four prime cancellation or the signed weighted Goldbach term.

## Remaining theorem

A concrete sufficient uniform-row gate is

\[
|Z_n|^2+4\sum_{\ell=1}^{n-1}
\left[\Re\frac{T_n(\ell)-\mathcal B(n)}{1-e^{-2\pi i\ell/n}}\right]^2
\ll n^2(\log n)^A.
\]

The delayed gauge is only polylogarithmic. A separate transfer from uniform row measure to the exact positive QIDR block measure remains necessary.

## Verification

```text
PASS_X_90704_Q4_FOURIER_GOLDBACH_NORMAL_FORM
```

The replay checks 1,404 exact rational row expansions, 97 Fourier identities, 398 sine-mode controls, and 250 formal prime-block identities.
