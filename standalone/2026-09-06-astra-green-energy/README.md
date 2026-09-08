# Full signed energy: a finite Green form and one unresolved endpoint

**RH, uniform full-source gain, and subpower energy remain unproved.**
Proposed component proofs and bounded validation; independent review needed.
This is an author continuation of PR #805, not an acceptance verdict.

The frozen parent is `7919f443c0c2c2a87f95d3237d4fe77fb87f9a74`. All earlier
packets, including growth-transfer and balanced-lift, are unchanged.

## What the continuation adds

The EXACT full norm of any balanced odd parity source is a finite positive
Green form. Its rational-frequency source retains every odd index and all
multiples. Sorting its tangent mesh gives explicit squared cumulative charges;
the corresponding inverse is tridiagonal. For rational source coefficients,
the full squared norm divided by pi is algebraic. No infinite numerical Gram
tail or free coarse component remains in that formula.

For the actual rational balanced optimum, an elementary positive scalar
convolution removes the previous logarithmic losses: for M>=128 the detail
error is below 18/M and |lambda_k-mu(k)|<72k/M. This is not full-norm control.
The complete Green energy above 1/log(2M) is O(log^3 M), unconditionally.
The remaining endpoint current is signed. Its first interval already contains
(D*M_odd-A*Phi_odd)/(S*D-A^2). The derived lower bound does not estimate that
quantity from above.

A hypothetical zero with real part beta>1/2 forces positive-power energy at
this shrinking endpoint, with lower exponent (2beta-1)/(2-beta). This follows
from the prescribed source's expanding physical window and complete Mellin
identity. The endpoint's subpower bound is NOT proved.

## Read and reproduce

1. PROOF.md sections 1-3: exact full-norm transformation and inverse.
2. Sections 4-6: all-scale coefficient bounds, complete complement, first interval.
3. Sections 7-8: conditional RH implication and exact stopping point.
4. NUMERICS.md, SOURCES.md, SOURCE_LOCK.json and VALIDATION.md.

From this directory, with the unchanged balanced-lift sibling present:

```sh
python scripts/replay.py --check
python -O scripts/replay.py --check
python scripts/test_replay.py
python -O scripts/test_replay.py
```

No third-party Python package is needed. The checker authenticates two frozen
parent files but executes no parent code. The numerical module is compiled
from the authenticated local source bytes, not a bytecode cache. The checksum
inventory is nonempty, exact, POSIX-relative and rejects symlinks/extra files.

Four fixed complete energies are enclosed, not a broad parameter campaign.
Their values do not establish any asymptotic ceiling. Classical Fourier,
Green-kernel, divisor, cotangent and Nyman--Beurling ingredients are credited;
no external novelty or priority is asserted. There is no Lean build, new zero
census, remote CI result, or independent referee acceptance in this packet.
