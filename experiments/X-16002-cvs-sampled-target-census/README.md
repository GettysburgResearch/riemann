# X-16002 — Certified real-root census of the CvS sampled-Ξ target

Experiment ID: `X-16002`
Authoring agent: `claude-fable-01`
Date: 2026-07-31
Associated claims: `L-16001`, `O-16001`, `L-16003`, `R-16001`
Associated issue: #151 (parallel positive-path continuation); relates to PR #158

## Research question

The working note of PR #158 reduces its cofinal programme to a finite gate: for every sufficiently large level
there must exist a rational `c` with `T_p(c) >= 0` and `ker T_p(c) = R p`. By `L-15108` that gate holds exactly
when the Connes–van Suijlekom interpolation polynomial

```text
P(s) = sum_{j=-N}^{N} xi_j * prod_{k != j} (k - s)
```

is real-rooted with simple roots. **Is that true for the target the programme actually constructs?**

## The target

Per `L-16001`, the repository's exact Weil-radical target is Pólya's function: `K(t) = k(e^t) = Phi(t)/4`, and
`hat k = Xi/4` (note the factor, which `L-15101.7` omits). Per `O-16001`, the CvS coordinates are Fourier
**coefficients**, not point samples, so with scale `alpha > 0` and window `|t| <= 1/(2 alpha)`:

```text
F(z)  = int_{|t| <= 1/(2 alpha)} Phi(t) e^{i alpha z t} dt        (approximates Xi(alpha z))
xi_j  = (-1)^j F(2 pi j)  ~  (-1)^j Xi(2 pi alpha j),   |j| <= N
```

## Method — what makes this certified rather than merely computed

1. `Xi` evaluated with `mpmath` at **120–150 decimal digits**.
2. Coefficients rationalized to **100 significant digits** as `fractions.Fraction`.
3. `P` expanded **exactly over Q**; squarefree part via exact `gcd(P, P')`.
4. Distinct real roots counted by an **exact Sturm sequence over Q** (`sympy.Poly.count_roots`).
5. Counts re-verified at rationalization precisions 20/30/40/50/60 digits — identical at every precision, so no
   result sits on a precision cliff.

Only step 1 uses floating point, and only to produce the numbers that are then rationalized; every
**decision** (root count, sign, degree) is exact rational arithmetic.

## Files

| file | purpose |
|---|---|
| `check3.py` | verifies `hat k = Xi/4` and `K > 0` to 32 digits (supports `L-16001`) |
| `alias.py` | verifies the Poisson/aliasing identity to 31 digits |
| `verify_id.py` | verifies that the truncated cardinal series approximates `Xi(alpha z)`, and the precision stability of the root count |
| `exact_count.py` | first exact Sturm census over `(alpha, N)` |
| `roots_hp.py` | 150-digit root locations plus exact Sturm counts |
| `threshold.py` | tests the predicted pass threshold |
| `threshold_scan.py` | wide `(alpha, N)` scan and bisection for `alpha_c` |
| `taper.py` | locations of the residual nonreal roots; five taper families |
| `controls.py` | control experiments (one-signed targets; exactly band-limited `sinc` targets) |
| `signlaw.py` | tests the `L-16003` gap-parity bound across three families |
| `results/` | raw outputs and JSON |

Dependencies: `python3`, `mpmath` 1.3.0, `sympy` 1.14.0. No network access needed.

## Principal results

**1. A sharp critical scale, independent of the level.** Bisection returns

```text
alpha_c in (1.064404, 1.064417)
```

identically for `N = 6, 8, 10, 14, 20, 26, 30`. For `alpha > alpha_c` the polynomial is real-rooted at every level
tested; for `alpha < alpha_c` it is not, and **raising `N` never repairs it**.

**2. Below threshold the deficit is bounded below by 4.** For `alpha` in `0.8 .. 1.05` and `N = 4 .. 20` the deficit
`2N - #real` is exactly `4`. At `alpha = 0.5` it is `12` for `N = 34, 38, 40, 44`.

**3. The obstructing roots depend on the scale, not the level, and not on tapering.** In the `Xi` variable
`w = 2 pi alpha s` they are `+-14.70184 +- 4.534335i` (`alpha = 0.8`), `+-13.17982 +- 2.654358i` (`alpha = 0.9`),
`+-12.57186 +- 1.564114i` (`alpha = 1.0`), agreeing to 7 significant figures across levels. Deficit stays exactly
`4` under hard, Fejér, Hann, Gaussian and Tukey tapering.

**4. Controls.**
- One-signed targets: deficit `0` exactly at `N = 4, 6, 8`, as `L-16003`(iii) requires — the pipeline does not
  manufacture complex roots.
- Exactly band-limited, provably real-rooted `sinc` targets (no aliasing possible): deficits `8, 10, 12`
  (`gamma = 0.2`), `4, 6, 6` (`gamma = 0.35`), `2, 2, 2` (`gamma = 0.45`). In **all nine** cases the real-root count
  equals the number of real zeros of the target inside the sampled window, exactly. The phenomenon is therefore a
  general property of truncated cardinal series driven by **zero density**, not an artefact of `Xi`, of aliasing,
  or of RH.

**5. Gap-parity bound.** `#real >= #same-sign adjacent pairs of xi` held in **26 of 26** cases across all three
families. It is attained with equality in all 8 one-signed and band-limited cases and strictly exceeded in 13 of
18 sampled-`Xi` cases — so the bound is sharp but the corresponding equality is **false** in general.

## Interpretation

See `R-16001`. In brief: passing requires the target transform to carry one zero per sample gap (critical Nyquist
density). Above `alpha_c` the window is so short that `F` is essentially a sinc-like bump transform, which has
exactly that density. Below `alpha_c` — that is, as soon as `F` starts genuinely converging to `Xi` — the sample
gaps nearest the origin contain no zero of `F` at all (`Xi`'s first zero is at `w = 14.134...`) and each empty gap
forfeits a real root. Convergence needs `alpha -> 0`; passing needs `alpha > alpha_c`. **For this target family the
two hypotheses of the note's Theorem 3.1 are incompatible.**

## Limitations

- The census covers the **naive sampled target**, not necessarily the repository's production "repaired" target.
  This is the load-bearing caveat; see `R-16001` gap audit item 1.
- The `N`-independence of `alpha_c` is an observation over seven levels, not a theorem.
- CvS's **parity** constraints (odd source, even diagonal) were not verified at passing levels, so a "PASS" here
  is necessary but possibly not sufficient for the note's gate.
- A `float64` run of the same computation produced nonreal roots apparently inside the RH strip; these are
  **numerical artefacts** that vanish at 150 digits. Do not use double precision for this computation — the
  sampled coefficients span a dynamic range of `1e-21` or worse.

## Reproduction

```bash
pip install mpmath sympy
cd experiments/X-16002-cvs-sampled-target-census
python3 check3.py       # normalization, ~1 min
python3 controls.py     # controls, ~5 min
python3 signlaw.py      # gap-parity law, ~15 min
python3 threshold.py    # threshold test, ~20 min
python3 taper.py        # residual roots and tapers, ~20 min
```
