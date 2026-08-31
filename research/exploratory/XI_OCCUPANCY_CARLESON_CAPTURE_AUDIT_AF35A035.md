# Independent frozen review: occupancy-weighted Xi capture

Verdict: **PASS within the explicit finite/analytic/conditional scope.**
No actionable mathematical or release-contract defect was found.

Scientific source: `af35a035a921a8e3164bda3dce95290afc456645`.
Scientific base: `a7479e85fdc2a464cdc753021435cfef7a1f3910`.
Review performed independently of the author in a separate worktree. None
of the five frozen scientific files was edited. The review script and its
fixture are separate review artifacts, not replacements for the source.

Load-bearing files: `XI_OCCUPANCY_CARLESON_CAPTURE.md`, matching lowercase
producer/fixture/source manifest, and `tests/test_xi_occupancy_carleson_capture.py`.
The fixture LF-SHA256 is
`2e698f7a1be78f54ef15187565659d0bd7afefc7ba2eb0efb32d6b9be61207c4`.
All five file hashes are retained in the independent review fixture.

## 1. Local crowding and the physical Hardy metric

The source proof at lines31--104 is sound including equality endpoints,
repeated atoms, and arbitrarily small positive heights. For any nonempty
subset A, its span and maximum height determine a positive r(A). A closed
interval of that length can contain all of A, so its box ratio is at least
sum_A y/r(A). Conversely the atoms of any nonempty box form a subset with
r(A)<=box length. Empty boxes have ratio0. These two directions establish
the subset formula, rather than only one inequality.

Taking a=min_A x and r=r(A) gives an enumerated endpoint/height candidate.
Adding other eligible atoms cannot lower its ratio. Since every candidate
is itself a real box, this proves the exact polynomial-size maximum. Open
boxes have the same supremum by an arbitrarily small enlargement; this
is important when a height or horizontal span equals the width exactly.

For the global measure sum_n c_n^-1 sum_(b in cell n)y_b delta_b, a box
of width r<1 meets at most two half-open cells and each contributes<=r.
For r>=1, at most r+2 cells are relevant, and each whole normalized cell
has mass<=1. Thus the single bound3r is valid, also for closed endpoints.
Unit-cell finiteness makes the atomic measure locally finite/regular. No
uniform lower height or node separation is being silently imposed.

The boundary-dx reproducing kernel has squared norm1/(4pi y), hence

    |<F,e_b>|^2 = 4pi y |F(b)|^2.

The classical Carleson embedding therefore gives a uniform Bessel bound
for e_b/sqrt(c_n), with an absolute embedding constant. I checked the
primary [Jacob--Partington--Pott Theorem1.1](https://arxiv.org/pdf/1201.1021)
on complete printed pages2--3, including the kernel normalization on p3.
Rotation from their right half-plane to the upper half-plane preserves
boundary Lebesgue measure. The source correctly does not identify box
constant3 with the full embedding constant.

These are test-vector weights, not a new physical norm. The input subspace
and the operator Pi_[0,D] P_U remain unchanged. No band-Loewner inference,
inner/projection commutation or Euclidean coefficient metric is used.

## 2. Independent local Jensen check

The new actual-Xi claim at source lines106--169 is a genuine local count,
not a restatement of the older global O(R log R) count. Fix lambda>0 and
H>0. Write w=1/2-iz using the functional equation and

    P(w)=w(w-1)pi^(-w/2)Gamma(w/2)/2.

For Re z near T tending to positive infinity and Im z in any fixed strip,
Stirling removes the Gamma exponential after multiplication by exp(pi z/4).
The remaining Gamma/polynomial factors have polynomial size. A fixed-order
Euler--Maclaurin expansion with cutoff ceil(T) bounds zeta throughout the
enlarged strip, including its left part. The remainder is polynomial in T;
the zeta pole is far away. Cauchy estimates on a fixed additional collar
give the same type of bound for every derivative through order6. Primary
formula checks: [DLMF5.11](https://dlmf.nist.gov/5.11), including the
digamma expansion, and [DLMF25.2(iii)](https://dlmf.nist.gov/25.2#iii).

At z_T=T+i(H+2), sigma=Re w_T=H+5/2>1. Absolute Euler convergence gives
bounded zeta derivatives and |zeta(w_T)|>=1/zeta(sigma). With
q(w)=log(w/(2pi))/2, differentiated Stirling and a finite product expansion
give xi_R^(j)(w_T)=P(w_T)q(w_T)^j[zeta(w_T)+O(1/log T)]. The factors from
D_z=-iD_w were rederived, not inferred from real-axis parity:

    (-i)^5=-i,  (-i)^6=-1,
    R_lambda(z_T)=i(lambda xi_R^(6)(w_T)-xi_R^(5)(w_T)).

Since lambda is fixed positive and |q| grows, the sixth-order term cannot
cancel the fifth-order term or the bounded zeta-derivative error. The
modulus of exp(pi z_T/4)P(w_T) is bounded below by a positive constant
times T^(sigma/2+3/2). Thus the stated anchor lower bound, including its
log^6 T factor and signs, is correct.

The desired rectangle lies strictly inside radius H+3 about z_T because
1+(H+2)^2<(H+3)^2. A concentric disk of twice that radius stays within a
fixed enlarged strip, so Jensen gives O_(H,lambda)(log T). An outer-circle
zero does not spoil Jensen: its logarithmic singularity is integrable,
or one takes limits through nearby regular radii. Finally real/even Xi
implies R_lambda(-conjugate z)=-conjugate(R_lambda(z)), paying the negative
T side. Remaining bounded T is a compact entire zero count. The anchor
also proves that R_lambda is not identically zero.

This proof is not uniform in H or in varying lambda. It supplies no
existence, lower density, simplicity, common-factor survival, or lower
height estimate for zeros. Those omissions are accurately preserved.

## 3. Conditional capture, and indispensable remaining hypotheses

I read the full frozen LB proof at `a7479e85...`, as well as the pinned
uniform companion and actual-kernel notes at `1904d20c...` and the complete
preregistration `4f38c14b...`. Normalizations agree. In particular LB's
physical formula contains the indispensable |U(b)| factor and uses
scalar modulus comparisons at b and ih, not projection order after a band.

Under the explicit common-inner premise, every declared surviving zero
b belongs to the denominator model space. Choosing h=|x| in LB and using
the fixed-lambda axis limit gives, eventually,

    ||Pi_[0,D]P_U e_b||^2
      >= |Theta0(b)|^2 y/(10|x|)-exp(-2D|x|).

Here y<=1<=|x|, the denominator bound is sqrt5|x|, the axis modulus is
eventually at least1/2, and [a-e]_+^2>=a^2/2-e^2. All constants match.
Divide by the SAME full-family c_n used for the Bessel family. The local
O(log(2+|n|)) zero count makes the negative exponential sum finite, while
the positive sum diverges precisely under the explicitly unpaid OC11.
For any finite prefix, synthesis of weighted kernels gives TT*<=C P_KB;
therefore sum||Pi P_U e_b||^2/c_n<=C||Pi P_U P_KB||_HS^2. The constant
does not depend on the prefix. This proves the conditional infinite-HS
conclusion without identifying nonorthogonal diagonal sums with a trace.

The coarser inverse-count and inverse-log criteria are valid sufficient
conditions. For arbitrary unit-cell-finite families the inverse-count
weights pay the exponential tail directly. The finer c_n weights need
the separate tail-count bound; the source explicitly retains it and pays
it for actual Xi. Choosing at most one node per cell resets c_n=1 for
that selected input family, and does not claim completeness of that family.

The synthetic crowded example satisfies the Blaschke condition since
sum log(n)/n^2 converges, while its unweighted finite Gram norms grow.
Its weighted alignment for U=1 is harmonic and divergent. This does show
that weighting is more than the old unweighted Bessel premise renamed.
The sparse dyadic-survey example only obstructs the sufficient alignment
criterion; it does not establish finite actual band energy. Both limits
are respected in the source.

Still unpaid: the literal inner premise, source-owned survival and a
divergent cofinal actual-Xi alignment sum. Neither the local count nor
the exact Carleson cost proves any one of them. No native decoder,
outer-metric identification, complete denominator census or RH conclusion
is accepted by this review.

## 4. Independent finite replay and hostile checks

The independent script reconstructs the complete32 family records from
the declared rational primitive formulas without importing author arithmetic.
Dispersed costs follow from the all-subset gap inequality; crowded costs
follow from diameter<height. The mixed control is checked by exhaustive
subsets. It independently reconstructs every one of600 interval rows,
all16 Rayleigh records using difference multiplicities instead of a double
node loop, and all32 dyadic-tail records from the closed formula.

Only after this reconstruction is author code imported, for384 additional
endpoint/subset cases and49 hostile rejection checks. The extra grid
includes all subsets of sizes1--5 from nine independent endpoint/height
nodes, plus repeated and edge-height cases. The attacks include fully
resealed numeric/type/coverage/order/metric/scope/artifact/source changes;
actual corruption of each of the four returned Git source byte streams;
mocked changes to every current bound artifact; duplicate/nonfinite JSON;
and integer/rational/depth/byte/coverage cap violations.

All four source Git blobs and LF hashes, all four current artifact hashes,
and the payload seal were independently authenticated. Every frozen
scientific file is compared with its exact Git source before review replay.
The author checker rebuilds the primitive rows, so re-sealing a forged JSON
does not authorize it. Its guards do not rely on Python assertions.

Results:

- Original18 tests: PASS normal5.134s; PASS under -O5.163s.
- Both original producer checks and all four LF-normalized emit comparisons:
  PASS. The original source fixture hash is recorded above.
- Independent full-record reconstruction,384 additional cases and49
  hostile rejections: PASS in normal Python and under -O.
- Ruff lint/format and full scientific base-to-SHA whitespace check: PASS.
- All five science files remained unchanged; only the three review files
  belong to this review commit.

The finite arithmetic classification is MIXED with EXACT_RATIONAL and
CERTIFIED_INTEGER_COVERAGE; rounding is none. No numerical Xi evaluation,
directed transcendental certificate or analytic theorem formalization is
claimed. The written proof audit, imported classical results, and exact
finite replay are distinct obligations.

Replay the review itself:

    python -B research/exploratory/xi_occupancy_independent_audit_af35a035.py --check
    python -B -O research/exploratory/xi_occupancy_independent_audit_af35a035.py --check

Smallest analytic invalidator: failure of the noncancelling fixed-lambda
Euler anchor would remove the local logarithmic Jensen estimate; failure
of the source-compatible inner premise or OC11 would prevent the cofinal
application, but those are hypotheses, not claims proved here.
