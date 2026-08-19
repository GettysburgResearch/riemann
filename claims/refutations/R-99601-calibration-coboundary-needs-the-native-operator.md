# R-99601 — A Bellman calibration coboundary cannot repair an unproved native operator

Claim ID: `R-99601`  
Status: **PROVED EXACT TYPE FIREWALL**  
Created: 2026-08-20  
Compared input: PR #648  
RH status: **not assumed**

The algebra

\[
E=P+A,\qquad P=J+PT
\]

implies

\[
E=J+ET+(A-AT)
\]

and, for nilpotent \(T\),

\[
E=J(I-T)^{-1}+A.
\]

This is exact and useful. It proves descendant calibration cancellation once
all three objects \(E,P,A\) use the same already-established physical child
operator.

It does **not** prove any of the following:

1. that \(P\) has the native Möbius root marginal;
2. that the recursively exported coefficient is \(p^{-1/2}\);
3. that an endpoint RN restriction has the same rough-prime coefficient as the
   native Euler occurrence;
4. that an abstract equality \(E=P+A\) is source-owned rather than defined
   after observation.

The one-prime separator `R-99600` is invariant under the coboundary algebra:
with the contracted alpha operator, the shifted coefficient remains zero (or
\(2r^2\) in the parity export), not the native \(r\).

Therefore the application order is binding:

```text
prove the native source/operator dictionary;
prove one common RN/source coupling;
only then telescope calibration as A-AT.
```

PR #648's abstract theorem survives. Its use as a complete closure theorem
remains conditional on the first line, which is replaced by the exact
first-owner identity in `L-99601`.
