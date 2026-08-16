# R-95040 — Root neutrality does not imply positive interior fragmentation

Claim ID: `R-95040`  
Status: **EXACT FINITE SEPARATOR / SCOPE FIREWALL**  
Created: 2026-08-16  
Corrects any inference from `L-95040` signed span to positive CRCTP

At endpoint `X=6`, define the carry target

\[
t(2)=t(6)=1,
\qquad
t(3)=t(4)=t(5)=0.
\]

For

\[
b_2=(\varepsilon-\delta_2)*\mu,
\]

one has

\[
b_2(2)=-2,
\qquad
b_2(6)=2,
\]

so the target is root neutral:

\[
\sum_qb_2(q)t(q)=0.
\]

Its exact multiples-Möbius divergence is

\[
r(1)=0,
\quad r(2)=1,
\quad r(3)=-1,
\quad r(4)=0,
\quad r(5)=-1,
\quad r(6)=1.
\]

Define the node potential

\[
y(2)=-1,
\qquad y(4)=1,
\qquad y(n)=0\text{ otherwise}.
\]

For every quarter-balanced interior split through node six,

\[
y(n)-y(j)-y(n-j)\ge0.
\]

Explicitly the defects on

\[
4=2+2,
\quad5=2+3,
\quad6=2+4,
\quad6=3+3
\]

are respectively

\[
3,1,0,0.
\]

But

\[
\langle r,y\rangle=-1<0.
\]

Therefore no nonnegative interior flow can realize this root-neutral target.

\[
\boxed{
\text{root completion closes the signed span but not the positive cone.}
}
\]
