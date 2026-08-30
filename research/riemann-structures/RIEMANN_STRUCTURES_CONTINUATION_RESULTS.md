# Riemann Structures: continuation checkpoint

Status: source-bound exact results and explicit open interfaces for
[programme #763](https://github.com/gfreund123/riemann/issues/763),
carried by [draft PR #765](https://github.com/gfreund123/riemann/pull/765).
This is a research checkpoint, not completion of the requested eight-hour
pass, a canonical repository integration, or an RH claim.

## Five-minute result

The useful structural distinction is now sharper: retaining a scalar
sequence, retaining its labelled source, and retaining its metric are
different requirements. A successful structure must preserve the particular
operation the consumer needs. None of the packets below constructs a new
number-field geometry or supplies the missing RH-level estimate.

| Mechanism | Exact result now available | Boundary that still matters |
|---|---|---|
| Marked finite-field source | Shared-conductor support and the Wick occupancy spectrum; explicit live source collisions | A surviving cell and an indefinite form do not prove freedom of native coefficients or a signed trace bound |
| Source algebra before pushforward | Literal diagonal tensor and relative Adams extraction require the retained finite source algebra | Isomorphic pushed Frobenius representations can give different diagonal and primitive-orbit data |
| Signed history recombination | History-only representation interference has a subpower principal-channel payment in the original integrated source | Cross terms between distinct retained groups remain, including groups with the same arithmetic tuple but different labels |
| Archimedean ladder | Infinite polynomial ladders reproduce gamma factors; finite virtual gamma cancellation and parity defects are explicit | The odd duality/tensor boundary is not repaired by calling the ladder a finite Euler object |
| Unlabelled family control | A principal labelled value is not determined by its unlabelled family except on all-equal orbits | This does not forbid stronger labelled data or the native signed identity P=A-K |
| Earlier actual-Xi source | A direct real-kernel proof gives sharp current concentration and carrier-mismatch asymptotics | Source-frequency softness is not a physical or outer-normalized Pick-metric bound |

## What to read first

1. [Signed history recombination](../l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md)
   and its [independent review](../l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION_AUDIT.md).
   This identifies a real payment, not just an obstruction.
2. [Source-algebra diagonal/Adams adapter](SOURCE_ALGEBRA_DIAGONAL_ADAMS_ADAPTER.md).
   This is the cleanest finite example of why source identity matters.
3. [Actual Xi concentration](../exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md)
   and its [exact-source review](../exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION_AUDIT.md).
   This supplies a previously conditional analytic input.
4. [Archimedean ladder boundary](ARCHIMEDEAN_LADDER_BOUNDARY.md)
   and its [review](ARCHIMEDEAN_LADDER_BOUNDARY_AUDIT.md).
5. [Unlabelled-family firewall](FAMILY_BINDING_PERMUTATION_FIREWALL.md).

The [original wave-2 portfolio](RIEMANN_STRUCTURES_WAVE2_PORTFOLIO.md)
remains the broader literature and mechanism map. Its unfinished-work
lists are historical; this checkpoint supersedes their status.

## The finite-field result is not just a synthetic collision

The [live shared-fibre packet](../l-families/atlas/function_field/FFPS_LIVE_SHARED_FIBRE_COLLISIONS.md)
constructs actual owner/cofactor labels obeying the frozen source windows.
Its two-core-by-two-core control has four arithmetic pairs and sixteen
histories in one residue cell. A separate one-pair control has one hundred
histories, signed total 4, literal squared diagonal 676, and recombination
defect -660.

Those controls establish physical occupancy. They do not let us choose
arbitrary coefficients in the negative eigenspaces of the
[occupancy form](../l-families/atlas/function_field/FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md).
The native coefficient and phase constraints must remain attached.

More importantly, grouping histories while retaining every other label
gives an exact diagonal correction. The dangerous additive and character
corrections cancel jointly to the principal correction. The original
integrated principal diagonal and the subpower history multiplicity pay
that correction. This preserves the uncentered principal source and its
centered target at the stated subpower scale.

The unpaid object is the cross-group source. Distinct retained groups
need not have distinct arithmetic tuples: masks, carriers, and other
retained labels can differ. The full signed cancellation and principal
binding problem has not disappeared.

## Earlier work is explicitly retained

### Architecture A: the central 67-free source

[PR #760](https://github.com/gfreund123/riemann/pull/760) remains the
separate home of the core-wavelet work. The new single-channel packet
proves that the complete beta source is the stable second multiplicative
difference of one 67-free Mobius source:

    beta = (delta_1-delta_67)^(*2) * mu^(67-free).

Its finite sharp-prefix inverse preserves the relevant positive-exponent
maximal L2 bounds. It reduces the three exceptional panels to one central
source for this purpose. The assembled central criterion remains
RH-equivalent and unproved; the stronger positive core gates are sufficient
routes, not estimates already supplied by the reduction.

That packet lives on the PR760 branch, not as a duplicate theorem on this
branch. Its file is
FFPS_BETA_SECOND_DIFFERENCE_SINGLE_CHANNEL_REDUCTION.md under the
function-field atlas.

### Architecture B: relative extraction and source labels

The earlier PR756/757/760 work supplies the relative-first extraction
problem. The new finite source-algebra adapter explains why extracting
after forgetting the source changes the problem. It constructs no
complete native sheaf, partial-Frobenius realization, or uniform Betti
bound. Those are still substantive targets.

### Actual Xi: a new proof, not an inherited assertion

For every fixed positive odd K, the literal current measure now satisfies

\[
 m_2\sim\frac{3}{2\pi}e^{-\xi},\qquad
 g_K\sim\frac{\pi}{K}\xi^2e^\xi,\qquad p_K\longrightarrow\frac1{2K}.
\]

The proof includes all-real tail domination, a positive denominator
bound, and fixed exponential-weighted moments. It corrects an old
factor-of-two Fourier-kernel normalization without editing the historical
source; all normalized ratios are unchanged.

Together with the [near-adapted-scale scout](../exploratory/XI_NEAR_ADAPTED_SCALE_FIREWALL.md),
it shows that bounded mismatch requires relative tuning on the scale
exp(-xi)/xi^2. The common outer factor, physical constant companion,
collective/confluent localization, and source-Pick free energy remain
separate analytic requirements.

## Next scientific decisions

1. Test the actual outer-retaining denominator-jet band metric. A confluent
   packet extension is under construction; no result from that unfinished
   packet is imported here.
2. Analyze the native cross-group signed form, retaining its coefficient
   factorization and all labels. Enlarging a free-vector matrix is not
   a substitute.
3. Attack an actual central-source cancellation estimate in Architecture A.
   Do not spend another pass merely renaming an RH-equivalent norm.
4. Use the archimedean and source-algebra examples as tests of any proposed
   common categorical object. It must explain an operation and a held-out
   phenomenon, not just contain the known scalar formulas.

The two new programmes retain separate branches. The generalized-L
programme tests scalar recovery, representation parents, and now global
completion obstructions; its claims are not dependencies of the signed
finite-field or Xi estimates.

## Reproducibility and priority

Each packet has its own frozen source manifest, bounded exact producer,
tests, and scope contract. Reviews identify the exact scientific commit.
Normal and optimized Python are both required. Bounded algebra does not
machine-prove an analytic asymptotic.

[Source acquisition instructions](CONTINUATION_SOURCE_REPLAY.md) retain
the original cherry-picked scientific identities for independent review.
Classical Frobenius, Adams, gamma, Hardy, and Laplace mathematics is
acknowledged. The research contribution is the specific tested interface
or obstruction; this checkpoint makes no external novelty claim.

RH and GRH remain unsolved.
