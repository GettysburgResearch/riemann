# L-15120 — Scale-optimized canonical-ray completion and an exact two-variable LP

Claim ID: `L-15120`  
Status: **PROVED FINITE-DIMENSIONAL SUFFICIENT THEOREM**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15111`, `L-15113`, `L-15116`  
Scope: corrected final arrow of the smooth-window/arithmetic-line program  
Related counterexample candidates: none

## 1. Why the previously proposed ratio is not invariant

The canonical completion is not one distinguished physical normalization.  If

\[
 Q^{\rm can}\succeq0,
 \qquad
 \ker Q^{\rm can}=\mathbb Rp,
\]

then every positive multiple

\[
 aQ^{\rm can},
 \qquad a>0,
\]

is an equally valid positive special completion with the same target kernel.
Therefore comparing the arithmetic matrix only with the single point
`Q^can` can reject an exact passing completion whose natural scale is `a!=1`.

The correct object is the **canonical positive ray**.

## 2. Setup

Let the nodes be distinct reals `lambda_i`, every `p_i` nonzero, and

\[
 \sum_i p_i=1.
\]

Assume the target polynomial has simple real roots, so the canonical matrix
`Q^can` is positive semidefinite of corank one.  Let

\[
 g_i=-\frac{P'(\lambda_i)}{P(\lambda_i)}
\]

be its special source, and let

\[
 m_{\rm can}
 =\lambda_{\min}(Q^{\rm can}|_{p^\perp})>0.
 \tag{L-15120.1}
\]

Let the arithmetic special matrix have source `beta_i`.  Its target-pinned line
has off-diagonal entries

\[
 T_p(c)_{ij}
 =\frac{\beta_i-\beta_j}{\lambda_i-\lambda_j}-c
 \qquad(i\ne j),
 \tag{L-15120.2}
\]

and its diagonal is forced by `T_p(c)p=0`.

For `a>0`, define

\[
 d_{ij}(a)
 =\frac{(\beta_i-\beta_j)-a(g_i-g_j)}
        {\lambda_i-\lambda_j}.
 \tag{L-15120.3}
\]

Then

\[
 (T_p(c)-aQ^{\rm can})_{ij}=d_{ij}(a)-c
 \qquad(i\ne j).
 \tag{L-15120.4}
\]

Because both matrices annihilate `p`, the diagonal difference is

\[
 (T_p(c)-aQ^{\rm can})_{ii}
 =-\frac1{p_i}
   \sum_{j\ne i}(d_{ij}(a)-c)p_j.
 \tag{L-15120.5}
\]

## 3. Scale-optimized row certificate

Put

\[
 \boxed{
 \mathcal E_p(a,c)
 =\max_i\sum_{j\ne i}
 |d_{ij}(a)-c|
 \left(1+\left|\frac{p_j}{p_i}\right|\right).}
 \tag{L-15120.6}
\]

Then

\[
 \|T_p(c)-aQ^{\rm can}\|_2
 \le\mathcal E_p(a,c).
 \tag{L-15120.7}
\]

Consequently,

\[
 \boxed{
 \mathcal E_p(a,c)<a m_{\rm can}
 \quad\Longrightarrow\quad
 T_p(c)\succeq0,
 \quad
 \ker T_p(c)=\mathbb Rp.}
 \tag{L-15120.8}
\]

### Proof

Equation (L-15120.7) follows from the maximum absolute row sum, using
(L-15120.4) for the off-diagonal and (L-15120.5) for the diagonal.  On
`p^perp`, the reference `aQ^can` has floor `a m_can`; the perturbation has
operator norm below that floor.  Thus `T_p(c)` is positive definite on
`p^perp`.  It annihilates `p` exactly by target pinning. QED.

## 4. The correct cofinal statistic

Define

\[
 \boxed{
 \Theta_j
 =\inf_{a>0,\ c\in\mathbb R}
   \frac{\mathcal E_{p_j}(a,c)}
        {a m_{{\rm can},j}}.}
 \tag{L-15120.9}
\]

Then

\[
 \boxed{
 \limsup_{j\to\infty}\Theta_j<1}
 \tag{L-15120.10}
\]

is sufficient for the arithmetic target-pinned line to pass cofinally.  The
stronger limit `Theta_j->0` is more than sufficient.

This replaces the unscaled expression

\[
 \inf_c\mathcal E_{p_j}(1,c)/m_{{\rm can},j},
\]

which is not a valid invariant of the completion problem.

## 5. Exact convex reformulation

Put

\[
 t=1/a>0,
 \qquad
 q=c/a,
\]

and define the arithmetic and canonical off-diagonal matrices

\[
 A_{ij}=\frac{\beta_i-\beta_j}{\lambda_i-\lambda_j},
 \qquad
 C_{ij}=\frac{g_i-g_j}{\lambda_i-\lambda_j}.
\]

Then

\[
 \frac{d_{ij}(a)-c}{a}=tA_{ij}-C_{ij}-q.
\]

Hence

\[
 \boxed{
 \Theta
 =\frac1{m_{\rm can}}
   \inf_{t>0,q\in\mathbb R}
   \max_i\sum_{j\ne i}
   \left(1+\left|\frac{p_j}{p_i}\right|\right)
   |tA_{ij}-C_{ij}-q|.}
 \tag{L-15120.11}
\]

The numerator is convex and piecewise linear in the two variables `(t,q)`.
For rational finite data it is an exact rational linear program.  Introduce
variables `z_ij>=0` and `M` with constraints

```text
z_ij >=  t A_ij-C_ij-q,
z_ij >= -t A_ij+C_ij+q,
M >= sum_(j!=i) w_ij z_ij for every i,
t > 0.
```

A rational feasible point with `M<m_can` is a complete proof certificate.
A rational dual LP with optimum `>=m_can` is a finite obstruction to this
**sufficient** canonical-ray criterion.

## 6. Exact counterexample to the unscaled criterion

Take

\[
 \lambda=(-1,0,1),
 \qquad
 p=(1/3,1/3,1/3).
\]

The canonical source and matrix are

\[
 g=(3,0,-3),
\]

\[
 Q^{\rm can}
 =\begin{pmatrix}
 6&-3&-3\\
 -3&6&-3\\
 -3&-3&6
 \end{pmatrix},
\]

with positive eigenvalues `9,9`.

Choose an arithmetic source

\[
 \beta_i=3g_i+2\lambda_i+5,
\]

namely

\[
 \beta=(12,5,-2).
\]

At the scalar `c=2`, the target-pinned matrix is exactly

\[
 T_p(2)=3Q^{\rm can},
\]

so it is a strict pass.  But comparison with the unscaled point `Q^can` leaves
`2Q^can`; its maximum row sum is `24`, larger than the canonical moat `9`.
The unscaled row criterion therefore fails on an exact positive completion.
The optimized criterion takes `a=3,c=2` and has zero error.

Thus scale optimization is load bearing, not cosmetic.

## 7. Exact versus sufficient geometry

In the residue coordinates of `L-15114`, the exact arithmetic gate asks whether
one affine line intersects the positive orthant.  The canonical-ray ball
criterion above asks whether that line enters a certified norm neighborhood of
the positive ray through `(1,...,1)`.

Therefore:

- `Theta<1` is sufficient, not necessary;
- failure of the LP does not prove that the arithmetic scalar line is
  infeasible;
- exact threshold separation or residue-orthant intersection remains the final
  decision when the canonical-ray moat test is inconclusive.

## 8. Gap audit

1. Canonical real-rootedness and a positive moat are prerequisites.
2. The source, nodes, target, and CCM phase adapter must use one normalization.
3. The row norm can be pessimistic; a directed operator-norm LMI is sharper.
4. Cofinal decay observed numerically is not a theorem.
5. Proving (L-15120.10) for the Riemann arithmetic source is still an RH-bearing
   arithmetic problem.