# Retain the primitive's mode-dependent energy in the Schur residual

Date: 2026-10-10. Conditional on the inherited operator/source-domain hypotheses
and the reviewed supporting lines, the following exact refinement avoids
charging every residual mode at the smallest primitive gap. The accompanying
directed moment computation is submitted for independent review.

## Weighted dual estimate

Suppose \(V\) removes \(m\) low sine moments and the three audited real
exponential moments. A proved global supporting line
\(P(x)V_2(\sqrt x)\ge\alpha x-C\) gives, before scalar Poincare,

\[
q(v,v)\ge b(\alpha\|\phi_v'\|_2^2-C\|\phi_v\|_2^2).
\tag{1}
\]

The nonnegative whole-source sinh tail can be dropped. Put \(g=\phi_v'\).
Its mean and first \(m\) cosine coefficients vanish. Expansion in the
orthonormal basis \(\sqrt2\cos(n\pi t)\) gives

\[
q(v,v)\ge b\sum_{n\ge m+1}\lambda_n|g_n|^2,\quad
\lambda_n=\alpha-\frac{C}{(n\pi)^2}>0.
\tag{2}
\]

Indeed \(\phi_v\) has the corresponding sine coefficients
\(g_n/(n\pi)\). Positivity of \(\lambda_{m+1}\) is a checked exact input.
The additional sinh constraint on \(g\) can be retained in a sharper dual
estimate, but can also be dropped safely here.

For any exact trials defining \(z_i\), let \(r_i=\Pi F_{z_i}\), where
\(\Pi\) is the original audited primitive-constraint projection. The coupling
is unchanged by this projection. Write
\(a_{ni}=\int_0^1r_i(t)\cos(n\pi t)dt\). Weighted Cauchy gives

\[
|q(v,z)|^2\le q(v,v)\ b\sum_{n\ge m+1}
 \frac{2|\sum_i a_{ni}z_i^{\rm coeff}|^2}{\lambda_n}.
\tag{3}
\]

For any finite \(N\ge m+1\), put \(t_N=1/\lambda_{N+1}\). Since the
inverse weights decrease with \(n\), Parseval implies the exact positive
matrix upper bound

\[
B_N=b\left[t_N R+2\sum_{n=m+1}^{N}
 (\lambda_n^{-1}-t_N)a_n^*a_n\right],\qquad
U-B_N\preceq S\preceq U.
\tag{4}
\]

Here \(R_{ij}=\langle r_i,r_j\rangle\). The complete remaining infinite
cosine tail is bounded by \(t_NR\) after subtracting the finite modes; it is
not truncated or assumed negligible. Every scalar multiplier in the finite
sum is positive. This improves the uniform cost
\(b\lambda_{m+1}^{-1}R\), and tends to charge high modes near \(b/\alpha\).
No inference of Fourier support from sine moments is made: the whole Fourier
supporting line is first integrated in(1), and the primitive's spatial sine
expansion is then used exactly.

For the dimension14 sector, use \(m=11,\alpha=13/10,C=710\).
For the phase-aware dimension8 sector, use \(m=5,\alpha=4/5,C=244\).
The latter's scalar residual coefficient27/2 is large; (4) pays that large
cost only near the first admitted primitive modes.

## Closed source moments without quadrature

Define \(T(\beta)=\int_0^1W(x)e^{\beta x}dx\) and
\(D(\eta,\beta)=\int_0^1e^{\eta t}K_\beta(t)dt\), with
\(K_\beta(t)=\int_0^1W(t-u)e^{\beta u}du\).
These are the exact complete Laplace/double transforms already derived and
reviewed in `CONTINUUM_RESIDUAL_DERIVATION.md`. In particular,
\(K_\beta(0)=T(\beta)\), \(K_\beta(1)=e^\beta T(-\beta)\).

Integration by parts, with \(F_\beta=-K_\beta'+c^2I_\beta\),
\(I_\beta(t)=\int_0^tK_\beta\), yields, for \(\nu=n\pi\),

\[
\int_0^1F_\beta(t)\cos(\nu t)dt
=T(\beta)-(-1)^n e^\beta T(-\beta)
 -(\nu+c^2/\nu)\frac{D(i\nu,\beta)-D(-i\nu,\beta)}{2i}.
\tag{5}
\]

The sine endpoint terms vanish exactly. For a nonzero real exponent
\(\eta\), the same argument gives

\[
\int_0^1F_\beta(t)e^{\eta t}dt
=T(\beta)-e^{\eta+\beta}T(-\beta)
 +(\eta-c^2/\eta)D(\eta,\beta)
 +\frac{c^2e^\eta}{\eta}D(0,\beta).
\tag{6}
\]

Subtracting(6) at \(\eta=b\) and \(\eta=-b\), and dividing by two,
provides the sinh moment. For the mean, let
\(D_\eta(0,\beta)=\partial_\eta D(\eta,\beta)|_{\eta=0}\). Then

\[
\int_0^1F_\beta=T(\beta)-e^\beta T(-\beta)
+c^2(D(0,\beta)-D_\eta(0,\beta)),
\]
\[
D_\eta(0,\beta)=
\frac{e^\beta\{T(0)+T(-\beta)-T'(0)\}-T'(0)-D(0,\beta)}{\beta}.
\tag{7}
\]

The source basis contains no \(\beta=0\), so(7) has no zero denominator.
Sine source moments are the imaginary parts at \(\beta=ij\pi\); the real
exponential and cosh moments follow by linearity. All are enclosed with the
same directed complete gamma-tail errors and source constants as the exactU.

Let \(P\) denote the original constraint basis
\(1,\cos(j\pi t)\ (1\le j\le m),\sinh(bt)\). If \(G_P\) is its exact
Gram matrix, and \(M_{ki}=\langle P_k,F_{z_i}\rangle\), then
\(r_i=F_{z_i}-\sum_k P_k(G_P^{-1}M)_{ki}\). For \(n>m\), orthogonality
of the constant and low cosines means only the sinh projection contributes:

\[
a_{ni}=\int F_{z_i}\cos(n\pi t)
 -\frac{b\{(-1)^n\cosh b-1\}}{b^2+n^2\pi^2}(G_P^{-1}M)_{s,i}.
\tag{8}
\]

Thus every moment in(4) has a complete analytic outward enclosure, without a
second cusp quadrature. The only genuinely continuous quadratic integral
remaining is the already enclosed \(R\). `analytic_source_moments.py`
implements(5)--(8); a subsequent directed LDL replay can apply(4) to a fullR
receipt. No sampled eigenvalue is used for acceptance.
