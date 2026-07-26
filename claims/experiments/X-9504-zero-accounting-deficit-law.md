# X-9504 — Scaling of the zero-accounting deficit

Claim ID: X-9504
Title: The `L-9507` deficit is tail-governed; both search knobs are bounded
Status: EMPIRICAL
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: L-9506, L-9507, X-9503
Scope: Issue #95; the arithmetic-progression screw route as a whole
Related counterexample candidates: none. **No counterexample is claimed.**

## Research question

`L-9506` showed that driving `n` upward drives `lambda_min(H^(n)(h))` to zero
and therefore cannot decide anything.  `L-9507` replaced the target with the
scale-free ratio `rho_Gamma = lambda_max(Z_Gamma, H)`, which RH forces below
`1`, and `X-9503` measured `rho = 0.9934` at the `X-9502` parameters.

The route can only produce a witness if the deficit `1 - rho_Gamma` can be
pushed below the width of a directed enclosure of the two sides.  So:

**how does the deficit scale in `T`, `n` and `h`, and what would the route
need in order to close?**

## Code, command, environment

```text
experiments/screw_deficit_law.py
  (imports screw_lib.py and screw_audit_and_ratio.py from X-9503)
```

```bash
python3 experiments/screw_deficit_law.py \
    --zeros    experiments/results/X-9503-screw-audit-ratio/zeros1000.json \
    --json-out experiments/results/X-9504-screw-deficit-law/deficit.json
```

```text
OS / arch          Linux 6.18.5, x86_64, glibc 2.39
interpreter        CPython 3.11.15
third-party libs   NONE (no numpy, mpmath, gmpy2, python-flint, GMP or MPFR)
numerical backend  IEEE binary64, round-to-nearest, no directed rounding
prime table        prime powers to e^16 = 8886112 (595341 primes, 595877 powers)
zero ordinates     649 binary64 ordinates below 1000, from X-9503
runtime            ~90 s
```

Feasibility constraint throughout: evaluating `Psi(nh)` needs prime powers to
`e^{nh}`, so every `(n,h)` pair obeys `n h <= 16`.

## Results

### A. The deficit is governed by the zero tail

At the `X-9502` proof-replay parameters `n=53`, `h=log(2)/3`, with
`S_T = sum_{|gamma|>T} gamma^{-2}` estimated from the Riemann-von Mangoldt
density:

```text
     T  #zeros           rho      deficit         S_T  deficit/S_T
   100      29   0.958050343   4.1950e-02   1.199e-02        3.498
   200      79   0.980248810   1.9751e-02   7.099e-03        2.782
   300     138   0.984294685   1.5705e-02   5.163e-03        3.042
   500     269   0.988417038   1.1583e-02   3.423e-03        3.384
   700     414   0.991049118   8.9509e-03   2.598e-03        3.445
  1000     649   0.993360504   6.6395e-03   1.932e-03        3.436
```

The ratio `deficit / S_T` is flat: mean `3.434`, spread `0.438`, over
`T in [600,1000]`.  So empirically

\[
 1-\rho_\Gamma \;\approx\; K\,S_T,
 \qquad K\approx3.43 .
\tag{X-9504.1}
\]

**The deficit is the unaccounted zero tail, nothing else.**  This is the
expected shape — the tail is exactly what `L-9507(a)` discards — but the
constant being flat means no cleverness in choosing `b` recovers the tail.

### B. Increasing `n` helps, slowly, and `n` is exponentially capped

At `h=log(2)/3`, `T=1000`:

```text
   n           rho      deficit
   8   0.982199475   1.7801e-02
  16   0.987134814   1.2865e-02
  32   0.991064018   8.9360e-03
  53   0.993360504   6.6395e-03
  68   0.994859421   5.1406e-03
```

A log-log fit over `8 <= n <= 68` gives

\[
 1-\rho \;\approx\; 0.0651\,n^{-0.582},
\tag{X-9504.2}
\]

with residual spread `0.165` in the log.  The deficit does decrease with `n` —
consistent with the captured and tail atoms being separable in the limit — but
only as a small power.

The binding constraint is that the prime-side cutoff is `e^{nh}`.  At
`h=log(2)/3` a prime table with `10^9` entries caps `n` at about `90`.

### C. `h` matters, and `log(2)/3` is not the right choice

Scanning `h` at `n=40`, `T=1000` (so `h <= 0.4`), the deficit is otherwise flat
near `8e-03`, but has a distinct minimum at the lowest-zero resonance

\[
 h_\star=\frac{\pi}{\gamma_1}=0.2222614\ldots
\]

```text
         h        rho        deficit    note
    0.1500   0.992116     7.8841e-03
    0.1900   0.991234     8.7657e-03
    0.2310   0.992531     7.4694e-03   h = log(2)/3   (the X-9502 choice)
    0.2214   0.995863     4.1371e-03   best in a fine scan
    0.2223   0.995376     4.6237e-03   h = pi/gamma_1
    0.2900   0.991335     8.6647e-03
```

`h_star` maximizes `sin^2(gamma_1 h/2)`, the weight with which the lowest zero
enters `Z_Gamma` (L-9507.2); `gamma_1` carries by far the largest `gamma^{-2}`
weight.  The corresponding resonances for higher zeros do **not** help:

```text
  pi/gamma_1 = 0.222261   deficit 4.6237e-03
  pi/gamma_2 = 0.149443   deficit 7.8563e-03
  pi/gamma_3 = 0.125609   deficit 8.4294e-03
  pi/gamma_4 = 0.103257   deficit 8.6714e-03
```

so the effect is specifically about `gamma_1`.  Choosing `h` near `h_star`
rather than `log(2)/3` improves the deficit by a factor `~1.6-1.8`.

**`log(2)/3` was selected in `X-9502` because it makes the prime-power
threshold the exact integer predicate `q^3 <= 2^k`.**  That is a real
advantage for exact replay, but it is an arithmetic convenience, not a
spectral one, and it costs most of the available factor.

Note also that `Psi(h)` does *not* track the deficit — `Psi` is slightly
*smaller* at `pi/gamma_1` than at `pi/gamma_2` — so "maximize the total mass
`2 Psi(h)`" is **not** the right heuristic for choosing `h`.  This refutes the
first guess I made about the mechanism.

### D. What the route would need

Inverting (X-9504.1) and (X-9504.2):

```text
target deficit   required T   certified zeros below T
        1e-06     1.730e+07                 3.808e+07
        1e-09     2.527e+10                 8.491e+10
        1e-12     3.311e+13                 1.491e+14

target deficit   required n   prime cutoff e^{n h}, h = log(2)/3
        1e-06     1.871e+08                  e^(4.3e+07)
        1e-09     2.675e+13                  e^(6.2e+12)
        1e-12     3.824e+18                  e^(8.8e+17)
```

Both knobs are out of reach, and the factor `~1.8` available from `h` changes
none of these numbers by more than a factor of two.

## Interpretation

Combining with `L-9506`, the arithmetic-progression screw route is bounded on
both sides:

- **the `n` knob** drives `lambda_min -> 0` (proved, `L-9506`), so it cannot
  produce a witness by shrinkage; and in the ratio formulation it improves the
  deficit only as `n^{-0.58}` while costing `e^{nh}` in prime-side work;
- **the `T` knob** improves the deficit only as fast as the zero tail
  `S_T ~ (log T)/(pi T)`, requiring of order `10^{14}` certified zero bins to
  reach a plausible certificate width.

I therefore do not expect a finite RH witness from arithmetic-progression screw
filters, at `h = log(2)/3` or at any other single step, with any resource this
project can bring to bear.  That is a bound on **this route**, not on `L-9504`,
`L-9505` or `L-9507`, which remain correct, and not on the screw function as a
source of witnesses generally.

## Limitations

- Everything is binary64 round-to-nearest.  No directed rounding, no interval
  arithmetic, no certified enclosure.
- `S_T` is the Riemann-von Mangoldt density estimate, not a proved tail bound.
  It is used for scaling and extrapolation only.
- (X-9504.1) is fitted over `T in [100,1000]` and (X-9504.2) over
  `n in [8,68]`.  Extrapolating them by ten or more orders of magnitude is a
  **heuristic** and is presented as such; the qualitative conclusion (both
  knobs are far out of reach) is robust to a large error in either exponent,
  but the tabulated `T` and `n` values are not to be quoted as estimates.
- The `h` scan is at `n=40`, `T=1000` only, on a grid of `40` points plus a
  fine window.  The fine structure of `rho` in `h` at the `1e-3` level may be
  affected by the conditioning of `H` (`~6e4`); the factor-`1.8` gap between
  `log(2)/3` and `pi/gamma_1` is well above that level, the point-to-point
  jitter is not.
- The zero ordinates are floating sign changes, not certified bins.
- No search over *non*-arithmetic node sets was performed.  The bound applies
  to the arithmetic-progression cone of `L-9504` only.

## Associated issues and claims

Issue #95; PR #98.  Claims: `L-9506`, `L-9507`, `X-9503` (all used),
`X-9502` (the route this bounds), `L-9504`, `L-9505` (unaffected).

## Suggested next attack

The screw geometry is not exhausted; the *arithmetic-progression* cone is.
Two directions that escape the bound above:

1. **Non-arithmetic nodes.**  `L-9504`'s cone is the equally-spaced one, and
   its Gram vectors `u_gamma(h)` are geometric progressions in `e^{i gamma h}`.
   A general node set `t_1,...,t_m` gives Gram vectors
   `(e^{i gamma t_j})_j`, i.e. arbitrary frequency sampling, and the deficit
   analysis above does not apply.  `L-9501`'s three-value determinant and
   `L-9502`'s Gaussian kernel already live outside the arithmetic cone.
2. **Multi-step combinations.**  A witness may use several steps `h_1,...,h_r`
   simultaneously; the tail contributions decorrelate across steps while the
   low-zero contributions can be made to add.  Whether that beats `K S_T` is
   open and is cheap to test with the existing code.
