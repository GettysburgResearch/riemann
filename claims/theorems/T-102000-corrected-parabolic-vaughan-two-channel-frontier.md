# T-102000 — Corrected parabolic Vaughan two-channel frontier

Claim ID: `T-102000`
Status: **PROVED CONDITIONAL COMPOSITION; TERMINAL COMPOSITE-OWNER ESTIMATE OPEN**
Created: 2026-08-21
Depends on: PR #685 `L-100310--L-100312`; PR #691 `L-100615`; `L-102001`; `R-102000`
RH status: **unproved**

The previous attempted composition incorrectly fed the positive cubic B-spline into the Type-I theorem of `L-100310`. `R-102000` makes that route bindingly invalid. The corrected conclusion graph keeps two kernels separate.

## Channel A — signed zero-moment conclusion kernel

Use the ratio-16 signed kernel `K_1` of `L-100310`. Its continuous half-order moment vanishes and `L-100311` gives

\[
\mathcal W_1(X)=\mathcal T_U(X)+\mathcal B_U(X),
\qquad U=\lfloor X^{1/3}\rfloor,
\]

with

\[
\int_2^\infty|\mathcal T_U(X)|\frac{dX}{X}<\infty.
\]

By `L-102001`, the balanced term is exactly

\[
\mathcal B_U(X)=
\sum_{d,e>U}\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_{K_1}(X/de).
\tag{T-102000.1}
\]

Thus the entire conclusion-facing obligation is a signed large-divisor Hankel estimate on the original zero-moment kernel.

## Channel B — positive compact structural kernel

Independently, `L-102000` supplies a nonnegative compact B-spline built from the centered cubic. It is not used to pay Type I. Its role is structural: it gives a positive compact probe on the same multiplicative endpoint geometry, with no off-line Mellin cancellation.

Any use of this channel must explicitly retain or subtract its nonzero half-order main term.

## Parabolic arithmetic input

`L-100615` proves that every actual-prime double-owner interval with

\[
q\le p^A,\qquad A<e^{3/4},
\]

is positive for sufficiently large lower endpoint prime. The exact Vaughan outer pair satisfies the stronger geometric localization

\[
\max(d,e)<\min(d,e)^2
\]

on its active asymptotic support.

The missing step is therefore not a geometric exponent. It is the **composite-owner lifting** from prime intervals to the large-divisor Hankel pair while preserving the signs and the coupled cutoff constraints.

Define `CPL102000` to be the following quantitative statement:

\[
\boxed{
\int_2^Y
\left(
\sum_{d,e>U_X}
\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_{K_1}(X/de)
\right)_-
\frac{dX}{X}
=Y^{o(1)}.
}
\tag{CPL102000}
\]

This is exactly `BVD100310` rewritten through `L-102001`, so `CPL102000` is conclusion-bearing but not new by itself. The point of the matrix is to assign its internal regions to proved tools:

```text
common square gcd core g^2       sign-free by L-102001.7;
coprime wing pair (a,b)          all signs explicit;
prime endpoint subintervals      positive through A<e^(3/4) by L-100615;
Type-I / complete-lattice part   already paid by L-100310--L-100311;
remaining object                 composite-owner recombination before absolute values.
```

Consequently

\[
\boxed{
\mathrm{CPL102000}\Longrightarrow RH
}
\tag{T-102000.2}
\]

through `L-100312`.

The route is deliberately fail-closed: `SCGR` and `PCWD` are not promoted to separate theorems because the exact gcd reparameterization keeps `g,a,b` coupled. A future proof must provide one actual inequality on (T-102000.1), not independent estimates on fictitious disjoint pieces.