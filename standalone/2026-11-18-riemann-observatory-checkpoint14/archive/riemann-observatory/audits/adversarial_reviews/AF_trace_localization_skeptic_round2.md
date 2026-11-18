# Independent localized repair of the AF trace estimate

Reviewer: search_skeptic. Date:2026-11-17. Sources inspected directly: Alpöge–Furman, arXiv2608.13637v2, §2.2–2.3, Lemma2.1 and Proposition4.2, pp4–6; Arias de Reyna, arXiv2610.24612v1, §7 Proposition16 and its footnote, pp14–16. This review concerns the trace only. It does not audit the Hilbert–Schmidt estimate, the formal artifact or the complete proportion theorem.

**Conclusion:** the printed distance step requires correction, but the trace conclusion has an independent localization proof. Under the stated fixed-window hypotheses one obtains

tr G̃=N(I)+O(√T),

and therefore, for the buffered interval I′=[T−√T,2T+√T),

tr G̃=N(I′)+O(√T log T).

This implies both the AF displayed O(√T L²) remainder and the weaker O(T/log T) accuracy, where L=log(T/(2π)). No counterexample to the trace estimate was found.

## Definitions and exact hypotheses used

Set L=log(T/(2π)), h=2π/L, X=e^L=T/(2π), d=floor(T/h), and α_k=T+kh. Retain k=0,…,d−1. Let I=[T,2T), I′_U=[T−U,2T+U), with0≤U≤T/2; the requested choice is U=√T. A zero is written z=t+iη in the γ-coordinate, with |η|≤1/2, and its positive integer multiplicity is m_z.

The matrix is

G̃_U=(aL²)^−1 Σ_{t∈I′_U}m_z v_z v_z^T,

(v_z)_k=φ̂(z−α_k), a=||φ||²_2/L.

The proof uses these explicit facts, all available for the two fixed AF windows:

1. φ is real, even and C², supported in[−L/2,L/2]. There is a T-independent bound |φ|≤M; AF has M=1. The normalization satisfies a≥a0>0 for all sufficiently large T. Fixed ψ and fixed cutoff χ give this through the bulk norm calculation.
2. The decay bound |φ̂(r+iη)|≤C e^{L|η|/2}|r|^−2 for |r|≥1, with C uniform in T. This is the two-integration-by-parts part of(2.8).
3. The diagonal Poisson identity Σ_{k∈Z}φ̂(z−α_k)^2=aL², including complex z.
4. The multiplicity-weighted number of zeros in every real ordinate interval of length1 within[T/2,3T] is O(log T)=O(L). This is the classical local zero-count bound used by both sources. It controls counts, not zero spacing.

The implied constants depend on M,a0,C and the local-count constant, hence on the fixed window/cutoff, but not T or U. This argument does not cover a varying family of windows without uniform versions of those bounds.

## What fails in the printed geometric step

The implication “k outside[0,d) implies α_k outside[T,2T)” is not true at the first omitted right grid point. If δ=2T−α_d, the exact floor relation is0≤δ<h. Thus α_d=2T−δ can lie inside I.

A separate issue remains even with an endpoint-aligned grid: for a zero ordinate t in the **exterior buffer**, distance to an omitted grid point can be tiny while distance to{T,2T} is large. The bound |t−α_k|≥dist(t,{T,2T}) is an interior-window assertion, not an assertion for all t∈I′_U. For example the real point t=α_−1 gives distance0 to that omitted point while its boundary distance is h. This example identifies the geometric defect; it is not claimed to be a zeta zero. For large U=√T the usual Riemann–von Mangoldt count also supplies actual zeros in exterior subintervals a distance comparable to U from T, where the nearest omitted lattice point is within h/2, so the missing interior restriction cannot be supplied by a special property of zeta zeros.

Arias de Reyna's Proposition16 instead bounds the entire enlarged endpoint region, containing O(U log T) zeros, by a worst-case per-zero estimate. At U=√T that error need not be o(N). This shows that particular bound is insufficient at that buffer size. It does not show the true trace estimate is false. The repair below handles far exterior zeros through their **retained-grid** tails and reserves the worst-case mass estimate for unit endpoint strips only.

## A uniform absolute lattice-mass bound

For z=t+iη, Parseval on the interval of length L gives the exact identity

Σ_{k∈Z}|φ̂(z−α_k)|²=L∫_{−L/2}^{L/2}φ(u)²e^{2ηu}du.

Indeed these transforms are, up to a unit complex phase, the Fourier coefficients of φ(u)e^{ηu}e^{−i(t−T)u} in the orthogonal basis of frequencies2πk/L. This identity is for absolute squares and is different from the bilinear diagonal Poisson identity.

Because |η|≤1/2,

∫_{−L/2}^{L/2}e^{2ηu}du

=2∫_0^{L/2}cosh(2ηu)du≤2∫_0^{L/2}cosh(u)du

=2sinh(L/2)≤e^{L/2}.

It follows that

(aL²)^−1 Σ_{k∈Z}|φ̂(z−α_k)|²≤(M²/a0)e^{L/2}/L.

There is no division by η and no issue at η=0. This estimate gains a factor L compared with bounding each transform at its largest possible size and then summing a crude envelope.

The bilinear Poisson identity needed for the trace can also be justified without assuming its complex extension: for real z, apply Poisson to φ̂², whose inverse transform is φ*φ and vanishes at the two endpoints ±L. The nonzero dual lattice terms vanish. The series of squares converges normally on compact complex sets by the C² decay, so the constant identity extends to complex z by the identity theorem. Evenness makes (φ*φ)(0)=||φ||²_2. No positivity of the individual complex squares is assumed.

## Three-region localization

Write E=e^{L/2}=√X and

p(z)=(aL²)^−1 Σ_{0≤k<d}φ̂(z−α_k)^2.

Then tr G̃_U=Σ_{t∈I′_U}m_z p(z). All inequalities below bound complex absolute values; conjugate pairing is unnecessary for the estimates themselves.

### 1. Unit endpoint strips

Consider |t−T|<1 or |t−2T|<1. The number of zeros, counted with multiplicity, is O(L). The absolute-mass bound gives |p(z)|≤C E/L. Thus their combined contribution to

Σ_{t∈I′_U}m_z[p(z)−1_I(t)]

is O(E+L)=O(E). This includes either endpoint convention and the first omitted right grid point.

### 2. Interior points away from endpoints

For t∈I with D=min(t−T,2T−t)≥1, the omitted grid points have distance at least D−h on the right and at least D on the left. For large T, h≤1/2, so D−h≥D/2. A one-sided lattice sum gives

Σ_{k outside[0,d)}|t−α_k|^−4

≤C[D^−4+h^−1 D^−3]≤C L D^−3.

By the bilinear Poisson identity and the uniform decay bound,

|p(z)−1|≤C(E/L)D^−3.

Partitioning distance into unit strips and using the local zero-count bound gives Σ m_z D^−3=O(L). Hence this entire interior region contributes O(E), despite containing O(TL) zeros.

### 3. Exterior buffer points away from endpoints

For t∈I′_U outside I, at distance r≥1 from I, estimate the **retained** lattice sum directly. Every retained α_k is in I; summing from the nearer end yields

Σ_{0≤k<d}|t−α_k|^−4≤C[r^−4+h^−1 r^−3]≤C L r^−3.

Therefore |p(z)|≤C(E/L)r^−3. The local zero-count bound gives Σ m_z r^−3=O(L), independently of U≤T/2, because Σ_{j≥1}j^−3 converges. The exterior contribution is again O(E). It is incorrect here to approximate each exterior zero's finite trace contribution by1.

## Trace and buffered-count conclusions

The three regions prove

|tr G̃_U−N(I)|≤C E=O(√T),

uniformly for0≤U≤T/2. Endpoint multiplicities are O(L) and are already covered by the unit-strip estimate.

The symmetric difference I′_U\I consists of two intervals of total length2U. Thus

|N(I′_U)−N(I)|≤C(U+1)L,

so

|tr G̃_U−N(I′_U)|≤C[√T+(U+1)L].

For U=√T this is O(√T L). Since L²/√T→0, this is o(T/L), and therefore certainly O(T/log T). It also implies the larger AF Proposition4.2 remainder O(√T L²).

The count N(I) here uses the same half-open interval as the matrix definition. Replacing it by a conventional N(T,2T] changes only endpoint counts O(L). No RH assumption, inter-zero separation or unproved density conjecture enters the repair.

## Audit status

The missing geometric restrictions and floor-grid endpoint correction are real issues in the printed passage. They do not furnish a counterexample to Proposition4.2. A detailed localization plus Parseval supplies the required trace estimate with room. Parent and root were informed while independently examining the same source question; final adjudication belongs in their combined review. This finding is best recorded as a repaired scoped argument, not an assertion that the author's main theorem is false.

Other parts of the AF and Arias de Reyna arguments remain outside this review. In particular this proof does not establish the Hilbert–Schmidt second moment, any operator positivity statement or the final zero proportions.
