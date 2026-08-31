# Independent review of Segre bridge 4a317ea5

Verdict: PASS for the stated local algebra, exact finite maps, and rank-three
purity chamber. This is a nonauthor review of the immutable scientific source
`4a317ea5c9d7aa016fba58a1d74746e437329ec7`, whose authoring base is
`7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e`. No source file was edited.

The verdict does not certify external novelty, an analytic completion,
automorphy, a positive global source, or RH/GRH. It also does not turn the
finite cubic map replay into a proof about every syzygy degree.

## 1. What was reviewed

The five frozen bridge files were read and their literal source and artifact
bindings replayed. The parent Segre sorting, quadratic-dual Lie convention,
and formal Koszul product were checked as accepted dependencies. The new
theorem arguments were reconstructed independently, including every sign in
SB9--SB14, finite Hankel rank, and the reduction-versus-specialization issue.

Primary literature checks confirmed the distinction between canonical Tor
modules and chosen free resolutions, the additive equivariant Euler identity,
and the classical cubic character in
[Snowden, sections 1.1, 3.1 and 4.7](https://websites.umich.edu/~asnowden/papers/segre-111810.pdf).
The associative quadratic dual, odd Lie presentation and infinite product
are classical constructions described in
[Gorbounov--Schechtman, section 3.4](https://sigma-journal.com/2009/034/sigma09-034.pdf).
Those primary pages are literature checks, not cryptographically authenticated
inputs to a numerical proof. The packet correctly does not claim these
classical mechanisms as discoveries.

## 2. Mathematical checks

### Three genuinely different polynomials

The ambient Euler numerator uses Tor over S=Sym(V tensor-power m), not Tor
over R. Its denominator is det(1-T A tensor-power m). Symmetrization in
characteristic zero gives the equivariant splitting needed for SB5. Thus
the extra determinant factor in the corrected dictionary is necessary.

For distinct eigenvalues, the partial-fraction coefficients in SB6 are all
nonzero. If the degree-m monomials are distinct, so are the poles in SB7,
and the universal denominator is genuinely minimal. On collisions one
must sum the residues before deciding whether a pole remains. Coincident
input eigenvalues require polynomial continuation, not substitution into
the singular partial-fraction coefficients.

The backward continuation has first nonzero negative term at -n. Expanding
the rational function at infinity therefore gives deficit n and top
coefficient

    (-1)^(N0+1+m(n-1)) det(A)^(mN0/n-m).

This coefficient remains nonzero on GL(V), so the claimed universal degree
does not merely hold generically. Cancelling a greatest common divisor
lowers numerator and denominator degrees equally. Reciprocity compares A
with A inverse; a fixed-matrix palindromy needs the extra self-duality used
in the slice.

The N0 by N0 Hankel block has the infinite Hankel rank: the universal
recurrence spans every later row and column. Properness and the invertible
last recurrence coefficient identify this with the reduced denominator
degree, including confluent cases. No generic distinct-root assumption
is silently used in SB15.

For pure input, all factors added or removed in the dictionary have inverse
roots on the input purity circle. Hence the off-purity divisors agree with
multiplicity. This retained conclusion is stronger than saying the proposed
superdeterminant identity was wrong, but it does not identify the polynomials.

### Multiplicative interpretation is sharply delimited

At the identity every natural representation action is the identity, so
a finite product of graded determinants or their inverses has only roots
of unity as its zeros and poles. The displayed noncyclotomic numerators
contradict precisely that interpretation. Virtual representations and fixed
parity signs do not evade the argument. Arbitrary added operators or
companion matrices are explicitly outside the claim.

### Actual maps and character

The source producer constructs the multiplication fibres before ranks are
computed. The 162 quadric differences are an actual basis of I2, and their
4374 generator multiples map into the 3654 commutative cubic monomials.
The quadratic-dual columns are actual ordered-pair fibre sums; nested odd
brackets have the stated signs. Their quotient and bar-incidence computations
are different finite rank algorithms. Neither sets a matrix rank from a
Hilbert numerator.

The cubic character formula agrees with the homogeneous cubic part of
Snowden's f3. The six ABC placements, two BBB copies, three BBC placements
and three BCC placements have total dimension 1720. The independently
computed cyclic character is (568,576,576), hence trace -8, while the
observable recurrence collapses to order three. This is an exact witness
against equating a reduced numerator spectrum with the actual syzygy action.

### Purity chamber and cancellation strata

Direct expansion gives B=2x^2+5x+2 and C=x^3+6x^2+7x+2. The reciprocal
quartic reduces purity to both roots of z^2+Bz+C-2 lying in [-2,2].
The endpoint factorizations exclude x>0; on [-2,0] the vertex is interior
and both endpoint values are nonnegative. The discriminant criterion is
therefore sufficient as well as necessary. Positive Bernstein coefficients
give one discriminant zero in [-2,-1], and the sum-of-squares identity
handles [-1,0]. Independent exact Sturm counts confirm both intervals and
the rational bracket (-5/3,-13/8).

Cancelling D7 factors cannot remove an off-unit-circle root for unitary
input. The x=-3 and x=-8 nonunitary cases were also reconstructed from
the grouped residue sums; they demonstrate cancellation without input
eigenvalue coincidence and retain deficit three.

## 3. Independent primitive replay beyond the author's tests

The companion `segre_bridge_independent_review.py` imports no author code.
Its result is resident in `segre_bridge_independent_review.json`.

First, it builds a graph on all 3654 commutative cubic monomials. An edge
swaps one coordinate between two of the three tensor generators. Such an
edge is literally a generator times a Segre quadric. There are 6561 distinct
edges and exactly 1000 connected components, one in every product-torus
weight fibre. Since every column preserves weight, connectivity supplies
both a lower and an upper bound for the cubic rank: 3654-1000=2654.
Independent pair-fibre counting gives domain dimension 4374, hence 1720
syzygies. This reproduces every one of the 460 nonzero weight multiplicities
and the cyclic character, not just the total dimension.

Second, three nondiagonal rank-three matrices are used: a unipotent Jordan
matrix, a companion matrix with determinant six, and a real order-four
rotation block with an additional fixed vector. The code constructs the
literal ten-dimensional Sym^3 matrix and its characteristic polynomial,
and computes 21 direct symmetric-power traces per matrix. It does not use
input eigenvalues to construct these recurrences. The reduced denominator
orders are respectively 7,10,3; their Hankel ranks agree. The universal top
coefficient and deficit-three claims pass in all three cases.

Third, exact symbolic Sturm calculations independently give discriminant
root counts 1 on (-2,-1), 0 on (-1,0), and 1 in the declared smaller bracket.
No rounded spectral roots are used.

The extra controls use integer/rational arithmetic and SymPy 1.14.0. They
are finite checks, not a formal proof of the analytic or all-parameter
statements. The written algebraic proofs above remain load-bearing.

## 4. Replay and release boundaries

On a clean detached checkout of the exact scientific SHA:

    python -B -m unittest tests.test_segre_recurrence_syzygy_bridge tests.test_segre_koszul_lie_parent
    python -B -O -m unittest tests.test_segre_recurrence_syzygy_bridge tests.test_segre_koszul_lie_parent

Both ran 58 tests and passed (5.067 and 4.925 seconds in this review).
The primitive producer, typed fixture replay, source locks, normal/optimized
outputs, formatting and complete base-to-head whitespace were also checked.
The source's strict duplicate-key, nonfinite-value, byte/depth and exact
arithmetic guards are part of the tested finite interface.

The independent replay script's fixed panel is not advertised as a generic
hostile-input API. Its source SHA and five frozen file hashes are recorded
in its output, and its own source hash is included as well.

No correction to the scientific source was required. Later extensions must
receive new identities and their own review. In particular, an open
two-parameter unitary chamber or higher coefficient powers are not included
in this verdict merely because they may be plausible consequences.
