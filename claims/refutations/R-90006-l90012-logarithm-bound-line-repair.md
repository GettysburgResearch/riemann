# R-90006 — Scope repair for the logarithm estimate in L-90012.8

Claim ID: `R-90006` (provisional range)  
Title: The displayed intermediate bound in `L-90012.8` must use separate upper and lower logarithm inequalities; the final base estimate and theorem remain valid  
Status: **EXACT PRESENTATIONAL/DERIVATION REPAIR — THE THEOREM IS RETAINED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Targets: `L-90012` §2, equations (L-90012.7)--(L-90012.8)  
Scope: corrects one invalid intermediate inequality; no change to `L-90012.8`'s final bound or any downstream constant

## 1. The issue

`L-90012` writes

\[
 \log{b\over a}\le{b-a\over\sqrt{ab}}
\]

and then displays the intermediate estimate

\[
 \mathcal D_XJ_\Lambda
 \le2\sum_{r=1}^{N-1}{1\over\sqrt r}
 -{2\over\sqrt X}\sum_{m=2}^{N}\sqrt{m\over m-1}.
\tag{R-90006.1}
\]

The second term does **not** follow from the same upper bound: its coefficient
is negative, so the direction reverses. Indeed

\[
 \log2<{1\over\sqrt2}.
\]

Thus (R-90006.1) is not a valid intermediate inequality as printed.

## 2. Correct derivation

Starting from the exact formula

\[
 \mathcal D_XJ_\Lambda(X)
 =\sum_{m=2}^{N}
 \left(2\sqrt m-{2m\over\sqrt X}\right)
 \log{m\over m-1},
\]

split the positive and negative pieces before estimating.

For the positive piece use

\[
\boxed{
 \log{m\over m-1}
 \le{1\over\sqrt{m(m-1)}}.
}
\tag{R-90006.2}
\]

For the negative piece use the elementary lower bound

\[
\boxed{
 \log{m\over m-1}
 =\log\left(1+{1\over m-1}\right)
 \ge{1\over m}.
}
\tag{R-90006.3}
\]

The second inequality is `log(1+x)>=x/(1+x)` for `x>=0`.

Therefore

\[
\begin{aligned}
 \mathcal D_XJ_\Lambda(X)
 &\le
 2\sum_{m=2}^{N}{1\over\sqrt{m-1}}
 -{2\over\sqrt X}\sum_{m=2}^{N}1\\
 &=\boxed{
 2S_{N-1}-{2(N-1)\over\sqrt X}.}
\end{aligned}
\tag{R-90006.4}
\]

This is exactly the **final** bound asserted in `L-90012.8`.

## 3. Downstream proof is unchanged

Substitution of the explicit Euler--Maclaurin estimate for `S_(N-1)` still gives

\[
 \mathcal D_XJ_\Lambda(X)-2\sqrt X
 \le2\zeta(1/2)+{1\over\sqrt{N-1}}
 -{2(\sqrt X-\sqrt{N-1})^2\over\sqrt X},
\]

and hence the same base budget

\[
 \mathcal D_XJ_\Lambda(X)-2\sqrt X<-2.8979
 \qquad(X\ge2000).
\]

Every higher-prime-power estimate, the final `-0.30` margin, `L-90014`, and all
retained certificates are therefore unchanged.

## 4. Exact boundary

Withdrawn:

- only the intermediate displayed inequality (R-90006.1).

Retained after the corrected two-sided logarithm argument:

```text
L-90012.8 final bound;
L-90012.10--25;
D_X M<-0.30 for X>=2000;
L-90014 global moat theorem.
```

This correction is load-bearing for proof presentation and must be folded into
`L-90012` during integration.
