# X-90301 — Claude signature-moment extension replay

Status: **DIAGNOSTIC FINITE REPLAY**  
Supports: `L-90301`, `T-90301`, `O-90302`  
Dependency: Python 3 standard library only

Run:

```bash
python3 verify.py
```

A successful run prints

```text
PASS_X_90301_CLAUDE_SIGNATURE_MOMENT
```

and writes `results/verification.json`.

## Checks

The script verifies or reproduces:

1. the optimized scalar constant
   \[
   c^*_{\lambda}
   =\frac{\sqrt2\tan(\lambda/\sqrt2)}
   {1+(\lambda/\sqrt2)\tan(\lambda/\sqrt2)};
   \]
2. the short-window/hybrid table for \(\lambda=\alpha/(1+\theta)\);
3. the threshold \(c^*_{\lambda}=1/2\), where the on-line/simple bound first becomes positive;
4. the elementary conductor-uniform omission bound
   \[
   \sum_{p\mid q}\frac{(\log p)^2}{p-1}\le\log q
   \]
   for every \(q\le100000\);
5. the exact logarithmic budget identity behind \(\lambda=\alpha/(1+\theta)\);
6. a pure-Python Gauss--Legendre/Nyström reconnaissance for the \(\xi'\) scalar-window Fredholm problem.

## Scope

The replay does **not** prove the short-window analytic asymptotics, the explicit formula, or RH. The theorem file contains the analytic proof reduction; this script checks constants and finite auxiliary claims only. The \(\xi'\) computation is exploratory, not an interval certificate.
