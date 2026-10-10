# Complete-census localization under differentiation

Status: proposed elementary analytic transport, pending independent review.
Scope: the positive even source and complete paired product in THEOREM.md,
a complete zero strip, and a complete simple real-zero census in a finite
central range. All zero multiplicities and all remaining tail blocks are
retained. This gives wide finite regions of derivative and companion
nonvanishing, plus a real-axis sector for every positive lambda. It does
not assert the companion sector throughout the corresponding lower strip.

## 1. A conjugate-pair sign localizes the derivative

Let `Q` be a nonconstant real polynomial. Suppose every zero is in
`|Im z|<=A`, and every nonreal zero has `|Re z|>=C`, where `C>A>=0`.
For `z=x-i*y`, `y>0`, a real zero contributes

\[
\operatorname{Im}\frac1{z-\alpha}
 =\frac{y}{(x-\alpha)^2+y^2}>0.
\tag{L1}
\]

A nonreal conjugate pair `gamma +/- i*eta`, of equal multiplicities,
contributes

\[
\operatorname{Im}\left(\frac1{z-\gamma-i\eta}
                       +\frac1{z-\gamma+i\eta}\right)
=\frac{2y[(x-\gamma)^2+y^2-\eta^2]}
 {[(x-\gamma)^2+(y+\eta)^2][(x-\gamma)^2+(y-\eta)^2]}.
\tag{L2}
\]

If `|x|<C-A`, then `|x-gamma|>A>=|eta|`. Each contribution in (L1)--(L2)
is strictly positive. The polynomial has no zeros there, and consequently

\[
\operatorname{Im}\frac{Q'}Q>0
\quad\text{on } |\operatorname{Re}z|<C-A,\quad\operatorname{Im}z<0.
\tag{L3}
\]

Thus `Q'` has no zeros in that lower region. Real coefficients give the
same zero exclusion in the reflected upper region. Gauss--Lucas still
keeps every derivative zero in `|Im z|<=A`; all nonreal derivative zeros
therefore have `|Re z|>=C-A`. This is the elementary conjugate-pair form
of localization by the disks centered at `gamma` with radius `|eta|`.

## 2. Pass the localization through the complete native product

Let `F` satisfy the source, order and complete-strip hypotheses of
[THEOREM.md](THEOREM.md). In addition suppose a **complete** census proves
that every zero with `|Re z|<=R` is real and simple, where `R>A`.
Define

\[
C_r=R-rA,\qquad H_r=F^{(r)},\qquad
E_r=H_r-i\lambda H_{r+1},\quad\lambda>0.
\tag{L4}
\]

The complete even real product approximants have all nonreal zeros outside
`|Re z|<=R`. Their degrees tend to infinity. For every fixed integer `r`,
use approximants of degree greater than `r+1`. Repeatedly applying (L3)
and Gauss--Lucas gives

\[
\text{every nonreal zero of }P_n^{(r)}
\text{ has }|\operatorname{Re}z|\ge C_r,
\qquad |\operatorname{Im}z|\le A,
\tag{L5}
\]

whenever `C_r>0`. The limits and all fixed derivatives are locally uniform.
The positive imaginary-axis moments in (O5)--(O7) exclude an identically
zero limit. Hurwitz on each connected open half of the vertical strip gives

\[
H_r(z)\ne0\quad\text{if }C_r>0,
\quad |\operatorname{Re}z|<C_r,
\quad\operatorname{Im}z\ne0.
\tag{L6}
\]

Gauss--Lucas and Hurwitz also retain the complete strip for the derivative.
Thus the complete nonreal zero set of `H_r` obeys (L5), independently of
whether every real derivative zero has yet been located.

On the smaller connected lower region with `|Re z|<C_(r+1)`, polynomial
logarithmic derivatives converge to `H_(r+1)/H_r` and have positive
imaginary part. Their limit has nonnegative imaginary part. At `z=-i*y`,
the source moments give the strictly positive anchor

\[
\frac{H_{r+1}(-iy)}{H_r(-iy)}
 =i\frac{A_{r+1}(y)}{A_r(y)},\qquad y>0.
\tag{L7}
\]

The harmonic minimum principle therefore makes the sign strict:

\[
\operatorname{Im}\frac{H_{r+1}}{H_r}>0
\quad\text{on } |\operatorname{Re}z|<C_{r+1},\quad\operatorname{Im}z<0,
\tag{L8}
\]

provided `C_(r+1)>0`. In particular

\[
\operatorname{Re}(E_r/H_r)
 =1+\lambda\operatorname{Im}(H_{r+1}/H_r)>1.
\tag{L9}
\]

It follows for **every** `lambda>0` that `E_r` is nonzero in that lower
region. Since `E_r'=E_(r+1)`, both `E_r,E_r'` are nonzero on

\[
|\operatorname{Re}z|<C_{r+2},\qquad\operatorname{Im}z<0,
\qquad C_{r+2}>0.
\tag{L10}
\]

These conclusions need the complete census and complete strip. Sign
brackets without a complete total count would not justify (L5).

## 3. Real derivative zeros remain simple in the protected central range

Each `H_r` has order below two and parity `H_r(-z)=(-1)^r H_r(z)`.
As in (O2)--(O3), dividing an odd function by `z` and passing to `z^2`
gives a complete genus-zero paired product, with no omitted exponential
factor. The source moments at zero show that even `H_r(0)` is nonzero,
while an odd `H_r` has a simple zero at zero. The imaginary-axis growth
also excludes a constant or monomial as the entire function `H_r`.

At a real point `x` away from its zeros, the complete product gives the
locally absolutely convergent identity

\[
-\left(\frac{H_r'}{H_r}\right)'(x)
=\sum_{\alpha\in Z(H_r)\cap\mathbb R}\frac{m_\alpha}{(x-\alpha)^2}
 +\sum_{\substack{\gamma+i\eta\in Z(H_r)\\\eta>0}}
 \frac{2m_\rho[(x-\gamma)^2-\eta^2]}
      {[(x-\gamma)^2+\eta^2]^2}>0
\tag{L11}
\]

for `|x|<C_(r+1)`. Nonreal pairs have `|gamma|>=C_r` and `|eta|<=A`,
so every displayed summand is positive; at least one zero is present.

The simple-census premise starts induction at `r=0`. Suppose every real
zero of `H_(r-1)` in `|x|<C_(r-1)` is simple. A real zero of `H_r` with
`|x|<C_r` cannot also be a zero of `H_(r-1)`, because the latter would
then be simple. At that point the logarithmic derivative of `H_(r-1)`
vanishes, and (L11) gives
`H_r'(x)=H_(r-1)(x)*(H_r/H_(r-1))'(x) != 0`.
This proves by induction that every real zero of `H_r` in `|x|<C_r` is
simple.

Thus `E_r` and `E_r'` are both nonzero on the real interval
`|x|<C_(r+1)`. At a zero of `H_r`, the strict Laguerre numerator is
`H_r'^2>0`; elsewhere (L11) proves it is strictly positive. Therefore

\[
\operatorname{Re}\frac{iE_r(x)}{E_r'(x)}
=\frac{\lambda[H_r'(x)^2-H_r(x)H_r''(x)]}
       {H_r'(x)^2+\lambda^2 H_r''(x)^2}>0
\quad (|x|<C_{r+1}).
\tag{L12}
\]

The quotient is also well defined on the whole closed lower region
`|Re z|<C_(r+2)`, `Im z<=0`, with `C_(r+2)>0`.
Equations (L8) and (L12) do **not** by themselves prove its strict
sector for every interior point. That remains a separate transport task.

## 4. Source-qualified actual Xi consequence

Use the exact complete census through `R=8192` in
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md): all 8,049 disjoint
native Hardy-Z sign changes plus the explicitly imported FLINT3.6.0
historical complete-count contract prove all zeros through this height are
simple and on the critical line. The classical complete strip is `A=1/2`.
For every fixed integer `r>=0`, with the displayed range positive,

\[
\begin{aligned}
\Xi^{(r)}(z)&\ne0 && (|T|<8192-r/2,\ y>0),\\
E_r(z)&\ne0 && (|T|<8192-(r+1)/2,\ y>0),\\
E_r(z),E_r'(z)&\ne0 && (|T|<8192-(r+2)/2,\ y\ge0),\\
\operatorname{Re}(iE_r/E_r')&>0
 && (z=T\in\mathbb R,\ |T|<8192-(r+1)/2).
\end{aligned}
\tag{L13}
\]

Here `z=T-i*y` and `lambda>0` is arbitrary. The off-axis nonvanishing
assertion for the real derivative `Xi^(r)` also reflects to the upper
half-plane. The formula uses finite imported census completeness; the historical
count input has not been independently rerun. It proves neither a complete
new derivative-zero census nor a sector at unbounded `|T|`, and supplies
no RH conclusion.

Combining (L10) with the global outer theorem and the finite Gaussian slab
requires preserving their different domains and lambda/order scopes.
The wide denominator region is useful for further harmonic transport, but
it does not replace the strict full-domain sector predicate.
