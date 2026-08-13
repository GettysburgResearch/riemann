# L-91410 — All mode-dependent rough branches and survival recanonicalize exactly after extracting their common parts

Claim ID: `L-91410`  
Status: **PROVED EXACT POINTWISE / MEASURE-VALUED REGENERATION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91335/L-91336`; packet-valued consumer `T-91401`  
RH status: **unproved**

## 1. Two mode ledgers

Fix one source point and its ordered active rough primes. For each mode `sigma in {X,Y}`, let

\[
 s_\infty^\sigma+\sum_j h_j^\sigma=1,
 \qquad s_\infty^\sigma,h_j^\sigma\ge0,
\]

be the exact survival and least-prime branch coefficients of `L-91336`.

For a positive physical state `u=(L,R)^T`, use the canonical hidden lift

\[
 Iu=(L,R,L,2R)^T.
\]

The survival matrix and branch matrices are

\[
 Q_\infty=\operatorname{diag}(s_\infty^X,s_\infty^X,s_\infty^Y,s_\infty^Y),
\]

\[
 H_j=\operatorname{diag}(h_j^X,h_j^X,h_j^Y,h_j^Y).
\]

## 2. Common canonical child

Define

\[
 \boxed{\alpha_j=\min(h_j^X,h_j^Y),}
 \qquad
 \Theta=\sum_j\alpha_j.
\]

Then

\[
 H_jIu=\alpha_jIu+(H_j-\alpha_jI_4)Iu,
\]

and every term is coordinatewise nonnegative.

## 3. Exact aggregate identity

The key point is that the survival packet and **all** mode-excess packets must be summed before physical observation. Their `X` coefficient is

\[
 s_\infty^X+\sum_j(h_j^X-\alpha_j)=1-\Theta,
\]

and the `Y` coefficient is identically

\[
 s_\infty^Y+\sum_j(h_j^Y-\alpha_j)=1-\Theta.
\]

Therefore

\[
 \boxed{
 Q_\infty Iu+\sum_j(H_j-\alpha_jI_4)Iu
 =(1-\Theta)Iu.
 }
\tag{L-91410.1}
\]

Equivalently,

\[
 \boxed{
 Iu=(1-\Theta)Iu+\sum_j\alpha_jIu.
 }
\tag{L-91410.2}
\]

Thus the aggregate remainder is not a noncanonical hidden packet. It is exactly one canonical positive current packet.

## 4. Pointwise source measures

When the active prime set depends on the source point, define `alpha_j` and `Theta` pointwise. Equation (L-91410.2) is then an identity of positive vector-valued measures.

The branch indexed by `j` is a literal submeasure of the exact least-prime branch and is transported to its genuine child endpoint `X/p_j`. The current coefficient is `1-Theta>=0`.

For every additive positive packet mass `m`,

\[
 \boxed{
 m(P_{\rm current})+\sum_jm(P_j)=m(P_{\rm parent}).
 }
\tag{L-91410.3}

No source atom is duplicated.

## 5. Target and score

Every term in (L-91410.2) is canonical before observation. Hence the same coefficient measure is used by both physical ledgers

\[
 L+2R,
 \qquad
 2L+R.
\]

This removes the reviewed mismatch in which one isolated mode-dependent branch had target `2r` and score `r^2`, while an `r`-scaled child demanded score `r`.

For the pure reserve one-prime test,

\[
 h^X=r^2,\qquad h^Y=r,
\]

so

\[
 \alpha=r^2,
 \qquad
 P_{\rm current}=(1-r^2)P,
 \qquad
 P_{\rm child}=r^2P.
\]

The apparent excess `r-r^2` is part of the current canonical packet after survival and all mode excesses are regrouped.

## 6. Tail index is retained

A child remains labelled by the next admissible prime index. No fixed small-prime block is reintroduced. The construction is uniform in the tail index because it uses only the exact local survival and branch coefficients.

## 7. Packet-cone consequence

If the parent belongs to a canonical positive packet cone closed under positive restriction and affine child pushforward, then the current packet and every child in (L-91410.2) remain in that cone.

Together with packet-deficit homogeneity and subadditivity, (L-91410.3) supplies the exact mass side of `T-91401` without scalar packet homogeneity.

```text
common child extraction                    EXACT
aggregate remainder = canonical packet     EXACT
pointwise measure partition                 EXACT
same target/score coefficient measures      EXACT
source mass equality                        EXACT
tail-prime index retained                    EXACT
finite physical producer                    SEPARATE INPUT
Riemann Hypothesis                           UNPROVED
```
