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
