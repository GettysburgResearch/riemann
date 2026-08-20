# R-99810 — Diagonal energy and free labelled energy do not close the physical owner packing

Claim ID: `R-99810`  
Status: **PROVED EXACT COUNTERFAMILY / INTERFACE FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

## 1. Distinct clustered frequencies defeat every diagonal-only bound

Fix `tau>0`. For integers

\[
 n_j=N^3+j,\qquad 1\le j\le N,
\]

and coefficients `c_(n_j)=1`, the minimum-kernel form of `L-99810` satisfies

\[
 Q_\tau(c)
 =\sum_{j,k}\min(n_j,n_k)^{2\tau}
 \ge N^2(N^3)^{2\tau}.
\]

The diagonal is

\[
 \mathcal D_\tau(c)
 =\sum_jn_j^{2\tau}
 \le N(2N^3)^{2\tau}.
\]

Hence

\[
\boxed{
 \frac{Q_\tau(c)}{\mathcal D_\tau(c)}
 \ge2^{-2\tau}N.
}
\tag{R-99810.1}
\]

The frequencies are distinct integers. Therefore no universal estimate of the
form

\[
 Q_\tau(c)\le X^{o(1)}\sum_n|c_n|^2n^{2\tau}
\]

can be obtained from the diagonal alone when the packet may contain a
power-sized cluster. For the exact fixture `N=64`, `tau=1/2`,

\[
 Q/\mathcal D
 =\frac{33557227}{524353}>63.
\]

## 2. Free labelled energy is also insufficient by itself

The first-owner Littlewood–Paley identity lives in a labelled subset space.
If `N` orthogonal labels have the same physical observation, the collapse map
has norm `sqrt(N)`. This is the exact firewall of PR #660.

`L-99812` avoids applying that map abstractly by transporting the native
identity into the physical Hardy target first. Nevertheless, its current
Hardy norms still contain signed correlations among distinct squarefree cores.
The free labelled polylogarithmic budget cannot replace those correlations.

## 3. Consequence

The remaining theorem must exploit at least one source-prescribed structure:

```text
truncated native tails;
divisor-GCD owner squares;
future-completed first ownership;
compact multiplicative support;
prime-exchange or logarithmic-owner geometry.
```

A diagonal large sieve, source-blind Cauchy--Schwarz, arbitrary Hilbert
contraction, or finite scan does not prove `GPMOC99800`, `HTOC99810`, or
`DGOC99810`.