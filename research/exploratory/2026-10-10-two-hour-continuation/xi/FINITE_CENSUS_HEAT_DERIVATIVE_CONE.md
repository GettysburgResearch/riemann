# A finite count-free census implies an infinite heat-derivative cone

Status: proposed complete analytic theorem with exact finite source guards.
Scope: actual Xi, all real u>=1 and all nonnegative integer derivative
orders r satisfying r<=u*5419^2/32. The whole source, unknown conjugate
blocks and all multiplicities remain in the heat trace. This cone leaves
many derivative/time pairs uncovered and does not establish RH.
Exact dependencies: the independently reviewed count-free complete real
census through 5419; one selected actual real root in (14,15); the complete
classical strip A=1/2; the actual-source upper count `N(T)<T*log T` for
T>=1024 from the previous wave's `heights/COARSE_ZERO_COUNT.md`; and HT1
and its absolutely convergent derivatives in
[COMPLETE_PRIME_HEAT_TRACE.md](COMPLETE_PRIME_HEAT_TRACE.md).
What was actually run: exact rational guards and frozen inherited source
hashes. This checker does not replay endpoint signs, a zero count, or the
infinitely many derivative/time values in the cone.
Smallest remaining gap: control every pair outside this cone from the
literal complete source. Finite real-head information alone cannot supply
the universal complete-monotonicity criterion.

## HD1. Whole-source decomposition and normalization

Let R>=1024 and suppose every actual source zero with positive real
coordinate gamma<=R is real. There is a known actual root gamma_* with
`l<gamma_*<b`, l>0. The multiplicity of that root is at least one;
simplicity is unnecessary for this implication. The complete heat trace
splits into the finite real head and all remaining gamma>R source zeros.
For every r>=0 and u>0,

\[
 (-1)^rK_{\rm head}^{(r)}(u)
     =\sum_{\gamma\le R}m_\gamma\gamma^{2r}e^{-\gamma^2u}
     \ge l^{2r}e^{-b^2u}>0.
 \tag{HD1}
\]

Under the classical strip |beta|<=A, the absolute whole tail derivative
satisfies

\[
 |K_{\rm tail}^{(r)}(u)|
    \le e^{A^2u}\sum_{\gamma>R}m_\rho
                  (\gamma^2+A^2)^r e^{-\gamma^2u}.
 \tag{HD2}
\]

The complete source upper count is `N(T)=sum_(0<gamma<=T)m_rho`. The
rotation s=1/2+i*z identifies this with the positive-ordinate count for xi
in the cited actual-source Jensen theorem. It counts off-real members and
multiplicities, not only the selected real roots. For T>=R it gives
`N(T)<T*log T<=T^2`.

## HD2. A complete Gaussian tail with exact endpoint accounting

For gamma>=R,

\[
 \frac{\gamma^2+A^2}{R^2+A^2}\le\frac{\gamma^2}{R^2},
 \qquad 2\log(\gamma/R)\le\gamma^2/R^2-1.
\]

Put v=u-r/R^2 and assume v>0. Then

\[
 (\gamma^2+A^2)^re^{-u\gamma^2}
      \le(R^2+A^2)^r e^{-r}e^{-v\gamma^2}.
 \tag{HD3}
\]

Stieltjes partial summation over the CLOSED head, so that only gamma>R
remains, gives

\[
 \begin{split}
 \sum_{\gamma>R}m_\rho e^{-v\gamma^2}
  &=-N(R)e^{-vR^2}+\int_R^\infty2vtN(t)e^{-vt^2}dt\\
  &\le\int_R^\infty2vt^3e^{-vt^2}dt
    =(R^2+1/v)e^{-vR^2}.
 \end{split}
 \tag{HD4}
\]

The negative endpoint is discarded in the safe direction. Infinite-endpoint
decay follows from the same complete source count. Thus HD2–HD4 imply

\[
 |K_{\rm tail}^{(r)}(u)|
      \le(R^2+A^2)^r(R^2+1/v)e^{-u(R^2-A^2)}.
 \tag{HD5}
\]

The factors `exp(-r)` and `exp(r)` have canceled exactly. This is a bound
on every remaining source occurrence, with no assumed real tail and no
truncated heat sum.

## HD3. The actual-Xi cone from the frozen count-free head

Set R=5419, A=1/2, l=14 and b=15. The known first selected sign interval
lies strictly in (14,15), so it supplies the actual gamma_* used in HD1.
The previously proved count-free census ensures the entire head is real.
For all u>=1 and integer `0<=r<=u*R^2/32`,

\[
 v\ge31u/32>0,\qquad R^2+1/v<R^2+2.
\]

The finite rational guards prove

\[
 \frac{R^2+1/4}{196}<(27/10)^{12}<e^{12},\qquad
 R^2+2<(27/10)^{18}<e^{18}.
 \tag{HD6}
\]

Here `e>sum_(j=0)^4 1/j!=65/24>27/10`; the remaining inequalities are
literal rational comparisons. Dividing HD5 by the head bound HD1 and
using HD6 gives a strict complete-source comparison

\[
 \begin{split}
 \log\frac{|K_{\rm tail}^{(r)}(u)|}{l^{2r}e^{-b^2u}}
 &<12r+18-u(R^2-1/4-225)\\
 &\le-u\left(\frac{5R^2}{8}-\frac{973}{4}\right)<0.
 \end{split}
 \tag{HD7}
\]

If the tail vanishes, the same strict conclusion follows directly without
taking its logarithm. The positive rational final constant is authenticated
by the checker. Consequently

\[
 (-1)^rK^{(r)}(u)>0
 \quad\text{for every real }u\ge1,
 \quad\text{every integer }0\le r\le u\,5419^2/32.
 \tag{HD8}
\]

At u=1 this includes every integer r<=917673. This finite-order number is
only a convenient slice of the infinite cone; monotonicity in u and the
proof above cover every real time in its stated domain, without enumerating
those times or derivatives.

## HD4. The remaining universal gap

Every fixed derivative order has a positive whole-source sign at all
sufficiently large times by HD8. This does not imply complete monotonicity:
HT7 requires EVERY r at EVERY u>0, including arbitrarily large r at one
fixed small or moderate u. The positive-Fourier late-lattice countermodel
also has eventual derivative signs for every fixed order while retaining
off-real poles. There is no cofinal zero-location conclusion here.

The inherited upper count is complete and derived from actual theta/Jensen;
the inherited real head is independently count-free. They play different
roles. A list of real sign changes with no head completeness would not
justify HD1–HD2's head/tail partition. A finite zero count with no full
tail upper estimate would not justify HD4. Neither input is silently
extended beyond its proved scope.
