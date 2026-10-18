# Independent read of the sparse-cut exponent consumer

Status: **source-qualified analytic review by the coordinating track.**
No new native contraction, zero-free boundary, or RH proof is asserted.

Source: #848, commit `99101457b32b6f10f4eda88ca998048404b860ea`,
`standalone/2026-09-12-astra-crossing-cofinal/PROOF.md`, Git blob
`0f9eac82fcbca61c7887a9fb71eb29d5a4181ce9`. The reviewer fetched and
read the complete proof at that identity, including its countermodels,
then independently reconstructed the load-bearing Sections 1 and 2.

Let Theta be the supremum of the real parts of nontrivial zeta zeros.
The source establishes an EVERY-PREFIX exponent limit

    log(1+F_Y)/log(Y+1) -> kappa=2Theta-1.

The distinction between a limit and a limsup is essential. A generic
monotone energy with only a polynomial bound does not permit the same
inference from arbitrarily sparse crossings.

The causal lower bound checks as follows. The finite completion of the
literal Mobius prefix with coefficient -M(Y) at Y+1 has full physical
energy E_Y. Its causal transform is C_Y(s)/s on s=z+1/2. The source's
factorial kernel has L1 norm at most6 and transform
(s-1)zeta(s)/s^2. Finite divisor inversion forces their convolution to
agree with exp(-t/2)(t-t^2/2) before log(Y+1). At ANY fixed zero
rho=beta+i gamma with beta>1/2, the transformed convolution vanishes,
whereas the reference transform equals (rho-1)/rho^3. The supported
future discrepancy and Cauchy--Schwarz therefore force
sqrt(E_Y)+O(1) >= c_rho (Y+1)^(beta-1/2) for EVERY Y. Taking the
supremum over fixed zeros proves the needed liminf, with no assumption
that the supremum is attained.

For the upper bound when Theta<1, the source reconstructs generalized
Littlewood: choose a strictly interior zero-free line sigma0>Theta.
Borel--Caratheodory on a disk centered at2+it bounds log zeta by log|t|;
three circles interpolates it with the bounded Euler logarithm on a
strictly smaller disk. This gives 1/zeta(sigma+it)=O_eta(|t|^eta)
uniformly for sigma>=sigma0 in the needed rectangle. Truncated Perron
at half-integers, height T=x^2, shifts without encountering poles and
gives M(x)=O_epsilon(x^(Theta+epsilon)). Partial summation then gives
m(Y)=O_epsilon(Y^(Theta-1+epsilon)) and the stated F upper exponent.
The Theta=1 endpoint is separately covered by |m(Y)|<=1. Thus the
argument does not assume a positive zero-free gap when none is given.

The unboundedness of native reciprocal sign crossings also checks:
the Mellin transform 1/[z zeta(z+1)] is analytic at every real z>-1,
but has a nonreal pole in that half-plane. If m were eventually of one
sign, Landau positivity would force its Laplace convergence abscissa
to a real singularity. The absence of such a real singularity would
instead make the integral analytic throughout Re z>-1, contradicting
the nonreal pole. Crossing through an exact zero is allowed.

Consequently, at ANY unbounded sequence of the exact native cuts,
an independently proved complete estimate

    F_((Y+1)^2-1) <= Y^(a+o(1))(1+F_Y)^p + Y^(e+o(1)),
    a,e>=0, 1<=p<2,

implies 2kappa<=max(a+p kappa,e), and hence

    kappa<=max(a/(2-p),e/2).

This is the exact consumer used for the zero-loss balanced reduction
(e=0) and the square-product alternative (e=2/3). No bound on the gaps
between selected cuts, no all-Y recurrence, and no finite numerical
trend are used. The new arithmetic estimates needed to activate this
consumer remain OPEN. This review found no blocking error in that
source-qualified implication; it does not constitute external referee
acceptance of the source or this new packet.
