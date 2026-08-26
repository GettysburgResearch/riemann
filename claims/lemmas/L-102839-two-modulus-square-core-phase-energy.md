# L-102839 — Two-modulus square-core phase energy has a product-scale long/short bound

Claim ID: `L-102839`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-24  
Depends on: `L-102838`; `L-102836`  
RH status: **not assumed**

Let `ell_1` and `ell_2` be distinct primes, put

\[
L=\ell_1\ell_2,
\]

and let `Q` be a semiprime squareclass coprime to `L`. On one square-core
octave `B<=b<2B`, define

\[
F_{h_1,h_2,Q}(u)
={1\over\sqrt Q}
\sum_{B\le b<2B}
{d_b\over b}
 e_{\ell_1}(h_1Qb^2)
 e_{\ell_2}(h_2Qb^2)
 \phi(u-\log Q-2\log b),
\]

where `|d_b|<=1` and the autocorrelation of `phi` is supported in
`[-log 8,log 8]`.

Then

\[
\boxed{
\sum_{h_1=0}^{\ell_1-1}
\sum_{h_2=0}^{\ell_2-1}
\|F_{h_1,h_2,Q}\|_2^2
\ll_\phi
{1\over Q}\left(1+{L\over B}\right).
}
\tag{L-102839.1}

The same estimate holds after restricting both phase coordinates to be
nonzero.

## Proof

Expand the square and sum the phases. Chinese-remainder orthogonality gives

\[
\ell_1\ell_2
\mathbf1_{Q(b^2-b'^2)\equiv0\pmod L}.
\]

Since `Q` is coprime to `L`, this is the congruence

\[
b'^2\equiv b^2\pmod{\ell_1},
\qquad
b'^2\equiv b^2\pmod{\ell_2}.
\]

For each prime, `b'` is congruent to `+b` or `-b`. Hence `b'` lies in at most
four residue classes modulo `L`.

The ratio-eight autocorrelation window forces

\[
1/\sqrt8<b/b'<\sqrt8.
\]

For each fixed `b`, the harmonic weight in four progressions is

\[
\ll {1\over L}+{1\over B}.
\]

The outer harmonic sum over one octave is `O(1)`. Multiplying by `L/Q` proves
(L-102839.1).

## Two regimes

```text
long core B>=ell_1 ell_2:
  double-phase energy <<1/Q;

short core B<ell_1 ell_2:
  double-phase energy <<ell_1 ell_2/(B Q).
```

This is strictly stronger than applying the one-modulus bound twice
separately: both principal frequencies are absent and the core congruence is
localized modulo the product of the two largest discrepancy primes.

## Scope

The theorem controls one fixed residual squareclass. Coherent summation over
all four-owner squareclasses remains the arithmetic interface in `T-102860`.