# Phase-locked safe-line carrier and two-row Mellin-Landau consumer

## Status

This is an unconditional theorem packet plus two explicit RH-bearing producer
targets. It is not an accepted proof of RH.

## Corrected carrier theorem

The raw centered-cubic carrier contains a continuous-prime mode of size
`exp(r/2)`. Its unweighted scale norm therefore diverges generically. Define
instead

\[
\mathcal G_C(r,t)
=e^{-r}\left[
\sum_{n\le e^r}\Lambda(n)n^{it}W_C(ne^{-r})
-\int_1^{e^r}x^{it}W_C(xe^{-r})dx
\right].
\]

Then

\[
\widehat{\mathcal G_C}(\xi,t)
=\widehat W_C(1+i\xi)
\left[-\frac{\zeta'}\zeta(1+i(\xi-t))
-\frac1{i(\xi-t)}\right]
\]

in the Abel boundary-value sense, and

\[
\|\mathcal G_C(\cdot,t)\|_2\ll\log^2(2+|t|)
\]

unconditionally.

The phase-lock

\[
P(z)=5-4\cos((\log4)z)
\]

has zeros at every critical-boundary lattice point. Therefore, for every
integer `m>=1`, the quotient

\[
\widehat A_{q,m}(\xi)
=\frac{P(\xi)^{2m}\widehat h_q(\xi)}
{\widehat k_C(-\xi)}
\]

has a residue-completed weighted inverse `B_(q,m)=exp(r/2)A_(q,m)` in the
Schwartz class. The filtered prime polynomial satisfies the legal identity

\[
S_{q,m}(t)-S_{q,m}^{cont}(t)
=\langle B_{q,m},\mathcal G_C(\cdot,t)\rangle.
\]

The remaining carrier theorem is a signed covariance inequality, not a raw
norm estimate.

## Two-row direct consumer

The fixed-row numerators are

\[
P_2(z)=2\,2^{-z}-1-3^{-z},
\]

\[
3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.
\]

If both vanish, putting `x=2^-z`, `y=3^-z` gives

\[
y=2x-1,
\qquad
-3(x-1)(x-2)=0.
\]

The only common zeros are `z=0,-1`. Hence every open-strip zeta zero survives
in at least one of rows two and three.

After removing primes two and three from the Möbius sieve, the two row
transforms are

\[
\mathcal C_j^{>3}(s)
=
\frac{C_j}{s^2(1-2^{-z})(1-3^{-z})}
+
\frac{P_j(z)}
{s^2\zeta(z)(1-2^{-z})(1-3^{-z})},
\qquad z=s+1/2.
\]

Thus positivity of only those two rows implies RH directly by Landau.
Their exact physical source is a positive `2,3`-smooth reservoir plus explicit
large-prime three/four-knot packets.

## Final boundary

```text
safe-line carrier normalization     proved at proposed analytic scope
critical-boundary pole cancellation exact
phase-locked cubic/Hermite identity exact
row-2/row-3 noncancellation          exact
LPTRP_23                             open / RH-bearing
SCID_PL                              open / RH-bearing
RH                                   unproved
```
