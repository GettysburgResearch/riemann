# Validation scope and reproducible commands

**Finite arithmetic/implementation checks, not an RH proof or independent
mathematical acceptance of KSC-1--5.** All code is standard-library Python;
acceptance uses explicit exceptions and remains active under -O and -OO.

## New finite protocol

From a checkout, with P=standalone/2026-09-09-astra-kernel-spectral-continuation:

```bash
python -B "$P/check.py" --check "$P/results.json" --self-test
python -O -B "$P/check.py" --check "$P/results.json" --self-test
python -OO -B "$P/check.py" --check "$P/results.json" --self-test
```

All three modes passed. The complete expected payload is regenerated and
compared, not just authenticated by a resealable hash. Twelve distinct mutated,
resealed records are rejected in every self-test. Tests change actual data,
coverage, source identity and scope claims; a no-op mutation is rejected as a
broken test. Duplicate JSON keys, floating values and nonfinite JSON constants
are not accepted.

| Exact check | Coverage and interpretation |
|---|---|
| Piecewise density/atom integrals versus divided differences | 672 off-diagonal rational pairs for individual divisor-kernel pieces; 20 summed-divisor cases. |
| Confluent diagonal | 112 exact constant/log-coefficient pairs, with logs symbolic rather than rounded. |
| Multiple-root contour algebra | 120 rational polynomial models including empty/nonempty selected root sets, multiplicities up to 3, and both presence/absence of the zero-pole background. These are SYNTHETIC F, not zeta values. |
| Root jets | 26 same-root entries and 22 distinct-root entries, plus exact antidiagonal determinants. |
| Conjugate-root real form | Nine rational complex synthetic pairs, including both sides of 1/2. Zero actual zeta locations are supplied. |
| Balanced cutoffs | 32 exact harmonic balances, 168 power moments, 24 log-background moments. Includes weighted-functional controls at s=-1/2, without calling them unweighted finite measures. |
| Kernel remainder | 64 midpoint differences and 120 rational-interval R(z) samples. Complete log and harmonic remainders are retained. |
| Native arithmetic | 1,089 Mobius values reconstructed by divisor inversion and checked by trial factorization; all cross terms of the terminal-balanced quadratic at 16 cutoffs Y=3,5,...,33. |

New semantic report digest:

`4b0a4b5e0ce35b4dbfd362a82eb12300599c5b4f1a51d5612e57351d848c2fc9`.

The analytic domain, continuation, contour identities and all-parameter
inequalities are justified in the manuscript, not proved by this finite code.
The transcript hashes summarize regenerated exact rows; no off-line zeta-zero
existence is inferred from a synthetic example.

## Previous source replay and storage contract

`prior/PROOF.md` and `prior/check.py` are exact copies from the preceding
user-supplied `riemann_astra_critical_source_attack.zip`, not newly repaired
versions. Their byte/Git hashes and the old canonical report's hashes are in
SOURCES.json. During this continuation:

```bash
python -B "$P/prior/check.py" --write /tmp/prior-results.json --self-test
```

passed, and the generated report matched the original 99,962-byte canonical
report BYTE-FOR-BYTE. It reproduced 4,225 primitive comparisons, 32 cutoffs,
488 finite source/energy predicates and 1,024 Euler-bridge checks, with eight
resealed rejections. The report's semantic digest remains

`e2843d1605d1e650705fd5c4103a364fe1739ae56600df6f991cc70924a55a3b`.

The large original report is not copied into this new directory; regenerating
it is intentional and writes only the explicitly supplied --write destination.
The earlier README and execution receipts are preserved in the original ZIP,
not represented as a newly published five-file packet. No historical receipt
is changed to claim a GitHub write that did not previously occur.

## Independence and limits

The new checker uses independently expressed sides of the finite identities:
piecewise integration versus divided differences; local Laurent coefficients
versus a polynomial two-variable kernel; divisor inversion versus trial
factorization. It imports no prior generator, verifier or repository module.
Both new and old implementations have the same author. Computational agreement
is not an independent mathematical review of that author's proofs.

An unsealed discovery-only floating eigenvalue scout was used to test whether
the continuum kernel might have a single sign. It was NOT an RH test and is
not a proof input or a certified spectral result. No values from that scout
are used in the manuscript, exact report or acceptance predicates. Earlier
floating exploratory Mobius/SHARP sums likewise supplied no theorem or bound.

Direct `git ls-remote` failed with `Could not resolve host: github.com`.
Consequently no full checkout or repository-wide validator was available.
Publishing via the connector and reading back Git objects, when recorded in
the PR receipt, is not execution of a full-repository validator. No Lean,
remote CI, actual zero-table calculation, or external formal proof was run.

## Independent review priorities

1. The endpoint atom and cancellation of the entire pole polynomial in KSC-2.
2. Holomorphic functional domains, especially s=0 versus literal harmonic balance.
3. Multiple-root jets and the nested-contour proof retaining the zero pole.
4. Compact cutoff convergence versus the divergent coefficient mass at the boundary.
5. The explicit separation of finite spectral models from the actual integer
   Mobius source and from an unproved infinite explicit formula.

Do not promote the OPEN native energy estimate through any of these identities.

## Final isolated replay

The eight-file packet was copied into a fresh isolated directory. The complete
new check and all twelve resealed rejections passed there in normal, -O and
-OO modes, with the same canonical digest. All files remained byte-identical
after execution. This was a packet replay, not a full repository checkout.
