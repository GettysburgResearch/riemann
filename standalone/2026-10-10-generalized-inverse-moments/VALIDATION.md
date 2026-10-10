# Validation of the generalized-moment packet

**Scope:** exact finite arithmetic and algebra checks, plus scoped reconstruction of the written proofs. A passing result does not establish the unproved short-row analytic moment estimate.

## 1. What was actually run

The author ran `checks/verify_algebra.py` in ordinary Python and in optimized Python (`python -O`). Both processes exited with code 0 and reported **32,473 passing predicates**. Their JSON outputs agree byte for byte. An independent AI agent reviewed the implementation and replayed the optimized command; its JSON also agrees byte for byte with `results/algebra.json`.

The checker uses exact integer arithmetic in the basis `1, zeta_6`, with `zeta_6^2 = zeta_6 - 1`. It raises explicit exceptions on failure; optimization does not disable its checks. It uses the Python standard library and has no network dependency.

| Object | SHA-256 |
|---|---|
| `checks/verify_algebra.py` | `362694b6c2257392c49e333b804d8767e56a3d34e172b5b0fc746efd96c337e8` |
| `results/algebra.json`, all three runs | `0dfd3fdd97a991bbb7acd4719a55618d08de5712ec729a9f489bcda76041fd47` |
| Independent implementation review | `b077bed9b0fd4a1b30d2c20091ae8f188637fe27fdce11234dbfab74b5951171` |

Read the [complete checker review](reviews/checker_review.md) for the independent derivation of the residue embeddings, exact arithmetic, conjugation, collision handling, and truncation coverage.

## 2. Coverage

| Predicate family | Count | What it authenticates |
|---|---:|---|
| Native character embeddings and states | 5 | Actual sextic symbols at two split Eisenstein prime ideals |
| Incidence polynomial identities | 80 | Independent direct multiplication and repeated-prime allocation |
| Native row identities | 7,280 | Every one of the 91 integer residue classes in every panel |
| Complete residue moments | 80 | Finite orthogonality with every algebraic sixth-power collision |
| Adversarial zero-mask checks | 2 | Rejection of replacing a positive sixth power by the constant one at a nonunit |
| Multinomial local inverses | 5,004 | The local inverse of `1 - sum(z_i)` |
| Euler corrections | 5,004 | The exact coefficient correction to the product of inverse Euler factors |
| Inverse corrections | 5,004 | The explicit inverse-correction coefficients |
| Two-way corrections | 5,004 | Composition of the two coefficient operators |
| Nonnegative inverse coefficients | 5,004 | Positivity of the finite inclusion-exclusion formula |
| Leading logarithmic cost | 6 | The degree-two coefficient `binom(r, 2)` in both absolute majorants |
| **Total** | **32,473** | **Finite arithmetic and algebra only** |

The prime ideals are `(7, omega - 4)` and `(13, omega - 9)`, with `omega^2 + omega + 1 = 0`. The residue classes `0,...,90` represent the complete product quotient. The 80 incidence panels cover moment orders `k = 1,...,8`, scales `D = 2,3,5,10,40`, and two local twist/weight configurations. The negative local signs are consistent with the fixed Hecke character obtained from the quadratic character modulo 5 composed with the norm. Only four squarefree column ideals are present in these fixtures.

The local series tests cover every nonnegative multiindex of total degree at most eight, for factor counts `r = 1,...,6`. This is 5,004 multiindices. Every term contributing to a tested convolution coefficient lies inside the same degree cutoff.

The finite weights are integer-scaled, compactly supported fixtures and are deliberately not smooth. The infinite proofs state the smooth-test hypotheses separately. Complete residue representatives are not the norm-ball row range of the open theorem.

## 3. Reproduction

From the repository root, run:

```sh
python standalone/2026-10-10-generalized-inverse-moments/checks/verify_algebra.py --output /tmp/riemann-generalized-moments-normal.json
python -O standalone/2026-10-10-generalized-inverse-moments/checks/verify_algebra.py --output /tmp/riemann-generalized-moments-optimized.json
cmp /tmp/riemann-generalized-moments-normal.json /tmp/riemann-generalized-moments-optimized.json
cmp /tmp/riemann-generalized-moments-normal.json standalone/2026-10-10-generalized-inverse-moments/results/algebra.json
```

Acceptance requires both checker processes and both comparisons to exit with code 0. The expected summary has `status = PASS`, `arithmetic = EXACT_INTEGER_IN_Z[zeta_6]`, and `total_predicates = 32473`. Merely reading those fields from the stored JSON is not a replay. Running the source reconstructs the actual character fixtures and the two independent sides of the algebraic identities.

## 4. What was not validated by computation

No numerical zero search, Lean or Comparator build, full repository test suite, or full independent reconstruction of either imported quasi-Riemann manuscript was performed in this pass. The checks do not establish uniform implied constants, prime-ideal asymptotics, the analytic theta reflection, Poisson cancellation over a short row range, the all-order moment bound, `17/24`, or RH.

The unconditional long-row moment and the all-order identities rest on their written proofs and stated standard inputs. The zero-growth characterization includes a separately reconstructed uniform reciprocal lemma. The proposed short-row mean square and the proposed large-value upper bound remain explicit missing analytic inputs. [REVIEW.md](REVIEW.md) binds the scope of the proof audits; [PROVENANCE.json](PROVENANCE.json) binds the delivered source and evidence bytes.
