# L-102868 — The stopped balanced core form is exact through phases and gauges

Claim ID: `L-102868`  
Status: **CORRECTED EXACT SOURCE-TYPING THEOREM**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-102830--L-102865`, `L-102869`  
RH status: **not assumed**

Retain one clean largest-two squareclass

\[
N=pq\,a^2,
\qquad p>q>P^+(a),
\]

and put `Y=X/(pq)`, `U=floor(Y^(1/6))`. The literal balanced core from
`L-102869` is

\[
\boxed{
\mathcal B_{p,q}(X)
=\frac1{\sqrt{pq}}
\sum_{\substack{u,v>U\\u,v,m\in\mathbb N_{<q}}}
\frac{a_{U,q}(u)a_{U,q}(v)\mu(m)}{uvm}
R_L\!\left(\frac{X}{pq\,u^2v^2m^2}\right).
}
\tag{L-102868.1}

The support gives

\[
u,v>Y^{1/6},
\qquad m\ll Y^{1/6},
\qquad uvm\asymp\sqrt Y.
\]

## 1. Phase functoriality

Every prime factor of `uvm` is smaller than `q`; hence it is coprime to every
selected external owner modulus in the clean sector. For any selected owner
phase `ell`,

\[
e_\ell(hN)=e_\ell(hpq\,u^2v^2m^2).
\]

The stopped Vaughan identity is coefficientwise and therefore commutes with:

```text
all nonzero additive owner phases;
all 15 adaptive phase choices;
owner and squareclass projections;
Euler/half-divisor/Wick gauge transfer;
the fixed outer-ray observation;
one-octave physical localization.
```

No zero phase or extra source copy is introduced.

## 2. Dyadic Type-II blocks

On dyadic ranges

\[
U_1\le u<2U_1,
\quad V_1\le v<2V_1,
\quad M\le m<2M,
\]

every nonempty block satisfies

\[
\boxed{
U_1,V_1>Y^{1/6},
\qquad M\ll Y^{1/6},
\qquad U_1V_1M\asymp\sqrt Y.
}
\tag{L-102868.2}

The coefficient bound

\[
|a_{U,q}(n)|\le\tau(n)
\]

keeps every representation multiplicity at `Y^o(1)`.

## 3. No owner-size inference from variable size

The first version of this file incorrectly inferred

\[
q>Y^{1/6}
\]

from `u,v>Y^(1/6)`. This is false: a large integer may be composed entirely of
primes below a small `q`. The only valid relation is

\[
P^+(uvm)<q.
\]

No quarter-power lower bound for `pq` follows from the stopped Vaughan ranges.
This correction is binding for every subsequent dyadic summation.

## 4. Exact surviving coherent form

For clean squareclasses `P=pq` and `Q=rs`, the balanced cross packet is a sum
of dyadic blocks

\[
\boxed{
\begin{aligned}
\mathscr B_{P,Q}
={}&\sum
\frac{a_{U_P,q}(u)a_{U_P,q}(v)\mu(m)}{uvm\sqrt P}
\frac{a_{U_Q,s}(u')a_{U_Q,s}(v')\mu(m')}{u'v'm'\sqrt Q}\\
&\times\mathcal K\!\left(
\log\frac{P(uvm)^2}{Q(u'v'm')^2}
\right),
\end{aligned}}
\tag{L-102868.3}

with the selected nonzero owner phases inserted as in `L-102865` and with all
six core variables retained in their corresponding stopped monoids.

This theorem types the balanced row exactly. It does not close the smooth
boundary `SCB102869` or the coherent balanced estimate `BCQDSP102880`.
