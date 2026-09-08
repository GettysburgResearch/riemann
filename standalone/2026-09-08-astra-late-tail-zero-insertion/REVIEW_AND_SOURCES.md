# Review targets and source boundaries

This is an author submission, not independent review. The attempted RH closure
fails; review is requested for the positive-source perturbation theorem and its
consequences. Do not treat this packet as evidence for an actual off-line zero.

## Main proof obligations

1. LT1: the global lower envelope for the literal source, including all log
   knots and the two strict norm margins. The periodic-Bernoulli remainder is
   supplied; Stirling's limiting constant is a classical input.
2. LT2: cancellation of the two apparent boundary poles, reality of U and V,
   exact safe jets, exact support, and the uniform relative tail bound. The
   inserted zeros must lie off the original discrete divisor. No simplicity
   assumption is needed. Check the distinction between an ordinary output and
   an exact compact-input realization (the latter is not claimed).
3. LT3: Hardy division by the ENTIRE original Blaschke factor, not just a
   finite zero panel. The modified source is in the old domain; its own
   cyclic domain is strictly smaller. The resulting projection-norm jump is
   exactly one, not merely a lower estimate for a trial vector.
4. LT4: exclusion of a singular inner factor, the strictly positive additional
   zero mass, and the integrable logarithmic majorant. Strong convergence of
   projections is not uniform convergence and must not be interchanged.
5. LT5: finite Gram and inverse perturbations with the original metric and
   EXACT unchanged target cross vector. Only finite collections of strict
   inequalities are preserved, not all ranks simultaneously.

## Exact predecessor

Repository GettysburgResearch/riemann, PR819, commit
`c4fb013692c51d6b26b8a3c33200615af764da82`.
Path `standalone/2026-09-08-astra-intrinsic-entropy/PROOF.md`.
Git blob `afb721d6eddae8eb4fe861091f9747394bd7c708`, 14992 bytes.
SHA256 `84f57cc91a8fb13d0e6892928c9968752f07e70da152d7608abc5af2a4c7d6c9`.

Its source formula, Hardy normalization and entropy/Blaschke identity were read.
The new construction rederives its source envelope and retains all possible
original interior zeros. No parent code, actual-source numerical certificate,
HC26 Sobolev argument or predecessor test suite is imported as newly executed.

## Classical sources consulted

- NIST Digital Library of Mathematical Functions, section25.10(i), especially
  the infinite real sign changes of Z(t) and consequent existence of critical-
  line zeros: https://dlmf.nist.gov/25.10 . Consulted 2026-09-08. Only qualitative
  existence is used, not the page's numerical verification-height discussion.
- DLMF section5.11: Stirling normalization and remainder framework,
  https://dlmf.nist.gov/5.11 . The all-real periodic-Bernoulli bound used in LT1
  is written in the proof, rather than inferred from a formal asymptotic series.
- H.M. Bui, S.J. Lester, M.B. Milinovich, *On Balazard, Saias, and Yor's
  equivalence to the Riemann Hypothesis*, arXiv:1306.0856 (2013),
  https://arxiv.org/abs/1306.0856 . Its abstract was consulted to check attribution
  and the distinction between a logarithmic criterion and a proved vanishing.
  No conditional truncated-integral estimate from that paper is used here.

Classical Laplace convolution, Hardy inner/outer factorization, uniqueness of
analytic continuation, dominated convergence, and Hilbert-space orthogonal
projection facts are used in their standard forms. The source-specific bounds
and finite formulas are proved in PROOF.md. No external priority claim is made.

## Interpretation and nonclaims

The changed source need not satisfy zeta's functional equation or ordinary
Euler product. It agrees with the actual factorial source only up to the
prescribed horizon, plus the specified finite Laplace jet and arbitrarily
small global relative error. Such agreement is NOT full primitive-source
binding. The theorem therefore diagnoses a source-blind stability shortcut,
not the failure of the still-open exact arithmetic estimate J(A)=0.
