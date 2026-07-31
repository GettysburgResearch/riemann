# O-15607 — Five-notch phase-band candidate at one exact dyadic translation

Claim ID: `O-15607`  
Status: `EMPIRICAL / PRODUCTION NOMINATION ONLY`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15613`, `T-15604`, PR #165 reconnaissance  
Counterexample status: none

## Exact translation nomination

Use the five-notch universal pole-free window from PR #165, with design ordinates at the first five positive critical-line zeros. Nominate

\[
 \boxed{
 x_0=\frac{8578244975439}{549755813888}
 =15.6037367113440268440172076225\ldots .}
\]

The ordinary FFT/spline reconnaissance uses maximum window support near `8.170124067971278`, so only one modest finite annulus contributes. It reports:

```text
prime-power terms at x0          64,542
raw prime midpoint               +4.183986431348427e-9
```

This is not a directed value and is dominated by the known FFT/interpolation floor.

## Ordinary zero-side planning calculation

Using 80-decimal arithmetic, midpoint first-100 zeta ordinates, the exact window product formula, and 40 trivial zeros gives:

```text
first-100 critical-zero phase model   +2.52207857747840836e-16
trivial-zero model                     +6.27075464069048215e-11
combined model                          +6.27077986147625694e-11
```

The ordinary raw-prime/model discrepancy is approximately `+4.12127863273366443e-9`. No sign inference is permitted.

## High-zero planning moat

Above the 100th zero, `T approximately 236.5242296658162`, the universal product bound may use `J=6`, five notch factors, and power `p=22`. Combining exact count `N(T)=100` with the Bellotti--Wong majorant gives the ordinary planning estimate

```text
sum_(gamma>T) gamma^-22          approximately 8.67939e-52
scalar high-zero radius           approximately 5.56e-26.
```

This is not directed because the notch ordinates, pi, product constant, zero height, and logarithms were ordinary high-precision values. It shows that a proof-grade implementation should have an enormous moat after the first 100 phases and trivial terms are retained.

## Decisive production test

1. certify the first 100 line-zero balls and multiplicities;
2. evaluate their phases and the first trivial-zero terms with directed balls;
3. prove the product/count tail with outward rational constants;
4. evaluate the exact infinite-convolution window at all 64,542 prime-power arguments, with no FFT interpolation;
5. compare through `X-15605`.

A residual interval outside the RH-valid band would be an unconditional off-line-zero witness through `T-15604`. A passing interval would diagnose the present `4e-9` discrepancy as numerical.

## Proof boundary

- Every displayed value is ordinary high-precision or IEEE-754 reconnaissance.
- The five notches were centered at midpoint zero ordinates.
- No directed prime interval or RH-valid band exists yet.
- No candidate ID is allocated.
