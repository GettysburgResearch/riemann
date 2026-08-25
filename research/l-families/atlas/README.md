# Phase-0 L-function detector atlas

Status: **exact finite exploration, exact synthetic algebra, and source-qualified discovery data**.

Scope: one small GL(1)/GL(2) local-Euler corpus; complete monic squarefree
cubic regressions over `F_q[T]` for `q=3,5,7,11,13`, including the original
100-member `F_5[T]` pilot; the complete genus-two quintic families over
`F_3[T]`, `F_5[T]`, and `F_7[T]` (162, 2,500, and 14,406 members); exact
rational central-deflation controls; one five-object classical reciprocal-
coefficient filter through `n<=256`; and conductor-coprime quadratic-character
covariance packets for `11.a2`, both pooled and split by the sourced twist root
number. An exact `USp(4)` comparator and proof-backed all-odd-prime-power
coefficient moments, negative-sign density floor, second-moment proof roadmap,
and twelve-moment polynomial sign bound accompany the genus-two scans. Exact
affine-family measures, an all-degree affine Burnside generating series, an
all-odd-`q` elliptic-stack moment theorem, a cross-rank symplectic
reclassification, an independently enumerated balanced-control scan,
Frobenius-power echo laws, a bounded tail-geometry packet, an exact elliptic
symmetric-cube pushforward, its exact intersection with the locked genus-two
coefficient lattice, an elliptic symmetric-fourth `SO(3)` slice, a sharp
symmetric-power trace-alias theorem, a product-variety tensor family, its
singular trace-zero strata and endoscopic rank-drop bridge, a primitive
exterior-square `SO(5)` family, an integral factor-locus census, a
Sym3-exterior/Sym4 plethysm bridge, an elliptic-pair Rankin--Selberg / tensor
`SO(4)` coefficient-region packet, a positive-rank elliptic `Sym^5`
scalar-collision Diophantine pilot, an exact `SO(4)`/Sym3 spectral-intersection
classification, a rational `Sym^5` coefficient-recovery theorem, a complete
all-`m` rational full-factor collision classification, an exact odd-order
cyclotomic spectral-alias theorem, its complete even-order parity-coset
counterpart, a complete degree-six tensor/Sym5 rational spectral-intersection
theorem, a generic all-symmetric-power subtorus rigidity theorem, a complete
integral degree-eight tensor/Sym7 intersection, universal tensor-ladder moment
and Hasse-graph count theorems, and an exact `USp(4)` virtual-character null-
direction packet are also included. Every atlas record is `DRAFT`. RH and GRH
remain open.

Exact sources or dependencies: classical completed GL(1) normalizations; the
displayed finite-field definitions; the standard level-one modular-stack
trace identity used by the genus-one all-weight theorem; LMFDB object
identifiers and dynamic
metadata for three elliptic-curve discovery rows; Rohrlich's and Conrey's
quadratic-twist sign formulas; the function-field even-character coefficient
identity cited in the genus-two proof; CPython 3.12.10 standard library; and the
exact repository packets named inside detector contracts. Ramakrishnan's
classical `GL(2) x GL(2)` automorphic tensor product, Lutz--Nagell, and
Waterhouse's finite-field isogeny-classification theorem are cited only as
boundaries for the two newest local packets.

What was actually run: five finite local-Euler evaluations through `p<=43`;
4,023 candidate cubics across `q=3,5,7,11,13`; all three complete genus-two
families above; exact `F_q/F_{q^2}` character reconstruction for the three
genus-two packets, including an independent 20,175-candidate balanced-control
replay with raw-sum provenance; twelve exact `USp(4)` Haar
moments and degree-six and degree-twelve sign majorants by bounded
Laurent-polynomial arithmetic; a deterministic
1,376,256-cell sign-probability quadrature; 656,024 exact genus-two
member-affine-action checks; five synthetic GL(2)
controls under two kernel conventions; one three-curve rank correction; and
pooled plus root-number-split character covariance summaries formed from at
most 1,142 discriminants and 13 primes. The all-q genus-two certificate uses
2,925 operations in `Q[q]`, while the separate second-moment roadmap enumerates
only 20+54 symbolic signatures; neither enumerates additional fields. The
new high-weight packet adds 23 cubic signatures, while the affine Burnside
packet evaluates a rational all-degree generating series and closed divisor
sums through genus eight without enumerating another field. The power-echo
packet applies exact Newton recurrences through `r=8` to the locked
`q=3,5,7` histograms and independently checks the `C_2` Haar frequencies; it
does not enumerate another family. The reciprocal filter evaluates five
objects, four endpoints, and every coefficient through 256. The elliptic-pair
packet transforms 645 locked histogram-atom pairs and accounts for 2,661 work
units under an exclusive cap of 4,000. The `Sym^5` pilot sieves 15,931
unordered Hasse trace pairs through `q<=2000`, accounts for 16,966 work
units under an exclusive cap of 500,000, and uses only six elliptic-curve group
additions after the bounded sieve. Neither packet enumerates a finite field, a
curve, or a model. The five previously integrated frontier packets add 43
focused tests, and all 386 tests passed both normally and under optimized
Python at that checkpoint. The two additional packets supply 24 focused tests
(14 plus 10); all 410 intended repository tests pass both normally and under
optimized Python at this integration checkpoint. The offline validator checks
64 artifact bindings across 15 evaluations. The two theorem follow-ups add
22 focused tests and only 3,334 plus 226 accounted work units; all 432
intended tests pass both normally and under optimized Python at that
checkpoint. The rational full-factor and odd-cyclotomic packets add 12 and 10
focused tests, respectively, with ledgers of `4,624/5,000` and
`58,326/100,000`; all 238 intended tests pass in each mode, or 476 executions
across the two modes, at the next checkpoint. Neither packet enumerates a
field, curve, or model. No broad zero, conductor, curve, field, or factor
search was run.

Smallest remaining gaps: derive one true source-faithful function-field analogue
of `XD` or `HCNC`; evaluate the single virtual weight-six channel `R_6` left by
the balanced control's exact third-moment reduction; prove or refute the
quarantined all-`q` second-power echo candidate; classify which near-edge Weil
classes are realized by marked genus-two Jacobians; replace independent
elliptic pairs by geometrically linked pairs and test which deformations of
the product law detect a correspondence; perform an exact descent /
`S`-integral analysis on the `Sym^5` collision curve while keeping
prime-power conditions separate; and prove a root-number-conditioned weighted
off-diagonal estimate uniform in a growing prime window.

## What this release contains

The atlas uses three record types:

- `LFunctionSpec` separates analytic continuation, functional equation, central
  order, Euler factors, zero coverage, and data-source rigor.
- `DetectorContract` fixes the mathematical definition, kernel convention,
  central-zero policy, typed inputs/parameters, family adapters, and failures.
- `EvaluationRecord` binds exact spec/detector contents, configuration, input
  artifacts, implementation, raw result, coverage, and interpretation.

Atlas records use deterministic `ATLAS.*.H<32 hex>` identities. They do not use
the programme/claim namespaces `LFAM2.*`, `LFAM3.*`, or `LFAM6.*`. Issues
[#737](https://github.com/gfreund123/riemann/issues/737),
[#738](https://github.com/gfreund123/riemann/issues/738), and
[#741](https://github.com/gfreund123/riemann/issues/741) are coordination
references, never misrecorded as source PRs.

The stable canonical contract at `canonical/provenance.schema.json` is unchanged.
An atlas record may become `RELEASED` only after it points to a separate full
canonical provenance sidecar with an exact object ID and content hash. These
first-pass records remain honestly unreviewed `DRAFT` objects. The sidecar hash
is defined over canonical UTF-8 NFC JSON, and the validator checks the canonical
schema, ID, digest, and backlink rather than accepting a path by presence alone.

## Compact result map

| Pilot | Arithmetic | Finite result | Boundary |
|---|---|---|---|
| normalized local Euler moments | exact integer point counts and rational even moments | GL(1) rows have `M2=M4=1`; three GL(2) rows already refute unit-magnitude prime coefficients | tiny prime window; curve metadata is discovery-only |
| classical reciprocal filter | exact integer coefficients and `Q(sqrt(2))` signs | the four-shell filter has mixed signs across objects/endpoints; no common finite sign survives | classical coefficients; unitary map explicit; four endpoints are not an abscissa or zero theorem |
| function field, genus 1 | exact cubic arithmetic at `q=3,5,7,11,13`; all-odd-`q` elliptic-stack trace formula and Burnside laws | every marked-model character and raw trace moment is explicit; full affine branch and elliptic coarse quotients are distinct; the first automorphic correction is at raw moment 10; the original `q=5` toy sign split is `40/20/40` | all-weight theorem uses the stated standard modular-trace input; five fields are frozen regressions, not its proof; toy `H_D(1)H_D(2)` is not canonical `XD`/`HCNC` |
| elliptic symmetric cube | exact `Sym^3 H^1` local factor; rational nodal coefficient curve; all-odd-`q` model/stack laws through base degree 12; 55-atom locked pushforward | `Sym^3(SU(2))` is a rank-one subimage of `USp(4)`; trace fourth moment is `4` versus generic `3`; `t -> t^3-2qt` is injective on integer traces for odd `q`; the coefficient curve has three real nodes | the lift is classical; curve membership does not certify arithmetic origin—`(0,0)` is an odd-`q` false positive; project-specific calculations have no literature-priority claim |
| elliptic symmetric fourth | exact `Sym^4 H^1` degree-five factor, rational normalized coefficient curve, odd-prime-power moment laws, and 55-atom locked pushforward | the principal `SO(3)` slice in `SO(5)` has equation `d^2+yd-y^2-y^3=0`; its node has no rational arithmetic preimage; thin trace moments first differ from generic `SO(5)` at order three | the transfer is classical; a pointwise middle eigenvalue is not a common Tate subsystem; coefficient-curve membership is not arithmetic recognition |
| symmetric-power trace aliasing | exact Dickson recurrence, parity-factor proof, and locked pushforwards through `m=18` | for every odd `q`, the scalar `Sym^m` trace recovers an integral base trace for `m=1,3 mod 6` and its sign-orbit for `m=2 mod 6`; the other classes have Hasse-admissible, source-witnessed collisions | a scalar trace is not a full local factor; the `m=5` quartic is a Diophantine target, not an integral-point classification or realization theorem |
| elliptic `Sym^5` collision geometry | exact collision factorization and full-factor coefficients; a discriminant-first census of all Hasse-admissible integer pairs over odd prime powers `q<=2000`; exact elliptic-curve maps and primality certificate | the non-diagonal collision quartic `z^2=x^4+5x^3y+9x^2y^2+5xy^3+y^4` is birational to `Y^2=X^3-6X+5` and has a certified nontorsion point; the census has 61 scalar collisions at 21 bases, only 4 general pairs, and prime-field examples at `31`, `1021`, and `363804984411209881` | only 3 of 61 scalar collisions have equal degree-six factors; positive rank gives rational points, not an integral/prime-power classification; Waterhouse realizes the three prime-base trace pairs but rules out their higher odd-degree scaled towers; no compatible global family, Euler product, or external priority claim |
| elliptic `Sym^5` coefficient recovery | exact rational difference quotients, literal `5 x 5` Sylvester determinant, rational-projective factor exclusions, exterior-power weight decompositions, and replay of all 61 source collisions | `(E_5,c_2)` determines the base trace except for sign pairs with `t^2=q` or `3q`; adding `c_3`, equivalently the complete reciprocal degree-six factor, leaves exactly the `t^2=3q` sign fiber; all general positive-rank collisions split at `T^2` | a local theorem over `Q` at fixed nonzero `q`; coefficient recovery supplies no elliptic realization, automorphy, compatible system, zero theorem, or external priority claim |
| complete rational symmetric-power factors | intrinsic root-quotient-group recovery, exact central-sign stabilizer theorem, cyclotomic-order exhaustion, closed exceptional factors, and integral odd-prime-power corollary | for every `m>=1` and fixed rational `q!=0`, complete-factor equality forces `x^2=y^2`; even `m` always forgets sign, while odd `m` has only the `x^2=2q, 4|(m+1)` and `x^2=3q, 6|(m+1)` sign loci; nonzero integral odd-prime-power aliases are exactly `m=5 mod 6`, `q=3^(odd)`, `t=+/-3^((a+1)/2)` | fixed-`q` local algebra over `Q`; `Sym^0` is excluded; Hasse admissibility is not curve realization, and no compatible family, Euler product, or external priority claim follows |
| odd cyclotomic complete-spectrum aliases | exact cyclic-interval stabilizer theorem for every odd root order, three universal factor identities, scalar-lift parity audit, and minimal-polynomial certificates at orders `5,7,9,11` | primitive classes have equal `Sym^m` spectra exactly for the original inversion class or `m=-2,-1,0 mod N`; for odd `N>=5`, all `phi(N)/2` primitive trace classes collapse at those powers, proving the rational recovery hypothesis is sharp | algebraic local torus classes only; `N=3` has no genuine non-sign pair; even root orders are handled by the separate parity-coset packet, while rational elliptic realization, global families, and novelty priority remain open |
| even cyclotomic complete-spectrum aliases | exact parity-cycle decomposition, affine-interval stabilizer theorem, central-lift audit, three closed edge factors, and global totient threshold | for `N=2M`, all units stabilize exactly when `(m+1) mod M` is `0,1,M-1`; in the interior only inversion survives at odd `m`, while even `m` additionally sees the central sign; an edge gives a genuine nonsign primitive collapse exactly for `N` outside `4,6,8,12` | local algebraic torus theorem; extra generic lifts are only the even-power central kernel; common determinant lifts, arithmetic realization, global families, even/odd trace-field descent, and novelty priority remain separate |
| degree-six tensor / `Sym^5` spectral intersection | exact Newton coefficients, a custom rational Groebner certificate, cyclotomic residual ideals, all-odd-prime-power Hasse-lattice counts, compact moments, and an all-`r` torus ladder | after the necessary `qT` dilation, `Std(E_A) tensor Sym^2(E_B)` equals `Sym^5(E_C)` over rational raw data exactly on `B^2=C^2, qA=C(C^2-3q)` or `A=C, qB^2=(C^2-2q)^2`; at `q=p^(2k)` the Hasse-lattice union has `8p^floor(k/3)+8p^floor(k/2)-1` triples | local formal factors and coefficient lattices only; orders `7,12,14` are algebraic residuals, only the `r=2` converse is complete, and no three-curve realization, representation homomorphism, global transfer, novelty, or RH/GRH claim follows |
| tensor/symmetric-power subtorus rigidity | elementary multiplicity and largest-weight proof, arbitrary nonprimitive target exponent, Dickson graph equations, central-sign parity, and a light bounded replay | for every `r>=1`, `Std(w^a) tensor Sym^r(w^b)` has the `Sym^(2r+1)(w)` weight multiset exactly for `(|a|,|b|)=(r+1,1)` or `(1,2)`; an exponent `c` on the target scales both pairs by `|c|` | exhaustive only among integer monomial one-parameter subtori; torsion parameters, nonmonomial curves, isolated rational points, arithmetic realization, and general full rational intersections remain separate |
| degree-eight tensor / `Sym^7` spectral intersection | four Newton coefficients, exact small elimination and residual-support certificates, cyclotomic witnesses, p-adic divisibility, locked nonsquare and synthetic square replays, and compact moments | after `q^(3/2)T` dilation, integral odd-prime-power solutions are exactly the same-sign `C4/z` and `z/C2` graphs; nonsquare `q` is empty, while `q=p^(2k)` has `8p^floor(k/4)+8p^floor(k/2)-4` Hasse triples; trace moments first split at degree six (`170` versus `260`) | nongraph algebraic strata remain at orders `8,16,20,9/18,7/14` but cannot descend to integral raw data; the count gives no three-curve realization, correspondence, global transfer, novelty, or RH/GRH claim |
| all-`r` tensor/symmetric-power moment ladder | exact `SU(2)` weight extraction, Clebsch--Gordan recurrences, closed invariant counts through degree eight, and rank-aware generic symplectic comparison | independent `Std x Sym^r` and principal `Sym^(2r+1)` moments agree through degree four and split first at degree six by `3r(r+1)(r+2)/2`; the eighth gap is `2r(r+1)(r+2)(3r^2+6r+5)` | compact Haar representation algebra only; `USp` is polarization-matched to the product only for even `r` (odd `r` needs an orthogonal comparator), rank exceptions are retained, and no finite-family equidistribution, monodromy, novelty, or zero theorem follows |
| all-`r` universal-graph Hasse counts | homogeneous Dickson valuation lemma, central-sign duplicate audit, exact Chebyshev overlap period, square and nonsquare odd-prime-power formulas, and recovery of the `r=1,2,3` packets | at `q=p^(2k)`, the graph union is `8p^floor(k/(r+1))+8p^floor(k/2)-1+1_(r odd)-4*1_(3 does not divide r+1)`; at nonsquare odd `q`, odd `r` is empty and even `r` has one explicit first-graph count | counts only the two universal graph loci; nonsquare `p=2` is excluded, and no claim is made that every full intersection lacks additional isolated points or that any triple is realized by linked curves |
| elliptic-pair Rankin--Selberg / tensor `SO(4)` | exact degree-four tensor polynomial, semialgebraic compact coefficient image, all-odd-prime-power low moments, and frozen independent-product pushforwards | normalized coefficients satisfy `x=uv`, `y=u^2+v^2-2`; the reconstruction fold is `D=(p-r)^2`, whereas the full root discriminant is `D(p-4)^2(r-4)^2`; `SO(4)` and `Sym^3(SU(2))` trace moments alias through order 4 and split at order 6 (`25` versus `34`) | the finite law is the ordered product of independent marked-model / elliptic-stack marginals, not a linked-curve or coarse-pair measure; a fold is not the full repeated-root locus; local equal/opposite traces imply no twist, isogeny, correspondence, automorphy, or global L-function identity |
| `SO(4)` / elliptic Sym3 spectral intersection | exact pullback factorization into four signed angle-doubling graphs, nonsquare valuation obstruction, square-`q` lattice parameterization, Waterhouse filter, and restricted discriminants | nonsquare odd prime powers have no integral intersection; for `q=p^(2k)` the Hasse lattice has `16p^floor(k/2)-4` points, but simultaneously realized elliptic pairs collapse to endpoint, unit, and zero-endpoint repeated-root strata | the tensor/Sym3 equality requires the stated weight dilation; angle doubling is not a representation homomorphism; Waterhouse gives separate local isogeny classes, not a curve correspondence or global family |
| Sym3/genus-two coefficient intersection | exact scaled curve, rational inverse off the nodal divisor, odd-prime candidate lemma, and complete transform of 251 locked atoms | exactly 7 atoms/451 members hit the curve; only 4 shapes/53 members are independently elliptic-trace witnessed, while 3 atoms/398 members are central ghosts | the factors have different weights; equal normalized coefficient shapes do not identify motives, families, or local factors |
| function field, genus 2 | exhaustive exact `F_q/F_{q^2}` arithmetic at `q=3,5,7`; exact all-q proof certificate; exhaustive affine action | normalized means are `-104/243`, `-1994/3125`, `-12340/16807`; all-q mean tends to `-1`, `liminf rho_->=1/20`, five low-weight character means are exact, and the second-moment gap reduces to `chi_(0,4)+chi_(2,2)+2chi_(0,3)` | orbit averages require stabilizer weights; the remaining high-weight decay and full sign law are conjectural; toy coefficient minor |
| product-variety tensor family | exact primitive degree-eight, weight-two `H^1(E)⊗H^1(C)` factor; all-`q` finite means from locked marginals; exact frozen `q=3,5,7` histogram convolution | compact image `(USp(2)×USp(4))/diag center` lies in `SO(8)`; `u^2h-u^4+2u^2v+u^2-2uw-w^2=0`; product-Haar trace `m4=6` versus generic `SO(8)` value `3`, and `(mean(h),mean(uw))=(1,1)` versus `(0,0)` | `A=-t_E` bridges the stored trace convention; frozen laws use ordered factor-pair model/curve-stack measure, not uniform coarse product varieties; no generic-`SO(8)` or convergence claim |
| tensor trace-zero singular strata | exact sparse-polynomial geometry plus a 2,471-atom-pair locked census | the ambient containing hypersurface has `F=(h+2v+2)u^2-u^4-(u+w)^2`; reduced singular plane `u=w=0`; rank drop on `h+2v+2=0`; reduced pullback branches `A=0,b=2q` and `a=0,b=2q-A^2` | equality with the full coefficient image is not asserted; a singular containing hypersurface is not a singular curve/variety; formal `P_C` factorizations import no isogeny or endomorphism theorem |
| tensor endoscopic rank-drop bridge | exact sum-of-squares identity, primary decomposition, and complete split/rank incidence census over the locked product atoms | `q^2(h+2v+2)=(A^2+b-2q)^2+(Aa)^2`; real/integer rank drop lies on two integral `+q` split branches, but most split atoms do not rank-drop | the doubled scheme pullback is not an asserted endoscopic moduli scheme; coefficient factorization imports no isogeny, polarization, or geometric splitting theorem |
| genus-two integral `+q` factor locus | exact discriminant/parity transform of all 251 frozen signed coefficient atoms | split fractions `1/6,141/500,85/343`; `B`, `F`, and the complete balanced echo each have cross-boundary collisions; cyclotomic spectra occur on both sides | complement may still factor over `Z`; no Honda--Tate, polarization, all-`q` density, or geometric-simplicity claim; q=7 split-orbit total remains exactly nonidentifiable in `86..88` |
| primitive genus-two exterior square | exact degree-five `SO(5)` factor, exact all-`q` character Gram formulas, and frozen trace pushforwards | after the canonical polarization line is removed, every local factor has a second `(1-qT)` divisor and hence a genuine fiberwise Frobenius-stable line; `SO(5)` trace moments through six are `1,0,1,0,3,1,15`; frozen fifth moments have the opposite sign | ambient `SO(5)` forces no second common line, but actual family monodromy is unproved and endoscopic loci can gain one; cross-family/cross-prime quartic compatibility is not established; three negative fifth moments imply no asymptotic law |
| Sym3 exterior/Sym4 plethysm bridge | exact characteristic-zero weight decomposition, six-coefficient local-factor identity, normalized curve map, and a 251-atom locked incidence transform | `wedge^2 Sym^3 V=(det V)^3 + (Sym^4 V tensor det V)` and the primitive factor is exactly `P_Sym4(qT)`; the Sym3 curve pulls back identically to the Sym4 curve | this is classical representation algebra plus a project-specific coefficient diagram; it does not identify the genus-two factors, motives, monodromy, or Euler products |
| exact `USp(4)` comparator | bounded Laurent-polynomial/Weyl arithmetic plus guarded shifted-grid quadrature | `F=(Tr U)^2-e_2(U)^2=-(1+chi_omega2+chi_2omega2)`, range `[-20,4/3]`, exact Haar moments through order 12; a degree-twelve majorant proves `P(F<0)>=0.480701...`; display-only `P(F<0)≈0.738` | the rational value is a lower bound, not the exact probability or a claimed optimal moment bound; finite-field higher-moment/sign-law convergence remains proposed |
| affine hyperelliptic presentation measures | exact Burnside fixed-locus divisor sums and a rational all-degree generating series, no field enumeration | marked affine-stack mass is `q^(2g-1)` in every genus; the universal leading coarse-orbit correction is `(q^g-(-1)^g)/(q+1)`; multiplicative resonances occur in degrees `0,1 mod d` for `d|q-1`, additive resonances in degrees divisible by `char(F_q)` | marked odd-degree equations, not the full unpointed hyperelliptic moduli stack; even degrees are covered by the series but define a different presentation problem |
| cross-rank coefficient minors | exact `USp(2g)` character algebra and bounded Weyl constant terms | the original alternating sign is all-rank Schur negativity; `B=2e_1^2-e_2^2` has symmetric arcsine-times-semicircle Haar law but exact finite mean `q^-1+q^-3-q^-4+q^-5` | no finite-family convergence; odd `B` moments remain arithmetic targets |
| virtual-character null directions | exact coefficient-square lattice, bounded integer panels, and independently reconstructed full `C_2` Weyl density | modulo `e_1e_3=e_1^2`, the only primitive coefficient-square direction is `B`; bounded panels isolate it among noncentral directions, while globally it generates `B Z[u^2+v^2,u^2v^2]` alongside the center-odd sector | bounded isolation is not global uniqueness, and the hardened full-density replay is a compact-group certificate only; no arithmetic-family claim |
| balanced genus-two control | independent exhaustive `q=3,5,7` coefficient scan with a source-locked member ledger | six exact frozen moments, signs, supports, affine orbits, and raw sums; the all-`q` mean is proved; `B^3=6B-2chi_(0,3)+R_6` reduces the first unresolved odd moment to one explicit virtual weight-six average | only the mean is all-`q`; raw sums and `mean(R_6)` are frozen three-field facts, not interpolated formulas |
| Frobenius-power echoes | exact Newton/Cayley--Hamilton transforms of the locked `q=3,5,7` histograms and independent `C_2` constant terms | the entire sequence is determined by `(B_1,B_2)`; distinct Haar frequencies are orthogonal, while mixed cubic moments resonate exactly when `r+s=t`; periodic frozen strata are recurrence-certified | orthogonality is not independence; the displayed all-`q` formula for `mean(B_2)` is a quarantined three-field conjecture; no endomorphism classification follows |
| genus-two tail geometry | exact reciprocal-quartic identities plus frozen support/orbit reconstruction | minima at `q=3,5,7` are split nonisotypic, repeated isotypic, and simple; repeated angles do not explain the dominant `q=7` tail | three fields only; coefficient admissibility is not Jacobian realization |
| high-weight channel probe | exact `C_2` triangularization and 23 bounded cubic signatures | isolates `b^3`, `a^2b^2`, `b^4`; records a sparse candidate implying `q^2 mean(H)->2` | candidate matches only three fields; primitive trace averages are unresolved |
| conductor-coprime twist precursor | exact pooled and sourced root-number-split character Gram/covariance matrices, marginal contrasts, and multiquadratic moments | through `X=2048`, local densities approach explicit comparators; root-sign Gram and character-mean contrast RMS shrink on the four frozen windows but their scaled/weighted corrections do not give a rate | no central ranks, fitted rate, growing-prime theorem, or twist-family limit |
| GL(2) deflation | exact `Fraction` matrices | central atom is rank one; Loewner sign is negative, Pick-sum sign positive; full deflation need not restore positivity | synthetic controls, no arithmetic L-values |
| rank stress | exact algebra on imported discrete metadata | rank 0 and minimal rank 1 give zero parity/full gap; rank 2 gives `25/4` at nodes `(1,2)` | three selected curves, not a twist family |

The detailed scientific synthesis and theorem nominations are in
[`FINDINGS.md`](FINDINGS.md) and [`THEOREM_TARGETS.md`](THEOREM_TARGETS.md).

## Layout

```text
schema/          three atlas schemas plus shared controlled vocabulary
specs/           ten content-addressed L-function/family specifications
detectors/       eleven typed detector contracts and seven raw-result schemas
evaluations/     fifteen content-bound evaluation wrappers
results/         compact derived raw outputs
sources/         compact source-identifier manifest, not a database mirror
core/            generators, exact local arithmetic, and offline validator
function_field/  exact finite-field implementation, fixture, and report
gl2/             exact deflation algebra, controls, verifier, and report
```

## Lightweight replay

From the repository root:

```powershell
python research/l-families/atlas/core/run_pilot.py
python research/l-families/atlas/function_field/pilot.py --check research/l-families/atlas/function_field/fixtures.json
python research/l-families/atlas/function_field/genus2_pilot.py --check research/l-families/atlas/function_field/genus2_f3_quintics.json
python research/l-families/atlas/function_field/genus2_q_scan.py --check research/l-families/atlas/function_field/genus2_q_scan.json
python research/l-families/atlas/function_field/genus2_moment_identity.py
python research/l-families/atlas/function_field/genus2_affine_orbits.py --check research/l-families/atlas/function_field/genus2_affine_orbits.json
python research/l-families/atlas/function_field/genus2_second_moment_reduction.py --check research/l-families/atlas/function_field/genus2_second_moment_reduction.json
python research/l-families/atlas/function_field/genus2_family_measures.py --check research/l-families/atlas/function_field/genus2_family_measures.json
python research/l-families/atlas/function_field/hyperelliptic_affine_burnside.py --check research/l-families/atlas/function_field/hyperelliptic_affine_burnside.json
python research/l-families/atlas/function_field/genus1_cubic_family_laws.py --check research/l-families/atlas/function_field/genus1_cubic_family_laws.json
python research/l-families/atlas/function_field/elliptic_symmetric_cube_family.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_fourth_so5_slice.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_power_trace_aliasing.py --check
python -B research/l-families/atlas/function_field/elliptic_sym5_collision_diophantine_pilot.py --check
python -B research/l-families/atlas/function_field/elliptic_pair_rankin_so4_family.py --check
python -B research/l-families/atlas/function_field/elliptic_so4_sym3_spectral_intersection.py --check
python -B research/l-families/atlas/function_field/elliptic_sym5_coefficient_recovery.py --check
python -B research/l-families/atlas/function_field/elliptic_symmetric_power_full_factor_sign_aliases.py --check
python -B research/l-families/atlas/function_field/elliptic_symmetric_power_cyclotomic_spectral_aliases.py --check
python -B research/l-families/atlas/function_field/elliptic_symmetric_power_even_cyclotomic_aliases.py --check
python -B research/l-families/atlas/function_field/elliptic_tensor_sym2_sym5_spectral_intersection.py --check
python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_subtorus_rigidity.py --check
python -B research/l-families/atlas/function_field/elliptic_tensor_sym3_sym7_spectral_intersection.py --check
python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check
python research/l-families/atlas/function_field/genus2_sym3_coefficient_intersection.py --check
python research/l-families/atlas/function_field/sym3_exterior_sym4_plethysm_bridge.py --check
python research/l-families/atlas/function_field/balanced_control_family_scan.py --check research/l-families/atlas/function_field/balanced_control_family_scan.json
python research/l-families/atlas/function_field/frobenius_power_echoes.py --check
python research/l-families/atlas/function_field/genus2_high_weight_channel_probe.py --check research/l-families/atlas/function_field/genus2_high_weight_channel_probe.json
python research/l-families/atlas/function_field/genus2_tail_geometry.py --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python research/l-families/atlas/function_field/product_variety_tensor_family.py --check research/l-families/atlas/function_field/product_variety_tensor_family.json
python research/l-families/atlas/function_field/tensor_trace_zero_singular_strata.py --check research/l-families/atlas/function_field/tensor_trace_zero_singular_strata.json
python research/l-families/atlas/function_field/tensor_endoscopic_rank_drop_bridge.py --check
python research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py --check
python research/l-families/atlas/function_field/genus2_primitive_exterior_square.py --check research/l-families/atlas/function_field/genus2_primitive_exterior_square.json
python research/l-families/atlas/function_field/virtual_character_null_directions.py --check
python research/l-families/atlas/function_field/usp4_toy_minor_moments.py --check research/l-families/atlas/function_field/usp4_toy_minor_moments.json
python research/l-families/atlas/function_field/usp4_toy_minor_character_decomposition.py --check
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
python research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.py --check research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.json
python research/l-families/atlas/function_field/usp4_sign_probability.py --check research/l-families/atlas/function_field/usp4_sign_probability.json
python research/l-families/atlas/gl2/verify.py --check research/l-families/atlas/gl2/results.json
python research/l-families/atlas/core/wrap_specialist_pilots.py
python research/l-families/atlas/core/wrap_genus2_pilot.py --check
python research/l-families/atlas/core/reciprocal_wavelet.py --check
python research/l-families/atlas/core/twist_character_covariance.py --check
python research/l-families/atlas/core/twist_root_number_covariance.py --check
python research/l-families/atlas/core/wrap_genus2_q_scan.py --check
python research/l-families/atlas/core/wrap_usp4_toy_minor_moments.py --check
python research/l-families/atlas/core/validate_atlas.py
python -m unittest discover -s tests -p "test_*.py"
```

The guarded producers refuse work at their declared caps and record complete
high-level work ledgers in their JSON artifacts. For an optimized replay,
insert `-O` after `python -B`. The two newest focused modules are
`tests.test_elliptic_tensor_symmetric_power_moment_ladder` and
`tests.test_elliptic_tensor_symmetric_power_hasse_graph_counts`; neither
replay constructs curves, finite fields, or polynomial models.

The offline validator uses only the standard library. It rejects duplicate JSON
keys, non-finite numbers, Unicode-normalization drift, unknown fields, stale
identity/configuration/content hashes, unsafe paths, parameter drift, unbound
released records, missing or malformed provenance sidecars, implementation-byte
drift, typed-input/output mismatches, incomplete artifacts, and several
rigor/scope confusions.

## Scientific firewalls

- Finite rows do not imply a prime limit, family law, RH, or GRH.
- Classical reciprocal coefficients for motivic weight one differ from unitary
  coefficients by `sqrt(n)`; their raw magnitudes are not cross-family moments.
- Known function-field root radius does not itself prove a project-specific
  signed detector estimate.
- A family mean is not a memberwise conclusion.
- Positive/negative discriminant strata are not root-number strata; the
  separate root-number packet uses the sourced rule
  `epsilon_d=sign(d)*(d/11)` for conductor-coprime twists of `11.a2`.
- A finite decrease in raw covariance RMS is not a uniform weighted moment bound.
- Three exact fields are not evidence for higher-moment equidistribution. The
  all-q first-moment identity is instead bound to a separate proof and exact
  polynomial certificate.
- The genus-one all-weight formulas use the explicitly stated standard
  modular-stack trace identity; the five frozen prime fields check the formulas
  but do not prove them. Signed trace descends to the elliptic quotient, not to
  the full affine branch quotient.
- The balanced scan independently locks its `q=3,5,7` raw sums and exact
  `R_6` reduction, but supplies no all-`q` formula for `mean(R_6)`.
- Frobenius-power echoes collapse pointwise to `(B_1,B_2)`. Their exact Haar
  frequency orthogonality is not independence, and the proposed all-`q`
  `mean(B_2)` formula remains explicitly conjectural.
- The product-variety packet uses `A=-t_E` to bridge the locked genus-one trace
  convention. Its all-`q` finite mean corrections come from locked marginal
  theorems, while its `q=3,5,7` laws are frozen histogram convolutions under
  ordered factor-pair model/curve-stack measure, not uniform coarse measure.
- The tensor singular-strata packet studies the containing coefficient
  hypersurface. Its pinch point, singular plane, rank-drop line, and branch
  factorizations do not make a source curve or product variety singular and do
  not import an isogeny or endomorphism theorem.
- The integral-factor packet classifies only integral factors with constant
  term `+q`; its complement can still factor over `Z`. Cross-boundary detector
  collisions, cyclotomic certificates, and the `q=7` orbit interval carry no
  all-`q`, polarization, or geometric-simplicity conclusion.
- The symmetric-cube packet studies a genuine functorial representation but
  does not reprove its classical automorphy. Its curve is a compact-image
  obstruction, not a local or global arithmetic recognition theorem; the
  `(0,0)` node is an explicit odd-`q` false positive.
- The symmetric-fourth packet studies the classical transfer's principal
  `SO(3)` coefficient slice, not a generic `SO(5)` family. Its nodal curve,
  moment comparison, and finite pushforward do not supply an arithmetic
  recognition theorem or a common Tate subsystem.
- The symmetric-power alias theorem classifies only one scalar trace. Its
  complementary collisions do not normally identify complete local factors,
  and its `m=5` collision curve is left as a guarded Diophantine target.
- The `Sym^5` pilot advances that target only to an exact positive-rank
  rational collision curve and a bounded Hasse-lattice census. Only three
  scalar collisions in the census have equal full degree-six factors.
  Waterhouse realizes the displayed primitive prime-base trace pairs as local
  elliptic isogeny classes, but excludes their nonzero higher odd-degree scaled
  traces; neither rational points nor weighted scaling supplies infinitely many
  primitive prime bases, a compatible family, or an Euler product.
- The elliptic-pair tensor packet uses independent ordered marginals. Its
  `SO(4)` coefficient region, exact finite corrections, and compact Haar
  moment comparison do not prove finite-family equidistribution, actual
  monodromy, or the existence of geometrically linked curves. The reconstruction
  fold `D=(p-r)^2` is not the full quartic root discriminant, and a
  one-prime coincidence `A=+/-B` gives no twist, isogeny, or global
  correspondence.
- The `SO(4)`/Sym3 intersection packet identifies four maximal-torus spectral
  graphs. Squaring a torus parameter is not a group-representation map, and
  its raw local factors match only after the stated square-`q` dilation.
  Waterhouse realization is pointwise and local; the remaining integral
  Hasse graph points are arithmetic ghosts, not evidence of a correspondence.
- The Sym5 recovery packet is an exact local algebra theorem. The plethystic
  descriptions of `c_2` and `c_3` do not create a new lift, while equality of
  a finite-place factor does not create a compatible family or Euler product.
- The complete symmetric-power factor theorem is local and fixed-`q`. Its
  rational conclusion `x=+/-y` excludes `Sym^0` and does not turn a
  Hasse-admissible exceptional sign trace into an elliptic curve, compatible
  system, or global identity. Even powers forget the central sign for formal
  representation-theoretic reasons.
- The cyclotomic packet concerns algebraic torus classes of odd order. Its
  universal equal factors use a common scalar lift; changing that lift at an
  odd symmetric power replaces `F(T)` by `F(-T)`. The order-three case is
  vacuous modulo inversion, and no even-order, finite-field realization,
  automorphy, zero-distribution, or literature-priority conclusion is made.
- The even-cyclotomic packet works on one parity coset of a primitive
  `N=2M` torus. Its two extra generic lifts when `4|N` are precisely the
  central sign at even symmetric power, not a new source of nonsign aliases.
  The all-unit edge collapse is local algebra: it neither realizes an
  elliptic Frobenius class nor supplies cross-prime compatibility or a global
  Euler product.
- The degree-six tensor/Sym5 packet compares factors of different weights only
  after the displayed `qT` dilation. Its two Chebyshev graph families exhaust
  rational formal trace data, but the Hasse-lattice count is not an elliptic
  realization theorem. The all-`r` ladder supplies sufficient spectral loci;
  within that packet only `r=2` has a complete converse, and no representation
  homomorphism, compatible system, automorphic transfer, or global Euler
  product follows.
- The subtorus-rigidity theorem upgrades those two all-`r` loci only for
  integer monomial cocharacters. At roots of unity the weights are reduced
  modulo the torsion order, while nonmonomial curves and isolated points are
  not controlled. It is not a general rational-intersection theorem.
- The degree-eight tensor/Sym7 packet supplies a complete integral raw theorem
  over odd prime powers after a chosen `q^(3/2)` dilation. Its cyclotomic
  residual strata are genuine algebraic points even though none descends to
  the raw lattice. The closed Hasse count does not realize three linked curves
  or create a correspondence, compatible system, or automorphic transfer.
- The all-`r` moment packet is compact representation-ring algebra. Its Haar
  separations do not prove finite arithmetic equidistribution or monodromy;
  generic symplectic comparison uses the displayed rank corrections.
- The all-`r` Hasse packet counts only the two universal graph loci. It neither
  excludes every possible isolated full-intersection point for `r>=4` nor
  realizes a counted trace triple by linked curves. Its nonsquare theorem is
  deliberately restricted to odd `p`, since `p=2` has exceptional zeros.
- The Sym3/genus-two intersection is between normalized coefficient shapes of
  different weights. Source-witnessing an elliptic trace does not make a
  genus-two member a symmetric-cube motive, and the central hits remain
  arithmetic ghosts.
- The Sym3-exterior/Sym4 bridge is classical plethysm plus an exact
  coefficient diagram. Equality of its formal transformed factors does not
  identify source motives, families, monodromy groups, or Euler products.
- The primitive exterior-square packet removes the canonical polarization
  line. Each finite-field fiber has a genuine second Frobenius-stable
  `q`-eigenline, while ambient `SO(5)` supplies no forced common line. The
  actual family monodromy is unproved, endoscopic loci can gain a second Tate
  line, and the varying quartics are not asserted to form a compatible motive.
- The virtual-character panels isolate `B` only inside their declared bounded
  boxes. The infinite module `B Z[u^2+v^2,u^2v^2]`, the separate center-odd
  sector, and the full-density replay are exact compact-group statements, not
  arithmetic-family laws.
- The proved negative-member proportion is a one-sided density floor, not a
  limiting sign law or a canonical detector conclusion.
- The degree-six and degree-twelve `USp(4)` certificates give rigorous Haar
  lower bounds, not the exact sign probability; their finite-family liminf
  consequences assume convergence of the first six or twelve moments.
- A forced central zero is legitimate critical-line geometry, not an off-line
  witness.
- Parity deflation and full-rank deflation use different information.
- `Loewner difference` and `Pick sum/Hankel` have opposite central-atom signs.
- Dynamic LMFDB rank/root metadata remains `DISCOVERY_ONLY` here.
