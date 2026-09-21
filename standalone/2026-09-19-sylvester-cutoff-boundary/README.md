# SBC26 — execute and correct the Sylvester-inspired boundary programme

**Status: proposed component proofs and exact finite computations, not an RH
proof.** This replaces the first five untested notes on draft PR #903 and
continues #848 without changing its accepted status. Date: 19 September 2026.
The correction history is explicit in [CORRECTIONS.md](CORRECTIONS.md).

## Results, not another architectural sketch

**The native boundary operator is now explicit.** We derive its rough-integer
incidence kernel, its full physical Gram matrix and mean restoration, and an
exact adapter to the SAME capped-completion harmonic Q used in PCR26/RCB26.
The previous error-collision description was misleading: e*e is zero below
(Y+1)^2. The operator actually reconstructing that annulus is g*e.

**The naive least-prime partition fails on the actual source.** Its block
containing all primes p>Y equals -[pi(x)-pi(Y)] for Y<=x<=2Y. Thus its energy
is at least asymptotic to

```text
(3/2 - 2 log 2) Y/(log Y)^2.
```

This is an all-scale obstruction to bounding that isolated block by a
subpower positive majorant, using the classical PNT, not RH. It does not
refute the signed Newton target or RCB26's DIFFERENT rough-parity partition.
We also bound the sum of individual large-prime self-energies by
E_Y sum_(Y<p<(Y+1)^2)1/p = (log 2+o(1))E_Y. Their cross-interactions are not
bounded by that diagonal estimate.

**The covariance calculation is executed.** Complete native physical annuli
at Y=3,15,63,255 are reproduced from boundary atoms and independently checked
against both divisor-first and product-first Newton reconstruction. Actual
harmonic distinct-product and rough-core covariances are computed at Y=3,7,15;
the exact harmonic-source adapter is checked through the full next prefix at
Y=3,7,15,63,255. All centered products beyond the observation cutoff are kept.

At Y=255, the full physical annular energy is 0.179852003503...:

| Partition / quantity | Value, descriptive only |
|---|---:|
| Coarse least-prime sum of row energies | 19.475518192540... |
| Its merged p>Y channel energy | 10.644637712762... |
| Individual p>Y self-energy sum | 0.705515697234... |
| Inherited NSR26 P=210 causal-bank row energy | 0.219222763075... |
| Actual completed A at B=65535 | 1.587579815075... |

A row-energy diagonal is NOT itself an upper bound. The complete signed
Grams and mean vectors are regenerated as `reports/boundary_results.json`,
with directed rational endpoints, not floating-point certificates. The
committed [RESULT_DIGESTS.json](RESULT_DIGESTS.json) authenticates their exact
canonical bytes. P=210
reproduces the predecessor's improvement; it is not a new claim of ours.

**The L-family connection is now mathematical and executable.** We derive
the degree-two local cutoff boundary for reciprocal elliptic L-coefficients.
At a good inert CM prime ell, a_ell=0 makes the boundary an ell^2-window,
not the zeta ell-window. A bounded three-good-prime fixture verifies this
identity and the general Newton identity without pretending to model bad
Euler factors or the full L-function.

We also reproduce the paper's three explicit local cases (q,p)=(13,17),
(13,107),(31,17) in exact F_(p^6) arithmetic: Fermat lift, lambda-isogeny,
Frobenius in two ways, nonzero kernel multiple and its sign. Both integral
cubic projectors are checked at orders 3,6,9,27,81. These are local and finite
checks, not independent verification of the global CM/Gross--Zagier proof.
Rank-one central deflation and its off-line/rank-three controls are explicit.

## Read and replay

Read [PROOF_NOTES.md](PROOF_NOTES.md) for the RH-side mathematics,
[LFAMILY_NOTE.md](LFAMILY_NOTE.md) for the distinct #738 extension, then
[RESEARCH_TARGET.md](RESEARCH_TARGET.md) for the revised direction.
[SOURCE_NOTE.md](SOURCE_NOTE.md) locks imported sources and reading scope.
[VALIDATION.md](VALIDATION.md) distinguishes executed tests from unrun work.

Python standard library only; tested with Python 3.13.5. From this directory:

```sh
python -I -S -B verify_receipts.py --write reports
python -I -S -B boundary.py --check reports/boundary_results.json
python -I -S -B harmonic_adapter.py --check reports/harmonic_results.json
python -I -S -B lfamily.py --check reports/lfamily_results.json
python -I -S -B test_packet.py
```

Repeat with `-O` as well. The receipt verifier checks all three full reports
before writing anything. Large generated JSON is not duplicated in Git;
its exact contents are reproducible from this packet, and included in the
chat archive. For each individual producer, `--write PATH` regenerates a report;
`--check PATH` recomputes and refuses a changed report. There is no
network access, optional numerical library, or remote computation in replay.

## What this changes

The promising continuation is a signed prime/composite compensation estimate
inside the existing harmonic source, not a separate positive least-prime
budget. This pass constructs and tests that source interface, eliminates a
specific native obstruction to our earlier plan, and supplies a usable CM
family reference. It does NOT prove the remaining uniform covariance gain.
No canonical theorem status, main-branch file, workflow or formal trust base
is changed. No priority claim is made for elementary convolution algebra.
