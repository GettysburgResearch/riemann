# Exact row peel and Boolean renewal — SUPERSEDED BY `R-91102`

> **Do not use the former exact-row-peel conclusion.** The Volterra integral
> generates the continuum equality seed, not the finite Riemann-sum equality
> seed. `R-91102` gives an exact counterexample at `X=3,m=2`, and `L-91112`
> is now marked refuted.

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Status: **SUPERSEDED / HISTORICAL REPORT**; RH remains unproved

## Correct surviving results

- rank-two endpoint geometry and score-positive butterflies;
- positive factor-54 continuum density;
- positive B-spline quantization and width-three collar;
- finite Euler correction and quotient-knot packets;
- 33-state parity shadow and globally positive sixteen-prime Boolean forcing;
- delayed rough-prime renewal identity.

The claimed identity

```text
finite equality seed = continuum Volterra endpoint integral
```

is false. Consequently the former claims of exact finite outer saturation,
exact terminal saturation and zero outer score debt are withdrawn.

## Corrected finite result

`L-91114` proves

\[
 E_X(n)-E_X(n+1)
 =d_X^\star(n)-\int_n^{n+1}d_X^\star(t)dt,
\]

and the explicit bounds

\[
 |\mathcal D_4v_q(E_X)|<32q^{-3/2},
\]

\[
 \frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}<\frac{174}{K}
 \qquad(K\le q\le X/4).
\]

Thus a nonnegative factor `(1+175/K)^(-1)` pays the finite mismatch and the
positive quantization collar on every interior outer column at bounded score
cost.

## Honest frontier

```text
false exact finite-row shortcut                   REFUTED
finite mismatch + interior collar                 PAID QUANTITATIVELY
terminal taper                                    BOUNDED QUOTIENT CERTIFICATE OPEN
sixteen-prime Boolean forcing                     POSITIVE / EXACT
rough-prime delayed inverse                       OPEN / RH-BEARING
capacity-faithful coefficient-one reset           OPEN
Riemann Hypothesis                                UNPROVEN
```

Current narrative:

```text
R-91102
L-91114
reports/gpt56-pro/2026-08-12-l91112-refutation-and-corrected-reset-frontier.md
reports/gpt56-pro/2026-08-12-finite-mismatch-gains-a-carry-derivative.md
```
