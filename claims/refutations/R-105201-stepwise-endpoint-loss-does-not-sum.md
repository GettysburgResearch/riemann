# R-105201 — The stepwise endpoint `-1` cannot be accumulated naively

Claim ID: `R-105201`
Status: **BINDING SCOPE FIREWALL**
Created: 2026-08-23
RH status: **not assumed**

The one-step inequality of `L-104522` is

\[
N_\mathbb R(f;(a,b))
\ge(2C-1)N_\mathbb R(f';(a,b))-1.
\]

Even when the product of the multiplicative factors `2C-1` has a positive
limit, summing the displayed `-1` over an arbitrarily long derivative ladder
would be invalid and can lose a quantity proportional to the number of
levels.

Therefore `L-105201.7` is a theorem about the **multiplicative coherence
factor only**. The endpoint terms must be handled by the exact endpoint and
winding ledger, or bypassed by the independent high-band zero-count theorem
`L-104517`.

In the high Xi derivative band, `L-104517` already gives the exact
sine/cosine-cell count with one global `O(1)` boundary error at each fixed
level. No conclusion in T-105200 is obtained by summing the coarse one-step
`-1` term.
