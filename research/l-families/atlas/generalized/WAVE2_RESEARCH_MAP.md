# Generalized local-power wave-2 research map

Status: **exploration and continuation map; not an additional theorem**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Exact theorem packets: the four notes linked from [README.md](README.md)

## What wave 2 closed

| Axis | Exact chamber now covered | First surviving boundary |
|---|---|---|
| trace geometry | determinant-one rank-two, hyperbolic positive and tempered rotation chambers | determinant parameter and higher rank |
| orbit type | irrational tempered rotations and every reduced rational rotation | nonperiodic higher-dimensional torus orbits |
| scalar transform | positive, absolute, and fixed real-axis complex powers | rational functions, coupled coefficients, and termwise branch data |
| zeros and branches | rational-orbit zero class, arbitrary \(0^0=z\), every fixed negative-axis logarithm branch | nonzero exponents with \(\operatorname{Re}\lambda\leq0\) |
| local recurrence | exact rationality, reduced denominators in the classified integer chambers, and rational-orbit collision sums | a uniform degree theorem over varying local angles |
| parent comparison | integer powers as weighted resolvent traces of genuine \(\operatorname{Sym}^k\) state spaces | coherent noninteger infinite-rank or categorical parent |

The two wave-2 packets add complementary information.  Rational rotations
show that pointwise local rationality is cheap: every fixed-branch sequence is
periodic, but its period can grow with the angle denominator.  Irrational
rotations restore rigidity: a fixed-branch complex power has a finite
recurrence exactly at nonnegative integers in the proved exponent domain.

## Held-out set

Any continuation should state which of these held-outs it tests rather than
retuning only inside the present rank-two model:

1. determinant \(\delta\neq1\), with the square-root and power branch fixed;
2. higher-rank semisimple local parameters and dense torus orbits;
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
| L3 | four determinant-one rank-two chambers are classified locally | uniform degree over varying rational denominators; determinant and higher-rank release |
| L4 | the integer state-space weights and determinant are explicit | weight, determinant, duality, and ramified-prime coherence across a family |
| L5 | nothing new | canonical conductor, gamma factors, and root number |
| L6 | nothing new | analytic continuation and functional equation |
| L7 | nothing new | twists, tensors, induction, and contragredients |
| L8 | a local finite-dimensional resolvent parent exists at integers | automorphic, motivic, spectral, dynamical, or categorical realization |
| L9 | nothing new | principled explicit formula, positivity, or zero theory |

## Ranked proof-sized queue

1. **Uniform-degree rational-angle rigidity.**  For a fixed noninteger
   exponent, prove that the number of nonzero discrete Fourier modes of
   \(|\sin(na\pi/b)|^\lambda\), or of its fixed-branch analogue, is
   unbounded with \(b\).  The strongest form would classify every vanishing
   mode.  This would turn pointwise periodic rationality into an exact
   uniform-L3 obstruction.  First audit the literature on power-sine windows,
   chordal-distance kernels, and conditionally positive definite functions.

2. **Determinant-parameter release.**  For
   \(u_{r+2}=x u_{r+1}-\delta u_r\), isolate the exact hypotheses under which
   normalization by \(\sqrt\delta\) and a rescaling of \(T\) transports the
   four classifications.  Track every square-root and complex-power branch.
   This target is being developed independently and should be cherry-picked
   rather than duplicated.

3. **Higher-rank dense-torus gate.**  Prove that an eventual recurrence for
   samples of a continuous function along a dense torus orbit forces finite
   character support.  Apply it to scalar transforms with singular
   hyperplanes, then compare the surviving integer locus with Schur-functor
   parents.

4. **The \(\operatorname{Re}\lambda\leq0\) irrational chamber.**  Replace
   the continuity argument with a theorem controlling recurrence sequences
   sampled arbitrarily close to a pole or logarithmic oscillation.  Do not
   infer the answer from the positive-real-part proof.

5. **Low-rank L4 compatibility.**  Impose determinant, duality, and one twist
   law on the exact local spectra and classify the resulting small moduli
   space.  This is the first target that can distinguish a convenient finite
   state-space realization from representation-theoretic coherence.

6. **Infinite-rank parent scout.**  If a noninteger transform is represented
   by an operator or category, require an exact scalar recovery map, a
   natural operation law, and a boundedness or determinant contract.  A bare
   diagonal operator containing the scalar coefficients is a counterfeit,
   not a promotion.

## Promotion and stop rules

Promote the line only when a continuation proves a uniform degree bound or
obstruction, closes a determinant/higher-rank component, or constructs a
non-scalar parent with an independent operation or coherence law.  Pause a
lane that yields only more periodic examples, numerical spectra, an ad hoc
gamma factor, or a larger coordinate space carrying no new coupling.

No item in this queue asserts a global Euler product, automorphy, a functional
equation, or an RH/GRH consequence.
