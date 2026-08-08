# M-30601 — Terminal-source fiber review protocol

Claim ID: `M-30601`  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Issue: #306

A terminal boundary-to-flow certificate is admissible only if it exports:

1. every arithmetic fiber `q_0` and quotient index `k` separately;
2. the physical divisor nodes `2kq_0,(2k+1)q_0`;
3. the exact flow dilation and its capacity scaling;
4. every carry-column replay, including columns dividing `q_0`;
5. common-destination recombination before any atomic or negative norm;
6. a complete top-band profile, not one atom at a time;
7. every lower-band leakage row;
8. all Pascal-cycle coordinates used to alter that leakage;
9. the final Cycle-Debt normalization of PR #272.

Automatic rejection applies if:

- `q_0` occurs only in a coefficient;
- the flow node remains `2k` or `2k+1` after physical dilation;
- a `q_0^(-1/2)` capacity factor is retained without proof;
- a stopped-power boundary is assigned polylog atomic norm contrary to `R-30602`;
- central top-band steps are iterated without the `R-30603` mutation;
- reviewers are asked to infer an omitted source map or recurrence.

The exact regression `X-30601` is a required mutation suite, not evidence for RH.
