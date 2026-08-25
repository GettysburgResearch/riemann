# Integral spectrum on the square-tower wavelet curve

Status: **PROVED**, conditional only on the source-locked algebraic equation
for the endpoint-three zero curve.  The replay uses integer arithmetic and
signed divisors.  It enumerates no finite field, curve, or L-function family.

Let \(q=s^2\), where \(s\geq3\) is odd, and write

\[
 P(u)=1+au+bu^2+s^2au^3+s^4u^4,
 \qquad P(u)^{-1}=\sum_{n\geq0}r(n)u^n.
\]

The square-tower packet proves that the native endpoint-three wavelet

\[
 W_3=r(3)-(1+s)r(2)+sr(1)
\]

vanishes precisely on

\[
 (2a+s+1)b
 =a\bigl(a^2+(s+1)a+s(s+1)\bigr).                 \tag{1}
\]

The present packet determines every integral coefficient point on (1),
then intersects that exact list with the compact \(USp(4)\) coefficient
region.  It also resolves the sign of the older minor

\[
 K=s^2a^2-b^2
\]

along the whole zero curve.

## 1. Signed-divisor parametrization

Put

\[
 t=2a+s+1,
 \qquad C_s=(s+1)^2(3s-1).
\]

The vertical value \(t=0\) is not a solution of (1): the upstream exact
certificate gives \(W_3=(s+1)^2(3s-1)/8>0\) there. For \(t\ne0\), direct
division gives

\[
 8b=t^2-(s+1)t+3s^2+2s-1-\frac{C_s}{t}.           \tag{2}
\]

Consequently every integral solution has \(t\mid C_s\). Conversely, every
signed divisor \(t\mid C_s\) satisfying

\[
 t\equiv s+1\pmod 2,
 \qquad
 t^2-(s+1)t+3s^2+2s-1-C_s/t\equiv0\pmod 8         \tag{3}
\]

gives exactly one integral solution

\[
 \boxed{
 a={t-s-1\over2},\qquad
 b={t^2-(s+1)t+3s^2+2s-1-C_s/t\over8}.}            \tag{4}
\]

Equations (3)--(4) are a bijection, not merely a search heuristic.  In
particular, the rational zero curve has at most \(2\tau(C_s)\) integral
coefficient points.  This is arithmetic sparsity on the coefficient
lattice; it is not a density statement for curves, because different
coefficient points can have very different family multiplicities.

## 2. Exact compact intersection

The reciprocal polynomial is compact-admissible exactly when its two
normalized quadratic parameters are real and lie in \([-2,2]\). In
coefficient coordinates this is

\[
 |a|\leq4s,
 \qquad
 2|a|s-2s^2\leq b,
 \qquad
 4b\leq a^2+8s^2.                                  \tag{5}
\]

Thus (3)--(5) give a finite exact classification for every odd square
field size. Once the divisors of \(C_s\) are available, exactly
\(2\tau(C_s)\) signed candidates are tested. The bounded replay below finds
those divisors by trial division, so divisor discovery itself takes
\(O(\sqrt{C_s})\) integer remainder tests; that separate cost is also metered.
The producer records six deliberately small arithmetic cross-sections:

| \(s\) | signed divisors tested | integral points | compact points |
|---:|---:|---:|---:|
| 3 | 16 | 6 | 5 |
| 5 | 48 | 12 | 7 |
| 7 | 36 | 16 | 10 |
| 9 | 48 | 12 | 4 |
| 11 | 60 | 30 | 15 |
| 13 | 48 | 12 | 4 |

The variation is genuinely arithmetic: \(s=9\) and \(s=13\) have only the
four universal \(K=0\) points below, whereas nearby \(s=11\) has eleven
additional compact integral points. No interpolation in \(s\) is used.

## 3. The minor becomes a chamber coordinate

On (1), exact factorization gives

\[
 \boxed{
 K={a^3(a+2s)(s-1-a)(a+s+1)\over(2a+s+1)^2}.}       \tag{6}
\]

The four distinct zero points are therefore

\[
 \boxed{
 (a,b)=(0,0),\ (s-1,s(s-1)),\ (-2s,2s^2),\
 (-s-1,s(s+1)).}                                    \tag{7}
\]

Away from the excluded vertical coordinate, the sign chambers are

| interval in \(a\) | sign of \(K\) |
|---|---:|
| \(a<-2s\) | \(-\) |
| \(-2s<a<-s-1\) | \(+\) |
| \(-s-1<a<0\) | \(-\) |
| \(0<a<s-1\) | \(+\) |
| \(a>s-1\) | \(-\) |

Thus the earlier minor does not vanish identically on the native-wavelet
zero curve.  It supplies an exact transverse chamber label, and its four
intersections are precisely the universal divisor parameters

\[
 t=\pm(s+1),\qquad t=\pm(3s-1).
\]

This is useful rare-event tomography: it distinguishes the universal
minor-zero skeleton from the additional square-tower wavelet zeros created
by the divisor arithmetic of \(C_s\).

## 4. Scope and replay

The compact inequalities assert only that a reciprocal polynomial has a
\(USp(4)\)-admissible spectrum. The packet does **not** assert that every
listed polynomial is realized by an abelian surface or a genus-two
Jacobian.  It makes no memberwise RH criterion, motive, compatible-system,
global Euler-product, or novelty claim.

From the repository root:

```text
python research/l-families/atlas/function_field/native_qadic_wavelet_square_integral_spectrum.py --check
python -O research/l-families/atlas/function_field/native_qadic_wavelet_square_integral_spectrum.py --check
python -m unittest tests.test_native_qadic_wavelet_square_integral_spectrum -v
python -O -m unittest tests.test_native_qadic_wavelet_square_integral_spectrum -v
```

The replay makes exactly 271 trial-division remainder tests and evaluates
exactly 256 signed divisors, under separate hard caps of 512 for each.
