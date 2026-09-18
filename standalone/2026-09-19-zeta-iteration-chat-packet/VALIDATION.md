# Validation performed for the comprehensive expansion

This is a documentation/source-preservation pass, not independent mathematical
review. Execution took place in the present Linux/Python environment; exact
versions and command receipts are in [replay.json](validation/replay.json).
All legacy execution occurred in a disposable copy, preserving the supplied
source bytes and historical result records.

| Fresh command | Arithmetic and result |
|---|---|
| Support `verify.py --check results.json --self-test` | PASS; exact integers/rationals; 8,940 counted comparisons and ten named controls. |
| Support `python -O verify.py --check results.json --self-test` | PASS; byte-identical stdout to normal mode. |
| Rigidity/GCD `check_identities.py` | PASS; exact rational identities and rational log interval for the mixed-metric refutation. |
| Mollifier `check_identities.py` | PASS; ordinary floating finite algebraic comparisons, not interval arithmetic. |
| Follow-up small `check_identities.py` | PASS; floating covariance/conditioning controls, not universal proof by enumeration. |
| Initial N20 `rh_arithmetic_certificate.py` | PASS; directed-interval recomputation of the fixed rational witness, D<0.00834. |
| Follow-up `verify_saved_certificate.py results/certificate_N256.json` | PASS; directed-interval recomputation and optimum enclosure, D<0.00413821. |

Support stdout SHA-256 in both modes:

    f5d0683a83d017a7200ee73e14b29b453b11785faa335dd0f99358eb8888acf9

Every command's stdout/stderr and digest are retained. Historical N512 and
N1024 interval certificates and the N2048 exploratory table were NOT recomputed
here. The source manifest preserves their original bytes and execution fields.
The numerical orbit and real fixed-point examples were separately recalculated
at 40 working decimal digits with mpmath; [dynamics_replay.json](validation/dynamics_replay.json)
labels them NON_DIRECTED_HIGH_PRECISION, not root certificates.

`verify_packet.py --self-test`, in normal and optimized Python, validates all
30 retained source members, the eight user-question headings, 46 claim entries,
38 correction entries, fresh replay output digests, and top-level local links.
It rejects an altered source, omitted question, modified execution output and
duplicate-key JSON. It checks integrity against the recorded manifests; it does
not authenticate a theorem merely because a JSON status says PASS.

No full-repository validator, clean installation, Lean build, remote CI,
external review, all-zero census, or unbounded arithmetic estimate was run or
proved. No earlier source record was rewritten to claim otherwise.

The original seven-file PR #901 packet is unchanged. Publication verification
must compare the actual remote subtree with this locally assembled snapshot;
the final exact commit and PR receipt belongs in the GitHub PR conversation,
not in a self-referential hash inside its own commit.
