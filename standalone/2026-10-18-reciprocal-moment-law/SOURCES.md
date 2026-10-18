# Sources, prior work, and exact import boundaries

## Load-bearing external input

**Alexandre de Faveri, Optimal large sieve for fixed order characters,
arXiv:2610.04045 (October 2026).**
https://arxiv.org/abs/2610.04045

The primary parsed manuscript was read at the following interfaces in this
pass: Section 1.1 equation (1.2), the squarefree versus n-free conventions,
Theorem 1.1 and the four-term bracket displayed in (1.8); Sections 2.3--2.5
(the finite ray quotient, choice-dependent family, literal zeros, conductor,
multiplicativity and reciprocity); Section 3.1 (Hecke functional-equation
normalization); and the proof of Corollary 1.5 in Section 9, including the
first-range parameters x=1/2, y=2/(4-nq), q=2sigma-1. The parser omits some
isolated displayed equations, including the stand-alone Theorem 1.1 display;
the surrounding statement, (1.8), and the identical pinned #979 contract
supply the explicitly identified four-term input. No stronger orthogonal
kernel U+V is substituted. Direct fresh URL access failed once; the previously
returned primary-text reference was successfully reopened. No PDF/source bytes
are mirrored or assigned an invented hash; no deep proof or Lean build was
independently reconstructed.

The classical Hecke functional equation, convexity, polynomial vertical-strip
bounds, Mellin inversion, finite-group Fourier inversion, ideal counting,
Borel--Caratheodory and three-circles are also used. Their normalization and
application are written in the proofs. These methods are not claimed new.
The fixed-psi zero-density adapter is explained in RECIPROCAL_MOMENTS Section 2;
it is not claimed that DF's printed Corollary 1.5 literally states that variant.

**Blomer--Goldmakher--Louvel, L-functions with n-th-order twists,
IMRN (2014), 1925--1955; arXiv:1112.1650.**
https://arxiv.org/abs/1112.1650

Classical predecessor credited by DF. The abstract and DF's use of its Section
5 were consulted; no new PDF-page rendering or full proof audit of BGL is
claimed here. Our load-bearing density input is DF and its stated fixed-twist
adapter, not a silently strengthened version of BGL (5.3).

## Prior-art boundary: this is not the invention of a random Euler model

**Akbary--Hamieh, Two dimensional value-distribution of cubic Hecke
L-functions, arXiv:2103.14786.**
https://arxiv.org/abs/2103.14786

Primary introduction, Theorem 1.3, Proposition 1.5 and displayed local factor
(2.2) were inspected. This paper already proves unconditional value-distribution
results in the cubic Eisenstein setting using zero density and Euler laws.
Its squarefree-row local unit probability q/(q+1) is different from our
FULL n-free row probability (1-1/q)/(1-1/q^n). Neither this distinction nor
our error term is a worldwide novelty claim: an exhaustive comparison of
all complex/negative-moment literature was not undertaken.

**Akbary--Hamieh, Value-distribution of cubic Hecke L-functions,
arXiv:1805.00724.** https://arxiv.org/abs/1805.00724
The abstract and its description in the later paper were read for attribution,
not imported as a stronger all-n-free moment theorem. Classical Bohr--Jessen,
Jessen--Wintner, and Ihara--Matsumoto value-distribution methods are credited
through the explicitly inspected discussion in the later paper.

## Frozen repository sources and overlap

- #979, 28fe7f5e50106ca55ee0b383afb2a26575b1a8a8,
  standalone/2026-10-18-sparsity-adapted-moments/: source family, complete-column
  adapter, selected-mollifier motivation. The source proof/archive is available
  in the conversation. The 5/7 zero-density theorem is not assumed here.
- #976, bf845aa1d9d06b0ce62440edc5726de997a888db: live description and prior
  full-strip numerator argument in context; its numerator and theta moments
  are NOT reciprocal moments and are not imported as such.
- #975, edbc27b61208ccc7ee1fa99fa3f4e861f5a03452, and #974: transverse
  prime-detector context only. No CT correction or theta theorem is needed.
- #931: historical independent-prime model is credited from this conversation;
  no fresh full audit or claim to have proved its physical discrepancy occurs.
- #978: prior reflected-ratio packet already published, no recovery needed.
- #980, 5fb1aa5b52065369bdb04c12d40333d99aa27387: inspected live recovery
  checkpoint/critical-translation description. No new analytic input taken.

Publication on a child branch does not certify these inherited papers or
promote their global claims. Main and all existing source files remain intact.
