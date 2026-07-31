# X-17203 — `q=8` two-trivial-annihilator certificate

Status: `DIRECTED_INHERITED_SINGLE_BACKEND_PROPOSED`  
Claim: `L-17202`  
Issue: #172, negative route

## Purpose

This artifact verifies the auxiliary filter

\[
 G_8=(I-\tfrac18\tau_{(6/5)\log2})
     (I-\tfrac18\tau_{(2/3)\log2})G_0,
\]

where `G_0` is the exact rational ten-notch filter certified by `X-17202`.
The new factors annihilate the shifted trivial zeros `-5/2` and `-9/2`
without introducing a zero anywhere in the shifted nontrivial-zero strip.

The exact rational replay proves

```text
support endpoint                 < 6499/600
critical-line inflation          <= 81/64
critical-line contribution       < 5.0625e-18
surviving trivial tail, x >= 18  < 5.46e-20
complete raw RH bound, x >= 18   < 6e-18
```

This moves a complete raw-prime tail moat into the range where the largest
contributing integer is below `exp(16)<9e6`, making it compatible with a
`10^7` prime-power manifest.

## Files

- `certificate.json` freezes the two annihilators and every declared rational
  constant.
- `verify.py` first runs `X-17202`'s rational verifier, then derives all new
  support, norm, and trivial-tail inequalities using `Fraction` arithmetic.
- `tests/test_mutations.py` checks fail-closed behavior for altered
  annihilators and understated bounds.
- `results/verification.json` records the retained exact-rational replay.
- `recon.py` optionally performs a clearly non-directed two-resolution FFT
  scan with a regenerated complete prime-power manifest.
- `results/recon-fft2p18-2p20-1e7.json` retains the first floating scan.  Its
  two resolutions disagree far above the moat and nominate no support.

## Replay

From this directory:

```powershell
python .\verify.py
python -m unittest discover -s .\tests -v
```

Optional floating reconnaissance near `x=18`:

```powershell
python .\recon.py --cutoff 10000000 --grid-points 65 `
  --fft-sizes 262144,1048576
```

Its cross-resolution comparison is only an error heuristic.  The four shifted
raw sums suffer severe cancellation, so no sampled run is a directed support.

To replay the inherited Arb/FLINT census as well, run from the sibling base
experiment:

```powershell
python ..\X-17202-rational-ten-notch-moat\verify.py --arb
```

## Certification boundary

`X-17203` performs no independent zero calculation.  The first-ten census,
`N(52.9)=10`, and the reciprocal-zero constant are inherited from
`L-17201/X-17202`, currently produced only with Arb/FLINT.  The raw smoothed
explicit-formula normalization is also inherited.  Accordingly both this
artifact and `L-17202` remain `PROPOSED` until those dependencies receive
independent analytic and numerical review.
