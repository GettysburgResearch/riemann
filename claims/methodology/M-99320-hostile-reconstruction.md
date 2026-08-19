# M-99320 — Hostile reconstruction protocol

Review in this order:

1. Expand \(Q_Y(j)\) directly and verify \(A_j,-B_j,C_j\).
2. Integrate both elementary target kernels term by term.
3. Check the first activation cell, both exact coefficient telescopes, the
   first complete cell, and the increment \(3N+2\).
4. At fixed \(t\), verify that the compact source bracket is exactly the
   target Hall problem at parameter \(x/t\), including every activation cutoff.
5. Verify the causal target difference separately on \(t\le Y/p\) and
   \(t>Y/p\).
6. Confirm that one random key, not one per row, creates all children.
7. Reconstruct the signed calibration identity before applying its bound.
8. Rebuild the fixed-row Mellin transform and large-\(j\) numerator asymptotic.
9. Treat the target Hall/root registry as the first imported arithmetic gate.
10. Do not represent publication as acceptance of RH.

Immediate falsifiers:

```text
one t,j with eta_j(t)<=0;
one missing activation convention;
one Hall coefficient depending on j;
one causal row coefficient different from its target coefficient;
one calibration term silently inserted into positive source;
one recursive coefficient outside the alpha children;
one off-line zero canceled by every P_j;
one claim that the replay proves the frozen Hall theorem or RH.
```
