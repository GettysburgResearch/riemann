# D16 verification scope

Status: proposed computer-assisted component proof. The numerical predicate is
complete for the stated finite root box, conditional on the analytic enclosure
arguments in PROOF.md. It is not a formal proof or independent referee acceptance.

## Primitive reconstruction

`certify.py --check result.json` reconstructs:

- all 84 degree-120 theta integration cells with 320-bit outward integer
  intervals; normalization and even moments zero through eighteen;
- every one of the four time tails and the complete theta-index tail n>=5;
- the normalized cumulants, all exact dimer coefficients, both rational
  eight-by-eight inverse products (128 entries), and the whole-box row sums;
- the strict root inequality, the complete target-perturbation and positive-
  coupling allowances, and the nonzero eighteenth-moment interval;
- 120 explicitly enumerated spin configurations across four small comparison
  models, 76 full moment comparisons, 72 cumulant comparisons, four exact
  Gibbs covariance derivatives, 27 polynomial derivative panels and one
  complete unit-cumulant comparison list.

The 2^280 configuration space is NOT enumerated. At j=0 its cumulants are
computed by exact independence between components; at j>0 its full-law
continuation is paid by the uniform Gibbs inequalities in the paper.

The new script contains no floating-point arithmetic, special-function oracle,
actual-zero input, or imported moment receipt. `primitive.py` adapts the ICR26
backend rather than providing an independent transcendental implementation.
The extension to moment eighteen has explicit complete remainder bounds.
The polynomial root is not represented by the rounded scouting weights.

## Accepting and adverse commands

The complete accepting commands are

```sh
python -I -S -B certify.py --check result.json
python -I -S -B -O certify.py --check result.json
```

The producer-only command `--emit` deliberately does not authenticate the
published file inventory. It is not counted as an accepting replay.

Each of the two rejection partitions starts with a complete pristine CLI
reconstruction. The nine changed-packet cases are wrong moment scope, wrong
numerical endpoint, duplicate JSON key, float alias, unexpected file, changed
theta primitive, changed pair cumulant primitive, unsealed proof, and a
symlinked proof. The primitive mutations are resealed before execution and
must fail the reconstructed mathematics, not merely their hashes. Parser and
inventory cases have separately stated, narrower coverage.

```sh
python -I -S -B test_rejections.py --part 1
python -I -S -B test_rejections.py --part 2
python -I -S -B test_rejections.py --part 1 --optimized
python -I -S -B test_rejections.py --part 2 --optimized
```

Symlink creation failures are explicitly reported as skips on hosts that do
not permit them. They are not reported as successful refusals. The external
DELIVERY.json records the actual host execution, whether any skips occurred,
checksums, and the byte comparisons after ZIP extraction and Git-patch application.
No accepting predicate relies on Python assert statements.

## Exploration excluded from evidence

NumPy/SciPy bounded searches proposed the five-dimer ansatz. A rational-coordinate
selection and high-precision mpmath Newton iteration proposed the exact rational
centers. Ordinary quadrature proposed targets only for those scouts. None of
their outputs is a source premise of the accepting calculation. The final
native integration is freshly reconstructed from the defining theta series.

Unsuccessful trials included one unequal dimer, variable dimer coupling, some
larger pair banks, small bridges between dimers, and attempts at higher moments.
They do not establish infeasibility. No certified eighteenth-moment solution
or global continuation path was obtained.

One initial isolated-interpreter invocation failed because the new file had
not inserted its own directory before importing its local primitive module.
The import was made explicit and the subsequent reconstructed certificate
succeeded. That setup failure is not counted as mathematical verification.

## External and repository boundaries

Weighted Lee--Yang for the connected extension is an explicit classical import.
The disconnected five-dimer product has a separate elementary real-zero proof.
Newman--Wu's parsed PDF statement at equation (21) was read; a web page-image
request failed with a cache miss. No image, diagram or table was a proof input.

No predecessor numerical campaign was rerun as part of this packet. The
ICR26 source code copy was authenticated to its known Git blob before adaptation.
The live #869 graft text was read to avoid claiming its already proved initial
motion as a new result. Other current PR descriptions were orientation only.

The optional use of #880's calibrated infinite completion is conditional on
that earlier proposed theorem and not required for D16-1--3. No new infinite
root or completed whole-law theta identification is numerically evaluated.

No whole-repository checkout/build, Lean/kernel proof, remote CI, actual-zeta
zero computation, independent review, external novelty, or RH proof is claimed.
