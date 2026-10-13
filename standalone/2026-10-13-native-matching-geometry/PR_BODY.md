## Status

PROPOSED component proofs. No full native moment, improved zero-free boundary,
or RH proof. Independent mathematical review is required.

This packet is intended to be stacked on #942 at
`377f548cab8759399aca80ed3188c495667d562a`. It adds only one standalone directory.
The authoring session did not have a working publishing route; this body is a
handoff template, not evidence that a PR has been opened.

## Results

- Sharp fixed-order principal reference:
  `B_(2k)(D) asymp D^k log(2+D)^((k-1)^2)`, for original squarefree columns,
  a fixed nonnegative compact test, exact local zero densities, and arbitrary
  unitary multiplicative column phases. Sixth-power aliases remain. Lower
  bounds use isolated squarefree charge blocks near the top of the support.
- Physical principal calibration without D^epsilon:
  sharp relative error `O(H^(-1/2))`; fixed-Schwartz relative error
  `O(log(2H)^(k^2)/H)`, uniformly in column scale. Constants depend on k.
- A graph-nullity count with unequal vertex caps and weighted divisor means.
  It sharpens the no-singleton signed-sector upper bound to
  `O(H D^k log(2+D)^(k(2k-3)))` for k>=2.
- The classical logarithmic exponents/Birkhoff connection are explicitly
  credited to Harper--Nikeghbali--Radziwill and Heap--Lindqvist. No independent
  random-model theorem is presented as physical-row cancellation.

## Remaining gap

The complete native signed nonprincipal large-radical sum with large singleton
products is still unbounded at the requested scale. The smaller no-singleton
sector here does not supersede #940's larger smooth-singleton union.

## Validation

165,577 exact finite predicates, ordinary and optimized replays byte-identical.
A separate exact principal-only calibration includes all good squarefree ideal
columns through hard-window scale D=2048, with 96-bit dyadic reference enclosures
and two sharp row heights at each of six scales. No full physical remainder is
newly measured. The unchanged arithmetic helper is authenticated to #942.

Read PROOF.md Sections 3--5 first, then VALIDATION.md. The proof and checkers
have one author. No independent referee, formal proof build, remote CI or
full-repository validator has been run. The manifest binds bytes, not truth.
