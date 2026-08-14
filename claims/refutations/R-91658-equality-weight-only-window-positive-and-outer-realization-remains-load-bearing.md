# R-91658 — The equality weight is only window-positive; the first hardening draft removed a load-bearing realization layer

Claim ID: `R-91658`  
Status: **EXACT SCOPE CORRECTION AND FINAL HARDENING FIREWALL**  
Created: 2026-08-14  
Corrects on PR #455: the first versions of `L-91669` and `T-91655`  
Replacement: corrected `L-91669` and corrected `T-91655`  
RH status: **unproved pending independent reconstruction**

## 1. The signed/global versus positive/window distinction

The exact reciprocal-zeta equality weight is

\[
 L_*(u)=
 \sum_{n\le e^u}\frac{\mu(n)}{\sqrt n}
 \left(2e^{(u-\log n)/2}-1\right).
\]

`L-26204/L-91107` identify its transform and explicitly state that global
positivity is RH-bearing.  The repository proves only

\[
 L_*(u)>0.3186
 \qquad
 0\le u\le\log(c_0^{-1}),
\]

on the fixed first factor-\(54.2\) quotient window.

The first hardening draft wrote the root target and score as though one positive
direct arithmetic packet could consume the complete equality state without the
finite-window endpoint realization.  That was too compressed.  It could be
read as either:

```text
assuming global positivity of L_*;
or identifying the continuum score packet with c_X merely from equal target.
```

Neither inference is permitted.

## 2. The outer realization remains load bearing

The correct route retains:

```text
finite-window positivity L-91107;
one positive endpoint quantization L-91110;
one collar and mismatch repair L-91111/L-91114;
one top omission L-91115;
the corrected one-use boundary reserve where invoked;
the score/normalization bridge L-91557.
```

These objects are current-owned and used once.  They are not deleted, and they
are not added as an independent second copy of the exact native row.  They form
the realization map by which the continuum equality score datum enters the
finite common-row construction.

## 3. What the direct-row theorem actually supplies

`L-91668` supplies the exact labelled arithmetic source identity and identifies
its observation with

\[
 c_X(j)=
 \sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\]

`L-91663` supplies the exact ordinary/detail response and same-index child
replacement after the complete current row is summed.  These theorems close the
physical recursive gate rejected by PR #450.  They do not, by themselves,
replace the continuum-to-finite score realization of `L-91557`.

Thus the final architecture is:

```text
finite positive equality window and one-use realization
 -> exact labelled finite native row
 -> leafwise Hall
 -> same-index child replacement
 -> coefficient-one score transfer
 -> logarithmic debt.
```

## 4. Supersession

```text
first L-91669 statement “outer packet not load bearing”      withdrawn
first T-91655 root score shortcut                            withdrawn
global positivity of L_*                                    never assumed
corrected L-91669 one-use realization/direct-row ledger      normative
corrected T-91655                                            normative
```

The Git history intentionally preserves the withdrawn draft; this refutation
prevents a reviewer from mistaking it for a valid alternate proof.

## 5. Exact review obligation

A reviewer must verify the normalization bridge, not merely the two endpoint
claims separately:

1. the continuum equality datum in `L-26204/L-91557`;
2. the positive finite-window endpoint realization in `L-91107--L-91115`;
3. the exact finite native observation in `L-91668`;
4. the statement that these are two stages/representations of the same root
   equality packet, with every current correction used once.

A mismatch at this interface rejects the full proposal while leaving the new
source-partition theorem and fixed-\(67\) score theorem intact.

```text
global L_* positivity                            NOT CLAIMED
finite-window L_* positivity                      LOAD BEARING
outer realization                                 LOAD BEARING / ONE USE
direct arithmetic packet                          LOAD BEARING
scalar target equality alone                       INSUFFICIENT
Riemann Hypothesis                                 UNPROVEN PENDING REVIEW
```
