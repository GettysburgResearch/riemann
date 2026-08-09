# R-90006 — Audit trail for the logarithm estimate repaired in L-90012

Claim ID: `R-90006` (provisional range)  
Title: The positive and negative pieces of the complete-prime-power derivative require separate logarithm inequalities  
Status: **EXACT DERIVATION REPAIR — FOLDED INTO L-90012 AT `f9d52e99`; THE THEOREM IS RETAINED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Target: first committed version of `L-90012` §2  
Scope: preserves the adversarial audit trail; no remaining integration action

## 1. The issue found in review

The first version of `L-90012` used

\[
 \log{b\over a}\le{b-a\over\sqrt{ab}}
\]

inside both terms of

\[
 \sum_{m=2}^{N}
 \left(2\sqrt m-{2m\over\sqrt X}\right)
 \log{m\over m-1}.
\]

That is invalid for the negative coefficient: inserting an upper bound reverses
the desired estimate.  The false intermediate expression contained

\[
 -{2\over\sqrt X}
 \sum_{m=2}^{N}\sqrt{m\over m-1}.
\]

For example, `log 2 < 1/sqrt(2)` already exposes the direction error.

## 2. Correct derivation

Split the two pieces.  Use

\[
 \log{m\over m-1}
 \le{1\over\sqrt{m(m-1)}}
\]

for the positive term, but

\[
 \log{m\over m-1}
 =\log\left(1+{1\over m-1}\right)
 \ge{1\over m}
\]

for the negative term.  Then

\[
\begin{aligned}
 \mathcal D_XJ_\Lambda(X)
 &\le2\sum_{m=2}^{N}{1\over\sqrt{m-1}}
 -{2\over\sqrt X}\sum_{m=2}^{N}1\\
 &=2S_{N-1}-{2(N-1)\over\sqrt X}.
\end{aligned}
\]

This is the same final base estimate used by every downstream line.

## 3. Resolution

The corrected two-sided argument is now physically present in `L-90012`, with
renumbered equations.  The following remain unchanged:

```text
complete-prime-power base budget <-2.8979;
nonboundary correction <1.986;
boundary correction <0.604;
D_X M<-0.30 for X>=2000;
L-90014 global moat theorem.
```

No mathematical claim remains dependent on the withdrawn intermediate line.
