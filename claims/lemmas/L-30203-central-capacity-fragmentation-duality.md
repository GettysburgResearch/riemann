# L-30203 — Central-capacity fragmentation duality

Claim ID: `L-30203`  
Title: The missing eta source-flow manifest is exactly a balanced-fragmentation feasibility problem with an explicit superadditive-potential dual  
Status: **PROPOSED COMPLETE FINITE LP DUALITY LEMMA**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #247/272 balanced fragmentation and Pascal cycle bases; `D-30201`  
Scope: one finite endpoint and one frozen source manifest; no cofinal estimate

## 1. Finite fragmentation system

Fix an endpoint `X` and a balanced edge set

\[
 \mathcal E_\eta(X)
 =\{[n,j]:2\le n\le X,\ \eta n\le j\le(1-\eta)n\}.
\]

Let

\[
 B:\mathbb R^{\mathcal E_\eta(X)}\to\mathbb R^{\{1,\ldots,X\}}
\]

be the node-divergence matrix. Let `r` be the exact divergence which the upper
flow must realize.

A frozen `D-30201` manifest declares a nonnegative required-capacity vector
`a`, supported on a finite set `C` of central edges. Thus

\[
 a_e\ge0,
 \qquad
 a_e=0\quad(e\notin C).
\]

The zero-defect source-flow problem is

\[
\boxed{
 Bd=r,
 \qquad
 d_e\ge a_e\quad(e\in C),
 \qquad
 d_e\ge0\quad(e\notin C).
}
\tag{L-30203.1}

## 2. Reduction to an ordinary positive fragmentation problem

Write

\[
 d=a+x.
\]

Then (L-30203.1) is equivalent to

\[
\boxed{
 x\ge0,
 \qquad
 Bx=r-Ba.
}
\tag{L-30203.2}

Thus the central-capacity requirement does not require a new class of flow. It
changes the target divergence from `r` to the explicit residual

\[
\boxed{r^{\rm cap}=r-Ba.}
\tag{L-30203.3}

Every coefficient and node of `r^cap` is finite and exactly computable from the
source and flow manifests.

## 3. Exact Farkas dual

For a node potential `F=(F(1),...,F(X))`,

\[
 (B^TF)_{[n,j]}
 =F(n)-F(j)-F(n-j).
\tag{L-30203.4}

Finite Farkas duality gives the following equivalence.

> There is a zero-defect source-flow completion if and only if
> \[
> \boxed{
> \sum_{m=1}^X F(m)r^{\rm cap}(m)\ge0
> }
> \tag{L-30203.5}
> \]
> for every balanced-superadditive potential satisfying
> \[
> \boxed{
> F(n)-F(j)-F(n-j)\ge0
> \quad([n,j]\in\mathcal E_\eta(X)).
> }
> \tag{L-30203.6}

The sign convention follows the parent-positive divergence used throughout the
carry repository. Reversing the convention reverses both displayed signs.

This dual is exact: one violating potential is a finite obstruction certificate,
and the absence of such a potential gives a finite nonnegative completion.

## 4. Defect-minimizing version

Let `omega_e>0` be the exact capacity weight. Permit shortages `delta_e>=0` on
the required central edges and minimize

\[
\boxed{
 \mathfrak C_X
 =\min
 \left\{
 \sum_{e\in C}\omega_e\delta_e:
 Bd=r,
 d\ge0,
 d_e+\delta_e\ge a_e\ (e\in C)
 \right\}.
}
\tag{L-30203.7
}

This is a finite linear program. Its dual consists of:

- a balanced-superadditive potential `F`;
- nonnegative central-edge prices `lambda_e` bounded by `omega_e`;
- edge inequalities coupling `B^TF` to those prices.

A proof object may emit exact primal and dual rational intervals and
primal-dual equality. No existence assertion is hidden behind the word
“capacity.”

## 5. Relation to the full RH obstruction

If `a=0`, (L-30203.5)--(L-30203.6) reduce to the balanced-fragmentation Farkas
dual already isolated on PR #247. Therefore the central-capacity theorem is not
an unrelated local lemma: it is a source-pinned strengthening of the same full
arithmetic cone.

The logarithmic/von-Mangoldt and fixed-ratio Möbius mutations remain admissible
dual tests. A generic positive-kernel or bounded-rank estimate cannot prove
(L-30203.5) without controlling those source-specific modes.

## 6. New attack interface

The analytic eta cascade gives considerably more structure than an arbitrary
`r^cap`:

```text
required capacities form Hausdorff sequences;
paired residuals form Hausdorff sequences by L-30202;
all unmatched terms are finite cutoff collars;
the support descends by a factor two per generation;
the bulk analytic bank contracts by 6/7.
```

A full proof of `SFC` may therefore attack the dual potentials in
(L-30203.5) generation by generation, rather than solving the ambient BCT cone.
The exact target is:

\[
 \left[-\sum_mF(m)r^{\rm cap}(m)\right]_+
 \le C\log^A(2X)
\]

for every normalized admissible `F` at every cascade depth.

## 7. Proof boundary

Closed exactly:

1. the capacity problem as a residual divergence;
2. the zero-defect Farkas alternative;
3. a finite weighted-defect LP;
4. the source-specific dual review interface.

Open:

1. a polylogarithmic bound for the actual critical manifests;
2. `SFC`;
3. RH.