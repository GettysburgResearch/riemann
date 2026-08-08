# M-29802 — Review protocol for the amortized source-to-Cycle-Debt closure

Claim ID: `M-29802`  
Title: Reconstruct the common Hausdorff tail, unmatched collar, nonnegative Pascal flow, and DCD metric before accepting the RH composition  
Status: **FAIL-CLOSED ADVERSARIAL REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29801/L-29806/L-29807`, `R-29802`, `T-29802`

## 1. Frozen inputs

```text
PR #272  5cb703bcc1593c4ce8f1f2d8d3840dc61d573dba
PR #286  6bba6161887b6913f4f50c1b90ee46a0fd84c339
PR #294  839900f2738c6a3da67f4754b462e953bc1034ba
PR #301  head at review start
```

## 2. Review order

1. `L-29801` — positive stopped-power resolution;
2. PR #286 `L-28401/L-28402` — exact analytic and cutoff ledger;
3. `L-29806` — Hausdorff monotonicity and amortized source budget;
4. `R-29802` — withdrawn arbitrary-label shortcut;
5. PR #294 `L-28301/L-28302` — exact eta/Pascal switch;
6. `L-29807` — nonnegative flow and DCD metric bridge;
7. PR #272 `L-27207/L-27208/T-27203`;
8. `T-29802` — complete composition;
9. exact checkers and corrected report.

## 3. Required row manifest

For every stopped endpoint `Y`, exponent `s`, source destination, quotient `q`, eta index `k`, Euler order `m`, and shifted/unshifted leg, emit:

```text
raw argument;
first omitted index;
Taylor correction order;
finite-difference coefficient;
exact remainder coefficient;
common-tail key;
unmatched-collar key;
V_even and V_odd;
central amount M;
sibling amount T;
central residual M-T;
Pascal edge;
capacity weight;
objective cost;
next endpoint.
```

All rows sharing a common destination must be recombined before testing `V_even>=V_odd` or capacity.

## 4. Binary acceptance tests

For the common tail verify exactly:

```text
V_even >= V_odd >=0;
T=V_odd/(2k+1) <= M=V_even/(2k);
carry(sibling)-carry(central)=e_(2k)-e_(2k+1);
central coefficient M-T >=0;
sibling coefficient T >=0;
negative capacity debt =0;
objective loss =T log((2k+1)/(2k)).
```

For unmatched terms verify:

```text
row appears in the declared collar;
collar flow reproduces its carry columns;
collar capacity is included in the polylog bound.
```

For the global recurrence verify:

```text
analytic injection is measured in the same source units;
no boundary source returns to current analytic bulk;
all Pascal costs are counted once;
DCD excess is bounded by collar debt only.
```

## 5. Automatic rejection mutations

Reject on any:

1. pairing before common-destination recombination;
2. omitted first odd or even term;
3. reversed argument order;
4. negative finite-difference coefficient;
5. exact Euler remainder treated as zero;
6. switch amount larger than central amount;
7. unbalanced sibling edge;
8. negative edge hidden inside a signed cycle;
9. objective cost substituted for capacity debt or vice versa;
10. collar capacity omitted;
11. bottom tree omitted;
12. wrong factor `2^-1/2` or capacity factor `1/2`;
13. boundary-to-current-bulk feedback;
14. finite test promoted to the cofinal statement.

## 6. Verdict boundary

The finite rational regressions are normalization checks. Acceptance requires the complete symbolic source manifest and independent replay of the PR #272 consumer.
