# Saddle-concentration addendum to the Xi reverse–Rolle programme

Date: 2026-08-30  
PR: #767  
Status: **general zero-localization theorem proved; Xi saddle estimate open**

The exact real descent theorem leaves two tasks: produce a high derivative with no off-line zeros in the target rectangle, and transport the discrete reverse–Rolle defect down to Xi.

`L-107102` supplies a clean sufficient theorem for the first task. A sine/cosine transform of a positive frequency measure supported in a window of relative width at most `1/32` has a strict Laguerre reserve on `|t| delta <=1/32`. If the stronger complex concentration condition

```text
delta (T+H+1/u0) exp(delta H) <= c0
```

holds, every zero in `|Re z|<=T`, `|Im z|<=H` is real and simple and corresponds to a zero of one carrier sine or cosine.

For Xi derivatives the positive measure is

```text
nu_k(du) proportional to u^k Phi(u) du.
```

The expected Laplace saddle has logarithmic centre and width

```text
delta_k ~ sqrt(log k/k).
```

A rigorous weighted-tail theorem at this scale would force `Xi^(k)` to have only real zeros in the complete critical strip below height

```text
T << sqrt(k/log k).
```

This is a concrete, falsifiable high-derivative theorem. It is much stronger than a percentage statement and does not require selecting the derivative order after observing a zero.

The remaining analytic target is now:

```text
XISADDLE107110:
  prove the stated concentration and weighted-tail bounds for Riemann's
  positive Fourier kernel uniformly in k.
```

The remaining descent target is:

```text
XICURV107110:
  control the accumulated discrete reverse-Rolle defects using the exact
  nonreal-pair curvature budget plus Xi-specific Pick/Loewner depth and
  separation estimates.
```

Neither target is proved here. RH remains unproved.