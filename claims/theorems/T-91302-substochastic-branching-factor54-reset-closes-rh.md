# T-91302 — A substochastic branching factor-54 reset closes RH

Claim ID: `T-91302`  
Status: **PROVED CONDITIONAL CONSUMER / EXACT BRANCHING GENERALIZATION**  
Created: 2026-08-12  
Depends on: PR #352 `L-90023/L-90029`, `T-91101`  
RH status: **unproved absent the reset hypothesis**

## 1. Why one contracted child is unnecessary

The least-prime rough Euler decomposition naturally produces several contracted
children. Requiring them to be compressed into one endpoint before score
accounting is stronger than necessary.

It is enough that the inherited score-loss coefficients form a subprobability
vector.

## 2. Branching reset hypothesis

Fix constants

\[
 0<c<1,
 \qquad C_0,C_1>0,
 \qquad A\ge0.
\]

For every sufficiently large endpoint `X`, suppose there are:

1. a nonnegative outer carry packing;
2. finitely or countably many child endpoints `Y_b` satisfying
   \[
   Y_b\le cX+C_0;
   \tag{T-91302.1}
   \]
3. nonnegative score-transfer weights `theta_b` satisfying
   \[
   \boxed{
   \sum_b\theta_b\le1;
   }
   \tag{T-91302.2}
   \]
4. a positive, capacity-faithful lift which combines arbitrary feasible child
   packings into one feasible parent packing;
5. the score-loss recurrence
   \[
   \boxed{
   \mathfrak L_X
   \le E_X+\sum_b\theta_b\mathfrak L_{Y_b};
   }
   \tag{T-91302.3}
   \]
6. the local debt bound
   \[
   E_X\le C_1(1+\log\log(3X))^A.
   \tag{T-91302.4}
   \]

A finite certified base is also assumed.

The sums are understood by monotone convergence when the branch set is
countable.

## 3. Tree expansion

Iterate the reset. A node `v` at depth `j` carries endpoint `X_v` and path weight

\[
 \Theta_v=\prod_{e\in[\varnothing,v]}\theta_e.
\]

The subprobability condition implies, by induction,

\[
 \boxed{
 
 \sum_{|v|=j}\Theta_v\le1
 }
\tag{T-91302.5}

for every depth `j`.

Every endpoint at depth `j` satisfies

\[
 X_v\le c^jX+C_0(1+c+\cdots+c^{j-1}).
\tag{T-91302.6}

After enlarging the finite base, the tree therefore terminates by depth

\[
 \boxed{
 J(X)=O(\log X/|\log c|).
 }
\tag{T-91302.7}

## 4. Total debt

Expanding (T-91302.3) through the tree gives

\[
 \mathfrak L_X
 \le C_{\rm base}
 +\sum_{j<J(X)}
  \sum_{|v|=j}\Theta_v E_{X_v}.
\tag{T-91302.8}

By (T-91302.4)--(T-91302.5),

\[
 \sum_{|v|=j}\Theta_v E_{X_v}
 \le C_1(1+\log\log(3X))^A.
\]

Hence

\[
 \boxed{
 \mathfrak L_X
 =O\!\left(
   \log X(1+\log\log X)^A
  \right)
 =o(\log^2X).
 }
\tag{T-91302.9
 }

PR #352 then gives

\[
 \boxed{
 \text{substochastic branching reset}
 \Longrightarrow\mathrm{RH}.
 }
\tag{T-91302.10
 }

## 5. Compatibility with rough-prime routing

For the factor-54 programme one may take `c=c_0`. The exact one-prime identity
`L-91330` places every canonical child at endpoint `X/p`, hence at most `X/67`,
and routes all other terms into positive slack/frontier channels.

The four-state mass telescope of `L-91327` and unique least-prime labels of
`L-91317` nominate the required subprobability weights. The affine score theorem
`L-91318`, local parity projection, butterfly lift and B-spline quantization are
all score-favorable.

Thus the remaining production theorem no longer asks for one contracted state.
It asks for the exact source/target partition proving (T-91302.2)--(T-91302.3)
for the least-prime tree.

## 6. Scope

This theorem is a consumer, not the missing producer. It does not infer
subprobability from positivity of one-prime matrices, nor from scalar SHARP
preservation.

```text
branching score telescope                         EXACT
subprobability mass at every depth                EXACT
factor-54 tree depth                              EXACT
polylog-log local debt -> o(log^2 X)              EXACT
branching reset -> RH                             COMPLETE CONDITIONAL
rough source/target subprobability partition      OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```
