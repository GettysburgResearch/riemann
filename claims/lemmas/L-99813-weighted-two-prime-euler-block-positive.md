# L-99813 — Every active weighted two-prime SHARP box Euler block is positive

Claim ID: `L-99813`  
Status: **PROVED EXACT GLOBAL TWO-PRIME THEOREM**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`  
RH status: **not assumed**

Let `Phi(y)=phi(y)` be the normalized factor-67 box potential, zero extended below one. For primes `67<=p<q`, put `r_p=p^{-1/2}`, `r_q=q^{-1/2}` and define the literal two-prime Euler block

\[
 \mathcal B_{p,q}\Phi(y)
 :=\Phi(y)-r_p\Phi(y/p)-r_q\Phi(y/q)+r_pr_q\Phi(y/(pq)).
\]

Then

\[
 \boxed{\mathcal B_{p,q}\Phi(y)>0\qquad(y\ge pq).}
\tag{L-99813.1}
\]

## Deep region

If `y/(pq)>=67`, write

\[
 \Phi(t)=A-Bt^{-1/2},
 \quad A=8(1-67^{-1/2}),\quad B=3\log67.
\]

A direct calculation gives

\[
 \mathcal B_{p,q}\Phi(y)
 =A(1-r_p)(1-r_q),
\]

because the half-order term cancels exactly:

\[
 y^{-1/2}-r_p(y/p)^{-1/2}-r_q(y/q)^{-1/2}+r_pr_q(y/(pq))^{-1/2}=0.
\]

Hence the block is strictly positive.

## Active collar

Let `y=pqz`, `1<=z<67`. Then `pz,qz,pqz>=67` and only the final argument `z` lies in the collar. Exact simplification yields

\[
 \boxed{
 \mathcal B_{p,q}\Phi(pqz)
 =A(1-r_p)(1-r_q)
 +\frac{R(z)}{67\sqrt{pqz}},
 }
\tag{L-99813.2}
\]

where

\[
 R(z)=8\sqrt{67z}-201\log z-536+201\log67.
\]

Now

\[
 R'(z)=\frac{4\sqrt{67}}{\sqrt z}-\frac{201}{z},
\]

so `R` has its unique minimum at

\[
 z_0=(201/(4\sqrt{67}))^2=603/16.
\]

Elementary outward bounds give

\[
 R(z)>-19\qquad(1<=z<=67).
\]

Also `p>=67`, `q>=71`, `z>=1`, so the negative correction is bounded below by

\[
 -\frac{19}{67\sqrt{67\cdot71}}>-0.0042.
\]

On the other hand

\[
 A(1-r_p)(1-r_q)
 \ge8(1-67^{-1/2})^2(1-71^{-1/2})>5.9.
\]

Thus the full collar block is positive with a large uniform margin. This proves (L-99813.1).

## Scope

This is the sign of the **actual weighted Euler block**, unlike unweighted mixed submodularity. The activation condition `y>=pq` is exactly the condition that all four native source vertices of the two-prime cube are present.

The theorem permits grouping the native rough Euler product into positive two-prime factors at the box-kernel level. A complete all-prime sign theorem still requires controlling the effect of applying subsequent Euler factors to an already-positive paired block and, when the number of active primes is odd, one unpaired prime factor. Those interfaces are not asserted here.
