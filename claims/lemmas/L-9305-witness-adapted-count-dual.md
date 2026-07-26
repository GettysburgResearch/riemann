# L-9305 — Witness-adapted count duals for direct-xi logarithmic rows

Claim ID: L-9305  
Title: A fixed direct-\(\xi\) witness can extract more rigorously certified zero mass than the universal radial count envelope  
Status: PROPOSED  
Authoring agent: `gpt56-01-j`  
Created: 2026-07-26  
Dependencies: L-7501, L-7502, L-9303, L-9304  
Scope: finite scalar logarithmic-modulus witnesses from unconditional exact zero counts  
Related counterexample candidates: none

## Summary

Let

\[
H_T(x^2)=\left|\xi\!\left(\frac12+x+iT\right)\right|^2,
\qquad G_T(u)=\log H_T(u).
\]

PR #104 constructs the largest **universal radial Stieltjes submeasure** forced by an arbitrary table of overlapping exact zero counts. That object is optimal when one wants a subtraction valid simultaneously for every positive Cauchy kernel.

A fixed witness needs less universality. This lemma proves that the same count table admits a row-specific linear-programming dual which can certify a strictly larger subtraction for one chosen logarithmic row. The certificate is finite and exact: one nonnegative integer primal vector and one rational dual vector with equal objectives.

For the existentially complete two-point row

\[
R_{u,v}(T)=G_T(v)-G_T(u),\qquad 0<u<v,
\]

one strict directed inequality

\[
\sup I_{R_{u,v}}<m^{\mathsf T}\lambda
\]

contradicts RH, provided the unconditional count gates, direct completed-\(\xi\) rectangles, and normalization have been independently validated.

## Count atoms

Fix a real ordinate \(T\). Let

\[
C_1<C_2<\cdots<C_J
\]

be pairwise-disjoint signed ordinate cells, ordered from left to right. The cells need not be symmetric about \(T\). Let \(x_j\) be the number of nontrivial zeta zeros whose ordinate lies in \(C_j\), counted with multiplicity.

Suppose an unconditional argument-principle or Turing computation gives exact counts in windows that are unions of consecutive cells. Write

\[
Ax=m,
\]

where

- \(A\in\{0,1\}^{R\times J}\) has the consecutive-ones property in every row;
- \(m\in\mathbf Z_{\ge0}^R\) is the vector of exact window counts;
- \(x\in\mathbf Z_{\ge0}^J\) is the unknown atom-count vector.

The count computation itself never assumes RH. Under the RH hypothesis used in a contradiction proof, every counted nontrivial zero lies on the critical line, so the same integers become critical-line multiplicities in the product for \(H_T\).

Zeros outside the union of the declared cells are deliberately left uncounted.

## General fixed logarithmic row

Choose exact positive nodes \(u_1,\ldots,u_n\) and exact rational coefficients \(\beta_1,\ldots,\beta_n\) satisfying

\[
\sum_{i=1}^n\beta_i=0.
\]

Define

\[
R_\beta(T)=\sum_{i=1}^n\beta_iG_T(u_i)
\]

and the response of one critical-line zero at squared distance \(y=(T-\gamma)^2\):

\[
\phi_\beta(y)=\sum_{i=1}^n\beta_i\log(u_i+y).
\]

Assume

\[
\phi_\beta(y)\ge0\qquad(y\ge0).
\]

This covers every RH-valid scalar logarithmic row from the direct-modulus hierarchy. The principal production case is

\[
\beta=(-1,+1),\qquad
\phi_{u,v}(y)=\log\frac{v+y}{u+y}>0.
\]

For each atom \(C_j\), choose an exact rational number \(c_j\) satisfying

\[
0\le c_j\le
\inf_{\gamma\in C_j}
\phi_\beta\bigl((T-\gamma)^2\bigr).
\]

For the two-point row, \(\phi_{u,v}\) decreases with \(y\), so if

\[
B_j=\sup_{\gamma\in C_j}(T-\gamma)^2,
\]

it is enough to prove

\[
c_j\le\log\frac{v+B_j}{u+B_j}.
\]

Rational lower enclosures for these logarithms are obtained by the positive \(\operatorname{atanh}\) series; no floating-point value enters the certificate.

## Dual certificate theorem

Let \(\lambda\in\mathbf Q^R\) be unrestricted in sign and satisfy

\[
\boxed{A^{\mathsf T}\lambda\le c}
\]

coordinatewise. Then RH implies

\[
\boxed{R_\beta(T)\ge m^{\mathsf T}\lambda.}
\]

### Proof

Under RH, the canonical product of L-7501/L-7502 gives

\[
R_\beta(T)
=
\sum_\gamma m_\gamma
\phi_\beta\bigl((T-\gamma)^2\bigr),
\]

with locally convergent nonnegative summands. Retain only zeros in the declared atoms. Every omitted zero contributes a nonnegative quantity, so

\[
R_\beta(T)
\ge
\sum_{j=1}^{J}c_jx_j
=c^{\mathsf T}x.
\]

Since \(x\ge0\) and \(A^{\mathsf T}\lambda\le c\),

\[
c^{\mathsf T}x
\ge
\lambda^{\mathsf T}Ax
=
\lambda^{\mathsf T}m.
\]

This proves the claim. ∎

## Strict finite RH-disproof criterion

Let directed completed-\(\xi\) rectangles produce a rational interval

\[
R_\beta(T)\in I_\beta.
\]

If

\[
\boxed{
\sup I_\beta-m^{\mathsf T}\lambda<0,
}
\]

then RH is false.

For the two-point row, the primitive interval is simply

\[
I_{u,v}
=
\log H_T(v)-\log H_T(u),
\]

formed from outward modulus-square intervals and exact rational logarithm enclosures. The certificate uses no \(\xi'/\xi\), no division by \(\xi\), no derivative jet, and no interval eigensolver.

## Exact optimality certificate

The dual vector alone proves a safe subtraction. To prove that it is the strongest subtraction supported by the declared rational cell costs, additionally provide a nonnegative integer vector \(x^*\) such that

\[
Ax^*=m
\]

and

\[
\boxed{
c^{\mathsf T}x^*=m^{\mathsf T}\lambda.}
\]

Weak duality then proves optimality.

The consecutive-ones matrix \(A\) is totally unimodular, so the linear relaxation has an integral optimum for integral \(m\). Integrality is useful for discovery, but it is not part of the checker trust boundary: the supplied integer primal and rational dual are verified directly.

## Why the universal radial envelope can be weaker

Pointwise radial minima and integration need not commute:

\[
\min_x\int N_x(s)w(s)\,ds
\quad\text{can exceed}\quad
\int\min_x N_x(s)w(s)\,ds.
\]

The universal envelope takes the right-hand quantity because it must be a common submeasure for every compatible zero configuration. A fixed row solves the left-hand optimization and retains correlations between overlapping asymmetric windows.

Thus L-9305 does not contradict the optimality statement of L-9304. It changes the optimization target:

- L-9304 is maximal among **universal positive-measure subtractions**;
- L-9305 is optimal for one **declared scalar response** after rational cell lower bounds are fixed.

## Strict exact separation

Take four signed atoms at offsets

\[
-2,-1,+1,+2
\]

with unknown counts \(x_0,x_1,x_2,x_3\). Suppose exact overlapping count windows give

\[
x_1+x_2+x_3=5,
\]

\[
x_0+x_1+x_2=6.
\]

Use the two-point row \(u=1,v=3\). The exact per-zero responses are

\[
\log\frac{7}{5}
\quad\text{at }|T-\gamma|=2,
\qquad
\log2
\quad\text{at }|T-\gamma|=1.
\]

The rational lower costs

\[
c=\left(\frac13,\frac12,\frac12,\frac13\right)
\]

are valid because

\[
\log\frac75>\frac13,
\qquad
\log2>\frac12.
\]

A coarse safe dual is

\[
\lambda_{\rm coarse}=\left(0,\frac13\right),
\qquad
m^{\mathsf T}\lambda_{\rm coarse}=2.
\]

The witness-adapted dual is

\[
\lambda_*=\left(\frac16,\frac13\right),
\qquad
m^{\mathsf T}\lambda_*=\frac{17}{6}.
\]

Indeed,

\[
A^{\mathsf T}\lambda_*
=
\left(\frac13,\frac12,\frac12,\frac16\right)
\le c.
\]

The integer primal

\[
x^*=(1,0,5,0)
\]

satisfies both count equations and

\[
c^{\mathsf T}x^*=\frac{17}{6},
\]

so the bound is optimal for the declared costs.

Now use the exact synthetic modulus

\[
H(u)=(u-5)^2(u+4)(u+1)^5.
\]

At \(u=1,v=3\),

\[
H(1)=2560,
\qquad H(3)=28672,
\]

and therefore

\[
\log\frac{H(3)}{H(1)}
=
\log\frac{56}{5}
\approx2.4159137783010487.
\]

The raw row is positive. The coarse count-deflated row remains positive:

\[
\log\frac{56}{5}-2
\approx+0.4159137783010489.
\]

But the exact witness-adapted row is negative:

\[
\boxed{
\log\frac{56}{5}-\frac{17}{6}
\approx-0.4174195550322845.
}
\]

Thus the row-adapted dual exposes a hidden synthetic off-line factor while both the undecomposed row and the weaker safe count subtraction fail.

This is an exact synthetic control, not a Riemann-\(\xi\) evaluation.

## Existential completeness

If RH fails at

\[
\rho=\frac12+\delta+i\gamma,
\qquad d=\delta^2>0,
\]

then near \(u=d\),

\[
G_\gamma(u)=2m\log|u-d|+A(u)
\]

with \(A\) analytic. The two-point row becomes arbitrarily negative as the right node approaches \(d\) from the left while the left node remains separated. Every finite count-dual subtraction is finite at fixed positive nodes. Therefore every off-line zero still supplies an open family of exact rational or dyadic negative witness-adapted rows.

## Production protocol

1. Partition the endpoints of every available exact count window into signed atom cells.
2. Choose a direct-\(xi\) two-point row, preferably nominated by ordinary high precision.
3. Compute exact rational lower bounds for each atom response using its farthest squared distance.
4. Solve the finite LP outside the trust boundary.
5. Export one integer primal and one rational dual with equal objectives.
6. Evaluate the two completed-\(xi\) values with directed arithmetic.
7. Run X-9304 and preserve the first strict negative interval before changing nodes or counts.
8. Independently reproduce both the count table and the completed-\(xi\) rectangles.

Because the LP is row-specific and inexpensive, the same count artifact can rank many candidate node pairs without another Turing computation.

## Proof boundary

- The theorem assumes the parent direct-modulus canonical product and normalization.
- Exact total-zero counts are converted to critical-line counts only inside the RH contradiction hypothesis.
- Every cell lower cost must be independently enclosed; midpoint logarithms are not admissible.
- The dual variables are unrestricted because the count constraints are equalities.
- Counts outside the declared atom union are not assumed absent; their row contributions remain nonnegative.
- A negative synthetic control is not a Riemann-\(xi\) candidate.
- A Riemann-\(xi\) negative still requires independent count and special-function reproduction.

## Suggested next attack

Apply X-9304 to the PR #71 overlapping count table from PR #104. Search two-point node pairs first, because their cell costs are monotone and cheap to certify. Rank additional asymmetric Turing windows by the exact increase in the dual objective of the tightest row rather than by radial-profile gain alone.
