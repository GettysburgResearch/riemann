# Gauss–Thorin positive-defect hierarchy

**Proposed mathematics; independent review required. RH is not proved.**

[PROOF.md](PROOF.md) connects PR #850's variance-matched gamma seed with PR #846's positive stochastic defect. It gives a canonical finite-gamma family at every moment order, a positive probability law for the complete Laplace error, its exact branching transport, and a source-bound Mellin error formula. The construction does not prove that its reflected Mellin transforms are zero-safe.

The first member is exactly `Gamma(5/2, scale 2/5)`. Its complete cubic defect has coefficient `4/175` and branching factor `31/80`. Higher Gaussian quadratures match the Brownian source through order `2m`; the complete error has order `2m+1` and an explicit positive-law factorization. The seed error constants admit the superfactorial bound in GTP3.

A directed diagnostic proves that the straightforward positive phase-derivative extension fails at the second member: the derivative at height 8 lies strictly in `(-13/1000,-11/1000)`. This is not an off-critical zero and does not refute RH or zero-safety of that member.

## Reproduce

Python 3.10 or later; standard library only:

```sh
python check.py --out checks.json
python check.py --verify checks.json
python -m unittest -v test_check
python -O -m unittest -v test_check
```

The checker reconstructs four exact Gaussian-quadrature fixtures from the sinh series, then encloses one complete hypergeometric/digamma diagnostic using directed dyadic arithmetic and analytic tails. It does not verify the analytic theorem packet, BPY's imported theorem, or RH. [VALIDATION.md](VALIDATION.md) records exactly what was run. [SOURCES.json](SOURCES.json) freezes selected sources and inspection limits.

For review, prioritize equations (8), (12), (19), (22), and (30) in the proof. The proposed zero-free ending in section 8 is explicitly open. No main-branch scientific status or existing claim ID is changed.
