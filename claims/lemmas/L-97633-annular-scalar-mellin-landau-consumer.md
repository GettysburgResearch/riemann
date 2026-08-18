# L-97633 — Zero-safe annular scalar Mellin–Landau consumer

Claim ID: `L-97633`  
Status: **EXACT CONDITIONAL CONSUMER**

Define
\[
\mathcal A_X=
5\!\left[c_X(2)-c_{X/4}(2)\right]
+3\!\left[c_X(3)-c_{X/4}(3)\right].
\]
Its Mellin transform is
\[
\int_1^\infty \mathcal A_XX^{-s-1}\,dX
=(1-4^{-s})
\left[
\frac6{s^2}
-\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
\right],
\qquad z=s+\frac12.
\]
For `Re s>0`, `1-4^{-s}` is nonzero. For `Re z>0`,
\[
(1-2^{-z})(2-2^{-z})
\]
is nonzero. Hence no off-critical-line zeta zero can be cancelled by the finite
multipliers. If `A_X>=0` for all sufficiently large real `X`, Landau's
one-sign theorem excludes zeros with `Re rho>1/2`; the functional equation
supplies the reflected half-plane.
