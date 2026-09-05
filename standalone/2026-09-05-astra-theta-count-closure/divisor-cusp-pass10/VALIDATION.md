# Executed checks and limits

## New packet

- `python verify.py --check result.json` passed 102 finite fixtures.
- `python -O verify.py --check result.json` passed the same 102 fixtures.
- Complete normal/optimized JSON outputs are byte-identical.
- `python test_rejections.py` rejected six deliberate corruptions in each
  interpreter mode, twelve cases total, with the expected error diagnostic.
- SHA256SUMS covers exactly all other files in this directory. The manifest
  and coverage check is run with `--manifest`.

The fixtures separately assemble the divisor diagonal, every ordered cusp
edge, and the completed squares in formal log-prime coordinates. Rational
complex vectors and rational primitive polynomials are both used. Ground
state, graph connectivity, factorial-floor grouping, Rayleigh numerator,
integer-knot and coarse constant budgets are included. A fixture is one
finite identity/control, not a new theorem or an infinite-dimensional proof.
An initial combined shell command reached its 30-second orchestration limit
after the twelve refusal records had completed. The final clean normal and
optimized checks plus manifest verification were rerun separately and passed.
The complete group counts are in result.json. Test reruns inside refusal
checks are not counted as additional distinct mathematical fixtures.

`verify.py` reads no network or secret and uses only Python's standard library.
Every numeric acceptance calculation uses Fraction. Prime logarithms are
formal labels; square roots are eliminated with v_j=r_j/sqrt(j). No directed
special-function routine or floating-point result is needed by acceptance.

## Predecessor verification and reading

The current #790 head was read as 8cc6fc78db37f42290c7372bc994b3bfa94898ef.
All nine pass9 files from the supplied archive had Git blob hashes equal to
the remote subtree 3ff752aa5c12ad0350749d4567422b71ac828f4c. Its 65-check
suite was rerun in normal and optimized Python; both passed. The source,
not a merely matching filename, was checked.

The #792 separated-window proof was read at the exact commit/blob in
SOURCE_LOCK.json. Its finite six-window interval certificate and code suite
were NOT rerun and are NOT premises of DC-3. Its exact full-source identities
and normalization are imported; the coarse local/regular bounds are proved
again here. This is not a comprehensive independent review of that branch.

A preliminary ordinary floating-point exploratory scan of pass9's balanced
spectral densities used cutoffs from 2 to 10000 and a grid on [0,40]. It was
used only to examine a discarded cutoff-positivity idea. It is not a certificate,
not retained as proof evidence, and does not support any new conclusion.

## What is not claimed

No actual full W or xi matrix was numerically certified in this new packet;
no zero census, large prime campaign, PNT saving, Lean build, remote CI run,
independent referee acceptance, global source sign, or RH proof is claimed.
Finite tests do not machine-prove the all-N estimates or L2 integration.

The full-function theorem is on the subspace with zero damped mean in EACH
of the N windows. Positivity of the window means and their mixed terms remains
unproved. T is the Hardy/Weil source from #792, not the heat-Hankel Gamma from
#790. The geometric support classes shrink in total measure; no cofinal
capture is inferred from these local positive subspaces.

## Review reproduction

From this directory:

    python verify.py --check result.json --manifest
    python -O verify.py --check result.json --manifest
    python test_rejections.py
    sha256sum -c SHA256SUMS

The saved records and manifest are integrity controls, not substitutes for
reviewing PROOF.md. A publication receipt is external to the committed packet
so no tracked file asserts its own commit hash.
