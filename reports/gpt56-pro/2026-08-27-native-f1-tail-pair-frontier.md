# Native F1 tail-pair frontier — checkpoint report

Date: 2026-08-27  
Durable PR: #730  
Base head: `b3114562acbeb8c5890ef7a5fc59eed8db71d29a`

## Executive scientific verdict

The latest correction on PR #719 changes the source genealogy of the F1
programme.  The harmonic equal-pair Euler–Beta completion is not a viable
producer: it has a deterministic negative semiprime main of order

\[
\sqrt X\frac{\log\log X}{\log X}.
\]

The correction does not refute every cutoff-dependent balanced F1 packet.
Those packets carry the coefficient \(b_U\), not \(\mu\), and
\(b_U(c)=0\) for \(c\le U^2\).  The exact failure was the source-identification
arrow from the harmonic completion to the balanced core.

This checkpoint retires that arrow and rebuilds the geometric route directly
on the ordinary-Möbius same-\(K_1\) scalar.

## New exact source algebra

Let

\[
\nu_U=\mu\mathbf1_{n>U},
\qquad
\mu_U=\mu\mathbf1_{n\le U},
\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\]

The identities

\[
a_U=\mathbf1*\nu_U,
\qquad
a_U*\mu=\nu_U
\]

immediately give

\[
\boxed{a_U*a_U*\mu=a_U*\nu_U=\mathbf1*\nu_U*\nu_U.}
\]

Thus the historical balanced trilinear is actually one ordinary cross-product
of two long fields.  Both vanish below \(U\).  This removes one entire source
coordinate without an estimate.

There is also a complete prime-color family.  Any coloring of the primes into
two sets gives

\[
\mu=\mu_\chi^+*\mu_\chi^-,
\]

and hence

\[
a_U*a_U*\mu
=(a_U*\mu_\chi^+)*(a_U*\mu_\chi^-).
\]

The local rigidity theorem shows that these endpoint colorings are the only
ordinary squarefree two-factor compactifications with no quadratic local
term.  The Chow midpoint is available only before physical compactification,
where \(h_p^2=0\).

## New F1/Hodge coordinate

The positive half-kernel \(A\) satisfies

\[
K_1=(D+\tfrac32)(D-\tfrac12)(A*_MA).
\]

For either the extreme tail pair \((\nu_U,a_U)\) or any colored pair, let
\(F^+,F^-\) be the corresponding fields through \(A\).  In logarithmic
coordinates define

\[
\mathcal D_\chi(x)
=
\frac14\|F^+_\chi-R_xF^-_\chi\|_2^2.
\]

Then the derivative same-\(K_1\) balanced current is exactly

\[
\boxed{
\mathcal B_U^{K_2}
=-2D(D+\tfrac32)(D-\tfrac12)\mathcal D_\chi,
\qquad K_2=DK_1.
}
\]

The color dependence of \(\mathcal D_\chi\) is only an additive constant.
Therefore the conclusion-facing differential mismatch is a flat prime-color
Hodge invariant.

This is not a positivity proof.  It is a source-exact replacement for the
invalid completed square: the live packet is a signed third-order variation of
one nonnegative mismatch energy.

## New exact discrete scalar

The derivative kernel is supported on `[1,16]` and is affine in `sqrt(y)` on
four dyadic bands.  For

\[
c_n=\frac{\mu(n)}{\sqrt n},
\]

put

\[
P(x)=\sum_{n\le x}c_n,
\qquad
Q(x)=\sum_{n\le x}\frac{c_n}{\sqrt n},
\qquad
W(x)=3P(x)-4\sqrt xQ(x),
\]

\[
\Delta_4=(I-S)^2(I-\sqrt2S)^2.
\]

The exact right sample is

\[
G_2(m+)=-\Delta_4W(m).
\]

The left sample is recovered by one atomic version of the same filter.  Its
weighted dyadic cost is `O(M^(-1/2))`.  Since every integer cell is affine in
`sqrt(X)`, its negative logarithmic area is an explicit elementary function
of the two endpoint values.  No quadrature, smoothing, or pair-owner tensor
remains.

## Correct conclusion interface

Freeze

\[
U_j=\lfloor2^{j/6}\rfloor
\]

on each dyadic block.  The zero moment of \(K_2\) and bounded variation of its
lattice profile give, after the finitely many initial blocks are absorbed, a complete Type-I estimate `O(X^(-1/6))`.  The remaining
balanced row is precisely the tail-pair mismatch above.  Hence

\[
\boxed{
\mathrm{NATIVEF1XD}_{105504}
\Longleftrightarrow
\mathrm{NATIVECELL}_{105504}
\Longleftrightarrow
\mathrm{RH}.
}
\]

The first condition is geometric; the second is a one-dimensional exact
arithmetic cell functional.  Neither is proved in this checkpoint.

## What this changes strategically

The branch should no longer spend effort proving positivity or a fourth moment
for the harmonic owner/core completion.  That source is now known to have the
wrong leading sign.

The live routes are instead:

1. **Tail-Hodge variation:** exploit the exact relation
   `a_U=1*nu_U` inside the reflected mismatch, retaining cross-scale signs.
2. **Discrete cell deficit:** attack the explicit `Delta4 W` endpoint sequence
   directly, perhaps through dyadic martingale or signed variation methods.
3. **Native near-collision:** square only after the complete ordinary-Möbius
   source is formed; retain the resulting signed off-diagonal rather than an
   absolute occupancy bound.
4. **Same-K1 largest-prime/Vaughan transport:** use the already-reviewed
   `L-103201` equivalence to choose whichever native terminal coordinate has
   the clearest arithmetic cancellation.

A source-blind Hodge, Schur, or coefficient-energy argument is still ruled out.
Any closure must use the Möbius tail signs, not only the positivity of the
mismatch energy.

## Authentication

```text
PASS_T105500_NATIVE_F1_TAIL_PAIR
e25255643bfd11e9fc931b4484189d0f6178bcf5537f39d734acb0b3da84a386
finite checks: 161264
rh_established: false
```

The finite diagnostic through `X=5000` is retained only as a regression test.
