# Execution, assurance and omissions

This is author evidence for proposed research, not independent mathematical acceptance. The analytic theorems in PROOF.md and remainder bounds in NUMERICS.md are written proofs. Finite programs do not machine-prove the unbounded statements.

## Complete source computation

On Linux with Python 3.13.5, the defining-theta program was generated and then run in ordinary and optimized isolated modes. Both accepting commands recompute every selected raw moment, normalize, form cumulants and all four interval LDL pivots, and compare the entire typed receipt. The outputs agree byte-for-byte.

- Source interval: 96 cells covering [0,3], degree-96 Taylor products.
- Explicit theta indices: 1 through 8, with 247 computed and 521 analytically enclosed cell-terms.
- Raw moments: 0,2,...,14; seven trace moments; one complete 4x4 Hankel matrix.
- Complete analytic remainders: every omitted theta index, the entire remaining time tail, skipped cells, and every complex-Taylor remainder. Numerical rounding remains in the intervals independently of that analytic budget.
- Accepted arithmetic: integers and outward 512-bit dyadics; pi and exponentials reconstructed by finite rational series with proved tails. No numerical zero or zeta/gamma oracle.

Canonical `moments.json` SHA256:

```
cb5f226e1d10631e6aec69d0048404e15fd5c5da0d274f2219d12d33fad60550
```

The certificate is genuinely for the complete theta source, but genuinely finite in Hankel order. Nothing asserts that order four controls all later orders.

## Bounded controls and actual refusal calls

`test_checks.py --cli` completes normally and with `-O --optimized`, without skips. Both full JSON summaries are identical to `tests.json`:

```
50bba09469fd34c742f4bd3787284ccb435167ccb5b3894707ca87cd86d0e6a1
```

Its 2,311 bounded controls comprise 1,976 directed rational arithmetic cases; an independent pi bracket and nine independently enclosed exponential inputs; twelve exact optimal two-vector metric identities; 299 finite cluster annihilation/norm identities; three weighted Vandermonde determinant models; two signed/complex spectral controls; exact reconstruction of the Gaussian-mixture cumulants; three Jordan metric-equation coefficients; and five strict JSON/type refusals. Repeated finite cases are not counts of distinct theorems.

In addition, each mode performs one pristine **full source reconstruction** and ten actual changed-receipt CLI refusals. These include a changed numerical endpoint (rejected after full reconstruction), duplicate keys, Boolean/float count aliases, a false RH flag, omitted tail coverage, reduced theta coverage, missing pivots, an extra field and an empty object. Preflight checks intentionally reject structurally invalid inputs before doing the expensive arithmetic.

`verify_packet.py` separately checks the exact eleven-entry SHA256 manifest and twelve regular-file inventory. Its self-test invokes actual copied CLIs with one pristine control and six refusals: added file, missing file, altered proof, empty manifest, duplicated manifest path and symbolic-link substitution. Symlink behavior is tested on Linux, not claimed on Windows. Full mode authenticates before and after the numerical reconstruction.

These integrity tests protect a known frozen packet. An adversary able to replace the entire program and trusted source reference is not defeated merely by recomputing hashes. The exact published Git identity and independent review remain part of the trust boundary.

## Reproduce

From this packet directory, with outputs outside the sealed inventory:

```sh
python -I -S -B verify_packet.py --full
python -I -S -B -O verify_packet.py --full
python -I -S -B verify_packet.py --self-test
python -I -S -B -O verify_packet.py --self-test
python -I -S -B test_checks.py --cli --output /tmp/theta-tests-normal.json
python -I -S -B -O test_checks.py --cli --optimized --output /tmp/theta-tests-optimized.json
cmp tests.json /tmp/theta-tests-normal.json
cmp /tmp/theta-tests-normal.json /tmp/theta-tests-optimized.json
```

No assert statement implements acceptance. The scripts require no third-party dependency. The source algorithm and accepting receipt are new here; no parent author program was imported or run.

## Disclosed intermediate work

A small preliminary nondirected mpmath moment scout informed the finite target and precision. Its approximate quadrature and seven-term truncated source are **not evidence** and are absent from the accepting code. The final computation uses a different, complete defining-integral algorithm with proved analytic remainders.

Two initial combined test orchestrations timed out while repeatedly running expensive reconstruction for malformed receipts. They are not counted as completed commands. The later preflight checks move structural rejection before reconstruction; the mathematical producer and its canonical moment output remain unchanged. Final ordinary and optimized test runs completed separately. A vacuous draft Jordan fixture was replaced by actual coefficient reconstruction of the equation GN=N*G before the retained tests were run.

## What is not claimed

No full repository checkout validation, Lean or other formal proof build, original parent package replay, remote CI success, actual zero computation, external simple-zero-proportion recomputation, complete literature/priority audit or independent referee identity is claimed. Metadata orientation of newer PRs is not substantive review of their manuscripts. The finite certificate does not establish a new all-height zero-free theorem.

The repository branch is intended to contain additions only. Main, the integration candidate, other research branches, their source proofs, settings, permissions and accepted statuses are not edited. Any subsequent review must use the exact published commit and compare later changes explicitly.
