# L-91364 — The canonical `P_61` finite-Euler component row is globally nonnegative

Claim ID: `L-91364`  
Status: **PROVED FROM `L-91346` PLUS A DIRECTED FINITE-CELL CERTIFICATE; INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91344`, `L-91346`, `L-91363`, `X-91138`

## Statement

Put
\[
P=P_{61}=\prod_{q\le61}q,
\qquad
D_{P,X}(j)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j),
\]
with causal zero extension. Then, for every real `X>=1` and `2<=j<=66`,
\[
\boxed{D_{P,X}(j)\ge0.}
\]
The inequality is strict when `X>j`. More precisely,
\[
\boxed{D_{P,X}(j)>1/500\qquad(X\ge67j).}
\]

## Finite base

Every activation knot has the form `X=dm` with integers `d,m`. On an open cell
`N<X<N+1`, all active sets are fixed and every ramp is affine in `log X`.
Thus
\[
D_{P,X}(j)=A_{N,j}\log X+B_{N,j}.
\]
Entering ramps vanish at their knot, so the row is continuous and its minimum
on a closed cell occurs at an endpoint.

The standard-library replay `X-91138` checks all
\[
2\le j\le66,
\qquad
j+1\le N\le67j.
\]
It evaluates exactly `145860` directed endpoint cells and proves
\[
\boxed{D_{P,N}(j)>1/525.}
\]
The smallest directed lower endpoint occurs at `(N,j)=(67,66)` and exceeds
`0.0019079896612261321`. Since `D_(P,j)(j)=0`, log-affine interpolation gives
\[
D_{P,X}(j)\ge0\qquad(j\le X\le67j),
\]
strictly for `X>j`.

## Real-dilation closure

The one-prime theorem `L-91346` holds for every real `p>=67`, not only for
prime `p`, and gives
\[
D_{P,py}(j)-p^{-1/2}D_{P,y}(j)>1/500
\]
for `2<=j<=y<=67`.

Fix `X>=67j` and choose
\[
(p,y)=
\begin{cases}
(67,X/67),&X\le67^2,\\
(X/67,67),&X\ge67^2.
\end{cases}
\]
Then `p>=67`, `j<=y<=67`, and `X=py`. The finite base gives
`D_(P,y)(j)>=0`, so the displayed one-prime inequality yields
`D_(P,X)(j)>1/500`.

No prime-gap theorem is used; the real-dilation scope is the decisive point.

## Physical-output consequence

By `L-91363`, this row has the exact nonnegative outputs
\[
C_{P,X}(q)=q^{-1/2}H_P(X/q)
\]
and
\[
\Theta_{P,X}(q)=q^{-1/2}[H_P(Z)-H_P(Z/4)],
\]
and its literal component entropy has the nonnegative arithmetic density
`lambda_P` of `L-91363.15`.

Because the row coefficients themselves are now nonnegative, the canonical
`P_61` finite forcing has one literal positive realization of its component
rows, ordinary capacities, radix-four capacities, and component entropy.

## Remaining boundary

This closes the row/capacity/entropy core of the Complete Finite-Forcing
Producer. It does not yet attach, in one typed packet, the terminal correction,
quantization collar, common endpoint port, and the common benchmark
normalization for the two fixed channel labels.

```text
canonical finite-Euler row sign                  CLOSED / L-91364
ordinary, radix-four, entropy core                CLOSED / L-91363+L-91364
complete collar/terminal/common-port attachment   OPEN / CFFP-PORT
complete global endpoint argument                 NOT CLAIMED
```
