# L-32412 — The true Q=4 pole current fits inside the Kummer reserve cofinally

Claim ID: `L-32412`  
Title: On every sufficiently large quarter-balanced carry row, the correctly typed Q=4 pole-sensitive physical square plus the complete Selberg forcing is bounded by the generalized-prime Kummer square  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32405`, `L-32411`  
Scope: cofinal balanced row inequality for the true centered-interval physical current; no reflected block recurrence or RH claim

## 1. Inputs

For the Q=4 Euler–Blaschke system define on a carry row `n=j+k`

\[
 P_4(n,j)=\sum_{q\le n}\Lambda_4(q)\chi_{n,q}(j),
\]

\[
 S_4(n,j)=\sum_{q\le n}
 [\Lambda_4\log+\Lambda_4*\Lambda_4](q)\chi_{n,q}(j),
\]

and

\[
 \mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j).
\]

`L-32405` proves

\[
 \mathcal R_4(n,j)>0
\]

for every quarter-balanced row and supplies a fixed quadratic moat on the
cofinal tail.

Let

\[
 Q_4^{\rm phys}(n,j)
 =G_4(n)-G_4(j)-G_4(k)
\]

be the correctly typed pole-sensitive centered-interval current of
`R-32403/L-32407`.

## 2. Vanishing relative current cost

`L-32411` proves

\[
 \boxed{
 \sup_{n/4\le j\le3n/4}
 \frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
 \longrightarrow0.
 }
 \tag{L-32412.1}
\]

Therefore there exists a finite `N_*` such that for every `n>=N_*` and every
quarter-balanced `j`,

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2\le\mathcal R_4(n,j).
 }
 \tag{L-32412.2}
\]

No effective value of `N_*` is required for the cofinal theorem. It may be made
effective by inserting any standard effective PNT remainder into `L-32411`.

## 3. Complete augmented Kummer inequality

Substitute

\[
 \mathcal R_4=P_4^2-S_4
\]

into (L-32412.2). This gives the source-matched augmented inequality

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2+S_4(n,j)
 \le P_4(n,j)^2
 }
 \tag{L-32412.3}
\]

for every `n>=N_*` and every quarter-balanced split.

Thus the complete generalized-prime Kummer square simultaneously pays:

1. the entire Q=4 Selberg second-moment forcing; and
2. the actual RH-sensitive physical pole current.

There is no double spending at one row: the current is paid by the explicit
remainder `R_4=P_4^2-S_4` left after the Selberg forcing has already been
charged.

More generally, for every fixed `0<delta<1`, cofinally

\[
 \boxed{
 |Q_4^{\rm phys}|^2+S_4
 \le P_4^2-(1-\delta)\mathcal R_4.
 }
 \tag{L-32412.4}
\]

So an arbitrarily large fraction of the Kummer reserve remains unused after the
physical pole current is absorbed.

## 4. Finite row-measure form

Let `nu(n,j)>=0` be any finite row measure supported on parents `n>=N_*` and
quarter-balanced positions. Summing (L-32412.3) gives

\[
 \boxed{
 \sum\nu |Q_4^{\rm phys}|^2
 +\sum\nu S_4
 \le\sum\nu P_4^2.
 }
 \tag{L-32412.5}
\]

Likewise (L-32412.4) leaves the positive unused slack

\[
 (1-\delta)\sum\nu\mathcal R_4.
\]

This is the exact form needed for a Schur/SOS assembly in a physical block:
the current square is already inside the source-matched Kummer budget before
any lower-scale source change is estimated.

## 5. What this closes and what it does not

This theorem closes the **one-row no-double-spend inequality** which was missing
from the earlier Q=4 discussion. It is stronger than a fixed transference
constant and uses the true pole-sensitive coordinate.

It does not by itself identify the complete independent-frequency reflected
product term with `P_4^2`, nor route the source-convolved product/individual terms
between blocks. Those are algebraic/block-assembly statements and remain the
last global step.

## 6. Proof boundary

Closed here, subject to review:

1. cofinal current-inside-reserve inequality;
2. the augmented Kummer inequality `|Q_phys|^2+S<=P^2`;
3. explicit no-double-spend interpretation;
4. finite row-measure version with positive leftover slack.

Still open:

1. complete two-frequency reflected block assembly and identification of its
   row measure;
2. strict-delay/neutral-scattering block recurrence;
3. RH.
