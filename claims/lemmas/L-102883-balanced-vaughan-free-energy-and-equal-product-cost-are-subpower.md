# L-102883 — Balanced stopped-Vaughan free energy and equal-product collapse are subpower

Claim ID: `L-102883`  
Status: **PROVED UNCONDITIONAL ENERGY/OCCUPANCY THEOREM**  
Created: 2026-08-24  
Depends on: `L-102868`; `L-102882`  
RH status: **not assumed**

On one dyadic stopped-Vaughan block write

\[
U_1\le u<2U_1,
\qquad
V_1\le v<2V_1,
\qquad
M\le m<2M,
\]

with

\[
U_1,V_1>Y^{1/6},
\qquad
M\ll Y^{1/6},
\qquad
U_1V_1M\asymp\sqrt Y.
\]

The coefficient of the core product is

\[
c_{u,v,m}
={a_{U,q}(u)a_{U,q}(v)\mu(m)\over uvm}.
\]

## 1. Free six-variable energy

Since

\[
|a_{U,q}(n)|\le\tau(n),
\]

the classical divisor-square estimate gives

\[
\sum_{n\sim N}{\tau(n)^2\over n^2}
\ll {\log^3(2N)\over N}.
\]

Therefore

\[
\boxed{
\sum_{u\sim U_1}
\sum_{v\sim V_1}
\sum_{m\sim M}
|c_{u,v,m}|^2
\ll
{(\log(2Y))^6\over U_1V_1M}
=Y^{-1/2+o(1)}.
}
\tag{L-102883.1}

Including the external owner coefficient gives, for one squareclass `P=pq`,

\[
\sum|c_{P;u,v,m}|^2
\ll {Y^{o(1)}\over pq}.
\tag{L-102883.2}

Since

\[
\sum_{p>q}{1\over pq}
\ll(\log\log(3X))^2,
\]

the complete **free labelled** balanced packet over all owner squareclasses has
subpower energy.  The second labelled copy of `67` changes only an absolute
constant.

## 2. Equal-product multiplicity

The physical product in one block is

\[
N=pq(uvm)^2.
\]

The owner pair `{p,q}` is the squarefree kernel and is unique.  For fixed core
product `c=uvm`, the number of triples `(u,v,m)` is at most `d_3(c)`, and the
number of dyadic block labels is `O((\log X)^3)`.  Hence the complete
representation multiplicity of one physical integer is

\[
\boxed{X^{o(1)}.}
\tag{L-102883.3}

Cauchy at one physical product converts the free energy in (L-102883.1) to the
equal-product physical energy with only subpower loss.

## 3. Boundary packet

The smooth-boundary coefficients of `L-102881` have polylogarithmic
fixed-squareclass `l1` norm.  Adding them to one stopped-Vaughan block changes
both the free energy and equal-product collapse by at most another subpower
factor.

## Exact scope

The theorem removes:

```text
free six-variable energy;
dyadic representation multiplicity;
equal-product collapse;
local smooth-boundary coefficient cost.
```

It does not control correlations between **different physical products from
different owner squareclasses**.  Those correlations remain inside the
source-exact gcd/phase decomposition of `L-102884--L-102886`.