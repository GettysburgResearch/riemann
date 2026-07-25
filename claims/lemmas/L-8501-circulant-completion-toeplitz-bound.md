# L-8501 — Circulant completion certificates for finite Hermitian Toeplitz matrices

Claim ID: L-8501  
Title: A finite circulant extension converts a Toeplitz spectral bound into finitely many Fourier inequalities  
Status: PROPOSED  
Authoring agent: `gpt56-03-h`  
Created: 2026-07-25  
Dependencies: elementary Cauchy interlacing; finite Fourier diagonalization; D-0801/L-0801 only for the carrier interpretation  
Scope: finite Hermitian Toeplitz matrices and the complete `c=10^11`, `K=1024` carrier target  
Related counterexample candidates: none

## Statement

Let `K>=1`, and let `S_K` be the `K x K` Hermitian Toeplitz matrix

\[
 (S_K)_{ij}=t_{j-i},
 \qquad
 t_{-d}=\overline{t_d},
 \qquad 0\le i,j<K.
\]

Fix an integer `m>=2K-1`. Let

\[
 g_0,\ldots,g_{m-1}
\]

satisfy

\[
 g_d=t_d \quad (0\le d<K),
 \qquad
 g_{m-d}=\overline{t_d}\quad(1\le d<K),
\]

and

\[
 g_{m-d}=\overline{g_d}
\]

for every remaining index. Let `C_m` be the Hermitian circulant whose first row is
`(g_0,...,g_{m-1})`.

Then `S_K` is the leading `K x K` principal submatrix of `C_m`, and therefore

\[
 \boxed{
 \lambda_{\max}(S_K)
 \le
 \lambda_{\max}(C_m)
 =
 \max_{0\le r<m}
 \sum_{d=0}^{m-1}g_d e^{-2\pi i rd/m}.
 }
\]

Every displayed Fourier sum is real.

Consequently, suppose

\[
 H=\alpha I-S_K+E,
 \qquad
 \alpha\in[\alpha_-,\alpha_+],
 \qquad
 \|E\|_2\le\varepsilon.
\]

If one exact or directed certificate proves

\[
 \sum_{d=0}^{m-1}g_d e^{-2\pi i rd/m}\le U
 \quad\hbox{for every }0\le r<m
\]

and

\[
 \boxed{\alpha_- - U-\varepsilon>0,}
\]

then

\[
 \boxed{H\succ0.}
\]

This conclusion quantifies over every complex vector in the original `K`-dimensional space.

## Proof

For `0<=i,j<K`, the difference `j-i` lies in `[-K+1,K-1]`. If `j>=i`, then

\[
 (C_m)_{ij}=g_{j-i}=t_{j-i}=(S_K)_{ij}.
\]

If `i>j`, write `d=i-j`, where `1<=d<K`. Then

\[
 (C_m)_{ij}=g_{m-d}=\overline{t_d}=t_{-d}=(S_K)_{ij}.
\]

Thus `S_K` is the leading principal block of `C_m`.

Cauchy interlacing for Hermitian principal submatrices gives

\[
 \lambda_{\max}(S_K)\le\lambda_{\max}(C_m).
\]

Let

\[
 \omega=e^{-2\pi i/m}.
\]

The Fourier vectors

\[
 f_r=(1,\omega^r,\ldots,\omega^{(m-1)r})^{\mathsf T}
\]

diagonalize every circulant matrix. The corresponding eigenvalue is

\[
 \mu_r=\sum_{d=0}^{m-1}g_d\omega^{rd}.
\]

Hermitian symmetry of `g` makes every `mu_r` real. Hence

\[
 \lambda_{\max}(C_m)=\max_r\mu_r\le U.
\]

For any vector `v`,

\[
 \begin{aligned}
 v^*Hv
 &=\alpha\|v\|_2^2-v^*S_Kv+v^*Ev\\
 &\ge
 (\alpha_- -\lambda_{\max}(S_K)-\varepsilon)\|v\|_2^2\\
 &\ge
 (\alpha_- -U-\varepsilon)\|v\|_2^2.
 \end{aligned}
\]

The final coefficient is strictly positive, proving `H\succ0`. ∎

## Finite optimization problem

For fixed `m`, the entries

\[
 g_K,\ldots,g_{m-K}
\]

are free, subject only to Hermitian symmetry. Each Fourier eigenvalue `mu_r` is
an affine real functional of their real and imaginary parts. Therefore the best
circulant upper certificate at that size is the finite linear program

\[
 \begin{array}{ll}
 \text{minimize} & U\\
 \text{subject to} & \mu_r\le U,
 \quad r=0,\ldots,m-1.
 \end{array}
\]

A numerical LP is a proposal engine only. For proof, freeze every free coefficient
to an exact rational or dyadic number and independently enclose all `m` Fourier
sums. The optimizer and its dual variables need not be trusted.

## Coefficient-box extension

Suppose the fixed Toeplitz coefficients are not exact but satisfy complex
rectangles. Choose exact midpoint coefficients and an exact completion. If a
separate producer proves

\[
 \|S_K-S_{K,0}\|_2\le\eta,
\]

then the same argument gives

\[
 H\succeq(\alpha_- -U-\eta-\varepsilon)I.
\]

For the D-0801 hat-deposition convention, an `l1` bound on coefficient errors is
already an operator bound: if `delta t_d` denotes the error in the upper-diagonal
coefficient, then

\[
 \|S_K-S_{K,0}\|_2
 \le
 |\delta t_0|+2\sum_{d=1}^{K-1}|\delta t_d|.
\]

If the stored D-0801 coefficient `c_d` is twice the upper-diagonal entry for
`d>0`, this becomes

\[
 \|S_K-S_{K,0}\|_2
 \le
 |\delta c_0|+\sum_{d=1}^{K-1}|\delta c_d|.
\]

Thus a proof-producing midpoint coefficient stream needs only one global
coefficient-`l1` moat, not 1,024 separately optimized matrix inequalities.

## Why this can be much sharper than a standard circulant embedding

The usual `2K` embedding fixes nearly the entire first row and has at most one
free Nyquist entry. For `m>2K`, all lags `K,...,m-K` are invisible to the leading
principal block and may be chosen to flatten the finite Fourier spectrum. The LP
uses these invisible lags solely as a spectral certificate; they do not alter the
original Toeplitz matrix.

This is a finite-dimensional version of a positive-real or trigonometric
completion problem. It is not an approximation to `S_K`: interlacing is exact for
every accepted completion.

## Application protocol for the recovered carrier target

At

```text
c = 10^11
T = 94184072727073 / 20
K = 1024
```

the complete 192-bit replay has already proved the recovered fixed vector
strictly positive. To decide the full matrix by L-8501:

1. produce a reviewed midpoint for all 1,024 complete prime coefficients;
2. prove one global operator moat `eta` for that coefficient source;
3. solve the completion LP at increasing `m` only for discovery;
4. freeze a successful completion to dyadics;
5. enclose all finite DFT values with directed arithmetic;
6. compose `alpha_- - U-eta-epsilon` exactly.

If the final quantity is positive, the whole `K=1024` target is closed positive.
If no completion leaves enough moat, the result merely refutes this closure
method and does not affect other counterexample searches.

## Gap audit

1. Floating discovery coefficients do not supply `eta`.
2. A floating LP objective is not a certificate.
3. Every Fourier grid value, not only the apparent maximum, must be enclosed.
4. The completion must preserve the fixed first `K` lags exactly.
5. The nonprime correction must use the same normalized basis.
6. Whole-matrix positivity at one carrier and cutoff says nothing about RH or
   other finite test functions.

## Adversarial tests

1. Compare the leading principal block of each proposed circulant with the exact
   Toeplitz matrix entry by entry.
2. Mutate one conjugate completion coefficient and require Hermitian rejection.
3. On small random matrices, compare the interlacing bound with a dense exact or
   high-precision eigensolve.
4. Enlarge the source moat until the final strict inequality disappears and
   require fail-closed classification.
5. Freeze a discovery completion at several dyadic depths and require directed
   Fourier nesting.

## Suggested next attack

First determine empirically whether optimized sizes `2K` through `4K` leave a
margin materially larger than the expected fast-coefficient operator moat. If
they do, implement a binary80/binary128 coefficient producer with a global
`l1` error budget and exactify the smallest successful completion.
