# Gaussian pole calibration, multiplicity, and the correct energy target

Status: proposed component theorem with a complete written proof. This is a
calibration and an obstruction, not an upper bound for the native arithmetic
energy or a proof of RH. Classical weak-Mertens and Laplace/Gram arguments
are credited in Section 8; no global novelty claim is made.

## 1. Exact source and all normalizations

Fix a number field F and a finite set S of its prime ideals. Write

    Z_F(s) = zeta_F^S(s)
           = zeta_F(s) product_(p in S)(1-(Np)^(-s)).

Let mu_F^S(I) be the ordinary ideal Mobius function on ideals prime to S,
extended by zero otherwise. Distinct ideals of equal norm stay distinct.
For a Gaussian width a>0 and a separately fixed real height t, define

    g_a(y) = exp(-y^2/(4a))/sqrt(4 pi a),
    G_(a,t)(x) = sum_I mu_F^S(I) (NI)^(-1/2-it)
                         g_a(x-log NI),
    E_(a,t)(L) = integral_(-infinity)^L |G_(a,t)(x)|^2 dx.       (1.1)

The sign of the twist is intentional. The older packets use coefficients
(NI)^(+it); their twist parameter equals minus the t used here. In the
physical norm horizon D, the critical energy is E_(a,t)(log D).

Ideal counting I_F(T)=O_F(T) gives absolute convergence of (1.1), including
all derivatives on compact x intervals. It gives G_(a,t)(x)=O_(F,a)(e^(x/2))
as x tends to +infinity. As x tends to -infinity it gives Gaussian decay,
uniformly in t. For example, when x<-a-1, factor exp(-x^2/(4a)) from the
summand and dominate the remaining ideal sum by a convergent zeta series.
These facts justify all the initial interchanges below; they make the
negative half-line Laplace transform entire.

On Re z>1/2 one has the literal bilateral Laplace identity

    integral_R G_(a,t)(x) exp(-z x) dx
         = exp(a z^2)/Z_F(1/2+z+it).                         (1.2)

Indeed, the integral of g_a(x-log NI) exp(-z x) equals
(NI)^(-z) exp(a z^2), and the resulting ideal series converges absolutely.
No line has been shifted through unknown zeros.

The original Gaussian in #952 is

    W_c(y) = y^(-c) exp(-(log y)^2/4)/(2 sqrt(pi)).

If A_(c,t)(X)=sum_I mu_F^S(I)(NI)^(-it)W_c(NI/X), then

    e^(-x/2) A_(c,t)(e^x)
       = exp((c-1/2)^2) G_(1,t)(x-2(c-1/2)),
    integral_0^D |A_(c,t)(X)|^2 dX/X^2
       = exp(2(c-1/2)^2) E_(1,t)(log D-2(c-1/2)).          (1.3)

Thus c=5/6 costs the exact fixed shift 2/3 and the squared-energy factor
exp(2/9). This is an identity, with the full small-scale Gaussian tail.

## 2. A finite Gram inequality with no zero-spacing premise

This elementary lemma is stated separately so that the analytic result does
not depend on a formal, possibly nonconvergent sum over all zeros.

Let h on [0,infinity) have Laplace transform H in some right half-plane.
Suppose H continues meromorphically to neighborhoods of distinct points
i v_1,...,i v_q, with a pole of order exactly m at each and leading coefficient
c_j:

    H(z) = c_j/(z-i v_j)^m + O((z-i v_j)^(1-m)).          (2.1)

Set r=2m-1. For epsilon>0 let

    J(epsilon)=integral_0^infinity |h(x)|^2 e^(-2 epsilon x) dx.

Whenever J(epsilon) is finite and the Laplace identity for H holds on
Re z>epsilon, define

    b_j(epsilon)=(-1)^(m-1) H^(m-1)(2 epsilon+i v_j),
    V_jk(epsilon)=Gamma(r)/[2 epsilon+i(v_j-v_k)]^r.       (2.2)

Then V is a positive definite Hermitian matrix and

    J(epsilon) >= b(epsilon)^* V(epsilon)^(-1)b(epsilon). (2.3)

Proof. In L2([0,infinity),dx), put f=h exp(-epsilon x) and
v_j(x)=x^(m-1) exp((-epsilon+i v_j)x). Use the inner product linear in
its first variable, so b_j=<f,v_j> and V_jk=<v_k,v_j>.
Integration of x^(r-1) exp(-(2 epsilon+i(v_j-v_k))x) gives (2.2).
The v_j are linearly independent: division by x^(m-1) exp(-epsilon x)
reduces this to linear independence of finitely many distinct exponentials
on an interval. The squared norm of the orthogonal projection of f to their
span is b^* V^(-1)b. This proves (2.3).

Differentiating the Laplace transform in (2.2) is justified by Cauchy-Schwarz
against the displayed square-integrable test. Notice that distinct zeros
need not be well separated. The exact Gram inverse retains their overlap.
Condition numbers can be poor at finite epsilon; no numerical stability
assertion is hidden in the formula.

For the application below H is the actual Laplace transform whenever J is
finite: Cauchy-Schwarz gives holomorphy on Re z>epsilon, and uniqueness of
analytic continuation identifies it there with the meromorphic expression.
If J is infinite, inequalities giving finite lower bounds are automatic.

### Boundary consequence

With the extended-real convention for J,

    liminf_(epsilon -> 0+) (2 epsilon)^r J(epsilon)
        >= Gamma(r)/Gamma(m)^2 sum_(j=1)^q |c_j|^2.       (2.4)

To prove it along any sequence with finite J, differentiate (2.1):

    b_j = [Gamma(r)/Gamma(m)] c_j (2 epsilon)^(-r)
                  + O(epsilon^(1-r)).

The normalized matrix (2 epsilon)^r V/Gamma(r) tends to the identity:
its diagonal is one and every off-diagonal tends to zero, because each
fixed v_j-v_k is nonzero. Substitute into (2.3). Sequences with infinite J
cause no problem. This argument needs finitely many specified poles only.

If C=limsup_(L -> infinity) integral_0^L |h(x)|^2 dx/L^r is finite, then
integration by parts and the definition of limsup give

    limsup_(epsilon -> 0+) (2 epsilon)^r J(epsilon)
          <= C Gamma(r+1).

Indeed J=2 epsilon integral_0^infinity [integral_0^L |h|^2]
e^(-2 epsilon L)dL. Consequently

    limsup_(L -> infinity) integral_0^L |h(x)|^2 dx/L^r
       >= [sum_j |c_j|^2]/[(2m-1) Gamma(m)^2].           (2.5)

This is a limsup assertion, not a lower bound at every sufficiently large L.

## 3. Exact power and logarithmic calibration for the native source

Let rho_j=1/2+delta+i gamma_j be any finite set of distinct nontrivial zeros
of Z_F, all on the displayed vertical line and all of multiplicity exactly
m. Here delta>=0, and no assertion that this is a rightmost zero line is
required. Put

    v_j=gamma_j-t,
    C_j(a,t)=m! exp(a(delta+i v_j)^2)/Z_F^(m)(rho_j).    (3.1)

Each C_j is nonzero. Apply Section 2 to

    h(x)=e^(-delta x)G_(a,t)(x), x>=0.

Its Laplace transform equals

    exp(a(z+delta)^2)/Z_F(1/2+delta+z+it)
       - integral_(-infinity)^0 G_(a,t)(x)e^(-(z+delta)x)dx,   (3.2)

initially far to the right. The second term is entire, so (3.1) is exactly
the leading Laurent coefficient in (2.1). In particular no unknown other
zero is removed and no residue expansion is assumed.

### Theorem 3.1: critical zeros

When delta=0,

    limsup_(L -> infinity) E_(a,t)(L)/L^(2m-1)
       >= [sum_j |C_j(a,t)|^2]/[(2m-1)((m-1)!)^2].     (3.3)

The finite negative half-line energy does not change this limit. For a
single simple critical zero this lower constant is

    exp(-2a(gamma-t)^2)/|Z_F'(1/2+i gamma)|^2.           (3.4)

For a zero of order m>=2 the logarithmic energy degree is 2m-1. In
physical scale D, the denominator in (3.3) is (log D)^(2m-1).

### Theorem 3.2: zeros to the right of the critical line

When delta>0,

    limsup_(L -> infinity)
       E_(a,t)(L)/[e^(2 delta L)L^(2m-2)]
         >= [sum_j |C_j(a,t)|^2]/[2 delta ((m-1)!)^2]. (3.5)

Proof. If the limsup on the left is infinite there is nothing to prove.
Call a finite value M. Let A(L)=integral_0^L |G_(a,t)(x)|^2 dx. Partial
integration gives

    integral_0^L e^(-2 delta x)|G_(a,t)(x)|^2 dx
       =e^(-2 delta L)A(L)
            +2 delta integral_0^L e^(-2 delta x)A(x)dx.

The assumption A(L)<=(M+eta)e^(2 delta L)L^(2m-2) for large L implies
that the limsup of the last displayed expression divided by L^(2m-1)
is at most 2 delta M/(2m-1). Compare this with (2.5) and let eta tend to
zero. This proves (3.5), including m=1. QED.

In physical scale (3.5) forces a positive-power energy along a sequence,
D^(2 Re(rho)-1)(log D)^(2m-2). A zero with greater real part, or a larger
multiplicity on the same line, may make this limsup infinite. Neither
possibility invalidates the theorem. No simplicity, RH, or rightmost-zero
assumption entered its proof.

### Sharpness of the analytic constants

For the model h(x)=c x^(m-1)e^(ivx)/(m-1)! on x>=0, its Laplace transform
is c/(z-iv)^m. Direct integration gives equality in (3.3); for the model
G(x)=e^(delta x)h(x), its energy has exactly the asymptotic constant in
(3.5). These models check the normalization. They are not claims that the
arithmetic source consists of finitely many zero modes.

## 4. Consequences for the proposed energy target

The native bound E_(a,t)(log D)=O_epsilon(D^epsilon) for every epsilon>0
remains compatible with any finite multiplicity of critical zeros. It is
the appropriately weak zero-exclusion target. This note does not prove it.

The much stronger bound E_(a,t)(log D)=O(log D) has additional consequences:

1. There can be no zero with Re rho>1/2, by (3.5).
2. Every critical zero must be simple, by (3.3).
3. For the simple critical zeros, finite-subset versions of (3.3) imply

       sum_(rho on Re=1/2)
          exp(-2a(Im rho-t)^2)/|Z_F'(rho)|^2
          <= limsup_(L -> infinity) E_(a,t)(L)/L.        (4.1)

The series in (4.1) is over distinct zeros, both signs included where they
occur. Its convergence is a necessary conclusion, not an assumption.
The Gaussian alone does not justify a residue sum if derivatives at zeros
are exceptionally small. A zero at s=1/2 is also covered by the argument.

More generally, O((log D)^A) implies m<=(A+1)/2 for every critical zero.
None of these stronger statements follows merely by knowing RH. In
particular the O(log D) equality-of-ideals diagonal from #952 does not
justify conjecturing that the complete scalar energy always has that size.

### An unconditional literal-source obstruction

The theorem of Hu--Kaneko--Martin--Schildkraut states that if F has a subfield
K for which F/K is a nonabelian Galois extension, then zeta_F has infinitely
many nontrivial zeros of multiplicity at least two. The same work gives
multiplicity at least three if Gal(F/K) has an irreducible representation
of dimension at least three. This is unconditional; it does not assume the
Artin holomorphy conjecture. See the primary source in Section 8.

Choose one of its multiple zeros and, if necessary, its functional-equation
reflection so that Re rho>=1/2. Finite missing Euler factors are nonzero in
Re s>0, so the multiplicity persists for Z_F. If Re rho>1/2, (3.5) forces
a positive power of D along a sequence. If Re rho=1/2, (3.3) forces at least
(log D)^3 along a sequence. Thus, for every fixed a>0 and t,

    E_(a,t)(log D) is not O(log D)                       (4.2)

for these actual number fields and actual native Mobius coefficients.
This is not a changed-phase or worst-moving-center counterexample. With
the dimension-three version, O((log D)^A) is impossible for every A<5.

Equation (4.2) does not contradict the subpower target in #952, its ideal
diagonal bound, or the proposed 11/12 zero-free half-plane in #959. It says
that multiple-zero contributions must be budgeted in the full covariance.

## 5. Optional explicit family: no fixed logarithmic degree works for all fields

The following argument uses only standard cyclotomic/Kummer theory and
finite-order Hecke factorization. Its purpose is to make the obstruction
concrete in fields containing mu_12. It is independent of a general Artin
holomorphy conjecture. It should receive separate algebraic review.

For an odd prime p>=5 put

    E=Q(zeta_(12p)),  alpha=2^(1/p) (the positive real root),
    F=E(alpha).                                        (5.1)

First, alpha is not in E. Otherwise Q(alpha) would be a subfield of the
abelian Galois extension E/Q and hence itself Galois over Q. But x^p-2 is
Eisenstein at 2 and Q(alpha) is real while its other conjugates are not,
so this degree-p field is not Galois. Since E contains mu_p, F/E is the
splitting field of x^p-2 and its Galois group injects into C_p by
sigma(alpha)/alpha. It is nontrivial, hence has degree p and equals C_p.

Every automorphism b of E/Q lifts to F by fixing alpha: the presentation
E[X]/(X^p-2) makes this well-defined. Its action on Gal(F/E)=C_p is
multiplication by b modulo p. The restriction map Gal(E/Q)->(Z/pZ)^* is
surjective. Consequently these automorphisms act transitively on the
p-1 nontrivial characters of C_p.

The exact abelian Hecke factorization is

    zeta_F(s)=zeta_E(s) product_(j=1)^(p-1) L_E(s,chi^j).

Conjugating a prime ideal of E by one of the displayed automorphisms
preserves its norm, ramification data and Frobenius character value after
transport. It therefore identifies the full Euler products of all the
nontrivial characters, including ramified local factors. Analytic
continuation yields one and the same entire Hecke L-function H(s), and

    zeta_F(s)=zeta_E(s) H(s)^(p-1).                     (5.2)

Here H is nonprincipal and of finite order, so the classical Hecke
theorem gives entireness; its positive-degree completed L-function has
infinitely many nontrivial zeros by its standard zero-counting formula.
At any such zero, the other factor zeta_E has no pole (its only pole is
at 1), so zeta_F has multiplicity at least p-1. Reflect if necessary to
Re rho>=1/2 and apply Section 3. Since F contains mu_12, these are allowed
field types for the imported Dedekind construction.

Thus, for any preassigned real A>=0, choosing p with 2p-3>A gives a fixed
number field F containing mu_12 for which, at every fixed a>0 and t,

    E_(a,t)(log D) is not O((log D)^A).                  (5.3)

The implicit constant in the false bound is allowed to depend on F, a
and t. The failure is the exponent A, not a requested uniform constant.
Nothing here precludes field-dependent logarithmic degrees, or the
all-epsilon subpower target. The group/character construction is classical;
the application being made here is to the exact Gaussian energy.

## 6. Height damping and a useful change of detector

From (3.1),

    |C_j(a,t)|^2
       = (m!)^2 exp(2a[delta^2-(gamma_j-t)^2])
                      /|Z_F^(m)(rho_j)|^2.             (6.1)

The untwisted width-one Gaussian pays exp(-2 gamma^2) in its squared-energy
signal. This is an exact attenuation factor, not a heuristic estimate of
the full arithmetic energy. For illustration, a mode of height 100 pays
exp(-20000), whose base-10 logarithm is approximately -8685.89. That example
does not assert that 1/2+100i is a zeta zero.

Two source-faithful ways to avoid this blindness are:

* Fix the height parameter t near a target ordinate gamma. At t=gamma
  the attenuation disappears: the factor is exp(2a delta^2).
* Use a narrower Gaussian a if a broad unmodulated height band is required.
  To keep the squared attenuation at least exp(-2) for |gamma|<=T, it is
  enough to take a<=T^(-2).

The latter narrows the physical log-scale window to width O(sqrt(a)).
It is a different smoothing profile, so constants and inherited theta
estimates must be re-established for it. The first option changes the
literal coefficient twist; any proof must retain this separately fixed t
or quantify its height dependence. Neither option supplies the missing
upper estimate. In particular, this note does not evade #955's theorem
that a bound uniform over every center is false.

For a local pole-mode comparison at delta>0, the exponential part of
(3.5) is exp(2 delta L-2a(gamma-t)^2). The balancing log-horizon is

    L approximately a(gamma-t)^2/delta.                 (6.2)

Equation (6.2) compares those exponential factors only. It is not a
finite-horizon detection guarantee: the unknown Laurent coefficient,
other zeros, and the non-effective onset in the limsup theorem remain.

## 7. What this changes in the proposed attack

The genuine alternative is to seek stability of the separately fixed
arithmetic source with a subpower budget, and to retain polynomial zero
modes at the critical boundary. Demanding uniformly bounded or merely
linear log-time energy would unknowingly impose simplicity, which is
already false for many Dedekind fields. Any proposed coercive energy or
semigroup contraction must survive this test before being used as an RH
strategy.

An off-critical zero produces an exponentially growing log-time mode;
a multiple critical zero produces a polynomially growing mode. A correct
stability principle must exclude the former while permitting the latter.
This distinction is especially relevant to a prime-memory delay equation:
a proof of strict contraction cannot be the right all-field conclusion.

For numerical work, use several specified heights and widths, and compare
the exact finite Gram lower bound (2.3), retaining the overlap of nearby
frequencies. Center-zero width-one energy on modest horizons cannot be
treated as a sensitive census of high-ordinate poles. Even height-adapted
experiments are finite diagnostics, not asymptotic upper bounds or RH
certificates.

## 8. Sources, prior art and review scope

1. Hu, Kaneko, Martin and Schildkraut, *Order of Zeros of Dedekind Zeta
   Functions*, arXiv:2107.03269v2; Proc. Amer. Math. Soc. 150 (2022),
   5111--5120. Primary text inspected at
   https://arxiv.org/html/2107.03269v2 . Their unconditional multiple-zero
   theorem is the imported premise in (4.2), not a result of this packet.

2. The same authors, *On a Mertens-type conjecture for number fields*,
   Cambridge primary article, published online 19 December 2024:
   https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/on-a-mertenstype-conjecture-for-number-fields/B01C7628DF4D57CAE8410901FD6A9321 .
   Sections 1--2 discuss weak-Mertens energy, zero multiplicity, and the
   nonabelian obstruction. Their Theorem 1.5 concerns an asymptotic for a
   different, unsmoothed Mertens source under additional hypotheses; none
   of those hypotheses is being silently imported here.

3. #952, frozen head 3b7d2948840446c752bbf284f6f90f6592395a29,
   standalone/2026-10-16-critical-gaussian-energy/ENERGY_THEOREM.md:
   the native full Gaussian, exact critical energy, logarithmic ideal
   diagonal, and open subpower target. Read in full for this note.

4. #955, frozen head 6d3d69c7896e3a5d61d1f67e4627125257398ec7,
   standalone/2026-10-17-native-twist-hull/THEOREMS.md:
   the obstruction to constants uniform over all real centers. Read in
   full. The present fixed-t statements retain that quantifier boundary.

5. #959, frozen head 7b845294207d96b883c1fa95028663082267804f,
   standalone/2026-10-17-numerator-mean-refinement/PROOF.md:
   the proposed 11/12 boundary and the warning that the unchanged positive
   theta estimate has reached its ceiling. No theorem in this note uses
   the proposed 11/12 result as an analytic premise.

The Laplace/Gram proof was derived here and finite normalizations are
checked separately. It does not reconstruct the entire Hecke analytic
theory, the imported papers, or the theta construction. The optional
Kummer family has a written algebraic proof but no computer-algebra
number-field calculation or independent algebraic referee is claimed.
The boundary results are lower/necessary statements; the arithmetic
upper bound remains open.
