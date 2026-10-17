# Sources, scope and credit

All source inputs are stated unconditionally in their cited versions. Imported
theorems are not independently reproved or formalized here. The new proofs use
classical approximate functional equations, Holder/Minkowski, zero detection,
Euler-factor masks, contour shifting and Mellin uniqueness. None of these general
methods is claimed new. The specific norm-exponent improvement and CT-family
composition are proposed additions relative to the inspected repository work;
a limited literature search does not establish global priority.

## 1. De Faveri: the sixth-power-free sieve and detector

Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1.
https://arxiv.org/html/2610.04045v1

Read in the primary HTML: Theorem 1.1; Sections 2.1--2.5 character construction,
allowed ideal representatives and twists; the AFE treatment in Sections 8--9;
and the complete detector calculation in the proof of Corollary 1.5, Section 9.
The full detector was reread after completing our proposed derivation.

The row AND column indices of Theta_6 are sixth-power-free, not squarefree.
The indexing norm is the full ideal norm. The four sieve monomials are
U,V,U^(5/6)V^(1/3),U^(1/3)V^(5/6). PROOF.md reconstructs the complete-column
extension rather than silently replacing AFE columns by flat columns.
The fixed-twist/generator adapter follows the separately frozen #959 source.

The count 43/60 is NOT a quotation from this paper. It is the new proposed
deduction obtained by retaining the exceptional subset in BGL's detector,
using the fourth moment, and solving the resulting self-selected inequality.
The old exponent 8/11 is obtained by the source's displayed middle-range
formula at sigma=3/4. Comparison concerns U powers at sufficiently small
polynomial height; we make no claim to match optimal T dependence.

## 2. BGL: pre-Cauchy zero detection and the central second mean

Valentin Blomer, Leo Goldmakher and Benoit Louvel,
*L-functions with n-th order twists*, arXiv:1112.1650.
https://arxiv.org/pdf/1112.1650

Read the primary Section 5 and rendered PDF pages 18--19 (PDF indices 17--18),
especially (5.1),(5.3),(5.4),(5.5), including the complete-column decomposition.
The page containing (5.3) and the next page were reread and rendered again
at final proof checking. Equation (5.3), BEFORE its first Cauchy application,
is the essential imported analytic detection inequality. DF explicitly adopts
this detector for the flat family. Keeping a row subset before summation is
explained in PROOF.md; it is not an assumed fourth-moment improvement to the
already optimized final density formula. The mollifier and detector coefficient
arrays remain common across the rows after the standard analytic separations.

The AFE, zero detector and their derivation in the cited prior analytic
literature are imported, not rebuilt from foundational complex analysis here.
A mistake in the subset/height interface would invalidate our density theorem.
No GRH-dependent statement is used.

## 3. CT v2: primary reflection and Poisson interfaces

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta
functions*, Hexagon 2610.00200v2.
https://hexagonmath.org/2610.00200v2
https://hexagonmath.org/pdf/2610.00200v2
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The v2 landing page, PDF and actual TeX were available through the web reader.
Freshly read the separated reflection/profile estimates in Section 8, the
quadratic-family and dyadic argument in Section 9, the unsimplified additive
normalization in Section 10, and the triple Mellin factorization, correction
domain and principal nonvanishing in Section 11. The principal nonvanishing
statement is Lemma 11.1, not the incorrect Lemma 11.2 citation found previously.

The short-support estimate is NOT imported by substituting M<1 into CT's
long-support proposition. It is proved in the recovered REFLECTED_MOMENT.md
from the unrestricted reflection and quadratic sieve. That full recovered
argument was reread against these primary formulas. The L<1 effective-length
case, the moving n cutoff, beta masses, original coprimality/nonunit conditions
and balanced S-unit generator multiplicity were checked in the written proof.
This was a same-author analytic reconstruction, not an independent referee.

The current global composition retains CT's xi+z Gaussian and z,w decay on
horizontal and original-line tails, including Im z approximately -Im xi.
No numerical original Table 1 parameter is transplanted to the new scale.
The main numerator H remains unchanged and is used only in its stated
nonvanishing half-plane Re s>2/3. No infinite-order angular twist is promoted
to the finite-order Hecke family.

## 4. Frozen internal sources

- #959: 7b845294207d96b883c1fa95028663082267804f,
  standalone/2026-10-17-numerator-mean-refinement/. The supplied source archive
  and live PR account give the complete numerator-mean/character adapter and
  Mellin normalization. It is credited, not independently certified here.
- Recovered short-support source: original thirteen-file tree
  a80cb7e2404e0f6835c47017597b6acbeb9cb264, base #959. Complete
  REFLECTED_MOMENT.md and PROOF.md read; original manifest and both checker
  modes freshly replayed. Old mutation records preserved, not freshly rerun.
- #961: 7bd275b44261fff93bb565a9342c44b7c66526f6,
  standalone/2026-10-17-review-imports-theta-escape/THETA_ESCAPE.md read in full
  through GitHub, plus its PR description. Its three-tie observation, low-
  powerful-row distinction, and warning on principal contour buffers are
  credited. OPEN-L is not an input. The other #961 files and newly imported
  papers are not claimed read in full or used as premises.
- #960 was inspected at PR-description scope only and supplies no premise.

The preceding native norm-divisibility/norm-fiber recoveries already occur in
#958; they are not newly duplicated, nor inputs to this density theorem.
Main/integrated status files are not edited. No upstream Lean build, axiom
audit, independent mathematical referee or full metaplectic reconstruction
has been performed. Upstream papers are linked, not falsely described as
byte-mirrored source archives.
