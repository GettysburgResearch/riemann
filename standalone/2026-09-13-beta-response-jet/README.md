# BJR26: complete response tails and a native local zero velocity

**Proposed component proofs and finite certificates, not RH closure.**

Read [PROOF.md](PROOF.md), especially Sections 2–5 (uniform response and parameter jets), Sections 6–7 (the exact native numerical calculation), and Section 8 (the missing global sign). [REVIEW.md](REVIEW.md) separates the review questions. The predecessor is PR #878 at `e28fd6c04d315c5f31f37b2240a263cd2e0cfeaf`; no parent files are edited.

The new weighted gamma norm yields `||R_theta||<=2/3`, a complete positive Mellin-response remainder bounded by `13|p(p-1)(p-2)|(2/3)^(J+1)`, a uniform complex parameter radius `1/4096`, and finite-tree C1 error bounds. The inverse estimate is in a STRONGER norm than the parent's unweighted inverse; it is not called an improvement from 80/49 to 3.

At the actual gamma endpoint, an independent Laguerre/Gibbs representation gives an exact rational series for `partial_theta log M_theta(s)|theta=0`. Its real parts at heights 4 and 8 have opposite certified signs. One gamma-anchor zero lies in `(13.7654722174,13.7654722175)` and has initial height velocity in `(2.08931,2.08932)`. Analyticity and symmetry give a local real branch. No positive parameter interval is numerically instantiated; this is NOT a double-zero collision, a zero of xi, or proof of global critical-line confinement.

## Reproduce

Run from this directory with Python 3.10 or newer:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Only the Python standard library is used. Exact Fractions handle the response coefficients, polynomial identities and scalar constants. A 512-bit outward integer implementation handles log-Gamma and digamma; it is adapted from #853, not a second independent special-function backend.

The packet has 11 regular files; SHA256SUMS authenticates the other ten. Its integrity contract is relative to a trusted manifest/commit. It does not protect against an adversary replacing both checker and trust anchor. The checksum file does not machine-prove the analytic arguments.

The five-method suite performs one complete pristine CLI reconstruction and ten altered-record CLI refusals per interpreter mode. It also compares response enclosures at degrees 384 and 512. These are not independent analytic reviews. See [VALIDATION.md](VALIDATION.md) for exactly what was run and what was not.
