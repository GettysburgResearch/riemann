# L-9308 — Resolvent-polynomial certificates for direct-xi logarithmic portfolios

Claim ID: L-9308  
Title: Exact polynomial sign certificates generate an RH-valid cone of multi-point direct-xi logarithmic witnesses  
Status: PROPOSED  
Authoring agent: `gpt56-01-k`  
Created: 2026-07-26  
Dependencies: L-7501, L-7502, L-9305  
Scope: finite direct-completed-xi portfolios and witness-adapted exact zero-count deflation  
Related counterexample candidates: none

## Statement

Fix exact positive nodes

\[
0<u_1<\cdots<u_n
\]

and exact rational coefficients \(\beta_1,\ldots,\beta_n\) with

\[
\sum_i\beta_i=0.
\]

For real \(T\), put

\[
G_T(u)=\log\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2,
\qquad
R_\beta(T)=\sum_i\beta_iG_T(u_i).
\]

Define the response of one critical-line zero at squared ordinate distance \(y\ge0\):

\[
\phi_\beta(y)=\sum_i\beta_i\log(u_i+y).
\]

Let

\[
D(y)=\prod_i(u_i+y)
\]

and

\[
\boxed{
P_\beta(y)
=-D(y)\phi_\beta'(y)
=-\sum_i\beta_i\prod_{j\ne i}(u_j+y).
}
\]

If

\[
P_\beta(y)\ge0\qquad(y\ge0),
\]

then

\[
\boxed{\phi_\beta(y)\ge0\qquad(y\ge0).}
\]

Consequently RH implies

\[
\boxed{R_\beta(T)\ge0.}
\]

More generally, combine the row with an exact total-zero count table \(Ax=m\), exact cell-response lower bounds \(c\), and an unrestricted rational L-9305 dual

\[
A^{\mathsf T}\lambda\le c.
\]

Then RH implies

\[
\boxed{R_\beta(T)\ge m^{\mathsf T}\lambda.}
\]

A directed interval satisfying

\[
\sup I_\beta<m^{\mathsf T}\lambda
\]

is therefore a finite RH-disproof witness, subject to the named direct-xi, count, normalization, and reproduction gates.

## Proof

The denominator \(D(y)\) is strictly positive on \([0,\infty)\). Hence

\[
\phi_\beta'(y)=-\frac{P_\beta(y)}{D(y)}\le0.
\]

Because \(\sum_i\beta_i=0\),

\[
\phi_\beta(y)
=\sum_i\beta_i\log\left(1+\frac{u_i}{y}\right)
\longrightarrow0
\]

as \(y\to\infty\). A nonincreasing function with limit zero at infinity is nonnegative, proving the response claim.

Under RH, the canonical product from L-7501/L-7502 gives

\[
R_\beta(T)
=
\sum_\gamma m_\gamma
\phi_\beta((T-\gamma)^2),
\]

with nonnegative summands. This proves \(R_\beta(T)\ge0\). The count-dual strengthening is exactly the L-9305 weak-duality argument applied to the cellwise lower bounds for \(\phi_\beta\). ∎

## Exact finite response certificates

The coefficients of \(P_\beta\) are exact rational linear functions of \(\beta\). The simplest proof object is

\[
P_\beta(y)=p_0+p_1y+\cdots+p_dy^d,
\qquad p_k\ge0.
\]

A standard-library checker recomputes the polynomial identity and verifies every coefficient sign. This sufficient cone is polyhedral and particularly convenient for exact discovery.

A larger optional certificate may use the substitution

\[
y=\frac{t}{1-t},\qquad0\le t<1,
\]

and verify nonnegative Bernstein coefficients for

\[
(1-t)^dP_\beta\!\left(\frac{t}{1-t}\right).
\]

That extension is mathematically valid but is not implemented in X-9305 and must not be assumed by its certificates.

## Exact three-point separator

Take

\[
(u_1,u_2,u_3)=(1,2,3),
\qquad
\beta=(-1,2,-1).
\]

Then

\[
\phi_\beta'(y)
=-\frac2{(y+1)(y+2)(y+3)},
\]

so

\[
\boxed{P_\beta(y)=2.}
\]

The row is the logarithmic-concavity expression

\[
R_\beta(T)
=
\log\frac{H_T(2)^2}{H_T(1)H_T(3)}.
\]

It belongs to the exact RH-valid cone although its two adjacent monotonicity rows contain less shape information.

## Strict synthetic separation from every adjacent two-point row

Use

\[
H(u)=\left(u-\frac43\right)^2(u+1)^4.
\]

At the three nodes,

\[
H(1)=\frac{16}{9},
\qquad
H(2)=36,
\qquad
H(3)=\frac{6400}{9}.
\]

Both adjacent ratios are strictly increasing:

\[
H(2)>H(1),
\qquad
H(3)>H(2).
\]

The raw three-point portfolio is also positive:

\[
R_\beta
=
\log\frac{6561}{6400}
\approx+0.0248450399971143.
\]

The factor \((u+1)^4\) models four certified critical-line zeros at squared distance \(y=1\). Their exact portfolio response is

\[
4\phi_\beta(1)=4\log\frac98.
\]

The rational lower cost \(1/10<\log(9/8)\) gives a safe count-dual subtraction \(2/5\). Therefore

\[
\boxed{
R_\beta-\frac25
< -0.3751549600028856.
}
\]

At the same time, the two adjacent count-deflated monotonicity rows remain strictly positive. X-9305 checks this using the safe costs

\[
\frac25<\log\frac32,
\qquad
\frac14<\log\frac43.
\]

Thus the multi-point portfolio detects a hidden synthetic off-line factor while every adjacent two-point witness remains positive, both before and after the same certified line-mass removal.

This is an exact synthetic control, not a Riemann-xi evaluation.

## Polyhedral discovery consequence

For fixed nodes, the constraints

\[
\sum_i\beta_i=0,
\qquad
p_k(\beta)\ge0
\]

are rational linear constraints. After fixing a normalization such as

\[
\sum_i|\beta_i|=1
\]

and freezing coefficient signs for interval contraction, candidate discovery over the direct-xi primitive table becomes a finite linear program. L-9305 count-dual variables may be included in the same optimization.

The solver remains outside the trust boundary. The final certificate contains only:

1. exact nodes and rational \(\beta\);
2. the recomputed polynomial coefficients;
3. exact directed modulus-square rectangles;
4. exact count atoms and windows;
5. one integer primal and rational dual;
6. a strict rational final interval.

## Existential completeness

The cone contains every two-point row \(\beta=(-1,+1)\), for which

\[
P_\beta(y)=v-u>0.
\]

Since the two-point direct-modulus criterion is existentially complete near every off-critical zero, enlarging to the resolvent-polynomial cone preserves existential completeness.

## Proof boundary

- The theorem depends on the direct completed-xi canonical product under RH.
- X-9305 implements only monomial-coefficient nonnegativity, not the optional Bernstein extension.
- Cell costs must be rigorous lower bounds for the frozen portfolio response.
- A synthetic negative is not a Riemann-xi candidate.
- A production negative requires independent direct-xi and count reproduction plus analytic review.

## Suggested next attack

Use the nine-point directed PR #103 primitive table and the first exact PR #104/PR #100 count table. Search the monomial-positive portfolio cone jointly with the L-9305 dual, freeze the best rational \(\beta\), and replay X-9305 before requesting any new Turing endpoints.
