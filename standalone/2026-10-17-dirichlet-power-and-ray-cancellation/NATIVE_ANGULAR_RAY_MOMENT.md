# Native cancellation on rational Eisenstein rays

Status: a proposed, unconditional component proof for the scalar native
source. It proves a quantitative second moment with a **fixed radial
parameter and only an angular average**. It does not estimate a single
angular character, the original principal member, or a zero-free region.
The elementary ingredients are squarefree inversion, cancellation of a
fixed periodic character, ideal counting, and Gaussian angular separation.
No global novelty claim is made for those ingredients.

This addresses the new angular family in [PR #963, PROOF.md](https://github.com/GettysburgResearch/riemann/blob/c91fd9ddfb37668338d9aec22c0e29cfe741cf07/standalone/2026-10-17-archimedean-ideal-resolution/PROOF.md).
Unlike its coefficient-uniform geometric estimate, the ray estimate below
uses the actual Mobius signs. Its source is exactly the scalar principal
native specialization; arbitrary row coefficients are not included.

## 1. Exact source and main theorem

Let K=Q(omega), omega^2+omega+1=0, O=Z[omega], and let Q be a fixed squarefree
positive integer divisible by 6. Let S contain **all** prime ideals above
the rational primes dividing Q, and no others. Thus S is rationally
saturated. This assumption is part of every statement below; an asymmetric
excluded set is not silently replaced by its saturation.

For I=(alpha), put

    psi_l(I)=(alpha/|alpha|)^(6l),  l in Z,
    mu_K^S(I)=mu_K(I) 1_((I,S)=1),
    A_(t,l)(X)=sum_(X/2<NI<=X) mu_K^S(I) (NI)^(it) psi_l(I).

The sixth power makes the character independent of the chosen generator.
Every ideal remains a distinct ideal. In particular, conjugate ideals of
the same rational norm have not been identified.

For R>=1 and an arbitrary integer center l0 define

    p_R(l)=exp[-l^2/(2R^2)] / sum_(j in Z) exp[-j^2/(2R^2)],
    M_R(X;t,l0)=sum_l p_R(l-l0) |A_(t,l)(X)|^2.

**Theorem 1 (finite angular moment, fixed radial parameter).** For X>=2,
R>=1, t real, and l0 integer,

    M_R(X;t,l0) <= C_Q (1+|t|)^2 X (1+X/R).               (1.1)

There is an exact nonnegative ray diagonal D_ray(X;t) such that

    |M_R(X;t,l0)-D_ray(X;t)|
           <= C_K (X/R) D_ray(X;t),                     (1.2)
    c_Q X <= D_ray(X;t) <= C_Q (1+|t|)^2 X               (1.3)

for all sufficiently large X. The lower bound in (1.3) is uniform in t.
Thus the angular Cesaro mean, or the limit as R tends to infinity, has
order X for each fixed t. A width R>=C_0 X makes the finite mean comparable
to this diagonal. In particular R=X already suffices for the upper bound
O_Q((1+|t|)^2 X).

There is no integration in t in (1.1). Taking t=0 keeps the original radial
parameter fixed throughout. The angular average is still present.

## 2. Unique primitive rays and the actual Mobius coefficient

Call an ideal J primitive if it is not divisible by (a) for any integer
a>1. Writing a generator as alpha=x+y omega, its rational content is
gcd(|x|,|y|). Multiplication by a unit is an invertible integral change of
the pair (x,y), so content is well defined on ideals. Every ideal has a
unique factorization

    I=(a)J,  a a positive integer, J primitive.           (2.1)

For a squarefree ideal I prime to S, its primitive part J is squarefree and
contains exactly one of the two prime ideals over each of its supporting
rational primes. All these primes split in K, hence are 1 modulo 3.
Inert prime ideals are rational ideals and have already entered (a).
Ramified primes are excluded because 3 divides Q. In particular NJ is a
squarefree rational integer consisting of split primes.

Let chi=chi_{-3}, the real primitive character modulo 3. Equation (2.1)
is a bijection between the squarefree ideals prime to S and pairs (a,J)
with

    J primitive squarefree, (J,S)=1,
    a squarefree, (a,Q NJ)=1.

The **actual** Mobius sign and angular character are

    mu_K((a)J)=mu_K(J) mu(a)^2 chi(a),
    psi_l((a)J)=psi_l(J).                                (2.2)

Indeed, a split rational prime in a supplies two prime ideals, with Mobius
sign +1, whereas an inert rational prime supplies one prime ideal, with
sign -1. These are exactly the two nonzero values of chi. The coprimality
condition prevents a prime already in J from being squared in I.

Primitive ideals have distinct angular characters psi_1. To see this,
if psi_1(J)=psi_1(J'), the quotient of generators has argument an integer
multiple of pi/3. After multiplying by a unit it is a positive real element
of K, hence a positive rational number. Thus J=(a/b)J' for relatively prime
positive integers a,b. The content of bJ equals b, and that of aJ' equals a;
their equality forces a=b=1 and J=J'. This also shows why the angular mean
identifies rational rays rather than every ideal separately.

Let P_Q be this set of primitive squarefree ideals prime to S, and set

    R_J=sqrt(X/NJ),
    b_J(X;t)=mu_K(J)(NJ)^(it)
       sum_(R_J/sqrt(2)<a<=R_J, (a,Q NJ)=1)
                   mu(a)^2 chi(a) a^(2it).               (2.3)

Only NJ<=X contributes. The source and its ray diagonal are exactly

    A_(t,l)(X)=sum_(J in P_Q, NJ<=X) b_J(X;t) psi_l(J),
    D_ray(X;t)=sum_J |b_J(X;t)|^2.                        (2.4)

No signs in the inner sum have been replaced by absolute values.

## 3. Periodic cancellation on each ray

For M a positive integer divisible by 3, define

    S_M(Y)=sum_(a<=Y, (a,M)=1) mu(a)^2 chi(a),
    f(M)=product_(p|M)(1+p^(-1/2)).

The periodic partial sums of chi satisfy |sum_(h<=V)chi(h)|<=1. Applying
mu(a)^2=sum_(d^2|a)mu(d) and then removing (m,M)=1 gives

    S_M(Y)=sum_(d<=sqrt(Y), (d,M)=1) mu(d)
       sum_(e|rad(M)) mu(e)chi(e)
                   sum_(h<=Y/(d^2 e)) chi(h).

Here chi(d^2)=1 whenever (d,M)=1; factors with chi(e)=0 cause no problem.
The last sum vanishes for d>sqrt(Y/e). Consequently, for every Y>0,

    |S_M(Y)| <= sqrt(Y) sum_(e|rad(M)) e^(-1/2)
               = sqrt(Y) f(M).                          (3.1)

This estimate is unconditional, uniform in M, and does not use any zero
estimate for an L-function.

Partial summation of a^(2it) over (R/sqrt(2),R] using (3.1) yields

    |sum_(R/sqrt(2)<a<=R, (a,M)=1) mu(a)^2 chi(a)a^(2it)|
       <= 2(1+|t|) sqrt(R) f(M).                         (3.2)

For example, the endpoint and derivative bound before enlargement is
sqrt(R)f(M)[1+2^(-1/4)+4|t|(1-2^(-1/4))]. The multiplicative interval has
fixed length in logarithmic coordinates; no log R is lost here.

Because Q and NJ are coprime, (2.3) and (3.2) imply

    |b_J(X;t)|^2
       <=4 f(Q)^2 (1+|t|)^2 sqrt(X/NJ) f(NJ)^2.          (3.3)

## 4. The cofactor weight has bounded mean, not a logarithmic loss

Elementary Eisenstein lattice counting gives

    # {I: NI<=Y}=kappa_K Y+O(sqrt(Y)+1),
    kappa_K=pi/(3sqrt(3)),

and in particular an upper bound C_K Y for Y>=1. For squarefree n,

    f(n)^2=sum_(d|n) h(d),
    h(d)=product_(p|d)(2p^(-1/2)+p^(-1)).

If d divides NJ for J in P_Q, each p|d is split. There are 2^omega(d)
possible ideal divisors of J of norm d. Counting all ideals divisible by
each such divisor gives

    sum_(J in P_Q, NJ<=Y) f(NJ)^2
      <= C_K Y sum_(d squarefree, p|d => p split) 2^omega(d)h(d)/d
      = C_K Y product_(p split)(1+4p^(-3/2)+2p^(-2))
      <= C'_K Y.                                        (4.1)

The product converges absolutely. There is no extra logarithm from the
split-prime primitive cores or the mask in (3.1). Partial summation gives

    sum_(J in P_Q, NJ<=X) f(NJ)^2/(NJ)^(1/2) <= C_K sqrt(X).

Summing (3.3) proves the upper bound in (1.3).

For completeness the lower bound uses a positive density of primitive
cores, proved without a prime ideal theorem. Their Dirichlet series is

    H_Q(s)=sum_(J in P_Q)(NJ)^(-s)
          =product_(p split, p not dividing Q)(1+2p^(-s))
          =zeta_K^S(s) V_Q(s),                           (4.2)

where

    V_Q(s)=product_(p split, p not dividing Q)
                     (1-3p^(-2s)+2p^(-3s))
           product_(p inert, p not dividing Q)(1-p^(-2s)).

The coefficient absolute mass of V_Q converges at every real s>1/2.
Convolving ideal counting with these coefficients at s=3/4 gives

    # {J in P_Q: NJ<=Y}=kappa_prim,Q Y+O_Q(Y^(3/4)),       (4.3)
    kappa_prim,Q=Res_(s=1)zeta_K^S(s) V_Q(1)>0.

The error follows by splitting the coefficient sum at d=Y: both the ideal
counting error and the omitted main-term tail are O(Y^(3/4)). Every Euler
factor defining V_Q(1) is positive and equals 1+O(p^(-2)), so its product
is positive. For X/2<NJ<=X, the inner sum in (2.3) consists only of a=1.
Thus each such J contributes exactly one to D_ray, proving its lower bound.

## 5. Finite angular resolution with no radial integration

Write phi_J=6 arg(alpha_J) modulo 2pi. For distinct primitive J,J' of norms
at most Y, rotate one generator by a unit to make their angle theta have
|theta|<=pi/6. They cannot be collinear by Section 2. Since

    Im(alpha_J conjugate(alpha_J')) is in (sqrt(3)/2) Z,

its nonzero absolute value is at least sqrt(3)/2. Therefore the circular
distance delta(phi_J,phi_J') satisfies

    delta=6|theta| >=6|sin(theta)|
                    >=3sqrt(3)/Y.                       (5.1)

This determinant estimate is for **primitive rational rays**. Applying it
to arbitrary distinct ideals would fail because rational multiples have
the same angle.

The exact Gaussian angular kernel is

    Theta_R(theta)=sum_l p_R(l)e^(il theta)
       = [sum_(j in Z) exp(-R^2(theta-2pi j)^2/2)]
          / [sum_(j in Z) exp(-2pi^2 R^2 j^2)].           (5.2)

For R>=1, Theta_R(0)=1 and

    0<=Theta_R(theta)<=3 exp[-R^2 delta(theta,2pi Z)^2/2].

Ordering separated ray angles on the two semicircles around a fixed ray,
the n-th neighbor in either direction has distance at least
n*3sqrt(3)/Y. Comparing the resulting Gaussian series to an integral yields

    sup_J sum_(J'!=J) |Theta_R(phi_J-phi_J')| <= C_K Y/R. (5.3)

The center l0 inserts only a unit phase in the quadratic form. The Schur
bound applied to (2.4) proves (1.2), and (1.1) follows. Since the source is
a finite trigonometric sum at a hard cutoff, its two-sided Cesaro mean also
equals D_ray exactly, by the distinct-frequency conclusion of Section 2.

## 6. Full Gaussian columns and one-log critical energy

Use the same full-tail Gaussian as PR #963:

    W_c(y)=y^(-c) exp[-(log y)^2/4]/(2sqrt(pi)),
    A^c_(t,l)(X)=sum_I mu_K^S(I)(NI)^(it)psi_l(I)W_c(NI/X).

Here c is any fixed real number; neither the column tail nor the angular
tail is truncated. Let b^c_J(X;t) be the exact rational-ray coefficient
obtained from (2.3) by replacing the hard window with W_c(a^2 NJ/X), and put

    D^c_ray(X;t)=sum_J |b^c_J(X;t)|^2,
    Delta^c_ray(D;t)=integral_0^D D^c_ray(X;t) dX/X^2,
    E^c_(t,l)(D)=integral_0^D |A^c_(t,l)(X)|^2 dX/X^2.

**Theorem 2 (full Gaussian energy at fixed radial parameter).** For D>=2,
R>=1, fixed c and Q, and arbitrary t and l0,

    Delta^c_ray(D;t) <= C_(c,Q)(1+|t|)^2 log(3+D),         (6.1)
    |sum_l p_R(l-l0) E^c_(t,l)(D)-Delta^c_ray(D;t)|
                   <= C_(c,Q)(1+|t|)^2 D/R.              (6.2)

For each fixed t, Delta^c_ray(D;t) has order log D. Consequently the
**angular-only** averaged complete critical energy at R=D has order log D.
In particular,

    sum_l p_D(l-l0) E^c_(0,l)(D) <= C_(c,Q) log(3+D).      (6.3)

The source in (6.3) retains its radial parameter t=0 and its native Mobius
signs. The averaging measure is different from the two-coordinate measure
in PR #963; no estimate for l=0 alone follows by substituting that value.

### Proof including all tails and cross-band terms

Partition NI/X into (2^j,2^(j+1)], j in Z, and put Y_j=2^(j+1)X. A band
with Y_j<1 is empty. Write w_j=sup_(2^j<y<=2^(j+1)) W_c(y). Then

    w_j <= C_c exp[-c_0 j^2+C_c|j|]

for an absolute c_0>0. On the same interval the logarithmic derivative of
W_c has absolute value at most C_c(1+|j|)W_c. Apply partial summation using
(3.1) to the actual ray weight a^(2it)W_c(a^2 NJ/X). The endpoint and
variation bound is the estimate (3.2) multiplied by at most
C_c(1+|j|)w_j. Thus the ray-coefficient ell2 norm of band j is at most

    C_(c,Q)(1+|t|) sqrt(Y_j) (1+|j|)w_j.                 (6.4)

Minkowski's inequality and the convergent Gaussian band sum give
D^c_ray(X;t)<=C_(c,Q)(1+|t|)^2 X for all X>0. For two different bands, use
the polarized Schur estimate (5.3) on their union of ray supports, with cap
max(Y_j,Y_k). Summing **every** cross-band term by (6.4) gives

    |sum_l p_R(l-l0)|A^c_(t,l)(X)|^2-D^c_ray(X;t)|
                <= C_(c,Q)(1+|t|)^2 X^2/R.              (6.5)

The double series converges because its Gaussian factors dominate
max(2^j,2^k)2^((j+k)/2) times any fixed polynomial in j,k. First do this
for finitely many bands and then pass to the limit in the relevant Hilbert
spaces. This retains all band cross terms and all angular integers.

On X<1, absolute ideal counting and W_c(y)<<_(A,c)y^(-A), y>=1, give
|A^c_(t,l)(X)|<=C_(A,c,Q)X^A for any fixed A>1, uniformly in t,l. The ray
diagonal obeys the same squared upper bound, since its ell2 norm is at most
the total absolute coefficient mass. This makes the entire interval (0,1)
integrable. Integrating (6.5) and the diagonal bounds proves (6.1),(6.2).

To verify the stated lower order despite possible cancellation within a
Gaussian ray, choose y0>=2 with 2c+log y0>=3. For y>=y0,

    W_c(a^2 y)/W_c(y)=a^(-2c-log y) exp[-(log a)^2],
    sum_(a>=2) W_c(a^2 y)/W_c(y)
                         <=sum_(a>=2)a^(-3)<=1/4.

For every primitive J with y0 X<NJ<=2y0 X, the a=1 term in its ray thus
has absolute value at least four times the absolute sum of the remaining
terms, even after their actual masks and phases are included. In particular
|b^c_J(X;t)|>=(3/4)min_(y0<=y<=2y0)W_c(y)>0, uniformly in t. The positive
density (4.3) gives D^c_ray(X;t)>=c_(c,Q)X for large X. Its integrated
diagonal therefore has order log D for fixed t, and (6.2) with R=D proves
the corresponding averaged-energy assertion.

## 7. What has advanced and the remaining principal extraction

The arithmetic step is (3.1), applied before taking absolute values along
each rational ray. It reduces a ray of length R from its unsigned size
O(R) to O(sqrt(R)) with an explicitly summable cofactor weight. This gives
the bounded mean (1.3), then a finite angular-only mean and complete
one-log Gaussian energy while the radial parameter remains fixed.

This cancellation is specific to the unchanged scalar Mobius source. It
cannot be inferred from the arbitrary-coefficient large sieve in PR #963.
It also does not prove that the angular average can be removed: positivity
alone costs p_R(-l0)^(-1) for any chosen angular member, which is of order
R even at the center. The companion ANGULAR_HULL_OBSTRUCTION.md proves
actual native moving-angle peaks at radial parameter zero, making the
uniform-center width cost X/R necessary up to constants in second order.

Nothing here assumes the repository's proposed quasi-RH exponents or the
finite-order Hecke conclusion. The added angular characters have infinite
order; no finite-order theorem is applied to them. This is a complete
source-specific averaged estimate, with fixed principal angular extraction
still the missing RH-bearing step.

## 8. A positive-coefficient control quantifies the arithmetic gain

For comparison within the coefficient-uniform class of PR #963, replace
the native coefficient by 1_((I,S)=1), explicitly a different control source.
Its exact angular-ray diagonal has order X log X. Here primitive cores
need not be squarefree; denote all primitive ideals prime to S by P_all,Q.
The content decomposition gives

    sum_(J in P_all,Q)(NJ)^(-s)=zeta_K^S(s)/zeta_Q^Q(2s).

Convolving the ideal count with mu^Q at square norms gives

    # {J in P_all,Q: NJ<=Y}
       = [kappa_S/zeta_Q^Q(2)]Y+O_Q(sqrt(Y)log(3Y)).

Its ray of parameter R=sqrt(X/NJ) contains

    # {R/sqrt(2)<a<=R: (a,Q)=1}
       = (phi(Q)/Q)(1-1/sqrt(2))R+O_Q(1)

terms, by finite inclusion-exclusion. Squaring this count and summing over
NJ<=X gives an upper bound O_Q(X log X). Restricting to NJ<=X/R_0^2 for a
sufficiently large fixed R_0 gives the matching lower bound: every such ray
has at least c_Q R terms, and the harmonic sum over its primitive cores is
asymptotic to a positive constant times log X. Thus the angular Cesaro
diagonal for this positive control is Theta_Q(X log X).

The native ray diagonal in Theorem 1 is Theta_Q(X). The removal of this
logarithm at fixed radial parameter is supplied by the actual signed
character sum (3.1); angular geometry alone also applies to the positive
control and therefore cannot supply that improvement for every coefficient
array.
