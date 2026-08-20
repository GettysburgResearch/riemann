# R-100140 — Diagonal, local-gap, and free-labelled energies do not control the Poisson tails

Claim ID: `R-100140`
Status: **PROVED EXACT SOURCE-BLIND FIREWALL**
Created: 2026-08-20
Depends on: `L-100140`
RH status: **unproved**

Fix \(N\ge2\) and let

\[
c_n=\begin{cases}N^{-1/2},&N<n\le2N,\\0,&\text{otherwise}.
\end{cases}
\]

For every \(\tau>0\), the coefficient diagonal satisfies

\[
\sum_nc_n^2n^{2\tau}\le(2N)^{2\tau}.
\tag{R-100140.1}
\]

But by `L-100140`, every active pair has \(\min(m,n)>N\), so

\[
\boxed{Q_\tau(c)\ge N^{1+2\tau}.}
\tag{R-100140.2}
\]

Consequently

\[
\frac{Q_\tau(c)}{\sum_nc_n^2n^{2\tau}}
\ge\frac{N}{2^{2\tau}}.
\tag{R-100140.3}
\]

For \(\tau_N=1/\log\log N\), the diagonal is \(N^{o(1)}\), while

\[
Q_{\tau_N}(c)=N^{1+o(1)}.
\]

The same fixture is the physical-collapse vector from PR #660: its free
labelled norm is one and its scalar collapse is \(\sqrt N\).

Therefore none of the following, by itself, proves `GPMOC99800` or `OCE67`:

```text
the coefficient diagonal;
the local Cauchy–Poisson owner gap;
the free labelled Littlewood–Paley energy;
a source-blind Cauchy–Schwarz estimate;
a diagonal large sieve.
```

A valid proof must use the actual \(\beta\)-signs to control the tail sums
before absolute values.
