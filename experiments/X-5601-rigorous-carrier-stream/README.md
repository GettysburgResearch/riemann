# X-5601 — Rigorous complete carrier stream and universal cell certificate

Experiment ID: `X-5601`
Agent: `opus5-01`
Issue: #55 (also #28)
Branch: `claude/riemann-counterexample-pipeline-io8s2k`
Date: 2026-07-25
Status: executed; results certified subject to the D-0801 normalization

## Research question

The Issue #55 hand-off reduced the D-0801 counterexample route to one concrete
object: *evaluate the complete `4,118,082,969`-term prime side at `c = 10^11`,
`K = 1024`, with carrier phases that carry a bound.*  Two further questions were
open: whether the phases used by the existing discovery streams were good enough
to support any claim at that scale, and whether the resulting certificate could
be made to cover the whole cell family instead of one nominated vector.

All three are answered here.

## What was produced

| artifact | what it is |
|---|---|
| `carrier_stream.c` | complete prime-power lag accumulator with the L-5601 exact-integer phase decomposition; 4.1e9 terms in 316 s on four cores |
| `reference_stream.py` | independent mpmath oracle, no shared code path |
| `analyze_stream.py` | checker: universal `lambda_max` bound (L-5602), L-4202/L-4203 gate, dyadic freeze, exact fixed-vector enclosure |
| `verify_dictionary.py` | end-to-end numerical check of the explicit-formula dictionary against genuine zeta zeros (T-5601) |
| `results/stream-c1e*.json` | the streams themselves, lag coefficients as exact double-double pairs in hex |
| `certificates/*.json` | the certified conclusions |
| `tests/test_stream.py` | 15 fail-closed adversarial tests |

## Headline result

At `T = 94184072727073/20`, `c = 10^11`, `K = 1024`:

```text
ordinary primes            4,118,054,813   = pi(10^11)
higher prime powers               28,156
total terms                4,118,082,969

ell_T                            4.35171995208831780660455253793
lambda_max(S_K) certified <=     4.351452765941646
archimedean gate B_A      <      1.6565935198410563e-10      (L-4202)
pole gate ||R_K||_2       <      2.9675898587588259e-17      (L-4203)
stream enclosure sum_d eta_d =   2.8298e-12                  (L-5601)

lambda_min(A_K + R_K - S_K)  >=  2.671859810125e-4   > 0
```

The last line holds for **every** `v` in `C^1024`, so the entire cell is
excluded as a counterexample source, not merely the nominated mode.  The
fixed-vector branch (leading eigenvector, frozen to exact 48/64/80/96-bit
Gaussian dyadics and re-evaluated against the exact lag coefficients) gives

```text
0.00026718705733232194 < v*(A_K + R_K - S_K)v / ||v||^2 < 0.00026718738867462775
```

## Why the earlier phases were not enough

`np.remainder(carrier * np.log(q.astype(np.longdouble)), TWO_PI_LD)` leaves an
absolute phase error of order `1e-5` radians at `T ~ 4.7e12`.  With total
amplitude `sum_q Lambda(q)/(pi sqrt q) ~ 2.0e5` that allows the prime Rayleigh
value to move by `~2`, against a margin of `2.7e-4`.  Merging the 50 committed
discovery shards and comparing lag by lag against this stream gives

```text
max_d |z_d(longdouble) - z_d(directed)|  =  0.00220063
sum_d |z_d(longdouble) - z_d(directed)|  =  0.355147        (margin: 2.67e-4)
```

while the shard *enumeration* is confirmed exactly correct (contiguous coverage
`[2, 100000000001)`, identical prime and prime-power counts).  See `R-5601`.

## Validation performed

1. **Independent oracle.**  `reference_stream.py` recomputes the lag
   coefficients with mpmath at 60 decimal digits, its own prime enumeration and
   direct evaluation of `log`, `sin`, `cos` at working precision.  Agreement at
   `c = 10^3 .. 10^6`, `K = 8 .. 1024`: `< 6e-20`, against a model bound of
   `~1e-15` at those cutoffs.
2. **Independent argument reduction.**  The producer was rebuilt with
   `JBITS = 14`, `TRIGBITS = 10` (different mantissa anchors, different residual
   `z`, different trigonometric anchors) and re-run on the full `c = 10^11`
   target with a different thread count, so the accumulation order also differs:

   ```text
   max_d |z_d(16/12) - z_d(14/10)| = 8.312e-20
   sum_d |z_d(16/12) - z_d(14/10)| = 2.287e-17     (model bound 2.83e-12)
   certified universal margin: identical to 15 digits
   ```
3. **Enumeration.**  Prime counts match `pi(10^k)` exactly for
   `k = 3,4,5,6,7,8,9,10,11`; higher prime powers match an independent
   enumeration.
4. **Explicit-formula dictionary.**  `verify_dictionary.py` evaluates
   `A + R - S` from the repository's compact formulas and, independently, sums
   `g_{T,v}` over genuine nontrivial zeros from `mpmath.zetazero` plus a
   Riemann-von Mangoldt density tail.  Two parameter sets, with the prime side
   of *opposite sign* in the two cases:

   | `c` | `K` | carrier | `A+R-S` | `sum over zeros` | rel. diff |
   |---|---|---|---|---|---|
   | 30 | 4 | `gamma_1 = 14.1347...` | `0.030686181992` | `0.030684023005` | `7.0e-5` |
   | 50 | 3 | `gamma_3 = 25.0108...` | `0.051644985855` | `0.051648675471` | `7.1e-5` |

   The residual is consistent with the density-tail approximation and shrinks
   as more zeros are used (`9.2e-5` at 120 zeros, `7.0e-5` at 400).
5. **Checker fail-closure.**  The Gram-factor bound returns "unresolved" when
   the trial threshold is below the true `lambda_max`; the symbol bound is
   tested to dominate the true `lambda_max` on random data.

## Cutoff ladder (same `T`, same `K = 1024`)

| `c` | terms | `lambda_max(S_K)` | certified universal margin |
|---|---|---|---|
| `10^7` | 665,134 | 4.324221453110360 | `2.74985e-2` |
| `10^8` | 5,762,859 | 4.345078477971280 | `6.64147e-3` |
| `10^9` | 50,851,223 | 4.349371237214889 | `2.34871e-3` |
| `10^10` | 455,062,595 | 4.351114054639547 | `6.05896e-4` |
| `10^11` | 4,118,082,969 | 4.351452764865313 | `2.67186e-4` |

The margin shrinks with `c` but stays positive and stays far above the
`1.66e-10` correction gate.  **This is a finite ladder, not a limit theorem.**

## Two further experiments run in this session

### Carrier landscape (`O-5602`)

256 complete directed streams at `c = 10^8`, `K = 1024`, carriers
`T_m = (94184072727073 + 4m)/20` (step `0.2`, about one per mean zero spacing):

```text
margin_min   0.0066414741   at m = 0, the Issue #42/#44 carrier
margin_max   0.3082187205
margin_mean  0.1091097185
margin_std   0.0908192719
```

A factor-46 spread, with the tuned carrier `16x` below the mean.  `ell_T` is
constant to `3e-14` over the window, so all of it is `lambda_max(S_K)`.
Per-carrier values are nominations; the extremum was re-certified.

### The Nyquist threshold, tested directly (`C-5601`)

`Delta = log(c)/2pi` is the density of zeros the family can place; `ell_T` is the
density of zeta zeros to be cancelled.  The barrier is at `Delta = ell_T`, i.e.
`c = T/(2 pi)`.  Choosing `T = 62831853071` puts that threshold at `c = 10^10`,
so the reachable ladder straddles it:

| `c` | `Delta - ell_T` | certified margin | factor |
|---|---|---|---|
| `10^7`  | `-1.099403` | `3.87378e-1` | — |
| `10^8`  | `-0.732936` | `1.93912e-1` | 2.0 |
| `10^9`  | `-0.366468` | `1.21071e-1` | 1.6 |
| `10^10` | `+0.000000` | `3.55470e-2` | 3.4 |
| `10^11` | `+0.366468` | `5.29784e-4` | **67** |

The margin collapses by a factor of 67 in the decade that crosses the barrier,
after falling by factors of 2.0, 1.6, 3.4 below it.  Every point is certified
positive with `b <= 1/20` verified.  Note the target of Issue #55 sits at
`c = 10^11` with `T/(2 pi) = 7.49e11`, i.e. **a factor 7.5 below its own
threshold** — the positive margin found there is what the counting argument
predicts.

## Build and run

```bash
gcc -O3 -march=native -mfma -std=c11 carrier_stream.c -o carrier_stream \
    -lmpfr -lgmp -lpthread -lm
gcc -O3 -march=native -mfma -std=c11 -DJBITS=14 -DTRIGBITS=10 \
    carrier_stream.c -o carrier_stream_alt -lmpfr -lgmp -lpthread -lm

./carrier_stream --cutoff-power10 11 --cells 1024 --threads 4 \
    --out results/stream-c1e11-k1024.json          # ~5 min on 4 cores
python3 analyze_stream.py results/stream-c1e11-k1024.json --grid-log2 24 \
    --out certificates/c1e11-k1024-certificate.json
python3 verify_dictionary.py --cutoff 30 --cells 4 --nzeros 400 --dps 25 \
    --out certificates/dictionary-check-c30.json   # ~15 min
python3 -m pytest tests/ -q
```

Do **not** build with `-ffast-math`, and do not build for a target without FMA:
the L-5601 error model assumes IEEE-754 binary64 with round-to-nearest-even and
a correctly rounded fused multiply-add.

## Environment of record

Ubuntu 24.04, Linux 6.18.5, x86-64 (AVX2, AVX512F, FMA), 4 threads, 15 GiB RAM;
gcc 13.3.0; MPFR 4.2.1; GMP 6.3.0; Python 3.11; numpy 2.4.6; mpmath 1.3.0.
Producer wall time at `c = 10^11`: 316 s.

## Limitations

- One carrier, one cutoff ladder, one cell count.  No statement about other `T`.
- Conditional on the D-0801 explicit-formula dictionary (`T-2801`, now
  independently reconstructed and numerically confirmed in `T-5601`, but still
  resting on one quoted classical theorem) and on `L-4202` / `L-4203`, which
  remain unreviewed by a second agent.
- The L-5601 error model is an argued per-step bound, not a machine-checked
  interval evaluation of the kernel.  The empirical safety factor is `~1e5`.
- **No counterexample was found and none is claimed.**  A positive value says
  only that this test function detects nothing; it is not evidence for RH.
