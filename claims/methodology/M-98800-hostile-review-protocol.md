# M-98800 — Hostile reconstruction protocol

Review in this order:

1. Reproduce the `x=2` negative Hall-edge score and confirm no new theorem
   assigns a score coordinate to the bonus.
2. Check target conservation and every component-row Hall identity on the same
   flow coefficients.
3. Verify that the bonus appears only in the current row and never in a child or
   target-mass calculation.
4. Reconstruct actual child masses before normalizing or grouping them.
5. Verify omissions occur before the common endpoint kernel.
6. Confirm the same Markov kernel acts on source and row-bonus sorts.
7. Confirm `q` and `4q` responses come from one row before taking detail.
8. Reconstruct the retained-cell seed for `2<=q<K`; reject a cutoff atom.
9. Verify top source is not both output and omitted.
10. Pair the actual final slack with `Y_4`; reject any use of
    `J_Lambda-4sqrt(X)`.
11. Reconstruct the endpoint, prime-square, Mellin-Landau, and reflection chain
    at the exact frozen normalizations.

Immediate falsifiers:

```text
bonus has target or declared score;
bonus is recursively copied;
separate quantizers by label/child;
omission after quantization;
signed mismatch promoted to positive source;
unweighted child-label counting;
q<K absent;
q and 4q taken from different rows;
root corrections copied at every generation;
RH-bearing benchmark bridge imported upstream.
```
