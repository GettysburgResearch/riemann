# T-93280 - Positivity of two explicit large-prime rows gives a direct Mellin-Landau proof candidate for RH

Claim ID: `T-93280`  
Status: **PROPOSED COMPLETE CONDITIONAL CONSUMER; TWO-ROW POSITIVITY OPEN**  
Created: 2026-08-16  
Depends on: `L-93283`, `L-93284`; the fixed-row Mellin calculation of PR #542; Landau's theorem for Mellin transforms of nonnegative functions  
RH status: **unproved**

Assume `LPTRP_23`:

\[
c_X^{>3}(2)\ge0,
\qquad c_X^{>3}(3)\ge0
\qquad(X\ge1).
\tag{T-93280.1}
\]

Put `z=s+1/2`. Direct Mellin integration gives

\[
\boxed{
\begin{aligned}
\mathcal C_j^{>3}(s)
={}&\int_1^\infty c_X^{>3}(j)X^{-s-1}\,dX\\
={}&\frac{C_j}{s^2(1-2^{-z})(1-3^{-z})}\\
&+\frac{P_j(z)}
{s^2\zeta(z)(1-2^{-z})(1-3^{-z})},
\qquad j=2,3.
\end{aligned}
}
\tag{T-93280.2}
\]

The formula is initially valid in absolute convergence and supplies meromorphic
continuation. On every positive real `s`, zeta has no zero at `s+1/2`; its pole
at one becomes a zero of the reciprocal term. The finite Euler factors are
also nonzero. Hence both transforms are analytic at every positive real `s`.

Because the defining functions are nonnegative, Landau's abscissa theorem
forces both Mellin integrals to be holomorphic throughout `Re s>0`.

Suppose `zeta(rho)=0` with `Re rho>1/2`, and put `s_rho=rho-1/2`. By
`L-93283`, at least one of `P_2(rho),P_3(rho)` is nonzero. The corresponding
transform in (T-93280.2) then has a nonremovable pole at `s_rho`, contradicting
holomorphy of the defining Mellin integral. Functional-equation symmetry gives
RH.

Therefore

\[
\boxed{\mathrm{LPTRP}_{23}\Longrightarrow\mathrm{RH}.}
\tag{T-93280.3}
\]

This consumer uses only two rows and primes greater than three. It imports no
endpoint benchmark, factor-67 compiler, Target-Lorenz theorem, CPBD estimate,
Mertens square-root bound, or power-saving PNT error.

The conclusion-producing producer `LPTRP_23` remains open. This theorem must not
be cited as an unconditional proof before that allocation is independently
proved.
