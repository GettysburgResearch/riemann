# L-25805 — Prime-anchor carry cluster descent

Claim ID: `L-25805`  
Title: The marked prime-power anchor admits the same bounded same-scale cluster solve and factor-two child descent as the signed carry constraint flow  
Status: **PROPOSED SOURCE ADAPTER; FINITE CLUSTER ALGEBRA EXACT, GLOBAL BINDING OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: `L-25801`, `L-25804`; PR #254 `L-25301`  
Scope: candidate producer for a `PADT(K)` certificate

## 1. Marked prime-power coordinate

The positive anchor of `L-25801` satisfies

\[
\boxed{
g_{K-1}=\Lambda*d_{K-1}.}
\tag{L-25805.1}
\]

Thus every anchor representation can be written as

\[
b=q\,c_1\cdots c_{K-1},
\qquad q=p^a,
\tag{L-25805.2}
\]

with coefficient `Lambda(q)` and unit coefficients on the remaining divisor
coordinates.

The marked `q` is the exact prime-power coordinate needed by the carry
constraint graph. It is not inserted after taking a norm.

## 2. Exact carry divisor-gradient

The adjacent flow on PR #254 has constraint change

\[
\boxed{
\Delta_qF
=\sum_jF_j
\left(
 \mathbf1_{q\mid j+1}
 -2\mathbf1_{q\mid j}
 +\mathbf1_{q\mid j-1}
\right).}
\tag{L-25805.3}
\]

If the diagonal transport index is `j=q`, its negative diagonal contribution is
`-2F_q`. Every positive child lies at a prime power dividing `q-1` or `q+1`.

Outside the case where `q-1` or `q+1` itself is a prime power, every child is at
most

\[
{q+1\over2}.
\tag{L-25805.4}
\]

This is a strict factor-two descent in the marked prime-power coordinate.

## 3. Uniform same-scale cluster solve

Consecutive prime powers above `5` form clusters of length at most three. The
exceptional initial cluster is

\[
\{2,3,4,5\}.
\]

For a path cluster of length `r<=3`, the same-scale matrix is

\[
A_r=2I-\operatorname{Adj}(P_r),
\tag{L-25805.5}
\]

and `A_r^-1` is entrywise nonnegative.

For the exceptional cluster, the exact matrix and inverse are

\[
A_{\rm exc}=
\begin{pmatrix}
2&-2&2&-2\\
-1&2&-1&-1\\
0&-1&2&-1\\
0&0&-1&2
\end{pmatrix},
\]

\[
A_{\rm exc}^{-1}=
\begin{pmatrix}
3/2&2&1&3\\
3/2&3&2&4\\
1&2&2&3\\
1/2&1&1&2
\end{pmatrix}\ge0.
\tag{L-25805.6}
\]

Therefore every nonnegative same-scale prime-power defect vector can be removed
by a joint nonnegative cluster solve. After that solve, all positive children
are at most half scale.

This finite algebra is inherited exactly from `L-25301`.

## 4. Depletion dipole supplies signed slack

The depleted top source is

\[
Z_{K,V,Q}
=(\varepsilon-\delta_Q)*\ell*r_V^{*(K-1)}.
\tag{L-25805.7}
\]

Thus every current-scale source row has a signed companion shifted by `Q`.
For

\[
Q=V^{\lfloor\delta_0K\rfloor},
\]

the companion lies a fixed fraction of `J` lower.

The proposed transport uses the current row as defect and the shifted row as
slack before any positive part is taken. This is the exact analogue of the
constraint dipole on PR #254, where positive and negative von-Mangoldt weighted
masses are separately macroscopic but their signed difference is small.

## 5. Source binding required for `PADT`

For every flow edge, the production object must exhibit an exact source pair

```text
marked prime power q
aggregate anchor index j
complete residual tuple fiber
current output/ratio cell
adjacent sibling at j+1 or j-1
```

and prove that the difference is either:

1. an internal adjacent current measured by `L-25804`;
2. a jointly solved same-scale prime-power cluster;
3. a child with marked prime-power endpoint at most half scale;
4. a residual-cutoff or compact-window boundary row;
5. an explicit `Q`-shifted slack row.

The finite cluster theorem does not itself prove this source binding. In
particular, changing `j` may cross a residual cutoff or alter a product cell.
Those events must be emitted as boundaries.

## 6. Proposed cost mechanism

The exact objective weight of adjacent carry transport is

\[
\log{j^2\over j^2-1}
=j^{-2}+O(j^{-4}).
\tag{L-25805.8}
\]

The physical displacement estimate of `L-25804` has the same order

\[
\log^2{j+1\over j}=j^{-2}+O(j^{-3}).
\tag{L-25805.9}
\]

This match is the reason to expect the signed carry flow to control the
prime-anchored physical Gram. The proposed theorem does not ask a scalar LP
objective to stand in for energy: the final quadratic cost is checked in the
actual two-frequency Gram.

## 7. Proof boundary

Closed exactly:

- the marked prime-power anchor;
- the carry divisor-gradient;
- bounded same-scale cluster inversion;
- factor-two child descent;
- equality of the natural transport-cost scales.

Open:

- the complete source binding;
- global signed flow construction;
- subexponential two-frequency transport cost;
- `PADT(K)` or RH.
