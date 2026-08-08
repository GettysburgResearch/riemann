# O-27201 — Ternary fragmentation reconnaissance and scope boundary

Claim ID: `O-27201`  
Status: **NON-DIRECTED DISCOVERY EVIDENCE / NOT A CERTIFICATE**

The deterministic ternary recurrence of `L-27201` was evaluated in ordinary
double precision for the actual logarithmic target through the endpoints

```text
X = 100000, 1000000, 5000000.
```

No negative coefficient was observed. Excluding the tautological terminal
coefficient `A_X(X)=0`, the smallest observed coefficients were approximately

```text
X=100000    3.16232e-8   at n=99999
X=1000000   1.00000e-9   at n=999999
X=5000000   8.94427e-11  at n=4999999.
```

The same computation distinguishes the proposal from the single central split:
the pure half-split recurrence already develops negative coefficients near a
fixed interior ratio, whereas the ternary producer did not on this range.

This is useful discovery evidence only. The smallest coefficients are far too
small for an undirected floating calculation to certify a cofinal sign, and a
hypothetical off-line zero would be expected to appear only through eventual
large-scale oscillation. No finite endpoint table is promoted to `TFP` or RH.

The exact proof-facing object remains the recurrence

```text
S_X(n)=u_n+S_X(ceil(3n/2))+S_X(3n-2),
A_X(n)=S_X(n)-S_X(n+1).
```

The next analytic attack should bind this renewal to the positive base-three
digit comb while retaining the divisibility boundary in `L-27202`.
