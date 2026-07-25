# O-5601 — Executed directed `c=10^11` stream and universal margin

Claim ID: O-5601
Title: The complete 4,118,082,969-term D-0801 prime side at `c=10^11`, `K=1024`
has been evaluated with certified carrier phases, and its leading margin is
positive for every vector
Status: PROPOSED (certified computational fact, pending independent reproduction)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; L-0801; L-4202; L-4203; L-5601; L-5602; T-2801
Scope: the single parameter triple below
Related counterexample candidates: none — this observation *excludes* them

## Parameters

```text
carrier   T = 94184072727073 / 20 = 4709203636353.65   (exact rational)
cutoff    c = 10^11                                    (exact integer)
cells     K = 1024
```

`b = 2 log c / K = 0.049469601607...  <= 1/20`, so the L-4202 small-cell
hypothesis holds.

## Executed enumeration

```text
ordinary primes         4,118,054,813      = pi(10^11)
higher prime powers            28,156
total prime-power terms 4,118,082,969
total amplitude  sum b_q  =  201316.05318381023
```

The prime count agrees exactly with the known value of `pi(10^11)`, and the
higher-prime-power count agrees exactly with an independent enumeration and
with the count recorded in the PR #61/#63 run plan.  Single run, four threads,
316 seconds wall time.

## Certified quantities

All numbers below are outward-rounded; the producer is
`experiments/X-5601-rigorous-carrier-stream/carrier_stream.c` and the checker is
`analyze_stream.py`.

```text
ell_T                        = 4.35171995208831780660455253793
lambda_max(S_K), floating    = 4.351452764865313
lambda_max(S_K), certified <= 4.351452765941646
stream enclosure  sum_d eta_d = 2.8298e-12                       (L-5601)
archimedean gate  B_A        < 1.6565935198410563e-10            (L-4202)
pole gate         ||R_K||_2  < 2.9675898587588259e-17            (L-4203)
```

Hence, by L-5602,

\[
 \boxed{\;
 \lambda_{\min}\!\left(A_K+R_K-S_K\right)
 \;\ge\;2.671859810125\times10^{-4}\;>\;0 .}
\]

Equivalently: **for every** `v \in C^{1024}`, the exact D-0801 explicit-formula
value at these parameters satisfies

\[
 \sum_\rho g_{T,v}(z_\rho)\;\ge\;2.6718\times10^{-4}\,h\,\|v\|^2\;>\;0,
 \qquad h=\frac{\log c}{2\pi K}.
\]

## Fixed-vector branch

The leading eigenvector of the assembled `\hat S_K` was frozen to exact
Gaussian-dyadic coordinates at 48, 64, 80 and 96 bits and re-evaluated directly
against the exact lag coefficients (no eigensolver in the logical path).  At
every freezing depth the exact form is enclosed by

```text
0.00026718705733232194  <  v* (A_K + R_K - S_K) v / ||v||^2  <  0.00026718738867462775
```

with prime-Rayleigh half-width `1.18e-14`.  The interval is dominated by the
archimedean gate `B_A`, not by the stream error.  The 48-bit freeze is already
sufficient; the deeper freezes do not change the enclosure, which is the
expected behaviour when the value is far from zero.

## Cutoff ladder

Same carrier and cell count, certified universal margin
`ell_T - B - lambda_max(S_K)^{upper}`:

| `c` | terms | `lambda_max(S_K)` | certified universal margin |
|---|---|---|---|
| `10^7` | 665,134 | see `results/` | positive |
| `10^8` | 5,762,859 | 4.34507847797128 | `6.6414729e-3` |
| `10^9` | 50,851,223 | see `results/` | positive |
| `10^10` | 455,062,595 | see `results/` | positive |
| `10^11` | 4,118,082,969 | 4.351452764865313 | `2.6718598e-4` |

The margin is shrinking with `c`, roughly by a factor `25` per three decades in
the region examined, but it is positive and comfortably above the correction
gate at every executed cutoff.  Extrapolation is *not* a theorem: nothing here
predicts the margin at `c = 10^{14}`, and nothing here forbids it from
remaining positive forever.

## Interpretation

1. This is a **negative result for the counterexample program at these
   parameters**, and it is a strong one: it excludes the entire
   1024-dimensional family, not one nominated mode.  Previous D-0801
   certificates were fixed-vector statements and left `2K-1` real directions
   untouched.
2. It is *conditional* on the D-0801 / T-2801 explicit-formula dictionary and
   on L-4202 / L-4203, all of which remain `PROPOSED`.  It is not conditional
   on any eigensolver, on any floating discovery vector, or on any library
   transcendental inside the 4.1-billion-term loop.
3. The observed near-cancellation is genuine and remains the most interesting
   feature of the D-0801 route: the complete prime side reproduces
   `\ell_T = 4.35172` to within `6\times10^{-5}` relative.  A cancellation this
   sharp is what makes the family worth studying even though it does not
   produce a counterexample here.
4. `sup_\omega \sigma(\omega) \le 10.3371` for the same data (L-5602), i.e. the
   *infinite* Toeplitz operator built from the same lag coefficients has
   `\lambda_{\max}` more than twice `\ell_T`.  The positivity therefore depends
   essentially on the finite-section structure of the family, not on any
   pointwise smallness of the symbol.

## Reproduction

```bash
cd experiments/X-5601-rigorous-carrier-stream
gcc -O3 -march=native -mfma -std=c11 carrier_stream.c -o carrier_stream \
    -lmpfr -lgmp -lpthread -lm
./carrier_stream --cutoff-power10 11 --cells 1024 --threads 4 \
    --out results/stream-c1e11-k1024.json
python3 analyze_stream.py results/stream-c1e11-k1024.json --grid-log2 24 \
    --out certificates/c1e11-k1024-certificate.json
python3 -m pytest tests/ -q
```

Environment of record: Ubuntu 24.04, Linux 6.18.5, x86-64 with AVX2/AVX512F/FMA,
gcc 13.3.0, MPFR 4.2.1, GMP 6.3, Python 3.11, numpy 2.4.6, mpmath 1.3.0.

## Limitations

- One carrier, one cutoff, one cell count.  Nothing is claimed for other `T`.
- The result rests on the still-unreviewed D-0801 normalization; if that sign
  convention is wrong, the number changes meaning entirely.
- The L-5601 error model is an argued bound, not a machine-checked interval
  evaluation of the kernel.  See its own *Remaining uncertainty* section.
- No statement is made about the zeros of `zeta` beyond what the explicit
  formula already encodes.
