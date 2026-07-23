# X-4701 — Exact synthetic controls for derivative-free xi witnesses

Status: exact finite synthetic regression; **not** a Riemann-xi computation  
Authoring agent: `gpt56-05-d`  
Related claims: L-4701, L-4702, L-4703  
Issue: #47

## Purpose

This experiment tests the complete algebraic boundary of three proposed value-only RH counterexample certificates:

1. a negative two-point secant of
   \[
   J_T(u)=\sqrt u\,\operatorname{Re}(\xi'/\xi)(1/2+\sqrt u+iT);
   \]
2. a forbidden sign in a finite divided difference of `J_T`;
3. a negative minor of a cross-Loewner matrix formed from values at distinct nodes.

The implementation replaces the actual xi logarithmic derivative by the finite synthetic model

\[
 F_Z(s)=\sum_{\rho\in Z}\frac1{s-\rho}
\]

and evaluates it with Python integers and `fractions.Fraction`. It therefore checks signs, factors, node squaring, divided-difference orientation, and exact determinants. It cannot produce a counterexample to RH.

## Committed synthetic zero multiset

The control uses the symmetry-closed off-line quartet

\[
 \frac12\pm\frac1{10}\pm i
\]

plus one critical-line conjugate pair

\[
 \frac12\pm2i.
\]

All tests are performed at height `T=1`.

### Positive values but negative secant

At

\[
 x_1=\frac{11}{100},
 \qquad
 x_2=\frac3{25},
\]

both exact scalar values are positive:

\[
 \operatorname{Re}F_Z(1/2+x_1+i)
 =\frac{3251554390096064674600}{30985710308604170301}>0,
\]

\[
 \operatorname{Re}F_Z(1/2+x_2+i)
 =\frac{18140976575309525}{331424333649453}>0.
\]

Nevertheless the exact `u=x^2` secant is

\[
 -\frac{731547432466485699533503019750000}
 {338221466643089412116103100731}<0.
\]

This is the finite-model right-side signature of L-4701.

### First secants positive but a second divided difference has the forbidden sign

At offsets

\[
 \frac3{10},\quad\frac12,\quad\frac35,
\]

`J_T` is increasing at the sampled values, but the second divided difference is

\[
 \frac{23648036546125}{10185650056764}>0.
\]

Under RH L-4702 requires every second divided difference to be nonpositive.

### Every matrix entry positive but the minor negative

Use row offsets

\[
 \left(\frac3{10},\frac12\right)
\]

and column offsets

\[
 \left(\frac35,\frac7{10}\right).
\]

The exact cross-Loewner matrix is

\[
 \begin{pmatrix}
 70490142715/137643919686 & 685314459725/1083451791864\\
 14851413215/16808003394 & 131435077460/148840530813
 \end{pmatrix}.
\]

Every entry is positive, but its determinant is

\[
 -\frac{17481975069014214761675}
 {163895952553969442277744}<0.
\]

Thus the total-nonnegativity test in L-4703 can expose incompatible multi-point geometry even when all four sampled scalar secants look harmless.

## Files

- `verify.py` — exact Gaussian-rational evaluator and fail-closed checker;
- `certificates/synthetic-offline-value-witnesses.json` — machine-readable control;
- `tests/test_verify.py` — theorem-sign and mutation regressions;
- `results/tests.txt` — committed command output.

## Reproduction

```bash
python verify.py certificates/synthetic-offline-value-witnesses.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Eight tests pass.

## Adversarial coverage

The tests require:

- exact reproduction of all committed rational endpoints;
- rejection after mutating the secant numerator;
- rejection after mutating the determinant numerator;
- rejection of cross-equal value-only nodes;
- rejection of unsorted node lists rather than silently repairing them;
- alternating divided-difference signs for a finite on-line zero model;
- positive `2x2` and `3x3` cross-Loewner minors for an on-line model with enough distinct atom locations;
- explicit confirmation that positive entries can coexist with a negative determinant in the off-line control.

## Proof boundary

The committed negative quantities belong only to the explicitly listed finite synthetic zero multiset. No zeta or xi special function is called. No interval arithmetic, high-height reconnaissance, actual RH candidate, or `Z-####` identifier is present.

A real proof producer must replace `F_Z` with directed ball evaluations of the corrected D-3201 formula at exact dyadic points, prove every denominator nonzero, and leave the final sign separated under independent reconstruction.
