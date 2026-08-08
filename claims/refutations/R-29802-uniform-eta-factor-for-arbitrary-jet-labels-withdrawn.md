# R-29802 — Uniform eta factor for arbitrary unequal jet labels is withdrawn

Claim ID: `R-29802`  
Title: The literal tensor proof of one uniform eta factor applies only to identical internal labels; the actual cutoff ledger requires the Hausdorff-jet amortized budget  
Status: **SCOPE CORRECTION / ORIGINAL STRONGER DERIVATION WITHDRAWN**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29802`, `L-29806`

## 1. The stronger statement that does not follow

`L-29802` first wrote the eta pair as

\[
 {1\over2k}(e_{2k}\otimes v)
 -{1\over2k+1}(e_{2k+1}\otimes v)
\]

with one identical internal jet label `v`.  At that scope, residual mass plus logarithmic transport cost is bounded by a strict factor smaller than one.

In the actual finite cutoff ledger, the first-omitted shifted and unshifted legs may carry different internal values:

\[
 v_e\ne v_o.
\]

The literal tensor calculation does not by itself prove

\[
 \text{output boundary norm}
 \le\theta_*\,	ext{input norm}
\]

for an arbitrary pair of unrelated labels.

Therefore the following uses are withdrawn:

1. applying one uniform `theta_*` to every boundary jet solely by tensoring;
2. the corresponding diagonal entry `theta_*` in `L-29803` without first proving the actual source comparison;
3. any claim that local capacity feasibility alone is an all-generation strict contraction.

This correction does not affect the exact eta-comb decomposition or the identical-label statement on PR #294.

## 2. The actual source has additional order

The real cutoff labels are not arbitrary.  After the positive stopped-power resolution, they are finite differences or exact Euler remainders of pure powers.  `L-29806` proves that all such sequences are decreasing Hausdorff moment sources.

Hence, after matching the common paired tail,

\[
 v_e\ge v_o\ge0.
\]

This is sufficient for the exact capacity decomposition

\[
 M e_{2k}-T e_{2k+1}
 =(M-T)e_{2k}+T(e_{2k}-e_{2k+1}),
 \qquad 0\le T\le M.
\]

Moreover

\[
 (M-T)+T\log{2k+1\over2k}\le M.
\]

Thus the valid all-generation invariant is amortized:

```text
residual boundary source
+
paid Pascal objective cost
<=
incoming boundary source.
```

No uniform strict factor on the boundary state is required.

## 3. Endpoint mismatch

The first omitted shifted-even and unshifted-odd quotient indices need not coincide.  Their unmatched initial terms are not silently paired.  They remain in the explicit finite collar of PR #286 `L-28402`, whose complete first-generation capacity is polylogarithmic by the divisor-switch estimate.

Only the common infinite tail is subjected to the Hausdorff/eta pairing.

## 4. Corrected global state

The corrected global state is:

```text
analytic bulk
  -> factor-6/7 analytic bulk
     + positive boundary injection;

boundary source
  -> lower-scale residual boundary source
     + paid Pascal cost,
     with residual+cost <= incoming source.
```

Since the analytic injection is summable up to a polylogarithmic collar, total boundary source plus accumulated objective cost is polylogarithmic.

The corrected full proposal is `T-29802`.

## 5. Verdict boundary

```text
eta comb and identical-label local switch       retained exact
uniform theta_* for arbitrary unequal labels    withdrawn
Hausdorff decreasing-source comparison          proposed exact
amortized residual-plus-cost invariant           proposed exact
corrected RH composition                         T-29802 / pending review
```
