# L-91784 — Native `Y_4` slack obeys the subcritical causal recurrence

Claim ID: `L-91784`  
Status: **PROVED EXACT ABSTRACT CONSUMER**  
Created: 2026-08-15  
Depends on: positive radix-four dual `L-91378`; causal coefficient budget  
RH status: **unproved**

Let

\[
 \mathcal D(X)=\sum_qY_4(q)s_X(q),
 \qquad
 s_X(q)=\Omega_X(q)-\Xi_{d_X}(q)\ge0.
\]

Assume one source-owned native decomposition gives

\[
 \mathcal D(X)
 \le g(X)+\sum_b\alpha_b\mathcal D(Y_b),
 \qquad
 \sum_b\alpha_b\le\rho<\frac18,
 \qquad
 Y_b\le X/67+C_0.
\tag{L-91784.1}
\]

If `g(X)<=C log(3X)+C_1`, then iteration gives

\[
 \boxed{\mathcal D(X)=O(\log X)=o(\log^2X).}
\tag{L-91784.2}
\]

If `g` is bounded, then `D(X)=O(1)`. Indeed, after `n` generations the total
coefficient mass is at most `rho^n`, while the endpoint scale is at most
`X/67^n+O(1)`. Summing the geometric series, including the logarithmic scale
loss, proves (L-91784.2).

The quantity in this recurrence is the **native positive weighted slack** from
`L-91378`. It is not a continuum equality score and no identity between those
two quantities is used. A producer must still establish (L-91784.1) in the
one-use native normalization.
