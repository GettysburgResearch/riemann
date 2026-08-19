# L-99101 — Partition first and normalize last

Claim ID: `L-99101`  
Status: **PROVED EXACT BARYCENTRIC TRANSFER THEOREM**  
Created: 2026-08-19  
RH status: **unproved**

Let a positive unnormalized packet decompose as

\[
 \mu=\sum_{a=0}^m\mu_a.
 \tag{L-99101.1}
\]

Let `M(mu)>=0` be additive, with `M(mu)>0`, and let

\[
 Z(\mu)=(R_1(\mu),\ldots,R_d(\mu))
\]

be a vector of additive real observables. For pieces of positive mass define

\[
 z(\mu_a)=\frac{Z(\mu_a)}{M(\mu_a)},
 \qquad
 w_a=\frac{M(\mu_a)}{M(\mu)}.
\]

Then

\[
 \boxed{
 z(\mu)=\sum_{a:M(\mu_a)>0}w_az(\mu_a),
 \qquad
 w_a\ge0,
 \quad\sum_aw_a=1.
 }
 \tag{L-99101.2}
\]

Consequently, for every convex function `Phi` on the normalized datum,

\[
 \boxed{
 \Phi(z(\mu))
 \le\sum_aw_a\Phi(z(\mu_a)).
 }
 \tag{L-99101.3}
\]

This is ordinary Jensen applied only after the source partition is complete. It is the correct interface when raw source ownership is literal but coordinatewise domination of already normalized child packets is unavailable.

In particular, if a native deficit is convex in the normalized target/row/score data, it can be controlled by the mass-weighted deficits of the actual pieces. No statement that a normalized child is a coordinatewise submeasure is needed.

## Scope firewall

The theorem does not prove convexity of a repository-specific native deficit. That must be checked from its exact formula. It also does not allow target mass, score, or endpoint capacities to be normalized with different denominators. All coordinates in one application must share the same additive mass `M`.
