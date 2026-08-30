# Canonical Koszul analytic parent

Status: proposed exact source construction for programme #764.
The old finite-parent obstruction is preserved; this packet constructs a
genuine infinite parity-graded parent for the `(2,3)` Segre source.

[MATHEMATICS.md](MATHEMATICS.md) defines the coordinate algebra and its
quadratic-dual Lie modules before forming the scalar series. Equivariant
Koszul exactness and PBW give a Fredholm superdeterminant with sharp
trace-class disk `|t|<1/2`, and sharp Schatten-p disk `|t|<2^(-1/p)`.
A native finite resolution gives an independent sharp zero-free disk:
unitary inputs reach its boundary only when both input matrices are scalar.

Classical imported inputs are explicitly named in the proof. No external
priority, global L-function, or RH/GRH consequence is claimed. Analytic
regularization beyond the ordinary determinant disk remains a separate gate.

`source.json` fixes the primitive rank profile and ordered-word quadratic
map. `replay.py` reconstructs every relation fibre and every Lie bracket
through degree three (largest word space: 216). It independently checks
the native syzygy maps, torus characters including repeated inputs, signed
Euler coefficients through degree 24, and rational enclosures for the
infinite product using the proved tail bound. Wrong duals, wrong parity,
out-of-domain inputs, and forged source contracts are explicit controls.

From this directory, with Python 3.11 or newer:

```text
python -B replay.py --write
python -B replay.py --check
python -B -O replay.py --check
python -B -m unittest discover -s tests -p test_replay.py
python -B -O -m unittest discover -s tests -p test_replay.py
```

`--write` regenerates the expected artifact; acceptance requires a
subsequent `--check`, which recomputes everything from the authenticated
primitive source. The fixture binds the source/proof/producer/test hashes
with LF normalization and authenticates the precursor's exact Git blob.
External classical theorems are cited and reviewed, not machine verified.
Fresh clones need the named precursor commit in their history; fetch full
history if a shallow clone omitted it.

Root's serialized run passed Ruff, producer write/check, optimized check,
and all 23 tests in both normal and optimized Python. The independent
reviewer has read the proof, classical inputs, producer, and tests with no
blocker; a report binding the checkpoint SHA is pending. No large quotient,
build, CAS, or parameter sweep was used.
