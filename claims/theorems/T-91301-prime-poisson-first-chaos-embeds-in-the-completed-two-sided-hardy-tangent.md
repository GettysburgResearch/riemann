# T-91301 — The ordinary-prime Poisson first chaos has an explicit completed-boundary Hardy component

Claim ID: `T-91301`  
Status: **PROVED EXACT PRIME BOUNDARY-COMPONENT COLLIGATION; COMMON COMPLETED SOURCE MAP OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: `L-91035`, `L-91036`, `L-91306`, `L-91307`, `L-91401`, `R-91301`, `R-91402`  
RH status: **unproved**

## 1. Exact prime component

Fix

\[
 a_0=4,
 \qquad c_0=\frac92.
\]

Let

\[
 d\beta_4(u)
 =4\sum_{n=p^k}\Lambda(n)n^{-9/2}
  \delta_{\log n}(du)
\tag{T-91301.1}
\]

and

\[
 (\mathsf H_{\beta_4}g)(t)
 =\int_{u>t}g(u-t)d\beta_4(u).
\tag{T-91301.2}
\]

Then:

1. after the standard Hardy reflection, `H_(beta_4)` is exactly the
   positive-frequency Hankel block of the ordinary-prime Suzuki scattering
   score;
2. the explicit maps `D_0,D_1,D_2` of `L-91307` satisfy
   \[
    \boxed{
    \|g\|^2
    =\|\mathsf H_{\beta_4}g\|^2
     +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2;
    }
    \tag{T-91301.3}
   \]
3. reflection gives the opposite Hardy orientation;
4. the gamma/pole factor enters the observed completed boundary derivative as
   the skew covariant connection of `L-91306`.

Thus the actual ordinary-prime source-linear output has an explicit
first-chaos/tail-Hankel Julia realization.  No square root of an unknown Weil
matrix is used.

## 2. Completed-boundary placement

Write on the real boundary

\[
 \Theta_a=\Gamma_aZ_a.
\]

The moving-unitary identity of `L-91306` is

\[
 \boxed{
 (I-Q_a)\partial_{\log a}M_{\Theta_a}
 =M_{\Gamma_a}(I-R_a)
  \left(\partial_{\log a}V_a+A_aV_a\right).
 }
\tag{T-91301.4}
\]

The ordinary-prime Hankel block is the prime component inside the covariant
source derivative.  The gamma/pole factor is retained rather than discarded as
a signed scalar remainder.

This is an exact placement at the **observed boundary-tangent level**.  It is
not yet an isometry from the prime Poisson probability source to the completed
xi Fisher probability source; `R-91402` proves that those two laws cannot be
identified as the same positive Levy source.

## 3. Correct delay statement

A raw delay does not generally preserve `K_(Theta_a)`.  For the positive Hardy
delay `S_tau`, `L-91401` supplies the exact Julia split

\[
 \boxed{
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g,
 }
\tag{T-91301.5}
\]

where

\[
 T_\tau^*T_\tau+R_\tau^*R_\tau=I.
\tag{T-91301.6}
\]

For every mixed-delay packet,

\[
 \boxed{
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
 }
\tag{T-91301.7}
\]

Thus the prime Hardy output extends to two orientations and arbitrary positive
delays once the explicit leakage reserve is retained.  Raw delay invariance is
not claimed.

## 4. Higher chaos

`L-91036` shows that, within a chosen positive Poisson product system, an
exactly source-linear target uses only compensated first chaos.  Hence higher
prime Poisson chaoses are unused environment for the ordinary-prime tangent.

This does not imply that the completed xi Fisher law is Poisson infinitely
divisible.  That separate shortcut is refuted by `R-91402`.

## 5. What remains

The closed component is

\[
 \boxed{
 \text{ordinary-prime Poisson first chaos}
 \longrightarrow
 \text{two-sided delayed prime Hardy output}
 \oplus
 \text{explicit Julia reserves}.
 }
\tag{T-91301.8}
\]

The open completion is a renormalized source map that sends the prime
Poisson/Julia source together with gamma/pole/theta channels into the completed
Fisher--Hankel source of `L-91316`, preserving the visible block and every
auxiliary norm.  After that map is constructed, its defect must still be
identified with the delayed zeta screw/Weil Gram.

## 6. Exact boundary

```text
ordinary-prime score measure                         EXACT
prime score -> Hardy tail-Hankel                     EXACT
explicit positive Julia reserve at a0=4             EXACT
opposite Hardy orientation                          EXACT
raw-delay invariance of K_Theta                     REFUTED
compressed delays + leakage                         EXACT
gamma/pole placement at observed tangent level      EXACT
prime Poisson law = completed Fisher law            REFUTED
renormalized common completed source map             OPEN
common-source defect = delayed screw/Weil Gram       OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
