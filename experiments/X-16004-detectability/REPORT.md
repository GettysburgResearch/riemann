# A detectability law for an off-line zero in a finite Loewner / Weil form

**Status: exploratory measurement. Nothing here is certified.** Every number below is
HIGH-PRECISION FLOAT (mpmath, dps stated per row), obtained by exact-arithmetic-style
symmetric congruence on floating-point matrices. No interval or ball arithmetic was used,
so no statement here is a CERTIFIED result, and none of it is EXACT except where labelled.
These are measurements on a **synthetic caricature**, offered for others to check and to
shoot at. Several of my own going-in predictions were wrong; they are recorded as such in
§11.

Working directory: `/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det/`
(code: `loewner.py`, `run.py`, `extra.py`, `mechanism.py`, `crit.py`, `bigN.py`, `bigN2.py`,
`check24.py`, `validate.py`, `validate2.py`, `analyze.py`; raw output: `out_all.txt`,
`out_p4.txt` … `out_p10.txt`, `out_p9b_*.txt`, `out_check24.txt`, `out_mech.txt`).

I made no intentional change in `/home/user/riemann`, and `git status` there is clean as I
leave it — **but one stray scratch file of mine was accidentally swept into another session's
commit, and the repository owner needs to remove it. See the incident note in §16.**

---

## 1. The model

Following L-16004, for a source with simple poles

  psi(x) = sum_p w_p / (mu_p − x),

the Loewner (divided-difference) matrix on the nodes lambda_j = j, j = −N..N (dim = 2N+1) is
**exactly**

  Q = sum_p w_p ell(mu_p) ell(mu_p)^T,   ell(mu)_j = 1/(lambda_j − mu).      [EXACT, L-16004(i)]

Unperturbed source (real poles, psi odd): for each k a pole at +mu_k and at −mu_k, weight a_k each.

Perturbed source: one real pole mu_* is split into a conjugate pair, mirrored at −mu_*, so psi
stays real and odd:

  a/(mu_* − x)  ->  (a/2)[ 1/(mu_*+i d − x) + 1/(mu_*−i d − x) ],  and the same at −mu_*.

This puts poles at **±mu_* ± i d** — four of them, weight a/2 each.

**Why that quadruple is the right caricature.** With psi_W(x) = (1/pi) Im sum_rho 1/(s−rho),
s = 1/2 + i x/Delta, a zero rho = beta + i gamma gives a pole of psi_W at

  s − rho = 0  =>  x = Delta*gamma − i*Delta*(beta − 1/2).

The functional equation and conjugation force the quadruple {beta±i gamma, (1−beta)±i gamma},
hence poles at x = ±Delta*gamma ± i*Delta*(beta − 1/2). So the synthetic perturbation is
exactly the shape a genuine off-line zero would impose, with

  **mu_* = Delta*gamma**  and  **d = Delta*|Re rho − 1/2|**,   i.e. |Re rho − 1/2| = d/Delta.

Throughout, Delta = 1.5, so |Re rho − 1/2| = d/1.5. The "realistic" profile uses
mu_k = 1.5*gamma_k with gamma_k the zeta ordinates taken from `mpmath.zetazero` (not from
memory), and all residues a_k = 1.

**This is a caricature, not the Weil matrix.** It has no archimedean block, no prime sum, no
pole/kappa/J terms; it is the pure zero-side Loewner form with unit residues and a truncated
pole set. Conclusions transfer to X-0001's Q_W only as heuristics.

## 2. Method, and why not `eigsy`

Per the O-16004 erratum, `mpmath.eigsy` achieves only ~1e-17 relative accuracy on these
matrices regardless of dps, so its lambda_min sign is meaningless here. Everything below
instead uses a **Bunch–Parlett symmetric-indefinite LDL^T congruence with 1x1 and 2x2 pivots**,
which returns the inertia (n_+, n_−, n_0) and is exact up to the working precision by
Sylvester's law.

All spectral quantities are then obtained from that one primitive:

- `lambda_min(Q)` = log-bisection on t of the inertia of Q − tI. (Log, not linear: a linear
  bisection has an absolute floor and would silently report the floor instead of a 1e-60
  eigenvalue. I hit exactly this bug in a first draft and fixed it.)
- `delta_c` = log-bisection on d of "does Q(d) have a negative eigenvalue".
- `delta_det(u)` = same, but testing "is lambda_min(Q(d)) < −10^−u * lambda_max", i.e. the
  smallest displacement an observer carrying u significant digits could actually resolve.

Precision: dps = 40 + 6N (64 … 124 for N = 4 … 14).

### Validation performed

| check | result |
|---|---|
| rank-one closed form vs. independent divided-difference build | agree to 6.2e-61 at dps 60 |
| inertia routine vs. known inertia (random L D L^T, signs and scales 1e-25..1e3) | 4/4 exact |
| L-16004(ii): #negative eigenvalues = #nonreal conjugate pairs | confirmed, inertia (9,2,0) for 2 pairs |
| `lambda_min` bisection vs `eigsy` on a **well-conditioned** case | agree to 10 digits (both signs) |
| **dps doubling**, N=8: dps 88 -> 176 | every printed digit identical |
| **dps doubling**, N=14: dps 124 -> 248 | every printed digit identical |
| **dps doubling**, N=22, M=60: dps 172 -> 344 | lambda_max, lambda_min and delta_c identical to all 9 printed digits |
| **dps doubling**, N=24, M=60: dps 184 -> 368 | identical to all 9 printed digits (lambda_min = 4.68195434e−104) |
| peak-signal scan at dps 60 vs dps 150 (3 cells) | identical to all 9 printed digits |
| scale-invariance null test (all weights x0.01, so Q -> 0.01 Q) | delta_c identical to 7 digits |
| unperturbed inertia = (dim, 0, 0) asserted on every reported row | passes except the rows explicitly discarded in §8/§12 |

---

## 3. The conditioning floor, and delta_c

Realistic profile: Delta = 1.5, M = 20 zeta poles, a = 1, perturbed pole = the lowest,
mu_* = 1.5*gamma_1 = 21.2021.

| N | dim | dps | lambda_max | lambda_min(unperturbed) | log10 cond | delta_c | delta_det(16) | delta_det(30) | delta_det(50) |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 9 | 64 | 1.2955e−01 | 1.175703e−24 | 23.04 | 4.399114e−02 | 4.463e−01 | 4.399e−02 | 4.399e−02 |
| 6 | 13 | 76 | 1.9018e−01 | 3.998086e−34 | 32.68 | 2.783990e−04 | 2.267e−01 | 1.638e−03 | 2.784e−04 |
| 8 | 17 | 88 | 2.5463e−01 | 4.475971e−43 | 41.76 | 6.502025e−07 | 1.196e−01 | 2.266e−04 | 6.502e−07 |
| 10 | 21 | 100 | 3.2506e−01 | 6.601643e−52 | 50.69 | 5.239814e−10 | 3.296e−02 | 3.194e−05 | 1.272e−09 |
| 12 | 25 | 112 | 4.0501e−01 | 1.287352e−60 | 59.50 | 1.650201e−13 | 1.259e−02 | 4.327e−06 | 7.359e−11 |
| 14 | 29 | 124 | 5.0131e−01 | 1.801243e−69 | 68.44 | 1.577975e−17 | 4.069e−03 | 5.049e−07 | 1.280e−12 |

Inertia of the unperturbed Q was (dim, 0, 0) — positive definite — in every row.

Fits over the measured range 4 ≤ N ≤ 14 only (**not** extrapolated):

- **log10 lambda_min(unperturbed) = −6.42 − 4.4626 N**, rms 0.21.
  This reproduces O-16004 §5's "roughly 10^−4.5N" for the genuine arithmetic form almost
  exactly, which I did not expect from a synthetic model and take as mild corroboration that
  the collapse is driven by the pole geometry rather than by the arithmetic blocks.
- **log10 delta_c = 1.6634 − 0.5316 N − 0.05618 N²**, rms 0.012.
  A straight line fits far worse (rms 0.56), so over this range delta_c falls *faster than
  geometrically*. I do **not** claim the true asymptotic form is quadratic; six points and
  three parameters.
- **log10 delta_det(16) = 0.586 − 0.2075 N**, rms 0.081 — a much shallower, roughly geometric decline.

## 4. The control — the actual deliverable

The question was whether the negative eigenvalue created at delta_c is above or below the level
a floating-point or interval computation could see. The answer is unambiguous and is visible
in two independent ways.

**(a) At delta_c the signal is, by construction, at the conditioning floor.** As d runs from 0
to delta_c, lambda_min sweeps continuously from +lambda_min(0) down through 0. So in any
neighbourhood of delta_c the eigenvalue's magnitude is *smaller* than lambda_min(unperturbed)
= lambda_max / cond. An observer carrying u significant digits can resolve the crossing only if

  **u > log10 cond(Q) ≈ 4.46 N + 5.5.**

This is confirmed directly by the delta_det(50) column: it equals delta_c to all digits exactly
when 50 > log10 cond — that is for N = 4, 6, 8 (log10 cond = 23.0, 32.7, 41.8) — and departs
from delta_c precisely when log10 cond crosses 50, at N = 10 (50.69, ratio 2.4x), N = 12
(59.50, ratio 4.5e2), N = 14 (68.44, ratio 8.1e4).

**Consequence for float64 (u ≈ 16): the transition at delta_c is invisible for every N ≥ 3.**
Already at N = 4 one needs 23 digits.

**(b) The blind band, in absolute terms.** Converting with |Re rho − 1/2| = delta/1.5:

| N | delta_c | \|Re rho − 1/2\| at delta_c | delta_det(16) | \|Re rho − 1/2\| detectable in float64 | blind-band ratio |
|---|---|---|---|---|---|
| 4 | 4.3991e−02 | 2.93e−02 | 4.463e−01 | 2.98e−01 | 1.0e+01 |
| 6 | 2.7840e−04 | 1.86e−04 | 2.267e−01 | 1.51e−01 | 8.1e+02 |
| 8 | 6.5020e−07 | 4.34e−07 | 1.196e−01 | 7.97e−02 | 1.8e+05 |
| 10 | 5.2398e−10 | 3.49e−10 | 3.296e−02 | 2.20e−02 | 6.3e+07 |
| 12 | 1.6502e−13 | 1.10e−13 | 1.259e−02 | 8.39e−03 | 7.6e+10 |
| 14 | 1.5780e−17 | 1.05e−17 | 4.069e−03 | 2.71e−03 | 2.6e+14 |

Read the two middle columns together. At N = 14 the form **mathematically** stops being
positive definite once Re rho − 1/2 exceeds about **1.1e−17** — an impressively sharp
criterion. But a float64 computation of the same matrix cannot notice anything until
Re rho − 1/2 exceeds about **2.7e−3**, a violation so gross that ordinary zero-finding would
have found it decades ago. The gap between the two is 14 orders of magnitude and **widens**
with N: the sensitivity of the criterion improves far faster than the ability of any
fixed-precision computation to read it.

So: **raising N makes the finite Weil/Loewner criterion enormously more sensitive in exact
arithmetic, while the gap between that sensitivity and what fixed precision can read grows
without bound.** The exact threshold is only readable if working precision is scaled as
~4.0–4.5 N digits, which is the same budget O-16004 §5 derived for merely certifying positivity.

> **Read §8 before quoting this section.** The table above stops at N = 14, where the perturbed
> pole still lies well outside the node band (mu_1/N = 1.51). Extending to N = 24 at a
> rank-safe pole count changes one of the two conclusions: the *blind band* keeps widening
> exactly as above, but the *absolute* float64-detectable displacement improves by a further
> 5.5 orders of magnitude once the pole enters the band. My first reading of this section
> over-claimed; §8 corrects it.

## 5. Signal strength lambda_min(Q(d)) vs d

N = 8 (dps 88), lambda_max = 2.5463e−01, lambda_min(0) = 4.4760e−43, delta_c = 6.502025e−07:

| d/delta_c | d | inertia | lambda_min | lambda_min/lambda_max |
|---|---|---|---|---|
| 0 | 0 | (17,0,0) | +4.475971e−43 | +1.758e−42 |
| 0.5 | 3.2510e−07 | (17,0,0) | +3.359429e−43 | +1.319e−42 |
| 0.9 | 5.8518e−07 | (17,0,0) | +8.524491e−44 | +3.348e−43 |
| 0.99 | 6.4370e−07 | (17,0,0) | +8.932727e−45 | +3.508e−44 |
| 1.01 | 6.5670e−07 | (16,1,0) | −9.023559e−45 | −3.544e−44 |
| 1.1 | 7.1522e−07 | (16,1,0) | −9.432841e−44 | −3.705e−43 |
| 2 | 1.3004e−06 | (16,1,0) | −1.358647e−42 | −5.336e−42 |
| 10 | 6.5020e−06 | (15,2,0) | −7.861273e−39 | −3.087e−38 |
| 100 | 6.5020e−05 | (15,2,0) | −1.647420e−34 | −6.470e−34 |
| 1e3 | 6.5020e−04 | (15,2,0) | −8.793909e−29 | −3.454e−28 |
| 1e6 | 6.5020e−01 | (15,2,0) | −1.089586e−12 | −4.279e−12 |
| 1e9 | 6.5020e+02 | (16,1,0) | −7.040785e−33 | −2.765e−32 |

N = 12 (dps 112), lambda_max = 4.0501e−01, lambda_min(0) = 1.2874e−60, delta_c = 1.650201e−13:

| d/delta_c | d | inertia | lambda_min | lambda_min/lambda_max |
|---|---|---|---|---|
| 0 | 0 | (25,0,0) | +1.287352e−60 | +3.179e−60 |
| 0.9 | 1.4852e−13 | (25,0,0) | +2.447250e−61 | +6.042e−61 |
| 0.99 | 1.6337e−13 | (25,0,0) | +2.563455e−62 | +6.329e−62 |
| 1.01 | 1.6667e−13 | (24,1,0) | −2.589285e−62 | −6.393e−62 |
| 2 | 3.3004e−13 | (24,1,0) | −3.872068e−60 | −9.560e−60 |
| 10 | 1.6502e−12 | (24,1,0) | −1.362556e−58 | −3.364e−58 |
| 100 | 1.6502e−11 | (23,2,0) | −1.623086e−52 | −4.008e−52 |
| 1e3 | 1.6502e−10 | (23,2,0) | −9.368355e−49 | −2.313e−48 |
| 1e6 | 1.6502e−07 | (23,2,0) | −1.093564e−36 | −2.700e−36 |
| 1e9 | 1.6502e−04 | (23,2,0) | −1.913600e−24 | −4.725e−24 |

Three features worth recording:

1. **The crossing is clean and locally odd.** At d/delta_c = 0.99 and 1.01 the eigenvalue is
   +8.93e−45 and −9.02e−45 (N=8): a simple, transversal zero crossing. Nothing pathological
   happens at delta_c.
2. **Two negative eigenvalues appear, at different thresholds.** The perturbation introduces
   two conjugate pairs (at +mu_* and −mu_*), and L-16004(ii) predicts two negative directions.
   They do not arrive together: the inertia goes (17,0,0) -> (16,1,0) -> (15,2,0). This is
   exactly what L-16004(iv) implies — Q commutes with the parity gamma, so the spectrum splits
   into even and odd sectors and the two directions cross zero independently, one per sector.
3. **The signal is NON-monotone in d and eventually collapses.** At d/delta_c = 1e9 (d = 650)
   the N=8 signal has fallen back to −7.0e−33 from its −1.1e−12 at d = 0.65, and the inertia
   returns to (16,1,0). This is structural: as d -> infinity, ell(mu_*±i d) -> 0, so
   Q(d) -> Q(0) with the starred rank-one terms simply deleted, which is PSD again. There is a
   **best** displacement, and a **ceiling** on the signal.

## 6. The ceiling: the best signal obtainable at any displacement

Because of feature 3, the right question is not only "how small a d is detectable" but "how
large can the negative eigenvalue ever get". Peak of |lambda_min| over d ∈ [1e−3, 1e4]
(zeta profile, M=20, a=1; dps 60 for the scan, with a dps-150 spot check):

| N | perturbed zero | mu_* | peak lambda_min | at d = | \|peak\|/lambda_max | digits an observer needs |
|---|---|---|---|---|---|---|
| 6 | gamma_1 | 21.202 | −1.933518e−05 | 9.07 | 1.0167e−04 | 3.99 |
| 6 | gamma_2 | 31.533 | −3.386591e−10 | 17.21 | 1.7807e−09 | 8.75 |
| 6 | gamma_3 | 37.516 | −1.198670e−14 | 24.80 | 6.3029e−14 | 13.20 |
| 6 | gamma_4 | 45.637 | −6.927531e−16 | 27.29 | 3.6427e−15 | 14.44 |
| 6 | gamma_5 | 49.403 | −6.031213e−20 | 31.90 | 3.1713e−19 | 18.50 |
| 6 | gamma_7 | 61.378 | −4.201202e−22 | 36.77 | 2.2091e−21 | 20.66 |
| 6 | gamma_10 | 74.661 | −6.318358e−27 | 44.35 | 3.3223e−26 | 25.48 |
| 10 | gamma_1 | 21.202 | −2.838220e−04 | 8.23 | 8.7315e−04 | 3.06 |
| 10 | gamma_2 | 31.533 | −3.711132e−08 | 16.35 | 1.1417e−07 | 6.94 |
| 10 | gamma_3 | 37.516 | −1.140480e−11 | 24.17 | 3.5086e−11 | 10.45 |
| 10 | gamma_4 | 45.637 | −4.091219e−13 | 26.54 | 1.2586e−12 | 11.90 |
| 10 | gamma_5 | 49.403 | −6.076754e−16 | 31.90 | 1.8694e−15 | 14.73 |
| 10 | gamma_7 | 61.378 | −9.331988e−20 | 36.96 | 2.8709e−19 | 18.54 |
| 10 | gamma_10 | 74.661 | −1.307351e−21 | 43.75 | 4.0219e−21 | 20.40 |
| 14 | gamma_1 | 21.202 | −2.323472e−03 | 6.85 | 4.6348e−03 | 2.33 |
| 14 | gamma_2 | 31.533 | −1.122666e−06 | 14.97 | 2.2395e−06 | 5.65 |
| 14 | gamma_3 | 37.516 | −1.303131e−09 | 23.17 | 2.5994e−09 | 8.59 |
| 14 | gamma_4 | 45.637 | −3.588452e−12 | 25.88 | 7.1581e−12 | 11.15 |
| 14 | gamma_5 | 49.403 | −2.594880e−13 | 31.60 | 5.1762e−13 | 12.29 |
| 14 | gamma_7 | 61.378 | −7.423798e−17 | 37.79 | 1.4809e−16 | 15.83 |

The last column is log10(lambda_max/|peak|): **an observer carrying fewer significant digits
than this can never detect that zero being off the line, at any displacement whatsoever.**

Three readings:

- The peak signal degrades by roughly **3.5–4 orders of magnitude per zero index**. Only the
  first two or three zeta zeros produce a float64-visible signal at these N; by gamma_4 at
  N = 6 one already needs > 14 digits, and by gamma_10, > 25.
- **This ceiling improves as N grows**, unlike the delta_c obstruction which worsens. For
  gamma_1 the digits needed fall 3.99 -> 3.06 -> 2.33 as N goes 6 -> 10 -> 14; for gamma_4,
  14.44 -> 11.90 -> 11.15. So enlarging the matrix genuinely buys resolving power for the
  higher zeros — it just does not buy the ability to read the *threshold*.
- The optimal displacement is d ≈ 0.4–0.6 * mu_*, i.e. **|Re rho − 1/2| of order gamma/2** —
  a "zero" nowhere near the critical strip. The configuration that maximises the finite form's
  response is not a near-critical violation at all.

## 7. Dependence on the height of the perturbed pole

Zeta profile, N = 10, M = 20, a = 1; the unperturbed Q (hence lambda_min = 6.6016e−52,
lambda_max = 3.2506e−01, log10 cond = 50.69) is the same in every row — only which pole is
split changes.

| perturbed zero | mu_* = 1.5 gamma | delta_c | \|Re rho−1/2\| at delta_c | delta_det(16) | delta_det(30) | delta_det(50) |
|---|---|---|---|---|---|---|
| gamma_1 | 21.202 | 5.239814e−10 | 3.49e−10 | 3.296e−02 | 3.194e−05 | 1.272e−09 |
| gamma_2 | 31.533 | 2.128031e−05 | 1.42e−05 | 1.437e+00 | 5.853e−02 | 5.101e−05 |
| gamma_3 | 37.516 | 1.646631e−03 | 1.10e−03 | 6.740e+00 | 6.324e−01 | 3.851e−03 |
| gamma_4 | 45.637 | 1.562723e−01 | 1.04e−01 | **never** | 2.720e+00 | 3.132e−01 |
| gamma_5 | 49.403 | 6.287765e−01 | 4.19e−01 | **never** | 7.103e+00 | 1.147e+00 |
| gamma_6 | 56.379 | 1.887319e+00 | 1.26e+00 | **never** | 9.427e+00 | 2.958e+00 |
| gamma_7 | 61.378 | 4.667957e+00 | 3.11e+00 | **never** | 1.235e+01 | 5.655e+00 |
| gamma_8 | 64.991 | 4.819967e+00 | 3.21e+00 | **never** | 1.559e+01 | 6.752e+00 |
| gamma_9 | 72.008 | 7.874676e+00 | 5.25e+00 | **never** | 2.555e+01 | 8.701e+00 |

"never" = no displacement in [1e−90, 1e3] produces a negative eigenvalue exceeding
1e−16 * lambda_max — consistent with the ceiling measured in §6.

delta_c degrades by ~4.6 orders of magnitude from gamma_1 to gamma_2 and another ~1.9 to
gamma_3, then reaches O(1) and beyond: by gamma_4 the "critical" displacement is
|Re rho − 1/2| ≈ 0.1, i.e. the zero would have to leave the critical strip's neighbourhood
entirely. **At N = 10 this form has real discriminating power only over the first two or
three zeta zeros.** That is a resolution statement and it matches O-16004 §2, where at N=10
only gamma_1..gamma_3 are resolved to many digits and gamma_4 onward are "resolution-limited
artefacts".

Note the important structural fact: with Delta = 1.5 the nodes are the integers |x| ≤ N while
mu_1 = 21.2, so **for every N ≤ 21 the perturbed pole lies outside the sampled node interval
altogether.** All of §3–§7 is therefore extrapolation from outside the band. §8 crosses that line.

## 8. Crossing into the band: the definitive sweep, N = 8 … 24 at M = 60

**First attempt discarded.** I first ran N = 16…24 at M = 20 and got apparently spectacular
numbers (delta_c below 1e-56). They are worthless: 2M = 40 rank-one terms cannot span
dimension 2N+1 > 40, and the measured inertia was **(40,0,1)** at N=20, **(40,0,5)** at N=22,
**(40,0,9)** at N=24 — Q is exactly singular by construction, so delta_c = 0 mathematically and
the reported values were precision floors. Recorded here because it is the same trap as the
N=12/M=10 row in §12, and it is easy to fall into: **a necessary sanity check on every row is
that the unperturbed inertia is exactly (dim, 0, 0).**

Rerun at **M = 60** (120 rank-one terms, comfortably spanning dim ≤ 49), all nine rows verified
full rank (dim, 0, 0). This is the cleanest series in the report — one fixed M, one fixed
perturbed pole (gamma_1), N doubled from 8 to 24, crossing mu_1/N = 1 between N = 20 and N = 22.

| N | dim | dps | mu_1/N | lambda_max | lambda_min(0) | log10 cond | delta_c | delta_det(16) | blind ratio |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 17 | 88 | 2.650 | 3.0008e−01 | 2.777477e−42 | 41.03 | 1.476018e−06 | 1.3058e−01 | 8.85e+04 |
| 10 | 21 | 100 | 2.120 | 3.8122e−01 | 1.391112e−50 | 49.44 | 2.182385e−09 | 3.9866e−02 | 1.83e+07 |
| 12 | 25 | 112 | 1.767 | 4.7183e−01 | 8.594257e−59 | 57.74 | 1.202314e−12 | 1.3895e−02 | 1.16e+10 |
| 14 | 29 | 124 | 1.514 | 5.7860e−01 | 1.416779e−66 | 65.61 | 3.948495e−16 | 4.3710e−03 | 1.11e+13 |
| 16 | 33 | 136 | 1.325 | 7.1741e−01 | 2.119599e−74 | 73.53 | 4.164553e−20 | 1.0025e−03 | 2.41e+16 |
| 18 | 37 | 148 | 1.178 | 9.4394e−01 | 7.200548e−82 | 81.12 | 1.872521e−24 | 1.1282e−04 | 6.03e+19 |
| 20 | 41 | 160 | 1.060 | 1.8346e+00 | 2.494864e−89 | 88.87 | 1.178458e−29 | 4.4766e−06 | 3.80e+23 |
| 22 | 45 | 172 | **0.964** | 2.7743e+01 | 7.571377e−97 | 97.56 | 3.085434e−36 | 4.0312e−08 | 1.31e+28 |
| 24 | 49 | 184 | **0.883** | 2.8120e+01 | 4.681954e−104 | 104.78 | 2.761934e−41 | 1.0124e−08 | 3.67e+32 |

Fits over 8 ≤ N ≤ 24:

- **log10 cond(Q) = 9.68 + 3.976 N**, rms 0.31. So the working precision needed merely to
  *resolve* the transition is ~**4.0 N + 10 significant digits**.
- **log10 lambda_min = −7.34 − 4.432 N + 0.0181 N²**, rms 0.086 (linear: rms 0.43).
- **log10 delta_c = −0.373 − 0.203 N − 0.0618 N²**, rms 0.31 (linear: rms 1.48). The
  super-geometric decay of delta_c is confirmed over a doubled range of N, and the M=20
  quadratic of §3 predicted the M=60 N=16 value to 0.09 decades.

**In |Re rho − 1/2| units (= delta/1.5):**

| N | mu_1/N | exact threshold | float64-detectable | blind band |
|---|---|---|---|---|
| 8 | 2.650 | 9.84e−07 | 8.71e−02 | 8.9e+04 |
| 12 | 1.767 | 8.02e−13 | 9.26e−03 | 1.2e+10 |
| 16 | 1.325 | 2.78e−20 | 6.68e−04 | 2.4e+16 |
| 20 | 1.060 | 7.86e−30 | 2.98e−06 | 3.8e+23 |
| 22 | 0.964 | 2.06e−36 | 2.69e−08 | 1.3e+28 |
| 24 | 0.883 | 1.84e−41 | 6.75e−09 | 3.7e+32 |

**This forces a correction to the tone of §4, and I want to flag it clearly.** Judging only
from N ≤ 14 (where the pole is far outside the node band) I concluded the float64 channel was
hopeless: it needed |Re rho − 1/2| ≳ 3e−3. That conclusion does **not** survive the extension.
Once the pole approaches and enters the band, the float64-detectable displacement improves
steeply — by 5.5 orders of magnitude between N = 14 and N = 24, reaching **6.7e−9**. The
per-step improvement in delta_det(16) accelerates from ~0.5 decades per ΔN=2 at small N to
~2.0 decades across the band crossing (N = 20 -> 22).

So the honest statement is a **split verdict**:

- the *blind band* (ratio between the exact and the float64-visible thresholds) widens
  monotonically and without any sign of turning over, from 8.9e+04 at N=8 to 3.7e+32 at N=24;
- but the *absolute* float64 sensitivity improves substantially with N, and at N = 24 is
  |Re rho − 1/2| ≈ 7e−9, which is not a ridiculous figure.

Both are true simultaneously; they answer different questions. If the question is "can a
fixed-precision computation locate the exact positivity threshold", the answer is firmly no and
gets worse. If it is "can a fixed-precision computation detect a sufficiently off-line zero at
all", the answer improves with N and is not hopeless — though 7e−9 at gamma_1 is still far
weaker than what direct zero-finding already certifies.

**Two caveats on the last two rows.** (i) lambda_max jumps from 1.83 (N=20) to 27.7 (N=22)
because node 21 sits only 0.2021 away from the pole mu_1 = 21.2021, so one entry of
ell(mu_1) blows up. That near-collision inflates lambda_max and hence the 1e−16*lambda_max
detection threshold, making delta_det(16) jumpy exactly across the band crossing; the N=22->24
step in delta_det(16) is only 0.6 decades against 2.0 for N=20->22. Reading a smooth law
through the crossing would be over-interpretation. (ii) The whole crossing region deserves a
finer scan in N and in the offset of the node lattice relative to the pole, which I did not do.

## 9. Weight dependence

Zeta profile, N = 8, star = gamma_1. **(a) scaling only the perturbed pole's weight a_\*:**

| a_* | lambda_max | lambda_min(0) | delta_c | delta_c * sqrt(a_*) |
|---|---|---|---|---|
| 0.01 | 1.7050e−01 | 4.475971e−43 | 6.502025e−06 | 6.502025e−07 |
| 0.1 | 1.7814e−01 | 4.475971e−43 | 2.056121e−06 | 6.502025e−07 |
| 1 | 2.5463e−01 | 4.475971e−43 | 6.502025e−07 | 6.502025e−07 |
| 10 | 1.0202e+00 | 4.475971e−43 | 2.056121e−07 | 6.502025e−07 |
| 100 | 8.6770e+00 | 4.475971e−43 | 6.502025e−08 | 6.502025e−07 |

**delta_c ∝ a_*^(−1/2) exactly**, to all 7 printed digits across four decades of a_*. And
lambda_min(unperturbed) is *identical* in all five rows — the starred pole contributes nothing
to the conditioning floor, only to the signal. This is precisely what the second-order model
of §10 predicts (the perturbation enters as a_* d², so a_* d² is the invariant).

**(b) null test, scaling all weights** (Q -> cQ, so delta_c must be invariant): with all
a = 0.01, lambda_max and lambda_min both scale by exactly 0.01 (4.475971e−45) and
delta_c = 6.502025e−07 is unchanged to all digits. Null test passes.

## 10. Mechanism: delta_c is a generalized eigenvalue, not sqrt(lambda_min)

Expanding ell(mu + i d) in d, the perturbed quadruple contributes
Q(d) = Q(0) + d² B + O(d⁴) with

  B = −a * sum over {+mu_*, −mu_*} of [ ell' ell'^T + (1/2)(ell ell''^T + ell'' ell^T) ],

derivatives in mu. Hence delta_c² = 1/rho with rho the largest eigenvalue of
−Q0^(−1/2) B Q0^(−1/2). Measured:

| N | delta_c (exact, all orders) | delta_c (quadratic model) | rel. diff | sqrt(lambda_min/lambda_max) | delta_c / that |
|---|---|---|---|---|---|
| 4 | 4.39911372e−02 | 4.39686431e−02 | 5.11e−04 | 3.0125e−12 | 1.460e+10 |
| 6 | 2.78398964e−04 | 2.78398951e−04 | 4.61e−08 | 4.5851e−17 | 6.072e+12 |
| 8 | 6.50202521e−07 | 6.50202521e−07 | 0 (all digits) | 1.3258e−21 | 4.904e+14 |
| 10 | 5.23981422e−10 | 5.23981422e−10 | 0 (all digits) | 4.5066e−26 | 1.163e+16 |
| 12 | 1.65020110e−13 | 1.65020110e−13 | 0 (all digits) | 1.7829e−30 | 9.256e+16 |

The quadratic model reproduces delta_c to full printed precision for N ≥ 8, so delta_c is
governed entirely by the O(d²) term — which also explains the exact a_*^(−1/2) law of §9.

The last two columns refute the naive guess (see §11): delta_c is **10 to 17 orders of
magnitude larger** than sqrt(lambda_min/lambda_max). The reason is alignment: B's negative
direction is ell'(mu_*), a smooth vector that lives overwhelmingly in the *top* eigenspace of
Q0, while lambda_min's eigenvector is a highly oscillatory one. The overlap is tiny, so the
perturbation is far less efficient at breaking positivity than a norm comparison suggests.

## 11. Predictions of mine that failed

1. **REFUTED — "delta_c ~ sqrt(lambda_min)".** I predicted going in that since the
   perturbation enters at O(d²) with strength ~a d²|ell'|², the threshold would be
   delta_c ≈ sqrt(lambda_min / ||B||), i.e. delta_c would fall like the square root of the
   conditioning floor, ~10^(−2.2N). Measured: delta_c exceeds sqrt(lambda_min/lambda_max) by
   1.5e10 (N=4) rising to 9.3e16 (N=12), and its log is fit by a *quadratic* in N
   (−0.53N − 0.056N²), not by half the lambda_min slope (−2.23N). The prediction is wrong in
   magnitude and in shape. The cause is the eigenvector alignment described in §10.
   Direction of the error: delta_c is **larger** than I predicted, i.e. detection is *harder*,
   not easier.
2. **REFUTED — "20 poles suffice".** See §12; the answer moves by a factor of ~5 between
   M = 20 and M = 100 and has not converged.
3. **Partly wrong — "each nonreal pair forces a negative eigenvalue".** This is L-16004(ii)'s
   phrasing and it is correct *in L-16004's own setting* (2N poles in dimension 2N+1, so the
   PSD part is rank-deficient and cannot cover the negative direction). It is **not** true for
   an over-determined form: see §13.
4. **REFUTED, my own §4 conclusion — "float64 could never detect this at any N".** On the
   N ≤ 14 data (pole outside the band) the float64-detectable displacement was ~3e−3 and
   falling only like 10^(−0.21N), which I read as hopeless. Extending to N = 24 with a
   rank-safe pole count, delta_det(16) falls to 1.0e−08 (|Re rho − 1/2| ≈ 6.7e−09), improving
   ~2 decades per ΔN=2 across the band crossing rather than ~0.5. The pessimistic reading was
   an artifact of only sampling N where the pole sat outside the node interval. See §8.
5. **A trap I fell into twice, worth recording as a methodological warning.** Both my N=12/M=10
   row (§12) and my entire first N ≥ 20 sweep (§8) were rank-deficient: with M poles the form
   has only 2M rank-one terms, so Q is exactly singular once 2M < 2N+1, and then delta_c = 0
   mathematically while the computation reports an impressive-looking precision floor
   (1e−56, 1e−62, 1e−68). Both times the numbers looked like a dramatic result. **The check
   that catches it is free: assert that the unperturbed inertia is exactly (dim, 0, 0).**
   This is the same species of error as the leading-principal-minor mistake recorded in
   L-16004's adversarial-tests section.

## 12. Convergence in the number of poles — this check FAILED

The brief asked me to include ≥20 poles and check that adding more does not change the answer
materially. **It does.** Zeta profile, star = gamma_1:

| M | N=8: lambda_min(0) | N=8: delta_c | change | N=10: lambda_min(0) | N=10: delta_c | change |
|---|---|---|---|---|---|---|
| 20 | 4.475971e−43 | 6.50202521e−07 | — | 6.601643e−52 | 5.23981422e−10 | — |
| 30 | 1.208997e−42 | 1.01883948e−06 | x1.567 | 3.718586e−51 | 1.18279866e−09 | x2.257 |
| 40 | 1.871427e−42 | 1.23849891e−06 | x1.216 | 7.505376e−51 | 1.63999337e−09 | x1.387 |
| 60 | 2.777477e−42 | 1.47601769e−06 | x1.192 | 1.391112e−50 | 2.18238513e−09 | x1.331 |
| 80 | 3.330984e−42 | 1.59971300e−06 | x1.084 | 1.839509e−50 | 2.48286658e−09 | x1.138 |
| 100 | 3.692339e−42 | 1.67423825e−06 | x1.047 | 2.150286e−50 | 2.66814544e−09 | x1.075 |

delta_c rises monotonically with M and is still creeping up by 5–7% per step at M = 100;
from M = 20 to M = 100 it moves by **x2.6 (N=8) and x5.1 (N=10)**. lambda_min(0) moves by
x8.2 and x33. So all absolute values in §3–§9, computed at M = 20, are **low by roughly half
an order of magnitude**, and should be read as order-of-magnitude only.

What *is* stable is the N-scaling: the exponent measured at M = 20 (log10 delta_c dropping
6.60 decades from N=8 to N=12) versus at M = 40 (6.19 decades) agrees to ~6%. The laws in
§3–§4 are therefore robust in shape even though the constants are not converged. All
conclusions in §4 concern ratios and slopes and are unaffected at the order-of-magnitude level.

**One row must be discarded outright.** At N = 12 with M = 10 the pole set gives only
2M = 20 rank-one terms in dimension 25, so Q is *singular* — measured inertia (20, 0, 5). Its
apparent lambda_min = 4.27e−107 and delta_c = 2.42e−40 are precision floors, not spectral
facts. **A necessary condition for any of this to mean anything is 2M > 2N+1, i.e. M > N.**

## 13. When the form NEVER loses positivity — and a caution about L-16004(ii)

To separate the effect of "how far outside the sampled band the pole sits" from "how
ill-conditioned Q is", I ran a second profile: a uniform ladder mu_k = k*pi/2, k = 1..20
(spacing irrational so no pole can land on an integer node — my first attempt used
mu_k = 1.5k, which put a pole exactly on node 3 and crashed). This profile puts several poles
*inside* the node band, and the resulting Q is far better conditioned: log10 cond = 6.8 at
N = 4 versus 23.0 for the zeta profile.

Ladder, M = 20, a = 1, delta scanned over [1e−90, 1e3] for delta_c and over [1e−3, 1e4] on a
29-point log grid for the deepest excursion of lambda_min:

| N | mu_* | mu_*/N | lambda_min(0) | min over d of lambda_min | at d | verdict | delta_c | delta_det(16) |
|---|---|---|---|---|---|---|---|---|
| 4 | 1.571 | 0.39 | +8.816056e−06 | −1.555813e+00 | 5.62e−01 | loses PD | 1.602e−03 | 1.602e−03 |
| 4 | 7.854 | 1.96 | +8.816056e−06 | +6.483914e−06 | 3.16e+00 | **NEVER** | never | never |
| 4 | 12.566 | 3.14 | +8.816056e−06 | +8.438576e−06 | 3.16e+01 | **NEVER** | never | never |
| 4 | 31.416 | 7.85 | +8.816056e−06 | +8.621168e−06 | 5.62e+01 | **NEVER** | never | never |
| 6 | 1.571 | 0.26 | +3.798906e−08 | −1.582885e+00 | 5.62e−01 | loses PD | 9.738e−05 | 9.738e−05 |
| 6 | 7.854 | 1.31 | +3.798906e−08 | −1.001426e−03 | 3.16e+00 | loses PD | 5.616e−01 | 5.616e−01 |
| 6 | 12.566 | 2.09 | +3.798906e−08 | +2.441840e−08 | 5.62e+00 | **NEVER** | never | never |
| 6 | 31.416 | 5.24 | +3.798906e−08 | +3.610868e−08 | 5.62e+01 | **NEVER** | never | never |
| 8 | 1.571 | 0.20 | +1.574355e−10 | −1.649617e+00 | 5.62e−01 | loses PD | 6.027e−06 | 6.027e−06 |
| 8 | 7.854 | 0.98 | +1.574355e−10 | −4.814851e+00 | 3.16e−01 | loses PD | 2.272e−03 | 2.272e−03 |
| 8 | 12.566 | 1.57 | +1.574355e−10 | −6.164319e−10 | 1.00e+01 | loses PD | 5.235e+00 | 5.235e+00 |
| 8 | 31.416 | 3.93 | +1.574355e−10 | +1.396879e−10 | 5.62e+01 | **NEVER** | never | never |
| 10 | 1.571 | 0.16 | +5.658630e−13 | −1.727276e+00 | 5.62e−01 | loses PD | 3.529e−07 | 3.547e−07 |
| 10 | 7.854 | 0.79 | +5.658630e−13 | −6.014295e+00 | 1.78e−01 | loses PD | 3.096e−05 | 3.112e−05 |
| 10 | 12.566 | 1.26 | +5.658630e−13 | −1.697183e−04 | 5.62e+00 | loses PD | 5.041e−01 | 5.061e−01 |
| 10 | 31.416 | 3.14 | +5.658630e−13 | +3.470408e−13 | 1.00e+02 | **NEVER** | never | never |
| 12 | 1.571 | 0.13 | +1.593040e−15 | −1.768928e+00 | 5.62e−01 | loses PD | 1.843e−08 | 8.175e−07 |
| 12 | 7.854 | 0.65 | +1.593040e−15 | −6.172045e+00 | 1.78e−01 | loses PD | 7.932e−07 | 5.981e−06 |
| 12 | 12.566 | 1.05 | +1.593040e−15 | −2.932757e−01 | 1.00e+00 | loses PD | 7.716e−03 | 2.330e−02 |
| 12 | 31.416 | 2.62 | +1.593040e−15 | −7.317804e−15 | 1.00e+02 | loses PD | 7.619e+00 | never |

Two things follow.

**(a) An off-line pole does not always break positivity.** In the rows marked NEVER, Q(d) is
positive definite for *every* displacement tested — over 94 decades of d in the delta_c scan
and across the full grid spanning the peak. The perturbation barely moves lambda_min at all
(N=4, mu_*=31.4: from 8.816e−06 down to 8.621e−06, a 2% dip). The NEVER/loses boundary in
mu_*/N sits between 0.39 and 1.96 at N=4, between 1.31 and 2.09 at N=6, between 1.57 and 3.93
at N=8, between 1.26 and 3.14 at N=10, and is above 2.62 at N=12 (where all four rows lose PD).
It **rises with N**, because lambda_min(0) is collapsing (8.8e−06 -> 1.6e−15 from N=4 to N=12)
and so ever less signal is needed to overcome it.

**This is a caution about how L-16004(ii) is quoted.** Its sentence "each nonreal pair forces a
negative eigenvalue and Q ⊁ 0" is correct *in its own setting* — there Q is built from exactly
2N poles in dimension 2N+1, so the PSD part contributed by the real poles has rank ≤ 2N−2 and
simply cannot cover the negative direction; the rank count does the work. Lifted out of that
setting to an **over-determined** form (here 2M = 40 rank-one terms in dimension 9–17), the
statement is **false**, and the rows above are explicit numerical counterexamples. This matters
for the programme because psi_W has infinitely many poles (all the zeta zeros) sampled at
finitely many nodes — the over-determined regime, not L-16004's. Whether a single off-line
zero must break positivity of a finite Weil matrix therefore does **not** follow from
L-16004(ii) and needs its own argument.

**(b) The trade-off, stated sharply.** In the ladder rows that do lose positivity,
delta_det(16) = delta_det(30) = delta_det(50) = delta_c *exactly*: because Q is well
conditioned (log10 cond ≈ 6.8–9.2), plain float64 resolves the true threshold perfectly. But
that threshold is large — delta_c = 1.6e−03 at N=4, and 5.6e−01 at N=6 for mu_*=7.854. Compare
the zeta profile at N=14, where delta_c = 1.6e−17 but 68 digits are needed to see it.

So across the two profiles the pattern is consistent and, I think, the main qualitative lesson:

> **Sensitivity and readability trade against each other.** Configurations in which the finite
> form is exquisitely sensitive to an off-line zero are exactly the configurations in which the
> form is so ill-conditioned that no fixed-precision computation can read the answer.
> Configurations a float64 computation can read are exactly the ones with a coarse threshold.
> I did not find a regime with both.

---

## 14. What these numbers do and do not show

**They do show,** within the synthetic model, at Delta = 1.5, M = 20–100 poles, unit residues,
4 ≤ N ≤ 24, and only for a perturbation of the form ±mu_* ± i d:

- the unperturbed finite Loewner form is positive definite with lambda_min decaying like
  10^(−4.4N), matching O-16004's independently measured 10^(−4.5N) for the arithmetic form;
- an off-line zero is detected in exact arithmetic at a threshold delta_c that falls
  **super-geometrically** in N: log10 delta_c ≈ −0.20N − 0.062N² over 8 ≤ N ≤ 24 at M = 60
  (a quadratic fits with rms 0.31 against 1.48 for a straight line);
- delta_c ∝ a_*^(−1/2) exactly, to 7 digits over four decades of a_*, and delta_c is exactly
  the O(d²) generalized-eigenvalue threshold (the quadratic model reproduces it to full
  printed precision for N ≥ 8);
- the signal at delta_c sits *at* the conditioning floor, so reading the transition requires
  ≳ 4.0N + 10 significant digits — **float64 cannot locate the exact threshold for any N ≥ 3**;
- the blind band between "mathematically broken" and "float64-visible" **widens monotonically
  and without turning over**, from 8.9e+04 at N = 8 to 3.7e+32 at N = 24;
- but the *absolute* float64-detectable displacement **improves** with N, from
  |Re rho − 1/2| ≈ 8.7e−02 at N = 8 to ≈ 6.7e−09 at N = 24, improving fastest as the pole
  enters the node band;
- the signal is bounded and non-monotone in d, so for high zeros there is a hard ceiling: at
  N = 10, detecting a displaced gamma_4 needs ≥ 12 digits *at the optimal displacement*, and
  no displacement whatsoever makes it float64-visible — though this ceiling improves with N
  (gamma_4 needs 14.4 digits at N = 6 and 11.2 at N = 14);
- an off-line pole does **not** always break positivity at all: in an over-determined form
  with a well-conditioned Q, Q(d) stayed positive definite for every d tested (§13).

**They do not show:**

- anything about the genuine Weil matrix Q_W of X-0001. This model has no archimedean block,
  no prime sum, no pole/kappa/J terms, unit residues, and a truncated pole set. The agreement
  of the lambda_min exponent with O-16004 is suggestive, not evidential.
- anything certified. No interval or ball arithmetic; the LDL^T congruence is exact only up to
  the working precision. The dps-doubling checks (N = 8, 14, 22 and 24, precision doubled, all
  printed digits identical) are strong self-consistency evidence, not proof.
- converged constants — see §12. Only slopes and ratios should be quoted.
- anything about N > 24, M > 100, Delta ≠ 1.5, non-unit residues, or perturbations other than
  a single symmetric quadruple. In particular I did not test several simultaneous off-line
  zeros, and the rank-one interlacing remark in O-16004 §4 suggests that case may behave
  differently.

## 15. Suggested follow-ups

1. Repeat §4's control on the **actual** Q_W from X-0001 by inserting a synthetic off-line
   zero into its zero-side source, to see whether the 4.5N-digit rule and the widening blind
   band survive the arithmetic blocks.
2. The alignment fact in §10 is the crux and deserves a proof: bound the overlap of
   ell'(mu_*) with the bottom eigenspace of Q0. If that overlap has a clean asymptotic, the
   quadratic-in-N shape of log delta_c should follow analytically.
3. Because the signal is non-monotone with a maximum near d ≈ 0.5 mu_*, any search strategy
   that scans small displacements is looking in the worst place. If the goal is to *falsify*
   positivity numerically, large displacements are far more efficient — though they correspond
   to zeros nowhere near the critical strip.
4. §8 shows the interesting action is at the band crossing mu_1/N ≈ 1, which I sampled at only
   two points (N = 22, 24) and where lambda_max is contaminated by a node–pole near-collision.
   A finer sweep, with the node lattice deliberately offset relative to mu_1, would separate
   the genuine band-crossing effect from that artifact.
5. Everything here is uncertified. The natural next step for anything load-bearing is to
   redo the inertia in ball arithmetic (Arb) on a rationalised matrix with an explicit moat,
   the way O-16004's erratum does, rather than in mpmath floats.

---

## 16. Incident note — action needed by the repository owner

I need to report a mistake of mine that touched the repository, contrary to my instructions.

While launching background jobs I wrote `cd <scratchpad> && nohup … &` followed by further
`nohup … &` commands in the same shell line. Because `&` backgrounded the whole `cd && …`
group, the *subsequent* commands ran in the original working directory, `/home/user/riemann`,
and one of them created a stray 92-byte scratch file there: `out_p7.txt`, whose contents are a
Python "can't open file" error message.

Within the same minute, a **concurrent session** committed
`fd37649 "observation: O-16006 — two measured laws, and a control that deflates half of one"`
(timestamp 2026-07-31 16:52:12) using `add -A`-style staging, and that commit **swept my stray
file into the repository**. `git show --stat fd37649` lists `out_p7.txt | 1 +` alongside its
five intended files.

What I did: I deleted the stray file, saw that `git status` then reported it as a deletion of a
*tracked* file, investigated, and confirmed it had been committed by the other session rather
than by me. I then ran `git checkout -- out_p7.txt` to restore the working tree so the repo is
**clean and exactly matches HEAD**. I did not commit, and I did not rewrite history — another
session is actively working in this repository and rewriting a shared commit would have been
far more damaging than the junk file.

**Action needed:** `out_p7.txt` is junk and should be removed from the repository by whoever
owns the branch, e.g. `git rm out_p7.txt && git commit -m "docs: remove stray scratch file
accidentally committed in fd37649"`. Nothing else in `/home/user/riemann` was created,
modified, or deleted by me, and `git status` is clean as I leave it.

Two process suggestions, offered in the spirit of README §15:

- Agents launching background jobs should use **absolute paths only** and never rely on `cd`
  in a line containing `&`. I have adopted this for the rest of the session.
- More importantly, this is a coordination hazard rather than a personal slip: any agent that
  stages with `git add -A` / `git commit -a` in a shared working directory will silently
  capture whatever another concurrent session happens to have left lying around. Staging
  explicit paths would have prevented it, and may be worth a line in the README's commit
  conventions.
