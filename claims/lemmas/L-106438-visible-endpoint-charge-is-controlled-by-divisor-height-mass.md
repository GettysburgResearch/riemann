# L-106438 — Visible endpoint charge is controlled by divisor height mass

Claim ID: `L-106438`  
Status: **PROVED EXACT FOR FINITE RATIONAL ENDPOINT SYMBOLS**  
Created: 2026-08-25  
Depends on: `L-106436--L-106437`  
RH status: **not assumed**

## 1. Inner-factor displacement norm

Let `B` be a finite upper-half-plane Blaschke product, normalized by
`B(infinity)=1`, with zeros `b_j=a_j+i y_j`, `y_j>0`.  Then

\[
\boxed{
\int_{\mathbb R}|1-B(t)|^2dt
 =4\pi\sum_j y_j.
}
\tag{L-106438.1}
\]

For one factor this is the elementary Cauchy-kernel integral.  For a product,
write

\[
1-B_1\cdots B_m
 =\sum_{j=1}^m
  B_1\cdots B_{j-1}(1-B_j).
\]

The summands lie in the mutually orthogonal model-space decomposition

\[
K_{B_1\cdots B_m}
 =K_{B_1}\oplus B_1K_{B_2}\oplus\cdots
  \oplus B_1\cdots B_{m-1}K_{B_m},
\]

which proves (L-106438.1).

## 2. Quotient displacement

Let

\[
U=B_+/B_-
\]

be a reduced finite all-pass quotient with both factors normalized at
infinity.  On the boundary,

\[
|U-1|=|B_+-B_-|.
\]

The Hilbert-space inequality `||x-y||^2<=2||x||^2+2||y||^2` and
(L-106438.1) give

\[
\boxed{
\int_{\mathbb R}|U(t)-1|^2dt
 \le8\pi
 \left(
  \sum_{B_+(b)=0}\operatorname{Im}b
  +\sum_{B_-(b)=0}\operatorname{Im}b
 \right).
}
\tag{L-106438.2}
\]

For `U=N/D` with `N=D^#` on the boundary, the two sums on the right are
exactly the total absolute imaginary height mass of the reduced denominator:
upper denominator zeros give `B_-`, while reflected lower denominator zeros
give `B_+`.  Hence

\[
\boxed{
\int_{\mathbb R}|U-1|^2
 \le8\pi\mathfrak h(D_{\rm red}).
}
\tag{L-106438.3}
\]

## 3. Hard-band visible charge

By `L-106436`,

\[
V_H^-(U)
 \le {H\over2\pi}\int_{\mathbb R}|U-1|^2dt.
\]

Combining with (L-106438.3) yields

\[
\boxed{
V_H^-(U)
 \le4H\mathfrak h(D_{\rm red}).
}
\tag{L-106438.4}
\]

For the endpoint denominator

\[
D=(p+i\lambda p')(p''-i\lambda p'''),
\]

`L-106437` gives the explicit source-free estimate

\[
\boxed{
V_H^-(U)
 \le8H\mathfrak h(p)+8\lambda H\deg p.
}
\tag{L-106438.5}
\]

This is an actual quotient-Hankel estimate, not a numerator-density proxy.

## 4. Slow-band corollary

Let `(p_T)` be a predeclared cofinal family of real-symmetric canonical-product
truncations of degree `n_T`.  If a predeclared bandwidth satisfies

\[
H_T\to\infty,
\qquad
{H_T\mathfrak h(p_T)\over n_T}\to0,
\qquad
\lambda_TH_T\to0,
\]

then

\[
\boxed{
V_{H_T}^-(U_T)=o(n_T).
}
\tag{L-106438.6}
\]

The companion winding is independent of the positive value of `lambda_T`, so
the last choice does not alter the finite endpoint index.  The signed
complement then carries the entire possible linear-scale obstruction.

## 5. Scope

The finite theorem is unconditional.  For Xi, one must pin a quantitative
zero-density input proving the required height-mass decay for the chosen
canonical truncation and verify the moving-window passage.  Even when the
visible term is `o(N)`, the signed tail may contain a positive linear number of
arbitrarily shallow adverse companion poles; therefore ninety percent is not
proved by this lemma.
