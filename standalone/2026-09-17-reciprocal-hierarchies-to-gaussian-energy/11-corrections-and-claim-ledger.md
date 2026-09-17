# 11. Claim ledger, corrections, and non-implications

**This ledger is part of the mathematics, not merely a disclaimer.** It fixes what the packet does and does not assert. IDs are local to RHG26 and do not replace historical repository claim IDs.

## 1. Claim status and dependency map

| ID | Claim / object | Status | Dependency / review location |
|---|---|---|---|
| RHG-H1 | Counting asymptotics imply harmonic asymptotics by partial summation | CLASSICAL / reconstructed | Chapter 02 §1 |
| RHG-H2 | Golomb count and sieve-product leading asymptotics | CLASSICAL IMPORT | Erdős [E61]; Chapter 02 §2 |
| RHG-H3 | Constant D_G and real-axis P_G,Z_G relations | DERIVED | E61 product plus summable corrections; Chs 02–03 |
| RHG-H4 | Every fixed level of the digit tower has iterated-log harmonic growth | DERIVED/PROPOSED | PNT block errors; Chapter 02 §4 |
| RHG-H5 | Nested residue-2 sieve inside G has next-log count | HEURISTIC/OPEN | Growing-modulus G-equidistribution and large-divisor tail missing |
| RHG-H6 | Direct multiple-residue rule's correct leading law | DISPUTED/UNRESOLVED | Printed extension versus heuristic; no complete refutation supplied |
| RHG-H7 | Divisor marking gives forward/backward identities | DERIVED | Finite divisor double-counting and partial summation |
| RHG-Z1 | Integer-generator product has multiplicative-partition coefficients and essential singularities at 1/k | DERIVED from standard identity | Chapter 03 §2; no full imaginary-axis claim |
| RHG-Z2 | Golomb-generated integers have harmonic mass C_G log_2x | DERIVED | Positive-coefficient Tauberian input; Chapter 03 §3 |
| RHG-Z3 | Regularized prime-zeta derivative criterion is RH-equivalent | CLASSICAL CONSEQUENCE | Holomorphic prime-power tail; Chapter 03 §4 |
| RHG-Z4 | Prime-subset Dirichlet series have zeros in Re s>1 | PROPOSED reconstruction of classical mechanism | Kronecker/Rouché; no critical-strip assumption |
| RHG-Z5 | Digit tower has a natural boundary at Re s=1 | PROPOSED PROOF | Fixed-modulus PNT, dense resonances; Chapter 03 §7 |
| RHG-Z6 | Infinite Golomb continuation to the critical strip | OPEN | Finite character-stage continuations not uniform |
| RHG-Z7 | Complementary centered digit filters give RH criterion | PROPOSED/CLASSICAL CONSEQUENCE | Both masks required; Chapter 03 §8 |
| RHG-R1 | d_alpha convolution and prime-power tangent | CLASSICAL / finite derivation | Chapter 04 §1 |
| RHG-R2 | Tangent of reciprocal-Gamma coefficients gives Li factorials | PROPOSED reconstruction | Locally uniform finite Selberg–Delange expansion required |
| RHG-R3 | Local zero branch produces -m Li(x^rho) at first order | LOCAL CALCULATION | No unrestricted contour deformation or zero sum claimed |
| RHG-R4 | Continuous counting law gives L_0 and R; power-free density coefficients | DERIVED | Absolutely convergent expansions; Chapter 04 §§4–5 |
| RHG-R5 | F and C_N decay criteria | CLASSICAL FAMILY / reconstructed specialization | Riesz/Báez-Duarte; Chapter 04 §§6–7 |
| RHG-E1 | Exact Gram, Mellin, derivative and restoration formulas for Q_j | PROPOSED COMPONENT PROOFS | Chapter 05; finite identities checked in code |
| RHG-E2 | Q_j has exact exponent 2Theta-1 for subpower depths | PROPOSED PROOF | Every-prefix leakage argument + interior Littlewood input; Chapter 06 |
| RHG-E3 | Critical multiplicity m forces log^(2m-1) Q_0 growth | PROPOSED PROOF | Adjoint vanishing moments; Chapter 06 §7 |
| RHG-E4 | Same-cutoff transfer from reciprocal-Möbius energy | PROPOSED FINITE INEQUALITY | Full multiplier constants; Chapter 07 §2 |
| RHG-E5 | Unconditional subexponential saving for Q_(log^4N) | CLASSICAL CONSEQUENCE | Lee–Leong-type M bound; no new exponent saving |
| RHG-P1 | Moment-packet norm bounds and exact extraction | PROPOSED / FINITE-EXACT checks | Chapter 08; supplied code |
| RHG-P2 | Listed Möbius Prouhet packets and N=512 budgets | FINITE-EXACT | Replayed supplied checker, exact fractions |
| RHG-P3 | Uniform packet remainder/interactions needed for completion | OPEN | Finite examples do not cover the all-scale source |
| RHG-G1 | Pólya–Gamma mixture representation of sech kernels | CLASSICAL law + DERIVED source application | Chapter 09 §§2–3 |
| RHG-G2 | Fixed logarithmic Gaussian sparse criterion | PROPOSED COMPLETE COMPONENT ARGUMENT | Chapter 09 §4; noncausal tail paid |
| RHG-G3 | Additive Gaussian / localized sech comparison from entrywise asymptotics | NOT ESTABLISHED / superseded | Replaced by exact log-Gaussian mixture |
| RHG-G4 | Correct additive Gaussian Fourier identity | EXACT | H^2 prefactor; Chapter 09 §1 |
| RHG-CLOSE | Native subpower covariance / fixed Gaussian upper bound on cofinal cutoffs | OPEN | No chapter supplies this bound; no RH completion |

## 2. Corrections that must travel with the packet

### C01. A family density is not its analytic continuation

G and the prime-digit family have comparable third-log reciprocal growth, yet the digit construction creates its own dense boundary resonances. Real-axis behavior at 1 cannot justify a common critical strip.

### C02. More forbidden residues do not automatically mean one more logarithm

The direct r-residue mean-field equation predicts a coefficient change. The handoff's critique of a printed Erdős extension is preserved, but not promoted to an accepted refutation. The nested construction is genuinely different and has its own unproved distribution requirements.

### C03. Seed 3 kills the nested residue-2 construction

All later G-primes lie in residue 2 mod 3. Starting at 5 removes only that immediate obstruction; it does not prove infinitude or the predicted density.

### C04. Prime-zeta zeros are not zeta zeros

The latter become singularities of P. P's own zeros already occur in its absolute-convergence half-plane and obstruct a globally holomorphic next logarithm. Coincident scaled singularities must have their coefficients combined.

### C05. Do not infer an imaginary-axis theorem for Z_int from an accumulation at 0 alone

The essential singularities at 1/k and their obstruction at 0 are proved by the displayed series. A statement at every other imaginary-axis point requires more work.

### C06. Smooth Li coefficients are not zero locations

The tangent calculation explains the factorial coefficients. Oscillatory x^rho terms remain beyond every fixed inverse-log order. Correct smooth coefficients are compatible with unknown real parts of zeros.

### C07. Fractional inverse factors have large deterministic main terms

Taking d_(-1/2) factors separately loses their cancellation at 1. A theorem about a product does not follow from small norms of factors which in fact are not small. Raw fractional differences also need correct centering.

### C08. Native source, exponent, and norm must all match

The harmonic product-box energy, causal prefix energy, reciprocal-Möbius energy, polynomial trace, Q_j and G_omega are not interchangeable by name or by matching exponents. Each transfer needs its complete terms and domain.

### C09. Localization and restoration can exactly balance

The absolute off-diagonal bound saves j^(-1/2), while restoration costs j^(1/2). The derivative identity identifies the added positive terms; they cannot be dropped from an upper bound.

### C10. Covariance is not always nonpositive

For the literal prefix (1,-1,-1), Q_8(3)-D(3)>0 by an exact rational calculation. This refutes a uniform sign shortcut, not a subpower growth claim.

### C11. Crossings cancel endpoint values, not accumulated energy

The finite adapter contains both Nm(N)^2/2 and the integral of m(x)^2. A crossing bounds only the former. The decaying oscillatory model in Chapter 07 demonstrates the logical distinction; it is not an arithmetic counterexample.

### C12. Sparse sufficiency does not construct good cutoffs

Every-prefix zero witnesses make any unbounded small-energy subsequence sufficient. They provide lower bounds under a hypothetical off-critical zero, not an unconditional upper subsequence.

### C13. Critical-line multiplicity is a different target

An O(log N) Q_0 estimate would also exclude multiple critical zeros. Subpower is the intended weaker target; simplicity is not assumed.

### C14. Local packets do not estimate the remainder

Prouhet moments and tiny finite isolated energies are exact, but the all-prefix extraction leaves expensive residuals. Coprime dilation retains a 1/zeta factor and need not annihilate its off-critical poles. Adjacent groups are not automatically orthogonal.

### C15. Additive Fourier normalization carries H^2

The correct identity is integral |S|^2=2pi H^2 integral exp(-4pi^2H^2xi^2)|A|^2. The target narrow-band mass is X^(1+o(1))/H, not X^(1+o(1)). The earlier response alternated between these and cannot be cited as a proof.

### C16. Entrywise kernel comparison is not signed quadratic-form ordering

Use exact Gram identities or nonnegative spectral multiplier ordering. The replacement in Chapter 09 is logarithmic Gaussian, not an unproved additive change of variables.

### C17. Long-window mean square is itself RH-strength

At H=X/log^2X, integration of the box sum recovers the long Mertens increment. Calling the target merely an average does not make it an already-available weak discorrelation statement.

### C18. Fixed-log savings cannot be silently iterated into power savings

Constants may depend on A; choosing A growing with X is not justified. Reapplying a theorem for mu to local averages of mu requires an invariant-family/operator estimate, not just the original one-vector bound.

### C19. Precise source versions matter

The short-interval paper was first submitted in November 2024; v2 is January 2026. Its displayed theorem has an upper X^(1-epsilon) restriction, while abstract/discussion consequences include longer ranges. Neither a simplistic direct-range assertion nor a blanket exclusion is accurate. No version supplies the random-variance bound by mere substitution.

### C20. Generic Type-II diagonal counting cannot prove the needed bound

Positive coefficients are coherent on |theta|<=c/X, producing narrow-band mass >>X. The target at H=X/log^2X is only log^2X X^(o(1)). Native Möbius signs and cross-piece cancellation cannot be discarded.

### C21. Kernel probability is not arithmetic randomness

Pólya–Gamma mixing is an exact identity for the detector. It does not replace mu by independent signs, confer martingale properties on the source, or prove a Gaussian-energy upper estimate.

## 3. Additional caution from packaging

- The historical Golomb constants, prime-zeta boundary decimal and 10^7 sequence counts lack supplied tail certificates or generation receipts. They are archived as historical approximations, not certified numerical claims.
- Only the supplied packet-checker artifact was available as a full executable from the earlier experiments. Other claimed prior executions are not treated as fresh publication-session tests.
- The public source arXiv:2608.07198 attributed in chat to a fractional Heath–Brown preprint could not be reopened during packaging. It is listed as an unresolved historical reference and is not imported into any proof.
- Primary references establish classical mechanisms; no priority claim is made for the packet's recombinations without an independent literature review.
- A successful Python run validates only its finite assertions. No Lean proof, whole-repository scientific validation, independent referee acceptance or native infinite-tail computation is claimed.
