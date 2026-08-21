# T-24503 — Green-energy parabolic carry proposal for RH

Claim ID: `T-24503`  
Status: `FULL PROPOSAL — one explicit Green-energy theorem open`  
Scope: full Riemann Hypothesis conditional on `GET`  
Issue: #245  
Depends on: `L-24501`, `L-24502`, `L-24508`, `L-24509`, the repository square-screw/Landau transfer

Define

\[
S_X=\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

Let `b_X^(0)` be the explicit parabolic seed of `L-24502`, let

\[
r_X(q)=v_q(b_X^{(0)})-q^{-1/2}\log(X/q),
\]

and let `G_X` be the endpoint-projected Dirichlet Gram of `L-24509`.

## Green-Energy Theorem (GET)

The sole new theorem in this proposal is

\[
\boxed{
\mathcal G_X:=r_X^TG_X^{-1}r_X
\le C\log^4(2X)
}
\tag{GET}
\]

for one absolute constant `C` and every integer `X>=2`.

The weaker subpower statement

\[
\mathcal G_X=X^{o(1)}
\tag{GET'}
\]

is enough for the rightmost-zero exponent argument.

## 1. GET gives the sharp prime ramp

By `L-24509`,

\[
S_X
\ge
J_X(b_X^{(0)})-\sqrt{6\mathcal G_X}.
\]

The explicit seed bound gives

\[
J_X(b_X^{(0)})
\ge4\sqrt X-6\log X+4-8X^{-1/2}.
\]

Therefore GET implies

\[
\boxed{
S_X\ge4\sqrt X-O(\log^2X).}
\tag{T-24503.1}
\]

Likewise GET' gives

\[
S_X\ge4\sqrt X-X^{o(1)}.
\tag{T-24503.2}
\]

## 2. Transfer to RH

The repository square-screw identity has the exact archimedean main term `4 sqrt(X)`. Either (T-24503.1), or the subpower form (T-24503.2), gives a subpower upper envelope for the negative square-screw channel. Landau continuation excludes every nontrivial zeta zero with real part greater than `1/2`; functional-equation symmetry gives

\[
\boxed{\mathrm{GET}\Longrightarrow\mathrm{RH}.}
\tag{T-24503.3}
\]

## 3. Variational form

Since `G_X>0`, the Green energy is equivalently

\[
\boxed{
\mathcal G_X
=
\sup_{T\ne0}
\frac{\left(\sum_{q\in\mathcal Q_X}r_X(q)T_q\right)^2}
{\sum_{j=0}^{X-1}
 \left(\sum_qT_q[f_q(j+1)-f_q(j)]\right)^2}.}
\tag{T-24503.4}
\]

Thus GET is one concrete finite inequality for additive prime-power functions. Writing

\[
A_T(j)=\sum_{q\mid j,\ q=p^a}T_q,
\]

the denominator is

\[
\sum_{j=0}^{X-1}
\left[
A_T(j+1)-A_T(j)-\frac{A_T(X)}X
ight]^2.
\tag{T-24503.5}
\]

The numerator is the pairing of the same prime-power coefficients with the explicit seed residual. There are no zeta zeros, contour integrals, operator domains, or limiting matrices in GET.

## 4. What has been removed

The Green formulation proves that the following are not necessary for this route:

- positivity of the original triangular carry inverse;
- positivity of the convexified coefficients `b_m`;
- a monotone divisibility cover, which is refuted by `R-24501`;
- convergence of the Jacobi PNC iteration;
- a separate endpoint-face enumeration.

The complete arithmetic burden is the one Hilbert-space scalar (GET).

## 5. Mandatory scalar firewall

Cauchy–Schwarz also gives the reverse lower bound

\[
\boxed{
\mathcal G_X
\ge
\frac{\left(J_X(b_X^{(0)})-S_X\right)^2}
{\lambda^TG_X\lambda}.}
\tag{T-24503.6}
\]

Since `lambda^T G_X lambda<=6`, a polynomial prime-ramp deficit forces polynomial Green energy. Thus GET genuinely retains the RH-bearing coherent scalar; it is not a generic matrix norm that can ignore the Mertens/prime-ramp firewall.

## 6. Proof attack requested

A proof of GET should proceed in the physical additive-function coordinates (T-24503.5). Promising interfaces are:

1. a shifted Turan–Kubilius inequality for `A_T(j+1)-A_T(j)`;
2. a Ramanujan/Farey diagonalization of the Dirichlet Gram with the endpoint projection retained;
3. an explicit low/high prime-power split using `L-24507` in the outer range;
4. a source-specific Selberg identity bounding the residual functional in the Dirichlet norm.

Any proof must retain the exact residual vector and may not replace it by rowwise absolute values.

## Status boundary

The deduction from GET to RH is complete. GET itself is not proved here. RH remains unproved.
