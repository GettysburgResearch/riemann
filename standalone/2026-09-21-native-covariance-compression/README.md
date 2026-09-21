# NRC32: native covariance at bounded resolution

**Proposed component mathematics requiring independent review. No full native
coarse-covariance bound or RH proof.** Additive continuation of PR #905,
parent `98cf588261473724178231c667595fc09cc216fe`; earlier files are unchanged.

Read [PROOF.md](PROOF.md), then [VALIDATION.md](VALIDATION.md). Replay:

```sh
python -I -S -B verify.py --receipt RECEIPT.json --write result.json
python -I -S -O -B verify.py --receipt RECEIPT.json --check result.json
```

Only the Python standard library is required. `result.json` is generated,
not a required repository input. Its full canonical SHA-256 is authenticated
by RECEIPT.json. The downloadable archive also includes that generated report
and execution controls. No compiled extension, network, zero table or floating
special-function value is used by acceptance.

## What is controlled

For b=Y+1, the actual native reciprocal square-step output has:

1. A complete sharp high-Mellin energy bound `44/3+8H_(b^2-1)/b` above `6b`,
   for the explicitly defined endpoint continuation. The endpoint term is
   retained. This is NOT DMC31's different global Newton-source projection.
2. An exact orthogonal coarse/detail split. Fewer than `10b` cubic-mesh means
   leave total detail energy `<5/6` on the ENTIRE square step. Precision R
   gives `<5/(6R^2)` with fewer than `10Rb` means when b>=R^3.
3. An exact finite formula for every coarse mean using only mu through Y.
   Full directed-energy panels through 1,048,575 are reconstructed from the
   prefix through 1,023, with an independent future sieve used only to check.

The remaining coarse sum is still a dense signed arithmetic problem. The
largest finite panel puts about 98.7% of annular energy in it. Neither this
percentage nor the finite observed sizes are extrapolated into a theorem.

## Source and overlap map

- ACC29/SFC30/DMC31: PR #905 parent above, path
  `standalone/2026-09-20-anchored-composite-covariance/`.
  The original DMC31 publication was verified already present; no duplicate
  upload or claim of a main merge is made.
- DSE27: `4e8dea7004874d1a9c679b58db1dca1fbb539388`,
  `standalone/2026-09-19-divisor-square-mesh/PROOF.md`, sections 1--4 read.
  Its physical-energy square-root mesh is credited, not relabeled as ours.
- MCB31: PR #904 publisher `aaea3f9605a430600bea0189397d93ca315b5f98`,
  `standalone/2026-09-20-microscopic-composite-band/PROOF.md`, sections 1--4
  read through the available extract. Its rational-angle microscopic band is
  different from Mellin frequency and from block-constant projection. No
  unexplained commuting or combined low-band theorem is claimed.
- Huxley--Watt, *Mertens Sums requiring Fewer Values of the Mobius function*,
  arXiv:1807.05890. The primary abstract was checked for attribution of the
  weighted short-source Newton identity; a full paper re-audit was not run.
  The finite identity actually used here is proved in PROOF.md section 1.

The argument does not import unreviewed predecessor estimates as axioms: its
component estimates are rederived. Prior packets are context and motivation.
There is no external novelty certification, full-repository validator run,
Lean build, remote CI result or independent mathematical acceptance.
