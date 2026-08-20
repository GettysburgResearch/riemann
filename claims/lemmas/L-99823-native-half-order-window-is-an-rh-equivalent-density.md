# L-99823 — The native half-order ratio-67 window is an exact RH-equivalent density

Claim ID: `L-99823`  
Status: **PROVED EXACT MELLIN/LANDAU EQUIVALENCE**  
Created: 2026-08-20  
Depends on: PR #653 `L-99270/L-99272`; `L-99821`  
RH status: **not assumed**

Define

\[
C_\beta(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n},
\qquad
D_{67}^{\beta}(x)=C_\beta(x)-C_\beta(x/67).
\]

For `Re(s)>1/2`, finite/absolute Fubini gives

\[
\boxed{
\int_1^\infty D_{67}^{\beta}(x)x^{-s-1}dx
=
\frac{(1-67^{-s})(1-67^{-(s+1/2)})}
{s\,\zeta(s+1/2)}.
}
\tag{L-99823.1}
\]

Both finite factors are nonzero in `Re(s)>0`. The right side is analytic at
every positive real `s`, including the removable point `s=1/2`, and every zeta
zero `rho` with `Re(rho)>1/2` gives a nonremovable pole at `s=rho-1/2`.

Write `D=D_+-D_-`. If

\[
\boxed{
\int_1^X D_-(x)\frac{dx}{x}=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0,
}
\tag{L-99823.2}
\]

then the Mellin transform of `D_-` is holomorphic in `Re(s)>0`. Hence the
transform of the nonnegative density `D_+` has every off-line pole in
(L-99823.1), while remaining analytic at all positive real points. The
specialized Landau theorem of PR #653 excludes this. Therefore

\[
\boxed{(L\text{-}99823.2)\Longrightarrow RH.}
\tag{L-99823.3}
\]

Conversely, RH gives the standard bound

\[
\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon}),
\]

and partial summation gives

\[
B_{1/2}(x)=O_\varepsilon(x^\varepsilon).
\]

Equation (L-99821.5) then gives `D_67^beta(x)=O_epsilon(x^epsilon)`, so
(L-99823.2) follows. Thus

\[
\boxed{
RH\iff
\int_1^X(D_{67}^{\beta}(x))_-\frac{dx}{x}=X^{o(1)}.
}
\tag{L-99823.4}
\]

This is the correctly normalized collar frontier. It is a sharper statement
of the remaining burden, not an unconditional proof of it.
