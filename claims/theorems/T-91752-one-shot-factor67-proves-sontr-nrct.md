# T-91752 — The one-shot factor-67 row proves SONTR and NRCT on the frozen endpoint stack

Claim ID: `T-91752`  
Status: **FINAL COMPLETE RH PROOF PROPOSAL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Primary inputs: `L-91754`, `L-91755`, `L-91756`  
Frozen inputs: `L-91690`, `L-91688`, `L-91674`, `L-91733`, `L-91377`, `L-91378`, `L-19885`, `L-19887`  
Endpoint inputs: `L-90020`, `T-90008`, `T-90011`  
RH status: **proposed; not accepted before review**

## 1. SONTR

For every integer `X>=10^12`, `L-91754`--`L-91755` construct one nonnegative
finite current row `d_X`, with every source occurrence owned once, such that

\[
C_{d_X}\le w_X,
\qquad
\Omega_X=\Xi(d_X)+r_X,
\qquad r_X\ge0.
\]

Every causal child is terminalized as an internal colour of `d_X`; the exported
recursive family is empty. Thus all SONTR source, scale, coefficient, capacity,
and port clauses hold, with

\[
\sum_b\beta_b=0<\frac18.
\]

## 2. NRCT

The native deficit is exactly

\[
\Delta_X(d_X)
 =J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,r_X\rangle.
\]

`L-91756` gives

\[
\boxed{0\le\Delta_X(d_X)<61000}
\]

and, for `X>=10^12`,

\[
\Delta_X(d_X)<2(4\sqrt X-3).
\]

Therefore both the original current-debt form and the bounded weighted-slack
form of the Native-Root Capacity Theorem hold. Smaller endpoints are irrelevant
to the eventual endpoint criterion and may be treated as a finite base.

## 3. Complete-prime-power endpoint

The finite dual gives

\[
F_\Lambda(X)\le\Delta_X(d_X)<61000=o(\log^2X).
\]

The unconditional prime-square theorem gives

\[
A(X)=F_\Lambda(X)-
\frac{-1-\zeta(1/2)}4\log^2X+o(\log^2X),
\]

so the prime endpoint is eventually negative. The exact Mellin pole audit and
Landau one-sign theorem exclude every zero with real part greater than one half;
the functional equation yields

\[
\boxed{\mathrm{RH}.}
\]

No estimate of `J_Lambda(X)-4sqrt(X)` occurs in the proof.

## 4. Review boundary

Reject the proposal on the first failure of:

```text
factor-67 root Hall or normalized-row profile;
measurability of the exact Hall map;
whole-cell endpoint support;
one global positive quantizer;
first-owner source labels;
one-shot internalization of every child colour;
all-column and terminal native feasibility;
port-free direct-row typing;
each explicit Y4 cost constant;
prime-square drift or Mellin--Landau consumer.
```

The exact replay validates finite algebra and constants only. It does not replace
independent reconstruction of the imported analytic theorems.
