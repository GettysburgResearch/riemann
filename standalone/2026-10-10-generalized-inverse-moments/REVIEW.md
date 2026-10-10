# Review scope and mathematical dependency boundary

**Status:** proposed standalone research. The audits below are scoped independent AI-agent reconstructions of specified file contents, not human mathematical acceptance, formal verification, or integration into the repository's accepted record. Agreement between agents is not a substitute for the written proofs.

The requested short-row fourth moment and generalized moment remain open. None of these reviews certifies a new zero-free boundary, a shrinking zero band, or RH.

## 1. Load-bearing files

| File | Native claim | Standard or conditional input |
|---|---|---|
| `LONG_ROW_AND_OBSTRUCTION.md` | `M_2k <= O(HD^(k+epsilon) + D^(3k+epsilon))`; positive-coefficient obstruction | Primitive Gauss sums, planar lattice Poisson, fixed-field ideal counting; prime-ideal theorem and squarefree density for the obstruction |
| `HYPERGRAPH_REDUCTION.md` | Exact all-order prime-incidence identity and logarithmic overlap cost | Elementary ideal arithmetic; the short-row rectangular estimate is explicitly assumed and remains open |
| `MASKS_AND_EULER_FACTORS.md` | Exact moving-mask inverse and two-way Euler correction with quantified norm costs | The unmasked estimate must hold at the same row set for all smaller rectangles and for the stated enlarged fixed bad-prime set |
| `MELLIN_AND_SPIKES.md` | Universal test, record-scale replicated spikes, cofinal criterion, moment-growth characterization | Standard Hecke continuation, functional equation, conductor control, prime-ideal theorem, and an explicitly reconstructed uniform reciprocal lemma |
| `BOOTSTRAP_LIMITS.md` | Sharp finite-moment interpolation and synthetic concentration examples | The arithmetic example is conditional on a uniform zero-free boundary and the imported second moment |
| `checks/verify_algebra.py` | Exact finite character, incidence, moment-orthogonality, and local-series predicates | Two actual split prime ideals and bounded finite fixtures; no infinite analytic assertion |

The upper moment-growth characterization uses a zero-free boundary as the rightmost-zero supremum of the same family. It does not insert the imported claimed quasi-Riemann boundary. The reciprocal lemma is reconstructed with explicit disk radii in `reviews/mellin_review.md`, starting from standard uniform Hecke strip growth. The principal regularization, deleted Euler factors, conductor dependence, and endpoint at supremum one are included.

## 2. Content hashes and reconstruction coverage

| Audited file | SHA-256 | Independent reconstruction |
|---|---|---|
| `HYPERGRAPH_REDUCTION.md` | `e22637f2378adf35768d62b1270eb63615cc1c3058faae976e3d28d2f0bf9dac` | Moment-obstruction agent and amplification agent |
| `LONG_ROW_AND_OBSTRUCTION.md` | `986fe6ce333566fdea0ef849001393e93923fa98561faffdb97aa3c8a63909ce` | Theta-closure agent |
| `MASKS_AND_EULER_FACTORS.md` | `5655f79355dd5c9a3bc357ed27304354a056b4415e12ed7907de7c969c932e60` | Amplification agent, including the final critical logarithmic cost |
| `MELLIN_AND_SPIKES.md` | `f3bdeb168714d838a4b13347cd353675d9644b9629041cdf7def78dc496162e3` | Moment-obstruction agent; secondary theta-closure audit |
| `BOOTSTRAP_LIMITS.md` | `34af6338d177dbc3295ca96c66109aa8b5f3e768cab181b7ef2a9ae0b60ecff2` | Review recorded in the companion bootstrap report |
| `checks/verify_algebra.py` | `362694b6c2257392c49e333b804d8767e56a3d34e172b5b0fc746efd96c337e8` | Theta-closure agent, including independent optimized replay |

The primary author also read every proof note and the independent reports. The content hashes identify the precise bytes audited before publication. The publication commit binds those bytes together; this is not an exact-commit integration review. Substantive future changes require a new review scope.

## 3. Preserved reports

- [Hypergraph and local-adapter review](reviews/hypergraph_review.md): independent reconstruction of the incidence proof, small-prime restoration, initial Euler operators, and the imported positive-gap mismatch. Its companion hash `c718a99f...` is an earlier version of the mask note; that review alone does not cover the later logarithmic refinement.
- [Incidence and final Euler-correction review](reviews/amplification_review.md): reconstruction of the final mask note at `5655f793...`, including the exact degree-two coefficient, prime-ideal Mertens normalization, and two-way logarithmic operator cost. It also records the initial finite-ladder obstruction derivation.
- [Universal-test and reciprocal-lemma review](reviews/mellin_review.md): reconstruction of the Mellin test and record argument, explicit-radius proof of the uniform reciprocal lemma, and the conditional higher-moment consequence of an assumed zero-free boundary.
- [Long-row and secondary Mellin review](reviews/long_row_review.md): independent reconstruction of the unconditional moment theorem and coefficient obstruction, plus a separate check of the zero-growth characterization.
- [Bootstrap review](reviews/bootstrap_review.md): independent audit of the standalone interpolation and synthetic-array note.
- [Checker review and replay](reviews/checker_review.md): native finite-field embeddings, exact arithmetic, independently assembled incidence expansion, complete-residue orthogonality, truncation semantics, and an optimized replay matching the authored JSON.

Some reports retain the names of their temporary working files. `analysis_theta_closure.md` at hash `5655f793...` is byte-identical to the delivered `MASKS_AND_EULER_FACTORS.md`; `analysis_amplification.md` at hash `f3bdeb16...` is byte-identical to `MELLIN_AND_SPIKES.md`. These are path mappings, not changes to the reviewed mathematics.

The overview received a separate scope check. The suggestion to describe the tail target without calling it stronger than full-moment control was incorporated, and its bootstrap discussion now links to the standalone proof. The overview is navigation; the fully quantified claims reside in the six files above.

## 4. Smallest unresolved statements

The sufficient generalized-moment input is the unmasked rectangular mean square in `HYPERGRAPH_REDUCTION.md`, equation (3.1), after the fixed small-prime convention of the mask note. It must be uniform for every nonvanishing smaller factor scale at the original common row length `H = D^(1+theta)`. The algebra and mask transfer do not prove it.

The large-value alternative is equation (4.2) in `MELLIN_AND_SPIKES.md`: an upper bound of `o(D^(h/6)/log D)` for the number of rows exceeding `C D^alpha`. The packet proves that this would suffice and that an off-line zero would require many large prime replicas. It does not prove the requisite upper bound.

The complete sextic diagonal has the claimed size, including the extra high-order configurations. The unresolved saving lies in the aggregate nonprincipal arithmetic contribution. Removing the necessary sixth-power rows, replacing the exact signed coefficients by arbitrary bounded weights, or expanding a known smaller row range would change or unjustifiably strengthen the theorem.

## 5. Imported sources and exclusions from review

The source family and analytic interfaces were read at the exact imported commits recorded in `PROVENANCE.json`. The October 5 and September 30 TeX blobs were checked against the then-current OpenAI/math head and found unchanged. This is a source-identity check, not acceptance of those manuscripts' full proofs.

No full upstream analytic audit, fresh Lean or Comparator build, numerical zero census, or integrated-record promotion was performed. The exact checker supports only its finite arithmetic and algebra scope, as recorded in `VALIDATION.md`. The new branch preserves the preceding import and research packets and is proposed for review through a draft PR.
