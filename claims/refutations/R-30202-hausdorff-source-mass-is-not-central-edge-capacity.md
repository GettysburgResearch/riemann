# R-30202 — Hausdorff source mass is not central-edge capacity

Claim ID: `R-30202`  
Title: The canonical positive flow representing a decreasing divisor source places the first difference, not the source value, on its root central edge  
Status: **EXACT SCOPE CORRECTION / COUNTEREXAMPLE TO AUTOMATIC CAPACITY BINDING**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
Dependencies: central trees of PR #272; `L-30202`  
Scope: the inference “Hausdorff coefficient `A_k` supplies central capacity `A_k`”

## 1. Positive tree layer cake for a divisor source

Let

\[
 c_2\ge c_3\ge\cdots\ge c_N\ge0,
 \qquad c_{N+1}=0,
\]

and consider the formal divisor source

\[
 \sigma=\sum_{n=2}^Nc_n e_n.
\tag{R-30202.1}

Its carry image is

\[
 L_q(\sigma)=\sum_{m\ge1}c_{mq}.
\tag{R-30202.2}

Let `T_n` be the complete central tree rooted at `n`, so its carry load is
`floor(n/q)`. Put

\[
 d_n=c_n-c_{n+1}\ge0
\]

and

\[
\boxed{
 \mathcal T(c)=\sum_{n=2}^Nd_nT_n.
}
\tag{R-30202.3}

Finite summation by parts gives

\[
\begin{aligned}
 L_q(\mathcal T(c))
 &=\sum_{n=2}^N(c_n-c_{n+1})\left\lfloor\frac nq\right\rfloor\\
 &=\sum_{m\ge1}c_{mq}.
\end{aligned}
\tag{R-30202.4}

Thus `mathcal T(c)` is an exact coefficientwise nonnegative flow realization of
the complete decreasing divisor source.

## 2. The root capacity is a first difference

The root central edge of `T_n` occurs with coefficient one. Therefore the
coefficient of the root central edge of size `n` in (R-30202.3) is

\[
\boxed{d_n=c_n-c_{n+1},}
\tag{R-30202.5}

not `c_n`.

After dyadic lifting, the available coefficient on `[2n,n]` remains the lifted
first difference, with the declared normalization factor. A source value and a
central-edge capacity cannot be identified without an additional cycle
construction.

## 3. Exact eta mismatch

For the basic eta source

\[
 c_n=\frac1n,
\]

one has at the even node `2k`

\[
 A_k=c_{2k}=\frac1{2k},
 \qquad
 B_k=c_{2k+1}=\frac1{2k+1}.
\]

The canonical positive-tree capacity at the corresponding root is

\[
\boxed{
 d_{2k}=A_k-B_k
 =\frac1{2k(2k+1)}.
}
\tag{R-30202.6}

The relative sibling replacement requires central capacity `B_k`. Their ratio is

\[
\boxed{
 \frac{B_k}{d_{2k}}=2k.
}
\tag{R-30202.7}

Already at `k=1`, the canonical source flow supplies capacity `1/6`, while the
switch requires `1/3`. The discrepancy grows linearly with `k`.

Consequently the inequalities

\[
 A_k\ge B_k
\]

and Hausdorff monotonicity do **not** prove that the required central edge is
available. They prove only that the residual source coefficient `A_k-B_k` is
nonnegative.

## 4. Capacity debt is not logarithmic objective cost

If the missing amount is paid by a negative central edge at parent `4k`, its
Cycle Debt weight is proportional to the carry capacity of that edge, which is
of square-root scale. In contrast, the eta objective cost

\[
 B_k\log\frac{2k+1}{2k}
\]

is of order `k^-2`. No generic norm comparison turns the latter into the former.
An exact cycle-adjusted capacity construction is mandatory.

## 5. What remains possible

This result does not prove that every positive realization lacks the needed
central capacity. Pascal cycles can change edge coefficients while preserving
divergence. The corrected question is precisely the finite optimization problem
of `L-30203`:

> Can one choose a cycle-equivalent nonnegative flow with the declared central
> capacities at only polylogarithmic weighted defect?

That theorem may still hold and would complete the source-bound eta–Pascal
proposal.

## 6. Verdict boundary

```text
Hausdorff residual positivity                     VERIFIED
positive central-tree source realization          VERIFIED
root central capacity equals source value A_k     FALSE
root central capacity equals A_k-B_k canonically   VERIFIED
alternative cycle-adjusted SFC construction       UNPROVEN
PR #301 as a completed RH proof                    UNPROVEN
Riemann Hypothesis                                 UNPROVEN
```
