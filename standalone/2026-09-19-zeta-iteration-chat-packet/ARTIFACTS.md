# Retained artifacts and reconstruction

Every supplied source file is retained byte-for-byte as a readable file under
[artifacts/retained](artifacts/retained). There are 30 files in five stages,
covering all four supplied ZIP archives and the initial two standalone files.
Original ZIP container hashes and per-member hashes are recorded in
[the source manifest](artifacts/SOURCE_MANIFEST.json). The ZIP containers
are not duplicated in Git: their complete member contents are preserved.
A separate compressed conversation download contains the same member bytes.

| Stage | Files | Contents and original status |
|---|---:|---|
| 01_arithmetic_certificate | 2 | Original N=20 digamma/interval producer and its saved result, including the exploratory-table option. |
| 02_arithmetic_followup | 13 | Full note, README, paired Vasyunin evaluator, refinement/replay scripts, small checks, exact rational coefficient arrays and interval results at N=256/512/1024, N=2048 floating reconnaissance, environment record and original hash manifest. |
| 03_mollifier_bridge | 3 | Full spectral/mollifier note, finite floating identity checker, and result. Its checks are not directed arithmetic or asymptotic evidence. |
| 04_rigidity_gcd | 4 | Full rigidity/GCD/separation proof, exact rational finite checker, saved result, and original hash list. |
| 05_support_leakage | 8 | The seven original PR #901 files plus its historical PUBLICATION.json receipt. All seven are also unchanged at the sibling repository path. |

The separately supplied copies of the follow-up note, N=1024 result, mollifier
note, rigidity note, and support proof exactly match their corresponding ZIP
members. Those duplicate comparisons are recorded in the manifest. No missing
artifact is invented, and no earlier claim of an execution is treated as fresh
execution merely because the corresponding JSON exists.

## Verification

From this packet directory:

```sh
python verify_packet.py
```

This authenticates every retained source against the manifest, checks local
Markdown navigation and the eight-question coverage headings, and checks
that fresh replay records distinguish their arithmetic classes and scope.
It is an integrity/coverage check, NOT a proof of the research statements.

Replay source programs in a disposable copy: some original checkers write their
result JSON beside themselves. Do not silently modify archived source records.
For example, after copying artifacts/retained to a scratch directory:

```sh
cd 05_support_leakage
python verify.py --check results.json --self-test
python -O verify.py --check results.json --self-test
```

The initial N20 script needs mpmath. The follow-up numerical code additionally
imports numpy, scipy, numba and threadpoolctl even for its saved-witness entry
point. Its ordinary floating constructor is distinct from the interval witness
calculation. The original historical environment record is retained; this
compilation is not a clean-install or cross-platform certification.

## Evidence boundaries

Normal-mode exact checks and directed interval evaluations were replayed as
listed in VALIDATION. Original N512/N1024 certificates and N2048 reconnaissance
are preserved but not rerun in this compilation. Python -O removes assertions
in several earlier scripts; only the latest packet's separately designed
normal/optimized checker is credited with that two-mode verification here.
Historical normal/optimized receipts for other packets are not extrapolated.

The source bundle contains original notes that call component deductions
unconditional. The current claim ledger qualifies them as proposed proofs
under their stated unconditional hypotheses, not independently accepted claims.
Retaining their exact bytes is historical preservation, not a silent promotion.
