# L-99102 — Integral Hall-flow decomposition gives samplewise feasible leaves

Claim ID: `L-99102`  
Status: **PROVED EXACT AT FINITE NETWORK-FLOW SCOPE**  
Created: 2026-08-19  
RH status: **unproved**

Let `G=(L,R,E)` be a finite bipartite graph. Give every left vertex an integer supply `c_l>=0`, every right vertex an integer capacity `b_r>=0`, and fix an integer total transported mass `M`.

Consider the finite flow polytope

\[
\begin{aligned}
 \mathcal P=\{x\in\mathbb R_{\ge0}^E:
 &\sum_{r:(l,r)\in E}x_{lr}\le c_l,\\
 &\sum_{l:(l,r)\in E}x_{lr}\le b_r,\\
 &\sum_{(l,r)\in E}x_{lr}=M\}.
\end{aligned}
\tag{L-99102.1}
\]

The constraint matrix is a network matrix and is totally unimodular. Since the right-hand sides are integral, every vertex of `P` is integral. Therefore every fractional flow `x in P` has a finite convex decomposition

\[
 \boxed{x=\sum_{a=1}^N\theta_ax^{(a)},
 \qquad
 \theta_a\ge0,
 \quad\sum_a\theta_a=1,}
 \tag{L-99102.2}
\]

where every `x^(a)` is an integral feasible flow.

Choosing one index `a` with probabilities `theta_a` gives a **samplewise** source-owned Hall-feasible allocation, while every linear row, endpoint, label, and score observable has exactly the prescribed fractional barycenter.

This is stronger than coordinatewise unbiased rounding: no sampled leaf can overfill a network capacity.

## Scope firewall

An additional arbitrary score inequality or nonlinear native constraint need not preserve total unimodularity. The theorem applies automatically only when all load-bearing restrictions are encoded by the same integral network-flow polytope, or when a separate proof shows that every integral leaf also satisfies the additional restrictions.
