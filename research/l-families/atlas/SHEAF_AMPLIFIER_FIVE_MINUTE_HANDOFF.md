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
off-diagonal compact-ratio beta correlation. No bound for it is proved.

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
summable. The decisive remaining gap is different and sharper: the stable
range `h>=5j+2`, the `O_(q,j)(M^-4)` errors, and complementary growing-depth
profiles are not uniform enough to sum conductor layers.

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
5. [`FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md`](function_field/FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md);
6. [`FFPS_BOUNDARY_FIELD_FINITE_SCOUT.md`](function_field/FFPS_BOUNDARY_FIELD_FINITE_SCOUT.md)
   only after the theorem packets.

If you care about hard masks and sheaves:

1. [`FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md`](function_field/FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md);
2. [`FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md`](function_field/FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md);
3. [`FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md`](function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md);
4. [`FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md`](function_field/FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md);
5. [`FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md`](function_field/FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md);
6. [`FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md`](function_field/FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md);
7. [`FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md);
8. [`FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md`](function_field/FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md).

If you care about standalone arithmetic geometry:

1. [`QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md);
2. [`QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY.md);
3. [`QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md`](function_field/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md);
4. [`QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md);
5. [`QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md);
6. [`QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md`](function_field/QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md);
7. [`GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md`](function_field/GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md).

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
- The forced selector mass is classical character theory used as a new
  project firewall; the finite derangement relaxation adds exact rational
  dual certificates, not an all-degree theorem. No novelty claim is made for
  the hook formula or weighted-`L1` framework itself.
- The fixed-depth `M^-2/M^-3` densities, their local anti-concentration law,
  and the `Sym^12` formal one-Tate localization are the strongest standalone-
  mathematics candidates. They require specialist literature and
  normalization review before any priority claim.
- The finite scout is only a conjecture generator. Its near-logarithmic trend
  is not evidence for RH.

## Smallest open statements

1. **Boundary/reflection gate:** prove subpower negative mass of the compact
   boundary field `G`, or equivalently the positive differentiated native
   reflection gate or compact-ratio off-diagonal beta correlation, without
   using RH.
2. **Relative sheaf gate:** construct the global varying-place complex where
   hard and selected cleanup remain common and `C-S=Pi_0` survives with a
   usable conductor ledger.
3. **Weighted source gate:** transfer rich-core supply through the actual
   Boolean/owner physical shell; ambient density alone is insufficient.
4. **Sym12 realization gate:** decide whether the formal `[5,1] tensor L`
   carrier occurs in actual compact-support Galois cohomology.
5. **Deeper notch gate:** make the stable profile range and
   `O_(q,j)(M^-4)` remainder uniform, then count complementary growing-depth
   layers. Local trace-zero probabilities already decay exponentially enough
   to sum the displayed coefficient tower.

## Recommended next ambitious pass

Run three lanes in parallel:

1. attack the exact ratio-16 beta correlation now isolated from the compact
   boundary field, preserving its signed Gram assembly;
2. build the relative varying-place cone before paying separate conductor
   costs, using subgroup masks of fixed quotient order;
3. attack the `Sym^12` Galois realization directly, preferably through a
   same-characteristic tower or explicit boundary cohomology rather than
   more unrelated small primes.

That keeps one direct RH lane, one family/sheaf moonshot, and one potentially
publishable arithmetic-geometry lane alive at the same time.
