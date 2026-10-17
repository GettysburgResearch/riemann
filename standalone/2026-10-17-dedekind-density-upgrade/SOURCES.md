# Sources, exact uses, and inspection boundaries

## CT: the general-field theta and Poisson construction

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta
functions*, Hexagon 2610.00200v2, version dated 14 October 2026.

https://hexagonmath.org/2610.00200v2
https://hexagonmath.org/pdf/2610.00200v2
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The v2 LaTeX was read through the public web viewer. The load-bearing sections
inspected are: the principal Mellin detector and descent; Section 7's allowed
generators, zero extensions, and Kummer frequencies; Section 9's reflected
moment and explicit arbitrary-fixed-M>1 proof; Section 10's additive norm;
Section 11's full Poisson factorization and correction domain/nonvanishing;
Sections 12--13's height, reciprocal and contour comparison. The original
Table 1 was also inspected as a rendered PDF page and independently reproduced
by test_verify.py. The requested v1 PDF has a different theorem (1-1/6000);
no v1 exponent is substituted for v2 here.

External mathematical inputs: the complete general-field theta/reflection
and common-prime Poisson identities, their fixed local data, and their analytic
estimates. CT in turn imports the OpenAI primitive construction and classical
metaplectic/Hecke/large-sieve results. We have NOT independently rebuilt those
foundations. We are not importing only CT's final 31/32 theorem and pretending
that it alone implies 23/24. The explicit rescalable estimates are necessary.

The current Lean repository snapshot discussed in #948/#949 is not rebuilt,
re-audited, or asserted to formalize our refinement. No upstream proof files
or entire paper bytes are vendored in this packet. The source is version-linked;
container network downloads failed, while the web viewer supplied the text.

## DF: stronger exceptional-family density

Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1, posted 2 October 2026.

https://arxiv.org/abs/2610.04045
https://arxiv.org/html/2610.04045v1

Inspected: Theorem 1.1; the precise squarefree versus sixth-power-free indexing;
Corollary 1.5; Sections 2.1--2.3 on the Kummer/ray-class family and its generator
choices; multiplicativity and primitive conductor facts; the complete displayed
zero-detector inequality and optimization in the proof of Corollary 1.5.
The full proof of the large-sieve theorem itself was NOT independently checked.
The statement is imported as an unconditional preprint theorem.

The sixth-power-free restriction is essential. Frequency norm means the norm
of the full ideal with exponents 0,...,5, NOT the norm of its radical. Fixed
S-unit twists are treated by our PROOF Sections 2--3; they are not silently
covered by changing the wording of DF's corollary. No infinite-order angular
character is used in the zero-density application.

## BGL: the analytic detector and squarefree mean-value input

Valentin Blomer, Leo Goldmakher, Benoit Louvel, *L-functions with n-th order
twists*, arXiv:1112.1650; published IMRN 2014, no. 7, 1925--1955.

https://arxiv.org/abs/1112.1650
https://arxiv.org/pdf/1112.1650

Inspected the preprint's Section 5, especially (5.1), (5.3)--(5.5), and the
full-column decompositions, with PDF pages 18--19 also rendered. Theorem 1.3's
squarefree large sieve is an imported input, not independently reproved. The
analytic zero detector (5.3), originally following Heath-Brown, is imported
explicitly; its complete-column and fixed-twist arithmetic adapters are
spelled out in PROOF Section 3. No GRH-dependent estimate is imported.

## Repository context and attribution

Live #955 was read at head 6d3d69c7896e3a5d61d1f67e4627125257398ec7, including
its ATTACK_AND_SOURCES.md. It still leaves the fixed-principal-center bound
open. Metadata for #948--#954 and the prior local import's parameter discussion
were used for orientation. No unreviewed moment or compensation conjecture
from those packets is an analytic premise here. Earlier import and parameter
reconstructions are credited; the new change is the DF density/family adapter
and the different all-field zero-free budget.

A limited repository/literature search was made for overlapping deductions;
it was not an exhaustive priority audit. We claim an improvement relative to
CT's stated v2 boundary, not that no other author has independently found it.

All finite tests and the written composition have the same author. There was
no independent mathematical referee, proof-assistant build, full upstream
source replay, remote CI result, or full-repository validation this pass.
