# T-19820 hostile review handoff — corrected factor-67 native slack

## Status

```text
R-19882  continuum/native normalization firewall       PROPOSED EXACT
L-19882  exact native slack cocycle                     PROPOSED EXACT
L-19885  Y4 sparsity and weighted root-error bounds     PROPOSED EXACT
T-19820  corrected factor-67 SONTR/NRCT composition     CANDIDATE ON FROZEN INPUTS
RH                                                       UNPROVED
```

This packet is not labelled a full proposal.

## Frozen factor-67 head

```text
PR #473  13ad1fdbf06edc931dc0c524327b701c5c8f86a3
```

## Reconstruction order

1. Reconstruct the exact formula
   \[
   Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
   \]
2. Prove the support classification:
   powers of two; `4^v p^a` for odd primes; zero otherwise.
3. Reconstruct the elementary series bounds
   \[
   \sum_qY_4(q)q^{-3/2}<11,
   \qquad
   \sum_{q\le X}Y_4(q)/q
   \le3+2L+2L^2.
   \]
4. Apply them to `L-91691.8--.9`; check mismatch cost `<392` and collar cost
   `o(1)`.
5. Check the safety estimate against the exact native benchmark, not the
   continuum target:
   \[
   (1-\sigma_K)J_\Lambda(X)=o(1).
   \]
6. Verify that the top omitted packet and finite base/current-port corrections
   are positive physical packets with uniformly bounded literal entropy.
7. Reconstruct the common-parent equality
   \[
   \Omega_X
   =\Xi(c_X)+r_X+\sum_b\alpha_bU_b\Omega_{Y_b}.
   \]
8. Check that no Hall, rough-owner, correction or port label is duplicated.
9. Apply `L-19882` and verify the exact scalar recurrence
   \[
   \Delta_X=\delta_X+\sum_b\alpha_b\Delta_{Y_b}.
   \]
10. Reconstruct the endpoint consumer `T-91313` from
    `Delta_X=O(1)=o(log^2 X)`.

## Mandatory rejection tests

Reject the corrected composition if:

```text
a Y4-positive column is omitted from the root-cost sum;
the mismatch is bounded in ordinary rather than detail coordinates;
the top packet has signed detail or signed endpoint weights;
the base/current-port score grows with X;
the common-parent identity reserves a child after its source was spent;
the same-index map changes q;
a normalized target deficit is again converted to 4 sqrt(X)-H;
the endpoint consumer requires the continuum deficit rather than J_Lambda-H.
```

## Replay

```bash
cd experiments/X-19885-y4-factor67-root-cost
python3 verify.py certificates/control.json --output /tmp/x19885.json
cmp /tmp/x19885.json results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_Y4_SPARSE_FACTOR67_ROOT_COST_PACKET
```

Retained proof-object digest:

```text
b9b061b50eb11901d1f4f76c596117cf30e4a932029c5388a2d5b6dc9d7b8b7c
```
