# Independent frozen review: Hecke-selected source concentration

Verdict: mathematical and exact finite-replay PASS at
eaa8e8263bb34b8b669f911580c9dd9e55766ba2.
A missing explicit arithmetic/rounding declaration is a release-contract
cleanup, not a mathematical gap. Any metadata successor needs its own identity
and a comparison review; this report does not pre-accept a future successor.

Review date: 2026-08-31. Reviewer: audit_764_wave2, a non-author.
Scientific parent: 070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22.
No author contact, scientific-file edit, amendment, push, or main-branch change
was used. The scientific diff contains exactly the five advertised additions.
This review and its independent script/fixture are separate additions.

## 1. Accepted theorem and sharp scope

For level-one even-weight cusp forms, with the original Petersson metric,
a unit vector supported on r simultaneous Hecke eigenlines and carrying fixed
positive cusp mass above y=eta*k requires r at least a fixed positive multiple
of k/log(k). Here eta is fixed before the weight tends to infinity.

For any Hecke-selected subspace of rank o(k/log(k)^5), the normalized completed
Eisenstein period converges in operator norm to -Id/(2c) at s=1-c/k, uniformly
on each fixed compact subset of Re(c)>0. Every internal restriction is therefore
nondegenerate there for sufficiently large weights. This second rank scale
must NOT be replaced by the stronger support threshold k/log(k).

The actual fixed-depth determinant-nullvectors from DL converge, up to phase,
to the corresponding normalized coefficient kernel. Consequently their exact
Hecke supports have size at least a fixed-depth multiple of k/log(k), and their
orthogonal projections into any selected rank o(k/log(k)) subspace tend to zero.

These assertions are eventual all-even-weight statements with fixed depth and
fixed compact sets. There is no effective onset, growing-depth theorem, full-space
Hecke diagonalization, codimension-fixed-flag conclusion, critical-line result,
global divisor census, or RH consequence. The zero-free statement concerns
small selected spaces and their INTERNAL restrictions, not arbitrary quotients
of the whole cusp space.

## 2. Independent mathematical checks

The complete HC proof and its five files were read. Load-bearing DL, LS and CF
source statements were checked at their literal pinned identities; the accepted
DL review was read as provenance, not used instead of reconstructing HC17--22.

### Classical imports and normalizations

The primary PDFs were read in text and their relevant printed pages rendered
and inspected: Holowinsky--Soundararajan p1523, Goldfeld--Hoffstein--Lieman p178,
and Iwaniec--Luo--Sarnak pp68,71,74.

* [Holowinsky--Soundararajan](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p18-p.pdf),
  section2 equations (2.1)--(2.2), explicitly states the completion and the
  uniform holomorphic weight-aspect bound L(1,sym^2 f) >> 1/log(k).
  It also states the relevant zero-free region.
* [Goldfeld--Hoffstein--Lieman](https://www.math.columbia.edu/~goldfeld/EffectiveZeroFreeRegion.pdf),
  p178 explicitly gives uniformity in holomorphic weight and excludes GL(1)
  lifts at level one. This is an imported theorem, not certified by the fixture.
* [Iwaniec--Luo--Sarnak](https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf),
  equations (2.14)--(2.20) supply the orthogonal eigenlines, first-coefficient
  normalization and divisor bound; Proposition2.1 and Lemma2.5 agree with
  the coefficient-kernel and Petersson constants after their opposite
  inner-product convention is accounted for.

Independent unfolding gives
G(f)=2 A_k(1)L_f=(k-1)A_1 L_f/(2*pi^2).
In ILS notation Z(1,f)=L_f/zeta(2); omitting this factor would be wrong.
Pairing the two adjacent Gamma_R factors twice yields the exact completion
ratio 2^(-k-1), as claimed in HC2.

For two distinct first-coefficient-one eigenforms the cross Dirichlet series
has first coefficient one. Thus it is not identically zero, although the
cross residue at s=1 vanishes by Petersson orthogonality. No simultaneous
period diagonalization follows from being a Hecke eigenbasis.

### Complete tails, moment and complex operator estimate

HC3 is valid on the complete width-one cusp rectangle, with eta*k>=1.
Writing the incomplete Gamma tail as P(Z>=a*n), Tonelli and
sum_(n<=u)n<=u^2 give
sum lambda(n)^2 Q(k-1,a*n)<=4(k-1)k/a^2.
Multiplication by the exact Petersson normalization gives precisely
1/(2*eta^2*k*L_f). The small-u case contributes zero, so no missing tail occurs.
Positive compression is bounded by its trace, including arbitrary off-diagonal
entries. This proves HC5--6 without assuming multiplication preserves cusp forms.

A separate Parseval calculation gives HC7 with coefficient pi/(2L_f), not the
HC3 coefficient. The prime-power identity
binom(a+3,3)-(a+1)^2=a(a-1)(a+1)/6 proves tau^2<=d4.
The complete convolution sum is at most H_floor(u)^4.
Using Z of Gamma shape k, log^+(Z/(4*pi))<=log(k)+Z/k and
E(Z/k)^4<=24 gives the stated constant 200 and hence HC10's 100*pi.
The low domain has cost at most one and is retained.

For compact complex c in Re(c)>0, the pinned LS Bessel proof gives the same
uniform Fourier remainder, not an analytic continuation of a real inequality.
The pointwise estimate
|y^(c/k)-1|<=2|c|y/k for y>=1 and large k pays the singular Laurent term.
On sqrt(3)/2<=y<=1 its analogue is uniformly O(1/k).
Consequently |E*(z,1-c/k)+k/(2c)|<=C_K max(1,y) holds on the WHOLE domain.
Weighted Cauchy--Schwarz followed by HC11 gives HC15 in the source operator norm.
Compression to every internal subspace preserves this bound. The Neumann
argument is uniform on a fixed compact set bounded away from c=0.
There is no illicit complex-Hermitian replacement.

### Complete native nullvector lift and coefficient kernel

At a DL zero, normalize the surviving h_J coefficient to one.
The literal column-scaled inverse is
H_MM^(-1)=diag(A_m)^(-1) C_M^(-1), with ||C_M^(-1)||=O_J(1/k).
Since H_MJ=O_J(A_J), each earlier coefficient obeys
|u_m|<=C_J A_J/(k A_m). Its total Petersson norm is bounded by
C_J A_J/(k sqrt(A_(J-1)))=o(sqrt(A_J)); the empty block is simply absent.

The remaining deep component uses the COMPLETE dual source norm from DL15 and
the source-metric inverse from DL16. Its norm is bounded by
C_J k^(J+1) sqrt(A_(J+1))=o(sqrt(A_J)).
The sum of the finitely many earlier coefficients stays bounded.
Thus no growing deep-dimension factor is lost, and HC19 follows after normalization.
The cusp-indicator contraction transfers the high-cusp mass to this full vector.
For i>1 it is a nullvector of the restricted form, not necessarily the full form.

With the first input conjugate-linear, unfolding the Poincare series gives
G(P_j,f)=A_j a_f(j). The printed Petersson formula and the elementary Bessel
series majorant give HC20. For fixed j, its error tends to zero by the factorial
denominator. Therefore p_j>0 eventually and HC21 has exactly the stated constant.
Both unit vectors h_J/sqrt(G(h_J)) and P_J/sqrt(A_J p_J) have overlap tending
to one; HC19 and orthogonal projection then prove HC22 uniformly over selections.
No growing j or k-dependent-depth extension is inferred.

## 3. Finite and hostile verification

The exact command was python [-O] -m unittest followed by these five modules:

* tests.test_cusp_flag_hecke_source_concentration
* tests.test_cusp_flag_fixed_depth_divisor_ladder
* tests.test_cusp_flag_native_denominator_poles
* tests.test_cusp_flag_local_simple_endpoint_zero
* tests.test_cusp_flag_all_weight_endpoint_separation

All 168 tests passed: normal 39.520 seconds; optimized 39.631 seconds.
Both producer checks and all four LF-exact fixture/manifest emissions passed.
Ruff lint and format checks and the full parent-to-source whitespace check passed.

A further 35 fresh resealed mutations were rejected by ACTUAL complete reconstruction
in EACH mode, without mocking the reconstruction or using a cached expected result.
They changed every chart's final coefficient, removed whole control rows, changed
coverage ordering/work count, changed type/caps, and promoted scope or analytic onset.
The unit tests separately cover duplicate keys, nonfinite values, source seams,
artifact seals, huge integers and depth/byte/work caps.

The resident independent helper imports NO author code. It reconstructs all 18
charts using a finite binomial Delta product and forward elimination, and checks
complete source prefixes. Before running it the reviewer preregistered:
T4=T2^2-2^(k-1)Id and T2*T5=T5*T2 across all 18 charts.
Both held-outs pass, with source q orders 25,30,35 and full action checked
through q^(d+3), one step beyond the author's action prefix.
It independently regroups all 32 harmonic-majorant rows and checks 25 orders
of the symbolic prime Euler-factor identity using integer Laurent coefficients.
These are finite controls, not proofs of analytic limits.

The helper and its fixture replay byte-for-byte in normal and optimized Python.
All seven literal Git blob/LF-SHA pairs, four artifact seals and payload seal match.
No numerical periods, Gamma values, zeros or sufficient-weight thresholds were sampled.

## 4. Exact identities and release cleanup

Scientific blobs:

| file | Git blob |
|---|---|
| proof | 6fdf7dca06b7b29bfdc65973b8105f29d19baaa6 |
| producer | 79be911d4744480ec3ad86716c7e25fc580ad8c5 |
| fixture | 9851ec556ee234083f5891fdaf55009f50a52119 |
| sources | 31201458c9ef415e3990264f1b6865c1ea1884cd |
| tests | 00db6212cfccf9095e6902d51b65caf35abafb41 |

Fixture LF SHA256:
1454e3fe336ac1366c607ae9ec1f3fa9dfd8d8cca30b251cdc5937e79a7f33c6

Payload SHA256:
72a913641426c720283e794a05c1bb8b9e29ef32703d52931f3aaf40ff02c948

The original producer payload around lines 441--465 and proof section8 omit
an explicit arithmetic class/components and rounding declaration. Inspection
shows exact integer arithmetic and Fraction operations with no rounding.
The resident release vocabulary can state MIXED with CERTIFIED_INTEGER_COVERAGE
and EXACT_RATIONAL, plus a no-rounding contract, in a separately identified
metadata repair. This omission does not invalidate HC1--22 or the finite values.
No scientific repair is requested by this audit.

Remaining analytic dependencies are the cited classical inputs and the fixed-depth
DL theorem. The bounds do not establish an optimal rank threshold or an effective
onset. None of these remaining boundaries is concealed by the passing finite replay.
