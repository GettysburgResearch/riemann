# M-99050 — Hostile reconstruction protocol for the score-last hardening

Review in this order:

1. Verify the one-node identity (L-99050.3) in every physical row coordinate.
2. Check that every current difference and terminal residual row is
   coefficientwise nonnegative.
3. Prove the endpoint depth bound (L-99050.7) for the actual `Y/67+1` scale.
4. Expand a complete finite rough-prime tree and verify source ownership.
5. Confirm the Hall bonus is included once and never enters a child.
6. Apply literal entropy only after the complete row expansion.
7. Reconstruct the endpoint-frame identity `H(R_eq)=4sqrt(X)` independently.
8. Recompute the top omission derivative and the bound `<60`.
9. Recompute the thinning bound `<792`.
10. Insert the resulting `<852` score loss into the exact all-column row and
    endpoint consumer.

Immediate falsifiers:

```text
an actual child endpoint fails to decrease;
a causal current row has a negative coefficient;
a source occurrence reaches two tree owners;
the Hall bonus is recursively copied;
endpoint integration changes a row identity;
the omitted top interval is also present in the output row;
H(R_eq) is a declared source score rather than literal physical-row entropy;
the final row differs from the row used in the capacity theorem.
```
