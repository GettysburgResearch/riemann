# L-100301 — The summed activation deficit is the exact one-sided quadratic producer

Claim ID: `L-100301`  
Status: **PROVED CONDITIONAL CONCLUSION + CONVERSE**  
Created: 2026-08-20  
Depends on: `L-100300`; PRs #668, #672, #676, #679, #681  
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
\mathcal B(z)=\frac{1-67^{-z}}{\zeta(z)}.
\]

Let \(U(y)=4(\sqrt y-1)_+\), and define

\[
H_2(X)=\sum_n\frac{\beta(n)}{\sqrt n}U(X/n)^2,
\]

\[
C_2=16\mathcal B(3/2),\qquad \mathcal E_2(X)=C_2X-H_2(X).
\]

The exact Mellin transform, initially for \(\Re s>1\), is

\[
\boxed{
\mathcal M\mathcal E_2(s)
=\frac{C_2}{s-1}
-\frac{8(1-67^{-(s+1/2)})}{s(s-\frac12)(s-1)\zeta(s+\frac12)}.
}
\tag{L-100301.1}
\]

The residue at \(s=1\) cancels by the definition of \(C_2\); the apparent
point \(s=1/2\) is removable because \(1/\zeta(s+1/2)\) vanishes there. Every
zero \(\rho\) of \(\zeta\) with \(\Re\rho>1/2\) produces a nonremovable pole at
\(s=\rho-1/2\).

Define the exact activation-deficit condition

\[
\boxed{\mathrm{CATD}_{100300}:\qquad \mathfrak D(Y)=Y^{o(1)},}
\tag{L-100301.2}
\]

where \(\mathfrak D\) is the finite-cell sum in `L-100300`.

Since \(\mathfrak D(Y)=\int_1^Y(\mathcal E_2)_-\,dX/X\), the specialized
one-sided Mellin--Landau theorem gives

\[
\boxed{\mathrm{CATD}_{100300}\Longrightarrow RH.}
\tag{L-100301.3}
\]

Conversely, RH gives the standard Littlewood bound

\[
\sum_{n\le x}\beta(n)=O_\varepsilon(x^{1/2+\varepsilon}).
\]

Partial summation in the exact future-tail identity

\[
\mathcal E_2(X)=X\sum_{n>X}\frac{\beta(n)}{n^{3/2}}
+3X\int_X^\infty H_1(t)\frac{dt}{t^2}
\]

then yields \(\mathcal E_2(X)=O_\varepsilon(X^\varepsilon)\). Consequently

\[
\boxed{RH\Longrightarrow\mathrm{CATD}_{100300}.}
\tag{L-100301.4}
\]

Thus `CATD100300` is RH-equivalent. Its value is structural localization:
instead of a global pointwise sign, the remaining arithmetic is the sum of
explicit quadratic-cell deficit areas.
