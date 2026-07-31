# L-15116 — Canonical-source proximity implies arithmetic scalar completion

Claim ID: `L-15116`  
Status: **PROVED FINITE-DIMENSIONAL SUFFICIENT LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15111`, `L-15113`, `L-15114`  
Scope: root-free transfer from a canonical positive special metric to the actual target-pinned scalar line  
Related counterexample candidates: none

## 1. Setup

Let the distinct real nodes be

\[
 \lambda_1,\ldots,\lambda_n,
\]

let every `p_i` be nonzero, and normalize

\[
 \sum_i p_i=1.
\]

Assume the target polynomial `P` has `n-1` simple real roots. Let

\[
 g_i=-\frac{P'(\lambda_i)}{P(\lambda_i)}
 \tag{L-15116.1}
\]

and let `Q^can` be the canonical positive Loewner completion of `L-15111`:

\[
 (Q^{\rm can})_{ij}
 =\begin{cases}
 (g_i-g_j)/(\lambda_i-\lambda_j),&i\ne j,\\
 g'(\lambda_i),&i=j.
 \end{cases}
 \tag{L-15116.2}
\]

Then

\[
 Q^{\rm can}\succeq0,
 \qquad
 \ker Q^{\rm can}=\mathbb Rp.
\]

Let the arithmetic special matrix have source values `beta_i`, and let

\[
 T_p(c)
\]

be its target-pinned scalar family. Off the diagonal,

\[
 (T_p(c))_{ij}
 =\frac{\beta_i-\beta_j}{\lambda_i-\lambda_j}-c.
 \tag{L-15116.3}
\]

## 2. Exact source-line discrepancy

For `i!=j`, define

\[
 \boxed{
 d_{ij}
 =\frac{(\beta_i-\beta_j)-(g_i-g_j)}
        {\lambda_i-\lambda_j}.}
 \tag{L-15116.4}
\]

Then

\[
 \boxed{
 (T_p(c)-Q^{\rm can})_{ij}=d_{ij}-c.}
 \tag{L-15116.5}
\]

The array `d_ij` is symmetric. It measures the divided-difference distance between the arithmetic source and the canonical Herglotz source. Addition of a constant to either source has no effect.

Because both matrices annihilate `p`, their diagonal difference is forced:

\[
 \boxed{
 (T_p(c)-Q^{\rm can})_{ii}
 =-\frac1{p_i}
   \sum_{j\ne i}(d_{ij}-c)p_j.}
 \tag{L-15116.6}
\]

Thus the complete matrix error is determined by the off-diagonal scalar fit.

## 3. Row-sum sufficient condition

Define

\[
 \boxed{
 \mathcal E_p(c)
 :=\max_i\sum_{j\ne i}
 |d_{ij}-c|
 \left(1+\left|\frac{p_j}{p_i}\right|\right).}
 \tag{L-15116.7}
\]

Equations (L-15116.5)--(L-15116.6) imply

\[
 \|T_p(c)-Q^{\rm can}\|_2
 \le
 \|T_p(c)-Q^{\rm can}\|_\infty
 \le\mathcal E_p(c).
 \tag{L-15116.8}
\]

Let the canonical positive moat be

\[
 m_{\rm can}
 =\lambda_{\min}(Q^{\rm can}|_{p^\perp})>0.
 \tag{L-15116.9}
\]

If

\[
 \boxed{
 \mathcal E_p(c)<m_{\rm can},}
 \tag{L-15116.10}
\]

then

\[
 \boxed{
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=\mathbb Rp.}
 \tag{L-15116.11}
\]

### Proof

The row bound follows by adding the absolute off-diagonal entries in (L-15116.5) and the diagonal estimate from (L-15116.6). Both matrices have the exact kernel vector `p`. Since the perturbation is smaller than the complete nonzero spectral moat of `Q^can`, the kernel-pinned inertia theorem `L-15113` preserves inertia `(n-1,0,1)`. QED.

## 4. Convex one-dimensional fit

The function

\[
 c\longmapsto\mathcal E_p(c)
\]

is convex and piecewise linear. Every breakpoint is one of the finite values `d_ij`. Hence its exact minimum can be found by one-dimensional rational convex optimization; an ordinary optimizer is unnecessary.

A particularly simple sufficient procedure is:

1. sort the exact/directed `d_ij` values;
2. test rational points in every resulting interval and at every rationally isolated breakpoint;
3. retain the smallest certified row bound;
4. compare it strictly with a directed lower bound for `m_can`.

A sharper proof object may build the full rational difference matrix at a nominated `c` and certify

\[
 \|T_p(c)-Q^{\rm can}\|_2<m_{\rm can}
\]

through a block LMI or exact generalized eigenvalue bound instead of the row-sum relaxation.

## 5. Cofinal criterion

For a target sequence, suppose:

1. the exact canonical Loewner matrices are PSD of corank one;
2. their positive moats are `m_j>0`;
3. there are rational scalars `c_j` with
   
   \[
   \mathcal E_{p_j}(c_j)<m_j
   \]
   
   for every sufficiently large `j`.

Then the arithmetic target-pinned scalar family passes cofinally. Together with local-uniform target convergence, `T-15104` implies RH.

The stronger asymptotic statement

\[
 \boxed{
 \frac{\inf_c\mathcal E_{p_j}(c)}{m_j}\longrightarrow0}
 \tag{L-15116.12}
\]

is therefore a sufficient positive-route theorem.

This is not asserted for the Riemann data. It is a new explicit analytic target: after removing one affine boundary source, the arithmetic divided differences must approach the canonical Herglotz divided differences relative to their positive moat.

## 6. Relation to residue weights

In the root basis of `L-15114`, the canonical completion has weights

\[
 w_k^{\rm can}=1,
\]

while the arithmetic scalar family has affine weights `w_k(c)`. Condition (L-15116.10) is a root-free sufficient condition that all arithmetic weights remain positive.

It can be stronger than necessary: the arithmetic line may enter the positive residue orthant even when its matrix distance from the canonical point exceeds the canonical Euclidean moat. Its advantage is that every quantity can be evaluated directly at the finite nodes.

## 7. Directed production interface

With interval target coefficients and arithmetic source intervals:

1. enclose `g_i=-P'(lambda_i)/P(lambda_i)` using `L-15113`;
2. enclose every `d_ij`;
3. choose a rational `c` and compute outward bounds for (L-15116.7);
4. independently certify a lower positive moat for the exact canonical matrix;
5. require strict separation.

If node values `P(lambda_i)` are small, the canonical source intervals can widen dramatically. No ordinary midpoint fit may be promoted without this denominator audit.

## 8. Gap audit

1. The theorem first requires canonical real-rootedness; it does not prove it.
2. The row-sum metric can be pessimistic when target coordinates have large dynamic range.
3. Closeness to the canonical point is sufficient, not necessary.
4. The actual arithmetic source must be in exactly the same node, phase, and boundary normalization.
5. Finite decay of the ratio in (L-15116.12) is reconnaissance until a cofinal theorem is proved.