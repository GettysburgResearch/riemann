# R-90411 — Normalization correction for the first coarse-Haar gate statement

Claim ID: `R-90411`  
Title: `L-90417.12--13` omitted one factor of the parent size when switching from continuous carry energy to PIG-normalized energy  
Status: **EXACT CORRECTION / SUPERSEDING ERRATUM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Scope: normalization only; the bridge, triangular-window, radix-four scaling, and fine-tree theorems of `L-90416/L-90417` are unaffected

## 1. The two energy normalizations

For a carry field at parent `N`, `L-90416` proves

\[
 \int_0^1|Q_N(\theta)|^2d\theta
 =|\overline R_N|^2
  +\frac1N\sum_{u,\ell}|H_{u,\ell}|^2.
\tag{R-90411.1}
\]

The PIG row quantity has one additional division by the parent:

\[
 \boxed{
 \mathcal P_N
 :=\frac1N\int_0^1|Q_N(\theta)|^2d\theta.
 }
\tag{R-90411.2}
\]

Therefore

\[
 \boxed{
 \mathcal P_N
 =\frac{|\overline R_N|^2}{N}
  +\frac1{N^2}\sum_{u,\ell}|H_{u,\ell}|^2.
 }
\tag{R-90411.3}
\]

## 2. Correction

`L-90417.12--13` mixed (R-90411.1) and (R-90411.3): its prose declared PIG-normalized units while its displayed mean/coarse terms retained the continuous-energy scaling.

The corrected coarse-Haar gate is

\[
 \boxed{
 \frac{|\overline R_N|^2}{N}
 +\frac1{N^2}
  \sum_{\substack{\ell>\sqrt N\\u}}
  |H_{u,\ell}|^2
 \ll\log^B N.
 }
\tag{R-90411.4}
\]

Equivalently, before the final PIG division,

\[
 \boxed{
 |\overline R_N|^2
 +\frac1N
  \sum_{\substack{\ell>\sqrt N\\u}}
  |H_{u,\ell}|^2
 \ll N\log^B N.
 }
\tag{R-90411.5}
\]

The fine-tree theorem is unchanged:

\[
 \frac1{N^2}
 \sum_{\substack{\ell\le\sqrt N\\u}}
 |H_{u,\ell}|^2
 \ll\log N.
\tag{R-90411.6}
\]

## 3. Lifecycle instruction

Use (R-90411.4) or (R-90411.5) everywhere. Do not cite the uncorrected normalization in `L-90417.12--13` or the first continuation report/PR comment.

The exact structural claims remain valid:

```text
bridge representation;
Haar Parseval;
reflected triangular-window formula;
fine-tree bound;
radix-four factor-eight Haar recurrence;
four-adic atom bound;
fewer than sqrt(N) coarse coefficients.
```

This correction neither proves nor refutes deterministic PIG or RH.
