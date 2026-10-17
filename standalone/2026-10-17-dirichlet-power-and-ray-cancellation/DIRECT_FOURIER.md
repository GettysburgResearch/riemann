# A direct power bound for finite reciprocal Dirichlet products

Status: PROPOSED complete deduction from the explicitly stated common-strip
input and the elementary estimates proved below. Independent mathematical
review is required. The application imports the reported OpenAI common
7/8 strip for all Dirichlet L-functions; that deep theorem is not proved or
formally certified here. This is not a new zero-free region or RH proof.

The rational Möbius case belongs to the classical Baker--Harman weak-GRH
exponential-sum theory. The contribution here is a written adapter for a
fixed finite product of reciprocal Dirichlet L-functions, with the exact
complete Eisenstein norm source as its first application. No global
priority claim is made for this extension, Vaughan/Heath--Brown identities,
or the major/minor-arc method.

## 1. The theorem and the exact source

Assume ZF(theta): EVERY primitive Dirichlet L-function has no zero in
Re(s)>theta, where 2/3<=theta<1. Principal poles at one are permitted.
Fix an integer r>=1 and Dirichlet characters xi_1,...,xi_r of fixed moduli,
with their usual zero extension. Define the ordinary Dirichlet convolution

    a=(mu xi_1)*...*(mu xi_r),
    A(s)=sum a(n)n^(-s)=product_j L(s,xi_j)^(-1), Re(s)>1.

For every epsilon>0,

    sup_(alpha real) |sum_(n<=x) a(n)e(alpha n)|
         <<_(theta,epsilon,r,xi) x^((1+theta)/2+epsilon), x>=2.   (1)

Here e(v)=exp(2 pi i v). Constants do not depend on alpha or a rational
approximation to it. The characters and r are fixed, not growing with x.
This theorem retains every integer coefficient, including imprimitive
zeros and all repeated-prime terms allowed by the convolution.

For K=Q(sqrt(-3)), with chi=chi_{-3}, the COMPLETE rational-norm coefficient
of 1/zeta_K is exactly

    a_K(n)=sum_(N I=n) mu_K(I)=mu*(mu chi)(n).                 (2)

For example a_K(p)=-2 at a split prime and a_K(p^2)=1; at an inert
prime a_K(p)=0 and a_K(p^2)=-1. The unique ramified prime has local
factor 1-3^(-s). Formula (2) follows directly from the splitting Euler
factors; distinct ideals of equal norm are all included. It is not an
application of a one-bounded theorem to a_K.

At the reported theta=7/8, (1) gives

    sup_alpha |sum_(n<=x) a_K(n)e(alpha n)| << x^(15/16+epsilon). (3)

The same exponent holds for every fixed r. A largest-factor convolution
bound applied only AFTER the rational Möbius theorem would instead lose
a factor r in the power saving. The direct finite inverse identity below
avoids that loss for the uncapped convolution. Separately capped factors
require the adapter and exponent stated in COMPLETION_AND_COVARIANCE.md.

## 2. Analytic major arcs

STRIP_AND_MAJOR_ARCS.md proves the following statement for the very same
coefficients and hypothesis. For reduced b/q, q>=1, beta=alpha-b/q,

    |sum_(n<=x) a(n)e(alpha n)|
       << x^(theta+epsilon) q^(1/2+epsilon)
                       (1+x|beta|)^(1/2+epsilon).             (4)

Only polynomially bounded x,q,1+x|beta| are needed below, so arbitrarily
small losses in its constituent estimates can be absorbed into epsilon.
The proof uses the uniform reciprocal bound furnished by ZF(theta),
oscillatory Mellin inversion, and a full q-supported cofactor decomposition.
It does not infer conductor-uniform bounds from unspecified constants in a
fixed-character Möbius estimate.

For clarity, that cofactor is d=(n,q^infinity), NOT gcd(n,q). It satisfies
d|rad(q)^r, since a(p^e)=0 for e>r; writing n=dm leaves (m,q)=1.
Multiplicativity gives a(n)=a(d)a(m). The rational phase reduces modulo
q/gcd(q,d), and character orthogonality retains all the zeros at primes
dividing q. Its Gauss expansion has l1 norm at most sqrt(q/gcd(q,d)).
The complete cofactor sum costs a bounded factor after sqrt(q), since

    sum_(d|rad(q)^r) |a(d)| d^(-theta)/sqrt(gcd(q,d))
      <= product_(p|q) [1+sum_(e=1)^r binom(r,e)
                         p^(-theta e-min(e,v_p(q))/2)]
      <<_(r,theta) 1.                                      (5)

The last product is uniformly bounded because theta+1/2>1. No shared-prime
terms or high valuations of q have been erased.

## 3. A finite inverse identity with no analytic remainder

Put kappa=1-theta, so 0<kappa<=1/3. Choose a fixed integer J>=1/kappa.
On a dyadic interval x/2<n<=x let U=ceil(x^(1/J)), and let a_U(n) be a(n)
for n<=U and zero otherwise. Let b=xi_1*...*xi_r, so a*b is the unit
for Dirichlet convolution. Then, for EVERY integer n<=x,

    a(n)=sum_(j=1)^J (-1)^(j-1) binom(J,j)
                       (a_U^(*j)*b^(*(j-1)))(n).             (6)

Proof. In formal Dirichlet series put E=1-B A_U. Its coefficients vanish
for n<=U, including n=1: B A_U agrees there with B A=1. Consequently
E^J has no coefficient at n<(U+1)^J, and neither does A E^J. Expanding
A(1-E^J), and using A B=1, gives the right side of (6). Since U^J>=x,
the omitted formal series contributes exactly zero through x. QED.

This is finite coefficient algebra. There is no convergence assumption,
unbounded moment order, smooth truncation, or small analytic error in (6).
All r(J-1) factors from b are expanded individually as the Dirichlet
characters xi_j; the other j factors are a_U. Their coefficients satisfy
|a(n)|<=d_r(n), hence every grouped coefficient is bounded by a fixed
divisor function. For each fixed eta>0 this is O_eta(n^eta).

## 4. Two elementary exponential-sum estimates

### 4.1 Type II

If (b,q)=1 and |alpha-b/q|<=q^(-2), coefficients bounded by fixed divisor
functions on m~M,n~N satisfy

    |sum_m u_m sum_n v_n e(alpha mn)|
      <<_eta (MN)^(1+eta)
         (q^(-1)+M^(-1)+N^(-1)+q/(MN))^(1/2).              (7)

This remains valid after fixed powers of logarithms, fixed multiplicative
characters, or arbitrary unit-modulus twists are put in either coefficient.

Proof. Cauchy in m, followed by expansion of the n square and geometric
summation in m, bounds the square by

    << (MN)^(1+eta) [M+sum_(1<=h<=2N) min(M,||alpha h||^(-1))].

In each block of length at most q/2, the alpha h are separated modulo one
by at least 1/(2q). This follows by subtracting the rational approximation;
for distinct indices their difference has modulus at least 1/q before an
error of at most 1/(2q). A block therefore contributes
O(M+q log(2q)) to the last sum. There are O(1+N/q) blocks. Thus the bracket
is O((MN/q+M+N+q) log(2q)), which gives (7), after renaming eta.
For q=1 the conclusion is the trivial bound and follows directly. QED.

A cutoff mn<=x can be separated with a logarithmic loss. Evaluate truncated
Perron at the half-integer floor(x)+1/2 on the line c=1/log(2x), with height
x^A for a fixed sufficiently large A. The distance of an integer product
from that cutoff is at least 1/2; summing the usual truncation errors over
the divisor-bounded coefficients is O(x^(-1)). On each Perron height the
factors m^(-it) and n^(-it) have modulus one, and the integral of
|c+it|^(-1) is O(log x). This proves the asserted cutoff version without
using derivatives of the arbitrary coefficients.

### 4.2 The Type I estimate needed here

Suppose the STRONGER approximation |alpha-b/q|<=1/(qQ) holds, with

    x^kappa << q<=Q, Q comparable to x^(1-kappa),
    1<=M<<x^kappa.

Let xi be any one of the fixed Dirichlet characters. In a dyadic product
box m~M, n~x/M, summing the n factor xi(n)e(alpha mn) on ANY subinterval
costs at most a fixed multiple of

    min(x/M, ||c_xi alpha m||^(-1)),

by separating its fixed residue classes; c_xi is its fixed modulus.
The complete sum in m, with divisor-bounded coefficients, is

    <<_eta x^eta (x/q+q) log(2x) << x^(1-kappa+eta).          (8)

Here and below harmless fixed constants in dyadic lengths only change
implied constants. To justify (8), reduce c_xi b/q to denominator q',
where q/c_xi<=q'<=q. Its error on m<<x^kappa is O(c_xi x^kappa/(qQ)),
which is o(1/q') because kappa<1/2. Nonzero rational residues remain a
distance at least a fixed multiple of 1/q' from zero. Within a complete
q' block their reciprocal distances sum to O(q' log(2q')). Multiples of
q' contribute at most O((1+M/q')x/M). If the interval's upper endpoint
is below q', there are none; otherwise M is at least a fixed multiple
of q', so each contributes O(x/q'). Since M/q'=O(1) in this Type I
range, this proves O((x/q'+q')log(2x)).
Splitting a bounded number of extra blocks treats all fixed dyadic constants.
The finitely many small x for which the separation inequality is not yet
valid are absorbed in the constant. This proof needs no character-sum
estimate for a growing modulus; c_xi is fixed.

## 5. Cover all frequencies and every inverse-identity box

Use Dirichlet approximation with Q=floor(x^(1-kappa)) to obtain reduced
b/q with 1<=q<=Q and |alpha-b/q|<=1/(qQ).

If q<=x^kappa, (4) gives, after allocating its epsilon losses,

    x^theta sqrt(q+x/Q) x^epsilon
       << x^(theta+kappa/2+epsilon)
        = x^(1-kappa/2+epsilon).                            (9)

For q>x^kappa use (6), expanding every factor and putting it in a dyadic
interval. There are only O((log x)^(J+r(J-1))) boxes; J and r are fixed.
Keep only boxes whose product interval meets (x/2,x]. Each product of
dyadic lengths is comparable to x by a constant depending on J,r.

If any variable has size larger than x^(1-kappa), it must be one of the
long character variables: all the a_U variables have length O(x^(1/J))
with 1/J<=kappa. The product of its cofactors is O(x^kappa). Keep its
actual upper endpoint from the product cutoff, sum that character variable
geometrically, and apply (8). Multiple cofactor tuples giving the same
integer have divisor-bounded total absolute weight; (8) applies to them
without deleting tuples. Their different admissible endpoints cause no
change, since the geometric estimate is uniform over subintervals.

Otherwise every variable has size O(x^(1-kappa)). If a variable already
has size at least x^kappa, put it in one group and all remaining variables
in the other. Both grouped lengths are at least a fixed multiple of
x^kappa. If every variable is smaller than x^kappa, multiply variables
in their fixed order until their product first reaches x^kappa. This
group is at most x^(2kappa), and its complement is at least a fixed
multiple of x^(1-2kappa)>=x^kappa. This covers all boxes because the
complete product is comparable to x. Equality kappa=1/3 is allowed.

Now (7), with its cutoff version, gives

    << x^(1+epsilon) (x^(-kappa))^(1/2)
     = x^(1-kappa/2+epsilon),                               (10)

since q>=x^kappa, q<=x^(1-kappa), and both grouped lengths are at least
constant multiples of x^kappa. All the powers of logarithms and fixed
divisor estimates are absorbed by choosing smaller positive losses first.
Equations (9)--(10) prove the theorem on each dyadic interval; summing them
proves (1). The interval near n=1 contributes only a bounded term.

## 6. What this result supplies

This supplies a genuine positive power saving, uniform in an arbitrary
additive phase, for the actual complete norm source. Its proof uses the
common zero-free strip only in the major arcs; finite inverse algebra and
bilinear cancellation handle the remaining frequencies. Neither a random
prime model nor a family-to-principal extraction occurs.

It does not improve the imported strip, prove square-root cancellation, or
justify a critical-energy bound. At alpha=0 the imported strip already
gives a stronger exponent theta+epsilon by ordinary Perron inversion.
The extra conclusion of (1) is uniformity over ALL additive frequencies,
not a stronger bound for the untwisted partial sum. The completed-source
and covariance consequences retain this exact distinction.
