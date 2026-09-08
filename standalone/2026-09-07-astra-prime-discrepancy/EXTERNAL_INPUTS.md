# External mathematical inputs and attribution

The uniform bounds (3), (4), and (6) use only elementary Euler products,
Chebyshev's binomial argument, the Cauchy Fourier integral, Fubini, partial
summation, and Lp inequalities. Their needed proofs are written in PROOF.md.
The finite-frequency kernel is exp(-|u-v|), not an independent-prime law.

The optional asymptotic (14) imports the classical prime number theorem
pi(x)~x/log x. No numerical constants from a PNT implementation are used.
The unconditional stopping-point discussion imports a classical remainder of
shape theta(x)-x=O(x exp(-c sqrt(log x))) for some c>0. For a primary modern
source giving stronger explicit versions, see:

Daniel R. Johnston and Andrew Yang, "Some explicit estimates for the error term
in the prime number theorem", arXiv:2204.01980.
https://arxiv.org/abs/2204.01980

The conditional paragraph (24) uses ONLY UNDER RH the classical implication
theta(x)-x=O(sqrt(x) log^2(2x)). A primary reference with refined explicit
RH-dependent bounds is Lee and Nosal, "Sharper bounds for the error in the
prime number theorem assuming the Riemann Hypothesis", arXiv:2312.05628v4.
https://arxiv.org/html/2312.05628v4

For surrounding finite-Euler-product literature, see S. M. Gonek, "Finite Euler
products and the Riemann Hypothesis", Transactions of the AMS 364 (2012),
2157-2191; arXiv:0704.3448.
https://arxiv.org/abs/0704.3448

These references supply background or the specifically labeled imports; they
do not prove the new packet's missing subpower estimate. No theorem about
ordinary pointwise critical-line Euler-product convergence is used. The new
higher-power convergence is in the stated weighted L2 norm.

No comprehensive external novelty search or independent referee acceptance is
claimed. The component results are source-specific combinations of classical
operations, submitted with complete proposed arguments for targeted review.
