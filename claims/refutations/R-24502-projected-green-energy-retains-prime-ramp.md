# R-24502 — The projected Green-energy shortcut retains the exact prime-ramp scalar

Claim ID: `R-24502`  
Status: `REFUTATION / SCOPE BOUNDARY`  
Scope: endpoint-projected correction route  
Issue: #245

Let `G_X` and `lambda_q=Lambda(q)` be as in `L-24509`, and let

\[
r_X(q)=v_q(b_X^{(0)})-w_X(q)
\qquad(q\in\mathcal Q_X).
\tag{R-24502.1}
\]

A tempting closure is the Green-energy estimate

\[
r_X^{\!T}G_X^{-1}r_X\ll (\log X)^C.
\tag{R-24502.2}
\]

This would indeed be sufficient, but it is not a soft consequence of positive
definiteness.

## 1. Exact logarithmic coordinate

By `L-24501`,

\[
\boxed{
\lambda^{\!T}r_X
=J_X(b_X^{(0)})-S_X.
}
\tag{R-24502.3}
\]

Thus the projection of the residual onto the explicit logarithmic coordinate is
exactly the deficit in the RH-bearing prime ramp.

Since `G_X` is positive definite, Cauchy--Schwarz in the Green metric gives

\[
\boxed{
\bigl(J_X(b_X^{(0)})-S_X\bigr)^2
\le
\bigl(\lambda^{\!T}G_X\lambda\bigr)
\bigl(r_X^{\!T}G_X^{-1}r_X\bigr).
}
\tag{R-24502.4}
\]

The first factor is bounded absolutely by `L-24509.11`. Therefore any
polylogarithmic proof of (R-24502.2) already proves

\[
S_X\ge J_X(b_X^{(0)})-O((\log X)^{C/2}),
\]

and hence the desired prime-ramp theorem after the explicit seed estimate.

The Green-energy statement has compressed the final scalar; it has not removed
it.

## 2. Linear-programming dual firewall

The projected nonnegative correction problem is

\[
\begin{aligned}
\text{minimize }& (G_X\lambda)^TT,\\
\text{subject to }&G_XT\ge r_X,\\
&T\ge0.
\end{aligned}
\tag{R-24502.5}
\]

Its finite dual is

\[
\begin{aligned}
\text{maximize }&r_X^T\mu,\\
\text{subject to }&G_X\mu\le G_X\lambda,\\
&\mu\ge0.
\end{aligned}
\tag{R-24502.6}
\]

The vector

\[
\boxed{\mu=\lambda}
\]

is always dual-feasible, with objective exactly

\[
r_X^T\lambda=J_X(b_X^{(0)})-S_X.
\tag{R-24502.7}
\]

Consequently no generic dual-energy estimate can produce a strict contraction
of the logarithmic deficit: the complete RH-bearing coordinate is literally a
member of the dual feasible set.

## 3. What survives

The exact Dirichlet Gram remains useful:

1. it replaces the nonsymmetric primitive-neighbor ledger by a canonical finite
   energy;
2. it removes Jacobi convergence and `b_m>=0` as artificial proof obligations;
3. it separates the one logarithmic low-energy mode from the coercive additive
   complement;
4. it supplies a clean location for any genuinely new signed arithmetic input.

But a proof must still control the logarithmic coordinate by a source-specific
identity. Calling (R-24502.2) an ordinary frame bound would be circular.

## Status boundary

This refutes the projected-Gram construction as an automatic closure. It does
not refute the carry route or the possibility of proving the Green estimate by
a genuinely new arithmetic argument.
