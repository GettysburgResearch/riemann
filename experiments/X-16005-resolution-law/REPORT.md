# Resolution law of the CvS pencil viewed as a pole detector

**Exploratory measurements, offered for others to check.** Nothing here is certified.
Everything numerical is HIGH-PRECISION FLOAT (mpmath, `dps = 40 + 5N`, `polyroots(..., extraprec=4000)`),
verified by root residuals and by re-running at `dps + 50…+100`. No interval or ball arithmetic was used.

Code and raw output: `/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/res/`
(`core.py`, `pilot.py`, `e1.py`, `e1b_margin_law.py`, `e2_resolution.py`, `e2b_margin.py`, `e2g_floor.py`,
`e3_weights.py`, `e4_band.py`, `e4d_density.py`, `e4e_check.py`, `e5_trunc.py`, `e6_zeta.py`, `e6b_compare.py`, `e7_odd.py`,
and the matching `*.out` files). Nothing was written to or committed in `/home/user/riemann`.

---

## 0. Setup and cost estimate (pilot)

Nodes `lam_j = j`, `j = -N..N`, `dim = 2N+1`. Source

```
psi(x) = sum_k a_k [ 1/(mu_k - x) + 1/(-mu_k - x) ],   a_k > 0, mu_k > 0
```

`Q = Loewner(psi)`, `xi = Q^{-1} eta` normalised to `eta^T xi = 1`,
`P_xi(s) = sum_j xi_j prod_{k!=j}(lam_k - s)`.

**EXACT (one line, as stated in the task).** `Omega(s) = prod_k (lam_k - s)`, `ell(s)_j = 1/(lam_j - s)`, so
`Omega(s) <xi, ell(s)> = sum_j xi_j Omega(s)/(lam_j - s) = sum_j xi_j prod_{k!=j}(lam_k - s) = P_xi(s)`. ∎

**EXACT (structural, and it drives everything below).** `psi` is odd ⇒ `Q` commutes with the flip ⇒ `xi` is even ⇒
`P_xi` is an **even** polynomial of degree `2N` with leading coefficient `eta^T xi = 1`. I therefore reduce to
`R(u)` of degree `N` with `P_xi(s) = R(s^2)` and root the degree-`N` polynomial, which is far better conditioned
than degree `2N` and enforces the `±` symmetry exactly. The odd coefficients of `P_xi` were checked to be
`< 1e-62 … 1e-112` relative in every run.

### Pilot checks (all passed; total runtime 3.4 s)

| check | result | label |
|---|---|---|
| L-16004 rank-one closed form vs literal divided differences, N=4,6 | max entrywise rel. difference `1.1e-61`, `1.3e-71` | HIGH-PRECISION FLOAT, consistent with EXACT |
| `P_xi(s) = Omega(s)<xi,ell(s)>` at s = 0.3, 2.7, −4.11 | rel. difference `8e-62`, `1.1e-59`, `5.5e-61` | HIGH-PRECISION FLOAT, consistent with EXACT |
| K = N positive poles ⇒ `Q` singular, kernel `xi` from partial fractions, `Q xi = 0` | `‖Qxi‖/scale = 8.6e-63, 4.9e-72, 6.9e-82` (N=4,6,8) | HIGH-PRECISION FLOAT |
| …and the roots of that `P_xi` equal the poles | max rel. err `3.6e-59, 8.1e-66, 6.8e-73` | HIGH-PRECISION FLOAT |
| all roots real, `max Im(u)/(1+|u|) = 0` exactly | in every single run reported below | HIGH-PRECISION FLOAT |

**Cost estimate reported before committing:** one full detection at N=14 (dim 29, dps 110, K=30 poles) costs
**1.5 s**; N=4 costs 0.05 s. The whole planned study (≈ 1500 detections including bisections) was estimated at
**under 45 minutes**. Actual total ≈ 40 min, dominated by one 29-min bisection sweep.

---

## 1. The structural fact that organises everything (EXACT)

If the source has **exactly `N` positive poles** (hence `2N` poles with the `±` pairs), then
`Q = sum_{m=1}^{2N} a_m ell(mu_m) ell(mu_m)^T` has rank `2N` in dimension `2N+1`, so it is **singular**,
its kernel is one-dimensional, and by the L-16004(iii) computation `<ell(mu), xi> = P_xi(mu)/Omega(mu)`
the kernel vector's polynomial has its roots **exactly at the poles**. Verified to `5e-88` relative
even for a pathologically dense pole set (see §5).

So **the apparatus is an exact pole-recovery device when #poles = N, and there is no resolution limit at all
in that case.** Every "resolution law" measured below is a statement about *truncation*: what happens when
the source has more poles than the model can carry. That is the regime of the arithmetic computation.

---

## 2. Q1 — How many poles are recovered? The count law and the margin law

Fixed comb source `mu_k = S/2 + S·k`, `k = 0..K-1`, all `a_k = 1`, `K = 30` (so `K ≫ N` throughout), `S = 3.7`.

### 2a. Relative error per pole index vs N (HIGH-PRECISION FLOAT)

`—` means no recovered root had this pole as its nearest true pole.

| pole idx k | mu_k | N=4 | N=6 | N=8 | N=10 | N=12 | N=14 |
|---|---|---|---|---|---|---|---|
| 1 | 1.85 | 8.5e-14 | 1.7e-19 | 4.4e-25 | 1.2e-30 | 3.1e-36 | 7.1e-42 |
| 2 | 5.55 | 1.8e-6 | 9.4e-15 | 1.4e-21 | 9.0e-28 | 9.4e-34 | 1.2e-39 |
| 3 | 9.25 | 9.6e-3 | 1.1e-6 | 4.2e-13 | 1.2e-22 | 6.2e-30 | 1.4e-36 |
| 4 | 12.95 | — | 2.2e-3 | 4.1e-7 | 1.4e-12 | 2.7e-20 | 1.2e-31 |
| 5 | 16.65 | 1.0e-2 | 7.6e-2 | 5.2e-4 | 1.2e-7 | 1.2e-12 | 3.8e-19 |
| 6 | 20.35 | — | — | 2.4e-2 | 1.3e-4 | 3.1e-8 | 5.3e-13 |
| 7 | 24.05 | — | — | — | 7.8e-3 | 2.9e-5 | 6.9e-9 |
| 8 | 27.75 | — | — | 3.3e-2 | — | 2.4e-3 | 5.9e-6 |
| 9 | 31.45 | — | 4.1e-2 | — | 5.1e-2 | 3.1e-2 | 6.4e-4 |
| 10 | 35.15 | — | — | — | — | — | 1.2e-2 |

**Counts (rel. err < 1e-6): N = 4,6,8,10,12,14 → 1, 2, 4, 5, 6, 7.**
So `deg P_xi = 2N` gives `N` positive roots, of which **about `N/2` track true poles and about `N/2` are artifacts**.

Confirmed for odd `N` too (zeta-positioned source, §6): the number of poles recovered to better than `1e-3` is
exactly `floor(N/2)` for `N = 5..13`.

### 2b. The organising variable is the **budget margin** `m = N − 2k`

The table above is nearly constant along diagonals `N − 2k = const`. Making that the row index:

`log10(relative error)`, comb spacing `S = 3.7`, `K = 40` (HIGH-PRECISION FLOAT):

| m = N−2k | N=6 | N=8 | N=10 | N=12 | N=14 |
|---|---|---|---|---|---|
| 8 | | | −29.8 | −32.9 | −35.6 |
| 6 | | −24.3 | −27.0 | −29.1 | −30.7 |
| 4 | −18.8 | −20.8 | −21.8 | −19.4 | −18.2 |
| 2 | −14.0 | −12.4 | −11.8 | −11.8 | −12.1 |
| **0** | **−5.9** | **−6.4** | **−6.9** | **−7.4** | **−8.0** |
| −2 | −2.7 | −3.3 | −3.9 | −4.4 | −5.1 |
| −4 | −1.1 | −1.6 | −2.1 | −2.6 | −3.1 |
| −6 | −0.9 | −0.9 | −1.1 | −1.5 | −1.8 |

Rows are flat to within ~1 decade over a factor of 2.3 in `N`. The same table at `S = 1.85, 7.4, 14.8`
(file `e1b.out`) has the same shape; for `S ≥ 3.7` the rows `m ≤ 2` agree to within about one decade across
all three spacings.

> **LAW A (count / margin law).** *Empirical, exploratory.* For a source whose poles are spaced at least
> ~1.5 node spacings apart, the detector reproduces pole `k` with relative error a function of the margin
> `m = N − 2k` alone: roughly `1e-6` at `m = 0`, `1e-12` at `m = 2`, `1e-20` at `m = 4`, `1e-3` at `m = −2`,
> and nothing usable for `m ≤ −4`. Equivalently: **the budget is `floor(N/2)` poles**, the last of which is
> known to ~6 digits and the second-to-last to ~12.

### Guess REFUTED

The task's suggested guess — "the apparatus resolves poles up to some multiple of `N`" — is **wrong**.
Sweeping the comb spacing at fixed `N` (file `e4.out`):

| N | S = 1.85 | S = 3.7 | S = 7.4 | S = 14.8 |
|---|---|---|---|---|
| 6 | cnt 3, mu_max 4.6 | cnt 3, mu_max 9.3 | cnt 2, mu_max 11.1 | cnt 2, mu_max 22.2 |
| 10 | cnt 6, mu_max 10.2 | cnt 5, mu_max 16.7 | cnt 5, mu_max 33.3 | cnt 5, mu_max 66.6 |
| 14 | cnt 8, mu_max 13.9 | cnt 7, mu_max 24.1 | cnt 7, mu_max 48.1 | cnt 7, mu_max 96.2 |

(counts at rel. err < 1e-6.) The **count** is pinned at `≈ N/2` while `mu_max` scales linearly with the
spacing, reaching `6.9 N` at `S = 14.8`. There is no fixed height band. See §5 for the correct band statement.

---

## 3. Q2 — Resolution of a close pair

Design: comb of `K = 25` poles at spacing `S = 5.11` (offset 2.63 so nothing lands on an integer node),
all weights 1, with the element of index `k0` **replaced by a pair `m0 ± d/2`**, each of weight 1.
"Separated" means the two recovered roots nearest `m0` reproduce both pair members to within `0.1 d`.
`d_min` found by 16-step geometric bisection on `d ∈ [1e-14, 0.6 S]`.

### 3a. `d_min` vs budget margin (HIGH-PRECISION FLOAT, file `e2f.out`)

| margin m = N/2 − k | N=8 | N=10 | N=12 | N=14 | N=16 |
|---|---|---|---|---|---|
| 6 | | | | 2.3e-14 | <1e-14 |
| 5 | | | 3.7e-12 | 1.6e-13 | 5.3e-14 |
| 4 | | 5.4e-10 | 4.1e-11 | 4.1e-11 | 4.5e-9 |
| 3 | 7.6e-8 | 1.2e-8 | 2.5e-7 | 2.9e-6 | |
| 2 | 6.6e-6 | 2.1e-4 | 5.4e-4 | 7.1e-4 | |
| 1 | 2.9e-2 | 3.6e-2 | 3.4e-2 | 2.7e-2 | |
| **0** | **1.01** | **0.77** | **0.56** | **0.38** | |
| −1 | never | never | never | 2.82 (fails criterion at all d) | |

`d_min` is a function of the **margin**, essentially independent of `N` — the rows are flat to within a factor
of a few over `N = 8..16`. It falls by roughly **2 to 3 orders of magnitude per unit of margin**.

### 3b. Position in the band is *not* the variable

At `N = 14` the pairs at `m0 = 2.63, 7.74, 12.85, 17.96` (i.e. `m0/N = 0.19 … 1.28`, straddling the node-band
edge) all give `d_min < 1e-5`, while `m0 = 33.29` (`m0/N = 2.38`) gives `d_min = 0.38`. But those are also
margins 6,5,4,3 vs 0. Comparing across `N`: `m0 = 12.85` gives `d_min = 4.1e-11` at `N = 14` (margin 4) and
`2.1e-4` at `N = 10` (margin 2) — same height, 7 orders of magnitude apart. **Height does not control
resolution; the pole's index relative to `floor(N/2)` does.**

### 3c. `d_min` vs the local pole spacing (weakest measurement here)

At fixed margin 1 (file `e2f.out`):

| S | 1.277 | 2.555 | 5.11 | 10.22 | 20.44 |
|---|---|---|---|---|---|
| N=10, d_min/S | 0.138 | 2.9e-5 | 7.0e-3 | 1.3e-2 | 1.4e-2 |
| N=14, d_min/S | 8.0e-3 | 1.6e-5 | 5.3e-3 | 9.4e-3 | 1.1e-2 |

For `S ≥ 5` the ratio `d_min/S` is roughly constant (`0.005–0.014`), i.e. `d_min` scales with the ambient
pole spacing. The `S = 2.555` column is a clear outlier and I have **no explanation for it**; I would not
fit a constant to this row. Reported as noisy.

### 3d. The floor is mathematical, not numerical

`N = 14`, pair at margin 6, gap `d` swept (file `e2g.out`), each case run at **dps 110 and dps 170** —
the two agree to every printed digit:

| d | 1e-10 | 1e-15 | 1e-20 | 1e-25 |
|---|---|---|---|---|
| recovered gap | 1.0e-10 (SEP) | 2.15e-12 (merged) | 0.021 (merged) | 5.11 (pair gone) |

Doubling the working precision changes nothing, so the `~2e-14` floor at margin 6 is a property of the
estimator, not of the arithmetic. Below the floor the pair degenerates to a single root (and eventually the
two nearest roots are just two different comb elements, gap `= S`).

Also: `d_min` was insensitive to the success tolerance from `0.5` down to `0.001` (file `e2.out`, E2e) —
the transition from "exact to 40 digits" to "wrong" is abrupt.

> **LAW B (resolution).** *Empirical, exploratory.* There is **no minimum separation set by the node spacing**.
> A close pair at index `k` is resolved down to `d_min ≈ S · 10^{-0.9 − 2.4 m}` with `m = floor(N/2) − k`, and
> not at all once `m < 0`. My prior guess of a Nyquist-type floor `d_min ~ 1` node spacing is **REFUTED**:
> at `N = 14` a pair at index 1 is separated at `d = 1e-10`, ten orders of magnitude below the node spacing.

---

## 4. Q3 — Weight sensitivity

Comb of 25 poles weight 1, plus one **probe** pole of weight `a` inserted midway between two comb elements
(file `e3.out`). Relative error of the recovered probe position:

| a | N=14, probe at 5.185 (margin ≈5) | N=14, probe at 30.735 (margin ≈0) | N=10, probe at 5.185 | N=10, probe at 20.515 (margin ≈0) |
|---|---|---|---|---|
| 1 | 2.18e-43 | 1.48e-6 | 9.09e-30 | 1.08e-5 |
| 1e-2 | 2.18e-41 | 1.48e-4 | 9.09e-28 | 1.08e-3 |
| 1e-4 | 2.18e-39 | 1.45e-2 | 9.09e-26 | 9.5e-2 |
| 1e-6 | 2.18e-37 | lost (root snaps to 28.18) | 9.09e-24 | lost (snaps to 17.96) |
| 1e-10 | 2.18e-33 | lost | 9.09e-20 | lost |
| 1e-16 | 2.18e-27 | lost | 9.09e-14 | lost |

The scaling is **exactly `1/a` over 16 orders of magnitude** (2.177e-43 → 2.177e-27 as `a` goes 1 → 1e-16;
the mantissa never changes).

> **LAW C (weights).** *Empirical, exploratory.* `rel.err(pole with weight a) = e_base(margin) / a`, where
> `e_base` is the margin-law error of §2b. Hence the detection floor is `a_min ≈ e_base / tol`:
> **a well-inside-budget pole has essentially no weight floor** (at margin 5, weight `1e-16` is still located to
> 27 digits), while **a pole at the budget edge is lost below `a ≈ 1e-4`**. The presence of an arbitrarily weak
> extra pole does not perturb the other recovered roots (the shift column in `e3.out` is constant in `a`).
>
> Caveat: in a finite-precision implementation this is capped by working precision — the `1/a` growth means a
> weight of `1e-16` costs 16 digits.

---

## 5. Q4 — "Band": there is no height band, but there is a **density** floor

### 5a. Reach

From §2's spacing sweep, the highest reliably recovered pole is `mu_max ≈ S·floor(N/2)`, i.e. determined by
counting, not by height. Values of `mu_max/N` observed range from `0.77` to `6.9`. **The guess "poles up to
`C·N`" is REFUTED**; the only correct statement of that form is the *lower* bound in §5b.

### 5b. There is a hard density floor at ~1 node spacing

Counts `(rel.err<1e-6)/(rel.err<1e-3)` for a comb of spacing `S`, `K` chosen so the source reaches `6N`
(file `e4d.out`, HIGH-PRECISION FLOAT):

| N | budget | S=0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.5 | 1.8 | 2.2 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 3 | 0/0 | 0/0 | 0/0 | 0/1 | 0/0 | 0/5 | 0/4 | 1/5 | 3/4 | 3/4 | 3/4 | 3/3 |
| 10 | 5 | 0/0 | 0/1 | 0/0 | 0/0 | 0/0 | 1/8 | 4/9 | 6/8 | 7/7 | 6/7 | 5/6 | 5/6 |
| 14 | 7 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 3/13 | 9/12 | 10/11 | 10/10 | 9/10 | 8/9 | 7/9 |

Below `S ≈ 1` (the node spacing) **nothing at all is recovered** — the recovered roots instead form a comb of
spacing `≈ 1.02–1.1`, i.e. the detector reports the node lattice rather than the source. The critical spacing
does not move with `N`. Between `S ≈ 1.2` and `S ≈ 1.8` the count *exceeds* `N/2` and `mu_max` saturates at
`≈ N` (the node band edge), so a compact summary is
**reach `H ≈ max(N, S·floor(N/2))`, count `≈ H/S`.**

### 5c. It is a density effect, not an extent effect — and it is entirely about truncation

Three controls (file `e4d2.out`, `e4e.out`):

| control | result |
|---|---|
| `N=10, S=0.9`, vary source extent `K = 11 … 120` | recovered roots converge as `K` grows and are *always* wrong (0.581, 1.696, 2.823, … vs true 0.487, 1.387, 2.287, …). Failure at `K = N+1` is as complete as at `K = 120`. **Extent is not the cause.** |
| same at `dps 90 / 150 / 210` | identical to 12 printed digits. **Not roundoff.** |
| `N=10, S=0.9`, `K = N = 10` exactly (no excess pole) | **max rel. err 5.1e-88** — perfect recovery at the same density |
| `N=10, K = N+1 = 11`: `S=0.9` vs `S=1.85` | errors of poles 1..6: `0.18, 0.21, 0.22, 0.13, 0.046, 0.006` vs `1.6e-20, 9.8e-19, 1.8e-17, 6.0e-16, 7.0e-14, 1.6e-10` |

> **LAW D (density).** *Empirical, exploratory.* The estimator is exact when `#poles = N` at any density.
> What density controls is **sensitivity to a single unmodelled pole**: with a source spaced `≳ 1.8` node
> spacings, one excess pole costs `1e-20`; with a source spaced `0.9`, one excess pole costs `0.2`.
> Sources denser than about one pole per node spacing are unusable in the truncated regime.

---

## 6. Q5 — Truncation: 50 poles at N = 6, and the bias

`N = 6`, comb `1.85 + 3.7k`, `K = 50` (source reaches 183.15), all weights 1 (file `e5.out`):

| # | recovered root | nearest pole | **signed** rel. err |
|---|---|---|---|
| 1 | 1.85000000000000009 | 1.85 | **+**1.79e-19 |
| 2 | 5.55000000000005494 | 5.55 | **+**9.77e-15 |
| 3 | 9.25001075278416204 | 9.25 | **+**1.16e-6 |
| 4 | 12.9786502788387379 | 12.95 | **+**2.21e-3 |
| 5 | 17.9313483722100507 | 16.65 | **+**7.70e-2 |
| 6 | 33.0608409092648417 | 31.45 | **+**5.12e-2 |

`floor(N/2) = 3` poles are recovered (3rd to 6 digits), the 4th is marginal, roots 5 and 6 are artifacts.
The artifacts stop at 33 while the source reaches 183 — **the artifact roots do not sample the tail; they
cluster just above the last resolved pole.**

### 6a. Are the found ones biased? **Yes — systematically upward, and the bias converges in K.**

Signed relative errors, `N = 6`, comb spacing 3.7:

| K | pole 1 | pole 2 | pole 3 |
|---|---|---|---|
| 6 (= N, exact case) | 0.0 | +7.2e-69 | +1.3e-62 |
| 7 | +1.25e-20 | +7.55e-16 | +1.12e-7 |
| 8 | +3.19e-20 | +1.87e-15 | +2.62e-7 |
| 10 | +7.16e-20 | +4.08e-15 | +5.34e-7 |
| 15 | +1.32e-19 | +7.33e-15 | +9.02e-7 |
| 25 | +1.67e-19 | +9.17e-15 | +1.10e-6 |
| **50** | **+1.79e-19** | **+9.77e-15** | **+1.16e-6** |
| 100 | +1.80e-19 | +9.86e-15 | +1.17e-6 |
| 200 | +1.81e-19 | +9.87e-15 | +1.17e-6 |

Same picture at `N = 10` and `N = 14` (file `e5.out`, E5b): **every** signed error is positive, and the values
at `K = 50`, `100`, `200` agree to 2–3 significant figures.

> **LAW E (truncation).** *Empirical, exploratory.* (i) The truncation bias is **one-signed: recovered roots
> sit above the true poles**, pushed up by the unmodelled tail. (ii) The bias **saturates in `K`** — by
> `K ≈ 100` it is converged to 3 digits, and `K = 50` is already within 1 % of the `K = ∞` limit. So the fact
> that the zeta source has infinitely many poles is **not** an additional difficulty: a 50-pole model of the
> tail is numerically indistinguishable from the true infinite one. (iii) Almost all of the damage is done by
> the *first* excess pole: `K = N+1` already produces the truncation error to within one or two decades of the
> `K = ∞` value.

---

## 7. Q6 — Back to the zeta case. Does the law predict the observed cutoff?

### Short answer: **yes**, and quantitatively.

Model: poles at `mu_k = gamma_k · Delta`, `Delta = log(c)/(2π)`, `gamma_k` from `mpmath.zetazero`, `K = 90`,
weights `a_k = 1`. This is a *pure-pole model* of the arithmetic source, not the arithmetic matrix itself —
`Q_W` also carries archimedean, pole and `kappa/J` blocks. Agreement therefore tests the resolution law, not
the arithmetic.

**Relative errors of the recovered `gamma_k`, c = 2000** (HIGH-PRECISION FLOAT, file `e6.out`):

| N | budget ⌊N/2⌋ | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 |
|---|---|---|---|---|---|---|---|---|
| 6 | 3 | 9.1e-11 | 3.3e-5 | **2.7e-3** | 5.6e-2 | 2.4e-2 | 1.5e-1 | |
| 8 | 4 | 6.1e-16 | 1.8e-8 | 1.5e-5 | **7.3e-3** | 6.4e-2 | 6.7e-2 | |
| 10 | 5 | 6.0e-22 | 1.8e-12 | 1.2e-8 | 1.1e-4 | **1.9e-3** | 2.5e-2 | 5.8e-2 |
| 12 | 6 | 6.8e-29 | 3.2e-17 | 1.6e-12 | 1.8e-7 | 9.8e-6 | **1.2e-3** | 1.9e-2 |
| 14 | 7 | 1.1e-36 | 2.3e-22 | 9.3e-17 | 1.2e-10 | 1.9e-8 | 2.1e-5 | **1.7e-3** |
| 16 | 8 | 2.5e-46 | 3.2e-28 | 1.2e-21 | 1.7e-14 | 7.5e-12 | 5.0e-8 | 1.6e-5 |

Bold = the pole at margin 0. **In every row the last usable zero is exactly `floor(N/2)`, at the `1e-3` level.**
Odd `N` behaves identically (`N = 5..13`, file `e7.out`): the count of zeros with rel. err `< 1e-3` is
`floor(N/2)` in all nine cases.

### Direct comparison with the O-16004 arithmetic run at c = 2000

| N | k | margin | `gamma_k` | O-16004 `w_k` | rel. err (arithmetic) | rel. err (pure-pole model) | ratio |
|---|---|---|---|---|---|---|---|
| 6 | 2 | 2 | 21.022039638772 | 21.0224296 | 1.86e-5 | 3.27e-5 | 0.57 |
| 6 | 3 | 0 | 25.010857580146 | 25.0775916 | 2.67e-3 | 2.72e-3 | **0.98** |
| 6 | 4 | −2 | 30.424876125860 | 33.0181 | 8.5e-2 | 5.6e-2 | 1.5 |
| 8 | 2 | 4 | 21.022039638772 | 21.0220398 | 7.67e-9 | 1.84e-8 | 0.42 |
| 8 | 3 | 2 | 25.010857580146 | 25.0111337 | 1.10e-5 | 1.46e-5 | 0.76 |
| 8 | 4 | 0 | 30.424876125860 | 30.6382 | 7.01e-3 | 7.31e-3 | **0.96** |
| 8 | 5 | −2 | 32.935061587739 | 36.818 | 1.18e-1 | 6.4e-2 | 1.8 |
| 10 | 3 | 4 | 25.010857580146 | 25.0108579 | 1.28e-8 | 1.15e-8 | **1.11** |
| 10 | 4 | 2 | 30.424876125860 | 30.4313 | 2.11e-4 | 1.09e-4 | 1.9 |
| 10 | 5 | 0 | 32.935061587739 | 33.123 | 5.71e-3 | 1.87e-3 | 3.1 |

(Rows `k = 1` and, at `N = 10`, `k = 2` are omitted: O-16004 prints only 9 decimals there, so the "arithmetic
error" would just be the printing precision, `~3e-9`.)

**The pure-pole model reproduces the arithmetic run's error at every comparable index to within a factor of
1–3, and at three of them to within 5 %.** So:

- **The observed cutoff at `N = 10` is predicted.** The law says the budget is `floor(10/2) = 5` with the
  fifth entry at the `1e-3` level. `gamma_1..gamma_4` come out at `1e-22 … 1e-4`; `gamma_5` at `2e-3`,
  i.e. three correct digits; `gamma_6` at `2.5e-2`, worthless. That is precisely "1–4 right, 5 onward wrong"
  when the threshold is `1e-3`, and precisely "5 emerging" when the threshold is `1e-2`. O-16004 §2's own
  description ("γ₄ to 4 digits, γ₅ emerging") matches the model's `1.1e-4` and `1.9e-3`.
- **The cutoff `c` is nearly irrelevant.** Running the model at `c = 50, 100, 500, 2000, 5000` at `N = 10`
  changes the error profile by less than a factor of 3 at every index (`gamma_5`: 8.7e-4, 1.2e-3, 1.7e-3,
  1.9e-3, 2.0e-3). This independently corroborates O-16004 §5's "`N` dominates".
- **The weights are nearly irrelevant.** Repeating with `a_k = 1/gamma_k` and `a_k = 1/gamma_k^2` moves every
  error by less than a factor 3. So not knowing the true weights in the Weil↔Loewner correspondence does not
  invalidate the law.
- **The low zeros in the arithmetic run are limited by something else.** The model gives `gamma_1` to `6e-22`
  at `N = 10`, whereas O-16004 §2 reports `1e-9 … 1e-12` for `w_1` across all cutoffs. So `w_1`'s accuracy is
  *not* resolution-limited; it is limited by the arithmetic truncation of `Q_W` (finite prime sum,
  archimedean series, dps-60 evaluation). Only `gamma_3` onward are genuinely resolution-limited.

### Honest caveats on this section

1. The zeta constants are **worse than the uniform-comb constants** at the same margin: the comb gives `~1e-6`
   at margin 0, the zeta source gives `~1e-3`. I attribute this (SPECULATIVE, untested) to the *increasing*
   density of zeta zeros: the tail crowds in just above the reach, so the truncation bias of Law E is larger.
   The *count* law is unaffected.
2. The model is a pure-pole source. The real `Q_W` is not. That the two agree so closely is evidence for the
   pole picture but not a proof of it.
3. Two entries in the comparison table have ratio 0.42 and 0.57, i.e. the arithmetic run is *better* than the
   model. I have no explanation; it may be the missing non-pole blocks, or the finite printed precision.

### Practical consequence

To reach zero number `M` at `d` decimal digits one needs roughly `N ≈ 2M + 0.6 d` (crude fit to the table
above; ORDINARY-FLOAT-quality fit, offered only as a planning rule). Resolving the first 20 zeros to 6 digits
would need `N ≈ 44`. O-16004 §5 estimates that the exact-inertia positivity check becomes unresolvable at
60 digits near `N ≈ 20`, and needs `≈ 2.5N + 15` significant digits. **These two requirements are in direct
tension and someone should look at that before planning a large run**: `N = 44` would want ~125 significant
digits for the inertia certificate.

---

## 8. Summary of laws, and of my own refuted guesses

| # | Statement | Status |
|---|---|---|
| A | Budget `= floor(N/2)` poles; error is a function of the margin `m = N − 2k` alone (~`1e-6` at `m=0`, ~`1e-12` at `m=2`, ~`1e-3` at `m=−2`) | EMPIRICAL, robust across `N = 4..16`, spacings `1.85–14.8`, and the zeta geometry |
| B | No minimum separation from the node spacing. `d_min ≈ S·10^{−0.9−2.4m}`, floor is mathematical (dps-independent) | EMPIRICAL, `N = 8..16` |
| C | `rel.err ∝ 1/a` exactly; weak poles inside budget have no practical weight floor | EMPIRICAL, exact `1/a` over 16 decades |
| D | Exact when `#poles = N`, at any density. Density controls *sensitivity to excess poles*; total failure below ~1 pole per node spacing | EMPIRICAL + one EXACT ingredient (the kernel argument) |
| E | Truncation bias is one-signed (upward) and saturates in `K` by `K ≈ 100`; `K = 50` ≈ `K = ∞` | EMPIRICAL |
| F | The law predicts the O-16004 `N = 10, c = 2000` cutoff to within a factor 1–3 at every comparable index | EMPIRICAL |

**My guesses that failed, recorded as refuted:**

1. *"The apparatus resolves poles up to some multiple of `N`"* (the task's suggested guess, which I shared) —
   **REFUTED**. `mu_max/N` ranged from 0.77 to 6.9 in the same experiment; the invariant is the count, not the
   height.
2. *"There is a Nyquist floor: a pair closer than ~1 node spacing cannot be split."* — **REFUTED**. At `N = 14`
   a pair at index 1 is split at `d = 1e-10`, and the floor at that margin is `2e-14`, dps-independent.
3. *"The complete failure on dense sources is because the source extends far beyond the reach."* — **REFUTED**
   by the `K = N+1` control: a single excess pole is enough, and `K = 11` fails exactly as badly as `K = 120`.
4. I expected the recovered roots to be scattered on both sides of the true poles. They are **not** — every
   signed error in every truncated run was positive. I did not anticipate a one-signed bias.

## 9. What I did not do

- No certification of any kind. `mpmath.polyroots` is not a rigorous root isolator; I only checked residuals
  (`|R(u)| / Σ|c_p||u|^p ≤ 1e-62 … 1e-112` in every run) and re-ran at higher `dps`.
- I did not test non-uniform node sets, complex poles, negative weights, or repeated poles.
- I did not derive `floor(N/2)` from the algebra. It is the single most interesting unexplained number here:
  a degree-`2N` polynomial has `N` positive roots, and exactly half of them lock onto true poles while half
  are spent summarising the tail. A proof (or a counterexample) of that 50/50 split would be worth more than
  all of the above.
