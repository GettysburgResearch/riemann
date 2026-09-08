# Validation and limits

Environment: Linux, CPython 3.13.5, GCC 14.2.0. Acceptance uses only the Python
standard library, integer-directed 192-bit arithmetic, and exact Fraction
inputs. The finite arithmetic is a computer-assisted proof with the explicit
Euler--Maclaurin/rounding contract in PROOF.md; it is not a Lean/kernel proof.

## Completed runs

```
python -I -S -B verify.py --write result.json
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B test_rejections.py --optimized
```

Normal and optimized reconstructions agree byte for byte. Each reconstructs
all four actual candidate norms and all four constrained-minimum intervals,
including the entire infinite period weights and dual residuals.

The five bounded control groups contain:

* 25 rational interval operand pairs, checking addition, multiplication and
  division against exact Fraction values;
* 78 period-residue weights, independently bracketed by 256-term rational
  partial sums and elementary complete tails, together with period mass checks;
* 154 balanced tail packets verifying finite-cell coercivity and their
  complete triangular Mobius inversion;
* 100 rational two-dimensional projection examples, including equality cases;
* nine rational complex-node Hardy Schur-complement identities.

These 466 bounded fixtures do not machine-prove the infinite analytic theorems.
The four arithmetic minimum certificates are separate from those fixture counts.
No boundary zeta function, numerical zero, external interval producer, or
quadrature evaluation is used to accept them.

In each interpreter mode a pristine copied packet passes the actual CLI.
Ten altered copies are refused: false RH status, false global-bound status,
Boolean alias, floating-point precision, duplicate JSON key, changed proof,
missing manifest, a resealed extra file, a resealed minimum, and resealed
candidate coefficients. The semantic record/candidate changes are resealed so
that reconstruction, not an unrevised checksum alone, must reject them.
The proof-byte mutation is NOT resealed and tests integrity only. Integrity
checks are not proofs that an edited manuscript remains mathematically true.

The manifest covers exactly eight files besides itself. Its expected names are
also fixed in the verifier; extra/missing paths and symlinks are refused.
No parent Python or earlier numerical producer is executed. The downloaded
parent manuscript was compared with its advertised Git blob and its separate
SHA-256 identity is recorded in SOURCES.json.

## Candidate discovery is not acceptance

A separate NumPy/SciPy calculation used the digamma period formula to solve the
finite constrained quadratic problem approximately. Free coefficients and dual
multipliers were rounded to exact rationals with denominator dividing 2^40 and
stored in candidates.json. Those numbers are arbitrary proposals from the
accepting checker's perspective. The two dependent coefficients are reconstructed
from the exact logarithmic formula (19), not rounded independently.

No floating objective, optimizer success flag or discovery Gram enters the
certificate. The accepting Gram is rebuilt from integer residue cells, explicit
logarithm remainders and the full Euler--Maclaurin remainder. The primal norm
and dual bound enclose the minimum independently of the optimizer's correctness.

## Delivery and publication

A separate delivery receipt records the archive SHA-256, exact file inventory,
Git packet tree and remote commit when successfully published. A minimal Git
patch roundtrip checks every new byte and preserves an unrelated sentinel;
it is not a full repository checkout, build, or remote CI run. The release
receipt must not be inferred from the mathematical status fields.

## What did not succeed

The finite optimization and normalization do not prove an all-Y subpower upper
bound. The original sparse-sign and signed-contour estimates remain open.
No new native annular positivity interval, zero-free region, global count saving,
independent referee acceptance, or complete RH proof is claimed. Four finite
minima cannot justify an infinite trend. Polynomial conditioning controls the
sensitivity of the finite solve, not the size of its affine minimum.
