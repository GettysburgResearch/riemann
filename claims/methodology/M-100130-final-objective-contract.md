# M-100130 — Final objective contract after the spectral audit

Methodology ID: `M-100130`  
Status: **BINDING RESEARCH CONTRACT**  
Created: 2026-08-20

The exact remaining arithmetic object is the ordinary-Möbius compact wavelet
of PR #674. A valid unconditional closure must prove one of the following
without importing an equivalent zero-free assertion:

1. `MWOC99910` directly;
2. the critical cumulative energy estimate
   \[
   \int_1^YQ_X\,{dX\over X^3}=Y^{o(1)};
   \]
3. a stronger source-faithful signed cross-core estimate which implies either
   display above.

`L-100131` proves that item 2 is equivalent to RH. Therefore a proof must use
specific arithmetic cancellation of the ordinary Möbius coefficients. The
following are not sufficient:

```text
compact support or zero moments alone;
diagonal or labelled-source Littlewood--Paley energy;
source-blind Cauchy--Schwarz / Schur / PSD collapse;
positive priority flux;
finite positive floor kernels;
finite positive von-Mangoldt scalar or PSD completions;
a fixed finite scale filter;
a coefficient estimate already equivalent to Mertens square-root cancellation.
```

## Required statement-to-use map

Any proposed theorem must provide an explicit inequality whose left side is
the live `Q_X` or `MWOC99910` packet, and whose right side is proved
unconditionally from one of:

```text
an exact first-owner/cross-core cancellation identity;
a signed multiplicative large-sieve estimate with all constants and ranges;
a finite-capacity prime-exchange flow with a proved live min-cut bound;
a genuinely phase-sensitive arithmetic embedding.
```

The theorem must retain the ordinary Möbius coefficient, the compact ratio-eight
activation, and the Cauchy--Poisson kernel. Replacing any of these by an
unsigned trace or an unrestricted matching is a different problem.

## Quantitative success criterion

A bound

\[
\int_1^YQ_X{dX\over X^3}
\ll_\varepsilon Y^{2\theta+\varepsilon}
\]

has a precise meaning: it proves

\[
\Re\rho\le\frac12+\theta.
\]

Thus partial progress should be reported as a quantitative zero-free region,
not as RH closure. The final value is `theta=0`.