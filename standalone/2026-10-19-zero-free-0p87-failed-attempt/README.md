# Recovery: failed 0.87 zero-free comparison

**No new zero-free region or RH proof.** This publishes the saved failed
attempt so its exact obstruction and rejected shortcuts remain available
for later research. Publication is not mathematical acceptance.

Read [REPORT.md](REPORT.md) for the argument and its assumptions,
[RESULTS.json](RESULTS.json) for the original exact output, and
[verify.py](verify.py) for the executable rational-arithmetic audit.

## What this record preserves

Within the explicitly stated sufficient-estimate model, the auxiliary zero
class a=25/36 prevents the proposed Re(s)>87/100 comparison from closing.
Even the more favorable diagnostic leaves an error exponent at least
6139/233550 > 1/40 throughout the enlarged parameter triangle. The report
also quantifies the missing count saving at b=1/8 and records why a raw
sieve substitution, scalar bias subtraction, cofactor orthogonality, and
a meromorphic identity did not supply the missing signed estimate.

This is a failure of the displayed estimates, not evidence for an actual
zero at 25/36, a lower bound on the arithmetic residual, or a general
impossibility theorem for the 0.87 target. The imported analytic formulas
retain the source and review limitations stated in the original report.

## Byte-preserved originals and historical status

The four original files REPORT.md, RESULTS.json, SHA256SUMS, and verify.py
are unchanged from the delivered archive. This README is the sole new file.
The original statements that no remote commit or PR was created, and the
checker's matching remote_publication string, describe the earlier attempt.
This recovery supersedes those publication-status statements only; it does
not rewrite their history or promote the mathematics.

- Archive: zero-free-0p87-attempt-20261019.zip (7,704 bytes).
- Archive SHA-256: a635c238428ca37024e4c8005da88f6c12283cec4afccecc0b15ec00ec048ca1.
- Original four-file Git tree: 155622858be39da1afedce3e809cc10d7c10402b.
- Parent: #1002 at 1319373815ee408146705b25a426fba6b22ed755.
- Publication branch: research/failed-0p87-comparison-20261019.

The original manifest authenticates the other three originals; it does not
include this separate publication notice. The enclosing draft PR records
the publication commit and final remote verification.

## Fresh recovery replay

The archive inventory and path safety were checked, and every original
manifest entry matched. Both commands were freshly executed successfully:

```sh
python -I -S -B verify.py
python -I -S -O -B verify.py
```

Each command's complete stdout matches the archived RESULTS.json byte for
byte, with SHA-256
70e3435ce181a2222d661d796bf17df9db11ca86b47077b458a22f8a641ea7af.
Neither run emitted stderr. The checker uses standard-library exact rational
arithmetic. It does not compute actual zeta values or zeros, validate an
infinite analytic estimate, or verify the reported external benchmark's
underlying theorem. No new independent referee review, upstream proof
reconstruction, Lean build, corruption campaign, full-repository validation,
or remote CI execution is claimed by this recovery.

The add-only publication leaves main, the parent branch, all inherited
proofs, and the integrated scientific status unchanged. No merge is made.
