# L-91335 — The factor-54 Hall shadow has a uniform one-rough-prime parameter corridor

Claim ID: `L-91335`  
Status: **PROPOSED COMPLETE DIRECTED ONE-STEP HALL THEOREM — ALL-GENERATION TYPED RESET OPEN**  
Created: 2026-08-12  
Depends on: `L-91109`, `L-91317`, `L-91328`  
RH status: **unproved**

## 1. Generalized parity weights

For `a>0`, real `x>=1`, and squarefree `n<=x`, put

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
\]

Let `E_a^x` and `O_a^x` denote the positive even- and odd-squarefree measures with these weights.

For a demand threshold `t` and displacement `delta`, define

\[
 \mathcal H_{a,t}^{(\delta)}(x)
 =\sum_{\substack{e\le t+\delta\\\mu(e)=1}}w_a(x,e)
  -\sum_{\substack{o\le t\\\mu(o)=-1}}w_a(x,o).
\tag{L-91335.1}
\]

On each activation cell the margin is affine in `sqrt(x)` and affine in `a`.

## 2. Rough one-step parameter range

For a prime `p>=67`, put `r=p^{-1/2}`. On the fully paired part of one Euler factor,

\[
 w_a(x,n)-w_a(x,pn)
 =(1-r)w_a(x(1+r)^2,n).
\]

Equivalently, in diagonal state notation, the parameter is multiplied by

\[
 a\longmapsto a(1+r).
\]

Thus the two critical inputs generate the intervals

\[
 1\le a\le1+67^{-1/2}
\]

and

\[
 2\le a\le2(1+67^{-1/2}).
\]

## 3. Directed Hall theorem

On the complete reset window

\[
 1\le x\le c_0^{-1},
\]

the companion directed checker proves:

### Reserve corridor

For every

\[
 1\le a\le1+67^{-1/2},
\]

and every active odd threshold,

\[
 \boxed{
 \mathcal H_{a,t}^{(0)}(x)>\frac8{25}.
 }
\tag{L-91335.2}
\]

Hence every odd demand transports to even capacity with support

\[
 e\le o.
\]

### Equality corridor

For every

\[
 2\le a\le2(1+67^{-1/2}),
\]

and every active odd threshold,

\[
 \boxed{
 \mathcal H_{a,t}^{(1)}(x)>\frac1{400}.
 }
\tag{L-91335.3}
\]

Hence every odd demand transports with support

\[
 e\le o+1.
\]

Because the margins are affine in `a`, it is enough to certify the two parameter endpoints. Because they are affine in `sqrt(x)` on each activation cell, cell endpoints suffice.

The replay checks `2148` endpoint/threshold gates in each channel with directed rational square-root enclosures.

## 4. Significance

The theorem supplies a robust local parity projection after **one new least rough prime**, exactly the one-prime-per-reset regime of `L-91328`. It survives the parameter deformation caused by one rough Euler factor and retains the same support graph used by the finite endpoint packets.

It is therefore concrete input for an interleaved reset construction of the kind isolated in `L-91334`.

## 5. Scope firewall

This theorem does not establish multiprime scalar tensorization. It also does not by itself prove that:

- the heterogeneous paired-interior and activation-frontier pieces combine into one typed endpoint source partition;
- the `+1` equality edges are realized with all physical capacities and score charged once;
- the controlled residual state returns to the required two-state cone at every generation.

Those are the remaining one-step assembly obligations.

## 6. Verification and boundary

Retained verdict:

```text
PASS_ONE_ROUGH_PRIME_HALL_CORRIDOR
```

```text
reserve one-prime parameter corridor             DIRECTED EXACT
equality one-prime parameter corridor            DIRECTED EXACT
one-prime Hall support graphs                     EXACT
multiprime scalar tensorization                   NOT CLAIMED
one-step typed endpoint/source reset              OPEN
all-generation coefficient-one recurrence         OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```
