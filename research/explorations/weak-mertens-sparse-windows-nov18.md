# Weak Mertens from arbitrarily sparse physical windows

Let $g(u)=e^{-u/2}M(e^u)$ for $u\ge0$. The weak Mertens hypothesis is
$\int_0^R |g(u)|^2du=O(R)$. For any fixed $d>1/2$ define
$$
 p_{n,d}(u)=2d e^{-2du}\frac{(2du)^{2n}}{(2n)!},\qquad
 W_{n,d}=\int_0^\infty p_{n,d}(u)|g(u)|^2du .
$$
Each probability density has mean $(2n+1)/(2d)$ and standard deviation
$\sqrt{2n+1}/(2d)$. The following implications use the proposed weak
Mertens converse and mean-square asymptotic in
[the trace note, equations (5)–(6)](trace-weak-mertens-nov18.md).
$$
 {\rm WMH}\ \Longleftrightarrow\
 \liminf_{n\to\infty} W_{n,d}<\infty
 \ \Longleftrightarrow\
 \liminf_{R\to\infty}
 \frac1{(b-a)R}\int_{aR}^{bR}|g(u)|^2du<\infty
 \quad(0<a<b\ {\rm fixed}).
 \tag{1}
$$
Thus under failure of weak Mertens each normalized expression tends to
infinity. Under weak Mertens the annular means tend to
$B=\sum_\rho|\rho\zeta'(\rho)|^{-2}$, while $W_{n,d}$ has liminf $B$,
Cesàro mean $B$, and tends to $B$ in natural density. The annular
integrals are precisely $\int_{e^{aR}}^{e^{bR}} M(x)^2x^{-2}dx$.
There is no restriction on the gaps between the tested scales. These
are implications about the original summatory Möbius function, without a
bound on its actual window values at unbounded scales.

## A single localized gamma norm bounds all critical reciprocal residues

Set $s_*=1/2+d$, $G(s)=1/(s\zeta(s))$, and
$A_{n,d}=(2n)!/((n!)^2(2d)^{2n+1})$. Absolute convergence at $s_*$
gives the Laplace transform of $g$. Differentiation and Plancherel give
$$
 W_{n,d}=\frac1{2\pi A_{n,d}}\int_\mathbb R
 \left|G^{(n)}(s_*+it)/n!\right|^2dt .
 \tag{2}
$$
If RH fails, some zeta zero is at distance less than $d$ from $s_*+it$
on a bounded interval of $t$. A finite set of poles competes there; the
pole at zero and the trivial zeros are farther away. Distinct poles have
equal distances only at isolated points on the vertical line of centers,
as the difference of squared distances is affine in $t$ and all poles
lie strictly to its left. On a closed subinterval of positive length
there is a unique nearest pole, separated by a common Cauchy circle from
every other pole and at distance bounded by a fixed $q<d$. If its order
is $m$, the leading Laurent coefficient contributes a nonzero constant
times $\binom{n+m-1}{m-1}(s_*+it-\rho)^{-n-m}$. Lower Laurent terms are
uniformly smaller by $O(1/n)$ relative to this term. The holomorphic
remainder is uniformly exponentially smaller by Cauchy. Since
$A_{n,d}\asymp_d d^{-2n}/\sqrt n$, (2) then tends to infinity
exponentially in $n$.

Under RH choose any finite set of distinct zeros. On a sufficiently small
closed interval about each selected ordinate, isolate its principal part
on a common Cauchy circle as above, taking the intervals disjoint. For a
simple zero, the $n$th Taylor coefficient in absolute value near the
ordinate is
$|1/(\rho\zeta'(\rho))|\,|d+i(t-\gamma)|^{-n-1}$ up to the uniform
exponentially smaller remainder. The integral of the squared kernel
over all $t$ is exactly $2\pi A_{n,d}$ by Plancherel. Its fraction outside
that fixed neighborhood tends exponentially to zero. A pole of order
$m>1$ instead contributes at least a constant times $n^{2m-2}$ to the
normalized integral there by integrating over $|t-\gamma|\le d/\sqrt n$.
It follows that boundedness of any subsequence forces RH, simplicity,
and $B<\infty$ by including arbitrarily many disjoint neighborhoods.
In the simple case the lower liminf is at least $B$, possibly infinite.
The cited converse now gives weak Mertens.

## Means over orders and localized physical intervals

Under weak Mertens the cited trace result gives
$L(R)=\int_0^R|g(u)|^2du\sim BR$. For $0<r<1$ one has exactly
$$
 \sum_{n\ge0}r^n p_{n,d}(u)
 =d\big[e^{-2d(1-\sqrt r)u}+e^{-2d(1+\sqrt r)u}\big].
$$
Together with $\int e^{-\eta u}dL(u)\sim B/\eta$ as $\eta\downarrow0$
this gives $(1-r)\sum r^n W_{n,d}\to B$. The nonnegative-coefficient
Hardy–Littlewood–Karamata Tauberian theorem gives
$N^{-1}\sum_{n<N}W_{n,d}\to B$. Combined with the lower liminf already
proved, this gives liminf $B$ and convergence in natural density.
Also $(L(bR)-L(aR))/((b-a)R)\to B$.

Conversely suppose the annular expression is bounded on a sequence.
Choose $a<a'<b'<b$ and retain every $n$ with $a'R\le n/d\le b'R$.
Take $d$ sufficiently large, depending only on these four endpoints.
Uniformly in these $n$, the portion of $W_{n,d}$ outside $[aR,bR]$
is exponentially small. Indeed $|g(u)|^2\le e^u$ unconditionally.
Tilting $p_{n,d}$ by $e^u$ gives
$(2d/(2d-1))^{2n+1}$ times the gamma law of shape $2n+1$ and rate
$2d-1$. Its mean stays strictly inside $[aR,bR]$, with relative margin
bounded below independent of all large $d$. The two gamma tails are
at most $\exp(-c n)$ by the exponential Markov inequality, where $c>0$
depends only on the relative margins. The prefactor costs $\exp(O(n/d))$.
Choosing $d$ sufficiently large proves the assertion. On the annulus
$\sum_np_{n,d}(u)=d(1+e^{-4du})\le2d$. There are $\asymp dR$ retained
orders, so some $W_{n,d}$ is bounded by an absolute multiple (depending
on $a,b,a',b'$) of the tested annular mean plus an exponentially small
error. These orders tend to infinity, and (2) proves weak Mertens.

## Compact windows of width only a power of a double logarithm

For the explicit choice $w(R)=(\log\log R)^3$, at large $R$ one has
$$
 {\rm WMH}\quad\Longleftrightarrow\quad
 \liminf_{R\to\infty}\frac1{w(R)}\int_R^{R+w(R)}
                 |g(u)|^2du<\infty .                                      \tag{3}
$$
On weak Mertens this lower limit equals $B$, with convergence to $B$
in density on dyadic $R$-intervals. Under failure the tested means tend
to infinity. The lower-bound argument works with any width satisfying
$w(R)/(\log\log R)^2\to\infty$ and $w(R)=o(R)$.
The explicit window in (3) tests ordinary $x$ from $X=e^R$ through
$X\exp((\log\log\log X)^3)$.

If RH fails, an off-line zero forces
$\|g\|_{L^2(Y,Y+w_0)}\gg e^{cY}$ on every sufficiently large interval
of some fixed length $w_0$. For completeness use the compact test
in [the isolated-zero construction](causal-isolated-zero-nov18.md) on
$G(1/2+z)=1/((1/2+z)\zeta(1/2+z))$. Choose a separating line to the
right of $1/2$ and to the left of the selected zero. Ingham's
sublinear count permits a genus-zero factor removing each competing
pole there and enough copies to leave the target simple. The compact
Gevrey multiplier dominates the $\exp(O(\log^2|t|))$ reciprocal-zeta
bound on the separated contour. The surviving convolution is a nonzero
multiple of $e^{(\rho-1/2)Y}$ plus an exponentially smaller remainder.
Cauchy–Schwarz on the test support gives the asserted fixed-window bound.
It implies divergence in (3) since $w=o(R)$.

Assume RH for the rest of the argument, allowing multiple zeros.
We use the following standard consequences of the zeta partial fractions.
For $R\ge3$ and $\epsilon=1/R$,
$$
 |G(1/2+\epsilon+it)|\le
 \exp(C\log(2+|t|)\log(2+R)).                                          \tag{4}
$$
Indeed integrate the local logarithmic-derivative formula horizontally
from $2+it$, where the Euler product is bounded above and below.
The $O(\log(2+|t|))$ nearby zero terms each have a log-modulus loss
$O(\log(2+R))$ by RH. The pole at one is harmless for this upper
bound on the reciprocal; bounded ordinates are also handled by compactness
and their finite Laurent expansions. The same argument by the local
log derivative, or its disk Blaschke version, bounds $|G|$ by
$\exp(O(\log V\log\log V))$ on horizontals of height $\asymp V$
separated in ordinate from every zero by $c/\log V$, over
$1/4\le\Re s\le1/2+\epsilon$. The path can cross the critical line
because of the ordinate separation. On $\Re s=1/4$, the functional
equation and the corresponding right-half-plane bound on $\Re s=3/4$
give $|G|\ll(2+|t|)^C$.

Fix one critical ordinate $\gamma$. Write $V=(\log R)^4$ and choose
$T\in[V,V+1]$ at distance $\gg1/\log V$ from every ordinate, by the
unit-interval zero count. Symmetry supplies the same separation at $-T$.
The following positive probability measure $\nu_{\gamma,R}$ is supported
on $[0,w]$. For every other distinct $\gamma'$ with $|\gamma'|\le T$,
convolve $m_{\gamma'}$ copies of
$$
 \tfrac12(\delta_0+\delta_h),\qquad h=\pi/|\gamma'-\gamma|.
$$
Its exponential transform vanishes at $i(\gamma'-\gamma)$, with at least
the required multiplicity after convolution. The total support length is
$O_\gamma((\log(2+V))^2)$ by partial summation of the zero count; the
finitely many ordinates near the fixed target cost a fixed constant.
Next convolve $k=\lceil C_1\log R\rceil$ uniform probability measures
on $[0,V^{-1/2}]$ with a sufficiently large absolute $C_1$. The added
support length tends to zero. Call the combined length $S=o(w)$.
Finally convolve with a uniform probability on $[0,w-S]$. Its density
$p_{\gamma,R}$ is at most $1/(w-S)$ everywhere, equal to $1/(w-S)$
on $[S,w-S]$ for all large $R$. Consequently
$$
 \|wp_{\gamma,R}-1\|_{L^2([0,w],dv/w)}=o(1).
 \tag{5}
$$
Write $L(z)=\int e^{zv}d\nu_{\gamma,R}(v)$. Throughout
$-1/4\le\Re z\le\epsilon$, all factors together cost at most $e^{\epsilon w}$
in absolute value, and for $|\Im z|\ge V/2$ there is the stronger bound
$$
 |L(z)|\le e^{\epsilon w}|\Im z|^{-k/3}.
$$
Indeed each of the $k$ short uniforms costs at most
$3\sqrt V/|\Im z|\le|\Im z|^{-1/3}$ there, for all sufficiently large $V$;
the remaining factors cost at most $e^{\epsilon w}$.

The linear statistic of interest is
$$
 \int g(R+v)e^{-i\gamma(R+v)}p_{\gamma,R}(v)\,dv
 =\frac1{2\pi i}\int_{\Re z=\epsilon}
 G(1/2+z)e^{(z-i\gamma)R}L(z-i\gamma)\,dz .                             \tag{6}
$$
Laplace Plancherel on the positive line gives this inversion: under RH
$g(u)\ll_\eta e^{\eta u}$ for every $\eta>0$, and the test has a compact,
bounded density. The integral also converges absolutely by (4) and the
short-uniform factors. The portions with $|\Im z|\ge T$ are $o(1)$ since
$C_1$ can be chosen to dominate (4) by an arbitrarily large fixed
multiple in its exponent. Shift the truncated line to $\Re z=-1/4$.
The horizontal sides are $o(1)$ by the separated bound, $e^{\Re zR}\le e$
and the same short-uniform decay. The left side is
$O(e^{-R/4}(2+V)^{C+1})=o(1)$. The factors in $L$ kill every intervening
pole except the target, and $L(0)=1$.

For a simple target the residue is exactly
$c_\gamma=1/(\rho\zeta'(\rho))$. For multiplicity $m>1$ the leading
Laurent coefficient $c_{\gamma,m}\ne0$ contributes
$c_{\gamma,m}\int(R+v)^{m-1}d\nu(v)/(m-1)!$
and the lower Laurent terms cost $O_\gamma((R+w)^{m-2})$.
Thus a multiple zero forces the modulus of (6) to grow at least as a
positive constant times $R^{m-1}$. Cauchy–Schwarz and (5) then force
the short-window squared means to diverge.

For a finite list of simple ordinates, regard the left sides in (6)
as inner products in $L^2([0,w],dv/w)$ with the corresponding rows
$w p_{\gamma,R}(v)e^{i\gamma(R+v)}$. By (5) these rows differ by
$o(1)$ in norm from the unit exponentials. Their finite Gram matrix
tends to the identity since $w\to\infty$. Bessel's inequality with
the largest Gram eigenvalue therefore gives lower liminf at least
$\sum_\gamma |c_\gamma|^2$ for this finite list. Increasing the list
proves the full lower bound $B$, including $B=\infty$. Together with
the cited converse this proves that the cofinal bound in (3) implies WMH.

Finally, on WMH and for the explicit $w(R)$ above, the mean over
$Y\le R\le2Y$ of the left side of (3) tends to $B$. To check this
use Tonelli, $w(R)/w(Y)\to1$ uniformly on that dyadic interval,
and $\int_0^Z g^2\sim BZ$. The two endpoint strips of length
$O(w(Y))=o(Y)$ have $g^2$-mass $o(Y)$ by the same asymptotic;
away from them the integrated window weights are $1+o(1)$.
The established lower liminf then gives the asserted convergence in
density and exact liminf. No upper bound on individual short windows
is asserted.

## Theta truncation reduces the required width to a single double logarithm

In (3) one may take the smaller explicit width
$w=(\log\log R)(\log\log\log R)$, or any
$w/\log\log R\to\infty$, $w=o(R)$ for the lower assertion. This uses the
actual theta kernel of completed zeta in place of the rank-by-rank factors.
The physical interval in $x$ for the explicit width extends from $X$ to
$X\exp((\log\log\log X)(\log\log\log\log X))$.

Here are the replacement tests in (6). Assume RH, fix the target
$\rho=1/2+i\gamma$ of order $m$, and put $c=\xi^{(m)}(\rho)/m!\ne0$.
In the demodulated variable $z$ use the exact transform
$$
 K(z)=\frac{\xi(\rho+z)}{cz^m},\qquad K(0)=1 .
$$
The classical theta representation $\xi(1/2+s)=\int\Phi(v)e^{sv}dv$
has even density $\Phi(v)\ll\exp(-c_0e^{2|v|})$ for some $c_0>0$;
see [the theta source and its tails](weil-contour-nov18.md).
Hence $K$ is the bilateral exponential transform of a fixed complex
density $k_\gamma(v)$ with
$|k_\gamma(v)|\ll_\gamma\exp(-c_1e^{2|v|})$ and $\int k_\gamma=1$.
Indeed integrate $e^{i\gamma v}\Phi(v)$ successively $m$ times from
$-\infty$ to $v$, inserting a factor $-1$ each time. All moments of
degrees $<m$ vanish by the order of $\xi$ at $\rho$, so on the positive
tail each primitive can instead be written as the corresponding tail
integral from $v$ to infinity. Polynomial factors are absorbed by
decreasing $c_1$.

Put $L=\log\log R$, $V=(\log R)^4$ and truncate $k_\gamma$ at
$|v|\le L$, renormalizing to integral one. Write $K_L$ for its transform.
Uniformly in $-1/4\le\Re z\le1/R$ and all imaginary parts,
$$
 |K_L(z)-K(z)|\ll_\gamma \exp(-c_2e^{2L}).
$$
This follows from the absolute exponential moments of the discarded
tails, including the negligible change from renormalization.
Translate the truncated density by $L$, placing its support in $[0,2L]$;
the resulting transform is $e^{Lz}K_L(z)$. Convolve with the $k=\lceil
C_1\log R\rceil$ uniform measures of width $V^{-1/2}$ used above and
one long uniform to bring total support to $[0,w]$. Denote the transform
of the two kinds of uniforms together by $U(z)$. The truncated density
has total variation $O_\gamma(1)$ uniformly in $R$, while the preliminary
support length is $S=2L+k/\sqrt V=o(w)$. The final complex density still
satisfies (5): it equals $1/(w-S)$ on the central interval and its
absolute value everywhere is at most $O_\gamma(1)/(w-S)$.

Apply (6) in the demodulated variable on $\Re z=1/R$. Replacing $K_L$
by $K$ costs $o(1)$ in that integral. Indeed on $|\Im z|\le2V$
the factor $G(\rho+z)$ costs at most $\exp(C_\gamma\log V\log R)$
by (4); this and the interval length are absorbed by the truncation
error. On its complement the short uniforms supply $|\Im z|^{-k/3}$
against (4), and both $K$ and $K_L$ are bounded. The exponential
translations cost only $e^{(R+w)/R}=O(1)$.

Now use the exact meromorphic simplification
$$
 G(\rho+z)K(z)=\frac{h(\rho+z)}{(\rho+z)cz^m},
 \qquad h(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2 .
$$
The remaining test factor is $e^{(R+L)z}U(z)$. Shift to $\Re z=-1/4$.
The gamma factor decays exponentially in height by Stirling and its
poles are outside the shifted strip. The new line costs $O_\gamma(e^{-R/4})$
since $U$ is the exponential transform of a positive probability measure
supported on the nonnegative axis. Only the pole at zero is crossed.
For $m=1$ its residue equals $1/(\rho\zeta'(\rho))$ as before. For
$m>1$ the leading term is the nonzero Laurent coefficient times
$\int(R+L+v)^{m-1}dU^\vee(v)/(m-1)!$, where $U^\vee$ denotes the
probability measure defining $U$. Lower terms are $O_\gamma((R+w)^{m-2})$.
The Gram argument following (6) applies with conjugation of the complex
test densities in the inner-product rows. All conclusions, including
the density statement for the displayed slowly varying $w$, follow.
