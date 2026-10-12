# Validation and publication scope

Status: proposed research contribution. The four mathematical notes contain written proofs at their declared scope. The finite diagnostics below exercise exact finite instances and common false substitutions. They do not establish an infinite analytic estimate or certify the truth of the notes merely by hashing them.

Base: PR 926, commit `086bf0560c0c2679a1fe41418f583d2c5ca743c3`, tree `45b1de6138270a914b0311a604293bd16218898c`. This packet adds a new directory and preserves the earlier packet. It does not integrate any later research branch or update main.

## 1. Mathematical scope

| Note | Written result | Material boundary |
|---|---|---|
| [ARITHMETIC_PARITY_OBSTRUCTION.md](ARITHMETIC_PARITY_OBSTRUCTION.md) | All-distinct prime-face growth for `0<h<6/5`; sixth-row amplification of noninteger prime-count deformations and their derivative | Principal finite datum and the stated nonnegative fixed test; selected-face lower bounds do not lower-bound the full Möbius moment; no obstruction is asserted at the original parameter `z=1` |
| [PARITY_DAMPED_MOMENTS.md](PARITY_DAMPED_MOMENTS.md) | Literal Walsh identity, positive parity damping, full damped moment hierarchy, smaller-scale moving-mask adapters, all-integer norm-envelope obstruction | `PW_b` and `NM2_w` are explicit distinct inputs where used; `b=1` follows from elementary counting; `b=7/8` is conditional; the abstract norm model is not an arithmetic counterexample |
| [CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md](CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md) | Exact cube action and complete-residue Riesz law, sharp truncated linear comparison, infinite-product dichotomy, noise floor, qualified zero adapter | Complete residues do not fit a short row budget for free; linear-space optimality is not optimality on the native positive moment cone; the noise floor assumes `t>0`; the zero adapter remains conditional on its arithmetic bound and source coverage |
| [BESSEL_CHANNELS_AND_LEAKAGE.md](BESSEL_CHANNELS_AND_LEAKAGE.md) | Finite Bessel spectrum, mixed compression/leakage, simultaneous S3 orbit, one-third invariant energy, repeated-reflection formula, native covariance mismatch, Mellin involution | The finite transform has not been identified with a contracting physical covariance; Gauss phases, conductor dependence, literal masks, and the transformed sampling weight remain essential |

The generalized undamped moment with cofinal sublinear losses is not proved. No new zero-free line or conclusion about RH is claimed. The smallest open target is README equation (5.1): retain diagonal size, up to sublinear losses, on the complete native moment while lowering damping below the threshold supplied by the pointwise input.

## 2. Exact finite replays

All three checkers use the Python standard library. Integer, rational, or exact cyclotomic arithmetic is used in the acceptance predicates; no numerical tolerance or floating-point rounding is an acceptance rule. Each failed predicate raises explicitly. Syntax inspection found no Python `assert` nodes, so optimization does not remove any acceptance predicate.

The packet coordinator executed every command below from this directory in both ordinary Python and `python -O`. All six processes exited with code zero. For each checker, ordinary and optimized JSON are byte-identical.

```sh
python checks/verify_parity_damping.py \
  --note PARITY_DAMPED_MOMENTS.md \
  --json results/parity_damping.json
python -O checks/verify_parity_damping.py \
  --note PARITY_DAMPED_MOMENTS.md \
  --json results/parity_damping_optimized.json

python checks/verify_cubic_fibers.py \
  --note CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md \
  --output results/cubic_fibers.json
python -O checks/verify_cubic_fibers.py \
  --note CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md \
  --output results/cubic_fibers_optimized.json

python checks/verify_bessel_channels.py \
  --note BESSEL_CHANNELS_AND_LEAKAGE.md \
  --output results/bessel_channels.json
python -O checks/verify_bessel_channels.py \
  --note BESSEL_CHANNELS_AND_LEAKAGE.md \
  --output results/bessel_channels_optimized.json
```

| Diagnostic | Exact finite coverage | Explicit acceptance count per execution |
|---|---|---:|
| Parity damping | Actual primitive F7/F13 symbols on all 91 CRT rows, including 19 rows with a zero symbol; four exclusion masks; orders 1, 2, 3; Walsh and centered-cofactor identities; finite rational exponent envelopes; cumulants and complete-residue resampling obstruction | 44,091 |
| Cubic fibers | Eisenstein arithmetic and native symbols at the displayed norm-7, norm-13, norm-19 ideals; complete CRT including zero masks; finite positive Riesz laws; exact centered projections; doubled-order comparison; explicit adversarial examples | 38,577 |
| Bessel channels | Direct finite kernels at both primes above 7, both above 13, and the inert norm-25 prime; all matrix entries and zero residues; exceptional channels; 510 native words, 247 mixed complement pairs, walk powers 0 through 8; exact physical row examples | 11,562 |

The total is 94,230 explicit finite predicates per ordinary/optimized set. This count includes arithmetic-domain and setup guards; it is not a count of independent theorems or asymptotic cases. In particular 5,225 of the parity checker guards are ring-domain checks. The ordinary and optimized executions each repeat the same finite scope.

The arithmetic parity obstruction note is an analytic argument, with no finite computation offered as a substitute for its proof. Its lattice count, coprime mask average, Mellin singularity lemma, prime-face subtraction, and sixth-row Hölder step require mathematical review.

The checkers do not authenticate remote GitHub bytes on their own. Their JSON records bind the supplied local proof and checker bytes. Remote source verification and exact-commit review are separate steps.

## 3. Source and artifact identities

[sources/repository_sources.json](sources/repository_sources.json) records 38 immutable repository sources retrieved during this reassessment, with commit, path, Git blob, byte length, and SHA-256. It is a retrieval record, not a claim that every source has been independently proved. Each mathematical note identifies the specific assertions it uses and retains their premises.

The imported reflection formula is bound to the canonical repository copy of `paper2.tex`, Git blob `2000faddbbebac5de0ecfe0b962534ea61a852d5`, SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`, 169,005 bytes. No GRH-dependent dispersion theorem is used as an input to an RH conclusion.

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records the frozen proof notes, overview, checkers, result JSON, and repository-source manifest. It deliberately excludes itself and this publication/review metadata document. The parity note differs from its author's frozen draft only by replacing the temporary source-manifest filename with its published path; its diagnostics were rerun against those final bytes. The other three mathematical notes and all three checkers retain their author's frozen bytes.

## 4. Independent review protocol

At the mathematical source freeze, no exact-commit independent verdict has yet been recorded. Following CONTRIBUTING.md, the full intended mathematical source will be published first. Nonauthor reviewers will then fetch the named files at that immutable commit, verify their byte identities, and record a scoped proof review and any replay they actually perform.

Those receipts and the publication identity may be appended in a metadata-only follow-up commit. The proof notes, overview, checker code, result JSON, and source manifest remain frozen. A material mathematical repair instead requires a new mathematical source identity and renewed review of the affected scope.

Automated-agent review is not human peer review or a main-branch integration verdict. Each receipt applies only to its named files and source commit, and cannot enlarge the conditional, finite, or cofinal conclusions stated here.
