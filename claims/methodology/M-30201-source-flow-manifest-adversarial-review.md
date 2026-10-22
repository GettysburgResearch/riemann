# M-30201 — Adversarial review of the eta source-flow manifest

Methodology ID: `M-30201`  
Status: **FAIL-CLOSED REVIEW PROTOCOL**  
Target: `T-30201` and any attempted repair of PR #301

## 1. Freeze

Record the exact reviewed commits for:

```text
PR #301 eta–Pascal proposal;
PR #272 DCD/Cycle Debt normal form;
PR #286 finite cutoff boundary ledger;
PR #294 eta source and Pascal identities;
this source-flow repair branch.
```

Do not review a moving head.

## 2. Reconstruct the local algebra

Without following the prose derivation, verify for every tested `k,q`:

\[
\chi_{4k,2k-1}(q)-\chi_{4k,2k}(q)
=\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}.
\]

Then separately compute:

```text
formal paired divisor-source load;
relative new-minus-old edge load;
standalone load of (A-B)C+B S.
```

The last two must never be conflated. The `k=1`, `q=2,3,4` table of
`R-30201` is mandatory.

## 3. Reconstruct the absolute source flow

Build the central trees `T_n`, adjacent commutators

\[
\mathcal E_h=T_{h+1}-T_h,
\]

and verify

\[
L_q(\mathcal E_h)=\mathbf1_{q\mid h+1}.
\]

For every paired source check

\[
A e_{2k}-B e_{2k+1}
\longleftrightarrow
A\mathcal E_{2k-1}-B\mathcal E_{2k}.
\]

A reviewer should reject any proof that replaces the signed right side directly
by `(A-B)C+B S` without an incoming-flow equality.

## 4. Reconstruct the Hausdorff residual

Derive the positive double-Laplace representation of `L-30202`. Verify:

```text
actual shifted-even argument 2kq-1;
actual odd argument (2k+1)q;
weights 1/(2k), 1/(2k+1);
all finite-difference and Euler-remainder factors;
cutoff-tail start index.
```

The residual must be shown to be a positive measure moment, not only checked at
finitely many differences.

## 5. Source mass versus edge capacity

For a decreasing source `c_n`, independently prove

\[
\sum_n(c_n-c_{n+1})\lfloor n/q\rfloor
=\sum_m c_{mq}.
\]

Record the actual root central coefficient `c_n-c_(n+1)`. For `c_n=1/n`, check

\[
\frac{B_k}{A_k-B_k}=2k.
\]

This mutation rejects any source-to-edge binding that spends the cumulative
source value `A_k` instead of an emitted edge coefficient.

## 6. Production `SFC` certificate

For every source destination, the proof object must emit:

```text
exact A_k and B_k;
exact incoming flow edge C_k and its coefficient;
one-use token for that coefficient;
new central and sibling edges;
relative carry-vector equality;
next-generation residual source;
all collar atoms;
capacity-debt total.
```

A source label, an aggregate mass, or a divisor atom is not an incoming edge.

## 7. Dual review

Construct the residual divergence `r^cap=r-Ba` of `L-30203`. Either:

1. emit a nonnegative completion, or
2. emit a balanced-superadditive potential violating the Farkas inequality.

The primal and dual should be generated independently. Any numerical interval
must be outward rounded and accompanied by exact source hashes.

Mandatory dual mutations include:

```text
logarithmic/von-Mangoldt ray;
fixed-ratio Möbius shell;
same-sign Möbius cube;
small k=1 eta pair;
cutoff odd-starts-one-earlier case.
```

## 8. Recurrence audit

Only after `SFC` is verified may the reviewer accept

\[
D_{a+1}\le\theta D_a+C A_a+\mathfrak C_a+P_M.
\]

Check that:

```text
mathfrak C_a is measured in capacity units;
no deficit is paid only in objective units;
residual sources never feed analytic bulk;
O(log X) generations include every collar;
the final bounded endpoint is explicit.
```

## 9. Automatic rejection conditions

Reject the proposed proof upon any one of:

1. standalone use of the relative edge replacement;
2. source mass identified with central capacity;
3. duplicated central capacity;
4. omitted `q=4k` column;
5. unmatched odd cutoff source;
6. residual sequence not source typed at the next generation;
7. a missing Pascal cycle;
8. capacity/objective norm substitution;
9. finite reconnaissance promoted to `SFC`;
10. missing prime-ramp or Landau normalization.

## 10. Classification grid

Classify separately:

```text
local carry algebra;
absolute source flow;
Hausdorff residual theorem;
central-capacity manifest;
collar ledger;
Farkas/cycle estimate;
triangular recurrence;
Cycle Debt consumer;
RH conclusion.
```

Use `FALSE` only for an exact contradicted claim. A missing manifest or
quantitative estimate is `UNPROVEN`.