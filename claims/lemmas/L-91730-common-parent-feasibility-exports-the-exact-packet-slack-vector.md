# L-91730 — Common-parent feasibility exports the exact packet-native slack vector

Claim ID: `L-91730`  
Status: **PROVED EXACT POSITIVE-LINEAR CAPACITY IDENTITY**  
Created: 2026-08-15  
Frozen inputs: common-parent sum and causal split from PRs #473/#479; packet-capacity formalism of `L-91727`  
RH status: **unproved**

Let `P_X` be the complete labelled positive parent packet after all common
positive omissions and thinning.  Suppose the all-column realization gives

\[
 \Xi(P_X)\le\Omega_X,
 \qquad e_X:=\Omega_X-\Xi(P_X)\ge0.
 \tag{L-91730.1}
\]

Suppose the aggregate causal split is exact in every component row and ordinary
response:

\[
 P_X=P_X^{\rm cur}+
 \int_Ba(b)U_bP_b\,d\nu(b).
 \tag{L-91730.2}
\]

Apply ordinary response at `q` and `4q` separately, then form radix-four detail:

\[
 \Xi(P_X)=\Xi(P_X^{\rm cur})+
 \int_Ba(b)U_b\Omega(P_b)\,d\nu(b).
 \tag{L-91730.3}
\]

Let `c_X` be a feasible row inside the current packet and put

\[
 h_X=\Xi(P_X^{\rm cur})-\Xi(c_X)\ge0,
 \qquad r_X=e_X+h_X.
\]

Then

\[
 \boxed{
 \Omega_X=\Xi(c_X)+r_X+
 \int_Ba(b)U_b\Omega(P_b)\,d\nu(b).
 }
 \tag{L-91730.4}
\]

This is the one-use capacity identity required by `L-91727`.  Every child owns
its actual packet capacity, not an independent copy of the native root
capacity.  Current response, current slack, external reserve, child capacity
and the separate common port each have one owner.

```text
common-parent all-column feasibility          PR #479 / FROZEN INPUT
exact aggregate packet split                  FROZEN LINEAR IDENTITY
q and 4q response equality                    EXACT
packet-native slack vector                    EXACT
native cost of that vector                    L-91728 / REVIEW
Riemann Hypothesis                            UNPROVED
```
