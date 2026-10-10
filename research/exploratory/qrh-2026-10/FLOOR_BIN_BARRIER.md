# The floor-bin barrier, and whether cancellation across rows can beat it

```text
Status: PROPOSED (mechanism analysis; conditional statements explicitly labeled)
Scope: exponent architecture of an external unreviewed manuscript; no RH claim
Exact sources or dependencies:
  [OAI] OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", 30 Sep 2026
        (sha256 in scripts/SOURCES.txt; text extraction used for line references), Sections 7.2
        (Euler region (7.14)), 8 (Lemma 8.1, floor bin), 10.4-10.6 (Lemmas 10.3, 10.4, eq. (10.15)),
        19-20 (Lemma 20.1, eq. (20.4), floor value (20.5)). Treated as untrusted external data.
  scripts/threshold_calculus.py (team exponent model of Part II), scripts/barrier_lp.py (coordinator
        LP, 167/192 and 13/15 certificates); prior notes: branch claude/openai-math-riemann-analysis-w5copg
        standalone/2026-10-07-openai-quasi-rh/README.md Sec. 6a; PR 910 (ref pr910)
        standalone/2026-10-10-quasi-riemann-height-descent/{UPSTREAM_HEIGHT_AND_MOMENTS.md Sec. 6,
        GEOMETRY_ENVELOPE_LIMIT.md}.
  Literature (cited, not re-verified here): see Sec. 6.
What was actually run:
  scripts/floor_theta.py  - wrapper around threshold_calculus.optimise; R_floor -> 1 - theta (or every
                            bin R -> max(R - theta, R/2)); Nelder-Mead over (lx, ly, ell); 4 processes.
  scripts/floor_lp.py     - exact-rational LP certificates (extends barrier_lp.py) for floor / DH /
                            all-bin savings, paper and "optimal" low-side energy, a0 = 51/100 and 1/2,
                            with an a-posteriori check of every bin delta in (delta0, 5/6].
  Literature lookups (WebSearch/WebFetch) for the ratios-conjecture and cubic/n-th order inputs.
Smallest remaining gap: no rigorous saving theta > 0 for the signed floor-bin sum is known; and
  below 13/15 the architecture needs, simultaneously, an improved low-side energy bound AND a signed
  (ratios-type) saving in EVERY near-critical bin, not only the floor.
```

RH remains unproved, and nothing below bears on the critical line. Everything here is a statement
about one external, unreviewed proof architecture, modelled through the stated output exponents of
its lemmas. "sigma0" is the zero-free boundary that architecture would deliver.

## 0. Bottom line

1. **The floor bin is a thin barrier.** With density-hypothesis-quality counts (DH) for every
   witnessed bin, the floor bin caps the architecture at exactly `167/192 = 0.869792`. The low side
   (the manuscript's energy lemma) caps it at `13/15 = 0.866667` for every geometry. The floor-bin
   barrier is therefore worth at most `167/192 - 13/15 = 1/320`.
2. **A floor saving theta is equivalent to lowering the detector floor.** At the optimal geometry
   `lx = ly`, the floor constraint depends on `tau = theta - delta0` only (Sec. 1.5):
   `sigma_FB(tau) = (13 - 18 tau)/(15 - 18 tau)`. A saving `theta = delta0 = 1/50` therefore does
   exactly what moving the floor from `51/100` to `1/2` does. Lowering the floor looks much cheaper
   than proving cancellation (Sec. 4.3; unverified).
3. **With the manuscript's own counts, floor cancellation gains nothing.** `sigma0 = 0.874961` for
   every theta, because the binding bins are the witnessed ones near `delta ~ 0.39` (PR 910's
   envelope limit `0.874957`). With DH counts, `sigma0(theta) = max(13/15, (167 - 225 theta)/(192 - 225 theta))`,
   so `13/15` is reached at `theta = 1/50` and nothing further is gained.
4. **Below 13/15 two barriers must move together.** At `(lx, ly, ell) = (2/5, 2/5, 1/5)` the
   low side and the near-critical band (bins just above the floor, counted at density `U^{1-delta}`)
   both sit at `13/15`. A signed saving theta in **every** bin (on top of DH counts), combined with
   the idealized low-side energy, gives `sigma0 = max(5/6, (167 - 225 theta)/(192 - 225 theta))`.
   This is `5/6` from `theta = 14/75` on. Below `5/6` one must leave `h <= 1`, which is the w5copg
   "h = 3/2" regime.
5. **Rigour.** Heuristically, square-root cancellation over rows is expected for the *complete*
   family: the twist `xi(u)` kills the diagonal, and Gauss-sum bias is expected to be lower order. Rigorously
   nothing is available. Large-sieve inputs give `theta = 0`, by a marginal-information no-gain
   argument (Sec. 3.3). Known ratios theorems need GRH for the family. The floor sum is over a
   zero-defined subset, with a reciprocal evaluated about `1/100` from the critical line.

## 1. Re-deriving the floor-bin constraint

### 1.1 Inputs from [OAI]

* **Common exponent (10.15), Lemma 10.4.** For a fixed bin `(i, a)`, with `delta = 2a - 1`, row norm `U = Z^d`,
  row-sum exponent `R` and `g = q ell` (slot amplitude mean `q`), the retained central-contour
  contribution relative to `Z^{C(sigma0)}` has exponent

  `E_{sigma0}(d; R, g) = a - sigma0 + h(z0 - 1/6) - a ly - ell/2 + g + d (R + delta/2 - z0)`,

  where `h = 1 - lx + ell` and `z0 = 17/50`. Relative to `C(beta*)`, replace `sigma0` by `beta*`.
  This is what must be negative (Lemma 10.4 proof; Sec. 20.4 subtracts `Delta = C(beta*) - C(7/8)`).
* **Floor bin.** `a0 = 51/100`, `delta0 = 1/50`. It has no zero witness. Its count is the trivial
  `#B << U`, i.e. `R = 1` ([OAI] l. 4076-4077, 4250-4252, Sec. 10.5 "For the floor this is the direct
  count O_eta(U) ... it uses no witness"). The amplitude bound `q <= delta0/2` gives (20.5).
* **Why 51/100.** The Euler region (7.14) for the correction `H_{eta,u}` requires `Re s >= 51/100`.
  The binding local exponent is `3/2 - 3 x_r <= -3/100` at primes `p | u` (proof of (7.14), l. ~3335).

### 1.2 The floor exponent at the top dyad

Take `R = 1`, `a = a0`, `q = delta0/2` (that is, `x = 1/2`). The `d`-slope `1 + delta0/2 - z0 = 67/100` is positive, so the worst dyad is
`d = h`. There the `z0` terms cancel exactly:

  `F_floor = a0 (1 - ly) - beta* + h (5/6 + delta0/2) - ell/2 + delta0 ell/2`.

Since `beta* > sigma0` can be arbitrarily close to `sigma0`, the floor forces

  **(FB)**  `sigma0 >= a0 (1 - ly) + h (5/6 + delta0/2) - ell/2 + delta0 ell/2`.

*Check against [OAI].* At the paper geometry `(17/48, 23/48, 1/6)`, `h = 13/16`, the right side
minus `7/8` is `-7/1200`. This is exactly (20.5) (`C0 + 3 delta0/4 = -7/1200`).

### 1.3 Model confirmation (counts = 'DH')

`threshold_calculus.optimise(11/12, Inputs(counts='DH'))` gives `sigma0 = 0.869838` (stored
`results/D_DHcounts.json`; the rerun with warm starts gives `0.869796`). Its arg-max is the floor:
`(delta, x, d, R) = (0.02, 1/2, h, 1)`. The exact LP (`barrier_lp.py`) gives `167/192` at
`(lx, ly, ell) = (13/32, 13/32, 3/16)`, `h = 25/32`. At that point every DH bin sits
`h delta0 = 1/64` below the floor, and the DH band is *flat* in delta when `lx = ly`. With `R = 1 - delta`
at `d = h`, the delta-coefficient of the exponent is `(lx - ly)/2`.

### 1.4 The near-critical band

The same computation with `R = 1 - delta` (DH) gives, at `d = h`,
`F_DH(delta) = (1-ly)/2 + 5h/6 - ell/2 - beta* + delta (lx - ly)/2 + (x - 1/2) delta ell`.
For `lx <= ly` this is maximal as `delta -> delta0+`. So the bins *just above* the floor are as
dangerous as the floor once the floor is repaired: the binding object is the whole
**near-critical band** of rows whose rightmost zero lies just right of the floor. These rows are
almost all rows, and each costs the reflected-numerator excess `U^{delta/2}` and `Z^{a(1-ly)}`.
Better counts of the form `R = 1 - kappa delta` cannot help here, since `R -> 1` as `delta -> 0`.
This is the coordinator's "167/192 for ANY row counting".

### 1.5 A unified formula: floor saving = floor lowering

Insert `R_floor = 1 - theta` in (FB) at `lx = ly = L`. Then
`a0(1-ly) + h(delta0/2 - theta) + delta0 ell/2 = (1-L)/2 + h (delta0 - theta)`,
because `(1 - L)/2 + h/2 + ell/2 = h`. So the floor constraint depends only on `tau := theta - delta0`.
Solving the floor row against the two low-side branches `E = M` and `E = 2M + ell - 1` gives the exact LP value

  `sigma_FB(tau) = (13 - 18 tau)/(15 - 18 tau)`

* `tau = -1/50` (no saving, a0 = 51/100): `167/192`;
* `tau = 0` (`theta = 1/50`, or a0 = 1/2 with no saving): `13/15`;
* `tau = 1/6`: `5/6`.

(Equivalently, `(167 - 225 theta)/(192 - 225 theta)` at `a0 = 51/100`.) The paper's third energy
branch `(2M + 1 + 3 ell)/4` truncates this at `13/15`.

## 2. sigma0(theta)

### 2.1 Full numerical model (`scripts/floor_theta.py`)

Floor-only means `R_floor = 1 - theta`. All bins means every bin gets `R -> max(R - theta, R/2)`
(the cap is square-root cancellation inside the bin). The previous boundary is `beta_prev = 11/12`
(paper counts with `beta_prev = 7/8` agree to `1e-6`). The optimiser keeps a `2e-5` penalty slack,
so model values sit about `4e-6` above the exact LP.

| theta | paper counts, floor only | paper counts, all bins | DH counts, floor only | DH counts, all bins | DH + optimal energy, floor only | DH + optimal energy, all bins |
|---|---|---|---|---|---|---|
| 0    | 0.874961 | 0.874961 | 0.869796 | 0.869796 | 0.869796 | 0.869796 |
| 0.05 | 0.874961 | 0.866737 | 0.866671 | 0.866667 | 0.866671 | 0.861692 |
| 0.10 | 0.874961 | 0.866667 | 0.866671 | 0.866667 | 0.866671 | 0.852544 |
| 0.25 | 0.874961 | 0.866667 | 0.866671 | 0.866667 | 0.866671 | 0.836341 |
| 0.50 | 0.874961 | 0.866667 | 0.866671 | 0.866667 | 0.866671 | 0.836341 |

Binding objects:
* Paper counts, floor only: the witnessed bins at `delta ~ 0.389`, `x = 1/2`, `d = h`. The floor is
  never binding.
* Paper counts, all bins: `13/15` from `theta ~ 0.1` on, set by the low side.
* DH counts: `167/192` at `theta = 0`. Then the bins just above the floor (`delta = 0.023`) and the
  low side tie at `13/15`, at `(2/5, 2/5, 1/5)`.

Lowering the floor without any saving (DH counts) gives `0.868252` at `delta0 = 1/100` and
`0.866990` at `delta0 = 1/500`. These match `(13 + 18 delta0)/(15 + 18 delta0)`. With paper counts
it changes nothing (`0.874958`, `0.874957`).

Optimal-energy columns:
* The all-bins column follows the LP formula `(167 - 225 theta)/(192 - 225 theta)` (`0.861687`,
  `0.852507`). Its plateau is `0.836341` rather than `5/6`: the model keeps the strict margins
  `lx - ell > 0.01`, `ly - ell > 0.01`, and the small-rows constraint `h(z0 - 1/6) - ly/2 < 0`
  binds there.
* With *paper* counts, optimal energy and all-bin savings, the sweep gives `0.866737` (theta = 0.05)
  and `0.857257` (theta = 0.10). For `theta >= 0.25` the optimiser's geometry fails the fine-grid
  check (sup F = +1.5e-3 at a bin `delta ~ 0.68` near `2 beta* - 1`). That entry, about `0.838`, is
  **not certified**.

### 2.2 Exact LP (`scripts/floor_lp.py`; DH counts for witnessed bins; all values certified)

| theta | a0=51/100, paper energy, floor only | a0=51/100, optimal energy, floor only (+DH bins) | a0=51/100, optimal energy, all bins | a0=1/2, optimal energy, all bins |
|---|---|---|---|---|
| 0    | 167/192 = 0.869792 | 167/192 | 167/192 | 13/15 = 0.866667 |
| 0.01 | 659/759 = 0.868248 | 659/759 | 659/759 | 641/741 = 0.865047 |
| 0.02 | 13/15 | 13/15 | 13/15 | 158/183 = 0.863388 |
| 0.05 | 13/15 | 13/15 | 623/723 = 0.861687 | 121/141 = 0.858156 |
| 0.10 | 13/15 | 13/15 | 289/339 = 0.852507 | 28/33 = 0.848485 |
| 0.25 | 13/15 | 13/15 | 5/6 | 5/6 |
| 0.50 | 13/15 | 13/15 | 5/6 | 5/6 |

"Optimal energy" is `threshold_calculus`'s `energy='optimal'`: only the large-sieve diagonal
branches `E = M`, `E = 2M + ell - 1`, plus `M >= 2 ell`, as in `barrier_lp.py` Barrier 3. It is a
*hypothetical* strengthening of [OAI] Lemma 14.3.

A "level" hypothesis gives **no** gain below `13/15` even with optimal energy (LP, all theta up to
1/4). This is the hypothesis that bins with `delta < theta` cancel down to `U^{1-theta}` while bins
with `delta >= theta` keep `R = 1 - delta`. The DH bins at `delta ~ theta` then have the same `R` as
the floor but larger `a` and numerator cost. **The saving must be in addition to DH counts in every
bin.**

### 2.3 Which dyads and which bins actually need the saving

* *Dyads.* At the solution the floor exponent is `0` at `d = h`, and its slope is `67/100 - theta`.
  The trivial count suffices for `d < h(1 - 100 theta/67)`. So the hypothesis is needed only on the
  top dyads `d in [h(1 - 100 theta/67), h + zeta]`: `d >= 0.970 h` for `theta = 1/50`, and
  `d >= 0.721 h` for `theta = 14/75`. Here `U ~ Z^{0.78}` to `Z^{0.8}` (`h = 25/32` to `4/5`), the full Poisson length.
* *Bins (sensitivity, LP exploration).* With counts `R = 1 - delta` the extra saving is needed in
  essentially all bins, because the band is flat at `lx = ly`. With counts `R = 1 - (3/2) delta`
  (the best PR 910's (6.7) could give at detector length `t = 3/2`), floor-only cancellation gives
  `0.864499` with optimal energy. The full formula is then reached once bins with `delta <~ 2 theta`
  also cancel. Only with such counts is the needed hypothesis genuinely "near-critical".

## 3. What the floor-bin sum is, and what cancellation is plausible

### 3.1 The object

For a dyad `U = Z^d`, the floor index `i`, and a retained point `(s, w, z)` on (10.11)
(`Re s = a0 + 16e`, `Re w = 1 - a0 - 6e`, `Re z = 17/50`, heights `<= c T1`, `T1 = Z^tau`), the sum is

  `S_floor(U; s, w, z) = sum_{u in B_floor(i, U)} xi(u) q_u^{-z} L^S(w, chi_.(u)) H_{eta,u,Z}(s, w, z) / L^S(s, eta chi_.(u))`.

* `u` ranges over sixth-power-free elements, unit factor included, with `(u, S) = 1` and `q_u ~ U`.
* `chi_.(u)` is the Hecke character `n -> chi_n(u)` (the sextic Kummer symbol, Lemma 4.1).
* `xi` is a fixed residue character mod `b*` (the product of the primes in `S`), **nonprincipal at
  every prime of S** and of order dividing 6 ([OAI] l. 2698-2702).
* `B_floor(i, U)` is the set of rows whose presentations in `X_u` have no zero with
  `Re >= 51/100 + 2e`, `|Im| <= 3(i+1) T1` (Lemma 8.1). It is fixed before any contour move
  (Lemma 10.3).
* In Part II, `H_{eta,u,Z}` carries the prime-slot factors. (10.13) is applied to pointwise amplitude
  subsets `B_{lambda,nu}(s, w, z)` defined by the sizes of those factors (Sec. 19.1, Lemma 20.1).

The trivial bound is `|S_floor| << U^{1 + delta0/2 - z0 + eps} Z^{ell(z0-1/2) + delta0 ell/2 + eps}`.
The factor `U^{delta0/2}` is sharp pointwise: by the functional equation,
`|L(1 - a0 - 6e + it)| ~ U^{a0 - 1/2 + 6e} |L(a0 + 6e - it)|`.

### 3.2 Heuristic expectation (ratios recipe; HEURISTIC, not a theorem)

Expand formally `L(w, chi_.(u)) = sum_n chi_n(u) N(n)^{-w}` (two-term approximate functional
equation) and `1/L(s, eta chi_.(u)) = sum_m mu(m) eta(m) chi_m(u) N(m)^{-s}`. Then average over `u`
as in Conrey-Farmer-Zirnbauer.

* **No diagonal.** For each `n, m` (prime to `S`), `u -> xi(u) chi_{nm}(u)` is a character modulo
  `b* nm` whose `b*`-component is `xi`, which is nonprincipal. So it is *never* principal, and the
  recipe's "first-part" main term vanishes identically. This is unlike the untwisted family, where
  `nm = sixth power` gives a main term `~ U` that would forbid any saving beyond `U^{delta0/2}`.
* **Dual part.** The root number of `chi_.(u)` is a normalized sextic Gauss sum attached to `u`.
  Averages of `xi(u) g~_6(u)` (twisted) are Fourier coefficients of metaplectic Eisenstein series on
  the 6-fold cover (Kubota, Patterson). For prime-power order `n` the bias has size `U^{1/2 + 1/n}`
  in the normalized variable (cubic: `5/6`, Heath-Brown-Patterson; Dunn-Radziwill). For `n = 6 = 2*3`
  the literature found here flags the general rule as *not* matching (Ma 2026, as summarised in
  search results; sharpness conjectured only for prime-power orders). The sextic exponent is not
  established in this note. Granting the
  `1/2 + 1/6 = 2/3` rule, the secondary term would be at most `U^{2/3 + delta0/2}`, i.e. `theta >= 1/3`.
  It is also a polar term in `z` that could in principle be extracted.
* **Off-diagonal.** Square-root size, `theta = 1/2 - O(delta0)`.

So for the *complete* family, heuristics predict `theta` between about `1/3` and `1/2`. That is far more than
the `1/50` needed to reach `13/15`, and more than the `14/75` needed (with idealized energy) to
reach `5/6`. The difficulty is entirely in rigour and in the subset `B_floor`.

### 3.3 Rigorous inputs, and what they actually give

| Input | What it controls | Floor-bin theta it yields |
|---|---|---|
| Large sieve: Heath-Brown cubic `(M+N+(MN)^{2/3})`; Blomer-Goldmakher-Louvel n-th order; Goldmakher-Louvel quadratic Hecke; [OAI]'s sextic large sieve | `sum_u |sum_n a_n chi_n(u)|^2` (orthogonality) | **0**. By duality, `sum_u b_u L(w, chi_u) << U^{1 + delta0/2 + eps}` for arbitrary `|b_u| <= 1`, which is trivial |
| Numerator first moments via double Dirichlet series (Friedberg-Hoffstein-Lieman 2003; BGL 2012 subconvexity; cubic: Baier-Young, Luo, David-de Faveri-Dunn-Stucky 2024) | `sum_u xi(u) L(w, chi_u) q_u^{-z} (nice weights)`; with nonprincipal `xi` no main term, so a power saving is plausible or provable | Not applicable: the weight `1/L(s, eta chi_u)` is not a "nice" weight |
| Mollifier / Dirichlet-polynomial approximation of `1/L` on floor rows | error `V^{-eta}` at distance `eta` from the nearest zeros | Floor rows have all zeros (`|Im| <~ T1`) in `|Re rho - 1/2| <= 1/100 + 2e`, by the floor condition and the conjugate functional equation, and they have `>> T1 log U` such zeros. So `eta <= 1/50 + 18e < 1/25`, and relative error `U^{-theta}` needs length `V ~ U^{theta/eta} >= U^{25 theta}`, far beyond any twisted-moment or large-sieve range: **0** |
| Ratios conjecture theorems via MDS: Cech (quadratic; arXiv 2110.04409); Gao-Zhao (cubic, prime moduli, arXiv 2311.08626; quadratic over Q(i)); Bui-Florea-Keating (function fields) | `sum L(1/2+alpha)/L(1/2+beta)` with one shift each | **All conditional on GRH for the family.** Under the contradiction hypothesis `beta* > sigma0`, the full-family ratio series has polar divisors at zeros of non-floor rows, so its continuation past `beta*` is the statement being proved |
| Pointwise bound `|1/L| << U^eps` on floor rows (Lemma 8.1, Borel-Caratheodory) | size only | **0** (no averageable structure) |

**No-gain remark (PROPOSED, elementary; the signed analogue of PR 910 Sec. 6.2).** Suppose an
argument uses only:
* the pointwise bound `|H/L(s, eta chi_u)| <= U^eps` on `B_floor`;
* any family moment bounds `sum_{u ~ U} |L(w, chi_u)|^{2k} << U^{1 + k delta0 + eps}`;
* the lower bound `sum_u |L(w, chi_u)| >> U^{1 + delta0/2 - eps}` (true if the family's first
  absolute moment at `1 - w` is `>> U^{1-eps}`).

Then that argument cannot give any `theta > eps`. The weights `b_u = U^{-eps} conj(L(w, chi_u))/|L(w, chi_u)|`
satisfy every listed constraint and make the signed sum as large as the absolute sum. A saving must
therefore use **joint** arithmetic information about the numerator `L(w, chi_.(u))` and the reciprocal
`1/L(s, eta chi_.(u))` on the specific zero-defined set. That is a restricted ratios statement.

### 3.4 Obstacles (task item 3)

1. **The reciprocal sits next to zeros.** On the floor contour, `Re s - 1/2 = 1/100 + 16e`. Every
   floor row has `>> T1 log U` zeros in the strip `|Re rho - 1/2| <= 1/100 + 2e` inside the
   retained box, so the nearest zero is at distance `< 1/25`. Away from them,
   `1/L(s, eta chi_u)` is controlled only by a non-linear (Borel-Caratheodory) argument. It has no
   short Dirichlet-polynomial model, which is what large sieves, moments and MDS consume.
2. **Bins are fixed before contour moves.** `B_floor` is defined by the *absence* of zeros. Completing
   it to the full family fails: the non-floor rows cannot be placed on the floor contour, because
   `1/L` has poles to its right and is unbounded near zeros. For arbitrary subsets of size `~U`,
   signed cancellation is false in general (take the rows where the summand has a fixed phase). A
   hypothesis must therefore assert that the zero-defined subset is *unbiased* with respect to the
   phase of the ratio. That is a joint zero/value statement.
3. **Pointwise size subsets in Part II.** The amplitude sets `B_{lambda,nu}(s, w, z)` are defined
   by sizes, pointwise in the contour variables. A signed hypothesis has to be stated for the
   undecomposed `H` (with the worst amplitude `g = delta0 ell/2`) or for an integrated form.
4. **Uniformity.** Exponents must be uniform in:
   * the target `eta`, since the denominator family `eta chi_.(u)` moves with it; constants may depend on `eta`;
   * the heights `|Im| <= c T1`;
   * the bin index `i`;
   * all `d` in the top range of Sec. 2.3.

   The hypothesis may be stated after integration against the Mellin weight `W`, which would allow
   hybrid averaging in `Im s, Im w, Im z`. That is the most natural weakening.
5. **The floor alone is not the obstruction below 13/15.** Sec. 1.4 and 2.2 show that the
   near-critical band and the low side are co-binding there. Floor cancellation without an
   all-bin saving and a better low side buys at most `1/320`.

## 4. Proposed conditional statements

Throughout, **(ARCH)** is the hypothesis that the stated outputs of [OAI]'s Part II lemmas hold at
the geometry used, as transcribed in `threshold_calculus.py`: low-side energy (Lemma 14.3), Gram
bound (Prop. 15.2), contour Lemmas 10.3/10.4, the principal-row Lemma 10.5, and small/large rows
(Sec. 20.3). For geometries other than the manuscript's this is an extrapolation, with the
lemma-range obligations listed in `THRESHOLD_CALCULUS.md`. Everything below is PROPOSED and
CONDITIONAL. None of it is a theorem of this repository.

**Hypothesis FB(theta) (signed floor-bin bound).** For every primitive target `eta`, every floor
bin `(i, 51/100)` of Lemma 8.1, every dyad `U = Z^d` with `d in [h(1 - 100 theta/67), h + zeta]`, and
uniformly at every retained point of (10.11):

  `|S_floor(U; s, w, z)| <<_eta U^{1 - theta + delta0/2 - z0 + eps} Z^{ell(z0 - 1/2) + delta0 ell/2 + eps} (1 + T1)^{A_eta}`,

where `S_floor` is the signed sum of Sec. 3.1 with the full correction `H`. The integrated version
(against `W` over the retained box) suffices.

**Hypothesis DH-rows.** Every witnessed bin (`delta > delta0`) at the top dyads has
`#B << U^{1 - delta + eps}`. This is a density-hypothesis statement for the twisted sextic
family, uniform in bins; unproved. PR 910's (6.6) would give `1 - delta(r+m)` on its range.

**Hypothesis NC(theta) (near-critical signed saving).** For every bin `(i, a)`, including the
floor, the signed bin sum at those dyads is
`<< U^{R_DH(delta) - theta + delta/2 - z0 + eps} Z^{...}`, with `R_DH(delta0) = 1` and
`R_DH(delta) = 1 - delta` otherwise. This is DH counts plus an extra signed saving theta in every bin.

**Hypothesis E\*.** The low-side energy satisfies the large-sieve-diagonal bound
`max(M, 2M + ell - 1)` (`energy='optimal'`).

**Proposition 4.1 (PROPOSED; conditional on ARCH and the named hypotheses).** The architecture
yields zero-freeness of every finite-order Hecke L-function over `Q(sqrt(-3))`, hence of every
Dirichlet L-function, in `Re s > sigma(X)`, where:

| X | sigma(X) | attained at |
|---|---|---|
| FB(theta), manuscript counts | `0.874957...` for all theta (no gain) | `(0.355, 0.478, 0.167)` |
| DH-rows + FB(theta) | `max(13/15, (167 - 225 theta)/(192 - 225 theta))`; `= 13/15` for `theta >= 1/50` | `(2/5, 2/5, 1/5)` |
| DH-rows with the floor moved to `a0 = 1/2 + eps` (no FB) | `13/15 + O(eps)` | `(2/5, 2/5, 1/5)` |
| NC(theta) (no E\*) | `max(13/15, ...)`, same as row 2 | |
| NC(theta) + E\* | `max(5/6, (167 - 225 theta)/(192 - 225 theta))`; `= 5/6` for `theta >= 14/75` | `(1/3, 1/3, 1/3)` at `5/6` (LP; the numerical model with strict margins gives `0.836341` at `(0.338, 0.341, 0.321)`, where the small-rows constraint of Sec. 20.3 binds) |

The `sigma(X)` entries come from exact LP certificates (`floor_lp.py`) and the full model
(`floor_theta.py`). Rows 2 and 5 are the honest form of "if cancellation across rows holds, the
boundary is sigma(theta)".

### 4.1 How hard is X?

* **FB(theta) for any theta > 0** is a restricted-ratios statement. It asks for cancellation in a
  sum of `L(w)/L(s)` with the reciprocal `1/100` from the critical line, over a subset defined by
  zero locations, unconditionally, under a contradiction hypothesis that allows zeros up to `beta*`.
  Every known ratios theorem (Cech; Gao-Zhao) assumes GRH for the family, under which the
  question is moot. By Sec. 3.3 the large-sieve/moment toolbox gives `theta = 0`. **Heuristically
  true (theta ~ 1/3-1/2); rigorously out of reach; arguably no easier than the zero-free region it
  would improve.**
* **FB alone is worthless with the manuscript's counts** (row 1). It needs DH-rows, which is itself
  beyond current technology for this family.
* **The cheapest route to the same 1/320 is not cancellation.** It is to lower the detector floor
  (Sec. 4.3).
* **NC(14/75) + E\*** combines two independent breakthroughs: ratios-type cancellation in every bin
  at the full Poisson length, and a low-side energy bound without the reflected-kernel branch. The
  payoff is at most `0.875 -> 0.8333`.

### 4.2 Relation to prior work

* **w5copg Sec. 6a.** That note lists "DH for every row: 13/15 (b=0, ell=1/5)". This agrees with
  the present `13/15` only after the floor is repaired. With the manuscript's floor `51/100`, DH
  gives `167/192` (Sec. 1.3); their model evidently had no floor excess. Their "Drop energy and
  dual-length constraints: floor 5/6" numerically coincides with our `NC + E*` plateau. Ours keeps
  `ell <= lx <= ly` and `M >= 2 ell`, so the two constraint sets differ.

  Their "reach 3/4 needs h = 3/2 with cross-row cancellation" is consistent with (FB) extended
  formally to `h > 1`, in the `a0 = 1/2` form at `lx = ly`:
  `sigma >= (1 - ly)/2 + h(5/6 - tau) - ell/2`.
  At `h = 3/2` and `sigma = 3/4` this needs a net saving `tau >= (2 - ly - ell)/3`, which is
  `>= 1/3` when `ly + ell <= 1`. That is beyond the heuristic Gauss-bias level and close to square
  root. This is a high-side necessary condition only; the low side at `h > 1` is not modelled.
  Within `h <= 1`, cross-row cancellation can take the architecture at most to `5/6`, and only
  together with E\*.
* **PR 910.** Its (6.6) `sum_u |M_u S_u(t_u)|^2 << U^{1+eps}` is an *absolute-value* joint moment.
  It improves **counts** of witnessed bins, to `R <= 1 - delta(r+m)`. By Sec. 1.4 it cannot touch
  the floor (no witness) or the near-floor bins (`R -> 1` as `delta -> delta0`). So its best possible
  effect is `0.874957` (its GEOMETRY_ENVELOPE_LIMIT) `-> 167/192`.

  FB/NC are the complementary *signed* inputs. Our no-gain remark (Sec. 3.3) is the signed analogue
  of its Sec. 6.2: marginal information cannot beat the separate bounds. If (6.6) held with
  `r + m = 3/2`, the extra signed saving would be needed only for `delta <~ 2 theta` (Sec. 2.3), a
  genuinely near-critical hypothesis.
* **Coordinator LP (`barrier_lp.py`).** Its values are `167/192` for any counts at `a0 = 51/100`,
  `13/15` at `a0 -> 1/2`, and `13/15` even with perfect energy and GLH row by row. These are
  reproduced: they are the `tau = -1/50` and `tau = 0` points of `sigma_FB(tau)`. The floor-only
  saving reproduces the `a0 -> 1/2` effect exactly and nothing more.

  The coordinator's low-side bilinear saving (`13/15 - 4 theta_low/5`) is the low-side counterpart
  of our high-side theta. By Sec. 0 item 4, either one alone is blocked at `13/15` by the other
  barrier. A joint optimisation of `(theta, theta_low)` was not run.

### 4.3 The cheap alternative: lowering the detector floor (PROPOSED observation, unverified)

`a0 = 51/100` is set by (7.14): at `p | u` the local exponent `3/2 - 3 x_r` must be `<= -3/100`. For
`x_r = 1/2 + eps` the `p | u` local factors are still `O_eps(1)`. Their product over the `omega(u)`
primes dividing `u` is `exp(O(omega(u))) = q_u^{o(1)}`, which is all that `H << q_u^eps` requires.
The `p not | u` exponents (`4 - 6x_r - 6z_r <= -1.04`, `1 - x_r - w_r - 6 z_r`) stay negative.

If the rest of the chain is uniform for a floor `delta0 = 2 eps` fixed before `Z`, this gives the
same `13/15 + O(eps)` (with DH-rows) as FB(1/50), without any cancellation. The rest of the chain
means Lemma 8.1's detector, the saturation losses "uniform because delta >= 1/50", and
`Re(s + w) >= 1 + eps0`. This is the first thing to check before investing in a ratios-type
hypothesis for the floor.

## 5. Reproduction

```text
cd research/exploratory/qrh-2026-10/scripts
python3 floor_lp.py                       # exact LP tables (seconds)
python3 floor_theta.py [/path/out.json]   # full-model sweep, 4 processes (~5 min)
python3 barrier_lp.py                     # coordinator certificates 13/15, 167/192
```

## 6. Literature consulted (bibliographic data from searches; statements as summarised there)

* J. Conrey, D. Farmer, M. Zirnbauer, *Autocorrelation of ratios of L-functions* (2008) — ratios recipe.
* M. Čech, *The ratios conjecture for real Dirichlet characters and multiple Dirichlet series*,
  arXiv:2110.04409 — one-shift ratios via MDS, **conditional on GRH**.
* P. Gao, L. Zhao, *Ratios conjecture of cubic L-functions of prime moduli*, arXiv:2311.08626
  (GRH); *Ratios conjecture for quadratic Hecke L-functions in the Gaussian field*, arXiv:2210.08840 (GRH).
* C. David, A. de Faveri, A. Dunn, J. Stucky, *Non-vanishing for cubic Hecke L-functions*,
  arXiv:2410.03048 — mollified first and second moments (unconditional), using Patterson's cubic
  theta coefficients and Heath-Brown's cubic large sieve.
* A. Dunn, M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, Ann. of Math. 200
  (2024) — includes sharpness of Heath-Brown's cubic large sieve under GRH.
* S. Friedberg, J. Hoffstein, D. Lieman, *Double Dirichlet series and the n-th order twists of
  Hecke L-series*, Math. Ann. 327 (2003) 315–338.
* V. Blomer, L. Goldmakher, B. Louvel, *L-functions with n-th order twists*, arXiv:1112.1650 —
  uniform subconvexity for the FHL double series; large sieve for n-th order characters.
* L. Goldmakher, B. Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642.
* S. Baier, M. Young, *Moments of cubic Dirichlet L-functions* (first moment, cubic family over Q).
* Z. Y. Ma, *Optimal homological vanishing: cancellation of character sums and Patterson's
  conjecture over F_q[t]*, arXiv:2606.26440 (2026; abstract only) — bias bounds for higher-order
  Gauss sums; sharpness conjectured for prime-power orders (relevant caveat for order 6).
