# SPL26: a small concrete improvement, not another RH completion criterion

Proposed computer-assisted component proof. Independent mathematical and code
review required. **RH is not proved.** This packet responds to the critique of
repeated RH-equivalent reformulations by targeting an actual numerical proportion.

The strengthened Montgomery--Taylor seven-point inequality uses pressure
`1/3433` and lower bound `13777/4000000 = 0.00344425`. The pressure differs from
the older `1/3000`, so its local constant must NOT be compared in isolation.
The complete interval exhaustion closes 920,463 nodes with zero unresolved
terminal cells. A rational witness puts the same-pressure infimum below
`0.003444256`.

Using the existing stability-enhanced rank inequality and the published
unconditional trace/sampling/tail inputs, a 308-point block yields

```
liminf simple-and-on-line zeros / all zeros >= 0.673030838638165527...
liminf distinct zeros / all zeros          >= 0.836515419319082763...
```

The first bound improves the repository's earlier proposed 280-block value
`0.673009652279136912...` by about 21.186 per million in the asymptotic proportion.
No current-world-record or exhaustive-priority claim is made. The entire zeta
argument is in PROOF.md, with the exact published inputs stated. No new
RH-strength arithmetic premise is left for reviewers to supply.

## Reading and execution

Read `PROOF.md`, `CRITIQUE_AND_DECISION.md`, and `VALIDATION.md` before using the
constant. `SOURCES.json` credits the inherited ainta algorithm and repository
block corrections. The new implementation uses MPFR-directed kernel enclosures,
outward binary64 search, and a stronger convex-quadratic lower certificate.
An independent rational calculation checks the final constants and selected
primitive values; it is not a second complete continuum proof.

On the tested LP64 Linux environment, with C++17 and MPFR 4.2.2 available:

```sh
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json --compiler clang++ --precision 256
```

No pip dependencies are required. The C++ build links `libmpfr.so.6`. The
header-free ABI declaration is deliberately restricted to LP64 and has a
compile-time size check. Windows/LLP64 is not supported by this supplied build.
The generated kernel table and binaries live in a temporary directory, not
inside this sealed packet. They are freshly reconstructed on every acceptance.

`--emit PATH` is producer-only. `--keep-dir PATH` preserves generated scratch
artifacts for inspection. Do not interpret a hash check alone as a mathematical
replay. `test_controls.py --work-dir PATH` uses a retained full-replay directory
to test actual refusal behavior and exact independent bounded algebra.

## Publication

Intended add-only branch from frozen main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`:
`research/astra/20260914-seven-point-pressure-lift`.

This authoring session has no GitHub write action. The supplied ZIP and add-only
patch are publication handoffs, not evidence of a new remote commit. A publisher
must record its actual PR and head after upload and preserve concurrent work.
Do not edit the previous Ising packet, main, reviews, or canonical status.
