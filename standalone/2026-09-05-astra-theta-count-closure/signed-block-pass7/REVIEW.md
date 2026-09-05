# Sources, continuation decision, and review contract

This manuscript continues a requested full-sign attempt. It does NOT prove RH.
Review the exact committed files, not an earlier PR description or a PASS flag.

## Source boundary

The published PR790 checkpoint was read at f0584f7a49550540eaed005868422a83cb3e1011.
Its import receipt confirms that prime-cutoff-pass6 was applied unchanged on
top of 288aa2b0ecf5965c5cf6bb421f69b238de6507cc, retaining signed-tail-pass6.
The nine imported file identities were compared against the supplied local
packet. The prior heat-Hankel proof and original low-zero code are retained,
not silently edited. The root SHA pinned here is the scientific parent,
not a claim that it remained the branch tip forever.

Cross-branch reading in this pass: PR793's PRIME_TAIL_TRANSITION.md at
 a4366436a248102f86f0d692366ca705cad3fca9 was read in full, and PR792's latest
cutoff disposition was read at PR-summary level. Their conclusions are not
inputs to our theorems. In particular this packet does not repeat the
already-refuted plan to prove positivity of raw finite prime cutoffs.
The ten-dimensional source certificate in signed-tail-pass6 was read at
README level; its computational suite and full proof were not re-reviewed.

## Classical inputs

1. Platt--Trudgian, The Riemann hypothesis is true up to 3*10^12,
   Bull. London Math. Soc. 53 (2021), 792--797,
   https://arxiv.org/abs/2004.09765 and https://doi.org/10.1112/blms.12460.
   Only V100 is used, in ASTRA-SB-01. The full published computation is
   imported, not rerun. No finite verification is used in SB-02 through 05.
2. NIST DLMF https://dlmf.nist.gov/18.3, /18.8 and /18.9:
   Jacobi/Legendre/Laguerre orthogonality, differential operators and recurrence.
   The exact energy inequalities needed here are reproved by integration by
   parts and degree-preserving symmetry in PROOF.md, not presumed from a
   fitted polynomial calculation. These are standard tools, not new general
   orthogonal-polynomial theorems.
3. NIST DLMF https://dlmf.nist.gov/5.4#E4 and /5.5:
   Gamma reflection, duplication, and absolute value at 1/2+it.
4. The unconditional Guinand--Weil explicit formula in the parent heat-Hankel
   proof, with full zero multiplicities and Fourier exponent exp(-ilx).
   Its parent external pin is Chirre--Goncalves, Math. Z. 300 (2022),
   Proposition 5, https://doi.org/10.1007/s00209-021-02820-9.
   No RH-conditional theorem in that source is imported.
5. The standard invariant product and xi reflection convention are unchanged;
   NIST DLMF https://dlmf.nist.gov/25.4 gives the completion convention.

## Six-sign analytic error contract

For s=1/2+it the Euler transformed eta series is

 eta(s)=sum_(k>=0) 2^(-k-1) sum_(j=0)^k (-1)^j binom(k,j)(j+1)^(-s).

Indeed (j+1)^(-s) has its usual Gamma integral. The inner binomial sum is
Gamma(s)^(-1) int_0^infinity x^(s-1)exp(-x)(1-exp(-x))^k dx.
Summing the geometric series recovers the eta integral. Absolute convergence
of the transformed series on Re s>0 follows from the same integral bound.
After N outer terms the error magnitude is at most

 [Gamma(1/2)/|Gamma(1/2+it)|] 2^(-N)=sqrt(cosh(pi*t))2^(-N).

At the six integer ordinates, |t|<=26 and N=192. Since
26*pi/2<41, e<3 and 3^41<2^66, the error is <2^(-126).
The script encloses it in the slightly larger complex rectangle with both
coordinate radii 2^(-120). Finite binomial weights are EXACT rationals.
All logarithms, exponentials, pi and Gamma evaluations then use mpmath.iv at
80 decimal digits, with version 1.3.0 explicitly checked. Its interval Gamma
implementation is a software trust dependency, not a kernel-certified theorem.

Xi(t)=xi(1/2+it) is real for real t by reflection and conjugation. Thus the
six strict signs prove one line zero in each of the three intervals. They
prove neither simplicity, exact zero counts in the intervals, nor V100.

## Priority proof review

First check the generalized-Vandermonde/Schur factorization and Cauchy step and the whole-tail factor theta_M in
(9): all signed coefficients must survive until AFTER the positive reservoir
is formed. The Schur ratio must be bounded at COMPLEX tail nodes uniformly in
the exponent gaps; its nonnegative coefficient expansion is supplied explicitly.
Check that 196, 678 and the minimum gap 141 follow from the
actual intervals, and that theta_5<1/3 uses rational arithmetic.

Next check the Jacobi norm, its endpoint exponents, and (16); the derivative
energy has eigenvalue D(D+beta+1/2), not a shifted convention. Check the
Legendre evaluation bound on a COMPLEX unit disk and the all-parameter
exponent in (20). The sum in (22) is weighted by 1/Re A before it is bounded.

Finally check endpoint zero, Fourier factors 4pi and 2, the sign of the
omitted tail, and the metric of the norm I. The escaping-space proof must
use the ORIGINAL time L2 metric, not I. The synthetic witness is a different
source and does not contradict the actual three-node theorem.

The claim labels are local research labels. No external priority, independent
referee acceptance, or canonical integration is asserted.
