# R-99260 — The positive causal parent decomposition is not the Möbius Euler update

Claim ID: `R-99260`  
Status: **REFUTATION — EXACT ONE-PRIME COUNTERIDENTITY**  
Created: 2026-08-20  
Frozen parent: PR #647 at `306d1c66fe4e848efda0bd78b5475aeeed3d5563`  
RH status: **unproved**

## 1. The two identities have different outputs

Let `P` be a nonzero positive canonical packet, let `P_p` be its same-index
child at the smaller endpoint, and put

\[
 r=p^{-1/2},\qquad 0<r<1.
\]

The literal one-prime Möbius/Euler update is

\[
 \boxed{D_p(P)=P-rP_p.}
 \tag{R-99260.1}
\]

For one active prime, the positive causal coefficients used in the factor-67
packet are

\[
 s=1-r,\qquad \lambda=r,\qquad \alpha=r^2.
\]

The current packet is therefore

\[
\begin{aligned}
 P^{\rm cur}
 &=sP+\lambda(P-rP_p)\\
 &=P-r^2P_p,
\end{aligned}
\tag{R-99260.2}
\]

and current plus recursive child is

\[
 \boxed{P^{\rm cur}+\alpha P_p=P.}
 \tag{R-99260.3}
\]

Neither expression equals the Möbius update:

\[
 P^{\rm cur}-D_p(P)=r(1-r)P_p>0,
\tag{R-99260.4}
\]

while

\[
 [P^{\rm cur}+\alpha P_p]-D_p(P)=rP_p>0.
\tag{R-99260.5}
\]

Thus the causal decomposition is an exact positive decomposition of the
**positive parent packet**. It is not an exact representation of the signed
Euler factor `(I-rU_p)P`.

## 2. Consequence for the fixed-row route

A finite tree obtained by recursively expanding (R-99260.3) still sums to its
positive root parent. It cannot, by algebra alone, establish positivity of the
full Möbius row

\[
 c_X(j)=\sum_n\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\]

An additional conclusion-producing theorem must supply one of:

```text
an exact signed parity/Harnack inequality;
a signed calibration with holomorphic Mellin transform;
or a direct positive representation of the actual Möbius marginal.
```

The Radon–Nikodym common-parent theorem repairs child ownership, but it does not
change (R-99260.1)--(R-99260.5).

## 3. Lifecycle boundary

```text
positive causal parent identity            retained exact
actual child-mass contraction               retained exact
raw-child ownership                         repaired by L-99250
causal tree = Möbius Euler row              false
PR #642 full-row positivity from that step  blocked
Riemann Hypothesis                          unproved
```
