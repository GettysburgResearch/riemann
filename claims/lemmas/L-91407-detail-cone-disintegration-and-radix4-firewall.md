# L-91407 — Signed radix-four capacity requires cone-valued disintegration, not coordinatewise positive color erasure

Claim ID: `L-91407`  
Status: **EXACT ABSTRACT THEOREM AND METHOD FIREWALL**  
Created: 2026-08-12  
Depends on: PR #399 `L-91324/L-91325`; `L-91401`  
RH status: **unproved**

## 1. Lift the signed detail to a positive two-coordinate order

Let `R_q` be a positive linear ordinary-column response on positive endpoint measures. Define

\[
 \mathbf R_q(\mu)
 =\bigl(R_q(\mu),\,2R_{4q}(\mu)\bigr)
\]

and the closed cone

\[
 \mathcal K=\{(x,y):x\ge y\ge0\}.
\]

Then

\[
 R_q(\mu)-2R_{4q}(\mu)\ge0
 \iff
 \mathbf R_q(\mu)\in\mathcal K.
\tag{L-91407.1}
\]

For two measures `d,t`, write

\[
 d\preceq_{q,\mathcal K}t
 \iff
 \mathbf R_q(t-d)\in\mathcal K.
\]

This is the correct order for a radix-four capacity constraint.

## 2. Cone-valued disintegration theorem

Let `mu=sum_b mu_b+mu_0` be a positive source partition, and let a positive Markov kernel send it to target shares

\[
 \nu_b(B)=\int K(x,B)d\mu_b(x),
 \qquad
 \nu=\sum_b\nu_b+\nu_0.
\]

Assume the kernel is detail-cone positive:

\[
 \boxed{
 \mathbf R_q(K_x)\in\mathcal K
 \quad\text{for every source point }x
 \text{ and every required }q.
 }
\tag{L-91407.2}
\]

Then every target share satisfies

\[
 \mathbf R_q(\nu_b)\in\mathcal K,
\]

and the shares add without spending the physical detail twice.

More generally, if branch packings `d_b` obey

\[
 d_b\preceq_{q,\mathcal K}\nu_b
\]

for every `b,q`, then

\[
 \boxed{
 \sum_bd_b\preceq_{q,\mathcal K}\nu.
 }
\tag{L-91407.3}
\]

The proof is closure of `K` under positive integration and addition.

## 3. Coordinatewise positivity is insufficient

Ordinary positive color erasure proves only that the two coordinates are nonnegative. It does not prove their difference has the required sign.

The elementary residual

\[
 R_q(t-d)=1,
 \qquad
 R_{4q}(t-d)=1
\]

satisfies both ordinary inequalities but has

\[
 R_q(t-d)-2R_{4q}(t-d)=-1.
\]

Equivalently, subtracting two valid ordinary inequalities is not an order-preserving operation. This is the exact abstract form of the radix-four scope warning already present in PR #399 `L-91324`.

## 4. Consequence for the factor-54 reset

A full reset certificate must include, for every active `q`, either

\[
 \bigl(R_q,2R_{4q}\bigr)\in\mathcal K
\]

or the equivalent signed-detail inequality itself. A positive partition of total endpoint mass, a SHARP-mass identity, or ordinary-column feasibility alone cannot certify the reset.

The robust grid theorem `L-91401` remains applicable after enlarging its finite output vector by these cone coordinates. The exact remaining finite task is therefore

\[
 \boxed{
 \text{certify a strictly positive dual margin in the complete signed-detail output cone.}
 }
\tag{L-91407.4}
\]

A positive margin produces an exact nonnegative integer-grid reset. A failed margin returns a separating functional identifying the first genuine radix-four deficit.

This theorem does not refute the factor-54 programme. It makes its last finite certificate fail-closed and prevents ordinary positive disintegration from being mistaken for signed-detail feasibility.
