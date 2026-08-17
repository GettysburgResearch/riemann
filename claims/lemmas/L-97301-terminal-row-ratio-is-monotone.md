# L-97301 — The terminal ratio Q_Y(3)/Q_Y(2) is globally nondecreasing

Claim ID: `L-97301`  
Status: **PROVED EXACT ANALYTIC LEMMA**  
Created: 2026-08-17  
RH status: **unproved**

For `m>=2`, put

\[
h_m(Y)=\frac1{\sqrt m}\log\frac Ym\,\mathbf1_{Y\ge m}.
\]

The canonical component-row formula specializes to

\[
Q_Y(2)=3h_2(Y)+\sum_{m\ge4}h_m(Y),
\tag{L-97301.1}
\]

\[
Q_Y(3)=2h_3(Y)-\frac23h_4(Y)
       +\frac13\sum_{m\ge5}h_m(Y).
\tag{L-97301.2}
\]

Since `Q_Y(2)>0` for `Y>2`, define

\[
\rho(Y)=\frac{Q_Y(3)}{Q_Y(2)}.
\]

Then

\[
\boxed{\rho\text{ is nondecreasing on }(2,\infty)
\text{ and strictly increasing on }(3,\infty).}
\tag{L-97301.3}
\]

## Proof on 2<Y<4

For `2<Y<=3`, `Q_Y(3)=0`, so `rho(Y)=0`.  For `3<Y<4`,

\[
\rho(Y)=
\frac{(2/\sqrt3)\log(Y/3)}{(3/\sqrt2)\log(Y/2)}.
\]

Its derivative has the sign of

\[
\log(Y/2)-\log(Y/3)=\log(3/2)>0.
\]

## Proof for Y>=4

Equations (L-97301.1)–(L-97301.2) give the tail cancellation

\[
3Q_Y(3)-Q_Y(2)=3D(Y),
\qquad
D(Y)=2h_3(Y)-h_4(Y)-h_2(Y).
\tag{L-97301.4}
\]

For `Y>=4`,

\[
D(Y)=A\log Y-B,
\]

where

\[
A=\frac2{\sqrt3}-\frac12-\frac1{\sqrt2}<0,
\qquad
B=\frac{2\log3}{\sqrt3}
  -\left(1+\frac1{\sqrt2}\right)\log2>0.
\tag{L-97301.5}
\]

The first sign follows because

\[
\left(\frac12+\frac1{\sqrt2}\right)^2
=\frac34+\frac1{\sqrt2}
>\frac34+\frac7{12}=\frac43.
\]

For the second, use

\[
\frac2{\sqrt3}>\frac87,
\qquad
1+\frac1{\sqrt2}<\frac{12}7,
\]

and hence

\[
B>\frac87\log3-\frac{12}7\log2
 =\frac47\log\frac98>0.
\]

On an activation cell `N<=Y<N+1`,

\[
Q_Y(2)=S_N\log Y-T_N,
\]

with

\[
S_N=\frac3{\sqrt2}+\sum_{m=4}^N\frac1{\sqrt m}>0,
\qquad
T_N=\frac{3\log2}{\sqrt2}+
    \sum_{m=4}^N\frac{\log m}{\sqrt m}>0.
\]

By (L-97301.4),

\[
\rho(Y)=\frac13+\frac{D(Y)}{Q_Y(2)}.
\]

Therefore

\[
\rho'(Y)
=
\frac{B S_N-A T_N}{YQ_Y(2)^2}>0.
\tag{L-97301.6}
\]

Every entering hinge vanishes at its activation knot, so both rows and their
ratio are continuous there.  This proves (L-97301.3).

## Correct coupling corollary

Let `Y_e>=Y_o>2`, let `b>=0`, and choose `u` by **row-2 exactness**

\[
uQ_{Y_e}(2)=bQ_{Y_o}(2).
\]

Then

\[
\boxed{
 uQ_{Y_e}(3)-bQ_{Y_o}(3)
 =bQ_{Y_o}(2)(\rho(Y_e)-\rho(Y_o))\ge0.
}
\tag{L-97301.7}
\]

This is a conditional edge lemma.  It neither supplies the row-2-exact
coefficient nor proves simultaneous target and score feasibility.
