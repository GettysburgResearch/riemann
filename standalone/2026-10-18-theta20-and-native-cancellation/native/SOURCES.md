# Exact sources and analytic dependencies

## Repository sources read in full

| Source | Exact commit | Source path and Git blob | Use |
|---|---|---|---|
| #905 | `0f82df3bf1d0bc669a1bbca09f8404b77c6fecde` | `standalone/2026-09-21-native-covariance-compression/PROOF.md`; `d0c978936caecf5ab1532290f8fd92a2c0ce78b7` | Literal truncated Möbius source and strict Newton square step. Reproved here. |
| #988 | `86c156baa3f10296a26e066f5f4d276776b79c27` | `standalone/2026-10-18-native-amplitude-and-theta18/newton/PROOF.md`; `850157ee1386f7e0b554a5c82484da66da5ab8dc` | Prior complete low-product amplitude estimate. This packet instead groups complete reduced denominators and adds the square/core sector. |
| #848 | `99101457b32b6f10f4eda88ca998048404b860ea` | `standalone/2026-09-12-astra-crossing-cofinal/PROOF.md`; `0f9eac82fcbca61c7887a9fb71eb29d5a4181ce9` | Cofinal reciprocal crossings and the ALL-PREFIX limit log(1+F_Y)/log(Y+1) -> 2Theta-1. Full exact source copy retained at `sources/848_PROOF.md`. |
| #991 | `b4d97d837214cf14fc09c093f66a50e798288afa` | `standalone/2026-10-18-chebyshev-critical-extraction/PROOF.md`; `86ba15bcc5bc86ce26994abca4d979b62315558f` | Full current extraction theorem read for overlap; not an arithmetic upper-bound input. |
| #991 | same | `FIXED_SHIFT_TARGET.md`; `17015195c9b338e397fef7c5b34226d64c8e9218` | Full fixed-measure critical criterion read; no inference that its open energy bound is proved. |
| #990 | `5f902c2d3591ea240d3f297083b2e643b4b16b12` | `standalone/2026-10-18-uniform-growing-native-moments/PROOF.md`; `2af2ae4c567bc2ae36604562513f70011d828188` | Full growing-order recovery read. Its CT/de Faveri inputs are not used. |

These are exact source dependencies and overlap reads, not independent
approval of every conclusion in the source PRs. The #991 and #990 source
documents were also read. Baseline `AGENTS.md`, integrated current-result
summaries, and the native/multiplicative-window discussions were consulted;
the new proofs are separate proposed components and do not edit their claims.

For the sparse-cutoff consumer, cofinality alone is insufficient. The
load-bearing extra input is #848's actual exponent LIMIT at every prefix,
including its causal lower bound and generalized Littlewood upper bound,
with Theta=1 treated separately. The checker does not certify those infinite
analytic arguments. The present paper needs no density or spacing of the
crossings and performs no interpolation across omitted scales.

## Classical primary source actually used

Terence Tao, **A remark on partial sums involving the Möbius function**,
[arXiv:0908.4323v5](https://arxiv.org/abs/0908.4323v5), 5 October 2009.
The full seven-page [PDF](https://arxiv.org/pdf/0908.4323) was retrieved and
read, with its page-one version header checked. Theorem 1.1 (page 3) is the
uniform prime-semigroup reciprocal bound; equation (9) (page 4) is exactly
the coprimality-mask bound used here. Its elementary proof is reproduced
in Section 2. Equation (1) records the ordinary PNT consequence m(x)=o(1)
used for the balance limit. No uniform decay of m_d(x) as the mask varies
is asserted; only its uniform magnitude bound is used for C_Y(q).

The paper itself credits earlier related results. This packet makes no
worldwide priority claim for masked sums, Ramanujan modes, Jordan factors,
harmonic remainders, Mellin transforms, or the spacing argument.

Classical zeta continuation and the existence of nonreal zeros are used in
the reproduced Landau sign-change argument. The background facts were
checked against [DLMF 25.2](https://dlmf.nist.gov/25.2) and
[DLMF 25.10](https://dlmf.nist.gov/25.10). No numerical zero census is used.
The elementary divisor bounds, full Gaussian-free Mellin normalization,
square/core norm bound, and all tails used in the new component estimates
are proved in PROOF.md.

## Authorship and review boundary

The native proof and finite checker have one author. Other agents' exact-hash
reviews are separate evidence and are not independent human referee approval.
Finite executions authenticate the specified algebra and coverage only.
No physical CT projection, Hecke-family mean, character-family mean, or
unproved native square-root cancellation is an input to the new estimates.
