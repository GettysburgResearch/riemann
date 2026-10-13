# Scoped AI review: periodic/abelian transfer and native heat defect

**Disposition: PASS for the stated mathematical and finite-diagnostic scope.** No blocking error was found in the three frozen manuscripts below. Their conditional arithmetic premises remain open; this receipt does not establish those premises or approve a new moment, zero-free boundary, or RH conclusion.

**Reviewer:** `/root/signed_sector`, an AI agent in the same research collaboration. This is an AI mathematical review and independent execution of the authors' finite checkers. It is not external human peer review, a Lean proof, or a formal proof-assistant verification.

**Frozen source commit:** `ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0`.

**Verified source tree:** `6622be6afbf5e293a07c71b2a9b556640557cc3f`.

All six source files were extracted with `git show` from that exact commit into the reviewer's scratch directory. The tree was checked with `git rev-parse`; extraction bytes were hashed independently and checked again before the finite reruns. No repository source file or Git ref was modified.

## 1. Scope, authorship, and exact reviewed bytes

The manuscript paths below are relative to `standalone/2026-10-13-principal-zeta-bridge/` at the frozen commit.

| Reviewed manuscript | Independently computed SHA-256 |
| --- | --- |
| `PERIODIC_DILATION_TRANSFER.md` | `ca8adadfc6d784a66682a691c38385915101894b7fb2ee3a6930c35c4f9f3cb9` |
| `ABELIAN_COMPANION_FILTERS.md` | `c4fc59f673f5f09a2e4e4b279c607db34f6803d0f6671fd84d0e416854d63fd3` |
| `NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md` | `9b351724607c7057a987e62835d9e4b4fe7a78f3b5e56b989a2af938b7689198` |

I did not author these three manuscripts or their finite checkers. I read preliminary versions, discussed their interfaces with the authors, warned against transferring the Eisenstein replica geometry to arbitrary fields, and requested that the heat note explicitly require unitary finite-ray values on its nonzero column support. Those scope clarifications are present in the frozen bytes. This is therefore a separately performed review with disclosed earlier feedback, not a blind review.

I authored `EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md`, its finite checker, and `SIGN_QUANTILE_CAPTURE_FOLLOWUP.md`. **Those objects are excluded from this receipt's independent-review coverage.** Their occurrence as companion interfaces does not turn this receipt into an independent review of my own work. The other packet manuscripts, navigation, and later integration claims are also outside the disposition above.

## 2. Periodic dilation transfer

I rederived the Abel identity in Section 1, including the lower boundary at `1-`. Causality makes the dilation sum finite, the prefix is exactly zero or one, and the change of variables gives the displayed kernel with no missing endpoint term. Local absolute continuity permits jumps in the derivative, while a jump in the function would need its full Stieltjes derivative; the manuscript distinguishes these cases.

The norm bound has constant `1/alpha` for every fixed `alpha>0`. It uses the scale derivative, not an absolute sum of the character coefficients. In particular no convergence of `sum |chi(m)|m^(-alpha)` below exponent one is assumed. The weighted row-norm application keeps one row space, one row height, and the same nonnegative row weights at every shorter column scale. The manuscript correctly requires the derivative-window estimate throughout `0<y<=D`; a bound only along `H=y^h`, only for the original window, or only on a grid does not supply that hypothesis.

I checked the Fourier normalization of the profile formula: the two character frequencies are `1/3` and `2/3`, the prefactor is `1/(i sqrt(3) x)`, and there is no zero frequency. Schwartz decay of the fixed Fourier transform gives the stated flatness at zero after any fixed number of derivatives. The profile can consequently touch zero in its support while extending smoothly by zero. The Mellin multiplier is the companion L-function and is deliberately allowed to vanish. It is not a nonvanishing detector for every Hecke row.

The one-sided estimate in Section 4 uses the special nonnegative prefix of `chi_-3`. Tonelli's change of variables gives the stated constant `L(sigma,chi_-3)/sigma`, positive and at most `1/sigma` for `sigma>0`. The finite-horizon bound follows by enlarging the nonnegative kernel integral. The subsequent finite Euler restoration is signed, so this one-sided inequality is not automatically preserved through it. That limitation is explicitly retained.

**Result:** the operator and profile identities and their conditional norm implications pass. No native derivative-window moment bound was established or assumed available by this review.

## 3. Fixed abelian companions

For finitely many mean-zero periodic sequences, each prefix is bounded and each causal Abel operator commutes with logarithmic differentiation and fixed dilation. Iteration gives exactly the product integral in (1.3). At a fixed physical scale the causal support restricts the logarithmic integration region to finite volume. Integrating the positive power weights yields `prod b_j / alpha^r` and loses no power of the scale, with the stated cost of `r` logarithmic derivatives.

I verified the local coefficient restoration algebra, including the distinction between prime ideals with equal norms. The trivial primitive character has conductor one, so its factor is the full ordinary zeta function. Multiplying the deleted ideal-Möbius Euler product by every specified companion and by one restoration factor for each bad prime ideal gives `1/zeta`. This coefficient argument is valid initially in absolute convergence and therefore coefficientwise at every finite physical scale. It does not require an inverse estimate for a companion L-function.

The classical factorization is an explicitly imported input. I independently opened the cited primary exposition and checked the locations: Sutherland's [MIT 18.785, Fall 2021, Lecture 19, Theorem 19.15](https://math.mit.edu/classes/18.785/2021fa/LectureNotes19.pdf) gives the product over primitive Dirichlet characters for the corresponding cyclotomic subfield; [Lecture 20, Theorem 20.1](https://math.mit.edu/classes/18.785/2021fa/LectureNotes20.pdf) supplies Kronecker–Weber for an arbitrary finite abelian extension. This review checks their use and citation, not a new proof of those classical theorems. The external PDF bytes were not content-hashed in this receipt.

The repeated profile transformation is valid: after one step, zero extension to the negative real axis is still compactly supported and smooth, with all derivatives zero at the origin. The same nonzero-frequency Poisson argument can be applied again. General complex periodic filters need not have nonnegative prefixes. Neither the special one-sided inequality nor a universal noncancellation assertion is imported into this case.

**Result:** the fixed-field coefficient and operator transfer passes. The constants and derivative count may depend on the fixed field. The manuscript supplies no uniformity for growing degree, discriminant, conductor, or bad-prime set, and constructs no ideal-parametrized sextic row family in other fields. Those exclusions are mathematically necessary and are retained.

## 4. Native heat defect and prime removal

I checked the exact physical-row normalization against the pinned PR #927 return formula in `SMALL_W_CORE_AUDIT.md`, equations (1.3)–(1.5). The factor is `1/L`, all nonzero element rows including all six units are present, the fixed ray coefficients need not be positive, and the subtracted diagonal is the physical product diagonal with its nonunit mask. Multiplying normalized Haar measure by the note's density `w_H` recovers those literal rows without a unit multiplicity error. The stated conductor exclusions guarantee `|nu(n)|=1` on nonzero support; this justifies both the diagonal and the cancellation of the common factor's character in (5.7).

For each active prime, direct expansion of `F=F_0+X_p F_1` gives the displayed positive local innovation and the signed physical defect. Self-adjointness of the coordinate expectation proves the weighted identity with the displayed sign and factor two. The coprime selector acts on original column indices and is not a positive projection. Every coefficient pair in the positive innovation shares the active prime, so its coprime part is zero. For a coprime pair, the product character instead has eigenvalue `log Nn + log Nm`. The entire coprime sector therefore occurs in the physical-density defect.

The Duhamel formula and the finite-time remainder follow from those eigenvalues. The unit pair is separately excluded, so no undamped constant is silently integrated. The heat intertwining is an equality for the coprime sector. Reexpressing coefficient damping as a changed native profile gives exactly the same normalization factor as smoothing the row density; it provides no independent saving. Uniform control of profiles at arbitrarily large heat time is not asserted.

I checked the Möbius prime-removal sign, the `Np^(-t)` factor, and the exact disjointness constraints in (5.3). A prime in a squarefree ordered native product occupies exactly one factor, giving the stated one-factor scale reduction while preserving the remaining exclusions and the coupled profile. The logarithmic allocation weights sum to one for every retained ordered pair. In the common-factor decomposition, the primitive unit pair is exactly the original diagonal and the mask `1_(g,x)=1` is retained. The active heat coordinates omit the primes of `g`; no row mask is averaged away.

The CRT Möbius gauge uses a residue with character value `-1` at every eligible sextic prime. It preserves complete-residue Haar measure and nonunit masks, but generally translates the physical density. Thus it diagnoses the limitation of the specified Haar/positive-innovation argument; it is not a lower bound or impossibility theorem for every source-specific method. The finite native four-prime witness and its counts check directly.

**Result:** the exact finite-prime identities, the source-qualified return interface, and the stated method-specific obstruction pass. Estimate (5.8) is explicitly open and is equivalent to the original centered covariance at that level of aggregation. This review supplies no bound for it. I read the imported #927 normalization and the #911 route-status boundary, but did not independently replay the original OpenAI arithmetic/Poisson primitives or the complete #911 proof packets.

## 5. Independent exact finite reruns

These are reruns of the **authors'** frozen checkers, not newly written independent mathematical oracles. I read their code and checked that the finite coverage statements match the quantities actually enumerated. Normal and optimized Python produced byte-identical report contents for each checker.

| Checker under `checks/` | Frozen checker SHA-256 | Exact replay coverage | Report SHA-256, identical in both modes |
| --- | --- | --- | --- |
| `check_periodic_transfer.py` | `3f5a8f9d939e754f75e7b705fadedb1a49ea93edf025f6398ea043f3d8697da3` | 1,916 Abel/sign cases from 4 rational piecewise-linear functions and 479 scales; 10,000 prefix checks | `fc18dc464ed9bfb866ac7d5603e205bf82d513e25151c939f74c879e54bcb9d6` |
| `check_abelian_companions.py` | `17bccc0d07e366ac76346d3439b75df03a97ad6bb5fd2078bc72c5387380d231` | 7,200 coefficient comparisons through 1,200 in `Q(zeta_12)`; 6 restoration masks; 4 duplicate-norm negative controls | `bd0f006f890fd84cbc8a6610a8942565904477a4b9863155c2378e94f60907fa` |
| `check_native_heat_defect.py` | `411337c393509979c6eb619b3736b3d9107c33b6c66099a68ce74a733f9d33d9` | Every `7^4=2,401` zero/sixth-root pattern with exact local multiplicities; report's declared coverage count is 28,812 | `39b06fdac71ea0f279f05fda48ec2dcb8527096de3dde167c3658d6ec9d585be` |

The heat computation uses exact integers and fractions in `Q(zeta_6)`. The periodic computation uses exact rational piecewise-linear integrals; the abelian computation uses exact integer Dirichlet coefficients. No floating-point tolerance or directed-rounding claim is involved.

Three intentional in-memory fault probes were also rejected under `python -O`: an incorrect periodic prefix, a zero replacement for a nonprincipal companion, and an explicitly false heat-checker gate. The frozen script bytes remained unchanged. This verifies the tested rejection paths survive optimization; it does not certify all conceivable failure paths.

The independent replay receipt has SHA-256 `acbc6faa188864a235b93c621235a961d18c0af7f0c35830741883fdb9591976`; the optimized guard receipt has SHA-256 `8c01cbe104b71797c6ff96fb7fa31711e845cae39578934e8390347e23e8d2b6`. The extraction metadata, complete reports, review-driver hash, dependency hashes, and scope declarations are retained in the accompanying `scoped_transfer_heat_review.json` and the reviewer's `frozen_review/` directory.

## 6. Decision and limits

No failed declared hypothesis or blocking defect was found in the reviewed derivations. This means the displayed implications are valid **under their stated premises**; it does not mean the missing native estimates hold. The common-height derivative-window bounds, the signed physical covariance estimate, and any subsequent arithmetic capture or moment estimate remain unproved by these three manuscripts and by this receipt.

The three artifacts are suitable for publication with those boundaries and their exact source lock. This disposition does not approve a full packet, an integrated theorem not listed here, GRH, RH, or an improved numerical zero-free constant.
