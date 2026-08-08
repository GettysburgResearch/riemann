# R-32201 — Strict eta-comb contraction cannot control zeta-zero modes

Claim ID: `R-32201`  
Title: At every zeta zero the critical eta-comb Fourier multiplier is exactly one; any strict contraction applies only to a function class excluding that oscillatory mode  
Status: **EXACT SCOPE FIREWALL / NO-GO FOR SOURCE-BLIND CONTRACTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #317 `L-30501`; elementary Fourier convolution  
Scope: contraction-based central/eta closures; does not refute source-specific coupled estimates

## 1. Critical eta comb

Retain the square-root normalized causal comb from PR #317,

\[
\beta
=\sum_{k\ge1}
\left[
(2k)^{-1/2}\delta_{\log(2k)}
-(2k+1)^{-1/2}\delta_{\log(2k+1)}
\right].
\tag{R-32201.1}
\]

Its Fourier multiplier, interpreted by the paired convergent series, is

\[
\boxed{
\widehat\beta(\xi)
=1-\eta(1/2+i\xi).
}
\tag{R-32201.2}
\]

## 2. Exact unit multiplier at every zeta zero

Let

\[
\rho=\frac12+i\gamma
\]

be any zeta zero on the critical line. Since

\[
\eta(s)=(1-2^{1-s})\zeta(s),
\]

one has

\[
\eta(\rho)=0.
\]

Therefore

\[
\boxed{
\widehat\beta(\gamma)=1.
}
\tag{R-32201.3}
\]

More generally, if a hypothetical off-line zero is

\[
\rho=\frac12+\delta+i\gamma,
\qquad \delta>0,
\]

then the exponentially weighted eta transfer has the same unit multiplier at the corresponding Mellin frequency.

Thus the RH-bearing oscillatory mode is a neutral mode of the unshifted eta transfer, not a strictly contracting mode.

## 3. Consequence for translation-invariant physical norms

On any translation-invariant Hilbert/Sobolev space for which convolution by `beta` is a Fourier multiplier and which contains wave packets localized arbitrarily tightly around `gamma`, the operator norm satisfies

\[
\boxed{
\|f\mapsto\beta*f\|\ge1.
}
\tag{R-32201.4}
\]

Indeed choose normalized Fourier wave packets supported in shrinking neighborhoods of `gamma`. Their multiplier ratio converges to

\[
|\widehat\beta(\gamma)|=1.
\]

Hence no strict physical contraction

\[
\|\beta*f\|\le\theta\|f\|,\qquad \theta<1,
\]

can hold on a space which actually contains the zeta-zero mode.

## 4. Why PR #317's weighted-jet theorem is not contradicted

PR #317 proves a strict estimate on the geometric all-jet norm

\[
\mathcal J_a(F)=\sum_{m\ge0}a^m\|F^{(m)}\|_1
\]

for sufficiently large derivative weight `a` (the retained instance uses weight two, with a finite-jet exported derivative formulation).

A pure oscillation `e^{i\gamma t}` formally contributes

\[
\sum_{m\ge0}(a|\gamma|)^m,
\]

which diverges whenever

\[
a|\gamma|\ge1.
\]

The known critical zeta zeros have frequencies far beyond this low-frequency analytic class. Thus the strict jet contraction is a valid low-frequency theorem while excluding the RH-bearing modes by its domain.

This is the precise scope boundary:

```text
strict eta jet contraction    valid on the declared analytic jet class;
strict contraction of complete RH source  impossible by this theorem alone;
critical/off-line zeta mode    neutral multiplier 1;
source-specific boundary/cycle coupling    still potentially viable.
```

## 5. Consequence for CBVR/CEV-style proposals

A proof of the remaining dyadic boundary recurrence may use the eta contraction for analytic bulk, but it cannot conclude RH by treating the complete propagated source as lying in that strictly contracting subspace.

A valid completion must do at least one of:

1. retain a separate source-specific channel which detects the neutral mode;
2. recombine the mode with a parity/boundary observable before the strict norm is applied;
3. use a one-sided positivity/Landau argument rather than a source-blind contraction;
4. produce a non-translation-invariant finite arithmetic certificate whose action on the zeta mode is explicitly checked.

## 6. Proof boundary

Established exactly:

1. the eta-comb multiplier;
2. unit multiplier at every critical zeta zero;
3. the resulting no-go for strict translation-invariant physical contraction containing the zero mode;
4. the reason the geometric weighted-jet theorem avoids contradiction by excluding high-frequency oscillations.

Not established:

1. failure of every source-specific finite recurrence;
2. RH or its negation.
