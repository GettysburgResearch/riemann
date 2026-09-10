# Three certified searches for an off-critical zeta zero

**Research only. No off-line zeta zero was found, and RH is neither proved nor
disproved here. Every conclusion below is a certified enclosure or an explicitly
labelled negative result, and all three experiments require independent review.**

Three deliberately high-variance, computationally light experiments were run,
each aimed at exhibiting a certified violation of a condition that RH implies.
A single certified violation in any one of them would refute RH. None occurred.
What the runs do produce is quantitative: detection boundaries, exclusion
windows, a self-contained lower bound on the de Bruijn–Newman constant, and the
first certified margin measurements for two families of RH-necessary predicates
that this repository already owned but had never evaluated against actual data.

All arithmetic is Arb ball arithmetic through `python-flint`. "Certified
negative" means the **entire** ball lies below zero, decided by Arb's comparison
operator, never by a midpoint.

| | Experiment | Mechanism | Certified violation? |
|---|---|---|---|
| **E1** | `e1_pick_loewner.py` | the repository's derivative-free xi/Pick/Loewner predicates, swept against actual zeta | none |
| **E2** | `e2_dbn_laguerre.py`, `e2_modes.py` | Laguerre inequality on the de Bruijn–Newman heat flow | none at t = 0 |
| **E3** | `e3_weil_form.py` | Weil explicit-formula quadratic form, minimised adversarially | none; form certified positive definite |

## E1 — sweeping the repository's own disproof architecture

`research/integrated/xi/derivative-free-pick-loewner.md` proves five value-only
predicates that any RH failure must violate, and proves the local converse: an
off-line pair creates an **open** negative basin, so a witness has positive
measure. That packet's own closing line is *"the remaining burden is precise:
authenticated primitive production and strict witness discovery"*, and its
assurance note records that the integration performed no Riemann–Siegel, zero,
or interval production replay. Before this run the predicates had been evaluated
at two ordinates in total.

Implemented here: the secant `S`, two-channel `A`, cross-Loewner 2x2 minors,
barycentric Pick localisers and alternating divided differences, at 13 dyadic
offsets `2^-17 ... 2^-5`, giving 203 certified predicates per ordinate. Every
point is checked to lie strictly right of the critical line and every `zeta`
enclosure is checked to justify the division before `F = xi'/xi` is formed;
points failing that test are rejected, not repaired.

**Detection calibration.** `results/e1_calibration.json` injects a synthetic
off-line pair at displacement `delta` and ordinate offset `tau` into the
RH-form resolvent against a realistic local zero field, and bisects for the
largest `tau` still detected. Every `delta` from `1.6e-2` down to `7.6e-6` is
detected, and the detection window scales like `tau_max ~ sqrt(delta)` — far
wider than `delta` itself, which is what makes a sweep on a feasible ordinate
grid meaningful rather than hopeless.

## E2 — de Bruijn–Newman flow and the Laguerre inequality

With `Phi(u) = sum_n (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u})`
and `H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(zu) du`, the de Bruijn–Newman
constant is `Lambda = inf{t : H_t has only real zeros}`; RH is equivalent to
`Lambda <= 0`, and Rodgers–Tao give `Lambda >= 0` unconditionally. So RH holds
here with **zero margin**, which is why this is the sharpest available pressure
point.

For a real entire function with only real zeros the Laguerre inequality holds
pointwise: `L_t(x) = H_t'(x)^2 - H_t(x) H_t''(x) >= 0`. Since
`L_t = H_t^2 sum_k 1/(x - z_k)^2`, a conjugate pair `a +/- i b` contributes
`2[(x-a)^2 - b^2]/((x-a)^2 + b^2)^2`, which is `-2/b^2` at `x = a`: a tight
complex pair drives `L_t` strictly negative near its real part. Hence

* a certified `L_0(x) < 0` proves Xi has a non-real zero — **RH is false**;
* a certified `L_t(x) < 0` for `t < 0` proves `Lambda > t`.

Nothing in E2 uses a zeta evaluator or a zero table; everything comes from
`Phi` and Arb's rigorous integrator. The normalisation was pinned by the run
itself: `H_0(z)` is proportional to `Xi(z/2)`, confirmed by a certified sign
change bracketing `z = 2 x 14.134725...`, and the census independently recovers
`z = 28.25, 42.25, 50.25, 60.75, 65.75, 75.25`, i.e. twice the classical
ordinates `14.13, 21.02, 25.01, 30.42, 32.94, 37.59`.

## E3 — adversarial minimisation of the Weil quadratic form

For `f` supported in `[0, A]`, `g = f * f~` and `h = |f-hat|^2 >= 0` on the reals,
Weil's explicit formula expresses `sum_rho h(gamma_rho)` through `Lambda(n)` for
`n < e^A` plus Gamma-function integrals — **no zeta evaluation and no zero data
at all**, which makes E3 an genuinely independent path from E1 and E2. With `f`
a combination of translated hats the functional is a quadratic form in the
coefficients depending only on `|j - k|`, so the matrix is symmetric **Toeplitz**
and only `N` distinct entries are needed. A certified negative `LDL^T` pivot
refutes RH; all pivots certified positive proves that no test function in the
whole family violates Weil positivity.

**This experiment initially reported a refutation of RH, and that report was a
bug.** Two defects were found and fixed, both by the validation step rather than
by inspection:

1. the sieve returned the prime `p` where the von Mangoldt weight `Lambda(n) = log p`
   was required;
2. the piecewise-cubic B-spline was evaluated through certified branch
   comparisons that silently select the wrong branch on a ball straddling a knot,
   and `v.real` inside the integrand made it non-holomorphic, which invalidates
   Arb's rigorous integration error bounds outright.

`e3_validate.py` is the safety net that caught both: it compares each `tau(m)`
against a direct sum over zeros obtained independently from mpmath's Hardy Z
function. It is a cross-check only and is never on an acceptance path. It now
reports agreement to about `1e-9` on every coefficient tested.

## Reproduce

```
pip install python-flint mpmath numpy
python3 e1_pick_loewner.py calibrate --prec 300 --out results/e1_calibration.json
python3 e1_pick_loewner.py sweep --t0-num 3000000000000 --step-num 3 --step-den 16 \
        --count 400 --budget 7000 --out results/e1_sweep_high_coarse.json
python3 e2_dbn_laguerre.py selftest --out results/e2_selftest.json
python3 e2_modes.py census --zlo 26 --zhi 1500 --step 0.3 --out results/e2_census.json
python3 e3_validate.py 0.25 9          # must print VALIDATION: PASS
python3 e3_run_all.py
python3 tests.py
```

`RESULTS.md` states what each run establishes and, more importantly, what it
does not. `VALIDATION.md` records the assurance boundary, including the two
bugs above and the limits of the ordinate grid.
