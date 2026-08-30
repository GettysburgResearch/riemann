# An infinite global determinant from the finite-grade S3 source

This companion completes the actual finite-grade cohomology family
constructed in `S3_RAMIFICATION_AND_GRADED_FAMILY.md`. Its source is

    R_n=Sym^n(V_std) tensor Sym^n(W_perm),

on the cubic S3 cover E -> P^1 over F_Q. These R_n have polynomial
dimension growth. They are not the exponentially growing homotopy-Lie
modules M_n of the preceding analytic parent. No improvement of that
earlier operator's trace-class radius is claimed.

The construction is a Hilbert completion of the family of actual finite
cohomology groups, with a grading parameter z. It is not identified with
the cohomology of a completed infinite-rank middle-extension sheaf:
commuting those operations would require a separate theorem. The result
is a genuine infinite determinant with an initial arithmetic Euler
product, explicit meromorphic continuation, and explicit failures of
some usual finite-rank L-function axioms. Its analytic ingredients are
classical; a claim of external priority is not made.

## 1. Actual source spaces and the necessary realization choices

Keep the generic source assumptions char(F_Q)>3, A!=0, and
-4A^3-27B^2!=0. The geometric source curves are

    E: y^2=x^3+Ax+B,
    D: v^2=-4A^3-27(B-u^2)^2,

with their smooth projective models. The discriminant/Galois-closure
companion independently realizes the sign sector D and compares it with
the two elliptic quotients of the genus-two source.

Let A_n=Hom_(S3)(1,R_n), B_n=Hom_(S3)(sgn,R_n), and
C_n=Hom_(S3)(V_std,R_n). These are multiplicity spaces of specified
representations, not integers introduced as exponents first. Their
dimensions a_n,b_n,c_n are those already proved. Write their generating
series as A(w),B(w),C(w); then

    A=(F_e+3F_s+2F_c)/6,
    B=(F_e-3F_s+2F_c)/6,
    C=(F_e-F_c)/3,                                        (1.1)

where F_e=(1+2w)/(1-w)^4, F_s=(1-w^2)^(-2), F_c=(1-w^3)^(-1).
In particular a_n~n^3/12, b_n~n^3/12, c_n~n^3/6.

The finite-grade cohomological identifications are

    H^0_n=A_n,
    H^2_n=A_n tensor Q_ell(-1),
    H^1_n=(B_n tensor H^1(D)) direct_sum (C_n tensor H^1(E)). (1.2)

To discuss complex Hilbert operators, make the following choices
explicit. Choose bases in the two finite-dimensional etale Frobenius
modules and a characteristic-zero subfield K containing their finitely
many matrix entries (and pairing entries if the pairings are used).
The field they generate over Q is finitely generated, so choose an
embedding K -> C. This descends and realizes the specified finite
Frobenius modules; it does not fit a new companion matrix to their
characteristic polynomials. Choose fixed Hermitian norms on the resulting
finite complex spaces H_E,H_D. Semisimplicity is not needed below.

Use the standard permutation norm on the source W, its induced norm on
V, and the induced symmetric-tensor norms on R_n and their multiplicity
spaces. The same chosen finite norm on H_E or H_D is used in every copy.
Thus changing either finite norm or finite basis gives uniformly bounded
similarity on the completed sums. The topology and source operators are
not claimed to be canonical without these choices. Their Fredholm
determinants will be independent of them and of the chosen complex
realization, because their finite characteristic polynomials lie in Z[T].

Form the orthogonal direct sums

    H_0=direct_sum_n A_n,
    H_2=direct_sum_n A_n,
    H_1=direct_sum_n [(B_n tensor H_D) direct_sum (C_n tensor H_E)].

Let F_D,F_E be the chosen actual Frobenius maps, and define

    K_0(z)|_(A_n)=z^n I,
    K_2(z)|_(A_n)=Q z^n I,
    K_1(z)|_n=z^n[(I_(B_n) tensor F_D) direct_sum
                         (I_(C_n) tensor F_E)].           (1.3)

The n=0 block is included: a_0=1, b_0=c_0=0, and z^0=1 even at z=0.
The operator is specified from source spaces and their Frobenius maps
before any determinant product is taken.

## 2. Schatten class and a two-variable meromorphic determinant

For every 1<=p<infinity and r=|z|<1,

    ||K_0(z)||_p^p=A(r^p),
    ||K_2(z)||_p^p=Q^p A(r^p),
    ||K_1(z)||_p^p=B(r^p)||F_D||_p^p+C(r^p)||F_E||_p^p.   (2.1)

These follow by summing singular values of orthogonal copies. Hence
all three operators lie in every such Schatten class exactly for |z|<1.
At |z|=1 they are bounded but not compact; at |z|>1 they are unbounded
on the displayed direct sums. Indeed nonzero source blocks occur in
arbitrarily high grades, and Frobenius is invertible on the fixed finite
spaces. On |z|<1 each K_i is holomorphic as a trace-class-valued map,
by uniform convergence of the polynomial-growth block sums on compact
subdisks. For example

    A(r^p) ~ 1/[2p^4(1-r)^4] as r increases to 1.            (2.2)

Thus this completion has a different and explicitly explained analytic
threshold from the Lie parent; it is not its regularization.

Define

    Lcal(z,T)=det(1-TK_1(z)) /
                  [det(1-TK_0(z)) det(1-TK_2(z))].          (2.3)

The numerator and denominator are jointly holomorphic on
{|z|<1} x C_T. Their ratio is jointly meromorphic there. For every fixed
|z|<1 it is meromorphic on the whole finite T-plane. The actual source
block decomposition gives

    Lcal(z,T)=product_(n>=0)
          Z(P^1,Tz^n)^a_n P_D(Tz^n)^b_n P_E(Tz^n)^c_n,    (2.4)

normally on compact sets away from its poles. This follows from
trace-class direct sums, or directly from absolute convergence of the
tails of each determinant product. In particular Lcal(0,T)=Z(P^1,T):
discarding the grade-zero blocks would be a different completion.

The H^1 numerator zeros of grade n have radius

    |T|=Q^(-1/2)|z|^(-n),                                 (2.5)

with multiplicity 2b_n+2c_n. The denominator poles before possible
cancellation have radii |z|^(-n) and Q^(-1)|z|^(-n), each with
multiplicity a_n. Smooth-projective-curve purity supplies the radius
Q^(-1/2) in each unscaled grade. The completed object has a sequence
of circles; it does not retain a single critical circle.

## 3. All closed points and the forced grading weight

Let v be a closed point of P^1 and write f_v=deg(v). The initial Euler
product is

    product_v product_(n>=0)
       det(1-T^f_v z^(n f_v) F_v | R_n^(I_v))^(-1).         (3.1)

The exponent n f_v is required: the grade-damping scalar z^n is raised
to the closed-point Frobenius degree together with T. Weighting every
closed point by z^n alone fails extension-field compatibility.
All ramified stalks and their residual Frobenius actions are those of
the preceding S3 theorem, including the Q mod3 sign at infinity.

For |T|<1/Q and |z|=r<1, (3.1) converges absolutely in logarithm. In
fact |tr(F_v^m|R_n^I)|<=d_n, where d_n=dim R_n, because the finite
monodromy action is unitary. Therefore the absolute logarithm is at most

    F_e(r) sum_v sum_(m>=1) |T|^(m f_v)/m
       =F_e(r)[-log(1-Q|T|)-log(1-|T|)].                   (3.2)

We used sum_n d_n r^(n m f_v)<=F_e(r). This proves the legitimacy of
interchanging the two products and the logarithmic sums. The already
proved finite-grade trace formula then identifies (3.1) with (2.3).
Consequently (2.3) supplies an actual cohomological meromorphic
continuation of this initial arithmetic Euler product.

Let e_D(m)=tr(F_D^m), e_E(m)=tr(F_E^m). The exact cohomological logarithm
in its initial domain is

    log Lcal(z,T)=sum_(m>=1) T^m/m *
      [A(z^m)(1+Q^m)-B(z^m)e_D(m)-C(z^m)e_E(m)].           (3.3)

This formula preserves the full three source sectors; it is not the
invariant-Lie shortcut disproved earlier. The complete rational-point
fibre histograms of the geometric source give the same coefficient at
each extension degree m, with the finite branch and infinity stalks
included. They supply a direct source check of the grading weight.

## 4. A precise boundary for duality and functional equations

Every finite grade has the established self-dual curve factors. With
k_n=a_n-b_n-c_n,

    L_n(1/(QT))=(QT^2)^k_n L_n(T).                         (4.1)

For the first N grades, the corresponding two-variable transformation
is (T,z)->(1/(QT),1/z), with prefactor

    product_(n=0)^N (QT^2 z^(2n))^k_n.                    (4.2)

This does not give a fixed-z functional equation for the completion.
The inverse grading parameter lies outside |z|<1, and the prefactor
has no finite limiting exponents: k_n~ -n^3/6.

There is also a direct obstruction, not merely an inability to pass
this proof to a limit. If 0<|z|<Q^(-1/2), numerator zeros cannot cancel
denominator poles. A cross-grade cancellation would require
|z|^j=Q^(-1/2) for a nonzero integer j, impossible in that range.
There are therefore infinitely many poles, including T=z^(-n) with
a_n>0. Under T->1/(QT), they accumulate at T=0. Since Lcal(z,T) is
holomorphic and equals one at T=0, no identity

    Lcal(z,T)=R(T) Lcal(z,1/(QT))                          (4.3)

with nonzero rational R(T) can hold near the puncture. A rational
prefactor cannot cancel infinitely many such poles. This excludes in
particular the usual finite monomial prefactor. It does not exclude
all conceivable infinite completion factors, another grading topology,
or a different two-variable functional relation.

For the same noncancellation range, with a=-log|z|, zero and pole counts
with multiplicity have the explicit asymptotics

    N_zero(R) ~ (log R)^4/(8a^4),
    N_pole(R) ~ (log R)^4/(24a^4).                          (4.4)

Indeed sum_(n<=N)(2b_n+2c_n)~N^4/8 and
sum_(n<=N) a_n~N^4/48, and the relevant grade cutoffs are
(log R+O(1))/a. Coincident denominator poles add multiplicities and
do not change this count. Each of the entire determinants in (2.3)
has order zero as an entire function of T: polynomial grade
multiplicities and geometric spectral decay bound its maximum
logarithm by O((log(2+|T|))^5). This infinite global object is therefore
not a disguised finite-degree cohomological polynomial.

## 5. Exact finite controls and convergence beyond the initial Euler disk

Put Gcal=Lcal/Z(P^1,T), retaining only grades n>=1 in (2.4). This
explicitly removes the two known grade-zero poles rather than hiding
them in a numerical logarithm. Let r=|z| and define the exact positive
source tail

    D_N(r)=F_e(r)-sum_(n=0)^N d_n r^n.

If Q|T|r^(N+1)<1, the tail after grade N in log Gcal has absolute value
at most

    2Q|T| D_N(r)/[1-Q|T|r^(N+1)].                         (5.1)

The combined dimension of H^0_n,H^1_n,H^2_n is
2a_n+d_n-t_n=(4d_n+2r_n)/3<=2d_n. Every Frobenius eigenvalue has
absolute value at most Q, proving (5.1) directly from the determinant
logarithms, without any chosen operator norm constant.

The cohomological series for log Gcal is (3.3) with A(z^m) replaced
by A(z^m)-1. It converges already when h=Q|T|r<1. For r>0, put
C_r=(F_e(r)-1)/r. Its tail after m=M is bounded by

    2 C_r h^(M+1)/[(M+1)(1-h)].                            (5.2)

Indeed F_e(r^m)-1<=C_r r^m and the total cohomological dimension bound
above applies. Thus (5.1) and (5.2) give independent finite-grade and
finite-power enclosures of the same source determinant logarithm.

The replay obtains P_E,P_D from the frozen primitive geometric source,
checks held-out extension counts, and compares the actual fibre-sector
trace with (3.3). It then applies both bounds at rational z,T, including
T=1/2,z=1/10 for Q=5 and 7. These points lie beyond |T|<1/Q while
Q|T|z<1. All real determinant factors of grades n>=1 are positive in
these controls; the separately stated grade-zero factor can have a
negative sign and is not replaced by its absolute value.

This is an explicitly sourced infinite global analytic object, with
ramification and closed-degree coherence. Its remaining failures are
equally explicit: no single critical circle, no usual fixed-z finite
functional equation in the range proved above, and no unproved exchange
of middle extension, cohomology, and Hilbert completion.
