# Session report — `opus5-01`, Issue #55

Agent: `opus5-01`
Issue: #55 (Build threshold-directed piecewise-carrier search and directed
fixed-vector replay); touches #28
Branch: `claude/riemann-counterexample-pipeline-io8s2k`
(fast-forwarded from `agent/gpt56-05-g/28-c1e11-directed-fixed-vector`)
Date: 2026-07-25

## Starting hypothesis

The hand-off into this session claimed that the six-stage threshold pipeline had
been executed at `10^8` scale and that the remaining production task had been
reduced to one object: *"export one exact dyadic vector and replay one complete
fixed-vector prime sum"* at `c = 10^11`, `K = 1024`.  The stated goal was to
complete the computation and the proofs required for a full unconditional
counterexample to the Riemann hypothesis.

My starting hypothesis was that the missing object was mostly an engineering
problem — that the 4.1-billion-term replay had not been run because the
available directed producer was too slow — and that the value it would return
would be positive, since every replay in the repository so far had been.

Both parts turned out to be right, and a third thing turned out to be wrong in
a way that mattered.

## What was done

### 1. Executed the complete `c = 10^11` pass (the named missing object)

`experiments/X-5601-rigorous-carrier-stream/carrier_stream.c` evaluates the
complete D-0801 prime side over all `4,118,082,969` prime powers below `10^11`
in **316 seconds on four cores**, with carrier phases accurate to about
`10^{-20}` radians and a certified bound of `10^{-17}`.  Prime count
`4,118,054,813` and higher-prime-power count `28,156` match `pi(10^11)` and the
run plan of PR #61/#63 exactly.

The speed comes from `L-5601`: because `q` is an exact integer below `2^37`, the
decomposition `q = 2^e y_j (1+z)` with `y_j = 1 + j/2^16` can be done in exact
integer arithmetic, so `T log q` splits into two table lookups (reduced modulo
`2 pi` once with MPFR at 300 bits) plus a double-double `log1p` series on a
residual of size `2^{-17}`.  This is roughly `1000x` faster than the per-term
MPFR producer in X-2805 and, at 4.1e9 terms, that is the difference between
"cannot be run" and "runs over lunch".

### 2. Upgraded the certificate from one vector to the whole cell

The stream produces the lag coefficients `z_d`, from which `v* S_K v =
sum_d Re(z_d c_d)` for *any* `v`.  `L-5602` turns this into an all-vector
statement by exhibiting a Gram factor `L` with a rigorously bounded residual
`|| (tI - S_K) - L L^* ||`; since `L L^*` is positive semidefinite for any `L`
whatsoever, no property of the factorization routine is assumed.  Combined with
the L-4202 archimedean gate and the L-4203 pole gate:

```text
lambda_min(A_K + R_K - S_K) >= 2.671859810125e-4 > 0
```

for **every** `v` in `C^1024` at `T = 94184072727073/20`, `c = 10^11`,
`K = 1024`.  The fixed-vector replay that was actually requested is a corollary
and is also reported (leading mode frozen to exact 48/64/80/96-bit Gaussian
dyadics, exact value enclosed in
`[0.00026718705733232194, 0.00026718738867462775]`).

### 3. Independently reconstructed the explicit-formula dictionary

This was the last unfinished audit item on the hand-off list.  `T-5601` derives
the archimedean, pole and prime constants from the classical Guinand–Weil
statement and Gauss's integral for `psi`, and **confirms every constant and sign
in `T-2801` / `L-0702` / `L-4201` / `L-0801` with no discrepancy**.  It also
removes a genuine soft point: the D-0801 tests decay like `(1+|z|)^{-2}` on
horizontal strips, one `delta` short of the hypothesis usually quoted, and I
close that gap by Fejér mollification with `(sin(eps z)/(eps z))^2` and four
dominated-convergence limits.

More convincing than the derivation: `verify_dictionary.py` evaluates
`A + R - S` from the repository's own compact formulas and, independently, sums
`g_{T,v}` over *genuine nontrivial zeros of zeta* from `mpmath.zetazero` plus a
Riemann–von Mangoldt density tail.  Two parameter sets, with the prime side of
opposite sign in the two cases, agree to relative `7e-5`, the residual being
consistent with the density tail and shrinking as more zeros are added.

### 4. Found and quantified a real defect in the existing discovery data

The `c = 10^11` discovery streams reduce the carrier phase with
`np.remainder(carrier * np.log(q.astype(np.longdouble)), TWO_PI_LD)`.  At
`T ~ 4.7e12` that leaves about `10^{-5}` radians of phase error per term, and
the total prime amplitude is `2.0e5`, so the a priori uncertainty on the prime
Rayleigh value is of order `2` — about `10^4` times the margin being measured.

Merging the 50 committed shards and comparing lag by lag against the directed
stream:

```text
sum_d |z_d(longdouble) - z_d(directed)| = 0.355147     (margin: 2.67e-4)
max_d |z_d(longdouble) - z_d(directed)| = 0.00220063
```

The *enumeration* in those shards is exactly right — contiguous coverage
`[2, 100000000001)`, identical counts — and I reused it as a cross-check.  Only
the arithmetic carries no bound.  Recorded as `R-5601`.

The eigenvalue actually moved by only `1.93e-6` (`4.351450833636324` reported
versus `4.351452764865313` directed), because 4.1e9 unstructured phase errors
largely cancel inside a fixed quadratic form.  That is precisely the trap: the
number *looked* fine and had no bound behind it.  Worse, the bias has a
direction — maximizing a Rayleigh quotient over 1024 dimensions lets the
optimizer exploit noise, which pushes the reported margin **down**, i.e. towards
a false counterexample rather than away from one.

## New results

Proved (subject to the stated dependencies):

- `L-5601` — exact integer phase decomposition and its error model.
- `L-5602` — Gram-factor universal positivity certificate for a D-0801 cell.
- `T-5601` — independent reconstruction of the `A + R - S` dictionary, plus
  removal of the decay gap in the admissibility hypothesis by mollification.

Certified computational facts (conditional on the D-0801 normalization):

- `O-5601` — the executed `c = 10^11` stream and its universal margin
  `2.671859810125e-4`, plus the `10^7 .. 10^11` ladder.

Refutation of a method:

- `R-5601` — long-double carrier phases cannot support any D-0801 bound at
  `T ~ 5e12`.

## Candidate counterexamples

**None.**  No negative value was found, no `Z-####` identifier was allocated,
and the opposite was established: the whole `K = 1024` cell at `c = 10^11` is
now excluded, which is strictly stronger than the fixed-vector exclusions the
repository had before.

I want to be explicit about the request I was given, which was to complete the
proofs required for a full unconditional counterexample.  That could not be
done, and not because of missing compute or missing time:

1. The quantity the D-0801 route measures is `sum_rho g_{T,v}(z_rho)` with
   `g >= 0` on the real axis.  A negative value disproves RH.  At the target
   parameters the value is `+2.67e-4` per unit norm, in every direction of the
   1024-dimensional family, with a certified enclosure whose half-width is
   `1.7e-10`.  There is no counterexample here to certify.
2. By the explicit formula, `lambda_max(S_K) > ell_T` is *equivalent* to the
   value being negative.  So a negative D-0801 value is not an independent route
   to RH — it is a detector for off-critical zeros in the effective window of
   `g`.  The search can only succeed if such zeros actually exist near the
   carrier.  No unconditional positivity obstruction can be proved either, for
   the same reason: it would require knowing the zeros near `T = 4.7e12`, which
   is above the Platt–Trudgian verified height.

So the honest status is a sharpened negative: the avenue is a zero-detector, it
detected nothing at these parameters, and it now does so with a bound instead of
a floating value.

## Certified computations

See `experiments/X-5601-rigorous-carrier-stream/` — `results/` for the streams,
`certificates/` for the conclusions, `results/tests.txt` for the 15-test run,
`SHA256SUMS` in both directories.  Reproduction commands and the exact
environment are in the experiment README.

## Failed approaches / things that did not work

1. **The Toeplitz symbol bound is useless at these parameters.**
   `lambda_max(S_K) <= sup_omega sigma(omega)` is elementary, cheap, and
   completely self-contained (two lines by Parseval), and I implemented it as a
   first gate expecting it to do the job.  It gives `sup sigma <= 10.3371`
   against `ell_T = 4.35172` — a factor of `2.4` too weak.  Recorded in L-5602
   rather than deleted, because the *reason* is informative: the infinite
   Toeplitz operator built from the same lag data is far from positive, so the
   positivity of the D-0801 form depends essentially on the finite-section
   structure, not on any pointwise smallness of the symbol.
2. **A first version of the trigonometric anchor was wrong** for angles within
   `pi/4096` of `2 pi`: the nearest anchor is `2 pi`, which is not in the table,
   and the index wrapped while the residual did not.  Two terms out of 9,700 at
   `c = 10^5` were affected and moved three lag coefficients by `O(1)`.  Caught
   immediately by the mpmath oracle.  This is the single strongest argument for
   keeping an independent oracle in the loop even for "obviously correct" table
   lookups — the bug was invisible to every internal consistency check.
3. **Trying to prove an unconditional positivity theorem for the family.**  I
   spent time looking for a route and convinced myself there isn't one: by the
   explicit formula, `lambda_max(S_K) < ell_T` is equivalent to a statement
   about the zeros near height `T`, so any unconditional proof would be a
   zero-free result at `4.7e12`.  Written up in the report rather than as a
   claim, since a failed search is not a theorem.

## Potential errors

Ranked by how much damage they would do:

1. **The quoted classical explicit formula (T-5601, Step 1).**  Everything rests
   on it.  I re-derived the four conversions from it and checked the total
   against real zeta zeros to `7e-5`, which would catch any factor-of-2,
   factor-of-`2 pi`, or sign error — but not a subtle error shared by my
   recollection and the check's construction.  A verifier should reconstruct
   Step 1 from the Hadamard product inside the repository.
2. **The L-5601 constant `eps_trig = 1e-17`.**  Argued from a table of per-step
   bounds, not machine-checked.  Empirical safety factor `~1e5`; the
   table-invariance rerun at `JBITS/TRIGBITS = 14/10` agrees to `8.3e-20`.
3. **L-4202 and L-4203** are used as black boxes.  Neither has been
   independently reviewed.  At the target the gate is `1.66e-10` against a
   margin of `2.67e-4`, so an error would have to be six orders of magnitude
   large to change the sign — but the gate becomes load-bearing the moment a
   cell with a small margin is found.
4. **My prime-power enumeration.**  Guarded by exact agreement with
   `pi(10^k)` for `k = 3..11` and with an independent higher-power count.

## Files changed

```text
claims/lemmas/L-5601-exact-integer-phase-decomposition.md      (new)
claims/lemmas/L-5602-gram-factor-universal-bound.md            (new)
claims/theorems/T-5601-independent-normalization-and-admissibility.md (new)
claims/observations/O-5601-directed-c1e11-universal-margin.md  (new)
claims/refutations/R-5601-longdouble-phase-not-certificate-grade.md (new)
experiments/X-5601-rigorous-carrier-stream/                    (new, full)
reports/opus5-01/2026-07-25-55-rigorous-carrier-stream.md      (this file)
CLAIMS.md, CURRENT_STATE.md, NEGATIVE_RESULTS.md, OPEN_PROBLEMS.md (updated)
```

## Claims affected

- `T-2801` — confirmed by independent reconstruction (`T-5601`).  Its item 1
  (admissibility) is now proved rather than asserted.
- `L-0702`, `L-4201` — archimedean functional confirmed verbatim.
- `L-0801` — prime coefficient `1/pi`, Toeplitz orientation and the `1/2`
  off-diagonal confirmed.
- `X-0801` — its stream metadata was accurate but its `c >= 10^10` output should
  be treated as nomination-only; see `R-5601`.
- `L-2806`, `L-5504` — the fixed-vector replay route they define is executed
  here and subsumed by the all-vector route of `L-5602`.
- The PR #61/#63/#64/#65 target runs are superseded for `c = 10^11`, `K = 1024`;
  their run plans and coverage checks remain correct and were reused.

## Recommended next actions

1. **Independent review of `T-5601` Step 1.**  Highest value per hour in the
   whole project right now: reconstruct the classical explicit formula from the
   Hadamard product inside the repository so the last external dependency of
   every certified number disappears.
2. **Retire the long-double phase path.**  Every D-0801 producer should use the
   L-5601 decomposition.  It is faster *and* bounded, so there is no trade-off.
3. **Search in `T`, not in `c`.**  The whole `c`-ladder now has certified
   margins, and they shrink smoothly.  The interesting free parameter is the
   carrier: `lambda_max(S_K)` at fixed `c` is a function of `T` whose maxima
   correspond to windows where the zeros conspire.  One `c = 10^9` stream costs
   3.5 seconds, so a scan over thousands of carriers is now cheap.  That is the
   natural continuation and it is a genuinely different search than the
   threshold-ranking of L-5501.
4. **Push `K` up at fixed `c`.**  All the certified margins here are at
   `K = 1024`.  `L-4202` requires `b = 2L/K <= 1/20`, i.e. `K >= 40 L`, which is
   satisfied for `K >= 1014` at `c = 10^11`; larger `K` is legal and gives the
   family more freedom.  The stream cost is independent of `K`.
5. **Review `L-4202` and `L-4203`** before any cell with a margin below `1e-8`
   is promoted.

## Organizational improvement ideas

1. **`CLAIMS.md` is four entries long and the repository has over forty claims
   across a dozen unmerged branches.**  Nothing is merged to `main`; every
   lineage re-derives context by reading sibling branches.  The registry is the
   one artifact that would make that cheap and it is the one artifact nobody
   updates.  Concretely: make the *last* commit of every agent branch a registry
   patch, and let the integrator merge only registry patches to `main`.  Claims
   files can stay on branches; the index should not.
2. **Numerical claims need a "bound or nomination" tag in the registry, not just
   in the file.**  `R-5601` exists because a stream honestly labelled
   `EMPIRICAL_NOT_CERTIFIED` was nevertheless consumed downstream as if it had
   digits.  A one-word column in `CLAIMS.md` would have made that visible.
3. **Every producer should ship an independent oracle before it ships a
   result.**  The anchor-wrap bug in this session was found in the first
   comparison run and would have survived every internal consistency test,
   including the table-invariance test, because both binaries shared the bug.
4. **Record the error budget alongside the value, always.**  The single most
   useful number in this report is not `2.67e-4`, it is `2.83e-12`.  A results
   table with a value column and no uncertainty column is what allowed the
   `c = 10^11` margin to be quoted to seven digits for two days.
5. **Prefer all-vector certificates to fixed-vector certificates when the
   operator is available.**  A fixed-vector replay costs the same 4.1e9-term
   pass as the lag coefficients, but answers a question about one direction out
   of 2048.  The lag-coefficient form answers the question you actually want and
   is reusable for every future vector at zero marginal cost.

---

## Addendum — two follow-up experiments run in the same session

After the main result was pushed I used the remaining budget on the direction I
had just recommended (`Q-5602`), and it produced the most consequential finding
of the session.

### A. Carrier landscape (`O-5602`)

256 complete directed streams at `c = 10^8`, `K = 1024`, stepping the carrier by
`0.2` (about one mean zero spacing) over 51 units:

```text
margin_min  0.0066414741   at the Issue #42/#44 carrier
margin_max  0.3082187205
margin_mean 0.1091097185      margin_std 0.0908192719
```

A factor-46 spread. `ell_T` is constant to `3e-14` across the window, so it is
all `lambda_max(S_K)`. The carrier that Issues #42/#44/#55 have been using sits
`16x` below the scan mean — the "optimized carrier continuation" of PR #42 found
something real, and every number in `O-5601` should be read as *the best carrier
known nearby*, not a typical one.

### B. The Nyquist threshold (`C-5601`) — and why the whole program has been
looking in the wrong place

While writing up A, the reason for the ladder's shape became clear.
`W_v` is the transform of a function supported on an interval of length
`Delta = log(c)/2pi`, hence of exponential type `pi Delta`, hence it can vanish
at at most `Delta` points per unit length. The zeros it must cancel have density
`ell_T = log(T/2pi)/2pi`. Same functional form, so the barrier is exactly

```text
Delta >= ell_T   <==>   c >= T/(2 pi).
```

**Every D-0801 computation in this repository has been below that barrier.**
At `T = 4709203636353.65` the threshold is `c* = 7.49e11 = 10^11.87`, and the
target of Issue #55 is `c = 10^11` — a factor `7.5` short. The positive margin
found there is exactly what the counting argument predicts; it is not evidence
that the family fails, it is evidence that the family was never given enough
support.

I tested this directly with a carrier low enough that the reachable ladder
straddles the barrier. At `T = 62831853071` (`T/2pi = 10^10`), certified
universal margins, `K = 1024`, `b <= 1/20` verified at every point:

| `c` | `Delta - ell_T` | certified margin | factor vs previous |
|---|---|---|---|
| `10^7`  | `-1.099403` | `3.87378e-1` | — |
| `10^8`  | `-0.732936` | `1.93912e-1` | 2.0 |
| `10^9`  | `-0.366468` | `1.21071e-1` | 1.6 |
| `10^10` | `+0.000000` | `3.55470e-2` | 3.4 |
| `10^11` | `+0.366468` | `5.29784e-4` | **67** |

Factors of 2.0, 1.6, 3.4 per decade below the barrier; **67 in the decade that
crosses it**. One carrier, five points, still a heuristic — but the qualitative
change happens at the predicted place.

### What follows

The two effects are independent and both large. Carrier tuning is worth `10^2`
to `10^3` (`O-5602`, and the `450x` gap between the tuned and untuned carriers
at comparable deficit); crossing the barrier is worth `~67x` per decade.
Together they put margins of `10^{-8}` to `10^{-9}` within reach — which is the
scale at which `B_A ~ 1.7e-10` stops being negligible.

So the concrete program is no longer "replay one more vector":

1. run above the barrier — either `c >= 10^12` at the current carrier (`3.8e10`
   terms, `K = 2048`, about an hour with this producer) or a lower carrier where
   the barrier is cheap to clear;
2. optimize the carrier *there*, not below it;
3. get `L-4202` and `L-4203` independently reviewed, and implement the exact
   archimedean block of `L-4201`, before any margin below `1e-8` is quoted.

None of that produces a counterexample by itself — under RH the margin stays
nonnegative however far one pushes. What it produces is the first D-0801
computation whose sign is genuinely in doubt in advance, which is the thing this
project has not had.

The producer already supports cutoffs up to `2^{61-JBITS}`; the `2^37` guard was
lifted and re-validated against the oracle during this session.

---

## Addendum 2 — past the barrier, the archimedean gate becomes the whole problem

Continuation after a container restart.  Two results, one of them a near-miss
with a false positive that is worth reading carefully.

### C. The depth grid (`O-5603`)

Sweeping both the deficit and `K` at a fixed cheap cutoff `c = 10^9` (3.5 s per
stream, carrier moved down as `T = 2 pi 10^m`) gives a sharper signature of the
C-5601 barrier than the cutoff ladder did:

- **below** the barrier the leading margin saturates in `K` (ratios `1.5, 1.1`
  across `K = 1024, 2048, 4096` at deficit `0`);
- **past** it the margin falls like `K^{-2}` (successive ratios cluster on `4` at
  deficits `+0.37, +0.73, +1.10, +1.47`).

That is what the counting argument predicts — past the barrier extra cells buy
genuine new zeros to place — and it means the *character* of the problem changes
there.  The `L-4202` gate scales like `K/T` while the margin falls like
`K^{-2}`, so `margin/gate ~ T/K^3`: past the barrier the archimedean bound, not
the prime side, is what stops the search.  Every deep grid point is unresolvable
against the gate despite the prime stream being certified to `3e-13`.

Smallest leading margin seen anywhere: `1.195e-7` at deficit `+1.832`,
`K = 2048`.  At `K = 4096` the same deficit gives `-3.77e-7`, i.e. the leading
screen has gone negative.

### D. The exact blocks, and a false positive avoided (`O-5603`)

So I assembled `A_K` (L-4201) and `R_K` (L-4203) directly instead of bounding
them — one-panel-per-oscillation Gauss-Legendre on the `K` compact oscillatory
integrals, plus the two rank-one pole factors.  At `c = 10^9`, `K = 1024`,
`T = 6283.185307` (deficit `+2.199`):

```text
lambda_min(ell_T I - S_K)      =  -0.3373320       <-- leading screen
lambda_min(A_K + R_K - S_K)    =  +3.34763e-6      <-- exact form
```

RH is verified far above `T = 6283`, so nonnegative is the only admissible
answer.  **A pipeline that screened on the leading matrix alone would have
reported a spectacular false counterexample at these parameters**, and the
`L-4202` gate (`B_A = 0.129`) is far too coarse to have caught it — what rescues
the sign is mostly `||R_K|| = 0.574`, the pole block that PR #37 and PR #44
dropped entirely.  Now locked in as a regression test.

Measured against the uniform bounds:

| `T` | `||A_K - ell_T I||` | `B_A` (L-4202) | ratio |
|---|---|---|---|
| `6283.185307` | `1.379e-3` | `1.287e-1` | 93 |
| `62831.85307` | `1.254e-4` | `1.287e-2` | 103 |
| `628318.5307` | `1.252e-5` | `1.287e-3` | 103 |

The `1/T` shape of L-4202 is confirmed; its constant is a stable factor `~100`
too large, which is precisely the carrier-phase cancellation among diagonals its
proof discards (`Q-5605`).  On top of that sits a second, larger pessimism: at
`T = 62831.85` a correction of norm `1.25e-4` moves `lambda_min` by only
`2.4e-8`, because it acts almost orthogonally to the minimizing direction.  An
operator-norm gate cannot see that; only assembling the matrix can.

Two further checks that had never been run anywhere in the repository, both now
passing: `L-4203`'s rank-two formula against a direct evaluation of
`2 g_{T,v}(i/2)/h` for random complex vectors, and `L-4202`'s `Ci`/`q_b`
decomposition of `alpha_0` against the raw `L-4201` integral.

### Revised roadmap

The bottleneck moved twice in this session.  It was the phase arithmetic (fixed,
`L-5601`); then it was the cutoff relative to the barrier (`C-5601`); now it is
the archimedean gate.  The next deliverable is therefore **not** more primes:

1. `Q-5604` — a *rigorous* quadrature for the `K` compact integrals of L-4201:
   outward-interval Gauss-Legendre with a Bernstein remainder while
   `T b <~ 10^5`, and the endpoint asymptotic expansion (integration by parts at
   the three kinks per lag) beyond, where it gets *more* accurate as `T` grows.
   Without it no sign past the barrier can be certified; with it the resolvable
   region opens by several orders of magnitude.
2. `Q-5605` — the cheap version: sharpen L-4202 by bounding through the Toeplitz
   symbol instead of a row sum, recovering the factor `~100` by proof rather
   than by computation.
3. Only then push `c` and `T` together.

18 tests pass.  Still no counterexample, still no `Z-####` — and one that a less
careful pipeline would have claimed was caught and turned into a regression
test.

---

## Addendum 3 — the archimedean bottleneck is gone (`L-5603`)

Addendum 2 ended with the archimedean gate as the binding constraint and
`Q-5604` — a rigorous evaluation of the L-4201 block — as the next deliverable.
The mathematics of that is now done.

### The observation

`varphi_d = k \cdot \tau_d(\cdot/b)` is supported on `[(d-1)b, (d+1)b]`,
vanishes at both outer endpoints, and is smooth except for the hat's kink at
`t = db`.  The hat is *affine*, so `u'' = 0` and
`varphi^{(m)} = k^{(m)}u + m k^{(m-1)}u'`.  Integrate by parts on each half:
every `m = 0` boundary term vanishes (continuity plus vanishing outer values),
the two `k^{(m)}` terms at the kink cancel in the difference, and what is left
is

```
int varphi_d e^{-i omega t} dt
  = sum_{m>=1} (i omega)^{-(m+1)} (m/b) D_d^{(m-1)},
  D_d^{(j)} = k^{(j)}((d-1)b) e^{-i omega (d-1)b}
            - 2 k^{(j)}(db)   e^{-i omega db}
            +   k^{(j)}((d+1)b) e^{-i omega (d+1)b}.
```

The series starts at `omega^{-2}`, not `omega^{-1}`.  **The archimedean
off-diagonals are `O(1/T^2)`**, smaller than L-4202's total-variation bound by a
factor of order `omega b = T log(c)/K`.  Lag `d = 1` is the exception: its
support reaches `t = 0` where the hat cancels `k`'s pole, leaving
`varphi_1(0) = 1/b` and a genuine `O(1/T)` term — the *only* one in the whole
block.

### What it buys

At the production carrier, where direct quadrature would need `10^{11}` panels
per lag, the whole block takes 1.5 seconds:

```text
alpha_0 - ell_T                 2.1924e-24
|z_1|                           1.3664e-12
sum_{d>=2} |z_d|                1.2006e-22
assembled row sum               1.3664e-12
expansion remainder bound       2.1924e-36
L-4202 uniform bound B_A        1.6566e-10      -> 121x larger
```

To ten significant figures the entire archimedean block is the single number
`z_1 = 1/(2 pi omega b) = K/(2 pi T log c)`.

Reassembling the production certificate with the computed blocks instead of the
L-4202/L-4203 envelopes:

```text
lambda_min(A_K + R_K - S_K)  floating   2.671872230e-4
                             lower      2.671861467e-4
total enclosure half-width              7.633e-11
  Gram residual + rounding              7.348e-11   <-- now dominant
  L-5601 stream enclosure               2.830e-12
  archimedean expansion remainder       2.192e-36
  pole block (assembled)                5.962e-18
```

### Where the bottleneck is now

It has moved four times in this session:

1. carrier phase arithmetic → fixed by `L-5601`;
2. cutoff relative to the Nyquist barrier → identified as `C-5601`;
3. the archimedean gate → removed by `L-5603`;
4. **the binary64 Gram factorization residual**, `7.35e-11`.

Number 4 is an artifact of the linear algebra, not of the mathematics, and is
removable by factoring in higher precision or by a sharper residual bound.  It
sits `3.5e6` below the current margin, so it does not matter yet; it will matter
the moment a cell with a margin near `10^{-10}` is found, which is precisely
what the C-5601 programme aims at.

The one genuinely analytic gap left in the chain is that `L-5603`'s
implementation is ordinary floating point.  Making it directed — interval
`k^{(j)}` at the knots, interval knot phases from L-5601, outward remainder — is
bookkeeping rather than mathematics, and it is the last thing standing between
this pipeline and a certified sign past the barrier.

21 tests pass.  Still no counterexample.

---

## Addendum 4 — the number that reframes the whole avenue (`L-5604`)

Three addenda spent on making the margin smaller and better bounded.  This one
asks the complementary question the project had never asked: **how small does
the margin have to be before the test could see a counterexample at all?**

### The response is quadratic

An off-critical zero `rho_0 = 1/2 + eta + i gamma` belongs to a quadruple whose
Weil coordinates are `gamma -+ i eta` and `-gamma -+ i eta`.  Since `g` is even,
entire, and real on the real axis, the quadruple contributes exactly
`4 Re g(gamma + i eta)`, and expanding about `gamma` (where all derivatives are
real, so the odd terms are purely imaginary and cancel):

```text
4 Re g(gamma + i eta) - 4 g(gamma) = -2 eta^2 g''(gamma) + O(eta^4).
```

**Second order in the displacement, with no first-order term.**  So a margin
`lambda_min` converts into a detection threshold
`eta_min = sqrt(lambda_min ghat(0) / (2 g''(gamma)))`.

### The optimal threshold, computed

`g''(T+u) = (1/2) v^* M''(u) v` with `M(u) = conj(beta) beta^T` rank one, so
`M''` has rank at most three, `M'' = C S C^*`.  A quadruple at `T+u` displaced
by `eta` makes the exact form negative *for some vector in the family* exactly
when `eta^2 > 1/lambda_max(S C^* Q^{-1} C)` — a `3x3` eigenproblem per `u`.  At
the production parameters, over 401 values of `u`:

```text
eta_min  optimal over all v      0.03154   at u = +0.26
eta_min  median over u           1.1429
eta_min  max over u              1.7866
```

I first computed this the lazy way, fixing `v` to the on-line minimizer and
taking `g''` at its steepest zero, and got `0.0153`.  That pairing is
inconsistent (global minimum in the numerator, one particular vector's curvature
in the denominator) and it was optimistic by a factor of two.  The pencil
computation is the correct one.

### What it means

A nontrivial zero has `0 < beta < 1`, so `|eta| < 1/2` always.  Therefore:

- at a **typical** position in the window, `eta_min = 1.14 > 1/2`: the executed
  configuration **could not have detected an off-critical zero there at all**,
  for any admissible displacement, and for no choice of vector whatsoever;
- at the single most favourable position, it could only have seen a zero
  displaced by more than `3 x 10^-2` — which the classical zero-free region
  already forbids at height `4.7e12`.

Combined with the `K^{-2}` law of O-5603, `eta_min` improves only like `K^{-1}`:
`10^{-3}` needs `K ~ 3e4`, `10^{-6}` needs `K ~ 3e7`.  A dense Hermitian
certificate at `K = 3e4` is already over 100 GB.

**So the honest assessment of the D-0801 avenue is not "nearly there".**  It is
many orders of magnitude short, and the reason is structural — the quadratic
response, not the quality of the arithmetic.  Every improvement in this session
(the `1000x` faster producer, the all-vector certificate, the `121x` tighter
archimedean block) sharpened a measurement whose sensitivity floor is set by
something none of them touch.

I want to be blunt about what this means for the request I was given.  The task
was to complete the computation and proofs for a full unconditional
counterexample.  Three sessions of this project's history had reduced that to
one big prime sum; I ran it, and it is positive.  This addendum explains why
that was never in doubt: **at these parameters the test cannot resolve any
displacement a real counterexample could plausibly have.**  A negative value
would have required an off-critical zero further from the line than the
zero-free region permits.

### What would actually change the picture

1. A different test family with a *first-order* response to displacement.  The
   quadratic response is forced here by `g >= 0` on the real axis, which is what
   makes the Weil criterion work in the first place — so this is a real tension,
   not an oversight, and worth its own issue.
2. Exploiting the Toeplitz structure to reach `K ~ 10^4`-`10^5` without dense
   linear algebra.  The symbol route of L-5602 is the natural vehicle and is
   currently far too weak (`10.34` against `ell_T = 4.35`); closing that gap is
   the concrete structural problem.
3. Accepting the avenue as a *measurement* rather than a search: the certified
   margins are quantitative statements about the zeros near the carrier, and
   `L-5604` says exactly what they exclude.  That is a real, if modest, result
   and it is what the repository actually has.

## Addendum 5 — the two positivity routes, costed; and the PR #71 candidate closed

The session's later half turned from *running* the D-0801 pipeline to asking
what it is worth running.  Three results, and they point the same way.

### The detection window is `O(1)` (`O-5606`)

`L-5604` answered "how small a displacement could this carrier see, at the best
offset?" — `eta_min = 0.0315`, comfortably under the ceiling `|eta| < 1/2` that
every nontrivial zero obeys.  Read alone that number is encouraging, and I read
it that way at the time.  The complementary number decides the question:

> For how many units of height does `eta_min(u)` stay below `1/2` at all?

Outside that set the pass cannot fire for *any* admissible displacement, so
those ordinates are simply not examined.  Measured on a 3001-point grid over 52
mean spacings, at three cutoffs:

```text
log c   prime work   margin       eta_min(best u)   DETECTION WINDOW
  9       x 1        2.3487e-03      0.1168            1.0320
 10       x 9        6.0590e-04      0.0529            1.0560
 11       x 82       2.6719e-04      0.0315            1.0720
```

Every column moves except the one that matters.  **Eighty-two times the work
buys `3.9%` more height.**  And over `88%` of the scanned range `eta_min > 1/2`,
where no zero can reach.

Combined with `C-5601`, which forces a search to `c > T/2pi`, this gives a cost
per unit of certified height of `~ pi(T/2pi) ~ T/(2 pi log T)` — **linear in
`T`** — against `~139 sqrt(T/2pi)` for a Riemann–Siegel scan.  The ratio grows
like `sqrt(T)`; at the production height it is `286` in terms and `45` in
measured wall clock.  The sensitivity comparison runs the same way: a scan sees
any `eta > 0`, everywhere, because an off-line zero produces no sign change of
`Z` and is caught by *counting* rather than by looking.

I want to be careful about what this does and does not say.  It does not retire
the route.  A negative D-0801 value would disprove RH outright, with no appeal
to an external bound; a Turing exclusion is conditional on precisely such a
bound, so the two failure modes are disjoint and that is worth something.  The
certificate machinery — `L-5601` exact phases, `L-5602` Gram factors, `L-5603`
archimedean endpoints — certifies *values*, and is indifferent to whether the
values were worth seeking.  What the observation says is narrower and, I think,
unavoidable: **compute spent enlarging `c` in the hope of a negative is spent at
the wrong exchange rate.**  Search with a scan; certify with D-0801.

The honest caveat is that all three rows sit *below* the Nyquist barrier, so the
extrapolation across it rests on a conjecture.  The window would have to widen
by a factor of `~300` on crossing to reach parity, against a measured `3.9%` per
two decades — but that is an argument, not a measurement, and `O-5606` says so.
The `c = 10^12`, `K = 2048`, `T = 3.1e12` stream (`Delta/ell_T = 1.03`) is the
smallest configuration that would settle it, and it was still running when this
addendum was written.

### The PR #71 candidate, closed twice over

Asked to look at the open full-complex Pick direction at
`T = 20225875608341108140435/2^32`, I attacked it from a direction that does not
require resolving its `-2.6e-33` vs `+1.2e-35` disagreement at all.

**Structurally (`O-5604`).**  A Riemann–Siegel scan shows the ordinate sits
inside a gap of `4.326` mean spacings — against a window mean of `1.004` — with
`|Z|` reaching `259.78` where the typical scale is `sqrt(log t) ~ 5`.  That
explains the nomination: since `xi'/xi(s) = sum_rho 1/(s-rho)`, the screen was
in effect finding a large zero gap, which is a sound instinct, because a pair
leaving the critical line would leave exactly such a gap behind.

Then Turing's method proper.  The empirical census is blind to the case that
matters, since an off-line zero contributes to `N` but produces no sign change.
The real argument turns on the **quantisation of the off-line correction's
slope**: `M(t) = mult * sum (t - tau_j)_+` has slope `0, mult, 2*mult, ...`, so
an `N(t_1)` off by an amount not divisible by `mult` cannot be repaired at all.
That leaves two surviving alternatives out of seven, and `tau_localise.py` then
shows neither can place an off-line zero within 5 units of the candidate
ordinate — under the conservative bound `3 + 0.1 log t` *or* Trudgian's sharper
one.  The surviving `-2` branch is the boundary degeneracy, compensated exactly
by a pair sitting on the left endpoint.

**Numerically (`R-5603`).**  Rather than propagate errors, I measured the
screen's false-positive rate.  Perturbing the eight kernel values by independent
`2^-p` relative errors and recomputing `lambda_min`, 300 times per precision:

```text
true lambda_min   +1.2259907375435524056e-35      cond = 1.4266243e+39

 p     flag rate    1-sigma spread    most negative in 300 trials
128      0.533        2.99e-33            -5.42e-33
136      0.173        1.18e-35            -8.47e-36
144      0.000        4.45e-38            +1.218e-35
160      0.000        7.03e-43            +1.226e-35
```

At 128 bits the signal is `244` times below the noise and **the screen is a coin
flip**; the nominated `-2.626e-33` is `0.88` spreads from the median of pure
noise.  Three independent routes agree on the true value to 20 digits, and the
branch's own 70-digit replay agrees too once its frozen-vector Rayleigh quotient
is distinguished from `lambda_min` — they differ by `2.996e-5` relative, exactly
the measured tilt `sin(theta) = 9.39e-8` of the frozen direction, whose square
times the spectral gap reproduces the difference to six digits.

The prescription is to screen at `>= 160` bits.  This refutes a procedure, not
the criterion: `K >= 0` under RH is correct, the Gram identity genuinely
requires `Re rho = 1/2`, and the fourteen 192-bit directed blocks have `10^13`
of headroom and stand.

### One real error on the import path (`R-5602`)

`D-3201` states that `g(tau) = i F(1/2 + i tau)` is Herglotz.  It is
anti-Herglotz: with `Xi(z) = xi(1/2+iz)` we have `Xi'/Xi(z) = i F(1/2+iz)`, a
sum of `1/(z-gamma)` over real poles, so `Im g < 0` on the upper half-plane.
Unconditionally, for `tau = iy`, `s = 1/2 - y` and `F(1/2-y) = -F(1/2+y) < 0`
since `xi` increases on `(1/2, inf)`.  Confirmed at 30 digits from actual `zeta`
values at four points.  The correct sign is `g = -i F(1/2 + i tau)`.

No number in the repository changes — every code path works directly in
`H_{1/2}` and the upper-half-plane form is never evaluated.  But `D-3201` is the
declared interface to the cited literature, and a reversed `Im` is silent: `g`
and `-g` have the same poles, the same zero set, and the same residue sign
pattern.  It surfaces only as an unexplained sign in some later positivity test.

### And the explicit formula, checked end to end (`O-5605`)

For the first time both sides of `sum_rho g(z_rho) = h v*(A_K + R_K - S_K) v`
were evaluated at the production parameters.  The right side is `4.12e9` prime
powers, `L-5601` phases, `L-5603` endpoints, a `1024 x 1024` eigensolve and a
dyadic freeze; the left is 173 sign changes of `Z` and one envelope evaluation.
They share no code, no data and no method, and they bracket correctly:

```text
1.02875e-6  <  1.05183e-6  <  1.09111e-6
located zeros    prime side    plus full Parseval tail
```

the lower bound because `g >= 0`, the upper because the tail is added at the
smooth density and therefore overshoots.  The residual `3.7%` lies entirely
inside the `5.7%` tail.  Both sides are ordinary floating computations; the
content is the agreement, which would not survive an error in the normalization,
the enumeration, the huge-phase arithmetic, or the block assembly.

### What I would do next

Not a larger `c`.  Give `rs_zeta` an interval evaluation of `Z`, enough to
*certify* each sign change rather than merely observe it.  That removes the
weaker of the two conditions under `O-5604`, reduces the whole Turing conclusion
to a single imported bound on `\int S`, and turns X-5602 into a certified
zero-counting detector — which, by `O-5606`, is the cheaper search primitive by
a factor growing like `sqrt(T)`.

A first step in that direction ran while this was written: a 1000-unit scan at
`t = 10^13`, well above the Platt–Trudgian verified height of `3.0000175e12`,
locating 4471 sign changes against a smooth count of `4471.5625` — a deficit of
`0.5625`, an ordinary `S(t)` fluctuation.  Uncertified, like everything else in
X-5602 today, which is exactly the gap worth closing.

## Addendum 6 — the predicate that works, and what it cost to find

An external adversarial review supplied the object this whole session had been
circling without naming: the **exact slab discrepancy**

\[
 D(a,b) \;=\; N(a,b) - N_0(a,b),
 \qquad D(a,b) > 0 \;\Longrightarrow\; \text{RH is false},
\]

where `N` counts all zeros of `zeta` in the strip with `a < \Im\rho < b`, with
multiplicity, and `N_0` counts those on the critical line.  `D \ge 0` always, and
`D` is even at positive ordinates by the functional equation.  No conditions —
no bound on `\int S`, no conjecture, no floating-point sign decision.  The review
reported that it could not evaluate `D`, having no FLINT available.

`pip install python-flint` works here.  So the rest of the session was spent
computing it.

### What was certified

```text
window                                        span   N     N_0   D   cost
(4709203636333.1875, 4709203636373.125)        39.9   172   172   0   102 s
(10000000000000.5,   10000000000999.5)        999     4467  4467  0   21 min
(100000000000000.5,  100000000000050.5)        50     242   242   0   10 min
```

Every zero in those slabs is on the critical line **and simple** — `N` counts
with multiplicity and simple sign changes exhaust it.  The first window is the
one the whole repository has been arguing about; the other two are `3.3` and
`33` times the Platt–Trudgian exhaustively-verified frontier.

### The two halves

`N` comes from Arb's `zeta_nzeros`, as a ball that must isolate a single
integer.  `N_0` comes from certified sign changes of Hardy's `Z`, evaluated as

\[
 Z(t)=e^{i\theta(t)}\zeta(\tfrac12+it),\qquad
 \theta(t)=\Im\log\Gamma\!\left(\tfrac14+\tfrac{it}{2}\right)-\tfrac{t}{2}\log\pi,
\]

in ball arithmetic, accepting a sign only when the ball lies strictly on one
side of zero.  The branch of `\log\Gamma` is unambiguous because
`\Re(1/4+it/2) = 1/4 > 0`; checked against the Stirling expansion, the two agree
to `5\times10^{-63}`.

Since `N_0 \le N` is automatic, a certified **lower** bound on `N_0` reaching `N`
forces `D = 0`.  That is the whole trick, and it is why this is cheap: it never
needs to *locate* a zero, only to see `Z` change sign.

### The single most useful thing learned

> A `\zeta` **jet** at large height is enormously more expensive than `\zeta`
> itself.  `acb_series([s,1]).zeta()` at `\Im s = 4.7\times10^{12}` did not
> return in `100` seconds; `acb.zeta` at the same point costs `~0.3` s.

Everything follows from this.  Locating a zero needs derivatives — hence
`acb.zeta_zeros` costs `15.7` s per zero at index `4.3\times10^{13}`, `56` times
more than sampling.  The argument principle needs `\xi'/\xi`, hence jets, hence
it is priced out above about `10^{6}` and cannot audit the production heights.
And the `D` predicate is cheap for exactly the complementary reason: **a sign of
`Z` needs `\zeta` alone.**

That is not a coincidence of implementation.  It says the right question to ask
about a stretch of critical line is a *counting* question, not a *locating*
question, and the two differ by one to two orders of magnitude in cost.

### The audit

Every certificate reduces to one external call.  Contour integration of
`\xi'/\xi` around `[-1,2]\times[y_0,y_1]` counts the same zeros by a genuinely
different route, and agrees at three heights spanning four orders of magnitude:

```text
[0.5, 100]              [29.0000 +/- 4.31e-5]   vs  29    PASSED
[1000.5, 1020.5]        [16.00 +/- 1.23e-3]     vs  16    PASSED
[1000000.5, 1000010.5]  [20.00 +/- 1.28e-3]     vs  20    PASSED
```

It cannot follow higher, for the jet reason above.  Worth noting separately:
the `D = 0` certificates were *already* a cross-check — `N` from
`arb_zeta_nzeros`, `N_0` from `acb_zeta` and `acb_lgamma`, different code —
and at `t = 10^{13}` the two agreed exactly on `4467` zeros.

### The result I did not expect

Checking where the repository's candidate ordinates actually sit: **every one of
them, from every route, lies inside the first window above.**  The PR #71
full-complex direction, the `j = -5` finalist, the whole `X-3902` `j`-grid from
`-29` to `+29`, and the D-0801 production carrier all fall in a `2`-unit stretch
with `19` units of clearance on either side.  An exhaustive search of every
remote branch for ordinate-shaped constants finds nothing outside it.

So the entire counterexample backlog of this repository is refuted by one
`102`-second certificate.  And the reason they coincide is the lesson: every
route that nominated an ordinate was a screen for *local anomaly*, and `O-5604`
showed the Pick screens were in effect finding a large zero gap.  Four
independent methods spent themselves on one `2`-unit stretch of the critical
line, none of them able to count.

### Two failures worth recording

**A precision trap, twice.**  The review caught `rs_zeta.c` collapsing zero
ordinates to binary64 at serialization (`ulp = 9.8\times10^{-4}` at
`4.7\times10^{12}`).  I fixed it — and then reproduced the identical defect in
new code, routing *sample positions* through `float`, where at `t = 10^{15}` an
ulp is `0.125` against a mean spacing of `0.188`.  The run stalled at
`N_0 \ge 43` of `52` and reported `D \le 9` rather than concluding.  Correctness
was never at risk, because a coarse sample position is not a wrong answer — the
sign certified *at* it is still certified.  That is the fail-closed design
earning its keep, and it is the second time in one session that a large ordinate
in a `double` has caused trouble.

**A 303 MB artifact.**  A stalled refinement left `3.4` million undecided
samples, all serialised into the result JSON, which git refused.  The undecided
list is now capped at `200` with a count.

### What I would do next

Not a higher `c` in the D-0801 programme, and not more precision on any Pick
candidate.  Two things:

1. **Bind Arb's Platt entry points.**  They are all exported from the bundled
   `libflint` and reachable by `ctypes`.  They evaluate `Z` on a whole block by
   FFT instead of one point at a time, which is the only known way to beat the
   `\sqrt{t}` per-zero cost that currently sets the ceiling.  The one
   measurement made here went the wrong way — but it measured the *zero finder*
   built on Platt, which needs derivatives, not the sign evaluation, which does
   not.
2. **Certify first, screen second.**  At `~0.3` s per zero, running a nominated
   ordinate through `X-5604` costs less than almost any nomination is worth.
   Had that been available a year ago, the entire `j`-grid campaign would have
   been answered in under two minutes.
