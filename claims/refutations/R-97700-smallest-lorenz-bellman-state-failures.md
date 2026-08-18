# R-97700 — Smallest exact failures of underspecified Lorenz-Bellman states

Claim ID: `R-97700`  
Status: **PROVED EXACT NO-GO THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

The following candidate states are insufficient.

1. **One scalar.** `D^+(0)` does not contain target capacity or the Lorenz threshold profile. `L-97702` gives a one-node NCBI-positive source with target capacity `1<2`; `D^+(-10)=-9`.
2. **Forward slack without reverse orientation.** At `lambda=1`, the empty source and a single even zero-scalar atom both have `D^+=0`, but reverse slacks `0` and `1`. A swapped rough child distinguishes them.
3. **Root value without the future quotient.** The recurrence `G_new(X)=G(X)-p^(-1/2)G(X/p)` uses a quotient value not determined by `G(X)`. Profiles with `G(X)=1` and child values `0` versus `2` give different descendants.
4. **Two-sided nonnegative cone.** This cone is preserved by positive swap addition but fails on the literal base source at the smallest endpoint. At `X=1`, `lambda=-1`, `(D^+,D^-)=(1,-1)`.
5. **Source-local one-channel contraction.** The two-node separator of `R-97500` remains binding: replacing raw coefficient `r` by `t<r` forces current `t-r<0` at the parent.

Therefore the smallest exact viable state exposed so far is the paired orientation profile on the actual future-prime quotient DAG. Any smaller state has an explicit separator above.