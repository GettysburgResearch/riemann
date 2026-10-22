# R-32401 — A nonnegative decreasing carry target need not lie in the balanced carry cone

Claim ID: `R-32401`  
Title: Generic monotonicity is insufficient for quarter-balanced carry feasibility  
Status: **EXACT FINITE REFUTATION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Scope: generic carry targets only; the critical target `q^(-1/2) log(X/q)` is not refuted

## 1. The false surrogate

Several surviving carry proposals use special regularity of the critical target

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

A tempting shortcut is to replace that arithmetic source by the generic statement

> every nonnegative decreasing carry-column target admits a nonnegative quarter-balanced split flow.

That statement is false.

Fix endpoint `X=50`. Let

\[
w(q)=\mathbf 1_{2\le q\le23}.
\tag{R-32401.1}
\]

This target is nonnegative and decreasing.

For a split `n=j+(n-j)`, write

\[
\chi_{n,j}(q)=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor.
\]

Use every quarter-balanced split

\[
2\le n\le50,
\qquad
\lceil n/4\rceil\le j\le\lfloor n/2\rfloor.
\tag{R-32401.2}
\]

## 2. Exact dual separator

Define the integer column vector `v` by

```text
v_4  =  1     v_5  = -1     v_6  =  1     v_7  =  2
v_8  = -2     v_9  = -1     v_10 =  3     v_11 =  1
v_12 = -3     v_13 =  1
v_17 =  2     v_18 =  1     v_19 =  4     v_20 =  5
v_21 = -5     v_22 = -5     v_23 = -5
v_q  =  5     for 24 <= q <= 50
v_q  =  0     otherwise.
```

The exact finite certificate is

\[
\boxed{
\sum_{q=2}^{50}v_q\chi_{n,j}(q)\ge0
}
\tag{R-32401.3}
\]

for every one of the `337` quarter-balanced splits in (R-32401.2). Of these, `30` have equality and `307` have strict positive value.

On the target, however,

\[
\boxed{
\sum_{q=2}^{50}v_qw(q)
=\sum_{q=2}^{23}v_q=-1.
}
\tag{R-32401.4}
\]

If a nonnegative balanced flow `d_(n,j)` realized `w`, then

\[
\begin{aligned}
-1
&=\sum_qv_qw(q)\\
&=\sum_{n,j}d_{n,j}\sum_qv_q\chi_{n,j}(q)\\
&\ge0,
\end{aligned}
\]

a contradiction.

Therefore

\[
\boxed{
w\notin\operatorname{cone}\{\chi_{n,j}:\text{quarter-balanced }(n,j)\}.}
\tag{R-32401.5}
\]

## 3. Consequence

A proof of the critical carry theorem cannot follow from any theorem whose only source hypotheses are

```text
nonnegative;
decreasing;
convex / bounded variation after a source-independent finite smoothing.
```

The arithmetic source must be used more specifically. This is consistent with the already known failures of fixed Abel positivity and with the exact Cycle-Debt duality of PR #272.

The counterexample does **not** contradict:

- feasibility of the actual critical target;
- the positive square-root hinge programme;
- a source-specific Pascal-cycle construction;
- Cycle Debt with subpower negative capacity.

## 4. Exact replay

`experiments/X-32401-extra-high-crosschecks/verify.py` recomputes all `337` inequalities using integer arithmetic and checks the target pairing `-1`.

## 5. Proof boundary

Proved exactly: the generic monotone-target balanced-cone statement is false.

Open: the source-specific critical carry theorem and RH.