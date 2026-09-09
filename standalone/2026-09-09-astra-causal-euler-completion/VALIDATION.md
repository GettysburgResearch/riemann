# EPC26 execution receipt and limits

**All mathematical claims remain PROPOSED. These checks are not an RH proof.**

From this packet directory:

```bash
python -S -B produce.py --check result.json
python -S -B verify.py result.json --self-test
python -S -O -B produce.py --check result.json
python -S -O -B verify.py result.json --self-test
```

All four final commands passed. Each implementation additionally emitted a
separate canonical reconstruction; all four files equal result.json byte for
byte. A full producer/verifier reconstruction of all 48 case records also
agrees byte for byte. `validation.json` contains actual commands, execution
times, return codes and output. The -S option isolates standard-library-only
execution from unrelated site-package startup hooks; it is not mathematically
necessary. No check relies on a removable Python assertion.

Canonical semantic SHA-256:

    ddf41a7acf1c5f427b06b218ace44a20a67e998403ed737039f168765c4bacde

Full reconstructed primitive/case-record SHA-256:

    d6cf1ed4e9a5460bee4383db4811adefd2366aa07a727e4e2907ccb1ecbdb676

## Exactly what is covered

- Ordinary Mobius prefixes at every Y=1,...,256; free/zero-at-one optima,
  stopped-source terminal term and exact rational native energies.
- 21 explicit tail perturbations testing both projection identities; all
  relevant inner products are recomputed, not asserted by a scope marker.
- 48 complete repaired OUTPUT polynomials: Y=2,3,5,7,11,13,17,19; H=Y^2,
  4Y^2,64Y^2; both free and zero-at-one targets. All nonzero output indices,
  their coefficients and the entire future enter the norms. No cutoff at
  an ordinary source height or frequency is used in these finite cases.
- Eight complete MULTIPLIER B expansions (Y=2,3,5,7, H=Y^2, both targets).
  Their complete product with the ordinary finite Euler polynomial is
  compared coefficient-for-coefficient with the independently formed output.
  The larger B dictionaries are not fully expanded or counted empirically.
- Integer prime-power exponent guards, exact late-only coefficient conditions,
  directed whole-norm bounds using integer square roots, complete coefficient
  budgets for the expanded B cases, and zero preservation.
- Controls for an omitted constant tail, an early factor spoiling the prefix,
  and the difference between zero total mass and a zero at s=1.

The compact result binds all 48 records through their rederived digest and
four retained panels. `--full-output /tmp/epc-full.json` writes the complete
case-record reconstruction. The polynomial hashes bind the full coefficient
lists computed internally; the two implementations recreate those lists.

The producer uses a Mobius sieve, sparse convolution and direct integer-cell
integration. The verifier uses trial factorization, Cartesian exponent sets,
divisor coefficient recovery and the ordered max-kernel work identity. It
imports no producer or repository module. Both programs have the same author;
implementation independence is not independent mathematical acceptance.

## Adversarial tests

Each verifier mode rejects 12 genuinely changed, freshly resealed reports:
RH/scope inflation, integer/float and boolean/integer aliases, reduced coverage,
a wrong prime-power lift, altered energy/optimum, omitted output count, discarded
terminal tail, a false complete-B coefficient digest, and a reduced projection
count. A pristine temporary file passes first. The actual validation function
reads each altered JSON file and compares canonical typed JSON against its
primitive reconstruction; rejection is not caused by a stale checksum.

## Unperformed work

No full repository validator/build, independent mathematical peer review,
external formalization, frequency quadrature, actual zeta-zero computation,
broad priority audit, or full replay/import of the previous NRT26 artifact
bundle was performed. The analytic all-Y bounds and RH implication require
review of PROOF.md; finite tests do not establish them. The native subpower
estimate is explicitly missing. The old written proof is preserved only as
historical motivation, not a newly verified dependency.

A checksum manifest authenticates the exact prepared packet files, excluding
itself. Its identity is anchored by the published Git commit, not by a claim
that an attacker cannot replace an unsigned local manifest. Separate bundle
validation records the add-only patch roundtrip; that fixture is not a full
repository checkout.
