# Square-divisibility covers: exact evaluation cost and a signed cusp saving

Status: proposed component theorems with complete proofs. No improved zero-free
half-plane is established. The finite-cover results are unconditional. The cusp
saving explicitly assumes a prior summatory-Mobius bound; it does not improve
that bound.

Scope: ordinary good-prime square-divisibility sections over K=Q(i). The exact
evaluation theorem applies to this incidence subspace, not automatically to the
whole metaplectic representation or to an arbitrary scattering image.

Exact source relationship: this resolves the elementary finite-cover evaluation
problem raised in PR #1016 at commit
`7ea66551190f291101b0dd44fb1fc9b3331c560d`, file
`standalone/2026-10-22-quartic-full-sieve/QUARTIC_SPECTRAL_INTERFACE.md`,
Sections 3 and 6. Its centered nonconstant-term estimate remains open. The
local ordinary Eisenstein identity used below is rederived here from primitive
bottom rows. No quartic automorphic mean is imported or asserted.

What was run: `python -I -S -B verify_finite_cover.py`, an exact-rational finite
product check. The script enumerates primitive projective-line representatives
at split prime-square moduli, then independently evaluates all product atoms
to check Gram orthogonality, evaluation norms, and sieve norms. It does not
prove an infinite analytic estimate or certify any external quasi-RH paper.

Smallest missing step for a boundary improvement: the actual centered
nonconstant Fourier contribution, with all row masks, common profiles,
cross-cusp terms and the complete primitive sieve, still needs a saving.

## 1. The exact finite-cover space

Fix a finite set S of excluded prime ideals (including the prime over 2).
Let P be a finite set of other Gaussian prime ideals. Write q_p=Np and set

    Omega_P = product_(p in P) P^1(O_K/p^2),
    delta_p = 1 / (q_p(q_p+1)).

Each factor has q_p^2+q_p points. Indeed over the local ring O_K/p^2 a
primitive row, modulo multiplication by a unit, has one of the unique forms
`(1,t)` for t in O_K/p^2 or `(t,1)` for t in p/p^2. Thus there are q_p^2
plus q_p points. Use uniform probability measure on each factor and the
product measure on Omega_P.

Let v_p be the indicator of the distinguished point `[0:1]` in the p factor.
For squarefree d supported on P, put v_d=product_(p|d) v_p, including v_1=1.
These are precisely the ordinary old sections which require the first
bottom-row coordinate to be divisible by d^2. At the distinguished product
point x_0, every v_d(x_0)=1. Their exact Gram kernel is

    <v_d,v_e> = delta_lcm(d,e),
    delta_d = product_(p|d) delta_p.                         (1)

This is conditional Haar normalization after any fixed excluded-prime/ray
component has been fixed. No factor of the size of the full cover is omitted.

For R>=1 define the divisor-closed collection

    D_R(P) = {squarefree d supported on P: Nd<=R},
    H_R(P) = span{v_d: d in D_R(P)}.

## 2. Exact Christoffel function at the distinguished point

**Theorem 1.** The squared norm of evaluation at x_0 on H_R(P) is exactly

    ||ev_x0||^2 = sum_(d in D_R(P))
                   product_(p|d) (q_p(q_p+1)-1).             (2)

In particular this cost depends on the growing subspace, rather than the
much larger cardinality of an unnecessarily large common cover. If P contains
all good primes of norm at most R, then, as R tends to infinity with S fixed,

    ||ev_x0||^2 asymp_S R^3,
    ||ev_x0|| asymp_S R^(3/2).                               (3)

*Proof.* Set

    w_d = product_(p|d) (v_p-delta_p).

The expansions of w_d into v_e and conversely use only e|d; since D_R is
divisor-closed, the w_d form a basis of H_R. Independence of the factors and
their zero means give

    <w_d,w_e> = 0             if d!=e,
    ||w_d||^2 = product_(p|d) delta_p(1-delta_p),
    w_d(x_0) = product_(p|d) (1-delta_p).

The squared norm of evaluation is the sum of the squared evaluations of this
orthonormal basis. Its d summand is
`product (1-delta_p)/delta_p`, which proves (2). Equality is attained by the
normalized Riesz vector, so (2) is an exact operator norm, not merely an upper
bound.

For completeness, the order R^3 does not require a prime ideal theorem. The
number A(X) of all Gaussian integral ideals of norm at most X is O(X), since
every ideal is principal and lattice points are counted modulo four units.
In fact A(X)<=2X for X>=1: put m=floor(sqrt(X)); the containing square has
`(2m+1)^2-1` nonzero lattice points, and division by the four units gives
`A(X)<=m^2+m<=X+sqrt(X)<=2X`. The elementary lattice disk estimate gives
A(X)=(pi/4)X+O(sqrt(X)). Squarefree inversion, with fixed excluded primes,
therefore gives

    #{d good squarefree: Nd<=X} = c_S X + O_S(sqrt(X) log(2X)),
    c_S>0.

Here the main constant is the positive squarefree Euler density; this follows
by summing mu(a)A(X/(Na)^2), and treating fixed exclusions by finite
inclusion-exclusion. The tail of the main sum is O(X^(-1/2)); the error sum
uses sum_(Na<=sqrt(X))1/Na=O(log(2X)). Hence a fixed annulus [R/2,R] contains
at least c'_S R good squarefree ideals for large R. Each summand in (2) is at
least (Nd)^2, proving the lower bound.

For the upper bound,

    product_(p|d)(q_p^2+q_p-1)
       <= (Nd)^2 product_(p|d)(1+1/q_p)
        = (Nd)^2 sum_(e|d) 1/Ne.

After dropping squarefreeness, the sum over d=em is at most

    sum_(Ne<=R) (Ne) sum_(Nm<=R/Ne) (Nm)^2
       << R^3 sum_e (Ne)^(-2) << R^3.

This proves (3). QED.

## 3. The actual Mobius sieve has bounded norm, including a tail rate

Put

    V_R = sum_(d in D_R(P)) mu_K(d) v_d.

**Theorem 2.** Uniformly in P and R,

    ||V_R||^2 <= product_(p in P)(1+3 delta_p)
                <= zeta_K(2)^3.                             (4)

If P contains all good primes with norm at most R, then

    V_R(x_0) = M_K^S(R)
             := sum_(Nd<=R, (d,S)=1) mu_K(d).                 (5)

Furthermore, with `V_full,P=product_(p in P)(1-v_p)`,

    ||V_full,P - V_R||^2 <= 96/R.                            (6)

There is an infinite-product version in which V_R converges in L2 to the
indicator that none of the events v_p=1 occurs. Its limit has norm squared
`product_(p notin S)(1-delta_p)>0`, while evaluation at the distinguished
all-events point is still the summatory Mobius expression (5).

*Proof.* Expand the square and bound by the absolute double sum in (1).
For each prime there are three nonempty choices of its membership in (d,e),
all contributing delta_p. Removing the norm cutoff gives the first product
in (4). Since delta_p<=q_p^(-2),
`1+3 delta_p <= (1-q_p^(-2))^(-3)`, proving the second bound. Equation (5)
follows from v_d(x_0)=1.

For (6), expand the exact finite difference using the d with Nd>R. Its norm
squared is at most the sum of delta_lcm(d,e) over those d,e. Write d=ga and
e=gb, where g=gcd(d,e). For squarefree d,e these three ideals are pairwise
coprime and lcm(d,e)=gab. Since delta_lcm<=N(lcm)^(-2), dropping all
coprimality and squarefreeness restrictions gives the majorant

    sum_g (Ng)^(-2)
       [sum_(Na>R/Ng) (Na)^(-2)]^2.                          (7)

The bound A(X)<=2X implies, by partial summation,
`sum_(Na>T) (Na)^(-2)<=4/T` for T>=1 and `zeta_K(2)<=4`.
The part Ng<=R of (7) is at most `16 A(R)/R^2<=32/R`; its complement is at
most `16*(4/R)=64/R`. This proves (6).

On the infinite product of the factor probability spaces, the events have
summable probabilities delta_p. Almost surely only finitely many occur.
Consequently inclusion-exclusion eventually gives the asserted limiting
indicator. Alternatively the uniform tail estimate (6), followed by finite
product limits, proves L2 convergence. The finite products have squared norm
`product_(p in P)(1-delta_p)`, which tends to the positive stated limit. QED.

**Meaning.** Uniformly small Haar norm, even with the explicit R^(-1/2) norm
tail (6), does not control evaluation at the particular arithmetic coset.
The complete cover-normalized operator cost is R^(3/2), and source-specific
evaluation of the actual sieve is exactly M_K^S(R). Assuming a bound
`|V_R(x_0)|<<_epsilon R^(theta+epsilon)` for all R would already continue
`1/zeta_K^S(s)` into Re(s)>theta by partial summation, and therefore prove
the corresponding zero-free half-plane. It cannot be silently supplied by
unitarity or by (4).

There is also an exact constructive consequence. In this paragraph assume
P contains all good primes of norm at most R, as in (5). Let r_R denote the Riesz
vector of evaluation and E_R the sum in (2). Then

    V_R^0 = V_R - (M_K^S(R)/E_R) r_R

has zero distinguished evaluation and is the closest such vector to V_R in
H_R. Its correction has squared norm `|M_K^S(R)|^2/E_R`. Thus a prior bound
`|M_K^S(R)|<<R^theta` pays only `O(R^(2theta-3))` in squared Haar norm;
the trivial summatory bound already pays O(1/R). This follows by orthogonal
projection onto the kernel of evaluation. The correction is explicit, but
the original arithmetic source must be restored, and cancellation of the
incoming value does not by itself cancel its scattering image.

### 3.1 The actual sieve can be large at other cosets

This is not merely an obstruction for arbitrary vectors in H_R. Suppose P
contains every good prime with norm at most R. Choose a product coset x_R
which is the distinguished point exactly at the primes in

    A_R={p good: sqrt(R)<Np<=R},

and is a nondistinguished point at all other factors. Any product of two
distinct primes in A_R has norm greater than R. Therefore the complete
finite inclusion-exclusion sum gives the exact identity

    V_R(x_R)=1-#A_R.                                        (7a)

The bounded norm (4) still holds for this same V_R. Thus the distinguished
coset formula (5), or the signed constant-term bound below, must not be
extended to all cosets. Identity (7a) is the unconditional finite result
used here; this note does not need a prime-counting asymptotic. If the
classical Gaussian prime ideal theorem is additionally imported, it gives
`#A_R asymp R/log R`, which rules out an every-coset bound
`O(R^theta)` for any fixed theta<1. The latter asymptotic is an additional
classical input, not a consequence of the finite checker.

## 4. A genuine source-specific saving for ordinary cusp constant terms

The preceding obstruction does not forbid exploiting known Mobius
cancellation. Here it yields a uniform, explicitly quantified saving for the
actual incoming and outgoing constant terms of the ordinary sieve.

Fix theta in (0,1) and assume the precise prior input

    |M_K^S(X)| <= C_theta X^theta,     X>=1.                   (M)

This is an explicit hypothesis. One may choose theta slightly above an
externally established fixed boundary only after supplying its standard
reciprocal-zeta/Mertens transfer with all dependencies. The present argument
does not certify that external input.

Normalize the ordinary level-one Eisenstein series on hyperbolic 3-space by
constant term `y^s+phi(s)y^(2-s)`. Let E_(d^2) be its primitive-bottom-row
subseries with d^2 dividing the first coordinate and incoming coefficient
one. For squarefree good d its outgoing coefficient is exactly

    phi(s) r_d(s),
    r_d(s)=(Nd)^(2-2s)
                 product_(p|d) (1-q_p^(-1))/(1-q_p^(-s)).     (8)

The expression is a meromorphic identity; at poles it is not read as a
finite numerical value. All bounds below concern r_d itself, leaving the
ordinary factor phi(s) explicit.

**Theorem 3.** Assume (M), let 0<u<=1 and theta+u>1, and set s=u+it. Then

    |sum_(Nd<=R, good squarefree) mu_K(d) r_d(s)|
       <<_(theta,u,C_theta,S) (1+|t|) R^(theta+2-2u),          (9)

uniformly for real t and R>=1. The constant is locally uniform when u and
theta vary over compact subsets of the strict conditions. The incoming
coefficient is bounded by C_theta R^theta. At u=1 both signed constant-term
coefficients therefore have size at most a constant times
`(1+|t|)R^theta`, before multiplication by the retained phi(s).

*Proof of (8).* For one prime p put q=Np and T_r(z,y)=(rz,|r|y).
Partition the primitive bottom rows for E(T_p w,s) according to whether p
divides their second coordinate. Removing a common p gives

    E(T_p w,s)=q^(s/2) E_p(w,s)+q^(-s/2)(E(w,s)-E_p(w,s)).

The corresponding three-way partition for T_(p^2) gives

    E(T_(p^2)w,s)=q^s E_(p^2)+(E_p-E_(p^2))+q^(-s)(E-E_p).

Eliminating E_p yields

    E_(p^2)=[E(T_(p^2)w,s)-q^(-s/2)E(T_pw,s)]/(q^s-1).

The outgoing constant terms of the two dilates have factors q^(2-s) and
q^((2-s)/2), respectively. Their quotient is
`q^(2-2s)(1-q^(-1))/(1-q^(-s))`. Independent local partitions give (8).
The proof starts in absolute convergence Re(s)>2, then continues
meromorphically. No metaplectic scattering assertion is involved.

*Proof of (9).* Let

    c_s(p)=(1-q^(-1))/(1-q^(-s)),
    a_s(d)=mu_K(d) product_(p|d)c_s(p).

The multiplicative Dirichlet convolution identity
`a_s=mu_K^S * h_s` holds with

    h_s(p^k)=1-c_s(p),    k>=1,
    h_s(1)=1,

and zero coefficients at excluded primes. Indeed the local formal series is
`(1-c_s(p)z)/(1-z)=1+(1-c_s(p))(z+z^2+...)`.
Uniformly in t, for 0<u<=1,

    |1-c_s(p)|
       <= (q^(-u)+q^(-1))/(1-q^(-u)) <<_u q^(-u).

It follows from theta+u>1 that

    sum_a |h_s(a)|/(Na)^theta
      = product_(p notin S)
          [1+|1-c_s(p)| q^(-theta)/(1-q^(-theta))]
      <= C_(theta,u,S),                                     (10)

uniformly in t. This uses absolute convergence of the ideal Euler product
to the right of one; no cancellation of h_s is assumed.

Convolution and (M) now give
`|sum_(Nd<=X)a_s(d)|<=C_theta C_(theta,u,S)X^theta`.
Apply partial summation to `(Nd)^(2-2s)`. Its derivative has modulus
`|2-2s| X^(1-2u)`, and theta+2-2u>0. The resulting bound is

    C_theta C_(theta,u,S) R^(theta+2-2u)
            [1+|2-2s|/(theta+2-2u)],

which proves (9). QED.

## 5. Exact limitation and next arithmetic task

If an admissible prior theta is near 0.874886647, then (9) at u=1 gives an
actual signed constant-term bound near R^0.874886647, whereas the
source-independent evaluation norm is of order R^1.5. This is a substantial
evaluation saving for this specified part of the source, conditional on (M).
The comparison is of norm exponents in R, not of attained zero-free bounds.

It remains invalid to insert (9) for the whole scalar Eisenstein packet.
Its nonconstant Fourier terms contain values at different translates,
divisibility masks and additive phases; they are not the single
multiplicative convolution used in (10). A bound for the two ordinary
constant terms does not establish the centered two-column metaplectic norm,
the arithmetic diagonal, or any cancellation between different cusps.

The concrete next target is to separate those exact constant terms before
estimating the nonconstant sector. Any claim that the remaining sector is
small must retain the actual scalar evaluation functional; it cannot appeal
only to Haar-normalized scattering unitarity. No number smaller than the
inherited working boundary is claimed in this note.
