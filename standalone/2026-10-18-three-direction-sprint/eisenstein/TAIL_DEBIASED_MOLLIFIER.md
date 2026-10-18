# A legal tail counterterm kills the primitive theta mean without killing the unit detector

**PROPOSED exact construction with source-qualified analytic consequences.**
The construction and its unit gate are elementary. The cheap joint norm
uses the precise zero-slot TWO-PLAIN theorem of the pinned original
Eisenstein source; it is not inferred from the elementary U+N^2 mean.
Its application to a primitive sextic residue uses the separately stated
averaged Type-I theorem in rStation paper 8. Neither whole imported proof
is independently validated here. The full mixed moment remains open.

## 1. Two independent linear responses

Work over E=Q(omega), outside the same fixed finite S. Set

    v(a)=product_(p|a) Q^2/(Q^2+Q-1), Q=Np.

This positive multiplicative function is needed only on squarefree a.
Choose a fixed smooth cutoff V equal to one on [0,1] and zero on [2,infty),
and a nonzero nonnegative smooth W supported in (2,3). For D>=1 put

    A_D=sum_a mu(a) V(Na/D) v(a)/(Na),
    B_D=sum_a mu(a)^2 W(Na/D)/(Na),
    c_D=-A_D/B_D,                                           (1)

whenever B_D>0. Fixed-field squarefree ideal density gives B_D bounded
above and below by positive constants for sufficiently large D. Trivial
ideal counting gives |A_D|=O(log(2D)), hence c_D=O(log(2D)). No Mobius
cancellation estimate is required for this bound.

Define the finite mollifier coefficients

    b_D(a)=mu(a)V(Na/D)
             +c_D mu(a)^2 v(a)^(-1)W(Na/D).                 (2)

They are squarefree-supported and bounded by O(log(2D)^2). Indeed
`v(a)^(-1)<=product_(p|a)(1+1/Q)=sum_(d|rad(a))1/Nd`
is O(log(2Na)) by the fixed-field ideal count. The product v(a)^(-1)
is not uniformly bounded; its individual factors cannot be replaced by
one constant independent of the number of primes. Every original
S deletion remains. By construction

    b_D(a)=mu(a) for Na<=D,
    b_D(1)=1,
    sum_a b_D(a)v(a)/(Na)=0.                               (3)

Thus unit response and the proposed nuisance functional are linearly
independent. The tail vector has zero unit response and strictly positive
nuisance response B_D. The coefficient c_D is affordable; it is not an
inverse of a possibly tiny oscillatory sum.

## 2. Exact zero retention and the completed prefix gate

For ANY original finite-order row character psi, including its displayed
zero extensions, let

    C_D(s,psi)=sum_a b_D(a)psi(a)(Na)^(-s).

It is a finite Dirichlet polynomial. At every zero rho of the original
entire nonprincipal L(s,psi),

    L(rho,psi) C_D(rho,psi)=0.                              (4)

For Nn<=D, all its divisors have norm <=D, so (3) gives exactly

    sum_(a|n)b_D(a)=sum_(a|n)mu(a)=1_(n=1).                (5)

The new term occurs only at Na>2D and does not alter a single low-product
coefficient. Consequently the native Gamma-integral detector proof
retains its unit contribution and its exact low-product cancellation.
The same finite profile cutoffs may be used. On its shifted contour the
mollifier has the same fixed polynomial bound as the old one, with an
extra logarithm, so the deliberately large smoothing horizon still makes
the shifted integral o(1).

For precision, at the native D=U^t, 1<=t<=3/2, and Y=U^20 the exact
legal observable before witness selection is

    J_psi(rho)=1/(2pi i) integral_(2)
       Y^z Gamma(z)L_orig(rho+z,psi)C_D(rho+z,psi) dz
      =sum_(a,n)b_D(a)psi(an)(Na Nn)^(-rho)exp(-Na Nn/Y). (5a)

Move to Re z=-1/4. The residue at z=0 vanishes by (4). The new finite
mollifier has coefficients O(log(2D)^2), support <=3D and therefore the same
trivial shifted-strip bound as the original mollifier up to logarithms.
The source's intentionally coarse L bound gives
`J_psi(rho)<<U^[-3+t(5/4-Re rho)+o(1)]`, which is o(1) uniformly for
Re rho>=51/100 and t<=3/2. This uses precisely the original detector's
fixed polynomial height hypotheses.

Insert the PRODUCT cutoff `1-V(2Na Nn/D)`. By (5) this removes exactly
the unit contribution exp(-1/Y), and nothing else with a nonzero
coefficient. Thus the resulting complete tail is -1+o(1). A terminal
PRODUCT cutoff equal to one below U^21 and zero beyond 2U^21 changes it
by o(1), using exponential decay and the divisor bound on b_D*1.
These are the same contour and terminal estimates as the source, with
only a fixed support enlargement and logarithmic coefficient loss.

Partitioning only the product A=an into annuli gives O(log U) exact
pieces with column coefficient `sum_(a|A)b_D(a)` and ONE norm profile
`W_(X,rho)(NA/X)`. In particular the full Re rho and Im rho dependence
stays in that product profile, not in the outer coefficients b_D(a).
This is the legal global observable to which Section 4 applies.

After the alternative common a/n profile separation, it also produces
a large matched M_b(D')S(N) witness. The support may enlarge the old maximum inverse
length by a fixed factor three, hence only O(1/log U) in exponent.
No independently differentiated L-function or division by an L-value is
introduced. Every hypothetical target zero remains visible.

## 3. Why the positive squarefree tail is actually cheap

Let w_p=v(p)^(-1)=1+Q^(-1)-Q^(-2). For a multiplicative zero-extended psi,
put X_p=psi(p)Q^(-s). In an initial absolute half-plane,

    sum_a mu(a)^2 v(a)^(-1)psi(a)(Na)^(-s)
       = L(s,psi)/L(2s,psi^2) * R(s,psi),                  (6)

where

    R_p=(1+w_p X_p)/(1+X_p)
        =1+(w_p-1)X_p/(1+X_p).                            (7)

Write R(s,psi)=sum_b r(b)psi(b)(Nb)^(-s); the coefficients r(b) are
independent of the row. At the central normalization

    sum_b |r(b)|/(Nb)^(1/2)<infty,                         (8)

because the local defect in its absolute Dirichlet algebra is at most

    (Q^(-1)-Q^(-2))Q^(-1/2)/(1-Q^(-1/2))=O(Q^(-3/2)).

All formulas remain exact when psi(p)=0. In particular no imprimitive
zero mask is inverted.

For the annular tail polynomial

    T_psi(D)=D^(-1/2)sum_a mu(a)^2 v(a)^(-1)psi(a)W(Na/D),

coefficient convolution in (6) gives the EXACT finite-at-each-scale form

    T_psi(D)=sum_(h,b)
       mu(h)r(b)psi(h^2 b)/[Nh sqrt(Nb)]
         S_psi(D/[(Nh)^2 Nb];W).                          (9)

Terms below the smallest nonempty annular scale vanish. Thus h is at
most a fixed multiple of sqrt(D), and (8) makes the full coefficient
mass O(log(2D)). The h,b may share all their primes with each other,
the remaining plain index and the row. Their zero extensions multiply
in (9), so shared nonunits still vanish.

Here is the EXACT analytic import. The original source's `lem:plain`,
around lines 12524--12561 of `_source-original-quasi.tex`, states

    sum_(k in R_0) |S_(psi_k)(n1;W1)S_(psi_k)(n2;W2)|^2
                     << U^(1+epsilon)                    (10)

in its zero-slot case, with NO restriction on bounded nonnegative
lengths n1,n2 and NO lower conductor bound. The row family R_0 consists
of nonprincipal inducing characters; fixed twists, common masks and
separated smooth height parameters have its stated uniformity.
Large good sixth-power-free physical rows induce nonprincipal characters,
so they belong to this family. The finite exceptional rows remain in the
native small-row treatment.

Apply Minkowski to (9) times the SAME plain S_psi(N). The factor
psi(h^2b) has modulus at most one and is removed after taking the row norm;
all retained plain factors keep the same original psi. Equations
(8)--(10) imply, for D,N in any prescribed bounded polynomial range,

    sum_(u physical) |T_(psi_u)(D) S_(psi_u)(N)|^2
       << U^(1+epsilon)log(2D)^2 (1+T)^A.                  (11)

Multiplication by c_D costs only more logarithms. This is where the
unrestricted TWO-PLAIN input matters. Replacing it by the elementary
single-plain U+D^2 estimate would NOT prove (11).

The same decomposition and the source's pointwise plain estimates show
`|T_psi(U^r)|^2<<U^(delta r+epsilon)` in the native buffered bins:
every rescaled plain length has exponent r'<=r and its bound
`delta min(r',1-r')` is no larger than delta r. Therefore the modified
inverse has the same inverse-type pointwise upper exponent and the
native witness argument forcing m<=1/2 is not lost. Its unmarked second
moment is also no worse than the existing amplified inverse moment plus
a row-size term from (11), with a fixed unit-scale second plain factor.

## 4. Which actual primitive nuisance is canceled

The primary statement of
[rStation paper 8, version 1, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/8)
has, for squarefree outer coefficients alpha_a, a primitive sextic residue
mean whose leading term is a fixed scalar times

    X^(5/6) What(5/6) sum_a alpha_a v(a)/(Na).              (12)

Its plain factor is unrestricted. Summing the finitely many dyadic pieces
of the global coefficient (2), while retaining ONE product-scale kernel,
makes the leading functional in (12) vanish EXACTLY by (3).
Fixed common finite ray twists act on the WHOLE product A; expand them
as the fixed numerator ray restrictions explicitly permitted by that
Type-I theorem. They do not insert a new twist in the outer functional.

For the lowest product annuli X≈D the outer support reaches 3D, whereas
the theorem states A_outer<=X. Choose instead X'=max(X,3D), changing
its product profile to `W'(y)=W(X'y/X)`. The product-tail support ensures
X>=cD for a fixed c>0, so X'/X is bounded. All profile seminorms remain
uniform and
`(X')^(5/6) What'(5/6)=X^(5/6) What(5/6)` exactly. The theorem therefore
applies to EVERY outer dyad, with the same polar prefactor, and no tail
of the canceling functional is omitted. Its error still has size (13).

It is essential to perform this cancellation before splitting the plain
variable into separate dyads. A separately imposed plain-variable cutoff
creates a Mellin family of different functionals and is not killed by one
scalar c_D.

The theorem's complete error, summed over the outer dyads Na<=3D, is

    O_epsilon(X^(1/3)D^(2/3)(DX)^epsilon),                 (13)

since ||alpha||_2 on a dyad A is O(A^(1/2)log(2D)^2). No sign cancellation of
mu is used. If this residue pairing enters an adjoint Gauss image with
its native factor U^(1/6)X^(-1/2), its squared error cost becomes

    U^(1/3)X^(-1/3)D^(4/3)(UDX)^epsilon.                  (14)

At D=U, X=U^(3/2) this is U^(7/6+epsilon). For the COMPLETE global
detector, however, X ranges from a fixed multiple of D to U^21. The
worst bound (14) at X≈D is U^(1/3)D, or U^(4/3) when D=U. Thus the
representative corner is not a complete global improving estimate. The leading polar term has
been removed without changing the low-product detector or paying a long
positive-tail mixed moment. This is an actual correlated arithmetic
counterterm, conditional on the stated Type-I theorem.

## 5. Remaining gates

The exact rank-two construction (1)--(5) and the Euler identity (6)--(9)
are independent of an unknown theta coefficient formula. The analytic
consequences (11) and (13) use the two named source inputs with their
precise scopes.

The cheap correction (11) means that a uniform-U mixed estimate for the
modified mollifier is EQUIVALENT, up to a row-size error and subpowers,
to that estimate for the original mollifier: use the triangle inequality
in both directions. The construction changes the useful arithmetic
representation; it does not prove an easier norm bound by itself.

The continuous primitive Kubota family is not the residue functional
(12). Growing numerator labels and the complete complementary row space
also remain. No theorem here says that killing this one global polar
mean controls the full mixed moment or the whole row operator. In
particular (14) alone does not establish the open uniform-U input in
MIXED_CONSUMER.md. No new zeta boundary is claimed.

## 6. Pinned comparison source and finite replay

The primary comparison statement was read directly and downloaded from
`https://rstation.ai/api/v1/papers/riemann_hypothesis_8/versions/1/download`.
Its local ignored copy `rstation-8-v1.md` has SHA256
`f1f9aed624908ccb9b6842911d898916230545ff76dc123187d7eadc3558def1`.
The raw source is a scoped analytic input, not a repository acceptance.

`tail_mollifier_check.py` passes both normal and optimized Python. It
reconstructs all 117 exterior integral ideals through norm 384 by HNF,
uses exact ideal Mobius signs, and checks three complete rational-profile
counterterms at D=32,64,128. All 67 low-product unit gates and exact zero
nuisance responses pass. Three missing-inverse-v mutations are rejected.
It also checks 238 exact local prime-power convolution coefficients.
The finite profiles have only the stated finite differentiability; their
purpose is exact coefficient algebra, while the analytic statement uses
smooth profiles with those same support/prefix conditions. No analytic
mean or asymptotic theta estimate is inferred from these fixtures.
