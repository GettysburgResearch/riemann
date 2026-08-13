# L-92200 — The safe-Xi Carathéodory determinant is a Cauchy–Krein double alternant

Claim ID: `L-92200`  
Status: **PROVED EXACT ALL-ORDER DETERMINANT IDENTITY — REVIEW REQUESTED**  
Created: 2026-08-13  
RH status: **unproved**

Let

\[
 0<x_1<\cdots<x_n,
 \qquad t_i=x_i^2,
 \qquad p_i>0,
\]

and define

\[
 H_{ij}=\frac{x_ip_i+x_jp_j}{x_i+x_j},
 \qquad
 \Delta_+(x)=\prod_{i<j}(x_i+x_j).
\]

For the safe Xi hierarchy,

\[
 p_i=x_i^{-1}\frac{\xi'}{\xi}\left(\frac12+x_i\right).
\]

## Even order

For `n=2m`, put

\[
 \mathcal A_{2m}^{(0)}
 =\det[1,t,\ldots,t^{m-1},p,tp,\ldots,t^{m-1}p]_{t=t_i},
\]

\[
 \mathcal A_{2m}^{(1)}
 =\det[1,t,\ldots,t^{m-1},tp,t^2p,\ldots,t^mp]_{t=t_i}.
\]

Then

\[
 \boxed{
 \det H
 =\frac{(-1)^m\mathcal A_{2m}^{(0)}\mathcal A_{2m}^{(1)}}
 {\Delta_+(x)^2}.
 }
 \tag{L-92200.1}

## Odd order

For `n=2m+1`, put

\[
 \mathcal A_{2m+1}^{(0)}
 =\det[1,t,\ldots,t^{m-1},p,tp,\ldots,t^mp]_{t=t_i},
\]

\[
 \mathcal A_{2m+1}^{(1)}
 =\det[1,t,\ldots,t^m,tp,t^2p,\ldots,t^mp]_{t=t_i}.
\]

Then

\[
 \boxed{
 \det H
 =\frac{\mathcal A_{2m+1}^{(0)}\mathcal A_{2m+1}^{(1)}}
 {\Delta_+(x)^2}.
 }
 \tag{L-92200.2}

Empty column families are omitted.

## Proof

Write

\[
 H=D_{xp}C+CD_{xp},
 \qquad C_{ij}=\frac1{x_i+x_j}.
\]

Multiply by the square of the Cauchy denominator and expand the bordered
Cauchy minors.  Separating even and odd powers of `x` gives exactly the two
alternants above.

Equivalently, apply Desnanot--Jacobi to `H`.  The alternant pairs obey the
matching Plücker relation, while the Cauchy denominator ratios supply the
factor `(x_1+x_n)^2`.  The base cases `n=1,2` are direct.  The parity switch
in the induction yields `(-1)^m` in the even case.

## First four orders

```text
n=1:
    det H=p_1;

n=2:
    det H=-det[1,p] det[1,tp]/(x_1+x_2)^2;

n=3:
    det H=det[1,p,tp] det[1,t,tp]/Delta_+^2;

n=4:
    det H=det[1,t,p,tp] det[1,t,tp,t^2p]/Delta_+^2.
```

The order-three identity is equivalent to `L-92000`.  At order four, the raw
matrix sign becomes two generalized-convexity signs.

## Significance

The all-order safe-real criterion is sign regularity of two interlacing
alternant systems:

```text
1,t,t^2,... interlaced with p,tp,t^2p,...;
1,t,t^2,... interlaced with tp,t^2p,t^3p,....
```

Under RH, `p` is a Stieltjes transform and these are extended Chebyshev
systems.  A false-RH pole must eventually flip one of the alternant signs.

## Boundary

```text
all-order determinant factorization     EXACT
orders two and three                     RECOVERED
order-four alternant pair                EXACT
all actual-Xi signs                      OPEN / RH-EQUIVALENT
Riemann Hypothesis                       UNPROVED
```
