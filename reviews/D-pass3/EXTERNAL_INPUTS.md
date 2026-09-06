# External and classical inputs — Reviewer D pass 3

These are imported background, not new repository theorems. No result is
accepted solely because it has a familiar structural name.

| Input | Exact use | Verification boundary |
|---|---|---|
| Jacobi theta inversion, psi(1/v)=sqrt(v)psi(v)+(sqrt(v)-1)/2 | R16 evenness and normalization of the actual Phi source | The identity is the classical Gaussian Poisson summation formula; the derivative and integration-by-parts adapter is reconstructed in R16. |
| Completed xi definition and functional equation | Fixed normalization xi(s)=s(s-1)Gamma(s/2)pi^(-s/2)zeta(s)/2 and reflected zeros | NIST DLMF 25.4.3–25.4.4; no zero verification or RH is imported. |
| Hurwitz Euler–Maclaurin with periodic B2 remainder | R21 square-root logarithmic ramp estimate, including exponent derivative | NIST DLMF 25.11(iii). Bound and differentiation integrability are checked in R21; no numerical zeta(1/2) primitive is used. |
| Hilbert transform on L2, pv kernel 1/(x-y) has norm pi | R18 separated finite-frequency inequality | Fourier multiplier has modulus pi; the discrete averaging and complete error bound are supplied here. The general literature comparator is H. L. Montgomery and R. C. Vaughan, “Hilbert's Inequality,” JLMS s2-8 (1974), 73–82, DOI 10.1112/jlms/s2-8.1.73. We do not assume its entire theorem to validate the flawed absolute-value argument. |
| Hilbert/RKHS interpolation and Schur complement | R16 finite minimum-norm formula | Derived from the positive finite Gram and least-norm right inverse, not a target-defined positive source. |
| Hadamard grouping, half-plane Blaschke convergence, and Stirling growth | S13 pole-removed inner factorization | The algebra after the factorization is reconstructed. The full common-map identification with the arithmetic source remains open. |
| Positive-measure Laplace continuity | R22 I_s to Lebesgue cumulative limit | Standard continuity theorem; the additional one-sided slope argument is indispensable and is reproduced. No derivative of a weak limit is taken. |
| PNT and Mertens prime product | S14–S15 asymptotic cutoff and product-boundary bounds | Only classical asymptotic statements: sum_(p<=Z)p^-1/2~2sqrt(Z)/log Z and product_(p<=Z)(1-1/p) of order 1/log Z. No explicit numerical threshold is claimed. |
| Dickman/de Bruijn and Vinogradov–Korobov inputs | Previous D2 source-comparison arguments after R21 supplies the base variation | Previous exact version and quantifier qualifications remain; this pass does not reclassify these as native new mathematics. |

Primary online references checked during this pass:

- NIST DLMF, section 25.4: `https://dlmf.nist.gov/25.4`.
- NIST DLMF, section 25.11(iii): `https://dlmf.nist.gov/25.11#iii`.
- NIST DLMF, section 20.7(viii), theta modular transformations:
  `https://dlmf.nist.gov/20.7#viii`.
- Montgomery–Vaughan journal record, DOI `10.1112/jlms/s2-8.1.73`.

No PDF figure, external proof archive or upstream formal library was analysed
or executed in this pass. A citation is an input declaration, not a replay.
