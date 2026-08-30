# Higher Kummer twists: ramification resonance and paired duality

Status: proposed exact theorem extending the frozen quadratic adapter
`23ad35cc8010f72cf1df54f09eccb4dcba108879` without changing it.
Scope: smooth projective function-field sources; no integer-source or
number-field RH claim. The geometry is classical; external priority is not claimed.

The quadratic twist has a self-dual rank-four cohomological factor. Higher
twists expose two distinct boundaries to that description: an order-three
twist gains an invariant line at infinity, and a nonreal twist is paired with
its inverse character rather than with itself.

## 1. Primitive source, coefficients and character convention

Let k=F_q have characteristic p, let m>=2 with p not dividing 6m, and assume
q=1 modulo m. Choose A,B in k with A!=0 and
Delta=-4A^3-27B^2 !=0. Keep the cubic map

    E: y^2=x^3+Ax+B -> P1_t,  t=y,

and form the smooth projective model

    C_m: w^(2m)=x^3+Ax+B,    h:C_m->E, y=w^m.

We use Q_ell(zeta_m) coefficients, with ell not dividing pm, and choose a
primitive m-th root eta in k and its coefficient-field image zeta_m. Label
the Kummer summands so that their geometric-Frobenius stalk traces are

    chi_j(t) = iota(t^((q-1)/m))^j,  j=0,...,m-1,

at nonzero k-rational t; here iota(eta)=zeta_m. Over F_(q^n), use the norm
to F_q before evaluating this character. At t=0 the nontrivial Kummer
middle extensions have trace zero.

This agrees with the pullback convention for the deck map
sigma:w->eta*w: on a fibre, the function taking eta^r*w0 to zeta_m^(jr)
has sigma-pullback eigenvalue zeta_m^j and geometric-Frobenius eigenvalue
chi_j(t). Arithmetic Frobenius on geometric points is inverted when it
acts on the corresponding sheaf representation. Replacing eta and zeta_m
by their inverses relabels j and -j everywhere, without changing a theorem.

Let W be the standard augmentation local system from the cubic cover, as
in the frozen packet. Write V_j=j_*(W tensor chi_j), including every
inertia-invariant stalk. The constant j=0 summand is the old elliptic one.

## 2. Global source and exact character dimensions

Set d=gcd(m,3), so d is one or three. At a simple zero of y the polynomial
W^m-y is Eisenstein for its discrete valuation. It is therefore irreducible
even for composite m, proving that h is connected of degree m. At the three
zeros of y it is totally ramified; over infinity it has d geometric points
with ramification index m/d. Tame Riemann-Hurwitz therefore gives

    2g(C_m)-2 = 3(m-1)+(m-d),
    g(C_m) = 2m-(1+d)/2.                                    (KT-1)

On the common unramified open, finite pushforward of the fibre product is

    direct_sum_(j=0)^(m-1) (chi_j direct_sum W tensor chi_j).

The normalization C_m supplies the extension by inertia invariants. Each
nontrivial chi_j by itself has global L-factor one: the full cyclic cover
P1_w->P1_t is again P1, and every nontrivial character summand has zero
cohomology. Consequently

    L(P1,V_j,T)=det(1-TF | H1(C_m)_j),
    P_(C_m)(T)=product_(j=0)^(m-1) P_j(T),   P_0=P_E.         (KT-2)

H0 and H2 occur only in the trivial deck character on C_m. Together with
the constant-base splitting for j=0, this shows that all V_j have vanishing
H0 and H2; no fitted polynomial quotient is being used.

Here is a source-geometric proof of the individual H1 dimensions. For a
nonidentity sigma^a, its affine fixed points are exactly the three points
w=0. At infinity the local leading ratio

    nu = w^(2m/d)/x^(3/d)

takes the d-th roots of unity. The deck map sigma^a multiplies nu by
zeta_d^(2a). Since d is one or three, all d points at infinity are fixed
exactly when d divides a; otherwise none is fixed. Tame fixed points have
Lefschetz multiplicity one. The finite-automorphism Lefschetz formula gives

    tr(sigma^a|H1(C_m)) = -1-d*1_(d divides a),   1<=a<m,
    tr(1|H1(C_m)) = 4m-1-d.

Taking the finite character Fourier transform yields

    dim H1(C_m)_0 = 2,
    dim H1(C_m)_j = 4 - 1_((m/d) divides j),  1<=j<m.        (KT-3)

Indeed, for j nonzero the sum of zeta_m^(-ja) over a=1,...,m-1 is -1,
and the sum restricted to d|a is
`(m/d)*1_((m/d)|j)-1`. Substitution gives (KT-3).
Thus a nontrivial twist has degree three precisely when its character has
order three; every other nontrivial twist has degree four. Summing the
dimensions recovers (KT-1), independently of the local conductor count.

The imported fixed-point theorem is classical. A primary account of the
tame equivariant Euler characteristic, including its constant-sheaf case,
is Kock, [Computing the equivariant Euler characteristic of Zariski and
etale sheaves on curves](https://arxiv.org/pdf/math/0104212), Theorem 2.1,
Remark 2.2(b), and the fixed-point proof. We apply its usual characteristic-zero
ell-adic version; the displayed finite Fourier evaluation is derived here.

## 3. Complete ramification ledger, including infinity's new factor

For j nonzero, put h_j=m/gcd(m,j), its character order.

| place | invariant dimension for W tensor chi_j | tame drop |
|---|---|---|
| zero | 0 | 2 |
| each of the four old finite branch points | 1 | 1 |
| infinity, h_j != 3 | 0 | 2 |
| infinity, h_j = 3 | 1 | 1 |

At an old finite branch v the Frobenius eigenvalue on its invariant line
is chi_j(t_v), evaluated in its actual residue field. At an unramified
place, replace z by chi_j(t_v)*z in the three standard denominators of the
frozen cubic source. At zero the factor is one.

The drop at infinity is a real resonance. The standard cubic inertia
eigenvalues are the two nontrivial cube roots of unity. Multiplying them
by the scalar Kummer inertia leaves a fixed vector exactly when that
scalar has order three.

More than the dimension is determined here. If d=3, all three points of
C_m over infinity are k-rational: their leading ratios nu are the cube
roots of one, and mu_3 is in k. Frobenius acts trivially on their permutation
space. Its nontrivial deck characters are exactly the two order-three
characters. Thus for h_j=3 the missing local factor is exactly

    (1-T)^(-1),                                             (KT-4)

and its extension-field stalk trace is +1 for every extension degree.
For every other nontrivial j the infinity factor is one. In particular,
using only affine character sums misses one in each power-trace sum for
the order-three factors and gives the wrong global polynomial: dropping
the factor (1-T)^(-1) replaces P_j(T) by (1-T)P_j(T), falsely restoring
degree four. The replay detects this exact extra linear factor.

The conductor total is 8 outside the order-three resonance and 7 at it.
The tame middle-extension Euler formula `chi=2*rank-sum(tame drops)`
then agrees with the degree-four/degree-three conclusion. This is a second
check; the fixed-point proof already establishes the dimensions. A readable
primary statement of this Euler formula is Hall--Keating--Roditty-Gershon,
[Variance of arithmetic sums and L-functions in Fq[t]](https://research-information.bris.ac.uk/ws/files/167837089/main_6.pdf),
Appendix B, Proposition B.1.1, with Swan terms zero here.

## 4. Paired functional equations; no imposed individual self-duality

Because q=1 modulo m, Frobenius preserves each deck character space. The
cup product pairs H_j with H_(-j), and is zero between H_j and H_k unless
j+k=0 modulo m. Nondegeneracy of the full pairing gives a perfect pairing
between the paired spaces. If r_j is their common dimension and

    c_j = coefficient of T^r_j in P_j(T) = (-1)^r_j det(F|H_j),

then the exact paired equations are

    P_j(T) = c_j T^r_j P_(-j)(1/(qT)),
    c_j*c_(-j) = q^r_j.                                    (KT-5)

To verify the normalization, pair an eigenvalue alpha on H_j with q/alpha
on H_(-j), multiply the corresponding linear factors, and collect the
leading coefficient. This proves (KT-5), including its sign, without
choosing square roots of q.

The curve weight theorem gives |alpha|=sqrt(q) on every summand, so
|c_j|=q^(r_j/2). This is an imported arithmetic theorem, not a consequence
of the finite Gram projector. In fact P_j lies in Z[zeta_m][T]. Every
finite-order character Euler factor has coefficients in Z[zeta_m], so its
formal product does too; cohomology has already proved it is a polynomial.
This identifies the coefficient field and integrality without attributing
either assertion to the finite-order projector alone.

For the quadratic character, j=-j and r_j=4; the alternating cup product
on that same space recovers c_j=q^2 and the old self-reciprocity. For a
nonreal character, (KT-5) pairs two generally different polynomials. No
individual reciprocal identity or real coefficients are imposed.

When order(chi_j)=3, r_j=3. An alternating perfect pairing on the same
three-dimensional space would be impossible. The inverse-character pair
has total dimension six, as the actual cup-product geometry requires.
Accidental coincidences of characteristic polynomials are not ruled out
by this dimension statement; a proposed universal self-dual source would
still have to supply a different pairing and cannot use this one.

## 5. Bounded exact replay and boundaries

The companion replay uses the already frozen finite-field model and exact
cyclotomic arithmetic. It forms multiplicative characters by norm from
extension fields, counts every affine fibre, includes the infinity term
(KT-4), and reconstructs P_j by Newton identities in the coefficient ring.
It compares the product of the character factors with complete point counts
of C_m and checks the paired equation (KT-5).

The declared six panels cover cubic and sextic twists over F7 and quartic
twists over F5, each with (A,B)=(1,1) and (-1,0). The degree-three factors admit an extra held-out fourth
extension within the existing 2401-element field cap. Wrongly dropping
infinity or imposing an individual self-reciprocity are explicit negative
controls. All 24 declared fields and 12 tests pass in ordinary and optimized
Python. The finite checks authenticate source conventions and local
factors; neither the all-m dimension theorem nor the imported weight
theorem is inferred from them.

For example, over F7 with A=B=1 and m=3, write zeta^2+zeta+1=0. The two
nontrivial factors are

    1+(1-2zeta)T+(5+8zeta)T^2+(21+14zeta)T^3,
    1+(3+2zeta)T+(-3-8zeta)T^2+(7-14zeta)T^3.

They are conjugate and satisfy (KT-5), with leading-coefficient product
343. Neither is individually self-reciprocal. Their fourth extension-field
traces are independently predicted by these cubic polynomials.

The assumption q=1 modulo m is substantive. Without it, Frobenius permutes
the character spaces and the individual P_j need not be defined over the
base field as Frobenius-stable factors. That descent problem is outside
the current statement, rather than silently absorbed into a scalar twist.
