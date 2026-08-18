# R-98611 — Positive completed deficit does not imply positive local two-level current

Claim ID: `R-98611`  
Status: **PROVED EXACT COUNTERMODEL**  
Created: 2026-08-18  
Depends on: `L-98611`  
RH status: **not assumed**

Take a three-node chain `v -> w -> u`, each edge of weight `r=1/2`. Let the only
nonzero local data be

\[
d_v^+=-1,\qquad d_u^+=8.
\]

Then at the terminal node

\[
D_u^+=8,
\]

at the middle node

\[
D_w^-=rD_u^+=4,
\]

and at the root

\[
D_v^+=d_v^+ +rD_w^-=-1+2=1>0.
\]

But the eliminated local current is

\[
g_v^+=d_v^+ +r d_w^-=-1<0,
\]

while the future repair is

\[
(R^2D^+)_v=r^2D_u^+=2.
\]

Thus `D_v^+=g_v^+ +(R^2D^+)_v=1`. Statewise positivity of `g^+` is an invalid
replacement for the nonlocal Bellman problem.
