# R-99701 — Positive Green energy does not orient the signed SHARP source

Claim ID: `R-99701`  
Status: **PROVED EXACT MECHANISM REFUTATION**  
Created: 2026-08-20  
Depends on: `L-99702`  
RH status: **not assumed**

`L-99702.13` proves the edgewise-positive identity

\[
\mathcal E_X(f,f\Phi_X)\ge0.
\]

It is tempting to interpret this as an orientation of

\[
\langle f,\Phi_X\rangle_\pi.
\]

That implication is false even in the smallest reversible network.

Take two vertices joined by one positive conductance, with

\[
f(1)=1,
\qquad f(2)=-1,
\qquad
0\le\Phi(1)<\Phi(2),
\]

and choose positive vertex masses with

\[
\pi(2)\Phi(2)>\pi(1)\Phi(1).
\]

Then

\[
\langle f,\Phi\rangle_\pi
=\pi(1)\Phi(1)-\pi(2)\Phi(2)<0,
\]

while the single edge contributes

\[
[f(1)-f(2)]
[f(1)\Phi(1)-f(2)\Phi(2)]
=2[\Phi(1)+\Phi(2)]>0.
\]

Thus positive common Schur/Green energy controls magnitude and covariance but not the source-channel marginal.

For the live arithmetic network this means:

```text
L-99702.13                    valid;
source sign h or S_67 h       not implied;
explicit cross-source capacity flow required.
```

This is the electrical analogue of the earlier pointwise-PSD and unconstrained-contraction firewalls. The max-flow/min-cut quantity in `L-99704`, rather than the positive Dirichlet form alone, is the conclusion-producing object.