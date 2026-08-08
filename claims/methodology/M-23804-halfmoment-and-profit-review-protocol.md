# M-23804 — Review protocol for the binary–ternary half-moment and profit coordinates

Claim ID: `M-23804`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238

## Frozen review order

1. `L-23810-carry-flow-divergence-and-mobius-inversion.md`
2. `L-23811-explicit-binary-ternary-signed-carry-flow.md`
3. `L-23812-binary-ternary-half-moment-collapse.md`
4. `R-23803-btf-is-not-yet-an-unconditional-closure.md`
5. `L-23813-profit-debt-fragmentation-criterion.md`
6. `T-23803-explicit-binary-ternary-flow-full-rh-proposal.md`
7. the continuation report

## Load-bearing checks

### A. Divergence sign convention

Verify directly that the declared recurrence gives

\[
 r(n)=A(n)-\text{incoming}(n).
\]

A reversed sign invalidates every moment identity.

### B. Concave moment

Reconstruct

\[
 -\sum_mr(m)m^\theta
 =\sum_nA(n)\Delta_\theta(n)
\]

and verify the exact child rounding in both splits.  Check separately that the
`theta=1/2` defect is bounded above and below by fixed positive multiples of
`sqrt(n)`.

### C. Positivity versus rate

Do not combine these two assertions:

```text
A_X(n)>=0 for every n and cofinally in X
mathfrak H_X=-sum r_X(n)sqrt(n)=X^o(1)
```

Both are required by the current half-moment route.  A finite positivity scan
proves neither cofinal statement.

### D. Target-coordinate inversion

Verify

\[
 h_\theta=\mu*(m^\theta-(m-1)^\theta)
\]

and

\[
 m^\theta=\sum_{q\le m}h_\theta(q)\lfloor m/q\rfloor.
\]

The row `q=1` vanishes only because the target convention enforces the exact
first-moment closure.

### E. Profit potential

Check

\[
 F(n)=\log(n!)-\mathcal D(n)
\]

and

\[
 F(n)-F(j)-F(n-j)
 =\log\binom nj-\sum_q\chi_{n,j}(q).
\]

Then reconstruct the exact global identity

\[
 \sum d\pi=\mathcal P(X)-\mathcal C(X).
\]

### F. Finite-exception gate

For a fixed bad parent `n`, every split satisfies `chi_(n,j)(n)=1`, hence its
coefficient mass is at most `w_X(n)`.  This is the sole reason a fixed finite
bad-parent set costs only `O(log X)`.

### G. Firewall

Any claimed generic theorem saying that exact flow feasibility automatically
produces subpolynomial negative debt must be rejected.  The dual potential
`-F` shows that the debt program directly sees the prime-ramp deficit.

## Required status boundary

```text
finite recurrence identities               verify independently
producer positivity                         separate theorem
half-moment rate                            separate theorem
profit/debt finite-exception construction   alternative separate theorem
conditional RH deduction                    retain if transfers pass
accepted RH proof                           NO until one full hinge is proved
```
