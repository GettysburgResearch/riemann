# R-91651 — Source mass does not scale an arbitrary signed packet deficit

Claim ID: `R-91651`  
Status: **EXACT ABSTRACT COUNTEREXAMPLE**  
Created: 2026-08-13  
RH status: **unproved**

Let a packet consist of two positive source atoms of equal mass. Suppose the
feasible packing pays the first atom completely and leaves positive deficit `H`
on the second. Then the complete packet has deficit `H`; the restriction to the
second atom has source mass fraction `1/2` but still has deficit `H`, not `H/2`.

Therefore

\[
m(P_B)=\theta m(P)
\quad\not\Longrightarrow\quad
\Delta(P_B)\le\theta\Delta(P).
\]

The valid replacements are:

1. positive homogeneity for a scalar multiple of the *same packet*;
2. subadditivity for sums of actual packets;
3. a worst-normalized-packet envelope for arbitrary restrictions.

This is the reason the provenance-causal proposal uses `L-91406/T-91401` rather
than historical scalar branch weights.