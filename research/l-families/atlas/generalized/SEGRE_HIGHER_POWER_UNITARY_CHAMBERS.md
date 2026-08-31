# Higher-power Segre unitary chambers and an open cubic torus chamber

Status: proposed exact algebra and exhaustive finite chamber certificate;
independent frozen review required. No global L-function or RH claim.
Base: 4a317ea5c9d7aa016fba58a1d74746e437329ec7.

## Held-out power-six record

This section is committed before computing the m=6 reciprocal numerator or
its discriminant/chamber table. Powers m=4 and m=5 have already been
constructed in an in-memory exact symbolic scout; those are discovery data,
not held-out predictions.

The general exponential expansion predicts denominator
D_13=product_(j=-6)^6(1-t^j T), generically reduced on the self-dual slice,
with reciprocal numerator degree ten. The reciprocal polynomial M_6(x,z)
has degree five in z. These statements will be proved for every positive m,
not inferred from this control.

Source-derived torsion predictions, before m=6 construction:

- At x=-1, M_6=(-2+z)^2(1+z)^3 and the reduced series is 1/(1-T^3).
- At x=0, M_6=z^2(z-2)(z+2)^2 and the reduced series is
  1/[(1-T)(1+T^2)].
- At x=1, the reduced numerator is 1+63T+T^2 and the denominator
  is (1-T^6)/(1+T). It is not pure.

A deliberately falsifiable extrapolation from the first tables is that
the m=6 purity set is contained in the m=5 purity set and has five
interval components. This is a test question, NOT a theorem.
Five preselected rational membership controls, using the m=5 verdicts
as the provisional m=6 predictions, are

| x | provisional m=6 pure verdict |
|---|---|
| -49/30 | false |
| -3/2 | true |
| -1/2 | true |
| -2/5 | false |
| -1/4 | true |

Every failed prediction must remain visible. No endpoint or rank will be
selected after the m=6 computation to make this record appear successful.

## Separately labeled structural cubic target

At x=-3/2 the cubic numerator from the frozen parent is
P=1-T+(13/8)T^2-T^3+T^4.
Its reciprocal z roots are (1+-sqrt(5/2))/2, both in (-2,2).
The degree-seven universal numerator is
P(1-T)(1+3T/2+T^2).

Prove all seven unit roots are distinct, then use determinant-one unitary
conjugate reciprocity and local uniqueness of roots to obtain an OPEN
two-parameter unitary-torus purity chamber. Every such neighborhood must
contain generic denominator-order-ten inputs. This must be distinguished
from fixed-A self-duality on the original one-parameter slice.

## 1. Frozen prediction outcome and contribution boundary

The preregistration above is preserved at
e21e44d84077b7703c6795a81c91fc305b3fe344. Its source-derived three
torsion predictions all pass. The five membership predictions pass except
x=-1/4: the sixth power is NOT pure there. The guessed containment in
power five is false in both directions. The guessed five components are
replaced by the exact six components proved below. These are recorded
failures, not revised predictions.

The contribution is an exact higher-power chamber classification on the
rank-three self-dual slice, plus a separately proved open two-parameter
unitary cubic chamber. The generating-function/combinatorial identity is
classical. In particular, [Carnevale--Voll, *Orbit Dirichlet Series and
Multiset Permutations*](https://angelacarnevale.github.io/papers/orbit.pdf),
Proposition 1.2 and equation (2.3), state the relevant MacMahon identity.
Their section 2.2 notion of a **bivariate unitary factor** F(s^a q^b) is
not our condition that, for a particular unitary input t, all roots of a
specialized numerator have modulus one. Their global orbit Dirichlet
series theorems are not imported here. No publication-priority or exhaustive
novelty claim is made.

The exact frozen parent is 4a317ea5c9d7aa016fba58a1d74746e437329ec7;
its independent review is acd91a621244872d49e0e4dfde76775879eadfc1.
Those source files are unchanged. This is a new proposed packet requiring
its own exact-SHA independent review.

## 2. The all-power slice and classical word character

Let m be a positive integer, t a nonzero complex number, x=t+t^-1 and
A=diag(t,1,t^-1). Write

    h_r=h_r(A),   F_m(T)=sum_(r>=0) h_r^m T^r.
    C_0(x)=2, C_1(x)=x, C_j=x C_(j-1)-C_(j-2).
    D_m(x,T)=(1-T) product_(j=1)^m (1-C_j(x)T+T^2).

Here D_m has degree 2m+1; the index m records the power, not its degree.
All series statements are formal rational identities.

### HP1. Exact denominator and reciprocal numerator for every m

There is a polynomial P_m in Z[x,T], of degree exactly 2m-2 in T,
constant and top coefficients one, such that

    F_m=P_m/D_m,                       (HP1)
    P_m(T)=T^(2m-2) P_m(T^-1),
    P_m(x,T)=T^(m-1) M_m(x,T+T^-1),    (HP2)

where M_m is monic of degree m-1 in its second variable and belongs to
Z[x,z]. For m=1, P_1=M_1=1. D_m is the **generic reduced denominator on
this slice**, not the reduced denominator at every specialization.

Proof. Outside t=1,-1, multiplication of the geometric series gives

    h_r=t^-r (1-t^(r+1))(1-t^(r+2))/[(1-t)(1-t^2)]
        =t^-r [r+2 choose 2]_t.        (HP3)

Expanding the mth power groups exponential weights t^j, -m<=j<=m.
The coefficient of (t^j)^r is

    (-1)^(j+m) t^(j+m) /[(1-t)^m(1-t^2)^m]
       * sum_b binom(m,j+m-b) binom(m,b) t^b,        (HP4)

with binomial coefficients zero outside 0..m. The final polynomial is
nonzero: all its nonzero coefficients are positive integers. Thus when
the 2m+1 weights are distinct and these finitely many polynomials do not
vanish, all poles occur and D_m is reduced. These conditions exclude only
a proper finite subset of C*. This proves generic minimality, not a
claim that all non-torsion inputs have full order.

The rank-three backward continuation from parent SB9--SB13 gives
h_-1=h_-2=0, h_-3=1, and F_m(T^-1)=-T^3 F_m(T) on this self-dual slice.
Therefore D_m F_m has degree 2m-2, top coefficient one, and (HP2).
Every coefficient of D_m F_m is a polynomial in x; the generic
vanishing of all higher coefficients proves the identity at every x,
including t=1,-1, by polynomial continuation. A reciprocal polynomial
with integer x coefficients has the unique folded expression (HP2):
T^j+T^-j=C_j(T+T^-1).

This intermediate P_m is not the universal recurrence numerator from
the parent. Sym^m(A) has dimension binom(m+2,2) and generally repeated
weights on this slice. Precisely,

    N_univ(A,T)=P_m(x,T) * D_sym(A,T)/D_m(x,T).      (HP5)

The quotient is a polynomial: each weight t^j in D_m occurs in Sym^m.
The ambient syzygy Euler polynomial has the further tensor-complement
determinant from parent SB5. Specialization must precede actual gcd
reduction. No finite natural-syzygy superdeterminant is asserted.

### HP2. Full word character, not an interpolation formula

Let words w have two copies of each letter 1,...,m, length N=2m.
Put des(w)=#{i:w_i>w_(i+1)} and
comaj(w)=sum_(i descent)(N-i). Then

    P_m(t+t^-1,T)
      =sum_w T^des(w) t^(comaj(w)-m des(w)).        (HP6)

For completeness, a direct proof of the classical identity is short.
A product of m Gaussian binomials [r+2 choose 2]_t enumerates m
weakly ordered pairs of integers in [0,r], weighted by t to their sum.
Stable-sort all 2m integers, with letters ordered increasingly on ties.
This gives a word w and weakly increasing b_1,...,b_N, required to be
strict at every descent of w; further strict inequalities are allowed. Set

    c_i=b_i-#{j<i:j is a descent of w}.

Then 0<=c_1<=...<=c_N<=r-des(w), and
sum b_i=sum c_i+comaj(w). Summing also over r transforms the weak
sequence into nonnegative successive gaps, whose generating function is
product_(j=0)^N (1-s t^j)^-1. Its word contribution is
s^des(w)t^comaj(w). Substitute s=Tt^-m and use (HP3).

Carnevale--Voll uses maj rather than comaj. Reverse the word and replace
each letter i by m+1-i: the equal-multiplicity multiset is preserved,
des is preserved, and maj becomes comaj (their Lemma 2.5).
Thus (HP6) is exactly their classical polynomial, not a different one.

The producer independently constructs P_m from the three-term h recurrence
over Z[x] and constructs the WHOLE Laurent character in (HP6) by dynamic
programming over counts/last letter/des/comaj. It covers respectively
2520, 113400 and 7484400 words for m=4,5,6, without enumerating the
largest word list individually. Every coefficient, not just the total
dimension, is compared.

## 3. Exact purity classifier and its certificate

For |t|=1, equivalently -2<=x<=2, all factors of D_m have unit roots.
Consequently P_m is pure if and only if its actual reduced numerator
is pure: gcd cancellation can remove only unit roots. By (HP2) this is
equivalent to every root of M_m(x,z) being real in [-2,2], counted with
multiplicity. A constant reduced numerator is vacuously pure.

Here is a fully specified finite recurrence defining every coefficient
used below; it also specifies M_6 without a fitted or decimal polynomial.
For this forward coefficient recursion only, take h_0=1 and h_r=0 for
r<0 (not the backward continuation used in HP1), and set for r>=1

    h_r=(x+1)h_(r-1)-(x+1)h_(r-2)+h_(r-3).
    d_j=[T^j]D_m.
    a_i=sum_(j=0)^i d_j h_(i-j)^m,  0<=i<=2m-2.
    M_m(x,z)=a_(m-1)+sum_(j=1)^(m-1) a_(m-1+j) C_j(z).   (HP7)

For reference, direct expansion gives

    M_4=z^3+(3x^3+9x^2+6x)z^2
      +(3x^5+17x^4+26x^3+9x^2-4x-4)z
      +x^6+12x^5+33x^4+20x^3-20x^2-16x,

    M_5=z^4+(4x^4+14x^3+13x^2+2x)z^3
      +(6x^7+36x^6+65x^5+25x^4-34x^3-28x^2-5x-4)z^2
      +(4x^9+39x^8+113x^7+91x^6-82x^5-144x^4-51x^3-5x^2+2x)z
      +x^10+20x^9+96x^8+140x^7-82x^6-340x^5-139x^4+150x^3+92x^2.

Let R_4,R_5,R_6 be the primitive positive-leading parts of

    disc_z(M_4)/(x+1)^2,
    disc_z(M_5)/[x^2(x+1)^6],
    disc_z(M_6)/[x^4(x+1)^10(x^2+x-1)^2],             (HP8)

respectively. Their degrees are 14,32,62 and their numbers of distinct
roots in (-2,2) are 3,10,22. Denote these roots in increasing order by
r_(m,j). Thus (HP7)--(HP8) define every endpoint algebraically, not
through a decimal approximation. Complete integer coefficient arrays,
disjoint rational isolating intervals, and exact Sturm variations are
resident in the fixture.

Define beta=(-7+sqrt(17))/2, gamma=(1-sqrt(5))/2, and let e be the
larger of the two roots in (-2,2) of
x^4+14x^3+48x^2+57x+20 (it lies between -615/1000 and -613/1000).

### Theorem GLO764.SEGRE_HIGHER_POWER_CHAMBERS_V1

The pure sets for the three powers are exactly the following closed sets:

    m=4:
      [r_(4,1), beta]
      union [-sqrt(2), r_(4,2)]
      union [r_(4,3), 0].

    m=5:
      [r_(5,2), r_(5,3)]
      union [-sqrt(2), gamma]
      union [e, r_(5,5)]
      union [r_(5,8), 0].

    m=6:
      [r_(6,2), r_(6,3)]
      union [-sqrt(2), r_(6,7)]
      union [r_(6,8), gamma]
      union [r_(6,10), r_(6,11)]
      union [r_(6,14), r_(6,15)]
      union [r_(6,16), 0].                         (HP9)

In particular the numbers of connected components are 3,4,6.
This is a finite classification for the specified powers, not a law for
all m. The exact rational countercontrols are

    x=-407/250: power five NOT pure; power six pure.
    x=-1/4:     power five pure; power six NOT pure.       (HP10)

So no nesting in either direction survives the held-out power six.

### Proof and complete coverage, including walls

For a monic real polynomial family, the number of simple roots in (-2,2)
is constant on every component of the complement of

    disc_z M_m * M_m(x,-2) * M_m(x,2)=0.             (HP11)

No root can leave the interval without hitting an endpoint or colliding.
The exact endpoint factorizations are:

    M_4(x,2)=x^2(x+1)^2(x^2+16x+34),
    M_4(x,-2)=x(x-1)(x^2-2)(x^2+7x+8);

    M_5(x,2)=x^2(x+1)^2(x^2+x-1)^2(x^2+24x+74),
    M_5(x,-2)=x(x-1)(x^2-2)(x^2-x-1)
                     (x^4+14x^3+48x^2+57x+20);

    M_6(x,2)=x^2(x-1)^2(x+1)^4(x^2+x-1)^2
                     (x^3+36x^2+222x+328),
    M_6(x,-2)=x^3(x-1)(x^2-2)(x^2-3)(x^2-x-1)
                     (x^5+22x^4+121x^3+263x^2+240x+73).   (HP12)

The producer constructs these from (HP7), factors (HP11), isolates
every real root in [-2,2], and verifies the complete root count for each
squarefree factor. There are respectively 9,21,36 distinct walls.
One rational point in EACH resulting open cell is tested by the Sturm
sequence p,p',-rem(p,p'),..., with zero signs omitted. Its implementation
uses integer pseudo-remainders: if e=deg(a)-deg(b)+1, prem(a,b)
=LC(b)^e rem(a,b). Correcting by sign(LC(b))^e and dividing by
positive coefficient content preserves each Sturm sign. Thus large
rational denominator growth is avoided without changing the theorem.
The difference
of variations at -2 and 2 counts the roots in that interval. All input
and intermediate recorded coefficients are exact rational numbers.
The full table has 10,22,37 cells, not a chosen collection of probes.
Joining the closures of the cells with m-1 roots gives exactly (HP9).
A second exact root-count interface agrees with each Sturm variation.

This covers open cells; the following argument is needed to rule out
additional isolated pure wall points. At an ordinary interior
discriminant wall the discriminant has a simple zero and neither
endpoint value vanishes. If all roots there are in (-2,2), exactly one
pair coalesces and all others are simple. Indeed a triple root or two
double roots gives discriminant order at least two, as follows either
from the local root factors or the Sylvester resultant's corank.
Isolate the double pair as a real-analytic monic quadratic. Its
discriminant has a simple sign change, so on one side both roots are
real and stay inside (-2,2); all other roots remain interior. Thus
one adjacent cell is pure. At an ordinary simple endpoint wall, with
nonzero discriminant and no other endpoint root, the single root
crosses the endpoint transversely; again its inward side is pure.
Neither kind of ordinary wall can be an isolated pure point.

All remaining shared or multiple factors in these three tables divide
x(x+1)(x-1)(x^2+x-1). This is checked exactly, including the fact that
R_m is squarefree and coprime to both endpoint polynomials. The
exceptional points are settled independently:

- x=-1 has h_r periodic [1,0,0], so F_m=1/(1-T^3).
- x=0 has h_r periodic [1,1,0,0], so F_m=1/[(1-T)(1+T^2)].
- x=1 has h_r periodic [1,2,2,1,0,0], so its reduced numerator is
  1+(2^m-1)T+T^2 and its denominator (1-T^6)/(1+T).
  It is not pure for m=4,5,6.
- If x^2+x-1=0, h_r is periodic [1,x+1,1,0,0], hence
  F_m=(1+(x+1)^m T+T^2)/(1-T^5).
  At the negative root |x+1|<1, so the quadratic is pure; at the
  positive root x+1=(1+sqrt(5))/2, its mth power is >2 for m>=2,
  so it is not pure. Cancellation against 1-T^5 cannot remove a
  nonunit root. In the tables the negative root is already in a
  pure interval; the positive root is not an extra point.
- At x=+-2 the exact specialized Sturm checks give fewer than m-1
  roots in [-2,2], with nonzero discriminants and endpoint values.
  These domain endpoints are not pure.

The pure set is closed by continuity of roots of a fixed-degree monic
polynomial. Thus all endpoints adjacent to pure cells are included,
and the preceding exhaustive wall argument excludes any others.
This completes the finite exact certificate proof of (HP9).

## 4. A separately labeled open SU(3)-torus cubic chamber

### Theorem GLO764.SEGRE_OPEN_SU3_CUBIC_CHAMBER_V1

There is a nonempty open subset of the determinant-one unitary diagonal
torus on which the rank-three cubic universal recurrence numerator
N_univ has seven distinct unit roots. Every neighborhood of the specific
point diag(t,1,t^-1), t+t^-1=-3/2, contains points of this open set
whose actual reduced denominator has generic order ten. The same
open set has pure ambient syzygy Euler polynomial and pure reduced
numerator in the parent's off-purity-divisor sense.

Proof. The exact polynomial at the indicated point is

    N(T)=(1-T)(1+3T/2+T^2)(1-T+13T^2/8-T^3+T^4).   (HP13)

The quartic folds to z^2-z-3/8, whose roots
(1+-sqrt(5/2))/2 are distinct and strictly between -2 and 2.
Each gives two distinct unit roots in T; the two pairs are disjoint.
The extra quadratic has folded coordinate -3/2, also strictly between
-2 and 2. It does not overlap the quartic because M(-3/2)=27/8.
Nor does T=1 overlap either factor: M(2)=13/8 and
1+3/2+1=7/2. Thus all seven roots are distinct.

For general determinant-one unitary diagonal A, parent SB14 says

    N_A(T)=-T^7 overline(N_A(1/overline(T))).        (HP14)

This is conjugate reciprocity; it does NOT assert real coefficients
or fixed-A palindromy. The constant coefficient is one and top
coefficient -1, so roots cannot appear at zero or infinity.

Choose seven disjoint small annular sectors around the seven roots
of (HP13), invariant under z -> 1/overline(z): use small angular
intervals and symmetric intervals for log|z|. Continuity of polynomial
roots, or Rouche on each boundary, gives exactly one root with
multiplicity in each sector for A in a sufficiently small torus
neighborhood. By (HP14) its reciprocal conjugate is another root in
the same sector. Uniqueness forces equality, hence modulus one.
Exactly one root counted with multiplicity also proves simplicity.

The ten degree-three monomials in the three torus eigenvalues are
distinct characters on SU(3). Indeed two exponent triples with sum
three restrict to the same character only when their difference is
a multiple of (1,1,1); its sum is zero, so that difference is zero.
Each equality between two distinct monomial values is a proper closed
subtorus (possibly disconnected). Their finite union has empty
interior. Avoid also the proper input-eigenvalue collision loci.
Every neighborhood therefore contains matrices with distinct input
eigenvalues and all ten monomials distinct. Parent SB6--SB7 then has
nonzero multinomial residue coefficients, giving actual order ten.
The parent dictionary adds or cancels only unit factors here.

There is also an open impure torus neighborhood near the identity:
parent SB17 has four simple nonunit roots, which remain off the
circle under small perturbation. Thus the new open pure chamber is
not automatic unitary-input purity. Along a continuous torus path,
loss of purity can occur only at a numerator-root collision: every
simple all-unit point is interior to the pure locus by the same
argument. This is a local deformation-spectrum consequence, not a
new natural representation, a finite syzygy superdeterminant, or
a global analytic completion.

No effective radius for the open neighborhood is asserted, and no
all-power full-torus chamber theorem is inferred from this cubic case.

## 5. Replay contract and unresolved scope

The manifest pins the five parent scientific files, the actual pre-m6
preregistration, and the independent parent review by exact commit,
Git blob and LF-normalized SHA-256. The five scientific files must
also match their current copies; the two historical notes need not.
The fixture seals the new proof, producer, tests and manifest plus
a canonical payload digest. Acceptance rebuilds the entire typed
payload; resealing a false result does not make it acceptable.

The fixed workload uses powers at most six, at most 250000 dynamic
states, polynomial total degree at most 80 at bounded interfaces,
at most 64 isolated walls, 2 MiB input/output byte bounds and JSON
depth 32. Rational inputs have a 1024-bit cap; recorded rational
results have a 65536-bit cap. SymPy exact rational polynomial,
factorization and real-root isolation routines are trusted finite
algebra backends; the producer does not claim an independently
verified kernel or per-internal-operation bit accounting for SymPy.
Its structural bounds and fixed finite panel prevent unbounded
user-supplied rank/degree workloads.

The arithmetic class is MIXED with EXACT_RATIONAL and
CERTIFIED_INTEGER_COVERAGE components, no rounding. There are no
floating root approximations, numerical periods or random inputs.
Whole word characters and every complementary Sturm cell are covered;
the all-m identity and open-neighborhood theorem are written proofs,
not conclusions inferred from finite replay.

    python -B research/l-families/atlas/generalized/segre_higher_power_unitary_chambers.py --check
    python -B -O research/l-families/atlas/generalized/segre_higher_power_unitary_chambers.py --check
    python -B -m unittest tests.test_segre_higher_power_unitary_chambers
    python -B -O -m unittest tests.test_segre_higher_power_unitary_chambers

The smallest invalidating statements are the full Laurent-character
identity, completeness of the wall factors/root isolators, the exact
Sturm counts, or the simple-root conjugate-reciprocity argument.
A failed m=6 prediction is retained as a failed prediction.

Nothing here constructs an Euler product, motive, Frobenius action,
automorphic family, global continuation, positive explicit formula,
or an RH/GRH argument. Higher-power torus geometry and all-m chamber
patterns remain open questions; the held-out counterexamples rule out
the most immediate nesting extrapolation.
