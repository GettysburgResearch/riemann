# M-19701 — Proof gate for the complete selected-real-zero kernel

Claim ID: `M-19701`  
Title: Separate old radical tails from the off-line-cardinal defect before claiming a cofinal kernel floor  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-o`  
Created: 2026-07-31  
Dependencies: `L-19701`, `T-19701`, `R-19701`

## Required packet ledger

Every production kernel packet must partition its basis metadata into:

```text
OLD_EXACT_RADICAL_TRUNCATION
SELECTED_LINE_CARDINAL_REMAINDER
ADDED_DEFICIT_KERNEL_DIRECTION
OTHER_EXPLICIT_SOURCE
```

A direction may be labeled radical-like only after an exact global radical
preimage and a form/metric error certificate have been supplied.

## Required complete synthesis certificate

For a basis map `J`, global radical synthesis `R`, error `E=J-R`, complement
block `C`, and cross map `Z`, certify

\[
 |Q(Ea,Ea)|+\|C^{-1/2}ZJa\|^2
 \le\eta\|Ja\|_G^2
\]

for every coefficient vector. The proof object must bind:

1. the complete basis, including all added deficit-kernel directions;
2. the denominator metric and its lower Gram;
3. exact radical provenance for every synthesis column;
4. a complete form error matrix or a rational Loewner radius;
5. the complete Schur cross correction;
6. one strict rational upper bound for `eta`.

## Mandatory negative control

Every checker must include the conjugate-cardinal block

\[
 m\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

and reject any certificate that attempts to classify its difference vector as a
small radical tail.

## Promotion rule

A cofinal kernel-floor claim may be promoted only if it either:

- proves the complete synthesis inequality with `eta_j->0`; or
- supplies another theorem that explicitly excludes every off-line-cardinal
  difference.

A packet count, selected-zero rank, `L2` density statement, or positive ambient
complement is not a substitute.
