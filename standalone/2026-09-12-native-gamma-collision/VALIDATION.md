# Executed evidence and limits

## Complete native integral campaign

`certificate.py` in this packet produced all three full point records in ordinary
and optimized isolated Python. The commands had the form

```sh
python -I -S -B certificate.py --case 0 --output /tmp/normal0.json --progress
python -I -S -B certificate.py --case 1 --output /tmp/normal1.json --progress
python -I -S -B certificate.py --case 2 --output /tmp/normal2.json --progress
```

The same three commands were also run with `-O`. All six finished successfully.
Each integrates 1,208 gap-free dyadic Taylor cells, degree 72, for I,I_z,I_zz;
all cells, Cauchy remainders, and the remaining compact-support endpoint are
included. Each paired normal/optimized output is byte-identical. These counts
are quadrature coverage, not independent theorem counts.

The exact suffix of `certificate.reconstruct`, after its integral-producing
stage, was evaluated on each trio of completed outputs. This produced identical
`result.json`, SHA256

    12ae6dad411b9e5b8dc843c8fd2e886d2c7da31d937b55c916db8346e746250f.

That assembly is contraction arithmetic on completed source enclosures, not a
new numerical replay. The complete primitive outputs are preserved inside
result.json. The monolithic `check.py --full` commands in README are supplied
for reproduction but were not additionally run in the author session.

The two-variable map satisfies beta <2.319e-5 and Newton displacement <3.882e-42
inside a radius-10^-35 square. The derivative signs are uniform on the square.
The separate full-tube arithmetic gives a uniform Rouché margin >6.48e-40,
negative curvature magnitude >1.30148e-9 and parameter derivative >2.16855e-10.
All these are outward bounds, not floating-point root-finder results.

## Independent bounded controls and accepting boundary

The bounded checker reconstructs 36 exact transition/Chapman--Kolmogorov panels,
90 compensated generator panels, 96 finite-density Laplace evaluations,
27 defect-flux chain-rule panels and 24 synthetic fold panels. Additional mean
and derivative-envelope checks are explicit in the source. Finite controls do
not machine-prove the written all-N martingale or endpoint arguments.

The test suite is intentionally bounded. It runs five methods per mode, one
pristine bounded CLI acceptance and four actual altered-and-resealed bounded
CLI refusals per mode. These are NOT corrupted native integral replays. The
source manifest authenticates all files; mathematical native acceptance via
`--full` additionally requires fresh reconstruction, not only those hashes.
Native integral endpoints were not subjected to an additional expensive
changed-copy full CLI replay in this session. No such test is claimed.

Strict JSON rejects duplicates, nonfinite values and floating numeric aliases.
Canonical comparison distinguishes Boolean/integer values. Main acceptance
checks do not use Python assertions. The primitive intervals are integers in
units 2^-512. Square roots, exp, sin/cos and pi include their analytic remainders.

## Numerical scouting, development, and source reuse

Ordinary mpmath calculations proposed the rational center. Exploratory probes
at u=0,0.1,0.25,0.5,0.75,1 suggested a collision. Those probes are not retained
as a certified trajectory or zero census. Their residuals do not enter the
acceptance calculation; the entire defining integral is freshly enclosed.

An initial fixed-radius degree-80 integral run was interrupted before completion
and is not counted. The final degree-72 adaptive radius uses the center-dependent
simplex strip, with its complete guard and remainder, and all six final runs
completed. No mathematical source was changed in that optimization.

The exact 512-bit primitive `interval.py` is inherited unchanged from #855,
Git blob 36d6341b574fe5a512196bfa0d66fbae897365a6. This is reuse, not an independent
special-function backend. #858's scaled-cell strategy was read; its native
N=5 calculation was not executed or imported as code. Normal/optimized runs
share one implementation and author.

## Delivery scope

The add-only patch and clean archive were checked for exact bytes and replayed
with the bounded checker/test suite in both modes. Full integral campaigns were
not repeated after these packaging roundtrips. Earlier supplied packet bytes
and unrelated sentinel files were preserved in the temporary Git fixture.
That fixture is not a full Riemann checkout.

No native Windows run, complete repository validator, remote CI, Lean build,
parent certificate campaign, actual xi zero computation, global zero count,
large-order quadrature solve, uniform defect gain, or independent mathematical
acceptance is claimed. The local tube does not identify the pair back to #858's
u=0 disk and says nothing about other roots at the same stage.
