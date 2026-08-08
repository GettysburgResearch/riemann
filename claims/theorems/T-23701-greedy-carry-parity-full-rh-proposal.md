# T-23701 — Greedy carry–parity full RH proposal

Claim ID: `T-23701`  
Title: A canonical nonnegative carry minorant with polylogarithmic digital blocker debt proves the Riemann Hypothesis  
Status: **FULL PROPOSAL — ONE AGGREGATE DIGITAL BLOCKER THEOREM OPEN; RH NOT CLAIMED PROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`--`L-23703`; PR #236 `L-23008`--`L-23012`; PRs #202/#218 square-screw transfer  
Scope: replacement elementary-facing completion; no generic parity-comb inversion and no generic balanced Type-II norm theorem

## 1. Strategic reset

The current repository has reduced the dominant arithmetic family to one fixed
Mertens shell, and then to source-specific inversion of the positive parity
comb. That scalar is honest and minimal, but a direct coercive inverse theorem
for the parity comb is already RH-bearing.

The present proposal changes the direction of the inequality.

Instead of trying to invert the positive kernel on the signed Möbius source, it
constructs a nonnegative finite carry combination **below** the prime ramp. It
asks only that this positive combination retain the sharp leading entropy mass.
This avoids both rejected shortcuts:

```text
generic Farey operator norm      not used
generic parity-comb inverse      not used
rowwise absolute Möbius bound    not used
pointwise Carry Saturation        not required
finite numerical ladder -> RH    not used
```

## 2. Canonical finite object

For every integer `X`, form the carry matrix

\[
\beta_{nq}
=
\frac{\lfloor n/q\rfloor(q-1-(n\bmod q))}{n+1}
\]

and target

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

Run the exact backward minimum-ratio algorithm of `L-23701`. It produces one
canonical vector

\[
d_X(n)\ge0
\]

satisfying

\[
\boxed{
\sum_{n=q}^X d_X(n)\beta_{nq}\le w_X(q)
\quad(2\le q\le X).}
\tag{T-23701.1}
\]

This statement is unconditional and finite.

## 3. Positive prime-ramp factorization

The exact average-binomial identity is

\[
G_n
=
\frac1{n+1}\sum_{j=0}^n\log{n\choose j}
=
\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.
\tag{T-23701.2}
\]

Since `Lambda(q)>=0`, (T-23701.1) gives

\[
\boxed{
\sum_{q=p^k\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge
\sum_{n=2}^X d_X(n)G_n.}
\tag{T-23701.3}
\]

The entropy bound

\[
G_n\ge n/2-\log(n+1)-3
\]

therefore reduces the complete prime estimate to the two positive scalar masses

\[
\mathfrak M_X=\sum n d_X(n),
\qquad
\mathfrak L_X=\sum d_X(n)(\log(n+1)+3).
\tag{T-23701.4}
\]

## 4. Sole load-bearing theorem

The proposal's independent arithmetic theorem is:

> **DBT — Digital Blocker Theorem.** For the exact greedy vectors of
> `L-23701`, there are absolute constants `A,C` such that
> \[
> \boxed{
> \mathfrak M_X
> \ge8\sqrt X-C\log^A(2X),}
> \tag{T-23701.5}
> \]
> and
> \[
> \boxed{
> \mathfrak L_X
> \le C\log^A(2X).}
> \tag{T-23701.6}
> \]

DBT is weaker than full Carry Saturation. It permits off-diagonal blockers and
positive slack in every finite carry row. It asks only that their aggregate cost
be lower order than the sharp `sqrt(X)` mass.

## 5. Proposed proof of DBT

The proof programme is finite and quotient-layer based.

### 5.1 Blocker tree

At stage `n`, record the least blocking constraint `q_X(n)` and its quotient

\[
r_X(n)=\lfloor n/q_X(n)\rfloor.
\]

Rows with the same quotient are grouped before any estimate. On one quotient
cell the carry kernel is affine in the remainder, so the complete cell has an
exact two-endpoint representation.

### 5.2 Multi-base digit martingales

For each prime power `p^k`, `beta_(n,p^k)` is an average carry indicator. The
sum over `k` is the base-`p` digit loss in Kummer's theorem. Thus a complete
quotient cell is a conditional-variance packet, not an arbitrary positive row.

The binary member is linked exactly to the positive digit and parity kernels:

\[
S_2*\beta_2
=w_\infty-\sqrt2\tau_{\log2}w_\infty,
\]

\[
P_2*\beta_2
=w_\infty-rac3{\sqrt2}\tau_{\log2}w_\infty
+\tau_{2\log2}w_\infty.
\]

These identities supply the boundary ledger for the bit filtration. Analogous
base-`p` digit sums supply the other prime-power rows.

### 5.3 Quotient-layer amortization

The proposed local inequality charges the loss of a non-diagonal blocker to:

1. the decrease of a positive digit potential on the same quotient cell;
2. the complete reflected Selberg square of the unmatched parity component;
3. a residual carry problem at a strictly smaller endpoint.

After summing a complete quotient layer, all internal carry boundaries cancel.
Only the two layer endpoints and the lower-scale residual survive. The endpoint
terms are `O(polylog X)` by the digit-sum bounds, while the residuals telescope
geometrically.

The resulting global ledger is proposed to be

\[
8\sqrt X-\mathfrak M_X+\mathfrak L_X
\le
C\log^A(2X).
\tag{T-23701.7}
\]

Equation (T-23701.7) is exactly DBT. A proof must write every quotient cell,
blocker, digit boundary, and lower endpoint explicitly; the review protocol
forbids the phrase “standard carry cancellation.”

## 6. Completion of RH

Assume DBT. Then `L-23702` gives

\[
\sum_{q=p^k\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge4\sqrt X-O(\log^A X).
\tag{T-23701.8}
\]

The exact square-screw formula therefore has only polylogarithmic negative part.
The square-sampling/Landau transfer gives

\[
\Theta_\zeta=0,
\]

and hence

\[
\boxed{\mathrm{RH}.}
\tag{T-23701.9}
\]

Every implication after DBT is already finite or is an explicitly named
square-screw normalization dependency.

## 7. Connection to the parity-comb endgame

PR #236 proves that all fixed-ratio Mertens shells have the same exponential
obstruction. In particular, a proof of (T-23701.8) closes the dyadic shell and
therefore the `2/3` first Farey cell by the exact causal ratio transfer.

The carry theorem is not merely a new equivalent scalar. Its feasible vector is
nonnegative before the von Mangoldt weights are inserted. Consequently entropy
can be applied without recovering a bounded inverse of the parity comb.

Conversely, the binary blocker ledger is required to reproduce the finite
identities

\[
\sum_{m\le N}b_2(m)
\mathbf1_{\{\lfloor N/m\rfloor\text{ odd}\}}=0
\quad(N\ge4)
\]

and

\[
\sum_{m\le N}b_2(m)s_2(\lfloor N/m\rfloor)=-1
\quad(N\ge2).
\]

These are mandatory mutations preventing a hidden deletion of the Möbius core.

## 8. Why this may evade generic BTP

The balanced Type-II theorem attempts to upper-bound a signed quadratic packet.
DBT instead constructs a positive **lower certificate** for the prime ramp.

The distinction is load bearing:

- no signed packet is replaced by total variation;
- no critical local embedding is asserted for arbitrary vectors;
- no inverse operator is bounded on a space containing hypothetical zero modes;
- only the actual carry residual generated by `w_X` is followed;
- only aggregate entropy mass is required.

Thus a successful DBT proof would be a genuinely elementary/combinatorial
completion, even though the parity-comb identities explain why its blocker
ledger contains the same reciprocal-zeta difficulty.

## 9. Review order

1. `L-23701` — greedy feasibility and blockers;
2. `L-23702` — entropy and square-screw deduction;
3. `L-23703` — digital/parity mutation ledger;
4. the exact checker `X-23701`;
5. the quotient-layer amortization proposed in Section 5;
6. PR #236 `L-23008`--`L-23012`;
7. the square-screw normalization on PRs #202/#218.

## 10. Status boundary

```text
greedy nonnegative carry minorant       PROPOSED EXACT
prime-ramp factorization                 PROPOSED EXACT
entropy transfer                         PROPOSED EXACT
parity/digit dictionary                  PROPOSED EXACT
Digital Blocker Theorem DBT              OPEN
DBT => square-screw bound => RH          PROPOSED COMPLETE
Riemann Hypothesis                       NOT PROVED
```

This is a full, fail-closed proof proposal with one explicit finite aggregate
theorem. It is not a claim that DBT has already been established.