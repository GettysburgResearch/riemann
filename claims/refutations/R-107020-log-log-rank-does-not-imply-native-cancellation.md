# R-107020 — Logarithmic-by-logarithmic rank does not imply native cancellation

Claim ID: `R-107020`  
Status: **PROVED EXACT SOURCE-BLIND FIREWALL**  
Created: 2026-08-27  
RH status: **unproved**

Let \(v\ne0\) be one vector in a feature space of arbitrary finite dimension.
For \(N\) labelled source atoms put

\[
v_j=v\qquad(1\le j\le N).
\]

The labelled diagonal energy is

\[
\sum_{j=1}^N\|v_j\|^2=N\|v\|^2,
\]

whereas coherent physical collapse gives

\[
\left\|\sum_{j=1}^Nv_j\right\|^2=N^2\|v\|^2.
\]

Thus even rank one permits a linear coherent amplification in the norm.
Consequently the rank bound in `T-107020` does not imply `HNBV107020`.

A continuation must use the literal signs

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\]

and correlate them before taking the feature norm. Random-projection,
source-blind trace and diagonal-only arguments are insufficient.
