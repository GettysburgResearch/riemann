# BNR26 execution and evidence boundary

The four final commands in validation.json completed with exit code zero.
Producer and separately written verifier reconstructed byte-identical result.json
in normal and optimized isolated Python. All mathematical acceptance uses
integers/Fractions and explicit checks; no removable assertion implements it.

The verifier imports neither producer nor repository modules. It authenticates
Mobius values by trial factorization rather than the sieve, builds the Newton
output through complete divisor fibers rather than pair convolution/multiples,
uses signed-work energy instead of cumulative-cell energy for the exact small
panels, and reconstructs the raw finite tail panels by literal floor sums.
The specified large energy cells use the same 128-bit outward arithmetic
CONTRACT; two ways to calculate a native value are not two independent authors.

## Complete declared finite corpus

- Recursive seed 1, followed by exact new prefixes through 3,15,255,65535.
  Every generated coefficient is checked, not merely a hash of claimed output.
- 72 compact constrained-projection perturbations at Y=1,...,24.
- 24 first-omitted-coefficient identities at (Y+1)^2; that endpoint is not
  falsely included in the native prefix.
- 24 complete joint energy/mean transitions; 440 centered hyperbola panels,
  including every nonzero collar and integer sawtooth endpoint term.
- 124 energy/mean cutoff enclosures; the specified candidate bound passes
  66 pairs, Y=1,...,64,127,255. This is NOT an all-Y or cofinal certificate.
- Four full raw-stage energy enclosures, integrating every cell k<4096 and
  paying the entire x>=4096 tail with the written analytic bound.
- Four generic non-Mobius quadratic countermodel panels, b=16,32,64,128.

The compact report stores full selected rows and content hashes of complete
reconstructed arrays. Both programs independently reconstruct those arrays;
passing the report is not merely checking internal agreement of derived JSON.
There is no externally supplied prime/zero table in the accepting computation.

## Adverse inputs

Each verifier mode rejects twelve altered and RESEALED report files: false RH
flag; boolean/integer and integer/float aliases; a changed prefix endpoint;
reduced kernel/primitive coverage; wrong first omitted coefficient; deleted
raw-tail cost; fake-source relabeling; deleted family; changed energy; and
changed recursive output identity. A duplicate-JSON-key file is also refused.
Canonical typed serialization is compared after primitive reconstruction.

Mutation tests reuse one reconstructed expected payload per full run. They do
not claim twelve fresh runs of every primitive arithmetic calculation, still
less twelve mathematical proof reviews. The producer's --check is nonmutating.

## Disclosures and limits

An initial serialization of very large exact annular fractions exceeded Python's
decimal digit limit. Before the canonical report was frozen, those finite sums
were replaced by explicit 128-bit outward cell sums, retaining a bound for
every rounding error and the entire analytic source tail. All final commands
were rerun on that protocol. Exploratory floating printing was diagnostic
only; no floating arithmetic or numerical quadrature enters acceptance.

No full Riemann repository checkout validator, parent checker, external proof
build, directed zeta evaluation, zero census, all-scale energy estimate, or
comprehensive priority review was run. The all-parameter claims rely on their
written arguments. The unbounded source-specific gain is OPEN.

The manifest is an inventory of the prepared bytes, not a proof of mathematics.
The external bundle receipt records a local add-only Git fixture/ZIP round trip
separately. Neither that fixture nor remote Git-tree identity is a complete
repository execution. Both implementations and proofs have the same author;
independent mathematical and code review remains necessary.
