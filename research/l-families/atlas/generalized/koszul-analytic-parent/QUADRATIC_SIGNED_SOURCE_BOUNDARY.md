# Quadratic signed sources and the S4 diagonal-infinity completion

This companion proves a general signed version of the finite-group
grading-boundary theorem and applies it to an actual quadratic twist
of the S4 source. Its ramification cannot be copied from S3: at S4
infinity the two quadratic inertia actions coincide diagonally, leaving
nonzero twisted stalks. A vanishing first Frobenius trace there does
not make the stalk vanish.

The preceding [finite-group theorem](FINITE_GROUP_SOURCE_BOUNDARY.md)
supplies the source character and Hilbert-space constructions. The
quadratic genus-nine [S3 case](RAMIFIED_TWISTED_GLOBAL_COMPLETION.md)
is a special case of the signed argument below. As throughout these
packets, curve purity, finite-cover invariant cohomology and Poincare
duality are classical imported theorems, not consequences of bounded
point-count tests. No RH or external priority claim is made.

For precise primary references, Milne's
[Lectures on Etale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf),
Theorems 24.1, 29.4 and 29.6 give duality and the additive and
determinant trace formulas. Finite pushforward and characteristic-zero
invariant projection pass from the open-cover statement to the full
ramified source: a finite map has finite geometric fibres and no higher
direct images of the constant coefficient sheaf. The bad-point terms
are the explicit invariant stalks, not omitted Euler factors.

## 1. General signed theorem and its essential hypotheses

Let Z -> P1 be a geometrically connected constant-G Galois cover over
F_Q. Let chi be a geometric quadratic character whose double cover is
geometrically disjoint from Z. The normalized joint cover Z_tilde has
group G times C2; equivalently Z_tilde -> Z is the connected quadratic
pullback. Let V,W be nonzero finite-dimensional representations of G,
with r=dim V, s=dim W, and define

    R_n=Sym^n(V) tensor Sym^n(W),   T_n=R_n tensor chi,
    D=r+s-1,   C=binom(D-1,r-1).

The twist is applied once after forming R_n, not raised to the grade.
Assume that identity is the only element of G acting as a scalar on
both inputs. A faithful permutation input W suffices. This hypothesis
is essential to the clean signed constant below: the additional scalar
resonances of the unsigned theorem can cancel after inserting signs.

Assume also that

    a=dim H^1(Z_tilde)^-=2g(Z_tilde)-2g(Z)>0.            (1.1)

Here the superscript minus denotes the actual quadratic anti-invariant
part. Its Frobenius F is invertible and pure of weight one. Thus

    Delta_m=#Z_tilde(F_{Q^m})-#Z(F_{Q^m})=-tr(F^m)

is an integer with |Delta_m|<=a Q^{m/2}. These properties come from
the connected source curves, not from a fitted recurrence.

The condition a>0 cannot be dropped. For the cover P1_v -> P1_u
over F_5, u=v^2, with G trivial and any trivial inputs, the chi cohomology is
zero in every degree. All T_n have L-function one; the completed
function is identically one and has no natural boundary despite its
infinite formal grading.

The input hypothesis is independently necessary. In the actual S4
pair below, the regular anti-invariant rank is sixty, but choosing
both inputs to be trivial makes every R_n trivial and every T_n
equal to chi_u. Their L-functions are all one. Every group element
then acts as a scalar, and the omitted signed nonidentity terms
cancel the identity contribution. A positive regular anti-rank alone
therefore does not imply a boundary for arbitrary selected inputs.

## 2. Actual cohomology, inertia and the entire determinant

At each closed point, take the full inertia group J inside G times C2.
The twisted extended trace is its signed average

    |J|^{-1} sum_{(g,epsilon) in Fr J}
                           epsilon * tr(g|R_n).        (2.1)

One must not assume J is a product of the two inertia groups. This
is precisely the issue in the S4 infinity example below.

The central quadratic factor acts as minus identity on every T_n,
so H^0 and H^2 vanish. There are finitely many nontrivial primitive
cohomology spaces H^1(P1,j_*(rho tensor chi)). With the consistent
associated-sheaf convention these are the corresponding dual
multiplicity spaces in H^1(Z_tilde)^-. The genuine multiplicity
spaces Hom_G(rho,R_n) therefore form a source-defined Hilbert sum
H_chi with block operator z^n Frobenius. Fixed finite-dimensional
complex realizations and norms are chosen once, as before.

The identity-only scalar hypothesis gives

    multiplicity(rho,R_n)=dim(rho)d_n/|G|+O(n^{D-2}),
    dim H^1(T_n)=a*d_n/|G|+O(n^{D-2}),                (2.2)

when D>=2. For D=1 the hypothesis forces G trivial, and the same
conclusion is direct. Formula (2.2) follows from character
orthogonality and the strict nonidentity pole-order bound. The
regular anti-invariant source has total dimension
sum_rho dim(rho)*dim H^1(rho tensor chi)=a.

It follows that this actual polynomial-growth cohomology operator
K_chi(z) is in every S_p, p>0, exactly for |z|<1; at the boundary it
is bounded and noncompact, and outside it is unbounded. In particular

    L_chi(z,T)=det(1-TK_chi(z))=product_n L(T_n,Tz^n)   (2.3)

is jointly holomorphic on |z|<1 and the whole complex T-plane.
This is a Hilbert sum of finite cohomology, not an assertion that
infinite sheaf completion commutes with cohomology, and not the
exponential-growth Koszul Lie operator.

In the initial region |T|<1/Q its logarithm is the actual closed-point
Euler logarithm with weights z^{n deg v}. Summing (2.1) over all
F_{Q^m} base points gives signed weights w_m^chi(g). Their total
absolute mass is at most Q^m+1, and

    w_m^chi(1_G)=Delta_m/|G|.                          (2.4)

To prove (2.4), the character of Reg(G) tensor chi is zero unless
g=1_G, when it is |G| times epsilon. Its complete local trace is
the quadratic anti-invariant regular-source trace. Globally this
is #Z_tilde-#Z, because the anti-invariant H^0 and H^2 vanish.
This proof includes ramified points with nonproduct inertia.

## 3. The signed natural boundary for every real 0<T<1/Q

Fix such a real T. At any root of unity zeta of exact order h,
the strict nonidentity pole-order bound and dominated convergence
give

    lim_{r->1-}(1-r)^D log L_chi(r*zeta,T)
      = (C/|G|) sum_{h divides m} Delta_m T^m/m^{D+1}.
                                                              (3.1)

The majorant is the same as in the unsigned theorem: absolute
averaging mass at most Q^m+1, character modulus bounded by F_e,
and bounded (1-r)^D F_e(r). The limit may be negative or zero.

There are infinitely many h with Delta_h nonzero. Otherwise the
invertible rank-a Frobenius characteristic recurrence, whose constant
term is nonzero, propagates eventual zero power traces backwards to
the zeroth trace a=0, contradicting (1.1). For such h, factor the
right side of (3.1) as

    C T^h/(|G| h^{D+1}) * (Delta_h+E_h),
    |E_h| <= a (QT)^h/[1-(sqrt(Q)T)^h] -> 0.            (3.2)

The estimate drops the denominator j^{D+1} in the j>=2 terms and
sums their geometric weight bound. Since Delta_h is a nonzero
integer, |Delta_h|>=1. Thus for every sufficiently large h in the
unbounded nonzero subsequence, the limit in (3.1) is nonzero and has
the sign of Delta_h.

Primitive h-th roots are dense along any unbounded sequence of
orders. In an angular interval of normalized length ell>0 their
number is ell*phi(h)+O(2^{omega(h)}). The elementary bounds
phi(h)>=sqrt(h/2) and 2^{omega(h)}<=64h^{1/4} make this positive
for all sufficiently large h. The bounds and inclusion-exclusion
proof were given in the S3 companion and do not require prime orders.

A positive limiting constant forces growth faster than a pole;
a negative one forces decay faster than a finite-order zero. Both
contradict a nonzero meromorphic germ. The obstructed primitive roots
are dense, hence |z|=1 is a meromorphic natural boundary of (2.3).
The theorem asserts neither positivity nor nonzero constants at every
root, and it does not assert a boundary for arbitrary complex T.

## 4. S4 and the coincident quadratic inertia at infinity

Return to the actual Bring-quartic cover of the preceding packet:

    E:y^2=f(x)=x^4+b x+c,   u=y,
    b!=0, 256c^3-27b^4!=0, p>3.

Let chi=chi_u and let Z be its genus-nineteen S4 closure. The S4
source is unramified at 0, whereas chi ramifies there, so the two
covers are geometrically disjoint. In Z, u has twenty-four simple
zeros over 0 and poles of order two at its twelve geometric points
over infinity. Thus Z_tilde=Z(sqrt(u)) ramifies at the former points
only. Riemann-Hurwitz gives

    g(Z_tilde)=2*19-1+24/2=49,
    dim H^1(Z_tilde)^-=98-38=60.                       (4.1)

At each of the six old finite branches the twisted trace is chi(u_v)
times the frozen S4 invariant trace. At 0 all twisted stalks vanish.
At infinity, however, joint inertia is the **diagonal** group

    J=< (d,-1) >,    d a double transposition.

The invariant twisted space is the minus-one eigenspace of d on
the original representation. For the five irreducibles ordered
1,sign,two,std,tw, its dimensions are (0,0,0,2,2).
For Q=1 modulo 4 Frobenius acts as identity there; for Q=3 modulo 4
the std and tw eigenvalues are 1,-1. Their local denominator is

    (1-T)(1-chi_Q(-1)T).                              (4.2)

In particular first trace zero at Q=3 modulo 4 is not a zero stalk:
the second trace is two and the denominator is 1-T^2.

One way to see the residual action is to choose the leading quartic
roots +/-sqrt(u), +/-i sqrt(u). Frobenius is identity modulo inertia
when i is rational, and a single transposition when it conjugates i.
Its product with d is the other transposition. The signed inertia
average is therefore (chi_rho(g)-chi_rho(gd))/2. The scalar square
root of u is already in the local S4 splitting field; adjoining it
globally does not double the local inertia at infinity.

For any R_n, writing d_n=dim R_n, s_n=tr(trans|R_n), and
q_n=tr(double-trans|R_n), the twisted infinity dimension is
(d_n-q_n)/2. At Q=1 modulo 4 its local denominator is
(1-T)^{(d_n-q_n)/2}; at Q=3 modulo 4 it is
(1-T^2)^{(d_n-q_n)/4}. The latter exponent is integral because
the two Frobenius eigenspaces have equal dimension. The full graded
infinity trace is (F_e-F_d)/2 in the former case and zero in the
latter; all Frobenius powers, not just the first, specify the factor.

## 5. Actual finite twisted cohomology and the entire S4 family

For an irreducible of dimension d and character values s at a
transposition and q at a double transposition, the conductor is

    3(d-s)+d+(d+q)/2.

The three terms come from the six old branches, the new point 0,
and diagonal infinity. Since H^0 and H^2 vanish, subtracting 2d
gives the twisted H^1 dimensions

    (0,6,6,4,10) for (1,sign,two,std,tw).              (5.1)

These are also realized by explicit quotient curves. Let
g(x)=-16x^6-40b x^3-27b^2 and let C:y^2=f(x),v^2=g(x),
the frozen genus-seven quotient. The twisted sources are

    D_chi:s^2=u[256(c-u^2)^3-27b^4],       genus 3;
    X:w^4=f(x),                            genus 3;
    R_chi:4z t^4=-z^3+4cz+b^2,            genus 4;
    C_chi:w^4=f(x),v^2=g(x),              genus 17.

All curves mean their smooth projective normalizations. X -> E
has anti-invariant rank four. R_chi maps to the frozen genus-one
resolvent R by u=t^2, with anti-invariant rank six. The latter
Kummer degree-four map to P1_z has three simple zero valuations,
a simple pole at 0 and a pole of order two at infinity, proving
its genus four. C_chi -> C ramifies at its eight points over u=0,
giving genus seventeen and anti-invariant rank twenty.

Write P_signchi=P_Dchi, P_stdchi=P_X/P_E,
P_twochi=P_Rchi/P_R. The actual twisted multiplicity space for tw
has rank ten, and

    P_Cchi/P_C = P_signchi P_stdchi P_twchi.             (5.2)

This constructs the last polynomial from cohomological summands;
formal division of arbitrary polynomials is not the existence proof.
The regular anti-invariant factor is

    P_Ztilde/P_Z=P_signchi P_twochi^2
                          P_stdchi^3 P_twchi^3,         (5.3)

of degree 6+12+12+30=60, matching (4.1).

Use the genuine S4 source multiplicities m_{rho,n} already proved
in the preceding companion. Then

    L(R_n tensor chi,T)=P_signchi(T)^{m_sign,n}
       P_twochi(T)^{m_two,n} P_stdchi(T)^{m_std,n}
       P_twchi(T)^{m_tw,n}.                            (5.4)

Its H^1 dimension is

    h_n=6m_sign,n+6m_two,n+4m_std,n+10m_tw,n
       =(5d_n-6s_n+q_n)/2.                            (5.5)

The completed ordinary determinant is the product of (5.4) at
Tz^n, entire in T for |z|<1, with grade-zero factor one. Its
zeros have radii Q^{-1/2}|z|^{-n}, so no finite rational prefactor
can supply a fixed-z reciprocal functional equation: reciprocal
zeros would accumulate at T=0, where the determinant equals one.
Again this does not exclude arbitrary alternative infinite completions.

By the general signed theorem the grading natural boundary holds
for every real 0<T<1/Q, with radial constants

    (5/12) sum_{h divides m}
       [#Z_tilde(F_{Q^m})-#Z(F_{Q^m})] T^m/m^7.         (5.6)

They can have either sign or vanish. No argument from positive
untwisted counts is being reused without the signed-trace proof.

For finite grade cutoff, set kappa_n=h_n/2. The source duality
prefactor is Q^{K_N}T^{2K_N}z^{2W_N}, where

    K_N=sum kappa_n ~ 5N^6/288,
    W_N=sum n*kappa_n ~ 5N^7/336.                      (5.7)

Here m_{rho,n}=dim(rho)d_n/24+O(n^3), d_n~n^5/12,
so kappa_n~5n^5/48. Grade zero contributes zero, in contrast to
the untwisted principal factor. These divergent native exponents
and opposite trace-class domains prevent a direct ordinary limit
of the finite duality prefactor.

## 6. Source and replay boundary

The separate [geometric packet](../global-s4-resolvent/QUADRATIC_TWIST_SOURCE_AND_DIAGONAL_INERTIA.md)
owns the explicit quotient-curve
construction and primitive reconstruction of the degree-ten tw-chi
polynomial. The analytic adapter authenticates its frozen proof,
runtime and artifact before using those finite Frobenius modules.
Any reused extension counts or reciprocity-supplied coefficients are
identified explicitly. A first-trace-zero infinity test must retain
the second Frobenius power and denominator (4.2).

The bounded replay does not prove density, eventual nonzero traces,
or purity by sampling. Those are mathematical consequences of the
actual source and the proofs above. The signed completion remains
distinct from both the positive untwisted object and the exponential
Lie parent.

For the exact analytic controls let F_e(z)=(1+6z+3z^2)/(1-z)^6,
0<r<1, T>=0, and QTr<1. The conservative estimate h_n<=6d_n
follows directly from (5.5) and the character bounds |s_n|,|q_n|<=d_n.
The finite grade-product logarithm tail after N is at most

    6QT [F_e(r)-sum_{n=0}^N d_n r^n]
                           /[1-QT r^{N+1}].           (6.1)

Writing h=QTr and C_r=(F_e(r)-1)/r, the power-log tail after M
is at most

    6 C_r h^{M+1}/[(M+1)(1-h)].                        (6.2)

These estimates use the actual grade-zero vanishing for chi_u.
They permit ordinary determinant controls beyond the initial Euler
T disk, for example T=1/2,r=1/10. Rational logarithm enclosures for
finite positive determinant values are bounded separately from both
infinite tails. With only a degree-four prefix of a degree-ten
polynomial, higher traces and a full completed determinant are not
available; the corresponding p7 panel remains a partial source.

For (5.6), the conservative rank-sixty bound |Delta_m|<=60Q^m
gives the signed constant tail after M

    25(QT)^{M+1}/[(M+1)^7(1-QT)].                      (6.3)

It makes no assumption about the sign of any primitive difference.
