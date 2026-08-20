# R-100321 — The isolated `+3` jump is not the current jump

Claim ID: `R-100321`  
Status: **PROVED EXACT ALGEBRAIC FIREWALL**  
Created: 2026-08-20  
RH status: **not assumed**

Let

\[
A_N=\sum_{n\le N}\frac{\beta(n)}n,
\qquad
B_N=\sum_{n\le N}\frac{\beta(n)}{\sqrt n},
\qquad
C_N=3B_N-4\sqrt N A_N.
\]

A tempting mutation is to treat the jump of `3B_N` as the complete current
jump and write coefficient `+3` in front of
`beta(N+1)/sqrt(N+1)`.  This is false because `A_N` jumps at the same integer.

Direct substitution gives

\[
\begin{aligned}
C_{N+1}-C_N
={}&3\frac{\beta(N+1)}{\sqrt{N+1}}
-4(\sqrt{N+1}-\sqrt N)A_N\\
&-4\sqrt{N+1}\frac{\beta(N+1)}{N+1}.
\end{aligned}
\]

The two activation coefficients combine as

\[
3-4=-1.
\]

Hence

\[
\boxed{
C_{N+1}=C_N-\frac{\beta(N+1)}{\sqrt{N+1}}
-4(\sqrt{N+1}-\sqrt N)A_N.
}
\]

The replay mutates `-1` back to `+3` and rejects every nonzero activation.
This file is a standalone firewall for any future rank-one-current proposal;
it does not declare a current live pull request refuted.
