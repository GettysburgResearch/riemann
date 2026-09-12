# Validation, arithmetic contract and limits

The mathematical assertions are proposed paper proofs, not independently
accepted mathematics or a machine proof of RH. Publication and file hashes do
not change that status.

## Bounded reconstruction

`check.py` uses only Python standard-library integers and exact Fractions.
Its counterlaw certificate applies the global inequality
1-v<=exp(-v)<=1-v+v^2/2 to a whole Gaussian integral and exact Gaussian moments.
It uses no Gaussian quadrature, numerical roots, floating arithmetic, zeta
oracle or actual theta moment. Bounds are rational inequalities, not ordinary
high precision described as directed intervals.

The retained result separately records 40 entropy panels, four formal rational
potential constructions, 28 complete spin/Walsh panels covering 2032 individual
coefficients, 132 conditional-attraction controls, four complete four-spin laws,
75 Bernstein binomial-variance identities, three partition-normalization panels,
five rational source/cumulant constants, one additional connected attractive
four-spin law, and one complete counterlaw enclosure.
The 2032 coefficient comparisons are PART OF the 28 panels, not additional
independent theorem counts. The large N values recorded for four potentials
are exact integer parameter definitions, not enumerated large spin systems.

Two finite methods reconstruct spin-subset coefficients: evaluation on all
configurations followed by a Walsh transform, and ordered-index parity counting.
They use no imported parent code. Same-author independent representations do
not constitute independent mathematical review.

Commands retained:

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Both full checker modes reconstruct identical JSON. Each test mode checks one
pristine copied packet and NINE actual corruptions through the accepting CLI:
false RH flag, false pair-realization flag, Boolean/integer alias, duplicate
JSON key, resealed entropy-coefficient producer mutation, resealed four-spin
producer mutation, changed unsealed manuscript, an extra file, and parent drift.
The producer mutations fail reconstruction of the mathematical identities,
not only hashes. The test only prints its passing count after all nine return
an actual rejection. `--emit` is producer-only and does not authenticate.

## Delivery boundaries

The complete inventory is nine regular files with eight SHA256 entries. Source
bytes of the 26436-byte parent proof were authenticated to Git blob
4f3cd5a983b651425ee659d021ce2875a711ef44; parent code and seed certificates were
not rerun. Sources and their actual reading scopes are recorded in SOURCES.json.

A minimal temporary-Git add-only patch roundtrip and a clean ZIP extraction
are replayed in both modes. These preserve an unrelated sentinel and every
packet byte; they are not a full riemann checkout, repository-wide validation,
remote CI, a Windows run, or a Lean/kernel build. Actual command outputs and
publication hashes are in the separately delivered receipt.

No growing theta polynomial sequence, large entropy model, pair replacement,
actual theta cumulant, new positive-window certificate or complex-zero census
is numerically computed. Uniform convergence of the infinite construction is
proved in the manuscript, not by the finite panels. Its pair-Ising replacement
is unproved, so RH remains open in this work.
