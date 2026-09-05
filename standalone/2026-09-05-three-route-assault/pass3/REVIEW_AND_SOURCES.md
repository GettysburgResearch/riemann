# Third-pass reading, source receipts, validation, and self-audit

Status: proposed research outside canonical integration. This is the author's proof/code self-audit, NOT independent referee acceptance. RH remains unproved.
Parent PR #793: `f22b67db113d1aa4f986fe35a2fc0321fdff7d47`.
Repository: GettysburgResearch/riemann, stable ID 1309150028.

## 1. What was actually read

A fresh connector survey covered the latest twelve PR descriptions, including the current heads below. Full proof reading was concentrated on the source-relevant documents, not advertised as a line-by-line audit of every branch.

- **#790 at 634d9a8ec4b0819442e601686a109ff7015b7b0b:** `standalone/2026-09-05-astra-theta-count-closure/joint-ray-pass4/PROOF.md`, blob `766b74627756283ddbfb3c4bec6f5707a31be4c3`. Read the Gamma-mixture uniformity argument, full prime-tail transfer, continuum subtraction, rational-ray detector, and the explicit remaining fixed-ray failure. This pass uses the distinction between the controlled t=O(log m) regime and the RH-sensitive t=m/u regime; no theorem outside that stated range is imported.
- **#792 at 875e8dd47186e924445533513a1ad405af09d7a7:** `standalone/2026-09-05-bernstein-chebyshev-growth/prime-energy-boundary/PROOF.md` and `BOUNDARY.md`. Read the moving-degree actual-prime diagonal proof, full signed Christoffel--Darboux identity, same-prime weight countermodel, meromorphic radial classification, and area-norm endpoint. The polynomial diagonal is genuinely paid, but its comparison with the signed energy is not. Our Route-2 proof uses alpha=0, a different source, and independent estimates, not a relabeling of those results.
- **#793/pass2:** read the complete source-defined Hardy kernel and capture proof, causal Mobius norm and anti-causal warning, and determinant compactness/finite-source records. The unchanged interval implementation is authenticated as described below. These are parent dependencies, not newly independently accepted theorems.
- **#785 at 9a965c26fd3e0310736829689db1734bcb5c3ec4 and #784 at d6d326b21d9526d9c91b18017bf550003f8f4f9b:** revisited their current all-rank/coefficient and Stieltjes/source-Weyl descriptions against the earlier proof reading. They already identify positivity endpoints; we do not claim to invent those endpoints.
- **#783 at 48d556561125cba3859a4c6d6747bcb44c1a7fc1:** the Poincare-frame/Hecke asymptotic description was considered as a construction model. Its different automorphic quotient is NOT imported as xi positivity or a native sampling-frame theorem.
- **#788 at a9c7b44f908c90f63d2f49a5fde58face5921e42:** the Hilbert/pair-correlation import was compared at its current summary and known proof boundary. No compact-support BGST theorem is applied in the new noncompact metric.
- **#786 at fc550cb0531e7abbc438a9b6eefa5ca11f90abc7:** its current assessment informs the demand for actual estimates rather than more named equivalent gates. Its broad criticisms and numerical limiting assertions are not imported as proved analytic facts.

AGENTS.md was reread at the exact parent head. No source PR, main, canonical registry, or formal library is modified. Local labels M1--M6, L1--L6, and G1--G8 are path-scoped, not new canonical claim IDs.

## 2. Classical literature boundary

The following primary/official sources were consulted online; no new external priority is claimed.

1. NIST DLMF, Chapter 18, particularly 18.12.13: https://dlmf.nist.gov/18.12#E13 . The Laguerre generating function, ordinary orthogonality, derivative relation, and Christoffel--Darboux mechanism are classical. Finite versions of all algebra used here are independently reconstructed in the checker.
2. Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, Journal of the London Mathematical Society (2023), DOI 10.1112/jlms.12785: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785 . Its online article situates the source/Hardy, moment, and Weil positivity endpoints. Local positivity and equivalent moment conditions are not themselves a proof of the global sign.
3. Belton, Guillot, Khare, Putinar, *Moment-sequence transforms*, author-repository abstract/record: https://eprints.lancs.ac.uk/id/eprint/144287/ . Used as a primary literature boundary for moment/Hankel positivity, not as an imported new xi theorem. No full-PDF review is claimed. Our compact moment implication and finite quadrature argument are proved in the packet.

Standard bounded spectral theorem, Stieltjes inversion, Euler--Maclaurin with periodic Bernoulli remainder, the invariant genus-zero product, and the classical coarse/leading zero-count laws are stated imports. R1 gives the needed bounded multiplication-operator argument; R3 proves the quantitative summation and normalization from the named count input. These imports are not machine-formalized by finite fixtures.

## 3. Primitive arithmetic certificate and dependency lock

The only executable parent import is `../pass2/source_certificate.py`:

    parent commit: f22b67db113d1aa4f986fe35a2fc0321fdff7d47
    Git blob:      144875db117fced3a506fb84331d2168d05b5f06
    SHA-256:       128df4f27cc62683a58ef74c1f374910db13b507208e00535df3e1c9a9b3c6e5

The new source implementation refuses a missing or changed parent before importing it. It reuses rational outward interval arithmetic, rational log tails, and Machin arctangent tails. It does not consume old PASS flags, old moment values, or an assumed RH spectrum.

The new zeta Taylor calculation uses N=256, twelve Bernoulli corrections, degree six, and a complex radius 1/4 for explicit Cauchy remainder bounds. The complete formula and proof are in R1_MOMENTS.md M5. All six lower principal-minor intervals must be strictly positive. A new result is compared to MOMENTS.json in canonical serialization.

REGRESSION.json is an independent mpmath 1.3.0, 70-digit differentiation cross-check on the safe s=2 source. It is NON_DIRECTED_HIGH_PRECISION and excluded from proof dependencies. regression.py makes the calculation reproducible; it is optional and not required for the exact standard-library suite.

## 4. Validation actually performed

The new exact suite reconstructs **622 distinct finite controls**, partitioned in RESULTS.json. The **six actual-source interval signs are INCLUDED**, not added again. It also reconstructs independent rational source-generating and zero-feature matrices on four synthetic conjugation/sign-invariant panels, exact geometric tails/traces, finite quadrature moments, ordinary Laguerre integrals and Christoffel--Darboux polynomials, and Cayley pole coordinates.

The normal and optimized runs of source_moments.py and verify.py pass and reproduce the same stored bytes. **Twelve unit/rejection tests** pass in each interpreter mode; these test executions are not counted as additional finite mathematical controls. They include numeric aliases, singularity/domain refusals, the tiny-prefactor correction, altered-result rejection, missing manifest coverage, and changed proof bytes.

Every SHA256SUMS entry is checked; the checker also requires exact manifest coverage, not just the hashes of whichever files happen to be listed. The optional high-precision regression was run and matched all six certified intervals. A read-back comparison of published blob hashes is a separate publication check and is not claimed until recorded in the PR receipt.

The inherited 447/640-control broad suites were NOT rerun in this pass. Only the parent interval implementation used by the new certificate was imported and freshly exercised. No Lean build, broad prime or zero enumeration, high-degree actual-zeta matrix sweep, directed contour integration, remote CI success, or independent referee acceptance is claimed.

## 5. Self-audit findings and binding distinctions

- The initial source run refused certification after an early-rounded tiny Euler--Maclaurin prefactor made the enclosure too wide. Exact rational prefactor multiplication before rounding fixed the enclosure. A dedicated unit test retains that failure mode. No parent file changed and no invalid result was accepted.
- The moment center is invariant coordinate 2, not the first/second pass's coordinate zero. Old minimal ranks cannot be compared with the new weighted quadrature as though they described the same problem.
- A positive three-node resolvent is not an ordinary rank-three determinant. Finite fractional residues are legitimate quadrature weights; integer multiplicities emerge only after the all-order meromorphic argument.
- All-order unshifted Hankel positivity is still RH-strength. The positive real axis is what removes negative support; unshifted positivity alone does not imply this for an arbitrary moment problem.
- A_N's rank-two displacement is not a positive right-hand side, a rank-two matrix, or a sign theorem. A synthetic nonreal pair produces a negative two-by-two determinant under the same recurrence.
- R3 deliberately fixes b=3/2 so its trace family matches R1's invariant center. All denominators, feature coefficients and test controls retain b^2=9/4. The basis-tail constants are conservative and depend on stated coarse count constants, not on an unreported numerical zero-count bound.
- A negative exact compression is already a negative direction of the full operator. The tail allowance is needed for lower certification and guaranteed finite capture, not to legitimize that implication.
- Under RH, the lost-trace asymptotic checks the convergence-rate scale; it is not an unconditional positivity argument.
- R2's altered sign source has exactly the same diagonal at every degree and an explicit interior pole. Its exponential energy is not evidence about the actual Mobius source, but it refutes sign-blind comparison.
- Reciprocal zeta has order-m poles at multiple zeros. Polynomial degree-energy bounds would uniformly limit m, unlike the logarithmic derivative in #792. Subexponential growth is the stated necessary-and-sufficient endpoint; no uniform multiplicity bound is assumed.
- Safe meromorphic continuation is not an identification of arbitrary boundary integrals with the causal source. The Taylor-germ construction is used before analytic continuation.

## 6. What would make the next pass mathematically substantive

A proof must control at least one of the three literal arithmetic objects: every source Hankel sign, the signed reciprocal-Laguerre energy, or the negative part of the predetermined Hardy matrix. Another finite-rank example, diagonal estimate, equivalent criterion, or improved basis truncation does not alone discharge that step. The published complete component proofs and countermodels are reusable, while all three conclusion-facing estimates remain explicitly open.
