# Future corrections: all-rank conditioning and compact-input realization

**Status:** proposed component theorems; independent review needed.
**RH and the growing-horizon correction estimate remain unproved.**

This continuation of the delivered optimal-tail packet proves:

1. For the actual critical factorial source and the all-pass parameter 1/2,
   every (K+1)-dimensional source Gram satisfies
   `lambda_min >= exp(-8 sqrt(K+4))/(K+1)^2`.
   The entirely rational floor in PROOF (1.2) is available to a checker.
   The actual minimum eigenvalue nevertheless tends to zero; no infinite
   bounded inverse or RH premise is hidden in the finite theorem.
2. The actual source has the sharp small-shift law
   `||S_s d-d||^2 = s log(1/s)+O(s)` and an explicit global small-shift bound.
   This gives a quantitative box-input replacement and a complete stable-input
   cutoff. Every finite closed-domain correction can be realized to an explicit
   tolerance using an ordinary compact L2 input while preserving its prefix.
3. A specified rational degree-four all-pass correction at the unchanged tiny
   horizon `T=log2` has full error below `1/1200`. Replacing it by the prescribed
   compact input (box width `2^-40`, input cutoff `128`) leaves error below
   `1/1000`, compared with a seed error above `3/10`: over 300-fold in squared
   error. This is not an all-horizon theorem or a new approximation record.

Read [PROOF.md](PROOF.md), [NUMERICS.md](NUMERICS.md), and
[VALIDATION.md](VALIDATION.md). The remaining target is an upper bound on the
optimal corrected error as the exact-prefix horizon grows. Good conditioning
and finite error reduction do not imply that bound.

Run from this directory using standard-library Python:

```bash
python -B check.py
python -O -B check.py
python -B test_check.py
python -O -B test_check.py
```

No network access, zero census, external numeric library, or broad campaign is
needed. The finite arithmetic and analytic tail contracts are explicit. The
checker does not machine-prove the infinite analytic arguments. Prior packets
and their historical execution records are not silently rerun or upgraded.
