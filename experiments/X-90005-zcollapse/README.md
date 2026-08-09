# X-90005 — z-collapse certification and regression

Companion artifacts for `L-90005`.

## Exact finite certificate

Run:

```bash
python experiments/X-90005-zcollapse/certify_finite.py
```

This uses only exact `fractions.Fraction` arithmetic plus integer-square-root
rational enclosures.  Every logarithm is enclosed by the positive atanh series
with an exact geometric tail bound after power-of-two range reduction.

It certifies the finite inequalities used by the analytic proof:

- the omitted small even knot increments `N=2,4,6`;
- directed signs/brackets for `Q_7` and `Q_8`;
- the `N=2,4,6` interior concave maxima;
- the fact that the critical points for `N=3,5,7` lie left of their cells;
- the rigorous `N=7` root bracket
  `0.14085203501383 < c_* < 0.14085203501385`;
- the `P_7'<=-1.7` transition derivative;
- the `-0.169 < C/h < 0.268` transition correction bounds;
- `F(5)>0.0155` for the cofinal integral comparison;
- the remaining direct `N=8,9,10` secant cases, including the exceptional
  divisible `N=8` lower bound.

Expected terminal line:

```text
PASS_X90005_EXACT_FINITE_CERTIFICATE
```

## Floating regression scan

Run:

```bash
python experiments/X-90005-zcollapse/verify.py
```

This standard-library regression harness checks:

- the corrected `N=7` continuum root `c_*` numerically;
- the same finite profile margins;
- direct exact-definition shell values around the small-`X` transition;
- every even endpoint through `X=20000` in a 26-integer band around `c_*X`.

Expected terminal line:

```text
PASS_X90005
```

The cofinal width-158 theorem itself is analytic; it is not delegated to a
finite scan.  `certify_finite.py` discharges only the finitely many exact seeds
used inside that analytic argument.  `verify.py` is a mutation/regression check
and records that the observed transition is much tighter (`+3` on the scanned
range).