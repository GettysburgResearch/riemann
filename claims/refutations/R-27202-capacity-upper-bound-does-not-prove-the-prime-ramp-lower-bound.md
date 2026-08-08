# R-27202 — The old capacity upper bound does not prove the prime-ramp lower bound

Claim ID: `R-27202`  
Title: `L-23809.2` has the wrong logical orientation for its advertised conclusion; the MFT implication requires a direct entropy-versus-unweighted-carry comparison  
Status: **DERIVATION REJECTED; CONCLUSION REPAIRED BY `L-27203/T-27202`**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Frozen target: PR #247 `L-23809`  
Scope: logical correction only; does not refute MFT

## 1. Frozen inference

The frozen argument established, for a nonnegative balanced flow,

\[
\log\binom nj\ge h_\eta n-O(\log X)
\tag{R-27202.1}
\]

and an **upper** capacity bound

\[
\mathcal M_X:=\sum_{n,j}n d_{n,j}
\le \frac{4}{h_\eta}\sqrt X+O(\log X).
\tag{R-27202.2}
\]

It then claimed

\[
\sum_{n,j}d_{n,j}\log\binom nj
\ge4\sqrt X-X^{o(1)}.
\tag{R-27202.3}
\]

But (R-27202.1) gives a lower bound proportional to `M_X`, while
(R-27202.2) bounds `M_X` from above. These two inequalities do not imply
(R-27202.3).

Thus the displayed derivation is invalid even if both inputs are correct.

## 2. What survives

The exact atomized identity survives:

\[
\log\binom nj
=
\sum_{q=p^a\le n}\Lambda(q)\chi_{n,j}(q).
\tag{R-27202.4}
\]

The MFT cone and its Farkas dual also survive. The failure is only the proposed
route from capacity to the sharp constant.

## 3. Repair

`L-27203` compares the entropy directly with the **unweighted** total carry
count

\[
\kappa(n,j)=\sum_{q=2}^{n}\chi_{n,j}(q).
\]

Both quantities have the same main term `n h(j/n)`, and their difference is
`O(sqrt(n))`. Feasibility itself gives

\[
\sum_{n,j}d_{n,j}\sqrt n=O_\eta(\log^2X),
\]

so the total comparison loss is polylogarithmic. This yields the desired sharp
prime-ramp lower bound with the correct orientation.

## 4. Classification

```text
L-23809 capacity estimate                   RETAIN AT ITS OWN SCOPE
L-23809 capacity -> sharp lower bound        REJECTED
MFT -> sharp prime ramp conclusion           REPAIRED BY L-27203/T-27202
MFT existence                                OPEN
RH                                           UNPROVED
```
