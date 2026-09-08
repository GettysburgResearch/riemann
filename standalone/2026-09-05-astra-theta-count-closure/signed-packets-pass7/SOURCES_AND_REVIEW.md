# Sources, attribution, and review boundary

The local labels SP7-1 through SP7-6 are proposed mathematical claims, not
canonical IDs, and not independently accepted results. No external novelty
claim is made. Jacobi/Legendre energy and interpolation arguments are
classical; the contribution offered here is their explicit source-normalized
application with all coefficient and tail budgets retained.

## Repository reads and exact pins

Repository: GettysburgResearch/riemann, stable ID 1309150028.
Current scientific base: f0584f7a49550540eaed005868422a83cb3e1011.

- PRIME_CUTOFF_IMPORT.md was read at that exact head. It records unchanged
  publication of prime-cutoff-pass6 and preservation of signed-tail-pass6.
- prime-cutoff-pass6/PROOF.md was read from the retained attachment; its
  locally recomputed Git blob is d9354917157bb80175093b6b44fc01a46ba4ffea,
  matching fresh remote metadata at the current head.
- signed-tail-pass6/PROOF.md was read remotely through its analytic cutoff
  and tail arguments and the statement of its ten-dimensional certificate.
  The certificate's interval implementation was NOT independently replayed
  in this continuation. No review verdict on that certificate is asserted.
- The heat-Hankel normalization comes from heat-hankel-pass5 at
  bce97be9727dea9968db7517738edc966d2cc86b, whose archived proof blob is
  caf9753e5c3e3bb918289da0f4e92ae7c6441f6c. The source constant argument
  needed here is rederived in S1, rather than importing the full operator
  approximation or inertia package.

Both pass-6 packets prove cutoff indefiniteness and selected signed tail
bounds. The unbounded-dimension theorem here is an ARBITRARY-VECTOR matrix
bound, using a degree-uniform polynomial concentration estimate. It is not
another instance of entrywise signs. The actual three-dimensional full
positivity theorem is a separate finite-real-reservoir argument.

## Classical references checked during this continuation

[D1] NIST DLMF 18.3, Table 18.3.1: Jacobi and shifted Legendre orthogonality.
https://dlmf.nist.gov/18.3

[D2] NIST DLMF 18.8, Table 18.8.1: the Jacobi differential equation and its
polynomial eigenvalues. The finite self-adjoint operator proof is supplied
in full in S9; a new Jacobi spectral theorem is not claimed.
https://dlmf.nist.gov/18.8

[D3] NIST DLMF 5.4 and 5.7: digamma special values/partial fractions, and
|Gamma(1/2+it)|^2=pi/cosh(pi t).
https://dlmf.nist.gov/5.4
https://dlmf.nist.gov/5.7

[D4] NIST DLMF 5.12: Euler beta integral and its Gamma evaluation. The
verifier uses exact normalized beta-moment ratios, not floating Gamma values.
https://dlmf.nist.gov/5.12

[EF] The parent explicit-formula normalization imports Proposition 5 of
Andres Chirre and Felipe Goncalves, 'Bounding the log-derivative of the
zeta-function', Mathematische Zeitschrift 300 (2022), DOI
10.1007/s00209-021-02820-9. Only the unconditional Guinand--Weil proposition
is used, NOT the paper's RH-conditional main estimates. The article HTML
was opened; no fresh PDF hash or page audit is claimed here.
https://link.springer.com/article/10.1007/s00209-021-02820-9

[V1] David Platt and Timothy Trudgian, 'The Riemann hypothesis is true up to
3*10^12', arXiv:2004.09765 (published in Bulletin of the London Mathematical
Society). Its theorem is used ONLY through height 100 in SP7-4. The abstract
and theorem scope were checked online; the full published verification was
not rerun and no new paper review is claimed.
https://arxiv.org/abs/2004.09765

Related, not a new dependency: D. R. Yafaev's sign/inertia theory of Hankel
operators is the established context for the parent. The new finite-cluster
argument in B11 is proved directly by interpolation and finite inertia
stability, with no unproved general infinite-Hankel theorem assumed.

## Priority review

1. Check both powers of (1-t) and the factor c in the exact change S8.
2. Check self-adjointness and the polynomial spectrum in S9, then the
   Cauchy--Schwarz step with t/(1-t). This is where arbitrary coefficient
   cancellation is controlled without a coefficientwise estimate.
3. Check the Legendre evaluation bound on the COMPLEX unit disk, the core
   lower bound, and the monotonicity in x used for the complete zero sum.
4. Check the all-d, all-m logarithmic inequalities in S15; the finite tests
   do not replace that parameter proof.
5. Check the sign and factor 2pi in S5, and retain the distinction among the
   full form Q, the literal cutoff Q_X, and the omitted tail T_X.
6. Check the exact metric S6. It is a real-frequency Gram metric, not the
   time-domain L2 metric used in the heat-Hankel compression theorem.
7. For full positivity, check the 1941 denominator in B5, the six interval
   separations, K<164, and the seed ratio at m=5. The first denominator for
   the second interval is 4*22^2+5=1941, not 1937.
8. Independently examine the directed eta/Gamma interval implementation and
   the analytic remainder. These six signs do not certify V100.
9. Check B11 over REAL polynomial coordinates, with conjugate data and
   multiplicities, and the relative rather than absolute tail comparison.
10. Verify that no positive-tail comparison or small-residual estimate is
    used to assert a sign of the full form in unbounded width.

The remaining full arithmetic sign is not routine, is not proved here,
and is not weakened merely by its expression in these packet coordinates.
