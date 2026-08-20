# R-99960 — Neither positive owner square removes the canonical scalar obstruction

Claim ID: `R-99960`  
Status: **PROVED EXACT INTERFACE FIREWALL**  
Created: 2026-08-20  
Frozen target: `HTOC99810` and `DGOC99810` in PR #666  
RH status: **unproved**

Let `f=sum_n c_n`.

The Hardy square has the exact decomposition

\[
Q_\tau(c)=|f|^2+Q_\tau^\circ(c),
\qquad Q_\tau^\circ(c)\ge0.
\]

The divisor square has

\[
\mathcal G_\tau(c)=|f|^2+
\sum_{d\ge2}J_{2\tau}(d)
\left|\sum_{d\mid n}c_n\right|^2.
\]

Therefore a proof which bounds only the non-root terms proves no sign or size
bound for `f`. This is not a technical omission: for a one-atom packet both
excesses vanish identically while `|f|` is arbitrary.

The same issue survives on native support. Choose a large interval containing
`N` distinct primes and give them the common native Möbius sign. On a subcell
where the physical kernel has one fixed nonzero sign and varies by `o(1)`, the
root term is of order `N^2`, while the coefficient diagonal is only order `N`.
The prime number theorem supplies such clusters with `N->infinity`.

Hence:

```text
Hardy excess without root term       insufficient;
divisor excess without d=1           insufficient;
diagonal/source-blind owner energy   insufficient even on native signs;
canonical scalar cancellation        still load-bearing.
```

The exact equivalence theorem `L-99960` is the correct lifecycle statement:
proving either full packing theorem is already proving RH.
