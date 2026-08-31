# Independent review of higher-power Segre chambers

Verdict: **PASS** for the exact algebra, exhaustive m=4,5,6 slice
classification, and separately stated open cubic SU(3)-torus chamber.
Scientific identity: `1c3c6880ce4db8b15a5e26c3c27e822f3f46365a`.
Authoring base: `4a317ea5c9d7aa016fba58a1d74746e437329ec7`.
Immediate parent: `e21e44d84077b7703c6795a81c91fc305b3fe344`, the actual
pre-computation power-six preregistration.

This is a non-author review. The author supplied the release identity and
replay commands only; the mathematical checks and independent computations
below were performed separately. No scientific source was edited.
No acceptance of novelty, an Euler product, automorphy, continuation,
an all-power chamber pattern, or RH/GRH is included.

## 1. Source and primary-literature checks

The complete new proof, producer, tests and manifest were read. Every
structured fixture field group was inspected, authenticated and replayed.
The complete frozen parent proof was read, with particular attention to
SB3--SB5, SB9--SB14, SB20--SB25 and the universal/reduced distinction.
The historical preregistration and separate parent review were read as
source records, not as substitutes for checking the new statements.

Exactly five files differ from the authoring base. The new fixture LF
SHA256 is

    57d266da50fba5dd253302a68f97541e88614ec379375f978c9411197d7719c0

and its canonical payload SHA256 is

    b6730f2b44c607cac79b21331b6ae2e6bb2377fbab1f1ceaa49de3eebd545c23.

All seven frozen parent bindings were checked by Git blob and LF SHA256;
the five current scientific parent copies also match. The four new
artifact seals and complete canonical payload were independently checked.
Source whitespace/control-byte checks passed.

Using the PDF skill, I personally inspected the rendered complete pages
2,4,5 of [Carnevale--Voll, *Orbit Dirichlet Series and Multiset
Permutations*](https://angelacarnevale.github.io/papers/orbit.pdf).
Proposition1.2, equations2.1--2.3 and Lemma2.5 support the classical
Hadamard/multiset dictionary and the maj/comaj conversion. Section2.2's
bivariate unitary-factor definition is different from this packet's
pointwise unit-circle condition. The packet states this distinction
correctly and does not import the paper's global theorems.

The retrieved PDF SHA256 was
`6c0b76d9618ed2c94cb13947efbea79cc6e7aa9b052bfeb6f24833101cfd36e6`.
It is a literature-inspection record, not a frozen arithmetic dependency.

## 2. All-power algebra and full character

The coefficient of the exponential weight t^(jr) in h_r^m follows by
choosing a factors from (1-t^(r+1))^m and b from (1-t^(r+2))^m.
Then j=a+b-m and the remaining power is t^(j+m+b), giving HP4 with
its stated sign. Its sum polynomial has positive integer coefficients
and is not identically zero. Avoiding its finitely many roots, the input
singularities, and the finitely many weight collisions proves generic
minimality of D_m. It does not prove minimality at every nontorsion t.

The first nonzero backward term is h_-3=1. Thus F_m has Laurent leading
term -T^-3 at infinity. D_m has degree2m+1 and leading coefficient -1,
so P_m has exact degree2m-2 and leading coefficient1. The inherited
inverse-matrix reciprocity becomes fixed-slice reciprocity only because
A is self-dual and determinant one. Coefficientwise polynomial
continuation includes t=1,-1 without substituting into singular partial
fractions. Folding the reciprocal Laurent polynomial gives the monic
M_m of degree m-1.

The full word proof is a literal bijection. Stable sorting the weak pairs
orders letters increasingly at ties, so a word descent forces a strict
increase of the sorted values. Removing the preceding descent count
leaves a weak sequence; each descent at j contributes 2m-j to its sum.
The nonnegative gap variables give all denominator weights, including
the zero gap weight. Substitution s=Tt^-m gives HP6. Equal multiplicities
are essential to the reverse-and-complement maj/comaj bijection.

The intermediate P_m, universal numerator N_univ and ambient syzygy Euler
polynomial remain distinct. D_sym/D_m is a genuine polynomial on the
slice because each weight t^j occurs. For unitary input the added and
cancelled factors are unitary, so the off-circle divisors agree; this
does not identify the polynomials or construct a natural finite syzygy
superdeterminant.

## 3. Exhaustive walls and multiplicities

For each monic M_m the root count inside (-2,2) is constant away from
the discriminant and both endpoint-value polynomials. The recorded
factorizations were reconstructed from independently obtained M_m.
Their high-degree residual discriminants have degrees14,32,62, with
3,10,22 real roots in (-2,2), respectively.

The independent exact counts give:

| power | full Laurent terms | words represented | wall factors | distinct walls | open cells | pure components |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 51 | 2520 | 7 | 9 | 10 | 3 |
| 5 | 109 | 113400 | 9 | 21 | 22 | 4 |
| 6 | 201 | 7484400 | 10 | 36 | 37 | 6 |

Every rational isolator is disjoint and has the stated one-root count;
the outer Sturm counts show that no factor root in the domain was
omitted. Every complementary cell is represented, not merely selected
membership probes. The component endpoint labels in HP9 agree with
the exact factor/root indices, including beta, gamma and the larger
quartic root e. Reduction removes only unit roots for unitary input.

The written wall argument is necessary and valid. A simple discriminant
zero has exactly one double root: a triple root or two double roots gives
Sylvester corank at least two and forces discriminant vanishing order
at least two. At a putatively pure ordinary wall, the double cluster's
real-analytic quadratic factor has a discriminant changing sign, while
the other roots remain simple and interior. One neighboring cell is
therefore pure. At an ordinary simple endpoint wall the simple root
crosses transversely, again with a pure inward neighbor.

All multiple/shared factors are covered by
x(x+1)(x-1)(x^2+x-1). The exact periodic source sequences settle the
exceptional points. In particular the negative root of x^2+x-1 is
pure and the positive root is not; this pair must not be confused with
gamma, the negative root of x^2-x-1. The x=+-2 controls are nonpure.
Closedness of the monic all-unit locus includes the adjacent component
endpoints and, with these wall arguments, excludes additional isolated
pure points. The classification is therefore complete, not just a list
of pure open intervals.

## 4. Preserved sixth-power failure

The exact preregistration really precedes construction of m=6. Its
three torsion predictions survive independent expansion. The five
membership predictions have outcomes pass,pass,pass,pass,FAIL: at
x=-1/4 the sixth power is not pure. The component prediction five is
false; the exact count is six.

The two independent rational witnesses are:

    x=-407/250: m5 impure, m6 pure;
    x=-1/4:     m5 pure, m6 impure.

Thus containment fails in both directions. The failed prediction is
visible in the prose and machine payload and was not retroactively
relabelled as a successful forecast.

## 5. Open two-parameter SU(3) statement

At x=-3/2, direct independent folding recovers z^2-z-3/8. Its two
distinct roots lie strictly in (-2,2), hence give four distinct unit
roots. M(-3/2)=27/8 separates the extra quadratic and M(2)=13/8
separates T=1; the quadratic's value at T=1 is7/2. Thus the universal
degree-seven numerator has seven distinct unit roots.

For general determinant-one unitary diagonal input, SB14 becomes
conjugate reciprocity with sign minus and degree seven. It does not
give real coefficients or fixed-A palindromy. The reciprocal-conjugate
map preserves sufficiently small annular sectors around the base roots.
Persistence of exactly one complex-counted root in each sector forces
it to be fixed by that map, hence unitary and simple. This proves a
genuine open two-real-parameter torus neighborhood, without an effective
radius and without extending to all powers.

The ten degree-three monomial characters remain distinct on the
determinant-one torus: equal restrictions would have exponent difference
a multiple of (1,1,1), whose zero total degree forces that multiple to
be zero. Their finitely many proper collision subtori cannot fill any
neighborhood. Away also from input collisions, the native partial
fractions have nonzero coefficients, proving generic reduced order ten
arbitrarily close to the base point. The statement does not assert
order ten at the specially self-dual base point itself.

The open impure neighborhood near the identity and the collision-only
boundary of simple all-unit points also follow by root continuity.
Neither gives an arithmetic/Frobenius interpretation or global completion.

## 6. Independent executable review and replay evidence

The companion `review_segre_higher_power_1c3c6880.py` imports no author
producer. It reads the exact scientific Git SHA, authenticates sources,
and constructs h_r directly by enumerating triples i+j+k=r and their
Laurent weight t^(i-k). Laurent convolution gives h_r^m and the product
over t^j, then reconstructs every coefficient and the folded M_m.
This is independent of both the author's x-recurrence and word-state DP.

Its Sturm route performs ordinary polynomial division over Python
Fraction, then clears denominators and divides only by positive content.
It does not call the author's pseudo-remainder code or SymPy's root-count
interface. It rebuilds all 26 factor chains, all 66 wall isolators, all 69
cell counts, all five held-out verdicts and both nonnesting witnesses.
Independent exceptional-factor identities, sixth-power torsion polynomials
and the cubic base polynomial are included. SymPy is still used for
exact symbolic discriminants and factorization identity expansion;
the review is not a formally verified algebra kernel.

Both normal and optimized runs of this independent replay pass. On the
exact scientific checkout the new and inherited suites ran **97 tests
per mode**, passing in 29.795 s and 20.146 s. The source producer's checks
and byte-for-byte LF emits passed in both modes. The fixture emit SHA
is the one recorded in Section1. Ruff, formatting and full authoring-base
whitespace checks pass.

Nine fresh resealed semantic/type/source attacks were rejected, including
omitted walls, altered cell verdicts, changed R6 coefficients, concealed
prediction failure, changed whole-character weight, claimed effective
radius, bool/int substitution, forged source hash and global overclaim.
Two were additionally sent through complete fresh check_fixture rebuilds,
without replacing the reconstruction: omitted wall and concealed failed
prediction both failed. No frozen file was modified by these attacks.

The executable is a fixed review panel, not a general hostile-input API.
The source appropriately bounds external degree/rank/data interfaces and
does not claim per-internal-operation SymPy bit accounting. Its backend
trust and finite scope remain explicit.

No correction to `1c3c6880ce4db8b15a5e26c3c27e822f3f46365a` is required.
This review adds only its report and independent replay script; it edits
no scientific or programme-front file and publishes nothing remotely.
