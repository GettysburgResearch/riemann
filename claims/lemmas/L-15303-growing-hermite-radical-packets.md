# L-15303 — Growing exact Hermite radical packets

Claim ID: `L-15303`  
Title: One self-dual Hermite sector supplies arbitrarily large independent blocks of exact Gaussian-tailed Weil radicals  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: the Connes--Consani `E`-range radical theorem; the Gaussian tail contraction method of the base `L-14312`; elementary Hermite/Fourier algebra  
Scope: candidate radical-like block for the corrected low-packet split of `L-15304`

## Exact source packet

Let

\[
 H_0,H_4,H_8,\ldots
\]

be real even Hermite functions in one self-dual Fourier sector, normalized so
that

\[
 \widehat H_{4j}=H_{4j}.                     \tag{1}
\]

Assume `H_0(0) != 0` and define

\[
 \boxed{
 \phi_j=H_0(0)H_{4j}-H_{4j}(0)H_0,
 \qquad j\ge1.}                              \tag{2}
\]

Then

\[
 \widehat\phi_j=\phi_j,
 \qquad
 \phi_j(0)=0,
 \qquad
 \int_{\mathbb R}\phi_j
 =\widehat\phi_j(0)=0.                       \tag{3}
\]

Thus every `phi_j` lies in the exact codimension-two even Schwartz source
space. The family is linearly independent: in a finite relation, comparison of
the independent coefficients of `H_4,H_8,...` forces every scalar to vanish.

For

\[
 r_j=\mathcal E(\phi_j),                     \tag{4}
\]

the imported global theorem gives

\[
 Q_W(r_j,g)=0                                \tag{5}
\]

for every admissible test vector. No finite prolate approximation and no source
Schwartzification are required.

## Gaussian-polynomial tails

Each source `phi_j` is a polynomial times `exp(-pi x^2)`. Its logarithmic
arithmetic representative

\[
 R_j(t)=r_j(e^t)
\]

therefore has double-Gaussian decay at both ends, with constants depending on
`j` only through a finite polynomial degree and coefficient bound.

For support half-width `a`, write

\[
 k_{j,a}=1_{[-a,a]}R_j,
 \qquad
 t_{j,a}=R_j-k_{j,a}.                        \tag{6}
\]

The term-by-term archimedean, boundary, and prime-translation argument of the
base Gaussian-tail theorem applies to every fixed finite collection. Therefore,
for each fixed `M`, there are constants `C_M,D_M` such that

\[
 \max_{1\le i,j\le M}
 |Q_W(t_{i,a},t_{j,a})|
 \le C_M e^{-\pi e^{2a}/2},                 \tag{7}
\]

and the complete cross map from the first `M` localized vectors into any
Hardy-normalized localized complement obeys

\[
 \sup_{\|g\|_{a,\tau_a}=1}
 \left(\sum_{j=1}^M|Q_W(k_{j,a},g)|^2\right)^{1/2}
 \le D_M e^{-\pi e^{2a}/2}.                 \tag{8}
\]

The exponent `1/2` is a deliberately weakened display; any fixed polynomial
loss is absorbed by increasing the support threshold. A production theorem may
retain the sharper polynomial-times-`exp(-pi e^(2a))` form.

By radicality and polarization,

\[
 Q_W(k_{i,a},k_{j,a})=Q_W(t_{i,a},t_{j,a}),  \tag{9}
\]

so (7) controls the complete finite low block, not merely its diagonal.

## Growing diagonal sequence

There exists an increasing sequence `a_M -> infinity` such that

\[
 \max_{1\le i,j\le M}
 |Q_W(k_{i,a_M},k_{j,a_M})|<M^{-1}          \tag{10}
\]

and the first-`M` cross-map norm in (8) is below `M^{-1}`.

For each fixed `M`, choose `a_M` large enough using (7)--(8), then enlarge it to
make the sequence increasing. Thus exact localized near-radical blocks of
arbitrarily large finite rank exist unconditionally.

## Transform limits

For every fixed `j`, the Mellin transform has the form

\[
 \widehat r_j(z)
 =\zeta\!\left(\frac12-iz\right)\Phi_j(z),  \tag{11}
\]

where `Phi_j` is the nonzero Hermite Mellin factor. The localized transforms
converge locally uniformly to (11) as `a->infinity`, because the double-Gaussian
tails vanish in every fixed Hardy substrip.

## Interaction with certified zero evaluations

Every transform in (11) vanishes at every zeta zero. `L-15304` therefore
implies that these packets can approximate only the certified-zero near-kernel
of a complete low-symbol packet when their tails are small. They are **not** a
candidate approximation to the entire low packet.

The corrected use is:

```text
complete low packet
  -> certified-zero near-kernel R_a
     + evaluation-visible block V_a
  -> fit a finite subset of {k_(j,a)} only to R_a
  -> certify V_a directly.
```

## What remains

The theorem supplies growing exact radical blocks and explicit tail decay. It
does not prove:

1. that their span captures the zero-evaluation near-kernel of the arithmetic
   low packet;
2. a uniform Gram condition as both rank and support grow;
3. a positive lower floor for the evaluation-visible block;
4. the cofinal Schur envelope required by `T-14302`.

## Status boundary

The Hermite algebra and diagonal existence argument are elementary. The exact
Gaussian cross-form bounds import the normalization and termwise estimates of
the base radical-tail theorem. No RH proof is claimed.