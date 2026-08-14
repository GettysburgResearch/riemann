# Review specification — T-91659 native-root compiler/separator

## Frozen objects

Reconstruct at the exact commits listed in `integration/2026-08-14/t91659-native-root-compiler-lock.json`. Do not substitute moving branch heads.

## Mandatory checks

### A. Raw separator

Verify independently:

1. the rough sets below `68` and `17`;
2. the ordinary response at `X=136,q=2`;
3. the exact terminal child response;
4. the detail response using columns `2` and `8`;
5. the lower bounds `delta>1/810` and `Y4(2)delta>1/1215`;
6. the infinite family `X=2(p+1)` and the surviving `m=67` reservoir term.

Reject `R-91686` if the raw child does not remove exactly the `m=p` term or if another normalization is silently used.

### B. Root-Hall compiler

For every clause of `T-91314`, identify the exact object exported by PR `#464`. Formal positive-linear commutation is not a finite source-owned realization. Check specifically:

```text
ordinary columns;
detail columns;
shared port;
finite mismatch/collar/omission ownership;
target-mass debt normalization;
Y4 slack vector.
```

### C. Lorenz LP theorem

Prove the two threshold-dual inequalities directly. Verify that the frozen profiles have the required monotone directions. A negative leftmost margin must be treated as a full-LP separator, not merely failure of one heuristic basis.

### D. Direct radix-four theorem

Check the inverse

\[
C(q)=\sum_{k\ge0}2^k\Xi(4^kq)
\]

before reconstructing rows. Verify the top two entries of `B^{-1}R_4e_q` from the exact carry coefficients. Inspect the full lower tail before using a zero-cost direction in a closure claim.

### E. Scope

The replay proves finite exact/directed statements only. It does not prove all activation cells, source-owned thinning, ports, NRCT, CFFP, or RH.

## Immediate falsifiers

```text
finite continuum defect is set to zero;
canonical finite-Euler capacity is called native;
raw current and child spend the same rough reservoir twice;
a non-leftmost LP basis is claimed to beat the leftmost optimum;
Y4-zero is inferred without checking all q/4^k prime-power terms;
ordinary feasibility is asserted from an inconsistent child detail packet;
response-space slack is treated as source provenance;
a root correction or port receives two owners.
```
