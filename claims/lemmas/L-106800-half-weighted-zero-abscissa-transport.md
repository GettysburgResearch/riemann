# L-106800 — Half-weight, logarithmic phase, rough deletion and duplicate-67 filtering preserve the zero abscissa

Claim ID: `L-106800`  
Status: **PROVED FROM THE CLASSICAL MERTENS ZERO-ABSCISSA THEOREM AND EXACT FINITE TRANSFORMS**  
Created: 2026-08-27  
Depends on: `FFPS_SHARP_ROUGH_SINGLE_HARMONIC_NORMAL_FORM`; `FFPS_CRITICAL_BETA_SPECTRAL_WITNESS_PRINCIPLE`  
RH status: **not assumed**

## 1. Power exponent

For a nonnegative function \(F(X)\) of real \(X\ge2\), define

\[
\operatorname{pexp}F
=
\inf\left\{
\alpha\ge0:
F(X)\ll_\epsilon X^{\alpha+\epsilon}
\text{ for every }\epsilon>0
\right\}.
\tag{L-106800.1}
\]

For polynomially bounded \(F\), this is equivalently

\[
\operatorname{pexp}F
=
\limsup_{X\to\infty}
\frac{\log(1+F(X))}{\log X}.
\tag{L-106800.2}
\]

Multiplication by \(X^{o(1)}\) does not alter `pexp`; squaring doubles it.

Let

\[
\Theta
=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\tag{L-106800.3}
\]

The classical Mertens zero-abscissa theorem is

\[
\boxed{
\operatorname{pexp}
\max_{N\le X}\left|\sum_{n\le N}\mu(n)\right|
=
\Theta .
}
\tag{L-106800.4}
\]

Equivalently, for every \(1/2\le\sigma\le1\),

\[
\zeta(s)\ne0\quad(\Re s>\sigma)
\]

if and only if

\[
\max_{N\le X}|M(N)|
\ll_\epsilon X^{\sigma+\epsilon}
\qquad(\epsilon>0).
\tag{L-106800.5}
\]

The easy direction follows from

\[
\frac1{\zeta(s)}
=
s\int_1^\infty M(x)x^{-s-1}\,dx.
\]

The converse is the standard Perron/contour form of the same theorem.

## 2. Exact half-weight shift

Put

\[
A_N(0)=\sum_{n\le N}\frac{\mu(n)}{\sqrt n},
\qquad
\mathfrak M_0(X)=\max_{N\le X}|A_N(0)|.
\tag{L-106800.6}
\]

Abel summation in both directions gives

\[
A_N(0)
=
\frac{M(N)}{\sqrt N}
+
\frac12\int_1^N M(u)u^{-3/2}\,du,
\tag{L-106800.7}
\]

and

\[
M(N)
=
\sqrt N\,A_N(0)
-
\frac12\int_1^N A_u(0)u^{-1/2}\,du.
\tag{L-106800.8}
\]

Using arbitrary epsilon slack at the endpoint \(\Theta=1/2\), these two
identities imply

\[
\boxed{
\operatorname{pexp}\mathfrak M_0
=
\Theta-\frac12 .
}
\tag{L-106800.9}
\]

The right side is nonnegative because the functional equation gives
\(\Theta\ge1/2\).

## 3. One fixed guarded harmonic

For arbitrary complex coefficients \(c_n\), define

\[
F_N(t)=\sum_{n\le N}c_nn^{-it},
\qquad
\mathfrak F_t(X)=\max_{N\le X}|F_N(t)|.
\]

Discrete Abel summation and reverse demodulation give the exact inequality

\[
\frac{\mathfrak F_0(X)}{1+|t|\log X}
\le
\mathfrak F_t(X)
\le
(1+|t|\log X)\mathfrak F_0(X).
\tag{L-106800.10}
\]

Fix \(h\ne0\), a kernel order \(r\ge1\), and

\[
t_{h,X}=\frac{2\pi h}{L_X},
\qquad
L_X=\log X+S_{r,\infty}+\delta .
\tag{L-106800.11}
\]

Then \(1+|t_{h,X}|\log X=O_h(1)\), so

\[
\boxed{
\operatorname{pexp}
\max_{N\le X}
\left|
\sum_{n\le N}\frac{\mu(n)}{n^{1/2+it_{h,X}}}
\right|
=
\Theta-\frac12 .
}
\tag{L-106800.12}
\]

Thus every fixed nonzero guarded logarithmic harmonic records the complete
zero abscissa, not only the binary RH threshold.

## 4. Rough deletion and the exceptional source

Freeze a rough cutoff \(y_X\) at the outer horizon and assume

\[
y_X\to\infty,
\qquad
\limsup_{X\to\infty}
\frac{\log y_X}{\log\log X}\le2.
\tag{L-106800.13}
\]

Let \(P_X=\prod_{p\le y_X}p\) and

\[
\mathfrak A_{h}(X)
=
\max_{N\le X}
\left|
\sum_{\substack{n\le N\\(n,P_X)=1}}
\frac{\mu(n)}{n^{1/2+it_{h,X}}}
\right|.
\tag{L-106800.14}
\]

The exact rough-coordinate inequalities have conditioning masses

\[
C_{\rm sf}(X,y_X),\ C_{\rm sm}(X,y_X)=X^{o(1)}
\]

through precisely the range (L-106800.13). Hence

\[
\boxed{
\operatorname{pexp}\mathfrak A_h
=
\Theta-\frac12 .
}
\tag{L-106800.15}
\]

For

\[
\beta(n)
=
\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\]

and

\[
\mathfrak D_h(X)
=
\max_{N\le X}
\left|
\sum_{n\le N}\frac{\beta(n)}{n^{1/2+it_{h,X}}}
\right|,
\tag{L-106800.16}
\]

the terminating duplicate-67 filter and its geometric inverse cost only the
fixed constants \(1+67^{-1/2}\) and \((1-67^{-1/2})^{-1}\). Therefore

\[
\boxed{
\operatorname{pexp}\mathfrak D_h
=
\Theta-\frac12 .
}
\tag{L-106800.17}
\]

Every transformation in this lemma is source-faithful and invertible at
power-exponent scale.
