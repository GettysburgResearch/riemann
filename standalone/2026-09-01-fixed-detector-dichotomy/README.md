# Fixed-detector positivity: the Landau–Ingham dichotomy

```text
Status:            PROVED (L-109000, T-109001), REFUTATION (R-109002),
                   EXACT/NUMERICAL RECORD (X-109003), EXACT CONTROL EXPERIMENT (X-109004).
                   RH remains unproved; nothing here is a route to RH.
Scope:             every fixed zero-safe Möbius/β detector of the 2026-08-22 release
                   (SHARP scalar h, rows 2 and 3, fixed 5:3 scalar, ratio-eight wavelet,
                   logarithmic-box smoothing); global statements.
Exact sources or dependencies:
                   L-99270, L-99272 (PR #653 @ e928fd615d75) for h and the consumer;
                   L-96000 (main @ 677203992eb0) for the rows;
                   L-99261 (PR #649 @ 433fd3662f7b) for the 5:3 scalar;
                   standalone/2026-08-20-minimal-mobius-wavelet/PROOF.md (PR #674 @ 9962f7f712ad);
                   Landau's theorem; Ingham (1942), reproved here as L-109000;
                   Titchmarsh Thm 14.2 / 14.16 (RH-conditional bounds on 1/zeta);
                   Odlyzko, first 100,000 zeros (9 decimals); mpmath 1.3.0.
What was actually run:
                   scripts/zetaprime.py  – zeta'(rho) at the first N zeros (mpmath, 20 digits);
                   scripts/detectors.py  – Möbius sieve to 1e7, direct evaluation of the six
                                           detectors, comparison with main term + zero residues,
                                           zero-mass tables, sign census;
                   scripts/ffield.py     – exact census over F_3, F_5, F_7 of the cumulative
                                           detector for quadratic characters mod irreducible Q.
                   Raw outputs are in outputs/ with SHA256SUMS.
Smallest remaining gap:
                   none for the theorems. The LI-conditional falsity of the pointwise SHARP
                   tail would become unconditional after a Kronecker-alignment computation
                   on a few thousand zeros (the first 17,496 already carry mass 3.22 > c_0 = 2.05).
```

## What this packet establishes

1. **Negative-mass targets are RH, verbatim.** For every fixed zero-safe band kernel
   `K`, `∫_1^X (D_K)_- dt/t = X^{o(1)}` is equivalent to RH (T-109001 A). The release's
   Mellin–Landau premise is therefore not an intermediate statement.
2. **Eventual-positivity targets are RH-plus-summability, or false.** If the detector has
   a growing positive main term (rows 2, 3, the 5:3 scalar, the 67-box smoothing) the
   target is implied by RH only together with a summability hypothesis on the zeros and
   implies RH; if it has a bounded main term (the SHARP scalar) it is false under linear
   independence of the ordinates, with the first few thousand zeros already carrying more
   oscillation mass than the main term; if it has no main term (the ratio-eight wavelet)
   it is false unconditionally (R-109002).
3. **Control where RH is a theorem.** Over `F_q[T]` the same detector, with Weil's RH in
   hand for every character, is eventually nonnegative for a minority of quadratic
   characters and negative infinitely often for the rest (X-109004). Positivity is a
   numerical accident of central value against residues, never a mechanism.

Read `PROOF.md`. The consequences for the open-cut inventory are in its §6.

## Replay

```bash
cd standalone/2026-09-01-fixed-detector-dichotomy/scripts
# zeros: place Odlyzko's zeros1 (first 100000 zeros) as ../zeros1.txt or fetch it from
# https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1
python3 zetaprime.py 20000 zetaprime.txt        # ~20 minutes
python3 detectors.py 10000000                   # expects zetaprime_100k.txt; see script header
python3 ffield.py 3 6 20000
```

`detectors.py` reads `zetaprime_100k.txt` from its working directory; rename the output
of `zetaprime.py` accordingly. All arithmetic is ordinary double precision except
`ζ'(ρ)`, which is `NON_DIRECTED_HIGH_PRECISION`; the theorems do not depend on any
numerical value except the simplicity of `ρ_1` and `K̂(iγ_1) ≠ 0`, both of which are
elementary to certify.
