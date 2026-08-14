# L-92204 — Reciprocal Loewner–Hankel matrices are exactly congruent

Claim ID: `L-92204`  
Status: **PROVED EXACT FORMAL-POWER-SERIES CONGRUENCE**  
Created: 2026-08-14  
Depends on: elementary reciprocal power-series algebra; Heinävaara source lock  
RH status: **unproved**

## 1. Setup

Let `p` be a real analytic function with `p(t)>0` on an interval and put

\[
 Z(t)=\frac1{p(t)}.
\]

At a fixed point `t`, define the signed Taylor coefficients

\[
 \boxed{
 A_k(t)=\frac{(-1)^k}{k!}p^{(k)}(t),
 \qquad
 B_k(t)=\frac{(-1)^k}{k!}Z^{(k)}(t).
 }
\tag{L-92204.1}
\]

Then

\[
 P(z):=p(t-z)=\sum_{k\ge0}A_kz^k,
 \qquad
 Q(z):=Z(t-z)=\sum_{k\ge0}B_kz^k,
\]

and

\[
 P(z)Q(z)=1.
\]

For `n>=1`, define the adjacent Hankel matrix

\[
 \boxed{
 H_n(p;t)=\bigl(A_{i+j+1}(t)\bigr)_{0\le i,j<n}
 }
\tag{L-92204.2}
\]

and the confluent Loewner/Dobsch matrix

\[
 \boxed{
 M_n(Z;t)
 =\left(
 \frac{Z^{(i+j+1)}(t)}{(i+j+1)!}
 \right)_{0\le i,j<n}.
 }
\tag{L-92204.3}

## 2. Difference-quotient identity

The reciprocal relation gives

\[
\boxed{
 \frac{Q(z)-Q(w)}{z-w}
 =-Q(z)Q(w)
   \frac{P(z)-P(w)}{z-w}.
}
\tag{L-92204.4}
\]

The coefficient of `z^i w^j` in the last difference quotient of `P` is
`A_(i+j+1)`.  Let

\[
 T_n(Q)=igl(B_{i-j}\mathbf1_{i\ge j}\bigr)_{0\le i,j<n}
\]

be the lower-triangular Toeplitz matrix of the reciprocal coefficients, and
let

\[
 D_n=\operatorname{diag}(1,-1,1,-1,\ldots).
\]

Taking coefficients in (L-92204.4) gives the finite exact identity

\[
 \bigl(B_{i+j+1}\bigr)_{i,j<n}
 =-T_n(Q)H_n(p;t)T_n(Q)^T.
\tag{L-92204.5}

Since

\[
 \frac{Z^{(i+j+1)}(t)}{(i+j+1)!}
 =(-1)^{i+j+1}B_{i+j+1},
\]

we obtain

\[
\boxed{
 M_n(Z;t)
 =D_nT_n(Q)H_n(p;t)T_n(Q)^TD_n.
}
\tag{L-92204.6}

The triangular factor is invertible because

\[
 B_0=Z(t)=\frac1{p(t)}>0.
\]

Therefore the two matrices have exactly the same inertia:

\[
\boxed{
 M_n(Z;t)\succeq0
 \quad\Longleftrightarrow\quad
 H_n(p;t)\succeq0.
}
\tag{L-92204.7}

Their determinants satisfy

\[
\boxed{
 \det M_n(Z;t)
 =p(t)^{-2n}\det H_n(p;t).
}
\tag{L-92204.8
}

## 3. Squared-pole Cauchy–Binet formula

Suppose now that

\[
 p(t)=\sum_\alpha\frac{w_\alpha}{t+s_\alpha},
 \qquad w_\alpha>0,
\]

with a conjugation-invariant locally summable pole set.  Then

\[
 A_k(t)=\sum_\alpha
 \frac{w_\alpha}{(t+s_\alpha)^{k+1}}.
\]

For finite truncations, Cauchy–Binet gives

\[
\boxed{
\begin{aligned}
 \det H_n(p;t)
 =\sum_{\alpha_1<\cdots<\alpha_n}
 &\left(\prod_{j=1}^n w_{\alpha_j}\right)
 \frac{
  \prod_{1\le i<j\le n}
  (s_{\alpha_i}-s_{\alpha_j})^2
 }{
  \prod_{j=1}^n(t+s_{\alpha_j})^{2n}
 }.
\end{aligned}}
\tag{L-92204.9
}

Normal convergence passes the identity to the complete Xi squared-pole
system on every compact safe interval.

Under RH all `s_alpha` are positive real, so every term in (L-92204.9) is
nonnegative.  Off-line conjugate poles create signed Vandermonde terms.

## 4. Finite-order matrix monotonicity

By the published Dobsch–Donoghue–Heinävaara local characterisation, a smooth
function `Z` is matrix monotone of order `n` precisely when

\[
 M_n(Z;t)\succeq0
\]

throughout the interval.  Thus (L-92204.7) yields the exact equivalence

\[
\boxed{
 Z\text{ is }n\text{-monotone on }(1/4,\infty)
 \quad\Longleftrightarrow\quad
 H_n(p;t)\succeq0
 \text{ for every }t>1/4.
}
\tag{L-92204.10
}

For `n=1`, this is `A_1=-p'>=0`.  For `n=2`, it is the Schwarzian/Hankel
minor of `L-92202`.  For `n=3`, the sole new local determinant is

\[
\boxed{
 \det
 \begin{pmatrix}
 A_1&A_2&A_3\\
 A_2&A_3&A_4\\
 A_3&A_4&A_5
 \end{pmatrix}.
}
\tag{L-92204.11}

This is the first open matrix-order gate after `T-92201`.

## 5. Significance

The complete-Bernstein Xi programme is now an ordinary Stieltjes moment
problem in derivative coordinates:

```text
Loewner order n for Z
    =
adjacent n x n Hankel positivity for p
    =
positivity of a squared-pole Vandermonde sum.
```

No nonlinear reciprocal-derivative algebra remains at higher orders.

## 6. Exact boundary

```text
reciprocal Toeplitz congruence                 EXACT
inertia and determinant identity              EXACT
squared-pole Cauchy–Binet formula              EXACT FINITE / PROPOSED LIMIT
finite-order monotonicity reduction            PUBLISHED INPUT + EXACT
order two Xi monotonicity                      PROPOSED CLOSED
order three Xi monotonicity                    OPEN HANKEL DETERMINANT
all-order complete Bernstein                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVED
```
