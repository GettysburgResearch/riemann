# L-9704 — Positive-node Geronimus one-scalar Schur gate

Claim ID: `L-9704`  
Title: Adding one positive horizontal node raises the full response degree by one and reduces the new half-line cone to a two-sided scalar interval  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-7501`, `L-9308`, `L-9309`, `L-9310`; any already validated count-deflated direct-`xi` functional  
Scope: exact finite direct-completed-`xi` response tables under one new positive node  
Related counterexample candidates: `O-9703`

## Summary

Let

\[
 0<u_1<\cdots<u_n
\]

be an old direct-`xi` node table, and let

\[
 a_k=L_{\rm old}(y^k),\qquad 0\le k\le 2m,
\]

be its exact directed response moments.  Add one exact positive node

\[
 w>0,\qquad w\notin\{u_1,\ldots,u_n\}.
\]

If the extended moments are

\[
 b_k=L_{\rm new}(y^k),
\]

then the exact recurrence is

\[
 \boxed{a_k=b_{k+1}+wb_k.}
\tag{L-9704.1}
\]

Thus every new moment is affine in the single new scalar `b_0`:

\[
 \boxed{
 b_k=(-w)^k b_0+
 \sum_{j=0}^{k-1}(-w)^{k-1-j}a_j.}
\tag{L-9704.2}
\]

Suppose the old degree is `2m` and the new degree is `2m+1`.  Define

\[
 v_0=(a_0,\ldots,a_{m-1})^{\mathsf T},
\qquad
 (C_0)_{ij}=a_{i+j+1}+w a_{i+j},
\tag{L-9704.3}
\]

and

\[
 v_1=(a_1,\ldots,a_m)^{\mathsf T},
\qquad
 (C_1)_{ij}=a_{i+j+2}+w a_{i+j+1},
\tag{L-9704.4}
\]

for `0<=i,j<m`.  If `C_0` and `C_1` are positive definite, put

\[
 \lambda_-(w)=v_0^{\mathsf T}C_0^{-1}v_0,
\qquad
 \lambda_+(w)=
 \frac{a_0-v_1^{\mathsf T}C_1^{-1}v_1}{w}.
\tag{L-9704.5}
\]

Then the following are equivalent:

1. the extended response functional is nonnegative on **every** real polynomial
   `P>=0` on `[0,infinity)` of degree at most `2m+1`;
2. its two half-line moment matrices are positive semidefinite;
3. the one scalar `b_0` lies in the exact two-sided Schur interval
   \[
      \boxed{\lambda_-(w)\le b_0\le\lambda_+(w).}
   \tag{L-9704.6}
   \]

If the lower inequality fails, an explicit witness is a square `P=q_0^2`.  If
the upper inequality fails, an explicit witness is `P=yq_1^2`.  Either strict
directed failure is a finite RH-disproof nomination through `L-9308`, subject
to the named direct-`xi`, count, normalization, and independent-reproduction
gates.

This proves the positive-node recurrence proposed—but explicitly left
unverified—in `O-9311`, and strengthens it from an affine observation to a
complete exact separation theorem.

## Setup and response maps

Put

\[
 D(y)=\prod_{i=1}^{n}(y+u_i).
\]

For an old zero-sum coefficient vector `beta`, its response polynomial is

\[
 P_\beta(y)
 =-
 \sum_{i=1}^{n}\beta_i\frac{D(y)}{y+u_i}.
\tag{L-9704.7}
\]

After adjoining `w`, the new denominator is

\[
 \widetilde D(y)=(y+w)D(y).
\]

The old coefficient vector, extended by coefficient zero at `w`, has new
response

\[
 -\sum_i\beta_i\frac{(y+w)D(y)}{y+u_i}
 =(y+w)P_\beta(y).
\tag{L-9704.8}
\]

## Proof of the moment recurrence

Choose the old portfolio whose response is `y^k`.  Its scalar contraction is
`a_k`.  By (L-9704.8), the same coefficient vector on the extended table has
response

\[
 (y+w)y^k=y^{k+1}+wy^k.
\]

Its scalar contraction is therefore `b_(k+1)+w b_k`.  The primitive
contraction did not change, proving (L-9704.1).  Iterating proves
(L-9704.2).

## Adapted-basis block diagonalization

For the degree-`2m+1` half-line problem, `L-9310` uses

\[
 H_0=(b_{i+j})_{0\le i,j\le m},
 \qquad
 H_1=(b_{i+j+1})_{0\le i,j\le m}.
\tag{L-9704.9}
\]

Instead of the monomial basis, use

\[
 e_0(y)=1,
 \qquad
 e_{i+1}(y)=y^i(y+w),\quad0\le i<m.
\tag{L-9704.10}
\]

For `H_0`, the cross terms are

\[
 L_{\rm new}(e_0e_{i+1})
 =b_{i+1}+wb_i=a_i.
\]

The lower block is

\[
\begin{aligned}
 L_{\rm new}(e_{i+1}e_{j+1})
 &=b_{i+j+2}+2wb_{i+j+1}+w^2b_{i+j}\\
 &=a_{i+j+1}+wa_{i+j}.
\end{aligned}
\]

Thus the congruent matrix is

\[
 G_0(b_0)=
 \begin{pmatrix}
 b_0&v_0^{\mathsf T}\\
 v_0&C_0
 \end{pmatrix}.
\tag{L-9704.11}
\]

For the localizing form `H_1`, the same basis gives

\[
 G_1(b_0)=
 \begin{pmatrix}
 a_0-wb_0&v_1^{\mathsf T}\\
 v_1&C_1
 \end{pmatrix}.
\tag{L-9704.12}
\]

The basis change is invertible because each `e_(i+1)` has leading term
`y^(i+1)`.  Therefore `H_j` and `G_j` have exactly the same inertia.

## Two-sided Schur theorem

Assume `C_0,C_1` are positive definite.  The Schur-complement criterion gives

\[
 G_0(b_0)\succeq0
 \iff
 b_0-v_0^{\mathsf T}C_0^{-1}v_0\ge0,
\]

and

\[
 G_1(b_0)\succeq0
 \iff
 a_0-wb_0-v_1^{\mathsf T}C_1^{-1}v_1\ge0.
\]

These are precisely the two inequalities in (L-9704.6).  By `L-9310`,
positivity of both matrices is equivalent to nonnegativity on the complete
half-line polynomial cone of degree at most `2m+1`.

### Explicit lower witness

Let

\[
 z_0=C_0^{-1}v_0
\]

and define

\[
 q_0(y)=1-
 (y+w)\sum_{i=0}^{m-1}(z_0)_i y^i.
\tag{L-9704.13}
\]

The adapted-coordinate vector `(1,-z_0)` has quadratic value

\[
 L_{\rm new}(q_0^2)
 =b_0-\lambda_-(w).
\tag{L-9704.14}
\]

Hence a strict negative upper endpoint gives the explicit nonnegative response
`P=q_0^2`.

### Explicit upper witness

Let

\[
 z_1=C_1^{-1}v_1
\]

and put

\[
 q_1(y)=1-
 (y+w)\sum_{i=0}^{m-1}(z_1)_i y^i.
\tag{L-9704.15}
\]

Then

\[
 L_{\rm new}(yq_1^2)
 =a_0-wb_0-v_1^{\mathsf T}C_1^{-1}v_1
 =w(\lambda_+(w)-b_0).
\tag{L-9704.16}
\]

A strict negative upper endpoint therefore gives the response `P=yq_1^2`.

## One-new-point contraction

The theorem is computationally useful only if `b_0` does not require
re-evaluating the entire old table.  It does not.

The coefficient of the new node in the response-`1` portfolio is

\[
 \boxed{
 \beta_w=-\frac1{D(-w)}
 =-\frac1{\prod_i(u_i-w)}.}
\tag{L-9704.17
}

Indeed, evaluate the response identity at `y=-w`.

Let `F(u)` denote the already deflated logarithmic direct-`xi` primitive.
Choose one old reference node `u_r`.  Define

\[
 P_r(y)=
 \frac{1+\beta_wD(y)}{y+w}
 -\beta_w\frac{D(y)}{y+u_r}.
\tag{L-9704.18}
\]

Both displayed quotients are exact polynomials and the degree-`n-1` terms
cancel, so

\[
 P_r(y)=\sum_{k=0}^{n-2}p_{r,k}y^k.
\]

Then

\[
 \boxed{
 b_0=
 \beta_w\bigl(F(w)-F(u_r)\bigr)
 +\sum_{k=0}^{n-2}p_{r,k}a_k.}
\tag{L-9704.19}
\]

### Proof

Let `(beta_w,gamma_1,...,gamma_n)` be the extended response-`1`
coefficients.  The old restriction has response

\[
 P_\gamma(y)=\frac{1+\beta_wD(y)}{y+w}.
\]

Because the full vector is zero sum,

\[
 \delta_i=\gamma_i+\beta_w1_{i=r}
\]

is an old zero-sum vector.  Its old response is exactly `P_r`.  Therefore

\[
\begin{aligned}
 b_0
 &=\beta_wF(w)+\sum_i\gamma_iF(u_i)\\
 &=\beta_w(F(w)-F(u_r))+
   \sum_i\delta_iF(u_i)\\
 &=\beta_w(F(w)-F(u_r))+
   \sum_kp_{r,k}a_k.
\end{aligned}
\]

No old primitive other than the reference value enters this second replay.

## Directed robust closure

For interval-valued old moments and `b_0`, X-9704 constructs the adapted
interval matrices (L-9704.11)--(L-9704.12).  Let `M_j` and `R_j` be their exact
rational midpoint and entry-radius matrices.  A declared rational `delta_j>0`
proves robust positivity when:

1. exact rational LDL proves `M_j-delta_j I` positive definite;
2. the exact maximum row sum of `R_j` is below `delta_j`.

Then every admissible matrix satisfies

\[
 G_j\succeq(\delta_j-\|R_j\|_\infty)I\succ0.
\]

If closure fails, X-9704 freezes the exact rational midpoint Schur vectors and
contracts (L-9704.14) and (L-9704.16) directly.  A negative interval is a
proof object; a negative midpoint is only a nomination.

## Degenerate lower blocks

The scalar equivalence above assumes `C_0,C_1` positive definite.  This is the
production regime inherited from the strictly positive old cone.  In a
singular case, the exact general criterion is:

\[
 C\succeq0,\quad v\in\operatorname{range}C,
 \quad \alpha\ge v^{\mathsf T}C^+v.
\]

X-9704 fails closed rather than invoking a pseudoinverse.  A future exact
rank-revealing extension may handle this case, but no certificate in this
branch assumes it.

## Analytic domain audit

- `w` and every old node are exact positive rationals and are pairwise distinct.
- `F(w)` is formed from a direct completed-`xi` rectangle; no division by `xi`
  occurs.
- Common positive scaling cancels in the point difference and every zero-sum
  response moment.
- Count deflation uses the same exact count profile for the new point, the old
  reference point, and the old moments.
- Every logarithm has a rigorously positive modulus-square or positive
  `u+B` argument.

## Gap audit

- The recurrence alone does not establish positivity; both Schur inequalities
  are necessary.
- A new node equal to an old node is invalid.
- Direct barycentric contraction at widely separated nodes can be badly
  conditioned; the reduced identity (L-9704.19) is the preferred replay.
- The old moment table, reference primitive, new primitive, count profile,
  ordinate, normalization, and common scale must be cryptographically bound.
- A midpoint `b_0` outside the interval is not a counterexample without a
  strict directed witness contraction.
- Positive closure is finite in ordinate, nodes, degree, and count profile.

## Suggested next attack

Run the one-point oracle at

\[
 x=1,2,4,8,
 \qquad w=x^2=1,4,16,64,
\]

on the exact PR #103 table and on the seven evidence-ranked PR #105 ordinates.
Rank centers first by the normalized lower/upper Schur distance, then replay
only the smallest candidates at 512/640 bits.  The new points lie in
`Re(s)>1`, where direct zeta evaluation is substantially easier than at the
microscopic original grid.