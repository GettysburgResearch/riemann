# X-4201 — Exact rational gate and prime-entry geometry for optimized carriers

Status: exact rational parameter/correction-bound verification and exact event regression  
Authoring agent: `gpt56-05-e`  
Issue: #42  
Related claims: L-4201, L-4202, L-4203, L-4204, O-4201

## Purpose

PR #44 reports a very small positive complete-prime leading margin at

```text
c = 10^11
K = 1024
T = 4709203636353.65
margin = +0.00026896626427230785
```

but omits the exact D-0801 archimedean and pole matrices. X-4201 checks, using
only exact rational arithmetic, that the uniform nonprime correction envelope
from L-4202/L-4203 is below `2.5e-10` at this parameter cell.

The experiment also contains `prime_entry.py`, an exact Gaussian-rational
regression of L-4204's first deposition cell. It checks the corner matrix,
fixed-vector formula, derivative limit, endpoint-neutral directions, unit-phase
requirement, and first-cell norm cap after stripping the common positive factor
`log(p)/(pi*sqrt(q))`.

The correction checker intentionally does **not** evaluate:

- the prime phases;
- a Toeplitz eigenvalue;
- `log`, `pi`, `sinh`, `cosh`, or `Ci` numerically;
- an archimedean integral;
- the Riemann zeta or xi function.

It substitutes elementary rational inequalities into the proved analytic
bounds.

## Exact parameter treatment

The displayed carrier decimal is interpreted exactly as

\[
 T=\frac{94184072727073}{20}.
\]

For `L=log(10^11)=11 log 10`, the checker uses

\[
 22<L<\frac{638}{25}.
\]

The upper inequality is supported by the exact finite sum

\[
 \sum_{n=0}^{6}\frac{(58/25)^n}{n!}
 =\frac{110699859859}{10986328125}>10.
\]

Thus `exp(58/25)>10` and `log 10<58/25`. The lower inequality follows from the
classical elementary estimate `e<3`, hence `e^2<9<10`.

Therefore

\[
 b=\frac{2L}{1024}<\frac{319}{6400}<\frac1{20},
\]

which proves applicability of L-4202.

The checker also uses the elementary geometric inequality `pi>3`.

## Reconstructed bounds

The exact rational upper endpoints have the decimal sizes

```text
archimedean operator upper  1.7781072071831001710e-10
pole operator upper          1.6672791396873303641e-16
combined operator upper      1.7781088744622398584e-10
```

The certificate claims only the looser compact thresholds

```text
archimedean < 1 / 5,000,000,000
pole         < 1 / 5,000,000,000,000,000
combined     < 1 / 4,000,000,000
```

The empirical PR #44 margin string is greater than `1/4000`. Comparing only
those safe threshold values gives a factor of exactly one million. Comparing
the exact reconstructed upper with the reported decimal gives approximately
`1.5126535e6`.

The latter is a **scale comparison only**. The margin has not been converted to
a directed mathematical lower bound.

## Pole-envelope substitutions

The checker derives a deliberately loose pole bound using

\[
 \sinh(L/2)<\frac{\sqrt{10^{11}}}{2}<160000,
\]

\[
 \cosh^2(\pi h/2)<4,
\]

\[
 \pi^2h=\frac{\pi L}{2K}>\frac{3\cdot22}{2K},
\]

and

\[
 \sinh(\pi h)>\pi h=\frac{L}{2K}>\frac{22}{2K}.
\]

No floating hyperbolic evaluation is trusted.

## Prime-entry exact regression

For `K=8` and the dimensionless first-cell coordinate

\[
 \eta=\frac{\varepsilon}{L_0}=\frac1{100},
\]

`prime_entry.py` reconstructs

\[
 \tau_{K-1}=\frac{K\eta}{1+\eta}=\frac8{101}.
\]

With the exact unit phase

\[
 \frac35-\frac45i,
\]

the stripped corner coefficient has norm `4/101`. The tests independently
evaluate the two corner entries and the closed fixed-vector formula, verify

\[
 \frac{\tau_{K-1}}{2\eta}=\frac{K/2}{1+\eta}\to\frac K2,
\]

and require exact annihilation when either endpoint coordinate vanishes.

These are algebraic controls only; no actual prime phase is represented.

## Files

- `verify.py` — exact standard-library correction checker;
- `prime_entry.py` — exact Gaussian-rational L-4204 event kernel;
- `certificates/c11-k1024.json` — compact machine-readable correction certificate;
- `tests/test_verify.py` — threshold and proof-boundary mutation tests;
- `tests/test_prime_entry.py` — first-cell event regressions;
- `results/tests.txt` — recorded executed summary.

## Reproduction

```bash
python verify.py certificates/c11-k1024.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py prime_entry.py tests
```

Fourteen tests pass.

## Adversarial coverage

The tests require:

- exact reconstruction of the small-cell bound `319/6400`;
- exact reconstruction of the degree-six exponential control;
- rejection of an unjustifiably tighter total threshold;
- rejection if the empirical margin is relabeled as certified;
- rejection of a changed cell count;
- rejection of an inflated scale factor;
- exact harmonic helper controls;
- exact first-cell hat geometry;
- equality of corner-matrix and fixed-vector formulas;
- the correct one-sided derivative limit;
- endpoint-neutral event annihilation;
- first-cell boundary rejection;
- rejection of a nonunit synthetic phase.

## Proof boundary

Conditional on the proposed analytic normalization inherited by L-4201 through
L-4204, the correction and event formulas are rigorous.

The following are **not** certified by X-4201:

- the complete prime Toeplitz coefficients;
- huge-phase range reduction;
- summation rounding;
- the leading eigenvalue or frozen eigenvector;
- D-0801 admissibility;
- the Guinand--Weil sign convention.

Accordingly, the correction checker status is

```text
RIGOROUS_CORRECTION_BOUND_EMPIRICAL_MARGIN_ONLY
```

and never a candidate or counterexample status.

## Immediate use

A directed prime producer now has a simple terminal comparison. For a frozen
unit dyadic vector, emit a rigorous interval for

\[
 v^*(\ell_T I-S_K)v.
\]

If its lower endpoint exceeds `2.5e-10`, the exact full D-0801 value is positive
on that vector. If its upper endpoint is below `-2.5e-10`, the exact nonprime
corrections cannot erase the negative sign.

For cutoff exploration, use L-4204's endpoint susceptibility to rank prime-power
thresholds before performing full continuation.
