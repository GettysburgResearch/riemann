# A whole-xi proof attempt through positive gamma sums

Date: 2026-09-09. Status: FAILED FULL RH PROOF ATTEMPT, with proposed complete
component arguments for independent review. **RH is not proved.**

This is a change of attack, not another residual compression. The intended
complete proof was: construct explicit approximants to the whole completed
xi function from independent positive variables; impose the exact functional
equation; prove the approximants have no off-line critical-strip zeros; pass
to xi by local uniform convergence. The zero-location step is false for this
construction. We prove that failure, at an explicit cutoff and at every
sufficiently large cutoff. No zero constructed below is a zero of zeta or xi.

The probability representation and finite-convolution approximation method
are classical Biane--Pitman--Yor material [BPY]. In particular, their Section
5.4 explicitly suggests the shape-two computation. No external novelty or
priority is claimed. The reflection completion and its zero analysis are
proved here; finite checks are not a proof of their analytic quantifiers.

## 1. Fixed normalization and the candidate complete proof

Use the entire Riemann completion

    xi(s) = s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    xi(0)=xi(1)=1/2, xi(s)=xi(1-s).

The letter z below is HALF of the usual s coordinate: s=2z. The critical
line is Re z=1/4, not Re z=1/2.

Let G_n, n>=1, be independent Gamma(shape=2, rate=1) variables, with density
x exp(-x) on x>0. Define

    S_N=sum_(n=1)^N G_n/n^2,  S=sum_(n>=1)G_n/n^2,
    M_N(z)=E[(S_N/pi)^z],                 Re z>-2N.       (1)

Powers use the real logarithm of a positive random variable. This is a
positive convolution law, not a random-prime approximation.

Set, initially on -2N<Re z<2N+1/2,

    X_N(z)=[M_N(z)+M_N(1/2-z)]/4,
    R_N(z)=Gamma(2N)Gamma(2N+1/2)
                /[Gamma(2N+z)Gamma(2N+1/2-z)],
    F_N(s)=R_N(s/2)X_N(s/2)/[2X_N(0)].                  (2)

The reciprocal gamma factors extend the product in (2) to an entire
function, as proved below. They are NONZERO throughout 0<Re s<1.

**W1.** Each F_N is entire and real under conjugation, satisfies EXACTLY

    F_N(s)=F_N(1-s),  F_N(0)=F_N(1)=1/2,
    F_N(s)>0 for real 0<=s<=1,                           (3)

and, for every fixed compact K subset C,

    sup_(s in K)|F_N(s)-xi(s)| = O_K(1/N).               (4)

Constants in (4) are not numerically instantiated or uniform over growing
sets. No assertion about the zeros of F_N is contained in W1.

Before the reciprocal gamma multiplication, the symmetric function has a
literal positive-measure interpretation. With V_N=log(S_N/pi),

    X_N(1/4+it)/X_N(1/4)
      = E[exp(V_N/4) cos(t V_N)]/E[exp(V_N/4)].          (5)

It is the characteristic function of the symmetrization of an exponentially
tilted real random variable. More precisely, X_N(s/2)/(2X_N(0)) is half the
Mellin transform of a positive mean-one law satisfying reciprocal size-bias
symmetry: mix sqrt(S_N/pi) with its reciprocal, using weights 1 and
sqrt(S_N/pi), then normalize. All finite transforms are analytic on their
stated strips. Multiplying by R_N is NOT asserted to preserve a probability
law or positive Fourier density; it preserves the zero set within the
critical strip because it is nonzero there.

If the F_N were zero-free off the critical line in 0<Re s<1 for every N in
an unbounded sequence, Hurwitz on each connected half-strip would prove RH.
The limit is not identically zero, since xi is positive on the real part of
that strip. The proposed uniform finite-source zero theorem would therefore
be genuinely load-bearing, not merely an equivalent integral notation.

Here is the obstruction obtained by attempting to prove that theorem.

**W2 (explicit cutoff).** F_256 has infinitely many zeros s with

    2/3<Re s<1,  Im s>0,

with ordinates unbounded. Reflection gives corresponding zeros in
0<Re s<1/3. This is a rigorous existence theorem, not a computed ordinate.

**W3 (the problem persists at arbitrarily large cutoffs).** For every fixed
beta with 1/2<beta<1 there is N0(beta) such that, for EVERY integer N>=N0,
EVERY epsilon>0, and EVERY T0>0, F_N has a zero s satisfying

    |Re s-beta|<epsilon,  Im s>T0.                       (6)

One may reduce epsilon so the zero lies within the critical strip. W3 uses
only the ordinary unconditional PNT, finite prime-phase orthogonality,
Stirling asymptotics and elementary complex analysis. N0 and T0-dependent
phase-return heights are not numerically supplied. W2 does not use PNT.

Consequently no unbounded subsequence of these particular approximants can
satisfy the all-height off-line zero-free condition in the proposed proof.
This does not contradict their convergence to xi, and does not decide RH.

## 2. Exact finite formula, including every removable pole

Define positive rational weights and rational correction terms by

    w_(n,N)=[(N!)^2/((N-n)!(N+n)!)]^2,
    u_(n,N)=n[H_(N+n)-H_(N-n)], H_0=0,
    P_N(z)=sum_(n=1)^N w_(n,N)[z-1/2+u_(n,N)] n^(-2z).

Then

    M_N(z)=4 pi^(-z)Gamma(z+1)P_N(z).                    (7)

To prove it, the finite Laplace transform is

    L_N(t)=product_(n=1)^N [n^2/(n^2+t)]^2.

At its double pole -n^2 write its partial fractions as
A_n/(t+n^2)+B_n/(t+n^2)^2. Elementary products give

    B_n=4n^4 w_(n,N),
    A_n=-2B_n sum_(j!=n,1<=j<=N) 1/(j^2-n^2)
       =4n^2 w_(n,N)[u_(n,N)-3/2].                      (8)

The last equality follows from 1/(j^2-n^2)=[1/(j-n)-1/(j+n)]/(2n):

    sum_(j!=n)1/(j^2-n^2)=3/(4n^2)-u_(n,N)/(2n^2).

The inverse Laplace density is sum (A_n+B_n x)exp(-n^2x).
This finite signed expression is the density of the ORIGINAL positive
convolution, not a claim that each partial-fraction term is positive.
Integrate x^z term by term for Re z>-1. Formula (7) follows, and analytic
continuation extends it to Re z>-2N. The density near zero has order x^(2N-1)
with a positive leading constant, either by convolution on a simplex or by
scaling its 2N exponential coordinates. Its positive moments all exist.
This justifies the stated moment strip.

Since the left side of (7) is analytic at z=-1,...,-(2N-1),

    P_N(-j)=0 for j=1,...,2N-1.                          (9)

Thus, using Gamma(z+2N)/Gamma(z+1)=product_(j=1)^(2N-1)(z+j),

    M_N(z)/Gamma(2N+z)
      =4pi^(-z)P_N(z)/product_(j=1)^(2N-1)(z+j)          (10)

is entire, with the zero factors removed at (9). The empty product for N=1
is one. Multiplying either term of X_N by R_N now gives an entire function;
the other reciprocal gamma factor is entire as well. This proves the
entireness assertion of W1 without assigning arbitrary exceptional values.

The reflection, conjugation and positive real values in (3) follow directly
from (1)-(2). R_N(0)=R_N(1/2)=1; X_N(0)=X_N(1/2)>1/4. Hence the two endpoint
values are exactly 1/2. F_N is not an Euler product, and its full divisor is
not identified with that of xi. The regularization may introduce zeros
outside the moment strip; none of those is used in W2 or W3.

## 3. Whole-function convergence with the genuine infinite source retained

The sum S exists almost surely and in every positive L^p: E S=2sum n^-2 is
finite, and for 0<t<1, E exp(tS)=product(1-t/n^2)^(-2)<infinity. Also S>=S_m
for every m, and S_m has negative moments of all orders below 2m. Therefore
S has moments of every real order. Its Mellin transform is entire by compact
dominated differentiation (logarithmic powers are absorbed by slightly
larger positive/negative real exponents).

Under the natural coupling S_N<=S,

    E(S-S_N)^2=2sum_(n>N)n^-4+[2sum_(n>N)n^-2]^2=O(N^-2). (11)

Fix |z|<=R and an integer m>R+1. For N>=m, the derivative of x^z on x>0
bounds |S^z-S_N^z| by a constant depending on R times

    (S-S_N)[S_m^(-R-1)+1+S^(R+1)].

Cauchy--Schwarz and (11), together with the stated positive and negative
moments, prove

    M_N(z)->M(z):=E[(S/pi)^z] locally uniformly,
    sup_(|z|<=R)|M_N(z)-M(z)|=O_R(1/N).                 (12)

Here no infinite residual has been set to zero; (11) pays it.

For identification with xi we supply the short right-half-plane calculation
as well as crediting [BPY]. The recurrence for the factorial weights is

    w_(n,N)=product_(k=1)^n [(N-k+1)/(N+k)]^2.

In particular

    0<w_(n,N)<=exp(-n^2/N),  w_(n,N)->1 for fixed n.      (13)

The upper bound follows from log(1-v)<=-v applied to
(N-k+1)/(N+k)=1-(2k-1)/(N+k), then N+k<=2N.
Moreover u_(n,N)<=2n^2/(N-n+1). For Re z>=a>1/2,

    sum_(n<=N/2) w_(n,N)u_(n,N)n^(-2a)
       <=(4/N)sum_(n<=N/2)n^(2-2a)exp(-n^2/N)->0.

Integral comparison proves this limit (at a=3/2 use log N/N, above it use
O(1/N)). The n>N/2 part is bounded by a polynomial in N times exp(-N/4)
and also vanishes. Dominated convergence gives sum w_(n,N)n^(-2z)->zeta(2z)
for Re z>1/2. Equation (7) therefore identifies

    M(z)=4pi^(-z)Gamma(z+1)(z-1/2)zeta(2z)=2xi(2z).
                                                               (14)

Both sides are entire, so the identity theorem extends (14) to C. This
recovers the classical gamma/Brownian representation, not a new assertion
of real zeros. Gamma-ratio asymptotics [G] imply R_N(z)=1+O_K(1/N) on every
fixed compact; the powers (2N)^z and (2N)^(-z) cancel. Also 2X_N(0)->1 with
the same rate and 2X_N(0)>1/2. Combining with (12), (14), and xi reflection
proves (4).

This convergence is additive on fixed compacts. It gives neither relative
error near zeros nor uniform error on the whole critical strip.

## 4. How finite prime phases determine the approximants' remote zeros

For fixed N, define its leading Dirichlet polynomial

    A_N(z)=sum_(n=1)^N w_(n,N)n^(-2z),
    A_N^chi(z)=sum_(n=1)^N w_(n,N)chi(n)n^(-2z),          (15)

where chi is any completely multiplicative function with |chi(p)|=1 for
primes p<=N. This is an auxiliary phase choice, NOT a change of F_N.

**Prime-phase lemma.** For any such chi there are T_j->+infinity such that
p^(-2iT_j)->chi(p) simultaneously for all p<=N.

For completeness, a nontrivial integer vector (h_p) has sum h_p log p !=0
by unique factorization. The mean of exp(-2it sum h_p log p) over [0,T]
tends to zero by direct integration. Finite trigonometric polynomials and
uniform approximation of continuous functions on the finite torus imply
that this continuous flow is equidistributed for Haar measure. Every open
neighborhood is consequently visited at arbitrarily large positive times.
Taking nested neighborhoods gives the lemma. This is the classical
Kronecker/Bohr mechanism, not probabilistic independence of actual primes.

It follows, uniformly on compact z sets, that

    P_N(z+iT_j)/(iT_j)->A_N^chi(z).                      (16)

Every u_(n,N) is fixed while j tends to infinity, so its divided contribution
vanishes. Equal prime-power phases are retained by complete multiplicativity.

The reflection in X_N does NOT eliminate this limit to the right of Re z=1/4.
Indeed, from (7),

    X_N(z+iT)/(pi^(-z-iT)Gamma(1+z+iT)iT)
     =P_N(z+iT)/(iT)
      +pi^(2z+2iT-1/2) Gamma(3/2-z-iT)/Gamma(1+z+iT)
                            *P_N(1/2-z-iT)/(iT).        (17)

On every fixed compact with Re z>=a>1/4, the second term is
O_(N,K)(T^(1/2-2a)) and tends to zero. This follows from the two vertical
Stirling bounds [G]; both gamma factors have the same exponential decay,
and the remaining power is EXACTLY 1/2-2Re z. The finite reflected polynomial
divided by T is bounded on K. No limit in N is being interchanged here.
Thus the normalized functions in (17) converge to A_N^chi on that half-plane.

**Zero-transfer lemma.** If A_N^chi has a zero z0 with 1/4<Re z0<1/2, then
F_N has zeros s_j with Im s_j->infinity and Re s_j->2Re z0.

Proof. A_N^chi is not identically zero: as Re z->infinity its value tends
to w_(1,N)>0. Choose a small disk around z0, lying in 1/4<Re z<1/2, with
zero-free boundary. By (16)-(17), Rouche's theorem gives a zero of the
normalized X_N(z+iT_j) inside that disk, counting multiplicities. The
normalizing gamma factor has no zero or pole there for large j. The factor
R_N has no zero there either, because its two gamma arguments have positive
real part. Taking decreasing disks and a subsequence proves the stated
limits; disjoint large translates give distinct zeros. Rescale s=2z.
No simple-zero hypothesis or computed approximate root is needed.

## 5. An explicit exact-arithmetic obstruction at N=256

Take chi(n)=(-1)^Omega(n), the Liouville function (Omega counts prime factors
WITH multiplicity). The checker evaluates the real polynomial (15) at
z=1/3 and z=1/2 with the following rigorous outward bounds:

    -0.022398637467469 < A_256^chi(1/3) < -0.022398637467468,
     0.249365651389428 < A_256^chi(1/2) <  0.249365651389429.
                                                               (18)

The weights are exact factorial ratios. At 1/2 every n^(-2z) is the rational
number 1/n. At 1/3, the 96-bit interval for n^(-2/3) is computed by INTEGER
cube-root bisection: if k=floor(cuberoot(floor(2^288/n^2))), then

    k/2^96 <= n^(-2/3) <= (k+1)/2^96.

Each endpoint is checked by cubing; all signs and 256 terms are retained.
An independently trial-factored Liouville list agrees with the sieve list.
There is no ordinary floating evaluation in this certificate.

The intermediate value theorem gives a real zero z0 in (1/3,1/2) of the
nonconstant A_256^chi. Section 4 then proves W2. Equation (18) does not
compute an ordinate of F_256, much less of xi. The infinite family is an
analytic consequence of recurrence and Rouche, not a finite experiment.

## 6. The finite proof step fails at EVERY sufficiently large cutoff

The explicit cutoff could in principle be discarded. This section proves
W3, so ignoring finitely many cutoffs does not fix the all-height argument.

Fix sigma in (1/4,1/2), with beta=2sigma. We will construct a phase chi such
that A_N^chi(sigma)=0 for every sufficiently large N.

Let P_N^*= {p prime: sqrt(N)<p<=(11/10)sqrt(N)}.
Two primes from this set, including a repeated prime, have product greater
than N. Therefore every integer n<=N contains at most one selected prime,
and contains it to the first power. For fixed phases on the OTHER primes,
the finite polynomial at sigma has the exact decomposition

    A_N^chi(sigma)=C_N+sum_(p in P_N^*) chi(p)B_(p,N),
    B_(p,N)=p^(-2sigma)sum_(m<=N/p) w_(pm,N)chi(m)m^(-2sigma).
                                                               (19)

No m in (19) has a selected prime factor: m<N/p<sqrt(N).

### 6.1 The selected prime coefficients cannot disappear

For n<=N/2, the elementary logarithm remainders give

    |log w_(n,N)+2n^2/N| <=4n^3/N^2.                    (20)

To check the constant, use |log(1-x)+x|<=x^2 and
|log(1+x)-x|<=x^2 for 0<=x<=1/2, sum over k<=n in the product (13), and
use sum k^2<=n^3. For N>=10^6 and p in P_N^*, (20) yields
log w_(p,N)>-3, since 2(11/10)^2+4(11/10)^3/1000<3.
For every allowed m>=2, (13) gives w_(pm,N)<=exp(-m^2).
Thus UNIFORMLY over all other phases,

    p^(2sigma)|B_(p,N)|
      >=exp(-3)-sum_(m>=2)exp(-m^2)m^(-2sigma)
      >1/40,                 |B_(p,N)|<p^(-2sigma).     (21)

One elementary rational check is enough: 8/3<e<11/4 implies
exp(-3)>1/21 and sum_(m>=2)exp(-m^2)<2/99, because successive square
exponents are separated by at least 5. Then 1/21-2/99>1/40. Also
sum_(m>=1)exp(-m^2)<3/8+2/99<1, proving the upper bound.

### 6.2 The rest of the polynomial has a bounded possible value

Average C_N over independent uniform unit phases for the finitely many
other primes. Distinct integers give distinct torus monomials, so exactly

    E_torus |C_N|^2
      =sum_(n<=N, no selected prime divides n) w_(n,N)^2 n^(-4sigma)
      <=zeta(4sigma)<infinity.                          (22)

Hence there exists a choice of those phases with |C_N|<=sqrt(zeta(4sigma)).
This is a FINITE torus averaging identity justified by unique factorization,
not a statistical hypothesis about the ordinary primes or Mobius signs.
Fix such a choice. The coefficient lower bounds (21) remain valid for it.

The ordinary PNT [P] gives

    |P_N^*| ~ (1/5)sqrt(N)/log N.

Consequently (21) implies

    sum_(p in P_N^*)|B_(p,N)|
      >=(1/40)(11/10)^(-2sigma)N^(-sigma)|P_N^*|->infinity,
    max_(p in P_N^*)|B_(p,N)|<=N^(-sigma)->0.             (23)

This is where PNT is used. The needed primes occupy a fixed-ratio interval,
not a conjectural short interval; no uniform PNT error or numerical cutoff
is imported. The thresholds may depend on the fixed sigma.

### 6.3 Complete polygon cancellation and zero transfer

For complex vectors with independently variable phases and prescribed
lengths r_1,...,r_k, the attainable moduli of their sum fill the interval

    [max(0,2 max r_j-sum r_j), sum r_j].

This follows by the two-vector triangle interval and induction, with
continuity filling intermediate radii; rotation supplies every argument.
By (23), the lower endpoint is zero for all large N, and the upper endpoint
exceeds sqrt(zeta(4sigma)). Choose the selected phases in (19) to sum to
-C_N. Then A_N^chi(sigma)=0 EXACTLY.

The zero-transfer lemma produces F_N zeros with real part approaching
2sigma=beta and imaginary part unbounded. This holds for every sufficiently
large integer N and proves W3. All primes and powers in the finite polynomial
are retained; chi is a device for studying actual vertical translates, not
an alteration of the fixed approximant F_N.

## 7. What happened to the intended complete RH proof

The following construction steps are supplied on paper:

1. Independent positive gamma variables produce an explicit finite Mellin
   approximation of the ENTIRE limiting xi function, with compact error O(1/N).
2. Reflection gives exact functional symmetry and a positive symmetric
   characteristic law; a separately stated nonvanishing gamma completion
   gives entire functions with xi's exact two endpoint values.
3. A finite all-height off-line zero-free theorem would pass to xi by Hurwitz.

Step 3's proposed premise is FALSE for these functions. W2 gives an explicit
cutoff and W3 rules it out for every sufficiently large cutoff. It is therefore
not left as an apparently routine lemma for a reviewer to invent. The global
probability/functional-equation proof attempted in this pass does not close.

The failure occurs in the transforms themselves, not just in a loose upper
estimate. For fixed N, arbitrarily high vertical translates expose the finite
prime-phase polynomial; on Re z>1/4 the reflected term becomes negligible.
Positive convolution variables and exact reflection do not control those
phases. At fixed s, by contrast, N->infinity recovers xi. Exchanging these
orders of limits is not licensed by (4).

This is NOT a counterexample to RH. It does not show the new zeros persist
at any fixed height as N grows. Nor does it refute every possible growing-
height, N-dependent theorem for this family, another probability law, or a
source-preserving Lee--Yang construction. A theorem proving suitable off-line
zero exclusion on expanding rectangles remains unproved, and could not be
obtained here by the attempted all-height finite-source theorem.

No new estimate of the original annular failure count, the residual minimum,
or the intrinsic entropy is claimed. This packet should be reviewed as a
whole-function construction and the demonstrated failure of its proposed
RH-completing zero lemma, NOT as a claimed unconditional proof of RH.

## 8. Dependencies, provenance and execution boundary

[BPY] P. Biane, J. Pitman and M. Yor, *Probability laws related to the Jacobi
theta and Riemann zeta functions, and Brownian excursions*, arXiv:math/9912170v1.
Equations (5)-(8), Sections 2.2 and 5 are the primary background. Our shape-two
partial fractions and convergence are rederived. Their Section 5.4 already
suggests the corresponding finite approximation; it is not claimed new here.
The PDF masthead displays a later typesetting date despite its v1 arXiv
identifier; no new theorem date is inferred from that display.

[G] NIST DLMF 5.11 (Stirling and gamma ratios), used on fixed vertical strips
and fixed compact parameter sets only. Gamma has no zeros. Hurwitz/Rouche,
finite torus Fourier approximation, and the identity theorem are classical
complex-analysis ingredients; the phase lemma's reduction is proved above.

[P] Ordinary prime number theorem, e.g. NIST DLMF 27.12.1, used only in (23).
It is unconditional, unlike the RH-conditional prime-error inputs in some
other repository packets. No zero-free region improvement is claimed.

Exact source freezes and reading scopes are in SOURCES.json. The finite
checker tests (7)-(9), positive moments by an independent convolution,
(18), and the rational constants and selected-prime monomial geometry. It
contains no gamma/zeta evaluation, numerical zero, contour quadrature,
phase-return computation, large-cutoff PNT check or proof-assistant build.
Finite agreement is not used to prove (4), W2, or W3. Independent mathematical
review remains required, particularly for the order of limits in Section 4,
the large-prime selection in Section 6, and the nonzero regularizer.
