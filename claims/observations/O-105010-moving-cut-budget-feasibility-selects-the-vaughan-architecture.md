# O-105010 — Budget feasibility selects the moving-cut (Vaughan-type) architecture; the fixed factor-67 cut was infeasible from birth

Claim ID: `O-105010`
Status: **OBSERVATION / PROPOSED ARCHITECTURE — arithmetic verified (`X-105010`); no positivity theorem claimed**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `T-105000` (A.1/A.1′/A.2), `L-105001`
RH status: **unproved, not addressed**

## 1. The observation

The hazard-budget theorem prices native first-order delivery at
`(1+o(1))/p` of the unit node budget per rough prime, so a scheme whose
smooth/rough cut is **fixed** (rough alphabet `p \ge 67`) faces total price
`\sum_{67 \le p \le Y} 1/p = \log\log Y - O(1) \to \infty`: the practiced
architecture was budget-infeasible from birth — not by bad luck of any one
construction, but by the divergence itself (`T-105000`).

Let the cut **move with the endpoint**: rough primes `p > Y^\theta`. The
price becomes

```
sum_{Y^theta < p <= Y} 1/p  =  log(1/theta) + o(1),
```

so:

* `\theta \ge 1/e` — budget-feasible for all `Y` (marginal at `1/e`);
* `\theta \in (1/e, 1/2)` — feasible **and** every index's rough part has at
  most two prime factors (`k` factors `> Y^\theta` forces `Y^{k\theta} < Y`,
  i.e. `k < 1/\theta`): the recursion tree collapses to **depth 2**, a
  bilinear form in large primes;
* `\theta = 1/2` — feasible at price `\log 2 = 0.6931\ldots`, rough depth
  `\le 1`: the rough part is `1` or a single prime `> \sqrt Y`.

Verified (`X-105010`): at `Y = 10^7`, `\sum_{Y^{1/2}<p\le Y} 1/p = 0.6922`;
over `(Y^{0.368}, Y]`: `0.9930` (marginal); `\theta = 1/3` gives `1.0877 > 1`
(infeasible). A scale-dependent cut with a smooth block plus a bounded-depth
bilinear rough part **is the Vaughan/Heath-Brown decomposition**: the budget
theorem retro-derives the architecture classical analytic number theory
always used, as the unique budget-feasible shape of the admissible class.

**Fingerprint.** The classical Vaughan cut `X^{1/3}` sits just *below* the
feasibility boundary `1/e = 0.3679\ldots`: positive-scheme consumers demand
a strictly coarser cut than raw Vaughan needs. The window `(1/e, 1/2]` is a
new, program-specific selection principle with no classical counterpart.

## 2. What the demand becomes under the moving cut

1. **Smooth block** (indices `Y^\theta`-smooth): no longer the fixed
   66-fibre compact Hall problem — a growing Hall/Lorenz family on smooth
   numbers. At `\theta = 1/2` the block has Dickman density
   `\rho(2) = 1 - \log 2 = 0.30685\ldots` (exact for `1 \le u \le 2`).
   The compact moat `H_t(x) > 7/20` (`L-99020`/`L-99451`) must be replaced
   by a uniform-in-`\theta` smooth-fibre statement — a concrete, finite-at-
   each-scale question, and the natural import point for smooth-number
   technology (Dickman/de Bruijn, smooth equidistribution) that no branch
   has used.
2. **Rough part, depth `\le 2`**: the open demand migrates into exactly one
   object — a Type-II bilinear form in primes `p, q > Y^\theta` with the
   SHARP-kernel weights. This is where the live Vaughan lane connects:
   `L-102000` (positive cubic B-spline compactifier), `L-102009` (ratio-four
   factorization `K_1 = A_- * A_+`), `L-102010` (positive half-divisor
   square root) on `research/gpt56-sol/102000-parabolic-bessel-vaughan-
   correction` are precisely compact-kernel equipment for such bilinear
   objects.
3. **Depth accounting is budget-certified**: first-order (single large
   prime) currents cost `\log(1/\theta) < 1`; depth-2 mass is even-channel
   (two swaps), sign-free.

## 3. Honesty

* This does **not** evade the calibration/deficit fences or `T-105000`
  itself: a power-strength Type-II bound for a single Möbius-type form is
  the classical wall, and nothing here proves it.
* What changes is the **shape** of the residual demand: from an
  infinite-depth conserving-scheme demand — proved impossible inside the
  axioms (`T-105000`/`R-105000`) — to (i) a depth-`\le 2` bilinear estimate
  where a century of technology plus the newest in-repo kernels apply, and
  (ii) a growing smooth-block Hall family, a new finite-at-each-scale
  frontier. By the four-criteria test for reformulations (toolkit import,
  progress gradient, structural exposure, deformation family): imports
  smooth-number and bilinear technology; `\theta` is a continuous dial; the
  feasibility window `(1/e, 1/2]` is new structure.
* Proposed next steps, in order: (a) restate the SHARP source with the
  moving cut and prove the depth-2 collapse in the typed-coordinate
  formalism; (b) compute the smooth-fibre moat analogue at small scales and
  look for the uniform threshold; (c) write the exact Type-II object and
  hand it to the 102000 lane.

RH remains unproved; no step above claims otherwise.
