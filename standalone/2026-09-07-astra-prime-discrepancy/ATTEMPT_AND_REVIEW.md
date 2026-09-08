# Direct completion attempt and review boundary

Status: INCOMPLETE RH ATTEMPT; proposed component proofs available for review.
No statement in this packet supplies an unconditional RH proof.

## What the direct attack changed

The previous route introduced an adaptive tanh feedback and bounded its nonlinear
prime-jump corrections by O(log log X). The present calculation bypasses that
feedback altogether: the exact critical entropy differs by a uniform constant
from one half of the L1 norm of the real LINEAR prime discrepancy C_X.

The pointwise prime-square sum at y=0 diverges, but that is not the relevant
norm. The complete Cauchy-weighted L2 norm of all higher powers converges, with
an explicit infinite-tail bound. Treating pointwise divergence as a growing
whole-frequency cost loses information here. Conversely, L2 convergence does
not justify pointwise convergence at y=0.

The norm of the linear field has an exact scalar-state representation in terms
of R(x)=sum_(p<=x)sqrt(p)-integral_2^x sqrt(u)/log(u)du. This is an ordinary
weighted prime-counting discrepancy, not a new unknown operator or a freely
chosen source. Its squared energy retains every signed interaction.

## The attempted last inequality

The desired statement was an unconditional bound, on the actual primes,

    I(X)=integral_2^X R(x)^2/x^3 dx+R(X)^2/(2X^2)
                  <=C_epsilon X^epsilon for every epsilon>0.  (OPEN)

It would imply the parent's entropy criterion by the proved norm inequality.
Together with the classical RH-to-prime-error implication it is equivalent to
RH. There is no claim that this restatement is independently easier than RH.

I tried to obtain (OPEN) by Stieltjes integration of the exact first-prime
source and the available unconditional bound for theta(x)-x. The calculation
is PROOF.md (23)-(25). It gives only I(X)<<X exp(-c sqrt(log X)). No sign
cancellation is provided by taking the square in I. Diagonal-only evaluation
would discard the prime/continuum and off-diagonal terms and is not legitimate.

The conditional estimate R(x)=O(x log x) gives I=O(log^3 X), hence the sharper
conditional entropy bound E=O(log^(3/2) X). That paragraph assumes RH and is
not part of an unconditional completion. No implicit bootstrapping across
that assumption is allowed.

## Why the PNT-size hypotheses alone cannot pay the bound

The following continuous positive source is a CONTROL ONLY, not ordinary primes,
not a discrete prime system, and not a counterexample to RH. For a fixed
0<delta<1/2 set beta=1/2+delta and let

    dPi_beta(x)=[1+x^(beta-1)] dx/log x, x>=2.

It is positive. Its difference from the continuum has cumulative mass
O_beta(x^beta/log x), which is smaller than x exp(-c sqrt(log x)) for every
fixed c>0, for all sufficiently large x. Thus it satisfies the scale of the
ordinary PNT error bound, with constants adjusted on a compact interval.

Its corresponding linear discrepancy is

    C_X^beta(y)=integral_2^X x^(delta-1-iy)/log x dx.

For X>=2^(2/delta) and |y|<=1/log X, cos(y log x)>=1/2 for every 2<=x<=X.
On [sqrt X,X], 1/log x>=1/log X. Hence

    Re C_X^beta(y)>=X^delta/(4delta log X).

The Cauchy mass of that frequency interval is at least 1/(pi log X) when
log X>=1. Consequently

    ||Re C_X^beta||_(1,mu)>=X^delta/[4pi delta (log X)^2].

It is not subpower. For delta=1/4 the lower bound is
X^(1/4)/[pi(log X)^2] for X>=256.

This rejects a universal argument based only on positive density, the complete
Cauchy measure, and a classical-scale PNT remainder. It does NOT reject an
argument exploiting additional identities of the ordinary primes. In particular
it does not satisfy the exact ordinary integer/factorization identities, and
no such identities are claimed for it.

## Scope of the conditional completion

A subpower upper bound for ||Re C_X||_1 is exactly the needed growth target up
to the uniform additive error. I(X) is a sufficient quadratic majorant. For
actual primes, its subpower subsequence version is also RH-equivalent because
RH supplies a polylogarithmic bound. The manuscript does not identify L1 and
L2 pointwise or assert a reverse uniform norm comparison.

The use of OEC26.T3 is source-pinned and explicit: the parent proves that an
off-line zero forces E(X)>=c X^nu-C for each smaller positive exponent and all
X. The present norm bound then implies a positive growth exponent for I.
The parent component remains proposed mathematics requiring independent review;
this contribution is not independent acceptance of it.

## Review checklist

1. Verify the prime-square double sum (10), including its diagonal and the
   factor 1/2 on ordered off-diagonals, and the UNIFORM tail estimate (11).
2. Check the transition from finite square sums to the full L2 limit, and
   distinguish this from the pointwise exceptional frequency zero.
3. Audit the initial-field L2 bound and the exact signed mean. These are what
   make the additive linearization error independent of X.
4. Verify both Fourier normalizations in (20)-(22), including the real-part
   correction and the entire stopped-state future R(X)^2/(2X^2).
5. Keep the prime-2 lower boundary in (23), and keep the unconditional,
   PNT-dependent asymptotic, and RH-dependent conclusions separate.
6. Do not infer a new bound on R from the fact that its integrated energy is
   nonnegative. The upper estimate (OPEN) is the missing arithmetic statement.

No complete entropy/discrepancy quadrature or prime-counting-error campaign was
run. The exact checker verifies finite rational Fourier/state identities and
constants, not any unbounded estimate. Details are in VALIDATION.md.
