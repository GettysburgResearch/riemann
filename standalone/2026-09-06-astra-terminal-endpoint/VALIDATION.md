# Validation and unperformed work

Status: bounded author verification; mathematical/code review required.
RH, uniform full-source gain, and TE26.OPEN remain unproved.

## Exact source binding

SOURCE_LOCK.json fixes parent acb0a25a373b427c9694aff78cba396f26963e8b and
three unchanged files. Before executing the parent mathcore, replay.py checks
the literal SHA-256, byte count and Git blob against hardcoded values, then
compiles those bytes directly. Parent proof and numerical remainder note are
also checked. No bytecode cache or network source supplies a numeric input.
The new nonempty eight-path manifest uses POSIX paths; missing, extra,
duplicated and symlinked paths are rejected.

## Arithmetic and coverage

Mobius values through 513 are constructed by a sieve and checked by the
complete divisor identity; through 256 they are independently compared with
the parent's trial-factor construction. Exact Fractions produce the terminal
sources and scalar values at M=3,33,163,513. Rational source identities cover
96 physical cells per terminal panel. The scalar renewal is checked at
191 fixed rational points; interpolation is checked at 27 rational points,
and finite-source Mellin integration is evaluated independently on its
piecewise-linear intervals, including the infinite linear tail.

The five terminal full-energy panels have M=3,5,9,15,31. Two additional
panels use the unchanged constrained optimizer at M=8,16. Complete Green
meshes retain every rational frequency and all cross terms. The harmonic
norm is an exact rational quadratic polynomial in log2, not quadrature.
Sine versus primitive checks retain orientation, and a separate 256-cell
physical prefix with an amplitude tail checks each complete energy.

The inherited directed arithmetic uses 224-bit integer intervals; pi comes
from Machin's formula with 96-term rational arctangent bounds, trigonometric
functions from 80-term Taylor polynomials with explicit two-sided remainders,
and logs from a 96-term atanh series after exact range reduction. The parent
NUMERICS.md states the remainder proof; this pass reads and inherits it.
No floating-point value is accepted. The new sampling criterion itself uses
only rational scalar values and needs none of these transcendentals.

## Commands and outcomes

From standalone/2026-09-06-astra-terminal-endpoint/:

```bash
python -B scripts/replay.py --write verification.json
python -B scripts/replay.py --check
python -O -B scripts/replay.py --check
python -B scripts/test_replay.py
python -O -B scripts/test_replay.py
```

Both check modes reconstruct identical verification bytes and pass 1,704
controls. Both test modes pass seven unit methods, including twelve actual
CLI refusal cases per mode. Semantic output mutations are resealed to test
primitive reconstruction beyond hashes. Rejections cover an RH claim, a
false-to-zero flag alias, wrong scalar, wrong coefficient, empty panel,
duplicate JSON key, changed proof, extra/missing file, changed parent code,
changed parent proof and a symlinked payload. Unit tests also reject bools,
floats, out-of-scope integers, even terminal cutoffs and unbalanced sources.

Verification JSON retains exact rational grid scalars, source coefficients,
harmonic polynomial coefficients, and outward full/first Green and harmonic
energy endpoints. Each full harmonic mesh is reconstructed and its canonical
serialization hash retained. The finite values are not asymptotic evidence.

## Unperformed checks

No broad prime, zero, conductor, coefficient or large-matrix campaign; no
new zero census; no Lean or other proof-kernel build; no Windows run or
historical Windows-path repair; no external interval certificate replay;
no independent mathematical acceptance; no remote CI claim. The parent's
whole checker and unit suites were not rerun as part of this new checker.

The scope includes proofs of conditional implications, NOT a proof of the
unbounded arithmetic premise. The first Green interval of the old optimized
family has not been declared sufficient: the single-scalar criterion uses
the explicitly different terminal family. Arbitrary subsequences are not
covered by the fixed fourth-power interpolation theorem.
