# Exact sources and dependency boundary

## Current repository sources read in this pass

| PR | Exact head | File and Git blob | Use |
|---|---|---|---|
| #989 | `0162599b1373341b0b1622d1273c075da0f147b5` | `standalone/2026-10-18-two-mollifier-law/PROOF.md`, blob `7e79986c4a9b6a0cc9ddc08997481011f0d899b2` | Full proof read; source comparison only. Its capped family law is not an input. |
| #989 | same | `VERTICAL_CAP_AUDIT.md`, blob `4ba08daab084fb71de0122db299cff434bbede6d` | Full local-cap calculation read; not an input. |
| #990 | `5f902c2d3591ea240d3f297083b2e643b4b16b12` | `standalone/2026-10-18-uniform-growing-native-moments/PROOF.md`, blob `2af2ae4c567bc2ae36604562513f70011d828188` | Full growing-order proof read. Its CT 31/32 and de Faveri contracts are not inputs here. |
| #991 | `b4d97d837214cf14fc09c093f66a50e798288afa` | `standalone/2026-10-18-chebyshev-critical-extraction/PROOF.md`, blob `86ba15bcc5bc86ce26994abca4d979b62315558f` | Exact complete translation source, unit, one-sided continuum and Mellin normalization. Those elementary identities are rederived here. |
| #991 | same | `FIXED_SHIFT_TARGET.md`, blob `17015195c9b338e397fef7c5b34226d64c8e9218` | Fixed-measure comparison and pole argument read in full. The present one-shift chain and bounded large-shift transfer are separate proposed deductions. |

These heads were open draft PRs at the time of the reads. Reading their
mathematics is not independent acceptance of every claim or a replay of their
checkers. No code from these PRs was executed in this component's validation.
The exact #991 source descends from #980's same deformed ideal coefficients;
this packet does not rename those coefficients as native mu_F.

The reviewed baseline `AGENTS.md` and current `docs/REVIEWING.md` (blob
`de7a9b67e1332d825c1688db07a0887e324f5ccb`) require an exact frozen identity,
complete scope and independent reconstruction before mathematical acceptance.
This is a standalone proposed component, with inherited claims unchanged.

## External theorem actually imported

Terence Tao, **The logarithmically averaged Chowla and Elliott conjectures for
two-point correlations**, Forum of Mathematics, Pi 4 (2016), e8, 36 pages,
DOI [10.1017/fmp.2016.6](https://doi.org/10.1017/fmp.2016.6).

The full publisher PDF was retrieved and its theorem statement and scope
read, especially published Theorem 3 and Corollary 5 on pages 5-6 and the
following nonpretentiousness discussion on page 7:

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/48514F53D73B2C1277BD7232630F0694/S2050508616000068a.pdf/the-logarithmically-averaged-chowla-and-elliott-conjectures-for-two-point-correlations.pdf

Preprint identifier: [arXiv:1509.05422](https://arxiv.org/abs/1509.05422).
The publisher's numbering is used here. The imported result concerns
logarithmic averages for bounded multiplicative functions satisfying its
uniform strong nonpretentiousness condition. It does not give a rate uniform
in a growing affine shift. The proof's application to a(p)=-1+1/p uses only
the bounded change sum_p p^(-2) in that condition. The whole entropy-decrement
argument was not independently reproduced by this packet's author or checker.

The author's original discussion was also read:

https://terrytao.wordpress.com/2015/09/18/the-logarithmically-averaged-chowla-and-elliott-conjectures-for-two-point-correlations-the-erdos-discrepancy-problem/

The publisher theorem, rather than that discussion or search snippets, is the
analytic premise. A recent effective-window preprint appeared during search,
but its body could not be retrieved and no assertion from it is used.

## Other classical inputs, and what is newly derived here

Ordinary and fixed-field zeta continuation, the functional equation, its Euler
half-plane, polynomial strip growth, and standard reciprocal bounds on a
fixed zero-free half-plane are used only at their classical scopes. Necessity
of the RH criteria explicitly assumes field RH before a contour is moved.
The prime number theorem is used to show divergence of an ABSOLUTE proposed
double sum over comparable distinct prime ratios, not to bound the signed
correlation remainder.

The exact causal convolution, finite-horizon norm bounds, full Gaussian
kernel, local squared/ray Euler factors, signed divisibility-sector limit,
and its elementary finite sign certificate are derived in this packet. They
are applications of classical Dirichlet convolution, elementary summation
and Gaussian integration; no worldwide novelty claim is made. The Tao
fixed-band application is an imported-theorem deduction, not a new proof of
logarithmic Chowla.

This packet's algebra, proof and checker share an author. Any review by other
agents must be recorded separately with exact file hashes and must not be
confused with independent human referee acceptance.
