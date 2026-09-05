# O-105057 — Sub-diagonal reformulation of the HHFE gate and the deep sign hunt for O(X)

Claim ID: `O-105057`
Status: **PROVED ELEMENTARY REFORMULATION + LABELED SIGN CONJECTURE (OPEN) + DATA — RH not assumed, not claimed; gate HHFE102010 remains OPEN**
Created: 2026-08-23
Agent: claude (lane S, program A2)
Depends on: `L-103100`, `L-103101`, `L-103102` @ PR #702 `89f995450977c3590aada0c1447a7e6af7fcd9ac`; `L-105052`, `L-105053`, `O-105054` @ `claude/riemann-proof-review-8nz34i`; consumer-chain caveats per `T-105050` §4 and the Ht truncation repair of `T-105051` (all energies below are the TRUNCATED-field energies, n <= N_X = floor(X/U_X), exactly as in the deposited replay `experiments/X-105053-assault/`).
Replay: `experiments/X-105057-sign-hunt/` (fast_O.py, deep_run.py, out_*.json incl. out_onset_fine.json) (band-separation evaluator, validated to <= 2e-13 against the deposited exact pair sums at X = 1e4..4e6 and to <= 2e-13 against the exact field-integral sweep).
RH status: **unproved, not addressed**

## Objects

Notation of L-103100/L-103102: `eta` multiplicative with Dirichlet series
`zeta(z)^{1/2}`; `h_U = (mu 1_{>U}) * eta`; `A_-` the (1,2,4) Haar step;
`R` its ratio-four log-autocorrelation (`|R| <= 3 log 2`, `supp R = [-log 4, log 4]`);
`U_X = floor(X^{1/3})`, `N_X = floor(X/U_X)`. For `U = U_X`, `N = N_X`:

```
H(X) = int_U^{4N} | sum_{U<n<=N} h_U(n) n^{-1/2} A_-(Y/n) |^2 dY/Y   (>= 0),
D(X) = 3 log 2 * sum_{U<n<=N} h_U(n)^2 / n                            (>= 0),
O(X) = sum_{U<m!=n<=N, 1/4<m/n<4} h_U(m) h_U(n) (mn)^{-1/2} R(log(m/n)),
H = D + O   (Gram identity, L-103100.1; machine-verified).
```

Gate (`HCNC103100`, equivalent to `HHFE102010` by L-103102 + L-103101, and to
its near-coprime core by L-105053):

```
GATE:  E_+(L) := int_{2^L}^{2^{L+1}} [O(X)]_+ dX/X = 2^{o(L)}.
```

## Proved statements (all elementary; no new arithmetic input)

**(O-105057.1) [unconditional floor for O]** For every `X`,
`O(X) >= -D(X)`, hence by L-103101 `O(X) >= -X^{o(1)}`
(uniformly: for each `eps > 0` there is `C_eps` with `O(X) >= -C_eps X^eps`).

*Proof.* `H >= 0` (integral of a square) and `O = H - D`; L-103101 bounds `D`. QED

Consequence: `|O| <= [O]_+ + D`. The one-sided gate automatically controls
`|O|`; there is no separate "negative-spike" risk. The measured
`O(X) in [-3.8, -2.1]` with `D in [2.7, 4.84]` (below; the 4.84 at X = 1e12
per out_big.json — hostile-review data correction) sits inside this proved
floor with room ~1 — the floor is nearly active.

**(O-105057.2) [sub-diagonal energy reformulation]** The following differ
pairwise by at most `int_{oct} D dX/X <= (log 2) sup_{oct} D = 2^{o(L)}`, so
each is `2^{o(L)}` iff any other is:

```
(a) int_oct [O]_+ dX/X   (= GATE),
(b) int_oct |O| dX/X,
(c) int_oct H dX/X       (= HHFE102010, truncated reading Ht of T-105051).
```

Equivalently: GATE <=> "H(X) <= D(X) + (subpower) in octave mean" — the energy
never exceeds its diagonal by more than subpower on octave average. This is the
*sub-diagonal* formulation.

*Proof.* Pointwise: `[O]_+ = [H-D]_+ <= H` (since `D >= 0 <= H`);
`H = D + O <= D + [O]_+`; `|O| <= [O]_+ + D` (by O-105057.1). Integrate
`dX/X` over the octave; `int_oct D <= (log 2) C_eps 2^{eps(L+1)}` by L-103101.
QED. ((a)<=>(c) also follows from deposited L-103102; re-proved here to make
the `|O|` version and the constants explicit.)

**(O-105057.3) [sign conjecture ==> gate, with exact quantifiers]** Fix
`A >= 0`. Suppose there are `X_0` and, for each `L`, an exceptional set
`S_L subset [2^L, 2^{L+1})` with logarithmic measure
`mu_L := int_{S_L} dX/X <= 2^{-(2/3)L} epsilon(L)`, `epsilon(L) = 2^{o(L)}`,
such that

```
O(X) <= (log X)^A    for all X >= X_0, X notin S_L.
```

Then GATE holds. *Proof.* `[O]_+ <= (L+2)^A (log 2)^A`... precisely:
`int_oct [O]_+ <= (log 2)((L+1) log 2)^A + mu_L sup_oct [O]_+`, and
`sup_oct [O]_+ <= sup_oct sum |h_U(m) h_U(n)| (mn)^{-1/2} |R| << 2^{(2/3)L} L^{O(1)}`
(trivial bound: `|h_U| <= tau`, Cauchy–Schwarz on ratio-4 bands — L-105052/
O-105054 ledger, ANALYSIS §1 L-A4.1). Both terms are `2^{o(L)}`. QED

In particular, with `S_L` empty and `A = 0`:

**STRICT SIGN CONJECTURE (SC-105057-strict):** there is `X_1` with
`O(X) <= 0` for all `X >= X_1`. SC-strict ==> GATE ==> (deposited chain
L-103102 + L-102010/T-102001 + BVD100310, with the review-status caveats
enumerated in T-105050 §4 and the Ht repair of T-105051) RH.

**EMPIRICAL STATUS (this deposit's headline): SC-strict is REFUTED-shaped.**
The deep scan finds genuine sign changes of `O` in the canonical `U = X^{1/3}`
regime, first found at `X ~ 2.2e10`, verified in float128 and by the
independent exact field-integral sweep (Gram consistency ~5e-13 on the
lane's runs; an independent hostile replication of the 4e10 cell observed
4.6e-11 accumulation over 3.5e7 events — either way orders of magnitude
below the signal; the +0.604 value was reproduced to the last digit and
hardened by exact mu spot checks and a cancellation-free positive-term
sweep, H = 5.14461 > D = 4.54054): e.g. `O(4e10) = +0.604`,
`O(1e12) = +0.939`, `O = +7.76` at `X = 6.36e11`. The workable conjecture is
the BOUNDED/POLYLOG version (`A > 0` allowed, or `O <= C` with `C ~ 10`):
empirically `[O]_+ <= 7.8` throughout `X <= 1.2e12`, and O-105057.3 shows
this weaker statement still yields GATE. The lesson: the gate-relevant
quantity is the octave mean of `[O]_+`, which stays `O(1)`; pointwise
negativity was an artifact of the previously computed range `X <= 4e6`.

**Remark (no converse).** GATE does *not* imply any pointwise bound on `O`:
octave integrability tolerates power-size positive spikes of `O` on sets of
logarithmic measure `2^{-(2/3)L+o(L)}`. SC-105057 is strictly stronger than
needed; O-105057.3 is the exact amount of slack available.

**Remark (what would refute SC).** A single `X >= X_1` with `O(X) > 0` refutes
any given `X_1`; persistent positive octave mass refutes the gate route. The
data below is the falsifier map.

## §data — the deep sign hunt (band-separation evaluator; all values EXACT
evaluations of the deposited finite sums, not estimates)

Method: `R` is piecewise linear in `v = log(m/n)` on `(0, log 2]` and
`[log 2, log 4)`; hence with `c_n = h_U(n)/sqrt(n)`, `d_n = c_n log n` and
prefix sums `C`, `Dp`,

```
O = 2 sum_n c_n [ (3h + (3+sqrt2) log n)(C(m2)-C(n)) - (3+sqrt2)(Dp(m2)-Dp(n))
                + (-2 sqrt2 h - sqrt2 log n)(C(m4)-C(m2)) + sqrt2 (Dp(m4)-Dp(m2)) ],
h = log 2, m2 = min(2n, N), m4 = min(4n-1, N)
```

— an exact rearrangement of the pair sum (the pair `m = 4n` has `R = 0`), cost
`O(N)` after sieving `h_U` (cost `O(N log N)`), memory `O(N)`. This supersedes
the q-fiber plan: X = 1e12 costs N = 1e8. Validated: |band - deposited pair
sum| <= 2e-13 at all nine deposited X (1e4..4e6); Gram check |D+O-H_sweep| <=
2e-13.

**Scan inventory (304 distinct X in the canonical `U = X^{1/3}` regime, plus a
complete small-X census and theta-scans; every value an exact finite-sum
evaluation in float64, spot-checked in float128 and by the exact sweep):**

- Complete census: every integer `X in [8, 10^4]` (728 distinct `(U,N)`):
  `O(X) <= 0` for ALL, with equality iff the pair set is empty (`X = 8, 9`);
  strictly negative for all `X >= 10`. Range `[-2.18, -0.64]`.
- Dense grid, 6 pts/octave, `X = 1e4 .. 9.3e8` (100 pts): all `O < 0`,
  `O in [-3.43, -1.66]`, `H in [0.52, 2.33]`.
- Mid-cell U-scans `U = 1000..2780` step 20, `2700..4700` step 25,
  `8400..10800` step 100, plus big samples `2e9..1e12` and full-cell scans
  at `U = 3418..3420`: FIRST POSITIVE FOUND at `U = 2782`, `X = 2.154e10`
  (`O = +0.018` at the lane's in-cell point; the deposited step-1 fine scan
  `out_onset_fine.json`, `U = 2776..2800`, reproduces the onset with
  `O = +0.0149` at `U = 2782` and a near-miss `-0.0016` at `U = 2778`).
  Margins are razor-thin and the scans below `U = 2780` are step-20, so an
  isolated positive cell below 2780 is NOT excluded — "first found", not
  "first". Earlier near-miss `O = -0.45` at `X = 2.87e9`.
- Sign census at sampled points: 28/304 positive, all at `X >= 2.15e10`;
  global range `O in [-4.03, +9.54]`; max `O = +9.538` at `X = 9.70e11`
  (`U = 9900`); `O(1e12) = +0.939` (float128-verified).
- `O` is nearly constant across each `U`-cell (variation ~0.01-0.05) and
  jumps at `U -> U+1`: the natural scan variable is `U`.

**Octave table (mean over sampled points; `E_+ ~ mean([O]_+) * log 2`):**

```
L (X~2^L)  mean O   mean [O]_+  max [O]_+  mean H   D
13..33     -2.15 -> -3.09   0        0       0.55->1.33  2.70->4.43
34..35     -1.84/-1.97   0.19/0.20  2.29/2.33  2.65/2.59   4.49/4.56
36         -3.05        0.01       0.27       1.56        4.61
39         +0.70        2.00       9.54       5.52        4.82
40         +0.57        1.21       5.80       5.42        4.85
```

[H, heuristic labels] (i) The signed octave mean drifts down (-2.15 to -3.1
by L=33, slope ~ -0.089 per ln X on the negative-only range) and then RISES,
crossing to +0.7 by L=39: the "drift constant -2.3" of the deposited range is
transient, not asymptotic (consistent with lane M's finding that the signed
low-torsion skeleton drift sum tends to ~0, not -2.3). (ii) A single-zero
oscillation model (`gamma_1 = 14.1347` in `ln U` and/or `ln N`) fits poorly
(R^2 <= 0.14); the excursion structure is multi-frequency and its positive
envelope GROWS: max `[O]_+` per octave 0 (L<=33) -> 2.3 (L=34) -> 9.5 (L=39).
Envelope growth between the two anchors corresponds to `X^{0.43}` on two
points or `polylog` equally well — UNRESOLVED; this is exactly the gate
question. (iii) Octave `E_+` estimate stays `O(1)`: ~1.4 at L=39 vs `D ~ 4.8`
— the gate `E_+(L) = 2^{o(L)}` is unfalsified and the sub-diagonal form
`H <= D + O(1)`-per-octave-mean holds at every sampled octave so far
(mean H <= 5.5 <= D + 0.9 at L=39). (iv) theta-robustness: `theta = 1/3` and
`0.4` are sign-stable (all negative on `1e4..1e8`); `theta = 0.25` shows
positive windows already at `X ~ 4e7..2e8` (up to `O = +13.0`, `H = 17.9`,
sweep-verified): smaller `U` moves the sign-change onset DOWN — negativity is
a property of the `U >= X^{1/3}` truncation, and the canonical `U = X^{1/3}`
sits near the boundary where positivity first develops at `X ~ 2e10`.

## Falsifiers

Any `X` in the scanned ranges where an independent exact evaluation of `O(X)`
disagrees with the tables beyond 1e-9; an `X >= X_1(claimed)` with
`O(X) > 0` (refutes the empirical sign statement at that threshold);
failure of the band identity vs direct pair summation at any `X`.
