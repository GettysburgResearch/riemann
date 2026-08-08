# R-28001 — The continuum central cascade has its first sign defect at six

Claim ID: `R-28001`  
Title: The second continuum central residual is not monotone; the first exact defect is the multiplicative overlap `6=2*3`  
Status: **PROPOSED EXACT REFUTATION / SCOPE CORRECTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Scope: exact continuum algebra; no numerical input

## 1. The causal critical profile

Put

\[
 F(t)=t e^{t/2}\mathbf 1_{t\ge0}.
\]

This is the logarithmic form of the critical profile

\[
 W(x)=x^{-1/2}\log(1/x)\mathbf 1_{0<x\le1},
 \qquad t=\log(1/x).
\]

Define the continuum central residual operator

\[
 (\mathcal UF)(t)
 =\sum_{m\ge2}a(m)F(t-\log m),
 \qquad
 a(m)=(-1)^m.
\tag{R-28001.1}
\]

Equivalently,

\[
 (\mathcal TW)(x)
 =\sum_{k\ge1}\bigl[W(2kx)-W((2k+1)x)\bigr].
\]

All sums are finite at fixed `t` or `x` because the profile is causal / compactly supported.

## 2. Dirichlet-convolution powers

Iteration gives exactly

\[
 \boxed{
 \mathcal U^jF(t)
 =\sum_{n\ge2^j}a^{*j}(n)F(t-\log n),
 }
\tag{R-28001.2}
\]

where `*` is Dirichlet convolution.  For `j=2`, the first coefficients are

\[
 a^{*2}(4)=1,
 \qquad
 a^{*2}(6)=a(2)a(3)+a(3)a(2)=-2.
\tag{R-28001.3}
\]

No integer `n=5` can occur as a product of two integers at least two, and the next possible product after six is eight.  Consequently, throughout the exact interval

\[
 \log6<t<\log8,
\]

one has

\[
 \boxed{
 \mathcal U^2F(t)
 =F(t-\log4)-2F(t-\log6).
 }
\tag{R-28001.4}
\]

## 3. Exact loss of monotonicity

Take the right derivative at `t=log 6`.  Since

\[
 F'(u)=e^{u/2}\left(1+\frac u2\right)
 \qquad(u>0),
 \qquad F'(0+)=1,
\]

(R-28001.4) gives

\[
 \left(\mathcal U^2F\right)'(\log6+)
 =\sqrt{\frac32}
   \left(1+\frac12\log\frac32\right)-2.
\tag{R-28001.5}
\]

This quantity is strictly negative.  Indeed

\[
 \log\frac32<\frac12,
 \qquad
 \sqrt{\frac32}<\frac54,
\]

so

\[
 \sqrt{\frac32}
 \left(1+\frac12\log\frac32\right)
 <\frac54\cdot\frac54
 =\frac{25}{16}<2.
\]

Therefore

\[
 \boxed{
 \left(\mathcal U^2F\right)'(\log6+)<0.
 }
\tag{R-28001.6}
\]

Since increasing `t` corresponds to decreasing the physical ratio `x`, this says that the second continuum residual `\mathcal T^2W` is not nonincreasing as a function of `x`.  Thus the third central first-difference row necessarily has a negative continuum coefficient in a neighborhood of the product-six threshold.

## 4. Consequences

The following assertion is false:

```text
all continuum iterates of the central residual remain positive and decreasing,
and all later monotonicity defects are caused only by the finite lattice shift.
```

The first defect is already present before any `-1` lattice commutator is inserted.  It is the overlap of the two ordered factorizations

```text
6=2*3=3*2.
```

This identifies the first necessary mixed-radix repair.  A valid all-stage cascade must retain and recombine the binary and ternary channels; a purely binary central iteration cannot be certified by a continuum monotonicity argument.

The one-pass and two-pass positive packings remain unaffected.  The refutation applies only to the claimed all-order continuum monotonicity used to motivate later stages.

## 5. Proof boundary

Closed exactly:

- the Dirichlet-convolution formula for continuum iterates;
- the coefficient ledger through the first overlap;
- the strict negative derivative at `log 6`;
- the distinction between continuum and finite-lattice defects.

Not proved here:

- a binary–ternary repair of every later product overlap;
- a subpower debt theorem;
- RH.
