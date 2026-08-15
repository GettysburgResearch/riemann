# R-91870 — The canonical `P_61` rough lift is not the native input marginal

Claim ID: `R-91870`  
Status: **PROVED EXACT NORMALIZATION FIREWALL**  
Created: 2026-08-15  
Frozen predecessor: PR #500 at `d73c1e7a1a482cac31581211a84db43cc34c824e`  
RH status: **unproved**

Let

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j)
\]

be the full native Möbius row. Its ordinary and radix-four responses and literal
benchmark are exactly

\[
 C_{c_X}=w_X,\qquad \Xi_{c_X}=\Omega_X,\qquad
 \mathcal H(c_X)=J_\Lambda(X).
\tag{R-91870.1}
\]

The canonical finite-Euler row through `61` instead satisfies

\[
 D_{P_{61},X}
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}U_mc_{X/m},
\tag{R-91870.2}
\]

where `m=1` is the native term and every `m>1` is a positive rough reservoir in
ordinary, detail and benchmark coordinates.

At `X=136`, `q=2`, the only new rough integer below `X/q=68` is `67`; hence

\[
\boxed{
 C_{D_{P_{61},136}}(2)-w_{136}(2)
 =\frac{\log(68/67)}{\sqrt{134}}>\frac1{816}.
}
\tag{R-91870.3}
\]

Indeed `log(1+t)>t/(1+t)` with `t=1/67`, and `sqrt(134)<12`.

Therefore a physical coupling whose input marginal is the complete rough lift
cannot be a native root coupling. Adding nonnegative current packets or
nonnegative child placements cannot remove the positive overdraw in
(R-91870.3).

The successor must begin from the paired native Möbius source itself and must
derive every rough owner as a disjoint label inside that source. It may use the
rough lift only as an audit identity or separator.

```text
native source marginal                  full Mobius source
canonical P61 rough lift                enlarged / forbidden as parent
rough first-owner labels                allowed only inside native source
Riemann Hypothesis                      unproved
```
