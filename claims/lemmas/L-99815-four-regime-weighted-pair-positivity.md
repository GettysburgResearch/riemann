# L-99815 — Three-regime proof of global active weighted pair positivity

Claim ID: `L-99815`  
Status: **PROVED EXACT FINITE-REGIME THEOREM**  
Created: 2026-08-20  
Depends on: `L-99813`; PR #658 `L-99703`  
RH status: **not assumed**

For an active pair `67<=p<q` and `y>=pq`, put

\[
\mathcal B_{p,q}\Phi(y)
=\Phi(y)-p^{-1/2}\Phi(y/p)-q^{-1/2}\Phi(y/q)+(pq)^{-1/2}\Phi(y/(pq)).
\]

Away from activation left limits, the four arguments can occupy only

```text
(2,2,2,0),
(2,2,2,1),
(2,2,2,2),
```

relative to the box regions `0:<1`, `1:[1,67)`, `2:>=67`. The formal pattern `(2,2,1,0)` occurs only on the pre-activation side `y<pq`; it is not an active native two-prime cube. At `y=pq`, the fourth term activates with `Phi(1)=0`, so the weighted block is continuous.

`L-99813` proves positivity in `(2,2,2,1)` and `(2,2,2,2)`. It remains only `(2,2,2,0)`.

Here `y,y/p,y/q>=67` and `y/(pq)<1`. Write

\[
\Phi(t)=A-Bt^{-1/2},\qquad
A=8(1-67^{-1/2}),\quad B=3\log67.
\]

Then

\[
\begin{aligned}
\mathcal B_{p,q}\Phi(y)
&=A(1-p^{-1/2}-q^{-1/2})+B y^{-1/2}.
\end{aligned}
\]

Since `p>=67`, `q>=71`,

\[
1-p^{-1/2}-q^{-1/2}
\ge1-67^{-1/2}-71^{-1/2}>0.75,
\]

so the block is strictly positive. Continuity at `y=pq` handles the activation boundary.

Therefore

\[
\boxed{\mathcal B_{p,q}\Phi(y)>0\qquad(y>=pq)}
\]

for every rough prime pair.

The remaining many-prime question is compositional: whether successive pair operators preserve a cone on which the next pair remains positive. This theorem does not assume that closure.
