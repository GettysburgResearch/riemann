# R-104603 — A fixed source scale cannot recover shallow topological degree

Claim ID: `R-104603`  
Status: **EXACT MECHANISM FIREWALL**  
Created: 2026-08-27  
RH status: **not assumed**

For the one-zero Blaschke factor at `b=x+iy`, `L-105642` gives

\[
\operatorname{tr}_{K_{B_b}}M_{e^{-H\xi}}={2y\over H+2y}.
\]

For every fixed `H>0`, this tends to zero as `y` decreases to zero, although
the model-space degree is identically one. Therefore no fixed exponential
source metric, no finite collection of fixed positive heights, and no
uniformly bounded linear combination of them can dominate unweighted
canonical degree for arbitrarily shallow factors.

The fractional Calderón identity of `L-104631` is not an optional
regularization. Its continuum of scales is the exact mechanism by which the
missing unit mass is recovered:

\[
\int_0^\infty {2ayH^{a-1}\over(H+2y)^{a+1}}\,dH=1.
\]

This firewall rules out interpreting a small fixed-height current charge as a
proof of the shallow fifth-endpoint theorem.
