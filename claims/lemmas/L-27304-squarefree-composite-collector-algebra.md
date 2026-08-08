# L-27304 — Squarefree composite collectors are exactly proper-power neutral

Claim ID: `L-27304`  
Title: Constant blocks between squarefree endpoints transport ordinary-prime incidence while leaving every proper prime power unchanged  
Status: **PROPOSED COMPLETE EXACT FINITE ALGEBRA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: PR #248 `L-24520`; `R-27302`  
Scope: finite squarefree-incidence cone; no all-scale transport theorem and no RH claim

## 1. One squarefree collector block

Let

\[
1\le A<B\le X
\]

be squarefree integers, and let \(t\ge0\). Define the positive block

\[
\boxed{
h_m=t\mathbf1_{A<m\le B}.}
\tag{L-27304.1}
\]

For every prime power \(q\), telescoping gives

\[
\begin{aligned}
v_q(h)
&=
\sum_{m=A+1}^{B}
 t\left(\mathbf1_{q\mid m}-\mathbf1_{q\mid m-1}\right)\\
&=
 t\left(\mathbf1_{q\mid B}-\mathbf1_{q\mid A}\right).
\end{aligned}
\]

Hence

\[
\boxed{
v_q(h)
=t\left(\mathbf1_{q\mid B}-\mathbf1_{q\mid A}\right).}
\tag{L-27304.2}
\]

Because both endpoints are squarefree,

\[
\boxed{
v_{p^a}(h)=0
\qquad(a\ge2).}
\tag{L-27304.3}
\]

For ordinary primes,

\[
\boxed{
v_p(h)
=t\left(\mathbf1_{p\mid B}-\mathbf1_{p\mid A}\right).}
\tag{L-27304.4}
\]

Thus the block is automatically a Proper-Power-Neutral Lift atom.

## 2. Exact objective and incidence compression

The complete physical objective increment is

\[
\begin{aligned}
J_X(h)
&=
 t\sum_{m=A+1}^{B}\log\frac m{m-1}\\
&=
\boxed{t\log\frac BA\ge0.}
\end{aligned}
\tag{L-27304.5}
\]

Because the proper-power responses vanish, the ordinary-prime objective sees
the same increment:

\[
\boxed{
J_{\mathbb P,X}(h)=J_X(h)=t\log(B/A).
}
\tag{L-27304.6}
\]

Let \(\omega(n)\) be the number of distinct prime divisors. Summing
(L-27304.4) over ordinary primes gives

\[
\boxed{
\sum_{p\le X}v_p(h)
=t\bigl(\omega(B)-\omega(A)\bigr).
}
\tag{L-27304.7}
\]

Consequently a squarefree composite collector \(A\) with
\(\omega(A)>\omega(B)\) can destroy ordinary-prime incidence mass while
*increasing* the sharp objective and remaining invisible to all higher prime
powers.

For example, the block from

\[
A=30=2\cdot3\cdot5
\qquad\text{to}\qquad
B=43
\]

has

\[
\Delta v_2=\Delta v_3=\Delta v_5=-t,
\qquad
\Delta v_{43}=+t,
\]

zero response on every proper prime power, and total prime-incidence change
\(-2t\).

This is the exact finite mechanism absent from the rejected prime-to-prime
`PTC` route.

## 3. Squarefree Collector Lift (`SCL`)

Let \(\mathcal E_X\) be any declared family of ordered squarefree pairs

\[
(A,B),\qquad1\le A<B\le X.
\]

For nonnegative masses \(t_{A,B}\), define

\[
h_m
=
\sum_{(A,B)\in\mathcal E_X}
 t_{A,B}\mathbf1_{A<m\le B}.
\tag{L-27304.8}
\]

Then automatically

\[
h_m\ge0,
\qquad
v_{p^a}(h)=0\quad(a\ge2),
\tag{L-27304.9}
\]

and

\[
v_p(h)
=
\sum_{(A,B)\in\mathcal E_X}
 t_{A,B}
 \left(\mathbf1_{p\mid B}-\mathbf1_{p\mid A}\right).
\tag{L-27304.10}
\]

The proposed all-scale theorem is to choose the masses so that

\[
\boxed{
r_X(p)+v_p(h)\le0
\qquad(p\le X).}
\tag{SCL}
\]

Any such choice is an exact PNL certificate and has nonnegative objective
increment.

## 4. Exact Farkas dual

For \(y_p\ge0\), put

\[
Y_y(n)=\sum_{p\mid n}y_p.
\tag{L-27304.11}
\]

The squarefree collector system is infeasible exactly when there is a
nonnegative prime vector \(y\) such that

\[
\boxed{
Y_y(A)\le Y_y(B)
\qquad((A,B)\in\mathcal E_X)
}
\tag{L-27304.12}
\]

and

\[
\boxed{
\sum_{p\le X}y_pr_X(p)>0.
}
\tag{L-27304.13}
\]

Indeed, the edge column has dual pairing

\[
Y_y(B)-Y_y(A).
\]

For the complete squarefree edge family, (L-27304.12) says that the strongly
additive potential is nondecreasing on squarefree integers through \(X\).

The logarithmic ray

\[
y_p=\log p
\]

satisfies

\[
Y_y(n)=\log n
\]

on squarefree integers and is therefore admissible. Its source pairing is the
ordinary-prime ramp deficit. Thus SCL is genuinely RH-bearing and cannot follow
from a generic Hall theorem that discards the source weights.

## 5. Consequence of the density-drift refutation

`R-27302` proposes

\[
\sum_{p\le X}r_X(p)
\sim
4(1-\gamma)\frac{\sqrt X}{\log^2X}>0.
\tag{L-27304.14}
\]

Prime-to-prime blocks have \(\omega(A)=\omega(B)=1\), so they preserve total
ordinary-prime incidence and necessarily export this drift to the boundary.

A successful SCL construction must instead supply the exact incidence
compression

\[
\sum_{(A,B)}
 t_{A,B}\bigl(\omega(A)-\omega(B)\bigr)
\gtrsim
4(1-\gamma)\frac{\sqrt X}{\log^2X},
\tag{L-27304.15}
\]

while matching the individual residual rows. Composite collectors are therefore
not optional bookkeeping; they are forced by the first prime-density
correction.

## 6. Proposed constructive route

A source-level proof should:

1. use the continuum tail coupling from PR #265 to match defect scale to later
   slack scale;
2. replace each continuum transport parcel by a squarefree incidence edge;
3. use divisor-rich collectors only after exact product collisions are
   recombined;
4. reserve bounded small-prime helper rows as incidence sinks;
5. prove a Hall/Strassen cut inequality for every squarefree-monotone additive
   dual potential;
6. retain the logarithmic ray as the scalar firewall;
7. export every proper-power response, which must be exactly zero.

## 7. Proof boundary

```text
one squarefree block algebra              PROPOSED COMPLETE EXACT
proper-power neutrality                   PROPOSED COMPLETE EXACT
incidence-compression identity            PROPOSED COMPLETE EXACT
squarefree collector Farkas dual          PROPOSED COMPLETE EXACT
all-scale SCL construction                OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
