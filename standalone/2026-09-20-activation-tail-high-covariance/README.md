# ATC29 — pay the activation tail; preserve compulsory high-mode cancellation

**Proposed component mathematics; independent mathematical review required.**
**The full high-composite bound and RH remain open.**
20 September 2026. Continuation of strategy #902 on the existing draft #904.
Reading parent: `879497b4f11be2618c448efc1fa93f69b4022e4c`.

## What changed

NCG28 bounds a growing composite window in terms of the previous actual energy
`F_Y=sum_(k<=Y)(sum_(n<=k)mu(n)/n)^2`, but changing that window with physical time
creates a nonlocal future-activation correction. We now prove the complete bound

```
||activation correction||_2^2
 <= 2^34 C_0 H_L^3 F_Y^(4/3) Y^(-1/11),
```

where c is the same capped native completion, L<=2Y, and C_0 is NCG28's finite
absolute Euler constant. Every dyadic block and the whole future are included.
A periodic zero-mean calculation supplies the additional inverse power needed;
we do not subtract two large harmonic bounds independently.

The instantaneous low sum therefore retains its `O(H_Y^5 F_Y^(4/3))` budget.
The remaining high target can be stated using only modes currently above the
cutoff, with the correction paid separately. **This does not bound that high sum.**

A second result shows why controlling arbitrary high packets independently is
the wrong next step. For primes `3(Y+1)/4<p<=Y`, the ACTUAL native semiprime
packet, on `Y<k<=5Y/4`, is exactly

```
S_Y(k)=[(sum_p 1/p)^2-sum_p 1/p^2]*(H_k-2).
```

It has energy asymptotic to `log(4/3)^4 * Y/[4(log Y)^2]`. Thus NCG28's
any-subset subpower property cannot be extended to all denominators. This is a
native-source result, not a fake-source counterexample.

We further prove the signed covariance of this packet with the OTHER HIGH
composite modes is `-2||S_Y||^2+O_A(Y/(log Y)^A)` for every fixed A. That
asymptotic imports classical quantitative Mertens bounds. Its absolute error is
NOT RH-scale; this is not a new unbounded native energy gain.

## Read first

- [PROOF.md](PROOF.md), Sections 1--3: all-tail bound, source-amplitude input,
  dyadic summation and exact instantaneous/transformed comparison.
- Sections 4--6: generic auxiliary ceilings; exact semiprime packet; necessary
  high/high compensation and its classical-error limitation.
- [SOURCES.md](SOURCES.md): exact predecessor, copied arithmetic, external inputs
  and what was actually read.
- [VALIDATION.md](VALIDATION.md): finite coverage and execution boundaries.

## Reproduce

Standard library only, Python 3.10+:

```sh
python -S -B check.py --check results.json
python -O -S -B check.py --check results.json
python -S -B test_check.py
python -O -S -B test_check.py
```

Canonical result SHA256:
`331e41e255c9ed05ba64185340e1d13811f7577a4f46fd161ea14d0aadfe8a81`.

The optional `--quick` flag selects a DIFFERENT, labeled bounded campaign used
for CLI refusal tests. It is not a replacement for the default receipt. To write
its separate report, use `python -S -B check.py --quick --write quick.json`.
Do not overwrite the canonical default report with a quick report.

`ncg28_primitives.py` is a byte-for-byte, hash-authenticated copy of the previous
checker, used for its source algebra and outward arithmetic. Its historical
module docstring describes the older packet. ATC29 DOES reuse this implementation;
we do not call the copy an independent backend or a fresh run of its old campaign.

## Finite findings

The whole activation-correction energy, including all future blocks, is enclosed
at Y=31,63,95,127. At Y=127 it is approximately `0.0000072886983211`; the
independently summed component-tail envelope is below `0.061635`. The envelope
is deliberately conservative and does not use the huge asymptotic Euler constant
as a numerical certificate.

Small complete spectral panels show the semiprime/other-HIGH covariance is
positive at Y=95. The asymptotic negative sign is therefore not a universal
finite sign law. Three points in each panel also receive full direct high-mode
summation; other cells use exact complementary evaluation after complete native
Newton coefficient checks.

Larger panels compare the semiprime packet with ALL other spectral modes:

| Y | Prime count | Semiprime energy | Twice covariance | Complete Q energy |
|---:|---:|---:|---:|---:|
| 4,095 | 125 | 0.0745136400 | -0.1453849083 | 0.0044725030 |
| 16,383 | 431 | 0.2422071092 | -0.4972115886 | 0.0082811815 |
| 65,535 | 1,491 | 0.7410439746 | -1.5638782741 | 0.0040299836 |

These descriptive decimals come from directed finite enclosures, not a fitted
asymptotic law. At the largest cutoff, the other-mode energy is about
0.8268642831. All terms are needed to recover the small combined energy.
The interval ends at 81,918, NOT at the square-stage endpoint.

## Next mathematical target

Estimate the COMPLETE instantaneous high-composite sum on the full next native
annulus using signed divisor relations. The activation tail is now paid, but
arbitrary high subpackets can be power-sized. A successful bound must explain
compensation, not majorize every packet separately by a subpower quantity.

Do not interpret `O_A(Y/log^A Y)` for every fixed A as `Y^o(1)`. No new zero-free
region, full scale-to-scale gain, external priority, independent review, Lean
verification or accepted RH conclusion is claimed.
