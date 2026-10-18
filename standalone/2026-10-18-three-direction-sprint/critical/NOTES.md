# Critical Gaussian covariance exploration

Status: WORK IN PROGRESS / PROPOSED. Ordinary zeta only. No critical energy
upper estimate or new zero-free boundary is asserted.

Source: #994 at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`standalone/2026-10-18-theta20-and-native-cancellation/critical/ARITHMETIC.md`,
Git blob `56f0195a8b7471fc7409c0f8f55432d9c9ec44fc`.

The original coefficient is `a(n)=n^-1 product_(p|n)(1-p)` with `a(1)=1`.
The exact finite-horizon Gaussian Gram kernel retains the normal-CDF factor.
We explore actual signed primitive-ratio sectors, not independent random signs.

## Initial attacks

1. Pay the complete sector with `min(r,s)<=S` in the primitive decomposition
   `(n,m)=(rd,sd)`, `(r,s)=1`, by an absolute `O(S(1+log T))` bound. This allows
   any subpower growing S, not only the fixed divisibility sector in #994.
2. Establish a mean for `a(pd)a(qd)` uniform in distinct primes p,q, using two
   explicit absolutely convergent Euler modifications of the known a(n)^2
   mean. This should expose a polynomially large positive balanced prime-ratio
   sector at growing scales, which must be canceled by its complement.
3. Explore the complete primitive-ratio sector supported on a finite prime set.
   Its local Fourier factor is `1+2 Re sum_(j>=1) beta(p^j)p^(-j/2-ijt log p)`.
   Positivity and growing-prime behavior need an exact proof, not a fitted trend.

Every failed approach, meaningful finite calculation and resulting theorem will
be recorded with its actual scope. None of these sector arguments may erase
the cross-sector signed contribution of the full energy.
