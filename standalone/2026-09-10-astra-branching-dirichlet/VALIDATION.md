# Validation and execution boundaries

## Mathematical status

New source representation, exact poles, entire approximation and global
compact convergence: complete proposed paper proofs in PROOF.md. Independent
review is required. The phase diagnostic is one directed finite analytic
certificate, not a zeta-zero computation. RH is not proved.

## Frozen remote publication verified

PR #853 is open/draft at e0b82da7ecdd4ed21e47e8b6adbb8c5182eac048.
A directory read returned all nine file Git identities and sizes. Each matches
the supplied predecessor ZIP, independently calculated locally. This verifies
what was pushed, not the correctness of the parent mathematics. Its uploader's
Windows skips and author's historical Linux receipts remain distinct.

## New finite scope

- Seven depths n=0,...,6, with moments j=0,...,12: gamma-factor and pair-moment
  identities are compared with an independent raw-X moment recurrence.
- Exact beta-weight normalization at four shape values and fifteen degrees.
- Forty-one central U^-2 moments independently checked by binomial integration;
  twenty-five beta central moments checked via independent raw moments.
- The actual prescribed n=1 phase at s=1/2+23i: all 241 terms through degree
  240, complete remaining series and its derivative, and directed gamma/log
  primitives. The reported bracket is (-1.427840092064,-1.427840092063).
- S(s) is separately enclosed away from zero before taking its logarithmic
  derivative. This is not a zero or winding-number certificate.

The phase uses the unchanged parent certificate.py, authenticated by SHA256
f20b3528dfa626acf9a9d5f5c70bf0d8c147322bd0215045a7a469f3280070b2.
Its 512-bit outward integer interval primitives and fixed analytic remainders
are reused. The parent's root-reconstruction function and full test suite are
NOT invoked. No binary floating-point or external gamma/zeta evaluator enters
new acceptance.

## Commands executed on the final packet

```
python -I -S -B check.py --write result.json
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
sha256sum -c SHA256SUMS
```

The two accepting runs reconstruct the same canonical digest:

    de372f54ee102670be03562195346c78b8d0a333b76743782699d53f46e7a211

Five unittest methods pass per interpreter mode, zero skips/failures/errors.
The subprocess test executes one pristine acceptance plus twelve refusals:
ten independently altered receipt fields and two parser cases (duplicate keys
and decimal JSON). Bool/int aliases are compared through typed canonical JSON,
not Python's equal-value comparison. The actual return codes control success.
These finite checks do not machine-prove the analytic statements.

## Non-proof exploration and interruptions

Scouting used ordinary NumPy/SciPy quadrature and mpmath series at depths one
and two, and a separate point-mass starting law. They suggested phase locations
and trial roots. No absence of found zeros is used as evidence of zero-safety;
no scouted root is reported as a certified zero.

At n=2, a 1500-degree raw-to-central moment conversion at 700 decimal digits
failed its necessary moment-range check at degree1397. It was rejected. A
900-digit rerun passed that diagnostic, but neither run is part of acceptance.
This is a concrete warning about catastrophic cancellation in a raw-moment
implementation. The final phase certificate instead uses exact rational
central moments for n=1. Its phase trial point was selected from a scout on
integer heights0,...,30, then rebuilt with complete directed bounds.

## Delivery checks and omissions

A clean extraction and add-only temporary-Git patch application are checked
separately in the external delivery receipt. No full Riemann checkout/build,
Lean/Comparator run, remote CI, native Windows run, independent analytic review,
all-depth zero property, or large-rank certified root census is claimed.

Current connector tool discovery returned read actions and no create/write
operation. GitHub plugin discovery found the already-installed connector.
A direct Git read failed host-name resolution. No remote write was attempted
through an unavailable action, and no new publication is claimed by this
session. The prepared patch is restricted to this new directory.
