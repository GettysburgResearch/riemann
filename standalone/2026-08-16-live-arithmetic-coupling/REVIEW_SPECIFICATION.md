# Review specification

The first review target is the source-to-row compiler, not the endpoint theorem.

## Mandatory reconstruction

1. Verify PR #509 remains at `e01daee9cdfea35d2a7d2591f1df6c8080084119`.
2. Reproduce the exact negative interval for the PR #503 witness.
3. Confirm the bulk generator list contains only terminal `p_s` packets.
4. Confirm no bulk occurrence has a rough first owner.
5. Reconstruct the native hybrid identity and its signed defect.
6. Reconstruct the anchored source tree from literal native coefficients.
7. Verify every path coefficient and least rough owner.
8. Verify the complete AVLT/typed leaf from PR #508.
9. Check the same `u_e` in target, score and all rows.
10. Check all incidence marginals and physical placements.
11. Check the sole quantizer is label-blind and block diagonal.
12. Check `q` and `4q` on the same total row before detail.
13. Check every `q>=2`, native `Y_4`, and the upper-bound endpoint orientation.

## Immediate failure

Reject on the first:

```text
infinitesimal causal generator;
rough owner on a bulk p_s;
synthetic anchored leaf;
unproved path coefficient;
coordinate-dependent leaf coefficient;
duplicate source owner or placement;
branchwise detail;
omitted small q;
signed comparison in positive source;
Y4 cost >=60989.
```
