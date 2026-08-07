# M-23801 — Carry-envelope review and production protocol

Methodology ID: `M-23801`  
Title: Fail-closed review of the finite carry packing and reflected two-contact theorem  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238

## 1. Purpose

`T-23801` is intentionally split into:

1. exact finite algebra;
2. one proposed arithmetic/combinatorial hinge;
3. a complete conditional deduction to RH.

A reviewer should not spend time re-reviewing unrelated finite matrices or
operator normalizations before attacking the two-contact theorem.

## 2. Frozen dependencies

A proof packet must bind immutable source heads for:

```text
square-screw / Landau transfer        PR #202
safe-filter Hardy abscissa            PR #158, L-15151
high-order free-variable Euler        PR #158, L-15160
reflected Selberg identity            PR #226, L-9516
finite Mobius resolvent               PR #233, L-23201
first-cell Mertens decoder            PR #229
```

No status of an imported full proposal is inherited. Only the specifically
named source claims are used.

## 3. Exact finite certificate schema

For one endpoint `X`, a carry certificate contains:

```text
X
outward intervals for log(X/q)/sqrt(q)
exact beta matrix or a canonical reconstruction instruction
nonnegative rational packing d(n)
exact residual intervals rho(q)
outward lower intervals for G_n or the entropy lower h_n
claimed mass sum n d(n)
claimed logarithmic correction
canonical hashes of every input and output
```

The checker reconstructs `beta`, `B^T d`, the residual, and every mass. It
accepts only strict inequalities in the proof direction.

A solver may nominate `d`; the checker does not trust the solver or an LP basis.

## 4. Möbius-curvature replay

For every finite column `w`, independently reconstruct:

\[
 u(m)=\sum_{k\le X/m}\mu(k)w(mk),
\]

\[
 F(j)=\frac1{j-1}\sum_{m=j}^Xu(m),
\]

and check

\[
 d(j)=(j+1)\Delta^2P(j).
\]

The direct residual

\[
 w-B^Td
\]

must agree exactly with the divisor reconstruction

\[
 \rho(q)=\sum_{k\le X/q}
 \bigl[(qk-1)(F-P)(qk)-qk(F-P)(qk+1)\bigr].
\]

A mismatch rejects the packet before any asymptotic theorem is considered.

## 5. Symbolic terminal-face review

For packet orders `K=6` and `K=8`, export the complete same-scale obstacle
manifest:

```text
resolvent words in both reflected factors
all Mobius/binomial coefficients
first-crossing labels
frozen short products
active carry-obstacle constraints
null-moment eliminations
complexity destination
lower-scale destination
remaining free contact indices
first-cell mutation
```

For symbolic `K`, prove a structural dictionary theorem. Every terminal face
must be mapped to one maximal affine interval of the scalar convex profile and
therefore to at most two free contacts.

The reviewer should actively search for:

- nested active divisor constraints producing three contacts;
- transition rows that are not polynomial-null;
- a balanced packet silently routed through `BTP(K)`;
- reflected cross terms not consumed by the Hermitian square;
- a first-cell coefficient with the wrong Möbius sign.

## 6. Mutation tests

At minimum, the exact consumer must reject:

1. a negative packing coefficient;
2. one violated ramp coordinate;
3. a changed `beta_(nq)` floor or remainder;
4. a missing Möbius multiple in the residual reconstruction;
5. a false mass telescope;
6. a product-dilation/factor-ratio substitution;
7. a terminal face with three declared free contacts;
8. a lower-scale destination above `X^(1-delta)e^(O_K(1))`;
9. a first-cell mutation that does not recover the fixed-ratio Mertens row;
10. inference from finitely many orders to the all-order limit.

## 7. Proof-status discipline

The following classifications must remain distinct:

```text
exact finite carry algebra                    exact/proposed
synthetic checker replay                      exact finite control
K=6 or K=8 face enumeration                  finite evidence only
symbolic two-contact theorem                  RH-bearing hinge
T-23801 after that theorem                    full proof
```

No finite positive ladder, numerical LP trend, or empirical positivity of the
exact inverse proves RH.

## 8. Preferred production order

1. Audit `D-23801` algebra by hand and checker.
2. Emit actual directed carry packings through moderate `X`.
3. Compare greedy, exact inverse, and entropy-optimal packings.
4. Export the complete `K=6` packet-to-obstacle dictionary.
5. Verify the first-cell mutation.
6. Attempt to construct a three-contact counterface.
7. Only after the symbolic theorem survives, promote the RH conclusion.
