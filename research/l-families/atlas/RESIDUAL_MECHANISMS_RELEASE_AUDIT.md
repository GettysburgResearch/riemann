# Residual mechanisms release audit

## Verdict

The branch contains internally exact mathematics, exact finite experiments,
and formal models. It does not contain an RH or GRH proof.

The strongest paper-sized object is the combined marked and ambient
genus-two symmetric-power trace ladder through `Sym^10`. The strongest route
back toward RH is the FFPS restricted-frame mechanism, because it attacks
principal leverage after physical deletion. The latter still stops before
the varying-owner/conductor Wick-centered estimate and before any
average-to-principal individualization theorem.

“Internally exact” and “externally novel” are separate questions. The
proved marked `Sym^6/8/10` and ambient-ladder derivations replay for every
odd prime power rather than fitting a few fields. Finite-only and conditional
rows—notably `Sym^12`—are labelled separately. The surrounding
finite-field/cohomological machinery is established, and a specialist
literature search is still required.

## Graded result map

The proof grade is an internal audit grade, not peer review. RH criticality
distinguishes current direct relevance from possible upside.

| object | proof grade | defensible novelty statement | RH criticality |
|---|---:|---|---:|
| marked `Sym^6` law | A- | direct all-field formula not printed in the audited sources; likely close to consequences of established pointed-count machinery | C |
| marked `Sym^8` and `Sym^10` laws | A- | strongest candidate contribution: exact for all odd prime powers and not printed in the audited bounded/conjectural tables | C+ / B- as family mechanism |
| ambient `Sym^2,...,Sym^10` ladder | A- | exact boundary corollary and useful packaging; individual cohomology groups are not identified | C+ |
| `Sym^12` one-scalar inventory | A- | exact source-relative dependency theorem; isolates a project-defined Mobius-weighted aggregate of standard central coefficients but does not evaluate it | C+ |
| `Sym^12` finite cusp-trace scout | A as exact finite arithmetic | identifies the Fricke-negative weight-fourteen level-two channel at `p=3,5,7`; not interpolation or an all-prime theorem | C+ |
| `Sym^12` conditional defect identity | A as an exact reduction; imported premises remain open | Rösner's theorem gives the endoscopic channel; combining it with the exact project ambient identity and the defined Eisenstein/stable defects yields `Hhat_12=-L*f_-+Epsilon_Eis-Genuine` | C+ / B- as cohomological target |
| inverse cusp-channel filters | A | exact lattice and recurrence corollaries of the trace ladder | C+ |
| `Sym^10` finite rare-event tomography | A as an exact finite theorem | finite anatomy, not an all-`q` distribution or endoscopy theorem | D+ / C methodologically |
| scalar endpoint realization | A- | endpoint and seed are known; affine/twist orbit densities and the exact moment contribution are candidate additions | D+ |
| all-rank scalar-endpoint phase diagram | A | exact consequence of the constructed endpoint atoms; useful new packaging, not an endpoint classification or full-moment asymptotic | D direct / B- methodologically |
| high-rank Haar tail and boundary layer | A | exact and clean, including the mesoscopic and rank-scale crossover constants; external novelty uncertain and possibly folklore in harmonic-analysis pieces | D direct / B- methodologically |
| `USp(4)` virtual-character null module | A- | exact bounded representation-ring result; likely elementary but useful as a detector firewall | D direct / C methodologically |
| correlated and cyclic FFPS masks | A as formal tensor theorems | exact project-specific restricted-Gram optimizers; no global amplifier theorem | B now / A upside |
| checkerboard and cyclic source bridge | A- on one fixed fibre | corrects a real physical-invariance issue, extends it to exact order `k`, and proves a universal Wick-residual obstruction; the analytic lift remains open | B- |
| cyclic closure budget | A as exact linear algebra, conditional analytically | classifies the entire scalar-gate closure plane and isolates the one-sided `CYSEL` frontier; WCADD/WCKUM remain open | B / A upside |
| two-place cumulant defect | A | exact all-odd-`q` joint law and the first arithmetic residual for the renormalization model; external novelty unsearched | D direct / B methodologically |
| three-place elliptic interference | A | exact all-odd-`q` correlation and cumulant decomposition with an elliptic Frobenius trace; external novelty unsearched | D direct / B methodologically |
| multi-place squarefree `L`-identity | A | the Euler quotient is standard; the exact evaluation-character curve adapter, infinity/twist convention, degree-five geometric ladder, and connected-cumulant corollary are the packet contribution | D direct / B methodologically |
| six-place connected law and weight ceiling | A | exact corollary of the multi-place identity, Weil functional equation, set-partition formula, and symplectic exterior-character algebra; no external novelty claim | D direct / B methodologically |

## Best paper-sized theorem stack

Let

\[
 \mathcal H_5(q)=\{D\in\mathbf F_q[T]:D\text{ monic squarefree},\deg D=5\},
 \qquad P_D(u)^{-1}=\sum_{n\ge0}r_D(n)u^n.
\]

For every odd prime power, the branch proves

\[
 \sum_Dr_D(6)=-4q(q-1),
\]

\[
 \sum_Dr_D(8)
 =q(q-1)(-\Theta_{8,2}(q)-q-6),
\]

and

\[
 \sum_Dr_D(10)
 =q(q-1)((q-1)\Theta_\Delta(q)
 -\Theta_{8,2}(q)-\Theta_{10,2}(q)-q-7).
\]

Here the prime-power modular traces are Frobenius-root power sums, not a
naive use of Fourier coefficients at composite indices. The proofs use exact
reciprocal descent, Mobius/Euler algebra, elliptic quotient inventories, and
standard Eichler--Shimura trace inputs. The values at `q=3,5,7` are held-out
controls, not interpolation nodes.

Through the
[marked-Weierstrass adapter](function_field/GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md),
these are alternating compactly supported Frobenius traces on the marked
genus-two stack. Adding the independently rebuilt decomposable boundary gives

\[
 -2q,\quad -3q,\quad
 1-3q-q\Theta_{8,2},\quad
 1-4q-q\Theta_{10,2},\quad
 2-4q-2q\Theta_\Delta
\]

for the ambient `Sym^2,...,Sym^10` ladder. These are virtual alternating
traces, not decompositions of individual cohomology groups, motives, Galois
representations, or compatible systems.

The cleanest inverse-designed corollary is

\[
 H_D=r_D(10)-r_D(8)+r_D(4)-r_D(6),
\]

\[
 \sum_DH_D
 =q(q-1)((q-1)\Theta_\Delta(q)-\Theta_{10,2}(q)).
\]

The complete cancellation lattice and exact same-prime recurrence appear in
the [mixed-filter packet](function_field/GENUS2_MIXED_COHOMOLOGY_FILTER.md).

At the next rank, the one-step descent genuinely changes character. The
[`Sym^12` inventory](function_field/GENUS2_SYM12_ARITHMETIC_INVENTORY.md)
proves

\[
 T_{(12,0)}=\widehat H_{12}-2q-9-4\Theta_\Delta
 -\Theta_{8,2}-\Theta_{10,2},
\]

and after the decomposable boundary

\[
 \operatorname{Tr}(F_q,e_c(\mathcal A_2(w^1),V_{(12,0)}))
 =\widehat H_{12}+2-5q-q\Theta_{14,\Gamma_0(2)}.
\]

The finite scout then verifies

\[
 \widehat H_{12}(p)=-p\,a_p(f_-),\qquad p=3,5,7,
\]

for the Fricke-negative weight-fourteen level-two newform. This is exact
finite arithmetic, not an interpolation theorem.

The primary-literature comparison produces a more informative master
reduction. Write

\[
 \varepsilon_{\rm Eis}=e_{\rm Eis}^{S_5}-(2-5\mathbb L)
\]

and let `Genuine` be the stable/general `S5`-invariant channel, whose Euler
contribution is `-Genuine`. Rösner's theorem supports the endoscopic piece
`-L(f_++2f_-)`, so exact cancellation gives

\[
 \boxed{\widehat H_{12}=-\mathbb Lf_-+
 \varepsilon_{\rm Eis}-\mathrm{Genuine}.}
\]

BFG's formal nonregular continuation sets `Epsilon_Eis=0`; the conditional
`k=3` isotypical table predicts `Genuine=0`. Only together do they give the
clean all-`q` closure. Shmakov's printed Eisenstein pieces instead set
`Epsilon_Eis=L`, so the alternative relation retains `-Genuine`. This is not a
closed trace formula, but it reduces the higher-weight target to two sharply
separated cohomological questions.

For `q=p^r`, the expression `-L*f_-` means the Frobenius-root power sum
`-p^r(alpha_{-,p}^r+beta_{-,p}^r)`, not `-q` times a naive composite-index
Fourier coefficient.

## Primary-literature boundary

The following sources establish much of the surrounding language and
machinery.

- Bergstrom--Faber--van der Geer develop the marked level-two point-count
  framework in [Sections 1--3](https://arxiv.org/html/0803.0917#S1). Their
  exact computational data cover bounded odd fields in
  [Section 5](https://arxiv.org/html/0803.0917#S5). Theorem 4.2 and
  Corollary 4.5 are regular-only; Theorem 4.4 explicitly conjectures the
  `m=0` equivariant Eisenstein row used by formal continuation. The
  load-bearing expanded-endoscopy statement is
  [Conjecture 8.1](https://arxiv.org/html/0803.0917#S8.Thmconjecture1), while
  Section 10 gives conjectural examples rather than the general premise.
- [Rösner, Theorem 5.13](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf),
  proves the semisimplified inner/endoscopic contribution for `l>=m>=0`.
  Its natural six-Weierstrass-point action specializes at `(12,0)` to
  `-L(f_++2f_-)` after `S5` invariants.
- [Shmakov, Theorems 4.6.4--4.6.8](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf),
  supports the same inner channel, but its printed Siegel, Klingen, and Borel
  Eisenstein pieces specialize to `2-4L`, one Tate class away from BFG's
  formal `2-5L` continuation.
- [Bergstrom--Clery, Theorem 5.3 and Remark 5.4](https://arxiv.org/abs/2309.04388),
  makes the `k=3,j>0` isotypical decomposition conditional on BFG's
  nonregular conjecture. Combining that extension with the
  [official `(12,3)` table](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0)
  predicts no `[6]` or `[5,1]` channel, but that is not an unconditional
  vanishing theorem.
- [Clery--van der Geer 2026](https://arxiv.org/abs/2605.13300)
  unconditionally identifies the same quotient `A_2[w]=A_2[2]/S5` and gives
  a covariant/valuation description, but does not compute the `(12,3)`
  `S5`-isotypical dimension.
- [Clery--van der Geer 2018, pp. 1139--1140](https://ems.press/content/serial-article-files/26421)
  identifies the two rational weight-fourteen level-two expansions and their
  Fricke signs; in particular the finite scout's negative-sign target starts
  `f_-(Q)=Q+64Q^2+1236Q^3+...`. This coefficient provenance is separate from
  the 2026 structural quotient result.
- Bergstrom gives all-field pointed-hyperelliptic machinery through bounded
  weight in [Section 7](https://arxiv.org/html/math/0611813v2#S7), prints an
  unmarked weight-six result in
  [Theorem 11.6](https://arxiv.org/html/math/0611813v2#S11.Thmthm6), and
  explains the ramification-marked information in the broader package near
  [Remark 12.9](https://arxiv.org/html/math/0611813v2#S12.Thmthm9).
- Faber--van der Geer supply the level-one framework. Their regular formula is
  near [id413](https://arxiv.org/html/math/0305094#id413); the nonregular
  continuation at [id414](https://arxiv.org/html/math/0305094#id414) is
  explicitly prospective.
- Rudnick studies fixed finite field with genus tending to infinity in the
  [hyperelliptic ensemble](https://arxiv.org/abs/0811.3649). That is important
  context, but it is not the fixed-genus marked symmetric-power theorem here.
- Keating--Rudnick print the squarefree-character generating quotient
  `L(u,chi)/L(u^2,chi^2)` as
  [equation (9.7)](https://arxiv.org/html/1504.03444#S9.E7) and again as
  equation (10.4). The multi-place packet therefore makes no novelty claim
  for that Euler identity; it contributes the evaluation-character
  specialization, exact curve/infinity/twist adapter, and degree-five
  coefficient consequences.

Rudnick's Section 2.3 also fixes the closest standard analytic notation: for
an even degree-twelve quadratic `L`-polynomial, the packet's `Q_5(f)` is the
central completed coefficient `A_f^*(5)`. Thus the individual middle
coefficient is not new. The object isolated here is the project-defined
Mobius-weighted aggregate

\[
 \sum_{\substack{\deg f=12\\f\ \mathrm{squarefree}}}\mu(f)A_f^*(5),
\]

and its exact one-scalar role in the marked and ambient reductions. That
aggregate and the two displayed affine identities were not found printed in
the audited primary sources, although the BFG machinery gives bounded
numerical access to the relevant nonregular local system. This supports an
independently derived **source-relative reduction**, not a claim of global
novelty or a first computation of `Sym^12`.

The later source comparison does not turn the three finite matches into an
all-prime theorem. It exposes an exact one-Tate fork. Under Shmakov's printed
`2-4L` branch, the finite rows are compatible if `Tr(F_p,Genuine)=p` at
`p=3,5,7`; they contradict only the additional assumption `Genuine=0`. The same
ambient quotient and natural `S6` action occur on both sides, so no
open/ambient or outer-automorphism normalization escape was found.

The defensible release wording is therefore: the marked `Sym^6/8/10` and
ambient-ladder formulas are not printed in the audited sources, and this
branch supplies exact all-odd-`q` derivations beyond their bounded or
conjectural presentation. For `Sym^12`, the defensible claims are only an
exact one-scalar arithmetic reduction, a three-prime Fricke-negative match,
and an exact conditional defect identity. None is an unconditional
`Sym^12` evaluation for all odd prime powers, and none certifies that no
equivalent theorem exists elsewhere.

## Scalar endpoint correction

Howe's [Theorem 1.1](https://arxiv.org/html/math/0604413v1#S1.Thmtheorem1)
already lists the scalar supersingular endpoint Weil polynomials. Howe also
records `y^2=z^5+1` over `F_3` with Weil polynomial `x^4+9` in
[Section 5](https://arxiv.org/html/math/0604413v1#S5.p21).

Accordingly, the branch does not claim discovery of the endpoint or the seed
curve. Its distinct exact content is:

- an elementary reconstruction from `N_1=4,N_2=10`;
- two explicit square-affine twist orbits over `q=3^(4k)`;
- density exactly `1/(10q^3)` for each constructed orbit, hence only a lower
  bound of that size for the full endpoint population; and
- exact constructed contribution `286^m/(5q^3)` to the normalized absolute
  `Sym^10` moment.

The all-rank continuation replaces `286` by
`d_r=binom(r+3,3)`, proves the parity-sensitive signed subtotal, and gives
the exact constructed crossover surface
`m log d_r=3 log q+log 5`. The resulting fixed-`(q,r)` full absolute-moment
root limit is a positive-atom plus compact-character-bound theorem. It is
not an asymptotic formula for the full `(q,r,m)` phase diagram.

## FFPS criticality and firewall

The complete-frame theorem says that, for

\[
 G=\bigotimes_i(p_iI-J),
\]

arbitrary complex reweighting cannot beat the coherent uniform tensor.
Correlated hard deletion changes the metric to a principal submatrix and can
beat that complete-frame leverage. Cyclic quotient masks give exact positive
uniform optimizers and an explicit density dial.

This is not yet a global amplifier. The source audit proves that a raw core
Legendre label is not a function of `P*c^2`. A quartic orientation repairs it
inside a fixed owner quadratic sector and identifies its soft Fourier mode
with an existing double-nonprincipal Kummer channel. An exact-order-`2k`
root orientation does the same for every common exact-order-`k` cyclic mask.
But soft spectral containment does not re-invert the hard restricted Gram,
and every cyclic hard mask with improved leverage provably leaves a positive
conductor-dimensional Wick atomic term. The exact all-`k` centered projector
identity isolates the next analytic target; it does not prove it.

The current RH-bearing gate is therefore a globally recombined
varying-owner/conductor Wick-centered estimate plus an individualization
mechanism. No family average in this branch closes that gate.

The closure packet sharpens this statement. If `C` is the averaged rotated
hard current, `S` the selected Kummer trace, and `R` the residual Kummer
trace, then

\[
 A=C+R,\qquad K=S+R,\qquad P=A-K=C-S.
\]

The scalar WCADD/WCKUM measurements have kernel `(1,1,-1)` and control
exactly targets `uC+vS+wR` with `w=u+v`. Thus they conditionally close the
whole principal trace but cannot bound `C` or `S` separately. The smallest
new cyclic target is the one-sided upper estimate `CYSEL` for `S`; its lower
bound is already paid by the atomic diagonal.

## Moonshot conversion: arithmetic mixed-place theorems

The detector-renormalization packet originally stopped at an independent
compact model and named mixed-place cumulants as missing arithmetic data. The
[two-place packet](function_field/QUADRATIC_FAMILY_TWO_PLACE_CUMULANT_DEFECT.md)
now computes that first residual exactly for every odd prime power in the
squarefree-quintic family. For `X=chi(D(a))` and `Y=chi(D(b))`, it proves the
complete `3 x 3` joint law and exact defects through order six. Every allowed
nonzero channel begins at order `q^-4`; the odd channels vanish identically
for `q = 3 mod 4` and otherwise remember the oriented squareclass of `b-a`.
This is fixed-degree family coupling, not evidence for independent Euler
factors, a zero bias, or an RH implication.

The [three-place packet](function_field/QUADRATIC_FAMILY_THREE_PLACE_ELLIPTIC_INTERFERENCE.md)
then crosses from elementary local coupling to geometric spectroscopy. For
three distinct rational places it proves

\[
 \sum_{D\in\mathcal H_5(q)}
 \chi(D(a)D(b)D(c))=3(q-2)t,
\]

where `t` is the Frobenius trace of the oriented elliptic curve
`y^2=(a-z)(b-z)(c-z)`. Its exact third-cumulant defect is the sum of an
elementary pair term and `18(q-2)t/A`; when `q=3 mod 4` the pair term
vanishes. The elliptic contribution has Hasse upper-envelope scale
`q^-7/2`, versus `q^-4` for the pair channel. This realizes Frobenius
interferometry arithmetically, but it does not attach a new motive to an
individual detector or imply anything about zeros.

The [multi-place packet](function_field/QUADRATIC_FAMILY_MULTIPLACE_L_FUNCTION_IDENTITY.md)
shows that the preceding two rows are the beginning of one exact identity,

\[
 \sum_{n\geq0}\sum_{D\in\mathcal H_n(q)}\psi_A(D)u^n
 =L(u,\psi_A){1-qu^2\over(1-u^2)^m}.
\]

Its degree-five specializations progress from no one-place signal, through a
universal two-place channel, to elliptic traces at three and four places and
a genus-two trace at five places. At five places the middle reciprocal
coefficient cancels, leaving `(q^2-15)t`. This is a useful geometric
interaction hierarchy, but the quotient itself is the standard squarefree
character identity of Keating--Rudnick (their equations (9.7)/(10.4)); the
packet claims the exact adapter and specializations, not discovery of that
Euler product.

The connected version is more diagnostic. With
`N=q^4(q-1)` and `C=2q-3`, the fourth joint cumulant is

`[q^2-10+(4q-10)t_I]/N - 3C^2/N^2`,

so it has a universal `q^-3` background and an elliptic correction with
Hasse upper envelope `q^-7/2`. The fifth is

`(q^2-15)t_A/N - [3C(q-2)/N^2] sum_(|B|=3)t_B`.

Its leading Hasse envelope is genus-two and `q^-5/2`; the ten complementary
elliptic traces form a smaller `q^-15/2` correction. They generally differ
and cannot be replaced by ten copies of the five-place trace. This makes the
multi-place identity a finite geometric interaction hierarchy, not merely a
restatement of pair correlation. In particular, the order-two through
order-five exact/Hasse scales are `q^-4`, `q^-7/2`, `q^-3`, and `q^-5/2`.
This half-power sequence is a concrete warning for renormalization heuristics:
the full connected sequence can grow even though its leading channel changes
from a trace envelope to a universal background and back. The trace-dependent
`q^-7/2` and `q^-5/2` entries are Hasse envelopes, not distributional or
lower-bound theorems.

The
[six-place continuation](function_field/QUADRATIC_FAMILY_SIX_PLACE_CONNECTED_SATURATION.md)
then proves

`S_(5,6)=(q^2-21)t_A+(q-6)b_A-q^2+6q-21`

and subtracts every non-singleton partition profile `6`, `4+2`, `3+3`, and
`2+2+2` exactly. The resulting sixth cumulant differs from its raw moment by
`O(q^-7)`; its trace channel has Hasse ceiling `q^-5/2`, while the middle
coefficient and universal terms are `O(q^-3)`. Since
`b_A=(t_A^2-s_(2,A))/2`, this is also the first row in the marked-place
ladder that retains the second Frobenius power rather than only the first
trace.

The apparent five/six-place plateau is not the whole pattern. Normalize the
auxiliary Frobenius class to `U_A in USp(2g)` and put
`e_j=Tr(Lambda^j Std)(U_A)`. Exact coefficient extraction shows that the
parity-independent top-weight numerator channel is

`q^(5/2)(e_3-e_5)`.

Symplectic duality and primitive exterior powers identify this as
`chi_(omega_1)` for `g=2`, `chi_(omega_3)` for `g=3`, zero for `g=4`, and
`-chi_(omega_5)` for `g>=5`. Consequently the raw and connected nine-place
envelopes are `O(q^-7/2)`, while the split-infinity ten-place row is
`O(q^-3)`; proper partition products are too small to restore the cancelled
top channel. This is an exact weight-channel identity for fixed mark count,
not an assertion that any envelope is attained or a growing-rank asymptotic.

## Release integrity checkpoint

The bounded release replay covers 59 producer/test pairs and 56 stored JSON
companions. All 630 focused tests pass under ordinary and optimized Python.
All 59 producers also replay in both modes: 56 through their common
`--check` interface and three through the alternate CLI printed in their
notes. Packet tests recompute the canonical payload and source locks wherever
those locks are declared.

Ruff and formatting pass on 113 non-frozen Python files. The only Ruff debt
is provenance-frozen and predates this release checkpoint:

- `ffps_principal_leverage.py` and its test;
- `frobenius_interferometry_subgroup_selectors.py` and its test;
- `guarded_cohomology_conjecture_inference.py`.

A control-byte scan over all 236 changed files is clean. The working diff
passes `git diff --check`; the full range check reports only the deliberately
retained blank EOF in the provenance-frozen
`CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION.md`.

## Review checklist before a publication claim

1. Independently verify the marked-stack normalization and every imported
   elliptic trace convention.
2. Compare the exact trace rows against the full literature on local systems
   over `M_2(w^1)` and `A_2(w^1)`, not just the sources above.
3. State the result as an alternating trace identity unless individual
   cohomology groups are actually identified.
4. Keep the known Howe endpoint separate from the new orbit-density and
   moment statements.
5. For FFPS, distinguish complete inverse energy, restricted physical energy,
   soft Kummer modes, and Wick-centered global moments in every theorem
   statement.
6. Do not use “amplifier” without naming the normalization, physical support,
   owner/conductor summation, and principal-member inequality it proves.
7. For `Sym^12`, keep `Epsilon_Eis` and `Genuine` separate. The three finite
   rows cannot choose between the two without an independent vanishing or
   compact-support theorem.
8. For the multi-place packet, distinguish the standard squarefree Euler
   quotient from the evaluation-character curve adapter and the exact
   degree-five coefficient consequences.
9. For the weight-ceiling packet, distinguish a uniform Hasse/character
   upper envelope from sharpness or typical size, and retain the exact
   oriented twist and split-infinity conventions before interpreting an
   exterior-character channel.

The executable provenance and recommended reading paths are in
[RESIDUAL_MECHANISMS_RESEARCH_MAP.md](RESIDUAL_MECHANISMS_RESEARCH_MAP.md).
