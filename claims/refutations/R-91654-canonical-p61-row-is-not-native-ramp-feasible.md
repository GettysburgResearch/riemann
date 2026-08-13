# R-91654 — The canonical `P_61` row is not directly feasible for the native ordinary ramp

Claim ID: `R-91654`  
Status: **EXACT NORMALIZATION FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91363`, `L-91660`  
RH status: **unproved**

Put

\[
P=P_{61}=\prod_{\ell\le61}\ell.
\]

For the canonical finite-Euler row

\[
D_{P,X}(j)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j),
\]

`L-91363` gives the exact ordinary response

\[
C_{P,X}(q)=\frac1{\sqrt q}H_P(X/q),
\]

where

\[
H_P(Z)=\sum_{\substack{n\le Z\\(n,P)=1}}
\frac1{\sqrt n}\log\frac Zn.
\]

The native ordinary target of the endpoint criterion is

\[
w_X(q)=\frac1{\sqrt q}\log\frac Xq.
\]

Since the term `n=1` in `H_P` is exactly `log Z`, one has the identity

\[
\boxed{
C_{P,X}(q)-w_X(q)
=
\frac1{\sqrt q}
\sum_{\substack{2\le n\le X/q\\(n,P)=1}}
\frac1{\sqrt n}\log\frac{X}{qn}.
}
\tag{R-91654.1}
\]

Every summand is nonnegative.  The least integer greater than one and coprime to
`P_61` is `67`.  Hence

\[
C_{P,X}(q)=w_X(q)\quad\text{for }X/q\le67,
\]

while

\[
\boxed{C_{P,X}(q)>w_X(q)\quad\text{for }X/q>67.}
\tag{R-91654.2}
\]

For example, at `X=136,q=2`, the only nontrivial rough integer below `68` is
`67`, so exactly

\[
\boxed{
C_{P,136}(2)-w_{136}(2)
=
\frac1{\sqrt{134}}\log\frac{68}{67}>0.
}
\tag{R-91654.3}
\]

Therefore the nonnegative row `D_(P,X)` cannot be inserted unchanged into the
native feasible cone with ordinary budget `w_X`.  Its packet-specific capacities
are larger by the complete rough-number tail.

This does not refute coefficientwise positivity of `D_(P,X)`, its exact
packet-specific capacities, or its literal-entropy surplus.  It refutes only the
unproved identification

```text
canonical P61 packet capacity = native root ramp.
```

A valid full proof must instead do one of the following:

1. retain the two-labelled packet capacity and prove an exact root bridge;
2. subtract the actual rough-child capacity before physical packing;
3. use the provenance-causal difference `P_u-p^(-1/2)U_pP_(u/p)`, whose
   complete row and physical capacities are nonnegative by `L-91654`.

The corrected provenance-causal composition takes option 3.

```text
canonical P61 row sign                    NOT CHALLENGED
packet-specific ordinary capacity          EXACT
native ordinary ramp                       EXACT
naive direct native feasibility            FALSE
rough-child/provenance repair               REQUIRED
Riemann Hypothesis                          UNPROVED
```
