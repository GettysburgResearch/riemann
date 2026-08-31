# The actual cyclic-infinity module over its full invariant base

Status: proposed source theorem and bounded replay, separate from the frozen
extension-order packets. Scope: the actual coherent quadratic S3 source at
infinity, in characteristic-zero coefficients; no new global L-function or
analytic continuation is asserted. The matrix factorization below is a
relative covariant resolution, not a free resolution over the entire base.

Exact dependencies: finite comparison at
`0018b73f60e42bc793d172c381547de34322d8ca`, general invariant-base theorem at
`cfcfa42264a4ce5fc5846ac468c0c51c4cab9267`, and the Segre presentation and
Hilbert--Burch resolution in `../koszul-analytic-parent/MATHEMATICS.md` at
`7b320b3a9a55a16e73d99dd9bbab5bf592d50c93`.

## 1. Retain the quadratic inertia before taking cyclic invariants

Let k be a characteristic-zero field containing a primitive cube root of
unity. Put G=C3 and choose weight eigenvectors

    V=<v_+,v_->,              weights 1,2,
    W=<w_0,w_+,w_->,          weights 0,1,2,
    R_n=Sym^n(V) tensor Sym^n(W).

The commutative Segre algebra R is a domain, with its monomial realization
inside k[v_+,v_-,w_0,w_+,w_-]. At the infinity point of the actual quadratic
source, inertia is the joint cyclic group C6. Its quadratic subgroup acts
on R_n by (-1)^n and acts trivially on the added standard module S. Thus set

    A=direct_sum_(n even) R_n,
    P=Sym(S<2>)=k[p,q],       weights(p,q)=(1,2), deg(p)=deg(q)=2.

All degrees in this note retain the original grading; A has no odd grades.
The actual before stalk and its repaired full invariant base are

    C=(A tensor P)^G,
    B'=A^G tensor T,          T=P^G.

The original after stalk is B=A^G, since S^C6=0. Consequently C/B remains
the original graded B-module defect. It is not a B'-module: multiplying
1 in B by the nonconstant invariant pq leaves B. The finite-module results
below concern C over B', not a recategorization of the old cokernel.

Write A_i and P_i for G-weight i modulo3. The complete source decomposition is

    C=B' direct-sum (A_1 tensor P_2) direct-sum (A_2 tensor P_1).    (1.1)

The quadratic projection is essential. Replacing A by all of R gives a
different module, quantified in Section4, rather than a harmless change of
notation. Eigenvector choices mark a basis for the replay; the invariant
algebras and character summands themselves are defined by the given source.

## 2. Finiteness, Cohen--Macaulay property, and exact generic rank

The invariant polynomial algebra is the A2 hypersurface

    T=k[u,v,w]/(uw-v^3),
    u=p^3, v=pq, w=q^3,       degrees 6,4,6.                     (2.1)

Every invariant monomial p^a q^b has a-b divisible by3. Removing min(a,b)
copies of pq leaves a power of p^3 or q^3. The resulting normal forms,
with no simultaneous positive u- and w-exponents, prove both generation
and the single relation in (2.1).

**Theorem CINF.FINITE_CM_RANK.** C is a finite maximal Cohen--Macaulay
graded B'-module of generic rank3. In particular, maximal Cohen--Macaulay
does not imply free here: Section3 proves that C needs33 generators at the
homogeneous vertex.

**Proof.** Orbit polynomials make A finite over A^G and P finite over T.
Thus D=A tensor P is finite over B'. Reynolds averaging is a B'-linear
projection D->C, so C is finite over B'.

The frozen Segre resolution has length2 over the six-variable polynomial
ring and R has dimension4. The depth lemma gives depth(R)>=4, hence R is
Cohen--Macaulay. To justify all invariant-ring uses without assuming that
an arbitrary direct summand is Cohen--Macaulay, choose a homogeneous system
of parameters in the relevant finite invariant ring. Finiteness makes it
a system of parameters in R as well; it is therefore regular on R.
For invariant parameters, exact Reynolds averaging identifies invariants
of each successive quotient with the quotient of invariants. Their
regularity descends. Apply this first to the quadratic subgroup and then
to G: both A and A^G are Cohen--Macaulay of dimension4.

Choose four homogeneous parameters in A^G, and adjoin u,w from T. Their
quotient in T is k[v]/(v^3), so u,w are parameters and a regular sequence
on this two-dimensional hypersurface. On D the same six parameters are
regular: the first four act regularly on A, and u=p^3,w=q^3 form a regular
sequence in the independent polynomial factor P. Averaging the diagonal
G-action through these successive quotients proves that all six are
regular on C. They are parameters for the finite B'-module C. This proves
the claimed maximal Cohen--Macaulay property; it also gives the usual
local formulation by localization. The depth and parameter facts used
here are classical, as in [Stacks, Cohen--Macaulay rings](https://stacks.math.columbia.edu/tag/00N7).

For rank, let H=G times G act independently on D. Both actions are
faithful: A contains nonzero weight-one and weight-two degree2 monomials,
and P contains p,q. D is a domain because it is a polynomial extension of
the monomial domain A. We have D^H=B' and D^(diagonal G)=C.
For a finite group acting on a domain, its invariant fraction field is
the fraction field of the invariant ring: multiply a denominator by its
other group translates to produce an invariant denominator. Artin's
fixed-field theorem therefore gives

    [Frac(C):Frac(B')]=|H|/|G|=9/3=3.

Here the faithful independent actions and domain hypothesis are necessary;
rank3 was not read from a scalar numerator. The fixed-field input is
[Stacks, Lemma9.21.6](https://stacks.math.columbia.edu/tag/09I3). QED.

## 3. Literal minimal generators in all degrees

**Theorem CINF.MINIMAL_GENERATORS.** As A^G-modules, both A_1 and A_2 have
minimal generator polynomial 6t^2+2t^4. As a B'-module, C has minimal
generator polynomial

    1+12t^4+16t^6+4t^8.                                    (3.1)

Here the polynomial records the quotient C/(B'_+ C), not a formal Euler
characteristic. Its total dimension is33, whereas C has generic rank3.

**Proof.** A is generated by its degree2 monomials: independently partition
the V and W exponents of an even-degree Segre monomial into pairs and
match the pairs. Factor any A_i monomial into such degree2 pieces. If there
are at least three pieces and their total charge i is nonzero, a proper
nonempty subcollection has charge zero. Indeed a charge-zero piece works;
otherwise opposite charges form a pair; if every charge agrees, three
pieces work, and exactly three equal pieces would have total charge zero.
Remove that invariant product. Iteration proves generation in degrees2,4
for every grade, without extrapolating a finite enumeration.

A basis of R_m consists of

    v_+^a v_-^(m-a) w_0^b w_+^c w_-^d,
    0<=a<=m, b+c+d=m, charge=2m-a+c+2d modulo3.              (3.2)

At m=2, each nonzero charge has six monomials and there is no lower
positive degree in A. At m=4, each nonzero charge has25 monomials.
Their products from (A^G)_2 (A_i)_2 span exactly the monomials divisible
by an invariant degree2 Segre monomial. This is a literal monomial span;
no cancellation or choice of a character formula changes its rank.

For completeness the divisibility test is explicit. If alpha is the
number of v_+ factors removed, it must lie between max(0,a-2) and min(2,a).
An available W pair has the following required alpha:

| W pair | required alpha |
| --- | --- |
| w_0^2 or w_+ w_- | 1 |
| w_0 w_+ or w_-^2 | 2 |
| w_0 w_- or w_+^2 | 0 |

Applying this three-row test to (3.2) leaves exactly two nonzero-charge
exceptions in each character:

| charge | monomials not in (A^G)_2 (A_i)_2 |
| --- | --- |
| 1 | v_-^4 w_-^4, v_+^4 w_0^4 |
| 2 | v_-^4 w_0^4, v_+^4 w_+^4 |

For example a=2 permits every alpha and hence every W pair. For a=1
the only additional nondivisible W pattern is w_-^4, of total charge zero;
for a=3 it is w_+^4, again of charge zero. At a=0 and a=4 the table gives
the four displayed nonzero-charge exceptions; the other failures have
charge zero. Thus the old span has rank23 in each25-dimensional component.

The T-modules P_1 and P_2 are generated minimally by (p,q^2) and (q,p^2),
respectively, of degrees2,4. Remove pq, p^3, q^3 from any monomial to prove
generation; neither listed generator can be reduced by a positive
invariant. The minimal quotient of a tensor-product module over the
tensor-product base is the tensor product of its two minimal quotients.
Apply this to (1.1):

    1+2(6t^2+2t^4)(t^2+t^4)=1+12t^4+16t^6+4t^8.

This also proves minimality in every degree. A free module at the graded
vertex would have its number of minimal generators equal to its generic
rank. Since33!=3, C is not free there. QED.

At this homogeneous vertex C also has infinite projective dimension over
B'. Indeed both local depths are6. If its projective dimension were finite,
the classical [Auslander--Buchsbaum formula](https://stacks.math.columbia.edu/tag/090U)
would give projective dimension zero. A finite projective module over this
local ring is free, contradicting33 minimal generators and rank3. This is
a consequence of the classical formula, not an explicit free resolution
of C over B' or a whole-base periodicity assertion.

## 4. Quadratic omission and residual Frobenius are separate controls

If one incorrectly uses R instead of A at the actual infinity point,
the same argument gives two nontrivial covariants with minimal polynomial
2t+2t^2. The invariant degree-one factors are v_+ w_- and v_- w_+.
In degree2 the unreduced charge-one monomials are v_-^2 w_0^2 and
v_+^2 w_+^2; the charge-two monomials are v_-^2 w_-^2 and v_+^2 w_0^2.
The resulting untwisted calibration is

    1+4t^3+4t^4+4t^5+4t^6,                                (4.1)

with17 generators. It is a valid different source, but is a counterfeit
for the C6 stalk used here.

At split infinity the residual source action is the identity. At nonsplit
infinity choose the actual normalizer transposition phi. It swaps v_+ with
v_-, w_+ with w_-, and p with q, fixing w_0. Thus it interchanges the two
nontrivial summands in (1.1), preserves B'_+, and swaps the corresponding
minimal monomials. No positive-degree minimal generator is fixed. In the
three nonzero minimal degrees4,6,8 the dimensions and determinants are

| degree | dimension | trace(phi) | det(1-X phi) |
| --- | --- | --- | --- |
| 4 | 12 | 0 | (1-X^2)^6 |
| 6 | 16 | 0 | (1-X^2)^8 |
| 8 | 4 | 0 | (1-X^2)^2 |

The degree-zero line is fixed. Squaring phi recovers all dimensions.
This is the actual finite-monodromy residual action, not a claim that an
arbitrary scalar operator has been realized as arithmetic Frobenius.
The trace1 of the entire minimal quotient does not mean it has dimension1.

## 5. An explicit A2 covariant matrix factorization

Let N=P_1 with ordered generators (p,q^2), and keep the weighted T in (2.1).
Set

    F0=T(-2) direct-sum T(-4),
    F1=T(-8) direct-sum T(-10),
    D1=[[w,-v^2],[-v,u]],
    D2=[[u,v^2],[v,w]].                                    (5.1)

Over k[u,v,w], both products D1 D2 and D2 D1 equal (uw-v^3) times I2.
The grading is exact: D1:F1->F0 and D2:F0(-12)->F1. Over T the complex

    ... -> F1(-12) --D1--> F0(-12) --D2--> F1 --D1--> F0 -> N ->0

is an exact minimal free resolution. Here is a direct proof of exactness,
rather than an inference from a zero matrix product. For the last map
pi(a,b)=ap+bq^2, coprimality of p and q^2 in k[p,q] gives
(a,b)=(q^2 h,-p h), with h of charge2. Since h is generated over T by q,p^2,
this kernel is exactly the span of the columns of D1. Next D1(a,b)=0 is
equivalent to qa=p^2 b. Coprimality gives (a,b)=(p^2 h,qh), with h of
charge1, generated over T by p,q^2. These are the columns of D2. Similarly
D2(a,b)=0 is equivalent to pa=-q^2 b, giving the columns of D1 again.
All entries have positive degree, which proves minimality. Interchanging
p,q and u,w supplies the resolution of P_2.

Tensor these exact complexes over k with A_2 and A_1, respectively, and
adjoin the free B' summand in (1.1). This supplies explicit exact relative
complexes for the two nontrivial pieces of the actual C module. Their
terms A_i tensor T need not be free over A^G tensor T; this construction
does **not** identify them with a free two-periodic B'-resolution of C.
The residual normalizer exchanges the two covariant complexes.

## 6. What is new in scope, and what is not inferred

Finite invariant extensions, the A2 hypersurface, and its covariant matrix
factorizations are classical. The contribution here is their explicit
binding to the prescribed C6 infinity stalk, its literal33-generator
module, residual source action, and the exact distinction between the
old after base and the repaired full invariant base. No priority claim
for the classical algebra is intended.

The bounded replay will reconstruct monomial products and minimal quotients
independently of the displayed character polynomials, and check the matrix
identities before reducing modulo the hypersurface. All-grade generation
and exactness are proved above; finite ranks are controls, not proofs by
extrapolation. Nothing here makes the old cokernel finite over its original
base, turns this module into a unique source of its Euler function, or
improves an analytic radius from a vanishing residual trace.
