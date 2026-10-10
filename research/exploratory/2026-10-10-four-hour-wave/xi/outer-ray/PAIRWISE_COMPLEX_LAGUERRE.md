# A complete conjugate-pair complex Laguerre inequality

Status: proposed alternate analytic proof, pending independent review.
Scope: complete derivative products from the outer-ray source; nonreal zeros
with a protected horizontal gap. This strengthens the middle-coefficient
lemma in CENSUS_FULL_COLUMN_SECTOR.md to all nonreal depths. It does not
change that theorem's finite real-part range or imported census scope.
Exact dependencies: complete derivative product (FC4)--(FC5), nonempty zero
set, and derivative localization (L5)--(L8). No finite numerical evaluation
is promoted to a full-column assertion.
Smallest remaining gap: independent review of the new pairwise identity and
its infinite-product passage.

## 1. One real root and one conjugate pair

For a real root `alpha`, put `g(z)=z-alpha`. At `z=x-iy`, `y>0`, its
logarithmic derivative has positive imaginary part and

\[
2[\operatorname{Im}(g'/g)]^2
+\operatorname{Re}[-(g'/g)']
=\frac1{(x-\alpha)^2+y^2}>0.
\tag{PL1}
\]

For a nonreal conjugate pair `gamma +/- i eta`, put
`g(z)=(z-gamma)^2+eta^2`, `d=x-gamma`, and

\[
D=[d^2+(y+\eta)^2][d^2+(y-\eta)^2]=|g(x-iy)|^2.
\tag{PL2}
\]

Direct algebra gives

\[
\operatorname{Im}\frac{g'}g
=\frac{2y(d^2+y^2-\eta^2)}D,
\tag{PL3}
\]

and, since `g'=2(z-gamma)` and `g''=2`,

\[
2[\operatorname{Im}(g'/g)]^2
+\operatorname{Re}[-(g'/g)']
=\frac{|g'|^2-\operatorname{Re}(g\overline{g''})}{|g|^2}
=\frac{2(d^2+3y^2-\eta^2)}D.
\tag{PL4}
\]

Both quantities are strictly positive when `|d|>|eta|`, for **every**
`y>0`. Thus one complete conjugate pair supplies positivity without the
stronger individual-root separation `|d|>|y+eta|` used in (FC7).

## 2. Complete positive blocks and arbitrary multiplicities

At a protected point let `v_j=Im(g_j'/g_j)>0` for each real-root or
conjugate-pair block, and
`b_j=2v_j^2+Re[-(g_j'/g_j)']>0`. Give a block multiplicity `m_j>=1`.
For a finite complete block product `H`, its logarithmic derivative `q`
satisfies the exact identity

\[
2(\operatorname{Im}q)^2-\operatorname{Re}q'
=\sum_jm_jb_j
+2\sum_j(m_j^2-m_j)v_j^2
+4\sum_{j<k}m_jm_kv_jv_k
\ge\sum_jm_jb_j>0.
\tag{PL5}
\]

A real constant exponential in the canonical product has zero imaginary
logarithmic derivative and zero second logarithmic derivative, so does not
alter this identity. In the parity source (FC4) the exponential is constant
and even that linear term is absent.

For a complete infinite product, the imaginary logarithmic sums are
absolutely convergent, and `q'` is locally absolutely convergent by
`sum m/|rho|^2<infinity`. Pass through finite complete blocks: the first
positive block supplies a strict fixed positive lower bound, while the
complete derivatives converge. Equivalently, all additional terms in (PL5)
are nonnegative and the logarithmic sums converge. This proves

\[
|H'|^2-\operatorname{Re}(H\overline{H''})>0
\quad(y>0,\ |x-\operatorname{Re}\rho|>|\operatorname{Im}\rho|
\text{ for every nonreal zero }\rho).
\tag{PL6}
\]

There is no assertion of strictness at an arbitrary real multiple zero;
such a zero can make the unnormalized numerator vanish. The protected
simple-census real boundary is handled separately as in (L12).

## 3. Apply to the complete localized derivatives

For `H=F^(r)`, all nonreal zeros satisfy `|Re rho|>=C_r` and
`|Im rho|<=A`. Therefore (PL6) gives the strengthened middle-coefficient
statement

\[
|H'(z)|^2-\operatorname{Re}(H(z)\overline{H''(z)})>0
\quad(|\operatorname{Re}z|<C_{r+1},\ \operatorname{Im}z<0).
\tag{PL7}
\]

The complete zero set of every fixed derivative is nonempty by (FC4) and
the positive imaginary-axis source growth. In the smaller column
`|Re z|<C_(r+2)`, (FC3) makes the constant and quadratic companion
coefficients positive. Equation (PL7) makes the linear coefficient
positive at **every** lower depth. Thus (FC13) proves (FC2) directly on
`y>0`, without needing to divide the lower column into its finite slab and
outer part. The simple-census boundary (L12) completes `y>=0`.

This is an alternate proof of the already separately reviewed finite column.
The all-real-part outer theorem remains useful and is unchanged. The full
nonreal tail participates in every identity above; the argument does not
assume RH beyond the imported finite census.
