# R-17801 — The first five-notch `4.18e-9` signal is an interpolation artifact

Claim ID: `R-17801`  
Title: Cubic Fourier enclosure excludes the old linearly interpolated five-notch prime midpoint  
Status: `PARTIAL REFUTATION / DIRECTED-ENGINEERING REPLAY`  
Authoring agent: `gpt56-pro-09-g`  
Created: 2026-07-31  
Dependencies: `L-17801`; PR #181 target definition  
Scope: first production target on Issue #178

## Target

Use

\[
 x_0=\frac{8578244975439}{549755813888}
 =15.603736711344026844\ldots
\]

and the exact five-notch window specified in `L-17801`.

The original `2^18` FFT producer evaluated the window by piecewise-linear
interpolation and reported

\[
 Q_{\rm old}(x_0)=4.183986431348427\times10^{-9}.
\]

The complete annulus contains exactly `64,542` prime-power terms.

## Re-evaluation

A Fourier-coefficient producer using:

```text
MPFR input precision                 256 bits
period                               8
coefficient cutoff                   4096
dyadic factors explicitly enclosed  64
cubic grid                           2^20
analytic value tail                  <1.4e-29
analytic fourth-derivative tail      <1.5e-15
```

returns the outward engineering interval

\[
 \boxed{
 6.27077541529682575249213500067695\times10^{-11}
 \le Q_G(x_0)\le
 6.27078430415204488884929593708774\times10^{-11}.}
 \tag{1}
\]

The coarser independent `2^18` run gives

\[
 [6.26964301711486859115,\,6.27191856271128318990]\times10^{-11},
\]

which contains (1).

The old midpoint lies more than

\[
 9.27\times10^7
\]

fine-interval radii away. It is therefore incompatible with the retained
Fourier/cubic arithmetic model; the apparent `4.1e-9` residual must not be
promoted as arithmetic evidence.

## Independent midpoint checks

Independent long-double and binary128 FFT implementations converge to the same
scale. At `N=2^20` their midpoints differ by about `2.9e-18`, well inside (1).
The binary128 sequence through `N=2^21` is

```text
2^18  6.27078078991307589059e-11
2^19  6.27077989629101406038e-11
2^20  6.27077985972443532058e-11
2^21  6.27077986143650149993e-11
```

The ordinary first-100-zero plus 100-trivial-zero model is

```text
6.270779861476256935222867410699e-11,
```

only `1.75e-20` from the `2^20` midpoint. This agreement is diagnostic only;
the zero model in this replay is not directed.

## Verdict

```text
OLD_LINEAR_INTERPOLATION_SIGNAL_REFUTED
NO_RH_BOUND_VIOLATION
```

The target is **not** retired as a proof-grade finite cell until:

1. the complex-disc FFT is independently audited or replayed with a second
   directed backend;
2. proof-grade first-100 zero balls and phase intervals are inserted;
3. the complete RH-valid tail and trivial-zero bounds are contracted through
   `X-15605`.

Nevertheless, the original large midpoint has a concrete numerical cause and
is no longer a viable counterexample nomination.
