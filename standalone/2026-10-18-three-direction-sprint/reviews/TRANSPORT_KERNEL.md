# A pointwise estimate for the complete close-product transport kernel

Status: **PROPOSED elementary component lemma.** This estimates the full
harmonic-remainder source before its native denominator and core
projections. It does not estimate those projections or the reweighted
remainder. It is intended as a sharpening of the transport construction in
rational/, with no assumed cancellation among the target coefficients.

Let Y>=2, 1<=G<=Y^2/8, and let A be any set of distinct integers in
[Y^2/4,Y^2]. For each N in A choose an arbitrary probability distribution
pi_N on positive integers M satisfying |M-N|<=G. Repeated reference
products and repeated reference pairs are allowed. Define, for x>0,

    R(t)=H_floor(t)-log(t)-gamma,
    W(x)=sum_(N in A) (2/N) sum_M pi_N(M)[R(x/N)-R(x/M)].

Then throughout the full range 0<x<=2Y^2,

    |W(x)| <= 120(G+1)/Y^2,
    integral_0^(2Y^2) |W(x)|^2 dx <= 28800(G+1)^2/Y^2.       (1)

The discrete sum over at most 2Y^2+1 physical unit cells satisfies the
same bound with the corresponding cell count in place of 2Y^2. This
applies to the entire strict native step [Y,(Y+1)^2), since its endpoint
is below 2Y^2 for Y>=3.

## Proof retaining every harmonic jump

The Euler constant and log x cancel exactly:

    R(x/N)-R(x/M)
       =H_floor(x/N)-H_floor(x/M)+log(N/M).

Because min(N,M)>=Y^2/8,

    |log(N/M)|<=8G/Y^2.

There are at most Y^2 distinct integers in A and 2/N<=8/Y^2, so the
total logarithmic contribution is at most 64G/Y^2.

Write the harmonic-number difference as the complete finite sum

    sum_(j>=1) (1/j)[1_(x>=jN)-1_(x>=jM)].

For 0<x<=2Y^2, only j<=16 can contribute. Whenever the two indicators
differ, the real number x/j lies between N and M. In particular
|N-x/j|<=G. At each fixed x,j there are at most 2G+2 possible distinct
integer targets N. Each has total reference probability one; no estimate
for the multiplicity of a reference product is required. Hence all jump
contributions together have absolute value at most

    16(G+1) H_16/Y^2.

Since 64+16H_16<120, the first part of (1) follows. Squaring and
integrating proves the second. Every common jump, the small-argument
logarithm, and the upper part of the physical output interval have been
retained. This proof neither discards a floor-function discontinuity nor
uses a triangle inequality for the individual L2 norms of the modes.

## Use and limits for the actual top-prime targets

For unordered distinct primes p,l in (Y/2,Y], the products N=pl are
distinct and satisfy the hypotheses. If their reference products M=ab
come from squarefree old inputs a,b<=Y and have an even product, no
reference can be divisible by an odd top-prime target. Indeed each of
p,l has only one multiple among positive integers <=Y, namely itself;
divisibility by pl would force {a,b}={p,l}, giving an odd product. The
displayed full kernel therefore retains each top target's canonical
S_(pl) coefficient 2/(pl), including contributions from every reference.

The conversion R(x/d)=sum_(q|d) S_q(x) changes many complementary
denominator coefficients. Those must still be paid under the actual
moving low-denominator cutoff and the actual small-core cutoff. A
pointwise estimate for W does not imply the same estimate for either
projection. In particular (1) alone is not a bound for the complete
native rough amplitude and is not a new zeta zero-free estimate.

For transport gap G=Y^(7/10+eta), the full-kernel energy in (1) is
O(Y^(-3/5+2eta)); thus, if such references are supplied with controlled
input weights, the full-kernel term is much cheaper than its separate
mode L2 triangle bound. Projection costs may then be the binding terms.
