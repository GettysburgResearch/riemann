# Executed validation and limits

The accepting code uses Python standard-library integers and exact Fractions.
The only nonrational values in the explicit N=256 certificate are n^(-2/3),
which receive 96-bit outward brackets using integer cube-root bisection.
No gamma, zeta, xi, numerical zero, numerical contour, or transcendental
floating implementation enters acceptance.

## Mathematical reconstruction

The retained result reconstructs the positive moment formula by independently
convolving Gamma(2)/n^2 moments, checks the complete finite Laplace partial
fractions, and checks every removable negative-integer factor for 1<=N<=12.
It also compares a Liouville sieve with independent trial factorization
through 512, and reconstructs all 256 signed terms of the explicit twist.
The finite prime-product tests are only monomial-geometry controls; they
are not an experimental proof of PNT or of its sufficient cutoff.

The principal finite output is:

```
-0.022398637467469 < A_256^Liouville(1/3) < -0.022398637467468
 0.249365651389428 < A_256^Liouville(1/2) <  0.249365651389429
```

The actual approximant's high zeros are proved to EXIST through the paper's
recurrence/Rouche argument. No zero ordinate or simultaneous phase-return
height is certified. The finite signs alone are not the global zero proof.

## Commands

Both commands reconstruct the same JSON bytes:

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
```

Each of the following completes one pristine copied replay and six actual
CLI refusals: false RH flag, altered cutoff, floating numeric alias, duplicate
key, resealed producer-weight mutation, and unsealed manuscript change.

```
python -I -S -B test_verify.py
python -I -S -B test_verify.py --optimized
```

The unsealed-text refusal authenticates bytes, not the correctness of a
changed mathematical proof. Semantic result and producer changes are resealed
so their refusal exercises reconstruction rather than only hashes. No prior
research checker, repository-wide build, remote CI or Lean build is run.

A clean archive extraction and a minimal temporary-Git add-only patch replay
are performed separately. They authenticate this packet, not the complete
Riemann repository. No original branch or canonical theorem is modified.

## Scouting, explicitly non-proof

Before selecting the rational certificate, 55-digit mpmath calculations
examined zeros of the finite P_N and Liouville-twisted real values at several
cutoffs. Those calculations suggested N=256. Their floating roots and values
are excluded from the accepting result. The final sign computation has no
mpmath dependency. The all-sufficiently-large-N argument is analytic and
independent of those scouts.

The source PDF pages containing the Mellin/probability interpretation and
finite approximation formulas were inspected. One page screenshot failed
with a cache miss; other requested pages were successfully rendered. No claim
of a new publication date is inferred from the PDF's typesetting date.

## Unverified global claims

W1--W3 are author-proposed paper theorems requiring independent review. Code
checks do not machine-prove the Mellin analytic continuation, compact rate,
PNT, finite torus approximation or Rouche passage. There is no unconditional
RH proof, no new xi zero-free region, and no claim that these approximants'
off-line zeros survive the N limit. External novelty has not been assessed.
