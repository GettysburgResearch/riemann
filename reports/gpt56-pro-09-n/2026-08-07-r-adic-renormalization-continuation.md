# Full-problem continuation — integer-dilation renormalization

Date: 2026-08-07  
Agent: `gpt56-pro-09-n`  
Branch: `agent/gpt56-pro-09-n/202-haar-renormalization`  
Status: **PROPOSED; RH remains unproved and undisproved**

## Result

The dyadic Haar defect has been extended to every fixed integer dilation

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt),
 \qquad r\ge2.
\]

The new theorem proves, subject to independent review of the imported
screw/Landau interface,

\[
 RH
 \iff
 \mathcal D_r((2/r)\log n)\ge0\text{ eventually}
 \iff
 (-\mathcal D_r((2/r)\log n))_+=n^{o(1)}.
\]

The pole-descent map is

\[
 \rho\mapsto{1\over2}+{\rho-1/2\over r}.
\]

A positive mixture of finitely many dilation defects remains RH-nonnegative and
retains the converse: residue cancellation makes the parent multiplicity a
positive weighted average of descendant multiplicities, forcing an infinite
nondecreasing-multiplicity descendant path under any hypothetical off-line zero.

## Arithmetic gain

At the critical mesh, every level has the same complete square cutoff `q<=n^2`.
The exact prime weight is negative only below

\[
 q<n^{2/(r+1)}.
\]

The complete Lerch correction is termwise positive, and the polar term is an
exact nonpositive hyperbolic deficit. For `r=15,31,63`, the adverse prefix is
respectively `n^(1/8)`, `n^(1/16)`, and `n^(1/32)`.

The general Chebyshev–Riesz identity shows that its kernel is nonnegative on

\[
 e^2n^{2/(r+1)}\le x\le n^2,
\]

so every possible negative kernel value is confined to the same thin old
prefix.

## Finite Gram realization

The spectral polynomial factors exactly as

\[
 r^2(1-\cos x)-(1-\cos rx)
 ={1\over2}\sum_{0\le j<k<r}
 |(1-e^{-ix})(e^{-ijx}-e^{-ikx})|^2.
\]

Thus `D_r` is the exact finite Gram portfolio of the four-tap vectors

\[
 e_j-e_{j+1}-e_k+e_{k+1}.
\]

This supplies a stable dependence-preserving prime producer and embeds the
single-scalar global criterion directly in the repository's complete FIR screw
hierarchy.

## Exact regression

`X-20202` verifies with `Fraction` arithmetic:

- the `r=5` prime threshold exponent `1/3`;
- negative/zero/positive prime-weight rows;
- the positive Lerch numerator and lower bound;
- the positive-mixture residue balance;
- the dilation cocycle with an independently bound expected value.

Eight tests pass locally. The proof object is

```text
8a2d2a52203a38293cd3e2eeb904045a9b34e6404b9d3735ef3a6851295eee3f
```

and is synthetic only.

## Literature audit

The probability-law literature supports the relevance of the real-axis route:
there are unconditional off-center reciprocal-xi Lévy/GGC structures, and modern
Nakamura–Suzuki criteria make central infinite divisibility RH-equivalent.
However, positivity of an off-center representing measure does not survive
analytic continuation automatically. A central positive Thorin measure or an
explicit measure for `L_2` is the theorem to prove, not an imported shortcut.
`R-20201` records this boundary.

## Cross-route integration

A detailed connection was posted to PR #219. In its notation `Psi=F-G`, the
new statistic is the renormalized polygon chord

\[
 r^2F(t)-F(rt)+G(rt)-r^2G(t).
\]

The recommended joint attack is a block mass-transport or Selberg/prime-pair
identity that pays the explicit archimedean chord using the long nonnegative
prime band while isolating the short prefix.

## Exact remaining theorem

For one fixed `r` or one fixed positive mixture, prove

\[
 (-\mathcal H(n))_+=n^{o(1)}.
\]

No finite ladder, absolute PNT estimate, or analytic continuation of an
off-center probability measure establishes this. The serious live mechanisms
are:

1. prime-polygon quantile transport;
2. Selberg/prime-pair positive-square decomposition;
3. an all-positive real-axis Stieltjes continued fraction.
