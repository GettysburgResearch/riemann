# X-90005 — z-collapse regression

Companion regression harness for `L-90005`.

Run:

```bash
python experiments/X-90005-zcollapse/verify.py
```

The script uses only the Python standard library. It checks:

- the corrected `N=7` continuum root `c_*` to a 2e-14 bracket;
- the finite profile margins used in the analytic proof (`Q_7`, `Q_8`, and the `N=2,4,6` interior maxima);
- direct exact-definition shell values around the small-`X` transition;
- every even endpoint through `X=20000` in a 26-integer band around `c_*X`.

Expected terminal line:

```text
PASS_X90005
```

The exhaustive/cofinal content of `L-90005` is **not** delegated to this script: the width-158 theorem is analytic. The scan is a mutation/regression check and also records that the observed transition is much tighter (`+3` on the scanned range).
