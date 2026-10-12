# A complete local gamma integral enclosure without hypergeometric evaluation

This is a separate acceleration of the reviewed literal source. It changes no
kernel, trial, projection, Gaussian rule or continuum error theorem. The new
helper requires independent review. The frozen running producers remain
unchanged.

For (b=3/2), the reviewed literal gamma kernel is

\[
 \Gamma(x)=e^{-x/2}/6+\cosh(bx)\log(1+e^{-x})/3
                       +\sinh(bx)\log(1-e^{-x})/3.
\]

On the positive real axis write exactly

\[
 \Gamma(x)=A(x)+B(x)\log x,
\]

\[
 A(x)=e^{-x/2}/6+\cosh(bx)\log(1+e^{-x})/3
    +\sinh(bx)\log\big((1-e^{-x})/x\big)/3,
 \qquad B(x)=\sinh(bx)/3.                                  \tag{T1}
\]

Both (A) and (B) are analytic on a neighborhood of the closed unit disk,
with the logarithms continued from their positive values at zero. Indeed,
for \(|x|\leq1\),

\[
 \left|\frac{1-e^{-x}}x-1\right|\leq e-2<3/4,
 \qquad |(e^{-x}-1)/2|\leq(e-1)/2<7/8.
\]

The first quotient has its removable value one at zero. These disk bounds
exclude both zero and the logarithm cut for their normalized factors. The
elementary inequalities (e<11/4,e^{1/2}<2,e^{3/2}<5,
\log16<3,\log4<3/2) give

\[
 |A(x)|<8,\qquad |B(x)|<2\quad(|x|\leq1).                 \tag{T2}
\]

Let \(A_d,B_d\) retain coefficients of degrees zero through \(d\). Their
coefficients are computed by outward formal series arithmetic from (T1).
Cauchy's theorem gives, for real \(0\leq x\leq a\leq3/10\),

\[
 |A(x)-A_d(x)|\leq\frac{8x^{d+1}}{1-a},\qquad
 |B(x)-B_d(x)|\leq\frac{2x^{d+1}}{1-a}.                 \tag{T3}
\]

For a native exponential frequency \(z\in\{\pm1/2,\pm3/2,i j\pi\}\),
set \(E_{e,z}(x)=\sum_{k=0}^{e}(zx)^k/k!\) and

\[
 \delta_E=e^{|z|a}(|z|a)^{e+1}/(e+1)!.
\]

Taylor's absolute series remainder bounds the exponential error on the whole
integration path by \(\delta_E\). The helper requires \(\delta_E<1\).
Since \(|e^{zx}|\leq e^{(3/2)a}<2\), the polynomial exponential is bounded
by three. The literal gamma series has positive decreasing terms, so
\(0<\Gamma(x)\leq\Gamma(0)=1/6+\log2/3<2/5\).

The exact primitive of the polynomial/log product is evaluated using

\[
 \int_0^a x^k dx=\frac{a^{k+1}}{k+1},\quad
 \int_0^a x^k\log x\,dx=
  a^{k+1}\left(\frac{\log a}{k+1}-\frac1{(k+1)^2}\right).  \tag{T4}
\]

In particular it uses all product degrees through \(d+e\). The complete literal
incomplete gamma integral obeys the rigorous complex absolute error bound

\[
 \left|\int_0^a\Gamma(x)e^{zx}dx-
 \int_0^a[A_d(x)+B_d(x)\log x]E_{e,z}(x)dx\right|
 \leq\frac{3a^{d+2}}{1-a}
  \left[\frac8{d+2}+2\left(\frac{-\log a}{d+2}+\frac1{(d+2)^2}\right)\right]
             +\frac25 a\delta_E.                         \tag{T5}
\]

This follows by writing the product difference as the gamma error times the
polynomial exponential plus the exact gamma times the exponential error.
It integrates the entire omitted analytic and logarithmic tails. It is not
an ordinary Taylor approximation promoted to a certificate.

`taylor_convolution_source.py` adds a real/imaginary error rectangle whose
radius is an outward upper bound for (T5). It uses this route only when the
length is a strictly positive real Arb ball contained in \((0,3/10]\).
The chosen degrees are \((d,e)=(32,128)\) for \(a\leq1/100\), \((64,256)\)
for \(1/100<a\leq1/10\), and \((64,512)\) for \(1/10<a\leq3/10\).
The error bound is computed once at the upper cutoff of each tier and the
exponential remainder guard is checked there for each exact frequency. Both
terms in (T5) increase with \(a\): for the first term, writing \(p=d+2\),
the derivative of \(a^p[8/p+2/p^2-(2/p)\log a]\) has positive bracket
\(8-2\log a\); the additional factor \(1/(1-a)\) increases. The second
term increases directly. Thus that single cached radius covers the whole
tier, including arbitrarily small positive lengths. Real frequencies with
\(|\Re z|>3/2\) also use the unchanged fallback. Other
lengths retain the unchanged reviewed hypergeometric implementation.
Formal series operations explicitly raise `ctx.cap` to the required65/66
or \(d+e+1\) and check their returned precisions before reading coefficients;
the previous cap is restored. This is essential because the default series
cap is only10, even when a constructor requests a larger precision.

At the real Gaussian nodes the resulting source values remain outward balls
for exactly the same analytic functions. Therefore the earlier Cauchy/Gauss
integration error and endpoint source modulus remain valid without any new
analytic extension claim about this real-only evaluator.
