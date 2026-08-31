# Why the certified higher maps resolve the source in every degree

Status: a conditional proof and validation guide, not a report that the
pending degree-six or degree-seven acquisition has succeeded. The previous
898-row preflight failure proves no statement about those kernels. The new
original-row method has a separate declaration and certificate. No author
or reviewer scientific job is part of this note.

The statement concerns the marked source over Q:

    V=Q^3, W=Sym^3(V), S=Sym(W), m=S_{>0},
    R=direct_sum_j (Sym^j V) tensor (Sym^j V) tensor (Sym^j V).

The ten variables of S act by the literal symmetric sums in R_1. All modules
below are finitely generated, graded and bounded below. The target is an
exact sequence of S-modules, not an assertion that D1 or D2 is injective.

## 1. Independent inputs and the absence of a Hilbert-series inference

The source theorem and low-degree Koszul computation are frozen at
`a895f47628b0bc7c7ee5e0392df2f79c24166f92`; the complete character note is
`TERNARY_CUBE_TOR_CHARACTERS.md` at
`08147ccecfe684af76a8417861fcccda61abe601`. The marked first presentation
is frozen at `4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787`.
The full certified degree-five cache is frozen at
`742d68b6d3c37191589b0e6463bc122af6d90f76`.
These inputs have different roles and must not be replaced by an Euler
numerator that merely has the same alternating coefficients.

First, the classical finite Chow-module theorem gives finiteness over S
and Cohen--Macaulay dimension seven. Since S is a ten-variable polynomial
ring, its projective dimension is three. These are source theorems before
any choice of D2 or D3. Their attribution and conventions are recorded in
`MATHEMATICS.md`, SHS1--SHS2, and the cited work of Raicu--Sam--Weyman.

The canonical module supplies a second independent input. In the stated
Sym(V) convention the canonical module of this equal-rank Segre ring is

    omega_R = R(-3) tensor (det V)^3,
    omega_S = S(-10) tensor det(W),   det(W)=(det V)^10.

Consequently

    Ext^3_S(R,S) = R(7) tensor (det V)^(-7),
    Ext^i_S(R,S)=0 for i != 3.

Dualizing an abstract minimal free resolution therefore yields the graded
Tor duality

    Tor_(3-i,7-j)^S(R,Q)
        = Tor_(i,j)^S(R,Q)^* tensor (det V)^7.          (1)

Existence of this abstract resolution is the classical homological input;
it is not a claim that the new marked matrices already form that resolution.

Second, actual source multiplication in the Koszul complexes computes Tor
in internal degrees zero through three. In positive degrees1,2,3 its
dimensions are

    Tor_0: 17,11,0;    Tor_1: 0,20,65;
    Tor_2: 0,0,0;     Tor_3: 0,0,0.

Degree zero contributes only Tor_(0,0)=Q, and negative degrees vanish.
The full weight records, including the zero groups, come from those source
differentials. Equation(1) then determines every remaining internal degree:
degree j>=4 is paired with degree7-j<=3; for j>7 it is paired with a negative
degree. This gives

    Tor_0: 1 in degree0,17 in degree1,11 in degree2;
    Tor_1: 20 in degree2,65 in degree3;
    Tor_2: 65 in degree4,20 in degree5;
    Tor_3: 11 in degree5,17 in degree6,1 in degree7;
    Tor_i=0 for i>=4.                                 (2)

Thus the exclusion of unseen higher-degree generators uses actual low-degree
homology plus canonical-module duality and projective dimension. It does
not use the scalar Hilbert numerator, an assumed symmetry of that numerator,
or an alternating rank calculation for the proposed complex.

## 2. The graded generation lemma used at each stage

Let M be a finitely generated graded S-module bounded below. If homogeneous
elements have images forming a Q-basis of M/mM, they generate M: the quotient
by their span satisfies Q=mQ, hence is zero by graded Nakayama. Equivalently,
a nonzero quotient would have a smallest nonzero degree, impossible under
Q=mQ. If M/mM vanishes below degree d, the same least-degree argument gives
M_j=0 for j<d.

Suppose its quotient is supported in a known finite set of degrees. Work
upwards through those degrees. Once all lower-degree pieces are generated
by the selected elements, the degree-j part of mM is exactly the span of
all positive-degree monomial multiples of those lower elements. Computing
the actual full M_j and this actual old span, then selecting a basis of the
quotient, gives the required basis of (M/mM)_j. No assumption that the old
columns are linearly independent is permitted.

For a minimal graded free cover F -> M with kernel K, tensoring
0 -> K -> F -> M -> 0 with Q gives

    K/mK = Tor_1^S(M,Q).                              (3)

Here minimality means K is contained in mF, so the map K/mK -> F/mF is zero.
For an already exact sequence of preceding free covers, dimension shifting
identifies this Tor_1 with the corresponding higher Tor of R. This is why
each cover must be proved exact and minimal before using(3) at the next one.

## 3. Surjectivity onto the two actual higher kernels

The frozen marked source provides the exact minimal presentation

    F1 --D1--> F0 --epsilon--> R -> 0,
    F0=S+17S(-1)+11S(-2), F1=20S(-2)+65S(-3).

Its proof already applies the preceding lemma to Tor_0 and Tor_1. In
particular epsilon is globally surjective and image(D1)=ker(epsilon).

Put K1=ker(D1). By(3) and dimension shifting,
K1/mK1=Tor_2^S(R,Q), supported precisely in degrees4,5. Thus K1 vanishes
below4. The certified degree-four calculation gives all65 vectors of K1_4.
In degree5, construct all65*10=650 variable multiples in the original
F1_5 coordinates. Their independently computed rank is639, not650.
The full K1_5 has dimension659. The twenty selected quotient classes,
together with the65 degree-four classes, form a basis of K1/mK1.
Graded Nakayama now proves that the actual map

    D2: F2=65S(-4)+20S(-5) -> F1

has image exactly K1 in all degrees. Its entries have positive polynomial
degree, and its85 generator images are a basis modulo mK1; this is a minimal
free cover of K1. This conclusion uses the already certified stage-five
cache and does not depend on a successful new degree-six calculation.

Now put K2=ker(D2). Only after that conclusion may one identify
K2/mK2=Tor_3^S(R,Q), supported precisely in degrees5,6,7. Hence K2 vanishes
below5. The actual degree-five kernel has eleven vectors, all minimal.
The pending checks must establish the following statements directly:

| Degree | Full kernel dimension | All old monomial columns | Actual old rank | New quotient classes |
| --- | ---: | ---: | ---: | ---: |
| 5 | 11 | 0 | 0 | 11 |
| 6 | 127 | 11*10=110 | 110 | 17 |
| 7 | 776 | 11*55+17*10=775 | 775 | 1 |

The degree-six old columns are the variable multiples of the eleven
degree-five classes. The degree-seven old columns include every quadratic
multiple of those eleven and every variable multiple of the seventeen new
degree-six classes. Their ranks must be computed; the arithmetic counts
110 and775 do not prove the ranks. After the complete kernels, old spans,
compositions and quotient independence pass, the29 chosen classes form a
basis of K2/mK2. Graded Nakayama then proves image(D3)=K2 globally, for

    D3: F3=11S(-5)+17S(-6)+S(-7) -> F2.

The positive-degree entry check, including the absence of constant entries
from degree-five F3 into degree-five F2, is part of minimality. Comparing
every torus weight with(1) supplies a separate source-consistency check;
it cannot substitute for an actual kernel or quotient calculation.

## 4. Injectivity of the final differential and exactness at every term

At this point F3 -> K2 is an exact minimal free cover. Let K3=ker(D3).
Equation(3) and the already established preceding exact covers give

    K3/mK3 = Tor_4^S(R,Q)=0.

K3 is a finitely generated graded S-submodule of F3 because S is Noetherian.
Graded Nakayama therefore gives K3=0. This proves injectivity of D3 without
an unbounded matrix census. Together with the previous surjectivity results
it proves

    0 -> F3 --D3--> F2 --D2--> F1 --D1--> F0 -> R -> 0

is exact in every internal degree. All its differentials are minimal.
There is no circular appeal to the exactness of the proposed complex:
each cover is established from the preceding one before the next Tor
identification is used. Cohen--Macaulayness supplies the independent
projective-dimension bound; it does not by itself certify arbitrary matrices
with these free ranks or arbitrary compositions equal to zero.

## 5. What the new row-restricted certificate must prove

For a full integer weight block A, the selected r original rows form B.
Their independent modular rank proves rank_Q(B)=r. The unchanged rational
kernel algorithm supplies n-r independent vectors in ker(B). Checking all
of them against every original row of A proves ker(B)=ker(A), since
ker(A) is already contained in ker(B). Thus the retained vectors are the
complete full kernel required in the table, despite eliminating fewer rows.

This certificate must retain the original domain coordinates, actual full
compositions, independence and cardinality, and the independently computed
old quotient ranks. An unlucky fixed prime, missing witness, unverified
checkpoint, successful partial stage, matching Hilbert series or matching
total nullity alone does not meet these hypotheses. Only after both new
stages pass may the conditional conclusion above be recorded as executed.

The result is one complete marked resolution of the actual Chow module.
It does not make the marked generator lifts GL3-equivariant, turn the
K-polynomial into an automatic finite superdeterminant, or provide a new
general existence theorem for Chow resolutions.
