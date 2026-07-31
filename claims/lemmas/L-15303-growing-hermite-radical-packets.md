# L-15303 — Growing Hermite radical packets

Claim ID: `L-15303`  
Title: The self-dual Hermite sector supplies arbitrarily large independent blocks of exact compact near-radicals  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: `L-15301`; elementary Hermite/Fourier algebra; injectivity of the Mellin transform  
Scope: low-block construction for `L-14308` and `T-14302`

## Fixed-rank source packet

Let `H_j`, `j>=0`, be real even Hermite functions in one common self-dual
Fourier sector:

\[
 \widehat H_j=H_j.
\]

For example, take indices `0,4,8,...` in the standard convention. Assume
`H_0(0) != 0` and put

\[
 \phi_j=H_0(0)H_j-H_j(0)H_0,
 \qquad 1\le j\le M.                         \tag{1}
\]

Then

\[
 \widehat\phi_j=\phi_j,
 \qquad
 \phi_j(0)=0,
 \qquad
 \int\phi_j=\widehat\phi_j(0)=0.            \tag{2}
\]

The `M` functions are linearly independent: comparison of the independent
Hermite coefficients `H_1,...,H_M` in a vanishing linear combination forces all
coefficients to be zero.

Thus the two codimension-two source conditions collapse to one condition inside
a self-dual Fourier sector.

## Compact exact packet

Apply `L-15301` to each `phi_j`, using one common cutoff scale `R` and one fixed
correction bump. This gives compact even sources

\[
 f_{j,R}\in\mathcal S_0^{\rm ev},
 \qquad 1\le j\le M,                         \tag{3}
\]

with `f_{j,R}->phi_j` in Schwartz topology. Their arithmetic images

\[
 r_{j,R}=E(f_{j,R})
\]

belong to the exact global Weil radical.

Using the smooth multiplicative support cutoff from `L-15301`, write

\[
 r_{j,R}=k_{j,R}+t_{j,R}.
\]

For every fixed `M` and every fixed multiplicative Schwartz seminorm `q`,

\[
 \max_{1\le j\le M}q(t_{j,R})\longrightarrow0. \tag{4}
\]

Since every `r_{j,R}` is radical, polarization of `L-14309` gives

\[
 Q_W(k_{i,R},k_{j,R})=Q_W(t_{i,R},t_{j,R})\to0 \tag{5}
\]

and

\[
 Q_W(k_{j,R},\cdot)=-Q_W(t_{j,R},\cdot)\to0.   \tag{6}
\]

The identities are exact; only the limits use continuity.

## Growing diagonal packet

There is an increasing sequence `R_M -> infinity` such that the first `M`
targets obey

\[
 \max_{1\le i,j\le M}
 |Q_W(k_{i,R_M},k_{j,R_M})|<\frac1M          \tag{7}
\]

and every selected continuous residual seminorm is below `1/M`.

For each finite `M`, choose `R_M` using (4)--(6), then enlarge it to make the
sequence increasing. Therefore the positive program has exact localized
near-radical blocks of arbitrarily growing finite rank; it is not restricted to
one guessed prolate ground direction.

## Transform limits

For each fixed `j`,

\[
 \widehat{k_{j,R}}(z)\longrightarrow
 \zeta\!\left(\frac12-iz\right)\mathcal M\phi_j(z) \tag{8}
\]

locally uniformly on closed critical substrips. The auxiliary factor is not
identically zero because `phi_j` is nonzero and the Mellin transform is
injective.

Each individual limit is sufficient for `T-15301` if finite real-rooted
spectral transforms approach it.

## Relation to the block lower-floor route

`L-14308` asks for a finite block containing every near-radical mode. L-15303
supplies an exact source-domain family whose low block and cross residuals can be
made small simultaneously. It removes dependence on:

1. one simple ground state;
2. one `h_0/h_4` coefficient ratio;
3. an interval-truncated source outside the exact radical domain.

## Remaining decisive gap

L-15303 does not prove that its span contains every dangerous low direction of
the localized Weil operator. The missing theorem is a quantitative principal-
angle estimate between:

- the low spectral/prolate packet selected by `L-14310/L-14311`; and
- the repaired Hermite-radical packet above.

A vanishing subspace-angle bound, together with complement coercivity, would
feed directly into the exact block Schur floor of `T-14302`.

## Status boundary

The finite Hermite algebra and diagonal argument are elementary. The imported
`E` interfaces, form continuity, and any production subspace-angle estimate
remain to be independently audited. No RH proof is claimed.