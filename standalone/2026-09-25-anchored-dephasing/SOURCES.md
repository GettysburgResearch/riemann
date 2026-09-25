# ADP37 sources and attribution

## Frozen repository parent

- GettysburgResearch/riemann PR #907, CAP36, `c5ee83dc5f2f5f7ffa2d89b45298923a04e6cf0b`, `standalone/2026-09-25-completion-anchored-phase/PROOF.md`. Supplies the exact microscopic observable, its balance-invisible coordinate, capped source, factorwise compressed phase transport, and the distinction between comparison and absolute bounds.
- The parent head was read through the live GitHub connector. Its root tree is `66a7266de92c78775589ea99c6daf6b81792f8fb`. This continuation is add-only and does not alter inherited proofs or their statuses.
- CAP36's predecessor interfaces to MHB32/CQT32 remain as recorded there. Their full historical computations were not rerun here. We do not identify the microscopic mask with the full Newton covariance.

## Classical mathematical inputs

1. Finite geometric sums, the Fejer kernel, Fourier expansion of finite quadratic means, the Schur row bound, and the gcd parametrization of ab=cd. Complete proofs of the instances used are included. They are not new general harmonic-analysis or multiplicative-energy theorems.
2. H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Journal of the London Mathematical Society, second series 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`.
   https://doi.org/10.1112/jlms/s2-8.1.73
   The publisher's primary bibliographic record was checked. This is prior art for stronger separated-frequency/mean-value machinery, not an imported sharp theorem or constant. Our elementary Fejer/Schur proof is independent of any unverified weighted Hilbert-inequality constant.
3. NIST Digital Library of Mathematical Functions, Section 6.2: definition of Ci, its derivative, and the relation with the entire cosine integral.
   https://dlmf.nist.gov/6.2
   In particular Ci(x)=gamma+log x+integral_0^x(cos t-1)/t dt for x>0.
4. NIST DLMF 6.7.14, the auxiliary integral
   g(x)=integral_0^infinity cos(t)/(t+x) dt=integral_0^infinity t exp(-xt)/(1+t^2) dt.
   https://dlmf.nist.gov/6.7.E14
   Combined with DLMF 6.2.20 at x=2pi, this gives -Ci(2pi)=g(2pi). The polynomial lower bound on its Laplace integrand is proved in our note; it is not an uncontrolled asymptotic truncation.
   https://dlmf.nist.gov/6.2.E20
5. Elementary alternating arctangent series and Machin's identity, positive atanh series for logarithms, and Taylor's theorem for sin/cos. Their explicit remainders and outward use are recorded in VALIDATION.md. No numerical library special-function value enters acceptance.

External records were checked on 25 September 2026. No external or repository-wide priority claim is made. The contribution is the exact anchored, collision-preserving application to this observable and the actual-harmonic obstruction to generic principal extraction.

## Code provenance

The finite Mobius sieve/triangular inverse, cap definition, and Gaussian-rational arithmetic follow the project conventions in CAP36/RLC35. The new replay is a self-contained implementation; it is not an independent team's verification of the mathematics. The interval backend, actual harmonic/phase panels, collision counts, alias classification, Fejer tests, and CLI controls are local to ADP37. Historical check counts are not claimed as rerun here.
