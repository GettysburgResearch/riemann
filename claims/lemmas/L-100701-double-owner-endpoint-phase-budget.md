# L-100701 — Double-owner endpoint phases have an exact bounded Cauchy budget

Claim ID: `L-100701`  
Status: **PROVED EXACT PHASE/PROBABILITY THEOREM**  
Created: 2026-08-20  
Depends on: `L-100700`; PR #672 `L-99990--L-99991`  
RH status: **not assumed**

Let `P_tau(gamma)=tau/[pi(tau^2+gamma^2)]` and let a multiplicative phase
observation satisfy

\[
O_\gamma U_p=p^{i\gamma}O_\gamma.
\]

For `p<q`, the two endpoint differences in a double-owner block contribute

\[
(1-p^{i\gamma})(1-q^{i\gamma}).
\]

The Cauchy characteristic function

\[
\int_{\mathbb R}e^{iu\gamma}P_\tau(\gamma)d\gamma=e^{-\tau|u|}
\]

gives the exact formula

\[
\boxed{
\begin{aligned}
&\int_{\mathbb R}
 |1-p^{i\gamma}|^2|1-q^{i\gamma}|^2
 P_\tau(\gamma)d\gamma\\
&\quad=4\left[
1-p^{-\tau}-q^{-\tau}
+\frac12\left((p/q)^\tau+(pq)^{-\tau}\right)
\right].
\end{aligned}}
\tag{L-100701.1}
\]

For a singleton endpoint,

\[
\boxed{
\int|1-p^{i\gamma}|^2P_\tau(\gamma)d\gamma
=2(1-p^{-\tau}).
}
\tag{L-100701.2}
\]

In particular the singleton cost is at most `2`, the double-endpoint cost is
at most `16`, and both vanish at the neutral phase before averaging.

Use the convex double-owner weights of `L-100700`. Since they sum to one,

\[
\boxed{
\sum_iw_{i,i}
 \int|1-p_i^{i\gamma}|^2P_\tau d\gamma
+
\sum_{i<j}w_{i,j}
 \int|(1-p_i^{i\gamma})(1-p_j^{i\gamma})|^2P_\tau d\gamma
\le16.
}
\tag{L-100701.3}
\]

Thus neither the number of active primes nor the two labelled copies of `67`
create a phase-energy loss after the least/greatest-owner decoupling.

## Direct-sum form

Let `O_gamma` take values in an auxiliary Hilbert space and integrate its norm
against `P_tau`. Applying `L-100700` with

\[
K=L^2(\mathbb R,P_\tau;K_0)
\]

is legitimate. The endpoint factors above are then exact multipliers, while
the unresolved interior Euler packet remains inside one block norm.

This closes:

```text
cross-block phase interference;
neutral endpoint mode;
prime-count accumulation at the two endpoints.
```

It does not bound the physical sum of distinct interior squarefree cores. The
remaining phase theorem is therefore a blockwise cross-core estimate, not a
local Euler-symbol estimate.
