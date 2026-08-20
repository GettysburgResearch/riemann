# L-99812 — Phase twisting has an exact global Abelian spectral gap across squarefree cores

Claim ID: `L-99812`  
Status: **PROVED ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: the phase-owner square of PR #655; the classical PNT/nonvanishing of zeta on `Re(s)=1`  
RH status: **not assumed**

Fix a real `gamma!=0`.  For squarefree `n` coprime to `67`, put

\[
 \mathcal V_\gamma(n)
 =\sum_{p\mid n}\frac{\log p}{\log n}|1-p^{i\gamma}|^2,
 \qquad n>1,
\]

and set `V_gamma(1)=0`.  For real `sigma>1`, define

\[
 F(\sigma)=
 \sum_{\substack{n\ge1\;\mathrm{squarefree}\\(n,67)=1}}n^{-\sigma}
 =\prod_{p\ne67}(1+p^{-\sigma}).
\tag{L-99812.1}
\]

Finite differentiation of the Euler product gives

\[
 \sum_n n^{-\sigma}\log n
 =F(\sigma)
 \sum_{p\ne67}\frac{\log p}{p^\sigma+1},
\tag{L-99812.2}
\]

and finite subset switching gives

\[
 \sum_n n^{-\sigma}\log n\,\mathcal V_\gamma(n)
 =F(\sigma)
 \sum_{p\ne67}
 \frac{\log p}{p^\sigma+1}|1-p^{i\gamma}|^2.
\tag{L-99812.3}
\]

The prime number theorem yields

\[
 \sum_p\frac{\log p}{p^\sigma+1}
 =\frac1{\sigma-1}+O(1).
\tag{L-99812.4}
\]

Moreover

\[
 \sum_p\frac{\log p}{p^\sigma+1}p^{i\gamma}=O_\gamma(1)
 \qquad(\sigma\downarrow1),
\tag{L-99812.5}
\]

because it differs by an absolutely convergent prime-power correction from
`-zeta'/zeta(sigma-i gamma)`, and zeta is nonzero at `1-i gamma`.
Consequently

\[
 \sum_p\frac{\log p}{p^\sigma+1}|1-p^{i\gamma}|^2
 =\frac2{\sigma-1}+O_\gamma(1).
\tag{L-99812.6}
\]

Dividing (L-99812.3) by (L-99812.2) proves

\[
 \boxed{
 \lim_{\sigma\downarrow1}
 \frac{\sum_n n^{-\sigma}\log n\,\mathcal V_\gamma(n)}
      {\sum_n n^{-\sigma}\log n}
 =2.
 }
\tag{L-99812.7}
\]

Thus the local zero-dissipation result of PRs #655/#656 does not persist after
averaging across squarefree cores: every fixed nonzero phase has a strict
critical Abelian gap.

## Boundary

The theorem is global and Abelian.  It does not by itself localize the phase
energy to each multiplicative SHARP block, nor does it control the signed
cross-core Gram before absolute values.  That missing Abelian-to-Carleson
localization is the exact surviving proof obligation.
