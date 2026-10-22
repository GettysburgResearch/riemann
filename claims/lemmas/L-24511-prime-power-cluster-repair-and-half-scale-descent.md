# L-24511 — Prime-power cluster repair and half-scale descent

Claim ID: `L-24511`  
Status: `IMPORTED, REPROVED, AND SHARPENED — exact finite algebra`  
Scope: local signed adjacent-flow mechanism  
Issue: #245  
Source connection: PR #254, `L-25301`  
Depends on: `L-24502`, `L-24508`

For a flow supported at an integer `j`, the change in the `d`-constraint is

\[
\mathcal A(d,j)
=
\mathbf1_{d\mid j+1}
-2\mathbf1_{d\mid j}
+\mathbf1_{d\mid j-1}.
\tag{L-24511.1}
\]

Take `j=q`, where `q` is a prime power.

## 1. Sign geometry of one direct repair

The diagonal coefficient is

\[
\mathcal A(q,q)=-2.
\tag{L-24511.2}
\]

Every positive child `d` satisfies

\[
d\mid q-1
\quad\text{or}\quad
d\mid q+1.
\tag{L-24511.3}
\]

If `d` is not equal to `q-1` or `q+1`, then

\[
\boxed{d\le\frac{q+1}{2}.}
\tag{L-24511.4}
\]

Indeed, a proper divisor of a positive integer `N` is at most `N/2`.

Thus the only positive children above half scale are the neighboring integers `q-1` and `q+1`, when they are themselves prime powers.

Proper prime-power divisors of `q` occur with coefficient `-2` and are favorable.

## 2. Consecutive-prime-power clusters are uniformly short

A same-scale cluster is a maximal interval of consecutive integers, every member of which is a prime power.

Every four consecutive integers beginning above `2` contain an integer congruent to `2 mod 4` and greater than `2`. Such an integer has at least the two distinct prime divisors `2` and an odd prime, so it is not a prime power.

Therefore every same-scale cluster has length at most three, except

\[
\boxed{\{2,3,4,5\}.}
\tag{L-24511.5}
\]

## 3. Ordinary cluster solve

For a cluster of length `r<=3` above `5`, the same-scale negative correction matrix is

\[
A_r=2I-\operatorname{Adj}(P_r).
\tag{L-24511.6}
\]

Its inverse is entrywise nonnegative. Explicitly,

\[
A_1^{-1}=(1/2),
\]

\[
A_2^{-1}=\frac13
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\]

and

\[
A_3^{-1}=\frac14
\begin{pmatrix}
3&2&1\\
2&4&2\\
1&2&3
\end{pmatrix}.
\tag{L-24511.7}
\]

Hence, for any nonnegative current defect vector `e_C` on the cluster,

\[
F_C=A_r^{-1}e_C\ge0
\]

removes the complete same-scale defect exactly.

## 4. Exceptional cluster

In the ordered basis `(2,3,4,5)`, the exact same-scale matrix is

\[
A_{\rm exc}=
\begin{pmatrix}
2&-2&2&-2\\
-1&2&-1&-1\\
0&-1&2&-1\\
0&0&-1&2
\end{pmatrix}.
\tag{L-24511.8}
\]

Its inverse is

\[
\boxed{
A_{\rm exc}^{-1}=
\begin{pmatrix}
3/2&2&1&3\\
3/2&3&2&4\\
1&2&2&3\\
1/2&1&1&2
\end{pmatrix}\ge0.}
\tag{L-24511.9}
\]

Thus the exceptional same-scale block is also an inverse-positive M-matrix in the required orientation.

## 5. Exact descent theorem

Process one cluster jointly by the preceding inverse. Then:

1. every current positive defect on the cluster is removed;
2. no new positive defect remains in that cluster;
3. every positive child outside the cluster is a prime-power divisor of `q-1` or `q+1` for some cluster member `q`;
4. every such child obeys

\[
\boxed{d\le\frac{q+1}{2}.}
\tag{L-24511.10}
\]

Consequently the direct prime-power repair has a genuine factor-two scale descent after one uniformly bounded same-scale solve.

## 6. Sharpened proof boundary

PR #254 retained coefficientwise nonnegativity of the corrected carry vector as an obligation. `L-24508` proves that this is unnecessary for the direct prime-ramp consumer. The local theorem here therefore requires only constraint repair; no sign condition on the induced `b` vector is imposed.

What remains open is global: repeated cluster descent must exploit the negative slack as well as the positive defect and must have subpower exact objective cost. A positive-part recursion alone can accumulate square-root mass at small prime powers and is not a proof.

## Review boundary

All matrices and the factor-two descent are exact finite algebra. This lemma does not prove a global transport bound or RH.
