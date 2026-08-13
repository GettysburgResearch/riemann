# L-91660 — The native endpoint deficit dominates the complete prime-power gap

Claim ID: `L-91660`  
Status: **PROVED EXACT FINITE BRIDGE; RH CONSUMER FROZEN EXTERNALLY**  
Created: 2026-08-13  
Depends on: the exact average-binomial/von-Mangoldt identity; `L-91653`, `L-91659`  
External implication chain: PR #353 `L-90020`, `L-90021`, `L-90023`, `T-90011`; PR #352 `T-90008`  
RH status: **conditional only on the subquadratic deficit estimate**

## 1. Native benchmark and dual target

For the native datum `N_X` of `L-91659`, put

\[
J_\Lambda(X)=\sum_nd_X^{(0)}(n)G_n,
\]

where `d_X^(0)` is the positive parabolic seed, and

\[
P_\Lambda(X)
=\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

The complete prime-power gap is

\[
\boxed{
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
}
\tag{L-91660.1}
\]

## 2. Feasibility gives the dual score bound

Let `d(n)>=0` be ordinarily feasible for the native target:

\[
\sum_nd(n)\beta_{nq}
\le w_X(q)
=\frac1{\sqrt q}\log\frac Xq
\qquad(q\ge2).
\tag{L-91660.2}
\]

The exact finite von-Mangoldt identity is

\[
G_n=\sum_{q\le n}\Lambda(q)\beta_{nq}.
\tag{L-91660.3}
\]

All sums are finite and `Lambda(q)>=0`. Therefore

\[
\begin{aligned}
\operatorname{Score}(d)
&=\sum_nd(n)G_n\\
&=\sum_q\Lambda(q)\sum_nd(n)\beta_{nq}\\
&\le\sum_q\Lambda(q)w_X(q)
=P_\Lambda(X).
\end{aligned}
\tag{L-91660.4}
\]

No asymptotic estimate and no branch-qualified optimization theorem is needed for this inequality.

## 3. Deficit dominates the complete gap

For every feasible `d`, equations (L-91660.1) and (L-91660.4) give

\[
F_\Lambda(X)
\le J_\Lambda(X)-\operatorname{Score}(d).
\tag{L-91660.5}
\]

Taking the infimum over signed losses, equivalently the supremum over feasible scores, yields

\[
\boxed{
F_\Lambda(X)
\le\Delta_X(\mathcal N_X).
}
\tag{L-91660.6}
\]

The sign is now explicit: feasibility bounds the score from above, so subtracting the score bounds the gap from above.

## 4. Frozen RH implication

The external frozen chain supplies:

1. `L-90020`: the higher-prime-power source has the unconditional asymptotic
   \[
   F_\Lambda(X)-A(X)
   =\frac{-1-\zeta(1/2)}4\log^2X+o(\log^2X).
   \]
2. `T-90008`: eventual negativity of the prime-only endpoint `A(X)` implies RH.
3. `T-90011`: consequently
   \[
   F_\Lambda(X)=o(\log^2X)\Longrightarrow\mathrm{RH}.
   \]

Therefore

\[
\boxed{
\Delta_X(\mathcal N_X)=o(\log^2X)
\Longrightarrow\mathrm{RH}.
}
\tag{L-91660.7}
\]

The exact external paths, source commits, and blob SHAs are recorded in the full-ledger dependency lock. This lemma no longer delegates the sign to the branch-qualified `L-90029` prose.

```text
feasible score <= complete prime-power ramp        EXACT
F_Lambda <= native deficit                         EXACT
subquadratic F_Lambda -> RH                        FROZEN EXTERNAL CONSUMER
unconditional subquadratic native deficit          OPEN / PROPOSED BY T-91652
Riemann Hypothesis                                 UNPROVEN
```
