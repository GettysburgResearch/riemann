# Generalized L-objects wave-2 research map

Status: **exploration and continuation map; not an additional theorem**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Exact theorem packets: the six notes linked from [README.md](README.md)

## What wave 2 closed

| Axis | Exact chamber now covered | First surviving boundary |
|---|---|---|
| trace geometry | determinant-one rank-two scalar chambers; honest symmetric parents in arbitrary finite rank | scalar branch classification with varying determinant and higher-rank dense torus orbits |
| orbit type | irrational tempered rotations and every reduced rational rotation | nonperiodic higher-dimensional torus orbits |
| scalar transform | positive, absolute, and fixed real-axis complex powers | rational functions, coupled coefficients, and termwise branch data |
| zeros and branches | rational-orbit zero class, arbitrary \(0^0=z\), every fixed negative-axis logarithm branch | nonzero exponents with \(\operatorname{Re}\lambda\leq0\) |
| local recurrence | exact rationality, integer-chamber denominators, rational-orbit collision sums, and the sharp rational-angle uniform-degree classification | quantitative noninteger degree growth and exact finite-denominator cancellation strata |
| parent comparison | integer powers as matrix coefficients or weighted resolvent traces of genuine \(\operatorname{Sym}^k\) state spaces | coherent noninteger infinite-rank or categorical parent |
| determinant moduli | the filtered rank-\(n\) character count drops from \(\binom{n+d}{n}\) to \(\binom{n+d}{n}-\binom{d}{n}\) on the determinant-one torus | several independent monomial relations and scalar cancellation strata |

The rotation and parent packets add complementary information.  Rational
rotations show that pointwise local rationality is cheap: every fixed-branch
sequence is periodic, but its period can grow with the angle denominator.  Irrational
rotations restore rigidity: a fixed-branch complex power has a finite
recurrence exactly at nonnegative integers in the proved exponent domain.
The sampled-mode persistence theorem now proves that rational reduced degrees
are uniformly bounded only in the corresponding polynomial chambers.
The symmetric-parent packet then identifies the honest finite-dimensional
object at integer exponents, proves a finite-parent obstruction in the
positive hyperbolic chamber, and shows that determinant-one normalization
compresses an entire exponent polytope rather than merely changing one
recurrence coefficient.

## Held-out set

Any continuation should state which of these held-outs it tests rather than
retuning only inside the present rank-two model:

1. scalar power chambers with determinant \(\delta\neq1\), with the
   square-root and power branch fixed;
2. higher-rank semisimple local parameters and dense torus orbits (the parent
   weight count is now exact, the scalar rigidity theorem is not);
3. repeated eigenvalues, nonsemisimple Jordan blocks, and ramified factors;
4. GL(1), graph/dynamical, and function-field local recurrences;
5. a genuinely non-scalar determinant, transfer-operator, or categorical
   parent, not a coordinatewise copy of the scalar series;
6. twist, duality, tensor, and contragredient compatibility; and
7. nonzero \(\lambda\) with \(\operatorname{Re}\lambda\leq0\).

## L0--L9 state after wave 2

| Level | What is exact | What remains open |
|---|---|---|
| L0 | fixed branch and zero conventions are explicit; integer powers are branch-independent | unrestricted termwise branches and the nonpositive-real-part boundary |
| L1 | absolute powers and integer powers preserve scalar multiplicativity | a generic fixed-branch signed power does not; classify exceptional sign phases in broader coefficient fields |
| L2 | a formal Euler product exists only when L1 is supplied by the input | no new global Euler product is constructed |
| L3 | four determinant-one rank-two scalar chambers are classified; rational-angle degree is uniformly bounded exactly in the polynomial exponent chambers; all integer shadows have finite symmetric parents; the rank-\(n\) determinant-one character quotient is exact | quantitative rational-angle degree growth; higher-rank dense-orbit scalar classification; cancellation strata |
| L4 | integer state-space weights, the determinant relation, and its character-lattice quotient are explicit | duality, ramified-prime coherence, and compatibility across a global family |
| L5 | nothing new | canonical conductor, gamma factors, and root number |
| L6 | nothing new | analytic continuation and functional equation |
| L7 | nothing new | twists, tensors, induction, and contragredients |
| L8 | a local finite-dimensional resolvent parent exists at integers | automorphic, motivic, spectral, dynamical, or categorical realization |
| L9 | nothing new | principled explicit formula, positivity, or zero theory |

## Ranked proof-sized queue

1. **Quantitative rational-angle spectra.**  Uniform-degree rigidity is now
   proved: fixed nonpolynomial exponents have unbounded sampled Fourier
   support.  Determine a rate in \(b\), classify exceptional vanishing modes,
   and decide whether fixed real exponents have cofinally full or
   positive-density support.  Do not infer a rate from the qualitative
   Riemann-sum argument.

2. **Several-relation weight-polytopes.**  Generalize the proved
   determinant-one count by quotienting the exponent simplex by a saturated
   lattice of monomial relations.  Determine the exact character count,
   asymptotic degree, and special scalar-cancellation strata.  This is a
   finite moduli theorem target, not a new global `L`-function.

3. **Scalar determinant-parameter release.**  For
   \(u_{r+2}=x u_{r+1}-\delta u_r\), isolate the exact hypotheses under which
   normalization by \(\sqrt\delta\) and a rescaling of \(T\) transports the
   four classifications.  Track every square-root and complex-power branch.
   The parent-spectrum release is proved; this remaining target concerns the
   scalar branch classifications.

4. **Higher-rank dense-torus gate.**  Prove that an eventual recurrence for
   samples of a continuous function along a dense torus orbit forces finite
   character support.  Apply it to scalar transforms with singular
   hyperplanes, then compare the surviving integer locus with Schur-functor
   parents.

5. **The \(\operatorname{Re}\lambda\leq0\) irrational chamber.**  Replace
   the continuity argument with a theorem controlling recurrence sequences
   sampled arbitrarily close to a pole or logarithmic oscillation.  Do not
   infer the answer from the positive-real-part proof.

6. **Low-rank L4 compatibility.**  Impose determinant, duality, and one twist
   law on the exact local spectra and classify the resulting small moduli
   space.  This is the first target that can distinguish a convenient finite
   state-space realization from representation-theoretic coherence.

7. **Infinite-rank parent scout.**  If a noninteger transform is represented
   by an operator or category, require an exact scalar recovery map, a
   natural operation law, and a boundedness or determinant contract.  A bare
   diagonal operator containing the scalar coefficients is a counterfeit,
   not a promotion.

## Programme breadth beyond local powers

The six exact packets are probes, not the whole programme.  The next work
should keep four contrasting axes alive.

| axis | current exact foothold | next bounded target | rejection test |
|---|---|---|---|
| coefficient, zero, and branch transforms | four rank-two scalar chambers plus the sharp rational-angle uniform-degree gate | quantitative support growth and scalar varying-determinant classification | a finite period at each parameter is not uniform L3 |
| local parameters and representation parents | `Sym^k` matrix-coefficient identity; higher-rank determinant quotient | quotient exponent polytopes by several monomial relations; impose one duality and twist law | a scalar resolvent fit is not a determinant `L`-factor |
| multivariable and higher-dimensional parents | none claimed by these packets | compare one Brown-type completed object and one Weyl-group multiple Dirichlet series under a common specialization/coupling schema | a Cartesian or slice-wise repetition with no mixed coefficient or larger symmetry is rejected |
| prime, frequency, and dynamical worlds | none claimed by these packets | construct exact lower-level counterfeits using a Beurling or transfer-operator calibration and record the first survival failure | chosen primes, orbit lengths, or spectra fitted to desired zeros are circular |

The parent criterion is deliberately strict.  Added variables or dimensions
must introduce an exact coupling, symmetry, operation, or moduli law that is
visible before scalar specialization.

## Primary-literature boundary

The following sources delimit established territory; they are not novelty
evidence for this repository.

| territory | primary source | boundary for #764 |
|---|---|---|
| powers of second-order recurrences | Pantelimon Stănică, [*Generating Functions, Weighted and Non-Weighted Sums for Powers of Second-Order Recurrence Sequences*](https://arxiv.org/abs/math/0010149) | integer-power rationality is classical; the packet contribution is a source-locked parent/shadow and deformation boundary, not priority for the formulas |
| Hadamard-ring equations | Ferretti--Zannier, [*Equations in the Hadamard ring of rational functions*](https://arxiv.org/abs/math/0701772) | recurrence roots and Hadamard powers have an established arithmetic theory; broad novelty needs specialist comparison |
| complex-rank categories | Pavel Etingof, [*Representation theory in complex rank, I*](https://arxiv.org/abs/1401.6321) | the finite-state no-go does not exclude categorical interpolation |
| lambda structures | James Borger, [*Lambda-rings and the field with one element*](https://arxiv.org/abs/0906.3146) | Adams/lambda operations are established structural language; relabelling a coefficient transform is not a new operation |
| several-variable functional equations | Chinta--Gunnells, [*Constructing Weyl group multiple Dirichlet series*](https://arxiv.org/abs/0803.0691) | larger reflection groups with genuine coupled local data already exist |
| multivariable completed zeta | Francis Brown, [*A multi-variable version of the completed Riemann zeta function and other L-functions*](https://arxiv.org/abs/1904.00190) | functional equations, shuffle identities, singular hyperplanes, and recursive residues provide a nontrivial parent calibration |
| axiomatic global data | Andrew Booker, [*L-functions as distributions*](https://arxiv.org/abs/1308.3067) | Euler, functional-equation, and explicit-formula packages have a broad existing axiomatic setting |
| generalized primes | Hilberdink--Lapidus, [*Beurling Zeta Functions, Generalised Primes, and Fractal Membranes*](https://arxiv.org/abs/math/0410270) | prime-system deformation and functional equations are established research areas, not an empty novelty space |
| dynamical determinants | Giulietti--Liverani--Pollicott, [*Anosov Flows and Dynamical Zeta Functions*](https://arxiv.org/abs/1203.0904) | a genuine operator parent acts on independently defined spaces and controls continuation; a fitted finite matrix does not qualify |

The plausible unexplored territory lies in exact interfaces between these
packages—for example, how relation-lattice moduli constrain scalar shadows
under twist and duality—not in renaming one established class.

## Machine-readable corpus and held-outs

The exact corpus is carried by the six canonical JSON fixtures:

```text
nonintegral_local_power_rationality.json
irrational_rotation_absolute_power_rationality.json
rational_rotation_branch_census.json
irrational_rotation_principal_complex_power_rationality.json
transfer_matrix_symmetric_parent.json
rational_rotation_uniform_degree_gate.json
```

Each fixture records claims, arithmetic class, scope firewalls, source
authentication, and an L0--L9 or equivalent survival ledger.  The combined
held-out protocol is:

1. train no formula on both the generic `(2,3)` and determinant-one
   `(2,1/2)` parent controls;
2. retain `(2,4)` as a dependent-root counterfeit;
3. hold out rational rotations with new denominators, including zero and
   branch conventions;
4. hold out rank `3` through `5` determinant quotients from any rank-two
   derivation;
5. require the next promoted transform to pass one `GL(1)`, graph/dynamical,
   or function-field example without retuning; and
6. distinguish parent character count, scalar-observable support, and reduced
   denominator after cancellation.

The bounded replays validate exact identities.  They do not prove analytic
continuation, a functional equation, automorphy, or a zero theorem.

## Eight-hour continuation design

| time | work product | scientific stop |
|---|---|---|
| 0:00--1:15 | literature audit and exact formulation of the rational-angle Fourier-support target — **completed** | do not infer unbounded support from finite denominators |
| 1:15--2:30 | prove or refute the first uniform Fourier-mode lower bound for a fixed noninteger exponent — **completed sharply at the bounded/unbounded level** | a quantitative growth rate remains open |
| 2:30--3:45 | classify the scalar varying-determinant normalization with every square-root/power branch explicit | parent weight counts alone do not settle scalar branches |
| 3:45--5:00 | prove the dense-torus recurrence lemma in rank `n` and test singular-hyperplane transforms | no smoothness claim across an unhandled branch divisor |
| 5:00--6:00 | impose determinant, contragredient, and one twist law on the smallest local moduli | do not attach ramified or gamma data ad hoc |
| 6:00--7:00 | build the multivariable parent--shadow comparison schema on two established parents and one separable counterfeit | extra variables must carry mixed structure |
| 7:00--8:00 | run one generalized-prime or dynamical counterfeit comparison, update the atlas, and decide promotion/pause | no zero plot is a theorem |

## Coordination with the Riemann Structures and earlier lineages

The symmetric-parent theorem supplies #763 with an example of an honest
upstairs object and a warning: a matrix coefficient of a resolvent is not the
determinant inverse.  Conversely, #763's source-forgetting theorem supplies
#764 with a counterfeit test: scalar aggregation may erase a load-bearing
diagonal channel even when local rationality survives.

The highest-priority earlier work—source-faithful relative extraction,
signed divisor-wavelet cancellation, and principal binding—continues in the
#763/#760 dependency chain.  It should not be displaced by local-power
cataloguing.  A new #764 branch is justified for a genuinely independent
multivariable, relation-lattice, or infinite-parent theorem; minor scalar
extensions belong on the current branch.

## Promotion and stop rules

Promote the line only when a continuation proves a uniform degree bound or
obstruction, closes a determinant/higher-rank component, or constructs a
non-scalar parent with an independent operation or coherence law.  Pause a
lane that yields only more periodic examples, numerical spectra, an ad hoc
gamma factor, or a larger coordinate space carrying no new coupling.

No item in this queue asserts a global Euler product, automorphy, a functional
equation, or an RH/GRH consequence.
