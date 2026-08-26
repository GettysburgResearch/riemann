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
branch's derivations replay for every odd prime power, rather than fitting a
few fields, but the surrounding finite-field/cohomological machinery is
established and a specialist literature search is still required.

## Graded result map

The proof grade is an internal audit grade, not peer review. RH criticality
distinguishes current direct relevance from possible upside.

| object | proof grade | defensible novelty statement | RH criticality |
|---|---:|---|---:|
| marked `Sym^6` law | A- | direct all-field formula not printed in the audited sources; likely close to consequences of established pointed-count machinery | C |
| marked `Sym^8` and `Sym^10` laws | A- | strongest candidate contribution: exact for all odd prime powers and not printed in the audited bounded/conjectural tables | C+ / B- as family mechanism |
| ambient `Sym^2,...,Sym^10` ladder | A- | exact boundary corollary and useful packaging; individual cohomology groups are not identified | C+ |
| inverse cusp-channel filters | A | exact lattice and recurrence corollaries of the trace ladder | C+ |
| `Sym^10` finite rare-event tomography | A as an exact finite theorem | finite anatomy, not an all-`q` distribution or endoscopy theorem | D+ / C methodologically |
| scalar endpoint realization | A- | endpoint and seed are known; affine/twist orbit densities and the exact moment contribution are candidate additions | D+ |
| all-rank scalar-endpoint phase diagram | A | exact consequence of the constructed endpoint atoms; useful new packaging, not an endpoint classification or full-moment asymptotic | D direct / B- methodologically |
| high-rank Haar tail and boundary layer | A | exact and clean, including the mesoscopic and rank-scale crossover constants; external novelty uncertain and possibly folklore in harmonic-analysis pieces | D direct / B- methodologically |
| `USp(4)` virtual-character null module | A- | exact bounded representation-ring result; likely elementary but useful as a detector firewall | D direct / C methodologically |
| correlated and cyclic FFPS masks | A as formal tensor theorems | exact project-specific restricted-Gram optimizers; no global amplifier theorem | B now / A upside |
| checkerboard and cyclic source bridge | A- on one fixed fibre | corrects a real physical-invariance issue, extends it to exact order `k`, and proves a universal Wick-residual obstruction; the analytic lift remains open | B- |

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

## Primary-literature boundary

The following sources establish much of the surrounding language and
machinery.

- Bergstrom--Faber--van der Geer develop the marked level-two point-count
  framework in [Sections 1--3](https://arxiv.org/html/0803.0917#S1). Their
  exact computational data cover bounded odd fields in
  [Section 5](https://arxiv.org/html/0803.0917#S5). Their Eisenstein theorem
  is regular-weight, the nonregular continuation is presented as an
  expectation in
  [Theorem 4.2](https://arxiv.org/html/0803.0917#S4.Thmtheorem2), and later
  genuine/endoscopic extraction is conjectural in
  [Section 10](https://arxiv.org/html/0803.0917#S10).
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

The defensible release wording is therefore: **the formulas are not printed
in the audited sources and the branch supplies exact all-odd-`q`
derivations beyond their bounded or conjectural presentation**. That is not a
certification that no equivalent theorem exists elsewhere.

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

The executable provenance and recommended reading paths are in
[RESIDUAL_MECHANISMS_RESEARCH_MAP.md](RESIDUAL_MECHANISMS_RESEARCH_MAP.md).
