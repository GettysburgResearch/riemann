# First-Hermite/Q4 continuation from frozen PR #498

Frozen predecessor: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`.

## Executive result

The centered cubic identity, normalization, interpolation, Mellin pole audit, and the logical RH equivalence survive hostile reconstruction. The open `CPBD` statement does not become a proof from block count or common-half-plane alignment.

The successor replaces the broad prime-block endpoint by a narrower unconditional arithmetic reduction and redesigns the endpoint kernel at the same time:

```text
centered Q4 endpoint field
 -> zero-safe endpoint-order family G_r
 -> factor-four wavelet W_r with two Mellin moments
 -> remove all higher prime powers and small prime bases
 -> exact Vaughan decomposition
 -> close every Type-I term
 -> close every product mq<=N^(eta_r)
 -> one near-hyperbola Möbius-prime Type-II form
 -> one mollified carrier Fourier coefficient.
```

Here

\[
\eta_r=1-\frac1{2(r+1)}.
\]

The cubic gives `eta_1=3/4`; the quintic gives `eta_2=5/6`; fixed higher order localizes the unresolved product annulus arbitrarily close to `mq=N` while preserving every open-strip zero.

## Why this is not another CPBD rename

`CPBD` is the square of the complete prime-block sum. The present reduction:

1. removes the four-adic gauge;
2. removes every higher prime power;
3. removes all Type-I convolutions;
4. removes every product below `N^(eta_r)`;
5. identifies the exact second coefficient sequence
   \[
   a_U(q)=\sum_{d\mid q,d>U}\mu(d);
   \]
6. gives an exact critical-line carrier formula.

The remaining term is

\[
B_r^\sharp(N)=
\sum_{\substack{m,q>N^{1/3}\\N^{\eta_r}<mq\le N}}
\Lambda(m)a_U(q)W_r(mq/N).
\]

At `Re s=1/2`,

\[
B_r(N)=\frac{\sqrt N}{2\pi}
\int\widehat W_r(1/2+it)N^{it}
P_{V,N}(t)M_{U,N}(t)dt.
\]

The prime factor is the same critical-weight carrier appearing in the First-Hermite lane. Q4 adds a specified truncated-Mobius mollifier; First-Hermite adds a Gaussian-Hermite log window.

## Exact hostile findings

```text
Bernoulli/cubic finite identity          verified
Cauchy normalization                     verified
Mellin multiplier and zero survival      verified
integer-to-real interpolation            verified with standard endpoint bound
centered energy => RH                    verified on frozen analytic inputs
mean-free major-arc reduction            verified on frozen Fourier inputs
same-prime diagonal                      verified
```

`R-93254` remains binding. New `R-93301` shows that the balanced kernel has coefficient-blind operator ratio growing at least as `sqrt(N)` on all-one vectors. Any successful dispersion theorem must exploit the actual arithmetic signs or the carrier phase.

## Input audit

The new proved steps use only exact convolution, Chebyshev's elementary bound, divisor switching, scaled Euler/trapezoid estimates, Vaughan's identity, and Mellin inversion. No power-saving PNT, Mertens cancellation, GRH large sieve, CPBD, or RH-bearing benchmark bridge is assumed.

## Scientific boundary

No full RH proof is claimed. The new packet gives a self-contained unconditional reduction and a substantially more explicit producer. The open estimate is `T-93300.1`.

A credible next attack should focus on the single Fourier coefficient

\[
\mathcal F_t[
\widehat W_r(1/2+it)P_{V,N}(t)M_{U,N}(t)
](\log N),
\]

rather than on abstract block coherence. Candidate tools are a source-specific mollified large sieve, multiplicative dispersion retaining `a_U`, or a hybrid First-Hermite carrier argument.
