# Validation, exact commands, and unperformed checks

## Source and arithmetic contract

This is an author research packet on PR #805, based on
`0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`. Only the new sibling directory
is to be added. The original 22 files are preserved byte-for-byte.
Two parent proofs are SHA-256-bound and authenticated before acceptance;
no parent Python code, bytecode cache, zero table or numerical zeta value
is consumed. The source is the literal integer Mobius/fractional-part
system, not a zero-fitted finite spectrum or internally consistent JSON.

The checker uses Python 3.13.5 and the standard library only. All arithmetic
entering acceptance is integer or Fraction. The optimizer is normalized by
8/pi^2 so its coefficients are rational; pi is not approximated in this
replay. The finite operator algebra represents D_i D_j = D_(ij) exactly,
including prime powers in the forward and inverse convolution sequences.
No infinity limit or Hilbert-space norm is inferred from sampled data.

## Executed bounded coverage

The replay reconstructs **4,353 exact controls** in each interpreter mode:

- independent factorization versus divisor-recursive Mobius values through 96;
- finite floor, harmonic, 2-adic, and integer-damping identities through 96;
- all operator convolution coefficients through 81, including nonsquarefree
  inverse coefficients, and full summatory cutoff identities through 32;
- exact rational fractional-part values and initial horizons through 32;
- duals through index 32 paired with every generator through index 48;
- explicit first-cell overlap, missing-squarefree and nonsquarefree controls.

`verification.json` is reconstructed from those primitives and records the
per-family counts. Normal and optimized acceptance outputs match. Repeated
unit-test reconstructions are not counted as new mathematical controls.

Seven unit-test methods pass in both modes. The CLI method exercises
**13 distinct actual subprocess refusals per mode**: incorrect RH status,
empty scope, Boolean scope alias, changed coefficient, extra output key,
duplicate JSON key, floating-point alias, wrong parent commit, omitted
inverse prime-power data, changed proof bytes, empty manifest, unexpected
file, and changed parent proof bytes. Semantic output mutations are resealed
where appropriate so refusal is not merely a checksum mismatch.

The normal suite completed as one invocation. Initial aggregate optimized
invocations hit the execution-tool time limit and are not counted as passes.
The complete optimized suite was then run in four disjoint CLI groups below;
all 13 cases and all seven test methods completed successfully. The repeated
six non-CLI methods are counted only once per mode.

```bash
# Run in standalone/2026-09-06-astra-growth-transfer/
PYTHONDONTWRITEBYTECODE=1 python3 scripts/replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/replay.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_replay.py

GT26_CLI_CASES=rh_flag,scope_empty,scope_bool \
  PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
GT26_CLI_CASES=changed_coefficient,extra_key,duplicate_json \
  PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
GT26_CLI_CASES=float_alias,bad_parent,missing_prime_power \
  PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
GT26_CLI_CASES=proof_byte,manifest_empty,unexpected_file,parent_proof_byte \
  PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
```

Without the optional case filter the CLI test runs all 13 cases. Its output
reports the actual number executed; an empty or unknown filter is rejected.
The checksum inventory has exactly eight named POSIX-relative paths, plus
the manifest itself. It rejects missing/extra paths and symlinks. Both
parent proof byte identities are separately checked; the manifest is not
misrepresented as an external signature or independent scientific review.

## Analytic boundaries

PROOF.md supplies proposed full arguments for absolute operator convergence,
Mellin--Plancherel transfers, norm-growth exponents, the initial-horizon
nonconvergence obstruction, and target-support classification. These are
not established by the finite replay. The Balazard--Saias zero-free
hypothesis is retained in the exact-exponent argument. The support
sufficiency uses the RH-conditional damped approximation theorem. The
unconditional classical-scale norm estimate imports the standard quantitative
Mertens estimate, not the numerical constants or finite zero data in its
modern explicit source. Those analytic results were not reproved by code.

No uniform block gain, subpower full-norm bound, RH proof, improved zero-free
region, or zero-proportion theorem is claimed. No Lean build, proof-kernel
check, broad prime/conductor/zero campaign, new Gram-matrix campaign,
predecessor test suite, Windows run, remote CI success, or independent
referee acceptance was performed or claimed. This packet does not repair
the predecessor's Windows manifest portability issue by changing its source.

## Delivery

The intended publication is an add-only non-force commit on the existing
research branch. Final remote head, tree and blob observations belong in
its separate publication receipt, not recursively inside the source lock.
The download includes the unchanged parent packets needed for source
checks and the execution/publication receipts. Final clean-extraction
replay and byte comparison are recorded in that receipt when executed.
