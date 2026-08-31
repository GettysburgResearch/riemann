# Normalization fixes the declared algebraic source, not its analytic frame

Status: proposed sequel to `CYCLIC_INFINITY_INVARIANT_MODULE.md`.
Scope: the actual C6 infinity algebra, its finite cyclic cover, and an
infinite-generator criterion. No new Euler-function uniqueness or analytic
continuation follows from normalization. Exact source pins and execution
are declared separately by the companion replay.

Keep the preceding notation over a characteristic-zero field k containing
the cube roots of unity:

    R_n=Sym^n(V_std) tensor Sym^n(W_perm),
    A=direct_sum_(n even) R_n,  G=C3,
    P=k[p,q], weights(p,q)=(1,2), deg(p)=deg(q)=2,
    T=P^G=k[u,v,w]/(uw-v^3),
    B'=A^G tensor T,            C=(A tensor P)^G.

The quadratic-even projection is part of A. It is not removed in this
sequel. The old after algebra is A^G, whereas B' is its specified full
invariant-generator enlargement.

## 1. A precise uniqueness category

**Theorem NORM.CUBIC_SOURCE.** The domain C is the integral closure of B'
in the prescribed cyclic cubic field extension K=Frac(C) of F=Frac(B').
Consequently it is the unique integrally closed domain E with

    B' subset E subset K,  E integral over B',  Frac(E)=K.       (1.1)

The embeddings and the field K are part of the data. Equality of a Hilbert
series, local trace function, or Euler function is not substituted for them.

**Proof.** The Segre algebra is the invariant subring of
k[v_+,v_-,w_0,w_+,w_-] under the multiplicative group that scales V by t and
W by t^-1. It is normal. Indeed, for any group acting on a normal domain D,
an element x of Frac(D^G) integral over D^G is integral over D, hence belongs
to D; it is fixed and therefore belongs to D^G. This argument does not
require the acting group to be finite. Apply it first to the multiplicative
group and then to the quadratic subgroup to obtain normality of A.
Polynomial extension preserves normality. Therefore D=A[p,q], C=D^G and
B'=D^(G times G) are normal domains. The basic normal-domain statements
are classical; see [Stacks, normal rings](https://stacks.math.columbia.edu/tag/037B).

The two G actions on D are independent and faithful. The diagonal subgroup
is normal in the abelian group G times G. The fixed-field theorem gives
K/F cyclic of degree3, with deck group (G times G)/(diagonal G).
The preceding finite-base theorem proves C finite, hence integral, over B'.
If x in K is integral over B', its monic equation also has coefficients in
C, so normality of C gives x in C. Thus C is the whole integral closure.
The same argument applied to any E in (1.1) proves equality with C. QED.

This is a genuine algebraic universal specification relative to the stated
extension. It does not say that Euler data determine K or the prescribed
inclusion of B'. The earlier generization counterexample lives outside
this category and is not contradicted by the theorem.

## 2. The relative A2 matrices describe an actual local cover

Let U be the geometric free-action locus of G in Spec(A), and X=U/G.
The quotient U->X is a finite etale G-torsor. The free finite-group quotient
statement applies to this open subscheme of an affine scheme; see
[Stacks, Lemma66.14.2](https://stacks.math.columbia.edu/tag/07S7).
The group is finite etale here, so its torsor is etale.

Over X times Spec(T), pull back Spec(C)->Spec(B') along the torsor U->X.
The resulting morphism is exactly

    U times Spec(P) -> U times Spec(T).                         (2.1)

To verify (2.1), use the torsor identity U times_X U = G times U.
The diagonal G-invariants in the corresponding product of copies of P
are determined by one copy. Algebraically this identifies the base-changed
invariant algebra with O(U) tensor P. Invariants commute with this flat
base change, or directly with the averaging idempotent. Thus the covariant
matrix factorization in the preceding packet is the local standard model
of the actual cover after a specified etale pullback, not a matrix chosen
only to reproduce a numerator.

There is also a completely explicit source chart. Write the six Segre
coordinates as

    [[a,b,c],[d,e,f]]=[[v_+w_0,v_+w_+,v_+w_-],
                      [v_-w_0,v_-w_+,v_-w_-]].

The element z=a^2 lies in A, has G-weight2, and has original degree2.
Set s=z^3=a^6 in A^G and restrict to s!=0. Since z is invertible, every
G-covariant in A_s is an invariant multiple of 1,z or z^2. Hence

    A_s=(A^G)_s[z]/(z^3-s),

an etale cubic torsor, since 3z^2 is a unit. In C_s put x=zp and y=z^2q.
Every diagonal-invariant monomial is a polynomial in x,y over (A^G)_s:
the remaining power of z is a multiple of3 and so is a power of the unit s.
Algebraic independence of p,q proves

    C_s=(A^G)_s[x,y],
    x^3=s u,    xy=s v,    y^3=s^2 w.                          (2.2)

This is a scaled A2 quotient map. It is already an actual source chart;
no new arithmetic field panel or numerical parameter fitting is involved.

At the T-origin u=v=w=0 the fibre of P->T is

    k[p,q]/(p^3,pq,q^3),

with basis 1,p,q,p^2,q^2 and length5. Its generic rank is3. Therefore the
finite cover is not flat at that origin, and (2.1), or the explicit chart
(2.2), supplies an actual codimension-two nonflat stratum of C over B'.
The five-dimensional fibre is not confused with the33-dimensional minimal
quotient at the homogeneous vertex of the full base.

## 3. No branch divisor, despite the nonflat stratum

All assertions about fixed loci in this paragraph are geometric and may
be checked over an algebraic closure of k. On Spec(R), the nonzero-weight
coordinates are a,b,d,f. Setting them to zero leaves c,e with the Segre
relation ce=0. The G-fixed locus is the union of those two coordinate
axes and has dimension1.

Spec(A) is the quotient of Spec(R) by the sign action on all six Segre
coordinates. If a nonzero geometric point of Spec(A) is G-fixed, choose
a lift r in Spec(R). Its image gr must be r or -r. Since g has order3
and commutes with the sign action, gr=-r would imply r=-r, impossible
away from the origin in characteristic zero. Thus the geometric fixed
locus of A is the image of the same two axes. It has codimension3 in
the four-dimensional Spec(A). No claim that the scheme-theoretic fixed
locus of A is reduced is needed.

In Spec(P) the G-fixed locus is only p=q=0, of codimension2. Outside

    (Fix_G Spec(A)) times Spec(P)
       union Spec(A) times {(0,0)},                           (3.1)

the independent action of G times G is free. Its quotient residual action
on the diagonal quotient is also free: if h sends a diagonal orbit to
itself, some diagonal element d has d^-1 h fixing a point, so h is diagonal.
The cubic morphism Spec(C)->Spec(B') is consequently etale away from the
images of (3.1). Finite maps preserve dimensions, and these two images
have codimensions3 and2. In particular the morphism is etale at every
codimension-one point of the base.

This does not contradict the nonflat codimension-two fibre in Section2.
Nor is a stabilizer of order3 at that fibre called a divisorial ramification
index: the statement is about a finite cover of a singular base, with no
branch divisor. The distinction is relevant to interpreting the relative
matrix factorization.

## 4. The infinite-generator finiteness criterion

Now let S be a positively graded G-representation with finite-dimensional
grades, and put P_infinity=Sym(S). It may have infinitely many generators.
Keep the same finite source A, and define the degreewise finite algebras

    B'_infinity=A^G tensor P_infinity^G,
    C_infinity=(A tensor P_infinity)^G.

Write S=S_0 direct-sum S_1 direct-sum S_2 for its three character summands.

**Theorem NORM.INFINITE_FINITE_BASE.** C_infinity is a finite B'_infinity
module if and only if dim(S_1 direct-sum S_2) is finite. In all cases it is
the integral closure of B'_infinity in its prescribed fraction field.
If S_1 direct-sum S_2 is nonzero, that field extension has degree3; if it
is zero, C_infinity=B'_infinity. Neither Noetherianity nor a Cohen--Macaulay
assertion is imposed on these infinite algebras.

**Proof.** First suppose there are only finitely many nontrivial generator
directions. Separate the arbitrary trivial polynomial variables:

    P_infinity=Sym(S_0) tensor Sym(S_1 direct-sum S_2).

The finite-variable theorem makes the diagonal invariants finite over the
full independent invariant base. Tensoring that finite generating list
with Sym(S_0) proves finiteness here, even if S_0 is infinite-dimensional.

For the converse let Abar_i=A_i/((A^G)_+ A_i), and let
Pbar_i=(P_infinity)_i/((P_infinity^G)_+ (P_infinity)_i).
The minimal quotient over the connected graded base splits exactly as

    C_infinity/(B'_infinity,+ C_infinity)
      = k direct-sum (Abar_1 tensor Pbar_2)
          direct-sum (Abar_2 tensor Pbar_1).                  (4.1)

Each Abar_i has Hilbert polynomial a(t)=6t^2+2t^4 from the actual C6
packet. In fact the polynomial covariant quotients have the exact natural
description

    Pbar_1 = S_1 direct-sum Sym^2(S_2),
    Pbar_2 = S_2 direct-sum Sym^2(S_1).                       (4.2)

Choose a homogeneous character basis for S. A monomial containing a
trivial variable has a positive invariant factor. The same holds for a
monomial containing an opposite-charge pair or three equal charges.
Every nontrivial-charge monomial of polynomial length at least3 has one
of these proper invariant factors. Conversely, a single nontrivial
variable or two variables of the same nontrivial charge have no such
factor. The invariant monomials span the invariant ideal, so exactly
these independent monomials survive. Polynomial length and the symmetric
square identify the surviving spaces independently of the chosen basis.
This argument also works for infinitely many locally finite generators,
since each monomial has finite support.

Consequently the full minimal-generator series is exactly

    M(t)=1+a(t)[H_S1(t)+H_S2(t)
                 +H_Sym^2(S1)(t)+H_Sym^2(S2)(t)].            (4.3)

In particular infinitely many nontrivial directions make (4.1)
infinite-dimensional over k. A finite module would have a finite-dimensional
quotient by the base augmentation ideal, a contradiction.

For normality, a polynomial algebra in arbitrarily many variables over
the normal domain A is still normal: an integral equation and a fractional
element involve only finitely many variables, where normality is already
known. Taking invariants preserves normality by the argument of Section1.
Moreover C_infinity is integral over B'_infinity. The residual cyclic
group acts on it and its orbit polynomial has coefficients in B'_infinity;
no finite-generation hypothesis is needed for this monic equation.
The normal-domain argument then identifies it with the integral closure.
If any nontrivial generator exists, the independent finite group actions
on the fraction field are faithful, and the same fixed-field theorem
gives degree3. If none exists, taking invariants simply acts on A, giving
equality of the two algebras. QED.

Thus a specified normal integral source can be canonical in its declared
field extension while needing infinitely many module generators over its
full invariant base. An analytic topology, determinant regularization,
or scalar normalization is not part of this universal property.

## 5. Application to the existing actual Lie-generator ladder

The frozen completion source adjoins, in each positive even degree n,

    T_n=B_n sign direct-sum C_n Std.

On G=C3 the sign representation is trivial, while Std has the two
nontrivial characters. The source multiplicity theorem in
`../koszul-analytic-parent/GLOBAL_KOSZUL_LIE_COHOMOLOGY.md` gives

    C_n=(epsilon_n-tr(c|M_n))/3 ~ 2^n/(3n).

In particular infinitely many even degrees contain nontrivial directions.
The theorem applies to this actual source, not an arbitrary sequence fitted
to its scalar determinant. Its normalization remains a cubic-field
integral closure, but it is not finite over B'_infinity. Put
C(t)=sum_(n>=2, n even) C_n t^n. Both nontrivial generator summands have
this series, and H_Sym^2(S)(t)=[H_S(t)^2+H_S(t^2)]/2. Thus the exact full
minimal-generator series, including the quadratic covariants, is

    M(t)=1+(6t^2+2t^4)[2C(t)+C(t)^2+C(t^2)].                 (5.1)

For a finite even cutoff N, replace C by C_N=sum_(2<=n<=N, n even) C_n t^n.
This gives the exact finite minimal polynomial, not only a linear lower
bound. The sign summands in T_n are trivial on C3 and are already variables
of the base; they add no generators to this quotient.

There is also an all-degree asymptotic consequence. Write c_j=C_(2j), so
c_j~4^j/(6j). If mu_n is the coefficient of t^n in (5.1), then

    mu_(2j) ~ (13/144) 4^j log(j)/j,   mu_(2j+1)=0.          (5.2)

Indeed, the coefficient of t^(2j) in C(t)^2 is
sum_(k=1)^(j-1) c_k c_(j-k) ~ 4^j log(j)/(18j).
To justify this from the imported source asymptotic, fix epsilon>0 and
then K so c_k/(4^k/(6k)) lies between 1-epsilon and 1+epsilon for k>=K.
The finitely many endpoint terms contribute O_K(4^j/j). The middle terms
are squeezed using sum_(k=1)^(j-1) 1/[k(j-k)]=2H_(j-1)/j; deleting a fixed
number of endpoints changes that harmonic sum by O_K(1/j). Letting
epsilon tend to zero proves the displayed equivalence. No uniform
O(4^j/j) remainder for the whole convolution is inferred from ~ alone.
The shifts in a(t) multiply the leading constant 1/18 by
6/4+2/16, giving 13/144. The linear term and C(t^2) are lower order.
Equivalently along even n, mu_n~(13/72)2^n log(n)/n.

The field degree remains3 while minimal module generators have this
extra logarithmic growth. This statement concerns algebraic generators;
it does not change an operator ideal or define a determinant.

The actual source-normalization theorem and the earlier analytic cutoff
theorems answer different questions. This note neither picks one of the
many analytic regularization policies nor extends an ordinary Fredholm
operator beyond its proved ideal domain. Finite invariant theory, normal
closure, and torsor descent are classical; the new scope is the precise
finite/infinite source distinction, explicit local nonflat model, and its
application to the prescribed ladder.
