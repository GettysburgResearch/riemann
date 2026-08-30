# Riemann Structures: wave-2 portfolio and research boundary

Status: **programme map with exact finite-algebra results, open geometric and
analytic gates, and externally unreviewed novelty**

Issue: [#763](https://github.com/gfreund123/riemann/issues/763)

## Bottom line

The first marked-descent packet found a clean universal chart, but it did not
construct the complete native source or prove descent.  The source-faithful
second wave now changes the diagnosis more sharply:

1. the Wick pair lives in a relative self-product over one fixed conductor
   fibre; an independent product of two marked charts is the wrong object;
2. the exact finite operator separates into an aggregated residue term and an
   atomic diagonal-energy term;
3. residue aggregation alone is sufficient for every coefficient vector if
   and only if the live occupancy map is injective;
4. complete-cell occupancy is full-rank and indefinite, while incomplete
   occupancy can be singular.

This is a useful structural criterion, not native noncancellation.  It makes
live occupancy classification the first gate.  In parallel, an adapter meant
to work uniformly over arbitrary occupancies must retain literal diagonal data
before label forgetting and signed conductor recombination.

The programme should nevertheless remain broader than this one sheaf lane.
Four mechanisms are retained below: relative Frobenius geometry,
archimedean local objects, transfer/operator parents, and synthetic
counterfeit worlds.  They have different failure modes and held-out tests.

RH and GRH remain unproved.

## 1. Exact wave-2 result ledger

Let one native conductor fibre be indexed by

\[
 \iota=(g,\ell,\rho,\sigma,\tau),\qquad \ell\ne\rho,
\]

and let `Omega_iota` be its retained source atoms.  Two Wick atoms share
`iota`; they do not carry independently chosen marked primes.  If `R` is the
cell-by-atom incidence matrix for the crossed physical residue map, put

\[
 m_q=\frac{q-1}{2},\qquad
 H_q=I_{m_q}-\frac1qJ_{m_q},
\]

\[
 S=H_\ell\otimes H_\rho,
 \qquad
 d=\left(1-\frac1\ell\right)
   \left(1-\frac1\rho\right).
\]

The normalized fixed-fibre Wick operator is

\[
 \boxed{B_R=R^*SR-dI.}
\tag{1.1}
\]

For a coefficient vector `z`,

\[
 \boxed{
 z^*B_Rz=(Rz)^*S(Rz)-d\sum_\omega|z_\omega|^2.
 }
\tag{1.2}
\]

Equation (1.2) gives both an exact sufficiency criterion and a universal
replacement design.

| verdict | exact content | what it does not prove |
|---|---|---|
| shared-fibre carrier | the correct pair object is `(Omega x_I Omega) minus Delta`, with literal source diagonal | existence of a descended sheaf or commuting partial Frobenii |
| two-channel sufficiency | `(Rz, sum abs(z)^2)` reconstructs the finite Wick form exactly | that both channels occur canonically after native pushforward |
| residue-forgetting criterion | `Rz` determines the scalar for all vectors iff `ker R=0`; two same-cell atoms give the exact failure witness | a duplicate cell or free kernel-direction coefficients in the complete live source |
| kernel theorem | on `ker R`, `B_R=-dI`; source-difference energy is invisible to residue totals | a favourable sign after all source coefficients are inserted |
| complete-cell spectrum | one atom in every allowed cell gives four spectral blocks, every positive-multiplicity eigenvalue nonzero, and a full-rank indefinite operator for distinct odd primes | heredity to the live incomplete occupancy |
| incomplete-occupancy obstruction | singleton occupancy is zero; for `n>=2` and odd primes `p>=5`, `q=p(n-1)+1`, a `2 by n` rectangle and its transpose have nullity one | classification of the actual native occupancy matrix |

The exact source-locked theorem packet is
`FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md` in the function-field atlas.
Its replay, not this programme map, is the canonical proof artifact.

### Structural interpretation

The second term in (1.2) is not a bookkeeping nuisance.  It is precisely the
normal-ordering correction that distinguishes literal atom equality from
equality after physical collapse.  If the live occupancy is injective, it is
recoverable from `Rz`; if a cell is duplicated, it is not.  Therefore a
`ONEPLACEWEIL` object intended to work without first proving live injectivity
must retain either:

- the literal relative diagonal and its cone/complement;
- a second quadratic-energy channel compatible with pushforward; or
- an equivalent enriched object from which both statistics descend.

No duplicate occupied cell has yet been proved in a complete live fibre, and
native coefficients have not been shown to range freely in a kernel
direction.  The injectivity test and the universal enriched construction are
the two honest bridges to the unfinished #760 relative-first architecture.

## 2. Repository boundary map

| lineage | exact inheritance | boundary that remains open |
|---|---|---|
| [#737](https://github.com/gfreund123/riemann/issues/737) | function-field mirror and physical-occupancy problem | a source-faithful object binding the literal native source |
| [#739](https://github.com/gfreund123/riemann/issues/739) | trace-formula attack vocabulary and memberwise target | a usable relative trace theorem with principal individualization |
| [#743](https://github.com/gfreund123/riemann/issues/743) | common-mother and physical-restriction interfaces | exact gluing without source-blind collapse |
| [#746](https://github.com/gfreund123/riemann/issues/746) | Frobenius--Hodge and `F_1` candidate language | an honest object, polarization, and local--global theorem |
| [PR #756](https://github.com/gfreund123/riemann/pull/756) | exact residual mechanisms and physical-squareclass bridge | `CYSEL`, source port, and principal binding |
| [PR #757](https://github.com/gfreund123/riemann/pull/757) | cyclic torsor, partial Adams masks, divisor wavelet, and named trace gates | native external-product adapter and uniform trace control |
| [PR #760](https://github.com/gfreund123/riemann/pull/760) | full core-wavelet reduction and relative-first Adams interface | `NATREL`, `RELPARTFROB`, `RELTRACE`, and new principal binding |
| [PR #765](https://github.com/gfreund123/riemann/pull/765) | fixed-label rank-one trace externality and clean-chart support/rank tax | complete occupancy, signed descent, `ONEPLACEWEIL`, and member binding |

The present wave does not replace any open analytic gate by finite linear
algebra.  It refines `NATREL`: a native relative adapter must preserve the
diagonal-energy channel in (1.2).

## 3. Primary-literature boundary

These references mark established territories.  They are not evidence that
the repository packet is new.

| territory | primary boundary | lesson for this programme |
|---|---|---|
| weights and Frobenius | Pierre Deligne, [*La conjecture de Weil II*](https://publications.ias.edu/node/386) | a critical-line theorem in the function-field world uses an actual sheaf/cohomology/weight package, not the word “Frobenius” |
| trace and local `L`-functions | [SGA 4½, Exposé II: Trace formula and L-functions](https://grothendiecksga.com/read/sga4.5/en/II_3.html) | pointwise traces, compactly supported cohomology, and Euler factors are tied by a literal functorial trace formula |
| archimedean determinant models | Christopher Deninger, [*Local L-factors of motives and regularized determinants*](https://doi.org/10.1007/BF01231885) | writing a gamma factor as a determinant is established; naturality, duality, and tensor compatibility are the real tests |
| dynamical parents | Giulietti--Liverani--Pollicott, [*Anosov Flows and Dynamical Zeta Functions*](https://arxiv.org/abs/1203.0904) | a transfer operator acts on independently defined spaces and controls meromorphic continuation; a fitted finite matrix is not analogous |
| relative trace comparison | Yiannis Sakellaridis, [*Beyond Endoscopy for the Relative Trace Formula II*](https://arxiv.org/abs/1402.3524) | nonstandard transfer operators between trace formulae are established and highly structured; repository terminology alone creates no novelty |
| explicit-formula axioms | Andrew Booker, [*L-functions as distributions*](https://arxiv.org/abs/1308.3067) | Euler, functional-equation, and explicit-formula data can be organized distributionally; synthetic worlds must be compared with this existing framework |
| characteristic-one geometry | Connes--Consani, [*Geometry of the scaling site*](https://arxiv.org/abs/1603.03191) | arithmetic/scaling-site and tropical Riemann--Roch programmes already exist; any `F_1` proposal needs a precise non-overlap and stronger exact output |

The literature audit yields one immediate rule: “new Riemann structure” is
too strong a label until an independently defined object explains at least
two distinct phenomena and survives a held-out prediction or counterfeit.

## 4. Four contrasting mechanism lanes

### M1. Source-faithful relative Frobenius geometry

Candidate object: a relative complex on the shared conductor fibre product,
with a literal diagonal triangle and commuting total/partial Frobenius where
defined.

Required outputs:

1. recover both terms of (1.2), not only the residue aggregate;
2. support partial Adams extraction on the relative channel;
3. produce a signed trace with a uniform complexity bound;
4. bind the resulting family statement to the principal consumer.

Falsifier: after a duplicate live cell is proved, any construction whose
pushforward factors only through `Rz` is ruled out for arbitrary coefficient
vectors on that fibre.  Independently, a construction that recreates the
target quadratic form by choosing a bespoke inner product is fitted, not
geometric.

Promotion test: one honest complex should explain normal ordering and partial
Frobenius, then predict an unused conductor-recombination identity.

### M2. Archimedean local object and compatibility rigidity

Candidate object: an independently defined archimedean complex, flow, or
regularized operator carrying real/complex local types.

Required outputs:

1. the correct gamma factors;
2. contragredient/duality shifts;
3. tensor and parity rules;
4. the archimedean term of an explicit formula.

Falsifier: multiplying a determinant by an ad hoc entire symmetric factor can
preserve a formal functional equation.  Determinant form plus reflection is
therefore insufficient.

First bounded experiment: encode the `GL(1)` real and complex gamma factors,
their parity shifts, duals, and the smallest tensor products; classify
finite-rank determinant models satisfying all rules before allowing
regularization.  Failure is valuable if it isolates the exact need for an
infinite-dimensional object.

### M3. Transfer-operator or dynamical parent

Candidate object: a fixed dynamical system and Banach/Hilbert complex whose
periodic orbits produce prime-power terms and whose resonances produce the
spectral side.

Required outputs:

1. an independently defined orbit set;
2. a nuclear/Fredholm determinant or justified regularization;
3. a duality/time-reversal operation;
4. functorial behaviour across at least one twist family.

Falsifier: inserting prime powers as chosen orbit lengths or known zeros as
eigenvalues is circular.  Matching one explicit formula is not a held-out
prediction.

Held-out comparison: apply the same object schema without retuning to one
Ihara/graph example and one arithmetic twist.  The graph side is a calibration
world, not evidence that the number-field transfer exists.

### M4. Synthetic explicit-formula and family-binding worlds

Candidate objects: exact distributions or finite trace systems in which
Euler data, reflection, positivity, and member selection can be independently
switched on and off.

Required output: minimal counterexamples showing which combinations are
cheap to counterfeit and which force a genuine source.

Completed structural firewall:
[`FAMILY_BINDING_PERMUTATION_FIREWALL.md`](FAMILY_BINDING_PERMUTATION_FIREWALL.md)
constructs two labelings of the same complete unlabeled scalar-trace family
with identical every-order averages and opposite selected traces.  The
principal value is recoverable on a full permutation orbit exactly when
all entries are equal, including `N=1`.  A nonnegative first mean alone pays
the sharp factor `N`; signed mean-zero examples show why nonnegativity is
essential.  This is elementary exact interface algebra, not a novelty claim
or a counterfeit arithmetic `L`-function.

Next target: test a proposed binding axiom against the pair and quantify
its additional source information.  The firewall does not prohibit bounds
on every member from stronger symmetric data: the complete multiset knows
the maximum, and higher moments may improve the first-mean loss.  Nor does
it obstruct labeled signed extraction such as `P=A-K=C-S`.

Falsifier: a “counterfeit” defined by first choosing the desired zero set is
uninformative.  The synthetic world must be specified upstream by local or
trace data.

## 5. Exact bounded corpus and held-out tests

The first corpus is deliberately small enough for exact replay and broad
enough to reject fitted structures.

| corpus block | calibration data | held-out requirement |
|---|---|---|
| native shared fibres | distinct odd marked primes and the exact atom/residue map | arbitrary live occupancy and label multiplicity, not only one atom per cell |
| diagonal controls | singleton; two same-cell atoms; complete cell grid | exact `2 by n` singular family in both orientations and source coefficients with cancellations |
| source lineage | exact claims `L-106120`, `L-106131`, `L-106191`, `T-106140` | signed conductor recombination and equal-output split |
| function-field analogue | clean trace/weight examples | one literal relative pushforward with partial Frobenius |
| archimedean block | `GL(1)` real/complex gamma data | dual, parity, and tensor rule not used to fit the model |
| dynamical block | one finite graph/Ihara determinant | one Anosov/transfer determinant and one arithmetic twist schema |
| family-binding block | complete unlabeled scalar-trace multiset; every-order moment invariance; sharp nonnegative first-mean tax | a principal-label swap invisible to all symmetric data; `N=1`, repeated/all-equal, and signed controls |

The finite-cell rows test formulas; they are not evidence for live native
occupancy.  Broad finite-field or zero sweeps are not the next bottleneck.

## 6. Proof-sized targets

### T1. `DIAGREL`: a two-channel relative object

Construct a canonical relative triangle or graded object, valid without an
injectivity hypothesis, whose trace gives

\[
 (Rz)^*S(Rz)-d\sum|z|^2
\]

before source labels are forgotten.  Prove compatibility with the partial
Frobenius used by the #760 relative-first Adams extractor.

This is the highest-priority universal-object theorem after the live
injectivity audit.  It is stronger than adding the diagonal term by hand: the
term must arise functorially from the literal relative diagonal.

### T2. `OCCSPEC`: live occupancy classification

If cell multiplicities are recorded in a diagonal matrix `M`, classify the
zero and sign loci of

\[
 M^{1/2}SM^{1/2}-dI
\]

on the aggregated quotient, together with the fixed `-d` source-difference
space.  Then determine which multiplicity patterns the native owner/cofactor
constraints actually permit.

The exact rectangle null family `q=p(n-1)+1`, including the transposed
orientation, shows that full-cell invertibility is not the right conjecture.

### T3. `SIGNEDRECOMB`: cancellation before norms

Carry the complete coefficient ledger through label forgetting and conductor
recombination while preserving the two-channel statistic.  Prove either a
noncancellation theorem or an exact further cancellation identity.  Both
outcomes are progress.

### T4. `RELTRACE`: uniform signed trace control

Only after `DIAGREL` exists, prove a conductor/Betti or operator-norm bound for
the relative trace.  A positive-norm bound that discards the signed source is
not a substitute.

### T5. `PRINCIPAL_BINDING`: member selection

Give an explicit positive domination, affordable amplifier, exact inversion,
or rigidity theorem that sends the family-level result to the principal
consumer without a fatal family-size tax.

The permutation firewall rules out recovery from a purely label-erasing
interface, not from the labeled signed source.  In the already available
`P=A-K=C-S` architecture, proving either requisite pair of signed global
bounds already extracts `P`; no third algebraic amplifier is required.
For a positive-average route, any improvement over the sharp first-mean
factor `N` must use stronger moments or additional structure.

### T6. `ARCHRIGID`: archimedean uniqueness or no-go

Classify the smallest determinant models satisfying gamma, duality, parity,
and tensor constraints.  Either obtain a canonical object or prove that
finite rank cannot support the package.

### T7. `CROSSWORLD`: one schema, two worlds

Require a promoted structure to recover one function-field or graph identity
used for calibration and predict a second identity in a held-out world.
Without this, “unification” remains analogy.

## 7. Earlier high-priority leftovers

The new programmes do not erase the strongest unfinished work from the prior
lineage.

| earlier frontier | present decision | reason |
|---|---|---|
| source-faithful function-field relative sheaf and principal extraction | **absorbed as priority 1 of #763** | first classify live injectivity; a universal carrier must retain the two-channel diagonal datum |
| full primitive divisor wavelet / `COREWAVE` | **continue in parallel, separately source-locked** | it is the strongest exact one-variable reduction on Architecture A, but progress must use signed Möbius cancellation rather than another positive-norm relaxation |
| complete assembled beta source | **retain after occupancy audit** | it may prove live injectivity or expose the duplicate cells that force carrier enrichment |
| literal function-field mirror | **retain as the first `CROSSWORLD` held-out** | useful only when the same object and operations transfer literally, not by analogy |
| Xi/explicit-formula descent | **defer one dependency level** | a descent claim is premature before the finite and archimedean carriers are both source-faithful |
| bounded quartic moonshot | **keep as an independent low-cost scout** | it should not displace `DIAGREL`, but an exact multi-observable or no-go result could justify its own later branch |

This ordering is deliberate.  The central lesson of the earlier work is that
the next gain must exploit source cancellation rather than optimize the
container in which absolute values are taken.

## 8. Eight-hour continuation design

This is the recommended next concentrated pass after the current wave-2
packets are reviewed.

| time | work product | hard stop |
|---|---|---|
| 0:00--1:00 | extract the actual live occupancy/multiplicity map from the complete source labels | stop if any source coordinate has been silently collapsed |
| 1:00--2:15 | prove `OCCSPEC` for the first structured multiplicity families and isolate singularity equations | no broad enumeration; retain counterexamples |
| 2:15--4:00 | design and test the literal diagonal triangle/two-channel `DIAGREL` adapter | reject independent conductors; call residue-only invalid only after noninjectivity is proved |
| 4:00--5:00 | compose the adapter with partial Adams extraction and audit commuting Frobenius requirements | do not claim a sheaf if only finite matrices exist |
| 5:00--6:00 | push the full signed coefficient ledger through conductor recombination | take no absolute value before the source-cancellation question is answered |
| 6:00--7:00 | run the `GL(1)` archimedean compatibility census as an independent lane | determinant matching alone does not pass |
| 7:00--8:00 | test a proposed labeled binding mechanism against the exact family-binding counterfeit pair and quantify its cost | a symmetric bound is not principal recovery; no zero plots or novelty claims |

## 9. Ranked continuation queue

1. **The actual live occupancy map plus `DIAGREL`.**  The first decides
   whether residue forgetting occurs natively; the second supplies a
   source-faithful adapter uniformly over arbitrary occupancies and continues
   the most important #760 leftover.
2. **Signed conductor recombination.**  Source cancellation, not a larger
   positive container, is the remaining leverage.
3. **`RELTRACE` and `PRINCIPAL_BINDING`.**  These are the true RH-facing
   analytic and family-to-member gates, but they should not be attacked on an
   invalid carrier.
4. **Archimedean compatibility rigidity.**  Keep this independent so a
   finite-place failure does not consume the entire programme.
5. **Source-sensitive family binding after the counterfeit.**  The exact
   permutation pair and sharp first-mean tax now supply the baseline
   firewall.  Proceed only with a binding axiom or stronger estimate that
   explicitly escapes it, rather than producing more relabelings.
6. **Dynamical/graph held-out transfer.**  Promote only if one schema predicts
   an identity not used in construction.
7. **Scaling-site, categorical, or new-language moonshots.**  Open a separate
   branch only after an honest object and a nontrivial operation are defined.

## 10. Branch and promotion policy

Keep the shared-fibre, occupancy, diagonal, signed recombination, and
principal-binding work in the existing #763 branch: they are one dependency
chain.  A separate archimedean or dynamical branch becomes justified only
when it produces an independent exact theorem or reusable counterfeit suite.
Opening a new programme merely to hold speculation would fragment review.

Promote a lane when it produces at least one of:

- an honest object explaining two distinct phenomena;
- a source-faithful trace or determinant theorem;
- a rigidity/no-go theorem closing a broad ontology;
- a held-out cross-world prediction;
- a family individualization mechanism with quantified cost.

Pause a lane when it only renames existing theory, fits a target quadratic
form, repeats a scalar function in extra coordinates, or reaches the same
open inequality with no new cancellation mechanism.

## 11. Scientific firewall

The current exact mathematics is finite fixed-fibre algebra, elementary
finite-family recovery/mean-tax theorems, and authenticated source identities.
It does not construct `ONEPLACEWEIL`, prove `RELTRACE`,
bind the principal member, transfer function-field purity to number fields,
or prove a critical-line theorem.  The literature map is a boundary audit,
not a priority claim.  Every proposed object above remains a proposal until
its carrier, operations, trace law, and held-out test are exact.

RH and GRH remain open.
