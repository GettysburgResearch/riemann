# A full lower companion column from a complete real census

Status: proposed elementary analytic theorem, pending independent exact-source
review. It is a separate strengthening of the nonvanishing and real-boundary
statements in CENSUS_LOCALIZATION.md.
Scope: the positive even Fourier source, order below two, complete paired
product and complete zero-strip hypotheses in THEOREM.md, plus a complete
simple real census in a finite central range. Every source factor and every
zero multiplicity remains present. The theorem gives a finite real-part
column with unbounded lower depth, for every positive lambda and every fixed
derivative order with a positive displayed width. No RH claim is made.
Exact dependencies: [THEOREM.md](THEOREM.md) and
[CENSUS_LOCALIZATION.md](CENSUS_LOCALIZATION.md). Actual Xi additionally
uses the primitive census and imported complete-count qualifications in
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md).
What was actually run: the existing native replay proves 8,049 disjoint
critical-line sign changes through 8192; completeness retains its explicitly
imported FLINT historical finite-count contract. No new companion-zero census
or directed whole-column numerical run is claimed. The separate
[check_column_algebra.py](check_column_algebra.py) performs exact synthetic
polynomial controls of the complete root sums and three-coefficient identity;
its [receipt](column_algebra_controls.json) does not authenticate actual Xi
or the analytic whole-column conclusion.
Smallest remaining gap: independent review of this new analytic composition;
extension to unbounded real part remains outside the result.

## 1. Exact theorem

Let `F` satisfy (O1)--(O3) and the positive imaginary-axis moment identities
(O13)--(O16) in THEOREM.md. Suppose every zero is in `|Im z|<=A`, `A>=0`,
and a **complete** census proves every zero with `|Re z|<=R` is real and
simple. Fix an integer `r>=0` such that `C_(r+2)>0`, where

\[
C_j=R-jA,\qquad H_j=F^{(j)},\qquad
E_{r,\lambda}=H_r-i\lambda H_{r+1},\quad\lambda>0.
\tag{FC1}
\]

Then for every real `lambda>0`,

\[
\boxed{E_{r,\lambda}(z)\ne0,\quad E_{r,\lambda}'(z)\ne0,\quad
\operatorname{Re}\frac{iE_{r,\lambda}(z)}{E_{r,\lambda}'(z)}>0
\quad(z=T-iy,\ |T|<C_{r+2},\ y\ge0).}
\tag{FC2}
\]

The quantifiers are independent: there is no lower or upper bound on lambda,
and no order-dependent extra entry depth. The real-part range remains finite.
For `A=0`, the outer theorem already proves the interior `y>0`, and the
strict real-boundary result (L12) completes the assertion. Assume `A>0`
for the remaining proof.

## 2. Complete derivative product and localization inputs

Write `H=H_r`. The complete-product localization theorem gives:

* all zeros of `H_j` are in `|Im z|<=A`;
* every nonreal zero of `H_j` has `|Re z|>=C_j`;
* `H_j` is nonzero off the real axis in `|Re z|<C_j`;
* `Im(H_(j+1)/H_j)>0` in `|Re z|<C_(j+1)`, `Im z<0`;
* the real zeros of `H_j` in `|Re z|<C_j` are simple.

These are (L5)--(L8) and the induction preceding (L12), with all fixed
derivatives obtained from the complete product approximants. In particular,
on the claimed open lower column both `H,H'` are nonzero and

\[
\operatorname{Im}\frac{H'}H>0,\qquad
\operatorname{Im}\frac{H''}{H'}>0.
\tag{FC3}
\]

It is essential to account for the entire exponential factor. Each `H_j`
has order below two and parity `H_j(-z)=(-1)^j H_j(z)`. The positive source
moments give nonzero even `H_j(0)` and a simple zero at zero for odd `j`.
For `epsilon=0` or `1` according to the parity, write
`H_j(z)=z^epsilon G_j(z^2)`. The entire function `G_j` has order below one,
so its complete Hadamard factorization has genus zero and a **constant**
exponential factor. Consequently

\[
H_j(z)=c_jz^\epsilon
\prod_{\rho\in Z_+(H_j)}
\left(1-\frac{z^2}{\rho^2}\right)^{m_\rho},
\qquad\sum_{\rho\in Z_+(H_j)}\frac{m_\rho}{|\rho|^2}<\infty.
\tag{FC4}
\]

The product takes one representative of each `+/-` pair and complete
conjugate blocks. There is no missing linear or quadratic exponential.
The imaginary-axis source growth excludes a polynomial `H_j`: positive
source mass at some `t>0` gives exponential growth along `z=-iy`.
A finite zero set would make the displayed genus-zero product a polynomial,
so the complete zero set is infinite, in particular nonempty.
The paired logarithmic derivative converges locally normally away from the
zeros, and

\[
-\left(\frac{H_j'}{H_j}\right)'(z)
=\sum_{\rho\in Z(H_j)}\frac{m_\rho}{(z-\rho)^2}
\tag{FC5}
\]

converges locally absolutely. The zero at zero, when present, is included.
No `q'` contribution from an exponential is suppressed in (FC5).

## 3. The middle coefficient is positive on the protected slab

Let `z=x-iy` with `|x|<C_(r+2)` and `0<y<=A`, and put `q=H'/H`.
All nonreal zeros `rho=gamma+i eta` of `H` satisfy

\[
|x-\gamma|>C_r-C_{r+2}=2A
\ge|y+\eta|.
\tag{FC6}
\]

Thus each nonreal zero individually has

\[
\operatorname{Re}\frac1{(z-\rho)^2}
=\frac{(x-\gamma)^2-(y+\eta)^2}
       {[(x-\gamma)^2+(y+\eta)^2]^2}>0.
\tag{FC7}
\]

Separately, conjugate pairs of nonreal zeros have positive imaginary
logarithmic-derivative contribution by (L2), because
`|x-gamma|>2A>=|eta|`. A real zero `alpha`, of multiplicity `m_alpha`,
contributes `m_alpha*y/[(x-alpha)^2+y^2]>0`. These imaginary parts are
absolutely summable by (FC4), including the complete nonreal blocks.
Writing

\[
a_\alpha=\frac{y}{(x-\alpha)^2+y^2},
\tag{FC8}
\]

therefore gives

\[
\operatorname{Im}q\ge\sum_{\alpha\in Z(H)\cap\mathbb R}
m_\alpha a_\alpha\ge0,\qquad
(\operatorname{Im}q)^2
\ge\sum_{\alpha\in Z(H)\cap\mathbb R}m_\alpha a_\alpha^2.
\tag{FC9}
\]

For the second inequality, expand the square first for finitely many
nonnegative terms. Its diagonal terms are `m_alpha^2*a_alpha^2`, which
are at least `m_alpha*a_alpha^2` since multiplicities are positive integers;
all cross terms are nonnegative. Pass monotonically to the complete real
zero set. This does not assume simplicity outside the census range.

The complex Laguerre numerator has the exact normalized expression

\[
\frac{|H'|^2-\operatorname{Re}(H\overline{H''})}{|H|^2}
=|q|^2-\operatorname{Re}(q'+q^2)
=2(\operatorname{Im}q)^2-\operatorname{Re}q'.
\tag{FC10}
\]

Using (FC5), (FC7), and (FC9), this is at least

\[
\sum_{\alpha\in Z(H)\cap\mathbb R}
\frac{m_\alpha}{(x-\alpha)^2+y^2}
\;+
\sum_{\rho\in Z(H)\setminus\mathbb R}
m_\rho\operatorname{Re}\frac1{(z-\rho)^2}>0.
\tag{FC11}
\]

Indeed each real term combines
`2m*y^2/den^2 + m*((x-alpha)^2-y^2)/den^2 = m/den`.
Every nonreal term is strictly positive by (FC7), all displayed sums
converge, and the complete zero set is nonempty. If either part of the
zero set is empty, the other still supplies strict positivity. Thus

\[
|H'(z)|^2-\operatorname{Re}(H(z)\overline{H''(z)})>0
\quad(|x|<C_{r+2},\ 0<y\le A).
\tag{FC12}
\]

## 4. All three companion coefficients are positive

For `E=H-i lambda H'`, direct multiplication gives

\[
\begin{aligned}
\operatorname{Re}(iE\overline{E'})
={}&-\operatorname{Im}(H\overline{H'})\\
&+\lambda\,[|H'|^2-\operatorname{Re}(H\overline{H''})]\\
&-\lambda^2\operatorname{Im}(H'\overline{H''}).
\end{aligned}
\tag{FC13}
\]

The constant term equals `|H|^2*Im(H'/H)>0`, and the quadratic coefficient
equals `|H'|^2*Im(H''/H')>0`, by (FC3). The linear coefficient is positive
by (FC12). Therefore (FC13) is strictly positive for **every** `lambda>0`
on the whole protected slab `0<y<=A`. Both companions are nonzero there
by (L9)--(L10), and division by `|E'|^2` proves the strict sector.

For `y>A`, the all-order outer theorem gives the same strict conclusion
without restricting real part. At `y=0`, the complete census localization
and its simple-real-zero induction give both companions nonzero and the
strict sector (L12) on the larger interval `|x|<C_(r+1)`.
These domains meet directly, including `y=A`, and prove (FC2).

## 5. Source-qualified actual Xi corollary

Under the exact finite census through `R=8192` in the native certificate,
and the classical complete strip `A=1/2`, for every integer
`0<=r<=16381` and every real `lambda>0`,

\[
\boxed{\operatorname{Re}\frac{i[\Xi^{(r)}-i\lambda\Xi^{(r+1)}]}
 {\Xi^{(r+1)}-i\lambda\Xi^{(r+2)}}>0
\quad(z=T-iy,\ |T|<8192-(r+2)/2,\ y\ge0).}
\tag{FC14}
\]

Both numerator companion and denominator companion are nonzero there.
The upper bound on `r` records precisely when the finite real-part range
is positive; it is not an all-order finite-width claim. The outer theorem
continues to hold for every fixed order without that restriction.

The 8,049 directed native sign changes, saturated by the imported complete
FLINT count, prove the finite census premise at its stated historical-count
scope. No historical finite verification is independently reproduced here.
No higher derivative-zero census is supplied, and no statement extends
to unbounded real part. This finite column is compatible with nonreal zeros
outside it and has no RH implication.
