# Certified original-row restriction for the remaining Chow maps

This is a new acquisition contract. The first certified-cache continuation
stopped at its declared degree-six preflight: largest supported block898
rows by202 columns exceeded the old512-row limit. That was a mathematical
resource guard, not a RAM stop, successful degree-six acquisition or
evidence against the predicted resolution. The old producer, its26 tests,
the original full-resolution producer and every frozen file remain unchanged.

The input is the fully certified stage-five cache at
`742d68b6d3c37191589b0e6463bc122af6d90f76`, blob
`3f1689a7388de3b4cf3f33e3cc7057d51a94118b`, with the unchanged verifier
from `356160f075ee72aed21ee03a6daf30fa3222799a`. Its cache proof object is
`0ef850edcef35a4b01ed19e305e589ba1dd5efcc855b948c4062df7777e718f4`.
Every run reauthenticates the complete cache/verifier source chain and
reverifies all stage-five maps before continuing.

## Exact row-selection theorem

For one full integer weight block A with n columns, stream its original
supported rows in increasing coordinate order. Over the fixed prime65521,
retain the original rows that increase row rank. Let B be that original-row
submatrix, with r retained rows. Its modular row independence proves
rank_Q(B)=r. It has at most n rows.

Run the unchanged frozen rational kernel algorithm on B. Retain its
primitive integer kernel vectors in the original block-column order.
Verify their independence, number n-r, and their compositions against
EVERY original row of A, not just B. If they all vanish, then

    ker(A) subset ker(B), and basis(ker(B)) subset ker(A),

so the two kernels are equal. Equivalently the independent modular rows
give the rank lower bound r and the n-r full-composition witnesses give
the matching rank upper bound. No modular rank is guessed to be the
rational rank of the full matrix.

If any full composition is nonzero, record the failed modulus, selected
rows, complete restricted kernel and every nonzero full residual. Retry
only the second preregistered prime1000003. If it also fails, stop with
that negative certificate. Do not pick another modulus or hide a failed
attempt. A failure of the unchanged rational algorithm or a resource cap
also stops; it is not silently reclassified as an unlucky-prime result.

Original row indices, full target/domain bases, original ordered columns
and all weights are retained. No generic projection, row linear
combination, approximate nullspace or fitted Betti count is used.

## Limits and staged predictions

- Full target basis at most90000 entries; domain at most16000.
- Each full weight block at most4096 supported original rows and512 columns.
- Selected original-row submatrix at most512 rows by512 columns, within
  the unchanged exact kernel's old cap.
- Exact rational numerator/denominator4096bits; source/fixture64MiB.
- Root worker128MiB and free-RAM reserve2GiB; no reviewer or author jobs.

The first new run is degree six only. Predictions are checked after the
kernel calculation: domain3775, nullity127,110 old multiples of rank110,
seventeen new D3 columns. Only after root accepts its measurements may
degree seven run: domain15400, nullity776,775 old multiples of rank775,
one new D3 column. The actual old-multiple quotient algorithm remains
unchanged. Its supported target coordinates lie in the current kernel
domain block of at most512 columns; its own old preflight is still enforced.

Full kernel vectors, minimal-quotient lifts, polynomial maps and dual Tor
weights are retained. Global exactness remains the graded Nakayama/Tor
theorem in `TERNARY_CUBE_FULL_RESOLUTION.md`; no partial stage is called
a complete resolution, and no equivariant marked splitting is asserted.

## Durable complete weight blocks

The new producer may persist each completed weight block separately in
its own directory. A key binds the new algorithm and preregistration,
the exact certified source identity, full ordered matrix/basis digests,
weight and original column indices. Only complete atomically flushed
objects are reusable; temporary or partial files are not inputs.

On reuse, reconstruct the original block, reselect rows over every recorded
modulus, verify the selected modular rank, all primitive kernel vectors,
independence, full compositions and failed-attempt residuals. The final
successful attempt must prove the exact kernel equality above. Thus a
checkpoint saves rational elimination only, not source verification.
Changing the new algorithm or its declared acquisition invalidates keys.

These operational checkpoints are separate from the final proof artifact.
The latter has a new producer/test identity and binds all source records,
certificates and the final replay statement. The older26-test contract is
not weakened or repointed to this implementation.
