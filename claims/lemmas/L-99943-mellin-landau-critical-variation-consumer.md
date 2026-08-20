# L-99943 — Subpower critical negative mass implies RH

Claim ID: `L-99943`  
Status: **PROVED EXACT CONDITIONAL CONSUMER THEOREM**  
Created: 2026-08-20  
RH status: **not assumed; conclusion under the stated producer**

Put `h(x)=mathfrak H_1(x)`. For `Re(s)>1/2`, finite/absolute Fubini gives

\[
\boxed{
F(s):=\int_1^\infty h(x)x^{-s-1}\,dx
=\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-99943.1}
\]

Assume

\[
\boxed{
\int_1^Xh_-(x)\frac{dx}{x}=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{L-99943.2}
\]

Then

\[
N(s)=\int_1^\infty h_-(x)x^{-s-1}\,dx
\]

is holomorphic in `Re(s)>0`. On `Re(s)>1/2`,

\[
\int_1^\infty h_+(x)x^{-s-1}\,dx=F(s)+N(s).
\]

The left side is the Mellin transform of a nonnegative density. If its
abscissa of convergence is positive, Landau's theorem forces a singularity at
the corresponding positive real point; if the abscissa is nonpositive, the
transform is holomorphic throughout `Re(s)>0`. But the right side is analytic
at every positive real `s`: the apparent singularity at `s=1/2` is cancelled
by the pole of `zeta(1)`, and zeta has no real zero in `(1/2,1)`.

A hypothetical zero `rho` with `Re(rho)>1/2` would give a nonremovable pole at
`s=rho-1/2`, because

\[
1-67^{-\rho}\ne0.
\]

This contradicts the preceding Landau alternative. Hence no such zero exists;
functional-equation symmetry gives RH.
