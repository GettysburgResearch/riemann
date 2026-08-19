# L-99210 — Canonical parabolic packets form one endpoint-nested positive vector measure

Claim ID: `L-99210`  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Frozen application graph: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **not assumed**

## 1. The typed canonical packet

Fix one finite root endpoint `X`. All vectors below are zero-extended to the
finite coordinate ranges `2<=j,q<=X`.

For real `Y>=1`, put

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\,\mathbf 1_{m\le Y},
 \qquad S_Y(n)=\sum_{m\ge n}h_Y(m),
\]

and

\[
 Q_Y(j)=(j+1)\Delta_j^2\left[\frac{S_Y(j)}{j-1}\right].
\]

Retain also

\[
 T(Y)=4\sqrt Y-3,
\]

\[
 C_Y(q)=q^{-1/2}H(Y/q),
 \qquad H(Z)=\sum_{m\le Z}m^{-1/2}\log(Z/m),
\]

and

\[
 \Theta_Y(q)=q^{-1/2}[H(Y/q)-H(Y/(4q))].
\]

Define the finite typed vector

\[
 \mathbf P_Y=
 \bigl(T(Y),\,(Q_Y(j))_j,\,(C_Y(q))_q,
              (\Theta_Y(q))_q\bigr)
 \in\mathbb R_+^D.
\tag{L-99210.1}
\]

Literal entropy is not a separate source coordinate. It is a positive linear
row functional.

## 2. Coordinatewise endpoint monotonicity

The component-row expansion is

\[
\begin{aligned}
Q_Y(j)={}&
 \frac{j+1}{j-1}[h_Y(j)-h_Y(j+1)]
 +\frac{2(j+1)}{j(j-1)}h_Y(j+1)\\
&+\frac2{j(j-1)}\sum_{m\ge j+2}h_Y(m).
\end{aligned}
\tag{L-99210.2}
\]

Every `h_Y(m)` is continuous and nondecreasing in `Y`. The only difference
term is nondecreasing as well. Indeed,

\[
 \frac d{dY}[h_Y(j)-h_Y(j+1)]
 =\begin{cases}
 0,&Y<j,\\
 (Y\sqrt j)^{-1},&j<Y<j+1,\\
 Y^{-1}(j^{-1/2}-(j+1)^{-1/2}),&Y>j+1,
 \end{cases}
\]

and there is no adverse activation atom, since the newly activated logarithmic
term is zero at activation. Thus

\[
 Q_{Y_2}(j)\ge Q_{Y_1}(j)
 \qquad(1\le Y_1\le Y_2).
\tag{L-99210.3}
\]

The remaining coordinates are monotone because

\[
 T'(Y)=2Y^{-1/2}>0,
\]

\[
 H'(Z)=Z^{-1}\sum_{m\le Z}m^{-1/2}\ge0,
\]

and

\[
 \frac d{dZ}[H(Z)-H(Z/4)]
 =Z^{-1}\sum_{Z/4<m\le Z}m^{-1/2}\ge0.
\]

Consequently

\[
 \boxed{
 \mathbf P_{Y_2}-\mathbf P_{Y_1}\in\mathbb R_+^D
 \qquad(1\le Y_1\le Y_2).
 }
\tag{L-99210.4}
\]

## 3. One cone-valued Stieltjes source

Equation (L-99210.4) defines a positive vector measure `d\mathbf P(t)` on
`[1,X]` by

\[
 \mathbf M([1,Y])=\mathbf P_Y.
\tag{L-99210.5}
\]

Equivalently, put the base vector `\mathbf P_1` at `t=1` and use the
coordinatewise Lebesgue--Stieltjes increments thereafter. Because the
coordinate set is finite, one scalar control measure dominates every
coordinate.

For every `1<=Z<=Y`,

\[
 \boxed{
 \mathbf P_Z=\mathbf M([1,Z])
 \quad\text{is a literal restriction of}\quad
 \mathbf P_Y=\mathbf M([1,Y]).
 }
\tag{L-99210.6}
\]

This is stronger than target-mass nonexpansion. Target, every physical row,
every ordinary response and every radix-four response use the same endpoint
restriction.

## 4. Same-index child placement

The factor-67 causal construction uses same-index child placement: the child
label changes, but its numerical physical row, target and response coordinates
are the canonical coordinates at the smaller endpoint. Thus a child at
endpoint `Y_i<=Y` is the labelled pushforward of
`\mathbf M|_[1,Y_i]`.

If a positive Hall residual coefficient `c` is inherited unchanged, then

\[
 c\mathbf P_{Y_i}
 \quad\text{is the same restriction of}\quad
 c\mathbf P_Y.
\tag{L-99210.7}
\]

The statement remains true after adjoining low-prime, rough-history and
direct-integral endpoint labels by taking disjoint copies of the vector
measure.

## 5. Scope

This theorem supplies the repository-specific domination missing from the
abstract common-parent theorem of PR #632. It applies to the unnormalized
canonical packet and same-index placement, not to independently normalized
children or to operators changing the numerical row before ownership is
assigned.
