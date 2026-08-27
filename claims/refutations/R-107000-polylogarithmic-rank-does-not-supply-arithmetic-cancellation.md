# R-107000 — Polylogarithmic rank does not supply arithmetic cancellation

Claim ID: `R-107000`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-27  
Depends on: `L-107001`  
RH status: **unproved**

The finite-rank theorem does not imply its own norm bound.

Let \(v\ne0\) be one vector in a Hilbert space and take \(N\) labelled source
atoms, all with physical feature vector \(v\). Then

\[
\sum_{j=1}^N\|v\|^2=N\|v\|^2,
\]

while

\[
\left\|\sum_{j=1}^Nv\right\|^2=N^2\|v\|^2.
\]

The feature rank is one, but coherent collapse has an arbitrarily large
factor.

The same phenomenon can occur for logarithmically clustered integers:
\(n^{-it_{k,X}}\) and \(m^{-it_{k,X}}\) are close at every retained sample
when \(|\log(n/m)|K_A/P_X\) is small.

Therefore none of the following proves `NBV107000`:

```text
the feature dimension is polylogarithmic;
the diagonal energy is polylogarithmic;
each prime acts by a diagonal unitary phase;
a source-blind Gram rank bound;
triangle or Minkowski after separating owner/core fibres.
```

A proof must use the literal beta signs and correlations before taking the
norm.
