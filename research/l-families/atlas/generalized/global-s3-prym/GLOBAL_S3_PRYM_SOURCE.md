# A ramified global source for the holonomy projector and its Prym twist

Status: proposed exact function-field construction and deformation boundary.
Scope: smooth projective curves over finite fields of characteristic greater
than three. This is not an adapter for the repository's integer Möbius source,
and it is not a proof of number-field RH or GRH.

The source is specified by equations before any point counts or eigenvalues.
The construction joins a finite monodromy projector, all ramified local
factors, a global cohomological determinant, a genuinely ramified twist, and
a deformation on which a commutator detector fails. The ingredients are
classical; external mathematical priority is not claimed.

The holonomy precursor is frozen at
`e7fc8b0af2c42ce43384543972df2ed44f343300` (based word comparison), and the
positive-defect precursor at
`6b4f0f4a53bc9ff5bc6b84a2b6e3f603a04f2336`, in
`research/exploratory/marked-holonomy-response/`. The latter proof blob
`POSITIVE_DEFECT_AND_CRITICAL_CIRCLE.md` is
`56de4c6dbcd77bcb7a672e21153747af9e346074`. We rederive the needed finite
matrix identity below; no alteration of those reviewed sources is made.

## 1. Source and conventions

Let k=F_q with characteristic p>3. Choose A,B in k with

    Delta = -4 A^3 - 27 B^2 != 0.

Let E be the smooth projective elliptic curve y^2=x^3+Ax+B, with its usual
rational point at infinity. The first source map is f:E -> P^1_t, t=y.
Unless explicitly discussing the cyclic stratum, also assume A!=0.

Let C be the smooth projective curve with affine equation

    w^4 = x^3+Ax+B.

There is a degree-two map h:C -> E, y=w^2, and a degree-six map C -> P^1_t.
These denote the smooth projective models, not singular projective closures
silently used in place of their normalizations.

Fix an auxiliary prime ell distinct from p and work with Q_ell coefficients.
All displayed permutation projectors have rational coefficients. Positivity
of such a matrix refers to its usual real/complex permutation realization;
there is no ordering or positive cone on Q_ell being asserted.

Frobenius F is normalized by

    #X(F_(q^n)) = 1 + q^n - tr(F^n | H^1(X_bar,Q_ell))

for a smooth geometrically connected projective curve X. Thus the
eigenvalues on H^1 have complex absolute value sqrt(q), and on Q_ell(-1)
the action is q. Arithmetic-Galois Frobenius and its inverse must not be
interchanged when transporting this convention.

For a lisse sheaf V on a dense open j:U -> P^1, its unshifted
middle-extension sheaf here is j_*V. Its stalk at a deleted point is the
inertia-invariant space V^I. The Euler factor at a closed point v is

    det(1 - T^(deg v) F_v | V^I_v)^(-1).

This convention is not j_!V and does not delete ramified Euler factors.

## 2. The cubic monodromy and every ramified factor

**GSP-1.** For A!=0, the geometric and arithmetic monodromy groups of
f are S3 in their degree-three permutation action. The branch divisor is

    d(t) = -4 A^3 - 27 (B-t^2)^2 = 0,

together with infinity. There are four distinct geometric finite branch
points with transposition inertia and a three-cycle at infinity.

Proof. The map has degree three because y has a pole of order three at the
elliptic point at infinity. It is geometrically connected and separable.
The cubic x^3+Ax+(B-t^2) has discriminant d(t). A repeated zero of d would
require t=0 or B=t^2; these give Delta=0 or A=0, respectively. Both are
excluded. Each finite zero therefore has one simple ramification of index
two. The unique pole gives index three at infinity. The transitive
geometric degree-three group containing a transposition is S3. The
arithmetic group is a subgroup of S3 containing it, hence also S3.
All ramification is tame since p>3.

Let W be the standard two-dimensional summand of the permutation local
system on the complement of the branch divisor. Its extension is denoted
Wbar=j_*W. The rational augmentation projector is

    P = I - J/3,

where J is the all-ones 3-by-3 matrix. It commutes with every permutation,
and on the complete base there is an exact direct-sum decomposition

    f_* Q_ell = Q_ell direct_sum Wbar.                         (2.1)

This decomposition includes ramification: take inertia invariants of the
generic decomposition. The unit/trace splitting has generic degree three;
on a ramified stalk its trace weights the inertia orbits by their sizes.
It must not be replaced by the unweighted sum over distinct ramified
points. In contrast, the trace of Frobenius on the stalk counts those
distinct geometric points fixed by Frobenius.

At a finite branch point with residue t_0, the double root is

    r = 3(t_0^2-B)/(2A),

and the remaining root is -2r. Both lie in its residue field and are
distinct. Consequently W^I is one-dimensional and F_v acts as +1. The
local factor is (1-T^(deg v))^(-1). At infinity W^I=0 and the factor is
one. The tame conductor has total degree 4*1+2=6.

At an unramified closed point, the factors are determined by the cubic
factorization over its residue field. Writing z=T^(deg v):

| Frobenius permutation | cubic type | standard denominator |
|---|---|---|
| identity | 1+1+1 | (1-z)^2 |
| transposition | 1+2 | 1-z^2 |
| three-cycle | 3 | 1+z+z^2 |

These factors come from the permutation source, not fitted point counts.

## 3. The global elliptic factor and the positive projector

Finite pushforward and the trace formula applied to (2.1) give

    L(P^1,Wbar,T) = Z(E,T)/Z(P^1,T)
                 = P_E(T) = det(1-TF | H^1(E_bar,Q_ell)).     (3.1)

Equivalently, for every n>=1, summing the local stalk traces gives
#E(F_(q^n))-(q^n+1). This supplies the same formal Euler identity directly.
The direct summand identifies the cohomology: H^0(P^1,Wbar)=0,
H^2(P^1,Wbar)=0 and H^1(P^1,Wbar)=H^1(E_bar), of dimension two.
Thus the numerator and its degree follow from the source, not division of
a few computed polynomials.

In the S3 permutation representation let u,v be distinct transpositions.
Their commutator k=(uv)^(-1)vu is a three-cycle. The earlier holonomy defect
has the exact identity

    H = I - (k+k^(-1))/2 = (3/2)P.                            (3.2)

Indeed I+k+k^(-1)=J. This makes (2/3)H the actual augmentation projector.
Unlike a general fixed-label comparison, it is central in this monodromy
representation. It therefore defines an endomorphism of (2.1), including
every ramified stalk, and its image is exactly Wbar.

Equation (3.2) is also a positive real Gram identity on the finite
permutation fibre. It does not imply the weights of global Frobenius.
Those use the separately imported curve theorem. In our normalization

    P_E(T) = 1-a_q T+q T^2,
    P_E(T) = q T^2 P_E(1/(qT)),
    every root of P_E has absolute value q^(-1/2).             (3.3)

The reciprocal pairing is the cup product on H^1, not an inference from
positivity of H. The trivial base summand carries the P^1 Tate factors;
the positive projector removes that summand and retains the elliptic
cohomology. This should not be confused with selecting the principal
integer channel in a different arithmetic programme.

## 4. A genuinely ramified Kummer twist

Let chi_t be the quadratic Kummer local system from t=w^2 on G_m, with
middle extension to P^1. Its stalk trace at t in a finite field is the
quadratic character chi(t), extended by chi(0)=0. It is ramified at zero
and infinity, so this is not merely a constant-field quadratic twist.

Because Delta!=0, the divisor of y on E consists of three distinct simple
zeros and a pole of order three at infinity. The double cover h is
connected and branched at exactly these four points. Riemann-Hurwitz gives
2g(C)-2=2(2g(E)-2)+4=4, so g(C)=3.

On the common unramified open, the permutation representation of the
degree-six cover splits as

    1 direct_sum W direct_sum chi_t direct_sum (W tensor chi_t).

Finite pushforward from the smooth projective curves extends this splitting
by inertia invariants. Also

    L(P^1,j_*chi_t,T)=Z(P^1_w,T)/Z(P^1_t,T)=1.

It follows, with every ramified factor included, that

    L(P^1,j_*(W tensor chi_t),T)
       = Z(C,T)/Z(E,T) = P_C(T)/P_E(T) = P_-(T).               (4.1)

The degree-four assertion is geometric. The involution w -> -w splits
H^1(C) into the image of h^*H^1(E) and a four-dimensional anti-invariant
summand H^1(C)^-. Both summands are Frobenius stable. The pullback/trace
identities for this double cover identify the first summand with H^1(E).
Thus P_-=det(1-TF|H^1(C)^-) is a polynomial. It is the Prym factor in this
cohomological sense; no principal polarization type for the Prym variety
is asserted here.

The complete ramification ledger for W tensor chi_t is:

| place | inertia on the relevant fibre | invariant dimension | conductor |
|---|---|---|---|
| 0 | -I on the unramified rank-two W fibre | 0 | 2 |
| each original finite branch | transposition, with unramified chi_t | 1 | 1 |
| infinity | a three-cycle multiplied by -1 | 0 | 2 |

Zero is not an original branch because d(0)=Delta!=0. At an old branch
v the invariant Frobenius eigenvalue is chi_(k(v))(t_v), so its local
factor is (1-chi_(k(v))(t_v) T^(deg v))^(-1), not always (1-T^(deg v))^(-1).
At zero and infinity the factors are one. At other points replace z by
chi_(k(v))(t_v)z in the table of Section 2. The total conductor degree is
2+4+2=8, consistent with the rank-four cohomology. The genus and direct
summand proof above do not depend on deriving that degree from a conductor
formula.

The cup product pairs the plus and minus summands orthogonally, since the
involution changes the sign on exactly one argument of a mixed pairing.
Its restriction to the minus summand is nondegenerate and q-symplectic.
Consequently, for integers a,b,

    P_-(T)=1-aT+bT^2-qaT^3+q^2T^4,
    P_-(T)=q^2T^4 P_-(1/(qT)),                               (4.2)

and all four roots have absolute value q^(-1/2), by the curve weight
theorem and the source-defined direct summand. The finite Gram operator
does not prove this spectral bound.
Integrality also follows directly from (4.1): the two curve numerators
have integer coefficients and constant term one, so their formal quotient
has integer coefficients; cohomology has already shown that it is a polynomial.

## 5. Smooth deformation and a decisive limitation

Keep Delta!=0 but now specialize to A=0, B!=0. The curve remains smooth
and elliptic. Its cubic cover is x^3=t^2-B. Over an algebraically closed
constant field its monodromy is C3, with three branch points (the two
roots of t^2=B and infinity), each having index three. The geometric
commutator of every pair of holonomies is the identity. Hence every
commutator Gram defect of the earlier type vanishes.

Nevertheless the augmentation projector P=I-J/3 still exists and (3.1)
still recovers the nontrivial rank-two elliptic cohomology. The Kummer
double cover remains branched at four points, so the degree-four Prym
construction also persists. Thus the commutator description of P in
(3.2) fails at this stratum; the source's unit/trace projector does not.

For full arithmetic monodromy to be C3, assume mu_3 is contained in k,
equivalently q=1 mod 3. If q=2 mod 3, Frobenius can act by inversion and
the full arithmetic group is S3, even though geometric monodromy is C3.
We do not assert arithmetic commutator vanishing in that case.

This is a smooth family of curves with changing branch configuration and
ramification type. It is not a deformation inside a fixed punctured
local-system category. The consequence is narrow but useful: this
particular commutator cannot be a universal detector of the family's
cohomological L-factor. A finite collection of point counts is not needed
to establish that failure.

## 6. Imported mathematics and finite verification boundary

The load-bearing external theorems are finite-pushforward/base-change,
Riemann-Hurwitz, the cohomological trace formula, Poincare duality, and the
weight theorem for smooth projective curves. Source references are:

- [Stacks, 03QN](https://stacks.math.columbia.edu/tag/03QN), finite direct
  image and base change; [Stacks, 0C1B](https://stacks.math.columbia.edu/tag/0C1B),
  Riemann-Hurwitz and tame ramification.
- [Deligne, La conjecture de Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0/),
  (1.5.4), (1.6), (1.14), (1.15), and (2.3)--(2.6): determinant, weights,
  sheaf trace formula, Frobenius convention and duality.
- [Milne, Lectures on Etale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf),
  Theorems 24.1, 27.15 and 29.6, as readable supporting references.

The conductor ledger is computed directly from tame inertia; it is a
consistency check and does not replace the genus/direct-summand argument.
No external novelty of elliptic, Kummer, Prym, or permutation-sheaf theory
is claimed. The proposed repository result is the explicit adapter and
its demonstrated boundary for the previously constructed holonomy object.

The accompanying bounded producer uses exact finite fields and primitive
curve equations. It compares direct curve counts against all stalk traces,
reconstructs the low-degree polynomials, and tests held-out extension-field
predictions and branch factors. Such controls authenticate
the finite source and conventions, not the all-field theorems above.
No floating roots, numerical eigensystems or inferred global RH evidence
will be used.
