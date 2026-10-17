# Critical scattering, causal subspaces, and the exact missing projection

Status: proposed component analysis for independent review. This does not prove a
new zeta zero-free region. The Euler stripping itself is inherited from #948 and
#950. The point developed here is its noncausal critical-line operator, an exact
Hardy-space description of when it becomes causal, and a finite interpolation
certificate for the remaining defect.

Hadamard products, half-plane inner functions, Hardy model spaces, Plancherel,
and reproducing-kernel projection are classical. The proposed contribution is
their exact application to this source's stripping factor and localization
problem. No literature-priority claim is made.

## 1. Source and normalizations

CT v2 defines a unitary Hecke character theta whose angular exponent at every
complex place is +1 or -1. Its sixth power eta=theta^6 therefore has angular
exponent +6 or -6 and is nonprincipal. The field F is totally complex; write
d=[F:Q]=2g. For the primitive inducing character eta put

    Q_eta = |D_F| N conductor(eta),
    Lambda_eta(w) = Q_eta^(w/2) Gamma_C(w+3)^g L(w,eta),
    Gamma_C(w) = 2 (2 pi)^(-w) Gamma(w).

The completed Hecke function is entire of order one, its zeros lie in
0<Re w<1, and

    Lambda_eta(w) = epsilon_eta Lambda_bar_eta(1-w)
                  = epsilon_eta conjugate(Lambda_eta(1-conjugate(w))),
    |epsilon_eta|=1.

These are classical Hecke facts; nonvanishing on Re w=0,1 is included. They do
not assume GRH. They imply the symmetry rho -> 1-conjugate(rho) within this
same completed eta-function, even when eta is not a real character.

The full-L version of the known stripping multiplier is

    R(s) = L(6s-2,eta) / L(6s-3,eta).

Set r=s-1/2 and define

    Theta(r) = Lambda_eta(6r) / Lambda_eta(1+6r),
    C_eta = Q_eta^(-1/2) (2 pi)^g,
    A(r) = C_eta / (3+6r)^g.

The gamma recurrence gives the exact meromorphic identity

    R(r+1/2) = A(r) / Theta(r).                         (1)

All conductor and gamma factors in (1) are retained. No finite-order theorem
is applied to eta.

Primary sources: CT v2, Sections 7 and 11,
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex;
OpenAI's precise character and Euler construction is in
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex
(blob c8526f74b281d37fda034c17195c4bb5afd5f79b).

## 2. An unconditional inner function

**Lemma 1.** Theta is an inner function on the right half-plane: it is
holomorphic and bounded by one there, and its boundary values have modulus one.
Its zeros there are exactly rho/6, with multiplicity, for zeros rho of
Lambda_eta. In particular this inner-function assertion does not locate those
zeros on a vertical line.

Proof. The denominator has no zero when Re r>=0. The functional equation gives
|Lambda_eta(6it)|=|Lambda_eta(1+6it)|, so the boundary modulus is one.
For the interior bound, center the entire function at 1/2:

    phi(z)=Lambda_eta(1/2+z).

Its functional equation is phi(z)=epsilon_eta conjugate(phi(-conjugate(z))).
Factor a possible central zero of order m and take an order-one canonical
Hadamard product

    phi(z)=z^m exp(a+bz) product_alpha E_1(z/alpha).

The functional equation applied at zero after removing z^m implies Re b=0.
The nonzero roots can be grouped as alpha and -conjugate(alpha); imaginary
roots are their own partners. The ordering by |alpha| respects these pairs.
In the ratio phi(w-1/2)/phi(w+1/2), the global exponential has modulus one.
For a paired root, the two canonical exponential factors also contribute a
constant of modulus one, because 1/alpha-1/conjugate(alpha) is imaginary.

Writing rho=1/2+alpha, the remaining paired linear quotient has the same
modulus as the product of the two right-half-plane Blaschke factors

    (w-rho)/(w+conjugate(rho)),
    (w-(1-conjugate(rho)))/(w+(1-rho)).

Both zero real parts are positive. Each factor has modulus at most one when
Re w>0. A root on the symmetry line gives a single such factor, and the
central zero gives ((w-1/2)/(w+1/2))^m. Every finite paired product has the
required bound; the locally convergent canonical-product quotient preserves
it in the limit. Put w=6r. This proves the lemma. QED.

## 3. Exact critical multiplier and smoothing

For tau real set

    U_eta(tau) = epsilon_eta^(-1)
                 Lambda_eta(1+i tau)/conjugate(Lambda_eta(1+i tau)).

This has modulus one. On Re s=1/2, (1) gives

    R(1/2+it) = C_eta (3+6it)^(-g) U_eta(6t),
    |R(1/2+it)| = C_eta (9+36t^2)^(-g/2).              (2)

Let h belong to L2(R,du), with Fourier transform
F(it)=integral h(u) exp(-itu) du. Define T by the multiplier (2). Plancherel
proves, with the same Fourier normalization on both sides,

    ||T h||_2 <= C_eta 3^(-g) ||h||_2,
    ||(3+6 partial_u)^g T h||_2 = C_eta ||h||_2.        (3)

Thus the stripped multiplier is smoothing on the critical line. Its absolute
Dirichlet-convolution norm can diverge there without contradicting (3).
The inverse has a fixed Sobolev loss; it is not a bounded L2 inverse.

This claim applies to an input already in L2, such as any chosen finite
window of a locally square-integrable source. It does not assert that an
unwindowed reciprocal-zeta source is in L2 or is tempered.

## 4. Causality and the model-space defect

Use H2_+ for the Hardy space of the right half-plane, realized on its boundary
with norm (1/(2 pi)) integral |F(it)|^2 dt. By the Laplace/Paley-Wiener
identification it corresponds to L2 functions supported on u>=0.

The inner product is linear in its first argument:
(1/(2 pi)) integral F(it) conjugate(G(it)) dt. Define

    K_Theta = H2_+ orthogonal-complement (Theta H2_+).

Every F in H2_+ has a unique orthogonal decomposition

    F = Theta G + D,     G in H2_+, D in K_Theta.        (4)

Since multiplication by an inner function is an isometry, boundary division
by Theta yields

    conjugate(Theta) F = G + conjugate(Theta) D.         (5)

The second summand is in H2_-, the orthogonal complement of H2_+ in boundary
L2. Indeed its inner product with any H in H2_+ equals that of D with Theta H,
which is zero. Consequently (1) gives the exact defect identity

    ||P_- [C_eta^(-1) (3+6it)^g R(1/2+it) F(it)]||_2
         = ||P_(K_Theta) F||_2.                        (6)

The positive Hardy projection is exactly G, and their squared norms add to
||F||_2^2. Equation (6) describes the failure of causality, after removing the
explicit archimedean smoothing.

**Corollary 2.** On the precise closed subspace Theta H2_+, stripping is a
causal bounded smoothing operation. If F=Theta G, then RF=AG is analytic in
the right half-plane and satisfies (3). The causal kernel of A is explicitly

    a(u) = (C_eta/6^g) u^(g-1) exp(-u/2)/Gamma(g),
           u>=0,
    a(u) = 0, u<0.

For a general Hardy input, RF has an additional meromorphic term AD/Theta.
Its poles cannot be discarded by appealing to the bounded boundary multiplier.
Membership in Theta H2_+ is a real condition on the entire source, not a
property of its local Euler factors alone after an arbitrary truncation.

## 5. A finite interpolation certificate for the defect

Suppose lambda_1,...,lambda_n are distinct zeros of Theta. The functions

    k_j(r)=1/(r+conjugate(lambda_j))

belong to K_Theta, and are the Hardy evaluation kernels. Let

    v_j = F(lambda_j),
    G_ij = 1/(lambda_i+conjugate(lambda_j)).

The Gram matrix G is positive definite. Orthogonal projection onto the span
of these kernels gives the rigorous lower bound

    ||P_(K_Theta) F||_2^2 >= v^* G^(-1) v.              (7)

Equality holds when Theta is the finite Blaschke product with these simple
zeros. Multiple zeros require the corresponding derivative-evaluation kernels.
For a causal window h supported on [0,T], the measured quantities in (7) are
literal finite integrals

    v_j=integral_0^T h(u) exp(-lambda_j u) du.

This is a concrete source-specific diagnostic. It measures whether a chosen
window preserves the angular nulls required for causal stripping. Small values
at finitely many zeros do not control the omitted infinite model-space part.
No angular zero ordinates or finite numerical observations are used as premises
of a global conclusion here.

## 6. Finite-S repair

Let S0 consist of the primes omitted by S where the primitive eta is unramified,
and put P_S(w)=product_(p in S0)(1-eta(p)Np^(-w)). Then

    L^S(w,eta)=P_S(w)L(w,eta),
    R_S(s)=R(s) P_S(6s-2)/P_S(6s-3).

The extra denominator can vanish on Re s=1/2. Therefore (2)-(3) must NOT be
claimed for R_S without a repair. Define

    B_S(s)=P_S(6s-3)/P_S(6s-2).

Then B_S R_S=R. The repair is holomorphic and nowhere zero on Re s>1/2,
bounded on the critical line, and has only possible zeros, not poles, there.
Its denominator is bounded below there by product_(p in S0)(1-1/Np).
For a zero-excluding source Hhat_S/zeta_F^S, multiplication by B_S introduces
no new cancellation in the open half-plane Re s>1/2. Its boundary zeros and
the absence of a bounded boundary inverse must nevertheless be retained.

## 7. Why this does not furnish a proof of RH

A rational example isolates the obstruction. Fix a>1/2. The multiplier
1/(s-a) is bounded on Re s=1/2. Its inverse Mellin integral on a line c>a is

    x^a 1_(x>1),

whereas inversion on Re s=1/2 gives

    -x^a 1_(0<x<1).

Their difference is the nonzero residue x^a. A bounded boundary multiplier
selects a noncausal solution; it does not eliminate the growing causal mode.
The displayed indicator formulas are asserted for x!=1; either consistent
half-value convention at the single jump has no bearing on the argument.

There is also a localization issue before any zero question: CT's fixed
Gaussian logarithmic weight has tails at both ends. Its physical source is
not literally supported in a causal half-line. A one-sided cutoff, an actual
Hardy projection, or a justified tail decomposition is needed before applying
(4). Such a cutoff generally changes the angular null conditions.

For the actual full multiplier, its poles in Re s>1/2 occur at
s=(rho+3)/6 for angular zeros rho. In the exact untruncated product with the
CT source, these poles are canceled by its known numerator L(6s-3,eta).
That algebraic cancellation does not prove Hardy-space membership or a
uniform causal-window estimate. Truncation generally destroys the numerator
nulls, which is exactly what (6)-(7) detect.

After multiplying by the known stripped correction, any poles from target
zeta zeros remain. A contour shift for a Gaussian-damped meromorphic product
Q(s) reads

    inverse_Mellin_c(Q)(x)
      = inverse_Mellin_sigma(Q)(x)
         + sum_(sigma<Re p<c) Res_(s=p)(Q(s)x^s),

with the usual finite-height statement and justified limiting process. The
target-zero residues are precisely the terms that a proposed global estimate
must control. On the critical line itself, zeros permitted by RH also prevent
an automatic global L2 assertion for a reciprocal zeta function.

The distinct research target is therefore to construct a source-compatible
localization and projection retaining Theta divisibility, or to bound the
model-space defect together with all target-pole terms by arithmetic arguments.
This is a signed spectral projection problem. Theorems (1)-(7) identify the
operator and its obstruction; they do not establish that final bound.
