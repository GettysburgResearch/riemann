# L-105271 — Analytic endpoint taper and regular-ordinate suppression

Claim ID: `L-105271`  
Status: **PROVED ABSTRACTLY; XI APPLICATION USES STANDARD FIXED-STRIP GROWTH AND ZERO COUNT**  
Created: 2026-08-24  
Depends on: Cauchy/Jensen/Cartan minimum modulus; standard fixed-strip Xi growth  
RH status: not assumed

This lemma records a useful interface that survives R-105270: vertical endpoint
pieces can be removed for a **carrier-free** contour field.  The lemma cannot
make a holomorphic carrier conclusion-facing.

## 1. Endpoint-killing polynomial

Let

\[
\Omega_{H,\eta}
=\{z:|\Re z|\le H,\ |\Im z|\le\eta\},
\qquad H\to\infty.
\]

Choose integers

\[
M=M(H)\to\infty,\qquad r=r(H)\to\infty
\]

with

\[
M\eta/H=o(1),\qquad rM\eta/H=o(1).
\tag{1}
\]

Define

\[
\boxed{
W_{H,M,r}(z)
=\left(1-(z/H)^{2M}\right)^r.
}
\tag{2}
\]

Its zeros are

\[
z=H\exp(\pi i j/M),\qquad 0\le j<2M.
\]

If

\[
H\sin(\pi/M)>\eta,
\tag{3}
\]

then the only zeros in the closed strip are the two real endpoint zeros
\(\pm H\); there are no zeros in the open rectangle.

On either vertical side, the elementary estimate

\[
|(1+u)^{2M}-1|
\le 2M|u|e^{2M|u|}
\]

gives, uniformly for \(|y|\le\eta\),

\[
\boxed{
|W_{H,M,r}(\pm H+iy)|
\le
\left(4M\eta/H\right)^r
}
\tag{4}
\]

for all sufficiently large \(H\).

## 2. Flatness on the horizontal bulk

Put

\[
\delta=\frac{3\log r}{M}.
\]

If \(|x|\le(1-\delta)H\) and \(|y|\le\eta\), then

\[
|(x+iy)/H|^{2M}\le r^{-4}
\]

for all sufficiently large \(H\), and therefore

\[
\boxed{
W_{H,M,r}(x+iy)=1+O(r^{-3}).
}
\tag{5}
\]

The exceptional horizontal collar has relative length

\[
O(\delta)=O(\log r/M)=o(1).
\tag{6}
\]

A second elementary split—bulk versus the two endpoint collars—shows

\[
\sup_{\Omega_{H,\eta}}|W_{H,M,r}|=1+o(1)
\tag{7}
\]

under (1).  On the real interval, \(0\le W\le1\) and its total variation is at
most two.

Thus multiplication by \(W\) changes a constant-diagonal Paley--Wiener frame
by `o(d)` in normalized trace and Hilbert--Schmidt statistics while suppressing
both vertical sides superpolynomially.

One concrete choice is

\[
M=\lceil(\log H)^2\rceil,
\qquad
r=\lceil A\log H\rceil,
\tag{8}
\]

with arbitrary fixed \(A>0\).  Then the right side of (4) is

\[
\exp\bigl(-A(\log H)^2+O(\log H\log\log H)\bigr).
\tag{9}
\]

## 3. Regular vertical ordinates

Let \(g\) be analytic on a fixed-thickness enlargement of a unit rectangle,
with

\[
\log\sup|g|\le C\log T
\]

and with one point in the enlargement satisfying

\[
\log|g(z_0)|\ge-C\log T.
\]

Jensen's formula gives \(O(\log T)\) zeros in the smaller rectangle.  Factoring
those zeros and applying the minimum-modulus/Cartan lemma yields an abscissa
\(x_T\) in the unit horizontal interval such that

\[
\boxed{
\inf_{|y|\le\eta}|g(x_T+iy)|
\ge
\exp[-C_\eta(\log T)^2].
}
\tag{10}
\]

For

\[
g(z)=e^{\pi z/4}\Xi'(z),
\]

standard Stirling bounds give the polynomial upper bound in every fixed strip,
and the right safe line gives the polynomial nonzero anchor.  Hence endpoints
may be chosen within \(O(1)\) of \(T\) and \(2T\) so that

\[
\boxed{
\sup_{|y|\le\eta}
\left|\frac{\Xi(x_T+iy)}{\Xi'(x_T+iy)}\right|
\le
\exp[C_\eta(\log T)^2].
}
\tag{11}
\]

Choosing \(A>C_\eta/2\) in (8), the squared taper in (4) dominates (11), every
fixed-strip Paley--Wiener growth factor, and every polynomial dimension factor.
Thus the vertical boundary trace norm of a carrier-free field is `o(d)`.

## 4. Boundary

Equation (11) is an endpoint selection theorem, not a zero-free-strip theorem.
R-105270 still forces the complementary boundary of a holomorphic carrier to
cancel its safe-line contribution exactly.  L-105271 is therefore usable only
after carrier renormalization or in a contour field whose carrier is owned by
an actual pole/index.
