# T-100400 — Two surviving closure routes after exact interface reconstruction

Claim ID: `T-100400`  
Status: **UNCONDITIONAL REDUCTIONS; TWO FINAL GATES OPEN**  
Created: 2026-08-20  
Frozen base: PR #675 at `7b28224ba1b072d4ccd5b93ad37c0a64e7939740`  
RH status: **unproved**

## Route A: quadratic activation-collar gate

Let `mathcal E_2` be the quadratic upper-envelope defect and use the notation
of `L-100400`.  Define `QACG100400` to be eventual nonnegativity of either
side of the exact identity

\[
\begin{aligned}
\mathcal E_2(X)={}&
X(1+c)^2\sum_{n>\lambda_cX}{\beta(n)\over n^{3/2}}\\
&+(3-c)X\int_{\lambda_cX}^{\infty}L_c(t){dt\over t^2}
+P_c(X),
\qquad -1\le c\le0.
\end{aligned}
\]

The Mellin audit inherited from the quadratic-envelope route gives

\[
\boxed{\mathrm{QACG100400}\Longrightarrow\mathrm{RH}.}
\]

`R-100400` proves that no endpoint of this homotopy removes both atoms and
collar.

## Route B: rough largest-prime minimal wavelet

Let `G_rough` be (L-100410.4).  Define `LPMW100410` by

\[
\boxed{
\int_2^Z[G_{\rm rough}(X)]_-{dX\over X}=Z^{o(1)}.
}
\]

The smooth error has finite/subpower logarithmic mass, while PRs #674–#675
prove the minimal-wavelet negative-mass criterion equivalent to RH.  Hence

\[
\boxed{\mathrm{LPMW100410}\Longrightarrow\mathrm{RH}.}
\]

## Disposition of the phase-Hasse candidate

`L-100401` proves that the phase-Hasse symbol retains half of the Euler root at
nonzero phase.  It is therefore an auxiliary decomposition rather than a third
independent closure route.

```text
shifted-square atom/collar homotopy      PROVED EXACT
no simultaneous atom/collar removal      PROVED EXACT
QACG100400                                OPEN / RH-BEARING
largest-prime wavelet ownership           PROVED EXACT
smooth wavelet sector                     NEGLIGIBLE
LPMW100410                                OPEN / RH-BEARING
phase-Hasse root-free interpretation      REFUTED EXACTLY
Riemann Hypothesis                        UNPROVED
```
