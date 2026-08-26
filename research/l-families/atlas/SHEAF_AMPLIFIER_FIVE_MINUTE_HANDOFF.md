# PR #757 five-minute handoff

Status: **substantial exploratory release; RH and GRH remain open**

Frozen parent: PR #756 at
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`.  The final successor head and
complete replay ledger are recorded in
[`SHEAF_AMPLIFIER_RELEASE_AUDIT.md`](SHEAF_AMPLIFIER_RELEASE_AUDIT.md).

## What was actually found

### 1. A canonical source-exact RH criterion

For every fixed positive log-box width, the complete duplicate-`67` beta
detector satisfies

\[
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T(h_\varepsilon)_-\,dt=e^{o(T)}
 \Longleftrightarrow
 \int_0^T\lvert h_\varepsilon\rvert\,dt=e^{o(T)}.
\]

The same density is exactly a first difference of the boundary field `G`,
built from the compact-BV primitive `K_bd`, and a differentiated native half-
divisor reflection-odd energy. The box can be removed entirely:

\[
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T(G(t))_-\,dt=e^{o(T)}.
\]

The signed mass of the mollified detector telescopes to one terminal shell,
which exactly explains the finite scout's near `2:1` absolute/negative-mass
ratio. A countermodel proves this signed telescope alone cannot control
Jordan mass. These are the shortest RH-facing results in the branch. They do
not prove the required estimate; they identify it without a source-adapter
gap.

The finite prefix `L2` energy of `G` is also RH-equivalent. It expands as an
exact positive Gram sum over beta pairs with `1/16<=m/n<=16`; its diagonal is
an explicit logarithm. Thus the shortest quadratic target is one signed
off-diagonal compact-ratio beta correlation. Every fixed primitive rational
ray in that form is now evaluated exactly as `A_(a,b) log X+O(1)`, and all
rays of reduced height at most `H` cost only `O(H log(2X))` absolutely.
Consequently, for every prescribed `H=X^o(1)`, RH is equivalent to the
residual sector in which both reduced coordinates exceed `H/16`. No bound for
that high-height residual is proved.

That residual now has an exact five-oriented/three-reciprocal primitive-pair
decomposition.  The maximal harmonic square-mean estimate named `PRIMLS`
would imply RH, but is unproved and deliberately stronger than RH.  Two
further exact normal forms sharpen what it must do: coprimality Möbius
inversion writes every shell as a signed sum of one-dimensional Gram inner
products, while biased-Boolean Parseval diagonalizes every finite divisor
cube.  The latter retains the harmonic zero mode and has frozen rows at sieve
primes larger than the shell, proving that averaging over the common-factor
label alone cannot supply the missing cancellation.

The finite divisor cube is now connected back to the actual truncated
average. For every fixed primitive-height block, the `d^-1` square mean is an
exact incidence Gram with kernel `K_D(lcm(e,f))`; after division by `log D`
it converges to `67/(68 zeta(2))` times the biased-Boolean energy. Its zero
mode is an explicit `rho`-tilted Möbius pair whose Euler series still contains
`1/zeta(s)`. A dyadic nonmaximal gate named `PRIMCAR` implies `PRIMLS` and
hence conditionally RH, but is stronger and wholly unproved. The gain is an
exact analytic decomposition, not an estimate.

The `rho` weight itself is no longer mysterious. On integers prime to 67,
`mu*rho` is ordinary Möbius convolved with an explicit kernel `g`, and `g`
has an explicit inverse `h`; both are absolutely summable at half weight.
Consequently they give a bounded isomorphism on `ell^2(n^-1)`, preserve every
positive one-variable Mertens exponent in both directions, and transfer finite
pair tests as an exact weighted sum of multiplicatively dilated ordinary
Möbius tests. On squarefree-coprime primitive support this sum Boolean-
compresses: prime powers disappear, the two outer variables are coprime, and
forward and inverse have the same Euler-product mass `K_67`.
More strongly, all squarefreeness, cross-coprimality, and sieve conditions
reassemble into the same generalized ordinary primitive panel with
`(A,B,q)=(67^alpha r,67^gamma s,drs)`. For each of the three actual
`(alpha,0)` channels and fixed squarefree 67-free `q`, the
compatible image has exactly `3^omega(q)` colorings; its true
`d=1` zero mode has `2^omega(q)` saturated rays
`q=rs`. The exact positive-norm hierarchy is

`RAYPRIMCAR -> COLLPRIMCAR <- GENPRIMCAR`.

`COLLPRIMCAR` is the direct weighted-Minkowski input.
`RAYPRIMCAR` controls only compatible multiple rays and pays the
convergent `K_67(epsilon)` cost after choosing
`0<epsilon<1`; `GENPRIMCAR` controls every admissible
squarefree 67-free `q` in its stated ranges and, after harmonic
reindexing, pays `O(log^2 H)` in
vector norm / `O(log^4 H)` in energy. They are stronger,
incomparable sufficient routes at the stated subpower normalization. None is
proved. Before discarding phase, one may instead sum all compatible `r/s`
colors with the same fixed `(d,u=rs)`. This exact compression yields the
quadratic gate `AUXCOLORPRIMCAR`, with `COLORPRIMCAR` as its
`D=1` specialization. Weighted Hilbert Cauchy gives the sharp energy cost
`J_67`, and `RAYPRIMCAR` implies the auxiliary color gate. The color
gate is formally incomparable with `COLLPRIMCAR` and `GENPRIMCAR`:
it is a genuine additional cancellation target, but still unproved. Its
quadratic form is exactly a signed primitive-pair shared-support Gram with
kernel `prod_(p|gcd(N,M))(1+sqrt(p)/(p+1))`; the local Boolean block has
determinant `sqrt(p)/(p+1)`. This creates a concrete spectral/large-sieve
problem while warning that uniform inversion degenerates at large primes. The
full color family is an upper-divisor zeta transform of one coherently
oriented amplitude per product shell `N=ab`; finite-height Möbius inversion
recovers those shells exactly, while internal orientation modes are genuinely
absent at fixed `(alpha,d,I)`. Recovery in the local weighted overlap-Gram
norm has condition number asymptotic to `4sqrt(p)`, so a proof
should exploit the forward signed transform rather than whiten it prime by
prime. The scalar zero mode has no native `d`-average, and every one of these routes
leaves the nonzero incidence spectrum separate.

### 2. The raw version is impossible

The complete unmollified current has unavoidable negative atomic variation

\[
 \nu_{\rm ext}^-([1,Y])
 \ge {70+50\sqrt2\over\pi^2}\sqrt Y+O(\log Y).
\]

So the old raw-Jordan subpower premise is refuted, not open. Mollification is
load-bearing because cancellation must occur before taking the negative part.

### 3. Hard-mask amplification became exact geometry

The branch proves the sharp leverage/selected-mode Pareto frontier, shows why
dual weights do not evade it, and upgrades the relative identity

\[
 C-S=\Pi_0
\]

to honest endomorphisms on cyclic and finite-abelian torsors. Quotient masks
can compress exponentially many coordinates to fixed selected rank. The
remaining obstacle is global: construct the actual varying-place FFPS source
complex with common equivariant cleanup and conductor-uniform complexity.

For the minimal ternary mask, one formerly vague part of that sentence is now
explicit. Over every pair of squarefree degree shells `(a,b)` with
`q=1 mod 6`, universal norm lifts give a degree-16 orientation cover and one
cubic torsor. The raw, selected, and relative physical ranks are exactly
`48,32,16`; the generic selected invariant is zero; all toric ramification is
tame with support `6(a+b)`. The root monodromy and physical deck group split
as

\[
 (S_a\times S_b)\times(C_2^4\times C_3).
\]

Consequently the clean physical Kummer layer is scalable, while tensoring it
termwise with exact irreducibility still pays `2^(a+b-2)/(ab)`. This is a
local coefficient-space product-mass theorem.

There is now an exact categorical bypass. Closed-point Möbius inversion with
Adams operations extracts degrees `(a,b)` using
`2^(omega(a)+omega(b))` nonzero signed extension-field traces whenever the
joint kernel has commuting partial Frobenius actions, equivalently here a
finite external-product decomposition. The clean rank-48 ternary package
qualifies and partial Adams preserves its `48/32/16` deck-character ranks.
For `a=b`, removing ordered equal places costs another `2^omega(a)` nonzero
diagonal terms. An arbitrary sheaf on a
product has only diagonal Frobenius, so this cannot yet be applied to the
unbuilt owner/Boolean/Artin--Schreier FFPS source. It replaces an exponential
selector ledger, not the uniform Betti or signed-trace gate.

One apparent escape is now closed sharply. The exact universal `d`-cycle
selector has a unique hook-character expansion and forced absolute rank mass
`2^(d-1)/d`; no cheaper exact characteristic-zero semisimple `S_d`
presentation exists. The live escape is joint cancellation before that rank
is paid, a weaker source-specific selector, or different descended-orbit
geometry.

Even the most obvious relaxation does not help in the tested range. If a
selector need only vanish on fixed-point classes while taking arbitrary
values on all other derangement classes, exact rational dual certificates
still give, for every `2<=d<=10`, the same minimum `2^(d-1)/d` and the exact
cycle indicator as unique optimizer. This is an **exact finite** theorem;
the all-`d` statement is conjectural and no asymptotic or native-source lower
bound follows from ten degrees.

There is nevertheless an exact all-degree structure behind those finite
duals.  Their natural bounded Schur spectrum has generating series

\[
 \tanh\!\left(\sum_{r\ge1}{2^{r-1}\over r}p_rt^r\right).
\]

It saturates every hook, and its class transform depends only on the number
of cycles.  An unrestricted zero-hook algebraic correction always exists;
attaining the conjectured all-degree optimal value is now the coefficientwise
question of keeping one such correction inside every nonhook dimension box.
Strict interior inequalities are additionally needed for uniqueness.  Every
nonhook has the sharp all-degree capacity gap
`|b_(d,lambda)|/f^lambda<=(d-4)/d`, with equality on `(d-2,2)` and its
transpose.  Moreover, any bounded tableau weight depending only on the
descent set and retaining hook saturation is forced to be
`(-1)^|Des|`; it reproduces `tanh` and cannot repair the first odd-cycle
residual.  Any
nonzero perturbation supported solely on noncycle derangements with an even
number of cycles increases the exact-cycle mass globally, so an escape must
engage odd cycle counts at least three.  This is a structural reduction, not
an all-degree optimum theorem.

The contractive correction also cannot remain close to the hooks. If `X_j`
denotes its predecessor potential on `(d-1-j,j)`, every putative optimal lift
obeys the exact half-plane inequality

\[
 \operatorname{Re}\!\left((-1)^{j-1}X_j\right)
 \ge {2^d\over d}-{d\choose j}.
\]

It must therefore remain nonzero in forced alternating half-planes through

\[
 j={d\over2}-\left({1\over2}+o(1)\right)\sqrt{d\log d}.
\]

This rules out every bounded-depth, fixed-width, or merely near-hook repair.
For real lifts the half-planes are forced signs; complex lifts need not be
real. It remains a necessary condition: no contractive lift or all-degree
optimum has been constructed.

The propagation is not confined to two rows. For every fixed tail partition
`beta|-m`, every lift satisfies

\[
 \operatorname{Re}x_{(d-1-m,\beta)}
 =(-1)^{m+1}a_\beta{2^{d-1}\over d}+O_\beta(d^m),
\]

with an explicit positive Young-lattice recursion for `a_beta`. The first
three-row family has `a_(j,1)=2j+1`, and its leading diamond terms cancel
exactly. Thus fixed edge neighborhoods are rigid but consistent; the live
question is a moving-tail bulk matching theorem near the Young-lattice
center.

### 4. The first accidental notch layer is smaller than feared

The first boundary outside the support-forced detector-zero stratum is
nonzero for every family degree `n>=4`. The next boundary has an exact density
beginning at `M^-2`, with its `M^-3` correction also proved. It therefore does
not contribute another `c/M` term to the support-forced leading density.
The third boundary again begins at `M^-2`, now through `D_5=0`, and its first
mixed `D_5+D_3` channel enters at `M^-3`; both local probabilities are
positive for every odd prime power. This repeated scale makes the aggregate
growing-depth law, rather than another isolated shallow census, the real
question.

For every fixed depth `j`, exact residual/profile algebra and the standard
fixed-modulus prime-polynomial progression theorem give a fixed-`q,j`
`M^-2/M^-3` asymptotic in the finite probabilities
`Pr(D_(2j+1)+D_(2j+1-2s)=0)`. Hence no fixed depth can supply a new `1/M`
term. Moreover, independent top-degree signs give the uniform local bound

\[
 \delta_{j,s,q}=O_q(\sqrt j\,q^{-j}),
 \qquad
 \sum_s\delta_{j,s,q}=O_q(j^{3/2}q^{-j}).
\]

Thus the displayed `M^-2` and `M^-3` coefficient towers are absolutely
summable. By itself this left a different, sharper gap: the stable
range `h>=5j+2`, the `O_(q,j)(M^-4)` errors, and complementary growing-depth
profiles were not uniform enough to sum conductor layers.

That gap has now been crossed for a genuine initial growing window without
using the profile expansion.  Marking one least-degree prime, conditioning
the complete detector by CRT, and applying the function-field
prime-progression theorem gives a whole-layer bound.  For each fixed positive
`epsilon` and all sufficiently large `h`, summing through every

\[
 J\le(1/2-\varepsilon)\log_q h,
\]

the total density is still `O_q(M^-2)`.  Thus no new `1/M` population hides
in that logarithmically growing window.  The next barrier is explicit:
conditioning all lower signs costs a modulus of degree `Theta_q(q^(2j))`.

Profile averaging then crosses that first transition.  An exact weighted
chi-square/Parseval identity, together with the known function-field RH for
Dirichlet characters, gives a sufficient condition which permits the same
`O_q(M^-2)` law when the residue modulus lies within an explicit logarithmic
gap of the full conductor entropy.  It does not assert that the discrete
modulus lands in that gap for every `M`; the unconditional realized corollary
is `ell_r<=M/2` for all sufficiently large `M`.  The entropy bound also gives
a useful no-go: full residue equidistribution cannot create a
superlogarithmic window.  Beyond it, one must exploit the special detector-
zero sets or a new growing-monodromy small-ball mechanism.

The first such detector-specific compression is now exact.  The notch uses
only the quadratic sign at each small prime, so quotienting the full unit
residue space replaces its `q^ell_r` Fourier entropy by exactly `2^K_r`, where
`K_r` is the number of small primes.  The resulting unconditional gate
controls the terminal scale

\[
 r=\log_q M+\log_q\log M+O_q(1),
\]

and every earlier layer, still with total `O_q(M^-2)`.  This genuinely crosses
the generic residue wall by an unbounded additive `log log M` term, although
`r/log M` has not changed.  Degree-wise permutation symmetry gives an exact
Krawtchouk compression, but termwise character bounds recover `2^K_r`
exactly.  The open `KRAWLS` orbit-cancellation estimate would be a much larger
moonshot, conditionally reaching `r=Theta(sqrt M)`.

### 5. The finite `Sym^12` residual has a unique formal Tate repair

The arithmetic/stack adapter, ordered boundary, ambient identity, and
semisimplified stable channel `G=0` all survive re-audit. Against Shmakov's
displayed `2-4L` branch, the raw arithmetic residual is exactly `-p` at
`p=3,5,7`. The unique formal repair within the displayed carrier ledger is

\[
 [5,1]\otimes\mathbb L
\]

in the weight-16 Fricke-positive degree-three block. The unproved step is
realization of the displayed associated graded as the actual compact-support
Galois Euler class. Three rows do not prove an all-`q` correction.

## Best reading order

If you care about the direct RH mechanism:

1. [`FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md`](function_field/FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md);
2. [`FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md`](function_field/FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md);
3. [`FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md`](function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md);
4. [`FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md`](function_field/FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md);
5. [`FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md);
6. [`FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md);
7. [`FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md`](function_field/FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md);
8. [`FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md`](function_field/FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md);
9. [`FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md`](function_field/FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md);
10. [`FFPS_BOUNDARY_FIELD_FINITE_SCOUT.md`](function_field/FFPS_BOUNDARY_FIELD_FINITE_SCOUT.md)
   only after the theorem packets.

If you care about hard masks and sheaves:

1. [`FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md`](function_field/FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md);
2. [`FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md`](function_field/FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md);
3. [`FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md`](function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md);
4. [`FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md`](function_field/FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md);
5. [`FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md`](function_field/FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md);
6. [`FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md`](function_field/FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md);
7. [`FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md);
8. [`FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md);
9. [`FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md`](function_field/FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md);
10. [`FFPS_SELECTOR_STABLE_TAIL_TRANSPORT.md`](function_field/FFPS_SELECTOR_STABLE_TAIL_TRANSPORT.md);
11. [`FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md`](function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md);
12. [`FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md`](function_field/FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md);
13. [`FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md`](function_field/FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md).

If you care about standalone arithmetic geometry:

1. [`QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md);
2. [`QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY.md);
3. [`QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md`](function_field/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md);
4. [`QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md);
5. [`QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md);
6. [`QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md`](function_field/QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md);
7. [`QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md`](function_field/QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md);
8. [`QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md`](function_field/QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md);
9. [`QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md`](function_field/QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md);
10. [`GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md`](function_field/GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md).

Then read [`SHEAF_AMPLIFIER_RESEARCH_MAP.md`](SHEAF_AMPLIFIER_RESEARCH_MAP.md)
for the complete dependency and next-work map. Do not begin by reading commits
in chronological order.

## What is critical and what may be novel

- The RH equivalence is critical as a **calibration**: it proves the remaining
  one-sided estimate is neither too weak nor a surrogate. Equivalent
  criteria for RH are common, so external novelty is not asserted without a
  dedicated comparison. The source-exact reflection realization is the more
  project-specific part.
- The atomic refutation is critical internally because it kills an entire
  misleading strategy exactly.
- The torsor projector and subgroup compression are clean mechanism theorems.
  Their algebraic ingredients are classical Fourier theory; novelty, if any,
  lies in the physical-source and relative-cleanup architecture.
- The universal norm-torsor packet closes the varying-degree physical layer
  for one clean ternary shell and locates the coefficient-space exponential
  cost. The closed-point Adams packet then bypasses that cost for separable
  trace kernels. Norms, Kummer torsors, Adams operations, and cycle indicators
  are classical; external novelty is not claimed for the ingredients.
- The forced selector mass is classical character theory used as a new
  project firewall; the finite derangement relaxation adds exact rational
  dual certificates, while the all-degree `tanh` identity and algebraic lift
  isolate a contractive nonhook problem rather than prove the conjecture. No
  novelty claim is made for the hook formula, ribbon algebra, or
  weighted-`L1` framework itself.
- The fixed-depth `M^-2/M^-3` densities, their local anti-concentration law,
  the logarithmic growing-depth firewall, and the `Sym^12` formal one-Tate
  localization are the strongest standalone-mathematics candidates. They
  require specialist literature and normalization review before any priority
  claim.
- The finite scout is only a conjecture generator. Its near-logarithmic trend
  is not evidence for RH.

## Smallest open statements

1. **Boundary/reflection gate:** prove subpower negative mass of the compact
   boundary field `G`, or equivalently the positive differentiated native
   reflection gate or high-primitive-height beta correlation, without using
   RH.  A five-channel maximal sifted Möbius-pair large sieve is a clean
   sufficient statement, but is deliberately stronger than RH and unproved.
   The still stronger `PRIMCAR` removes the endpoint supremum and exposes an
   incidence Gram; it is also unproved. Its pair zero mode is now rewritten
   exactly as a Boolean-compressed generalized primitive panel. The smallest
   direct positive-norm target is `COLLPRIMCAR`; the coherent quadratic
   target is `AUXCOLORPRIMCAR`; the image-tailored uniform target is
   `RAYPRIMCAR`, while full-`q`
   `GENPRIMCAR` is a broader, differently normalized alternative.
   All are open and address only the auxiliary rho-sieved/zero-mode burden,
   not the nonzero incidence spectrum.
2. **Relative sheaf gate:** construct the global varying-place complex where
   hard and selected cleanup remain common and `C-S=Pi_0` survives with a
   usable conductor ledger. The clean ternary norm/Kummer factor and its
   divisor-cost Adams extractor now exist; the missing step is to make the
   native owner/Boolean/Artin--Schreier source separable or equip it with
   commuting partial Frobenii, then prove a uniform Betti/signed-trace bound.
3. **Weighted source gate:** transfer rich-core supply through the actual
   Boolean/owner physical shell; ambient density alone is insufficient.
4. **Sym12 realization gate:** decide whether the formal `[5,1] tensor L`
   carrier occurs in actual compact-support Galois cohomology.
5. **Deeper notch gate:** prove `KRAWLS`, or another structured small-ball
   estimate beyond the squareclass wall.  The exact quadratic quotient now
   reaches `log_q M+log_q log M+O_q(1)`; generic residue and termwise orbit
   estimates cannot reach a mesoscopic depth.
6. **Selector gate:** prove or disprove coefficientwise contractivity of the
   all-degree zero-hook lift. Algebraic existence and the global even-cycle
   no-go are settled; every solution propagates almost to the two-row equator
   and through every fixed tail. The live obstruction is moving-tail bulk
   matching; existence remains open.

## Recommended next ambitious pass

Run four lanes in parallel:

1. attack `COLLPRIMCAR` directly, exploit coherent core-color
   cancellation through `AUXCOLORPRIMCAR`, or prove the stronger
   `RAYPRIMCAR` along the exact compatible rays `q=drs`;
   retain full-`q` `GENPRIMCAR` as a broader alternative, not
   an intrinsic reformulation. The incidence predicate already survives,
   but the nonzero `PRIMCAR` spectrum remains separate;
2. prove the actual owner/Boolean/Artin--Schreier source has the partial-
   Frobenius/external-product structure required by the new Adams extractor,
   then simplify its signed divisor sum before any Betti norm;
3. attack the squareclass `KRAWLS` orbit sums or a growing-monodromy
   replacement; the exact quotient has crossed the generic entropy wall, but
   termwise character estimates stop at the additive `log log` gain;
4. attack the `Sym^12` Galois realization directly, preferably through a
   same-characteristic tower or explicit boundary cohomology rather than
   more unrelated small primes.

That keeps one direct RH lane, one family/sheaf moonshot, one notch small-ball
moonshot, and one potentially publishable arithmetic-geometry lane alive at
the same time.
