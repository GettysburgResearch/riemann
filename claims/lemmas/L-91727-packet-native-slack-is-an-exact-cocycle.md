# L-91727 — Packet-native slack is an exact cocycle

Claim ID: `L-91727`  
Status: **PROVED EXACT PACKET-CAPACITY RECURRENCE**  
Created: 2026-08-15  
Frozen inputs: `L-91378`, `L-91658`; native-slack correction of PR #477  
RH status: **unproved**

## 1. Packet capacity

A positive typed packet `P` carries target mass `m(P)`, packet-specific detail
capacity `Omega(P)>=0`, and a feasible row `d`.  Define

\[
 s(P,d)=\Omega(P)-\Xi(d),
 \qquad
 \Delta(P,d)=\langle Y_4,s(P,d)\rangle.
 \tag{L-91727.1}
\]

For the native root packet `N_X`,

\[
 \Delta(N_X,d)=J_\Lambda(X)-\mathcal H(d).
 \tag{L-91727.2}
\]

## 2. One-use identity and child insertion

Suppose

\[
 P=P^{\rm cur}+\int_Ba(b)U_bP_b\,d\nu(b)
 \tag{L-91727.3}
\]

and a current row `c` and nonnegative local slack `r(P)` satisfy

\[
 \boxed{
 \Omega(P)=\Xi(c)+r(P)+
 \int_Ba(b)U_b\Omega(P_b)\,d\nu(b).
 }
 \tag{L-91727.4}
\]

For feasible child rows `d_b`, put

\[
 d=c+\int_Ba(b)U_bd_b\,d\nu(b).
\]

Then

\[
 \boxed{
 s(P,d)=r(P)+\int_Ba(b)U_bs(P_b,d_b)\,d\nu(b)\ge0.
 }
 \tag{L-91727.5}
\]

Since normalized same-index placement preserves numerical detail coordinates,

\[
 \boxed{
 \Delta(P,d)=\delta(P)+
 \int_Ba(b)\Delta(P_b,d_b)\,d\nu(b),
 \quad \delta(P)=\langle Y_4,r(P)\rangle.
 }
 \tag{L-91727.6}
\]

No `4sqrt(X)` surrogate occurs.

## 3. Direct coefficient envelope

If

\[
 \int_Ba(b)\,d\nu(b)\le\rho<1,
 \qquad
 \operatorname{end}(P_b)\le X/67+C_0,
 \tag{L-91727.7}
\]

and `delta(P)<=g(X)`, then the worst canonical packet deficit satisfies

\[
 \boxed{E(X)\le g(X)+\rho E(X/67+C_0).}
 \tag{L-91727.8}
\]

Thus `g(X)=O(1+log X)` implies

\[
 \boxed{E(X)=O(1+\log X).}
 \tag{L-91727.9}
\]

This is the shortest native recurrence and uses the exact causal coefficients.

## 4. Target-normalized envelope

If additionally

\[
 \int_Ba(b)m(P_b)\,d\nu(b)\le\rho m(P)
 \tag{L-91727.10}
\]

and `delta(P)<=g(X)m(P)`, then the target-normalized worst deficit obeys the
same recurrence.  `L-91726` proves (L-91727.10) for the actual factor-67 packet.

The coefficient and target-mass envelopes are independent consistency checks;
neither is silently substituted for the other.

```text
packet-native capacity/slack definition       EXACT
child insertion cocycle                       EXACT
coefficient envelope                          EXACT
target-mass envelope                          EXACT
one-use root capacity identity                L-91730
local native root cost                        L-91728 / REVIEW
Riemann Hypothesis                            UNPROVED
```
