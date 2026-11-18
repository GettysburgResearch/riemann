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

## Arbitrarily slowly diverging widths and a spacing alternative

Let $w(R)\to\infty$ have no prescribed rate. On weak Mertens, the
corresponding short-window means always have lower liminf $B$ and,
for measurable $w$, converge to $B$ in density on dyadic intervals.
Conversely a finite lower liminf implies weak Mertens provided the
ordinates counted **with multiplicity** satisfy, for some $0<\eta<1$,
$$
 \gamma_{j+1}-\gamma_j\ \ge\ \exp(-\gamma_j^{1-\eta})
 \qquad\text{for all sufficiently large positive }\gamma_j .             \tag{7}
$$
In particular if boundedness holds cofinally and WMH fails, RH must hold
and (7) must fail for every $\eta>0$ in this range. This is a conditional
local-to-global implication. The spacing assumption itself does not assert
a negative-derivative moment bound of weak Mertens strength.

The off-line case is already excluded by the fixed compact filter (for
$w>R$ put that filter near the upper endpoint of the window). On RH
condition (7) allows only finitely many multiple zeros. At every sufficiently
high simple zero the local product formula
[(12)](trace-weak-mertens-nov18.md) and the unit-interval zero count show
$$
 |1/(\rho\zeta'(\rho))|\ll\exp(|\gamma|^{1-\eta/2}).
$$
There are $O(\log|\gamma|)$ relevant factors, and (7) bounds each of their
positive logarithms by $O(|\gamma|^{1-\eta})$. Finite multiple zeros do
not change the high-ordinate formula: their repeated factors in the
Hadamard product are included with multiplicities and stay far from the
target. On WMH itself $\sum|1/(\rho\zeta'(\rho))|^2<\infty$ gives this
growth condition directly, with no spacing assumption or multiple zeros.

For fixed $0<\delta<1/4$ take a positive smooth density $\phi$ on $[0,1]$
of integral one, $\|\phi\|_\infty\le1/(1-\delta)$, whose transform on the
imaginary axis satisfies $|\widehat\phi(y)|\le C\exp(-c|y|^\alpha)$ for
some $1-\eta/2<\alpha<1$. Such a test is obtained by convolving a uniform
density of length $1-\delta$ with a compact Gevrey density of width $\delta$;
translate to $[0,1]$. For each target separately put the two-atom factors
described above at all other **multiple** poles, with their multiplicities.
They have a fixed finite support length $D_\gamma$. Convolve with
$(w-D_\gamma)^{-1}\phi(v/(w-D_\gamma))\,dv$. For large $R$ the resulting
probability measure is supported on $[0,w]$, and its scaled density
in $L^2(dv/w)$ is $\phi(v/w)+o(1)$ by uniform continuity of $\phi$.

Shift (6) to $\Re z=-1/4$ across the entire line, leaving the stated
target and the other simple poles. For each fixed $R,w$ this is justified
by the separated horizontal bounds used above and the Gevrey decay
on each fixed horizontal-real-part strip for the transform. The latter
follows by differentiating the compact Gevrey density times an exponential
tilt, with constants allowed to depend on $w$ in passing the horizontal
cutoffs to infinity. On the left line the error is uniformly $O(e^{-R/4})$:
the tilted rescaled density and each fixed number of its physical derivatives
have bounded $L^1$ norms for $w-D_\gamma\ge1$, and the extra translated
atoms have bounded tilted mass. Polynomial vertical growth of $G$ is
therefore integrable after sufficiently many integrations by parts.

The contribution of the other simple poles is at most
$$
 \sum_{\gamma'\ne\gamma}
 |c_{\gamma'}|\, C\exp[-c|(w-D_\gamma)(\gamma'-\gamma)|^\alpha]=o(1).
$$
This is absolute convergence with a fixed summable majorant when $w$
is large, followed by dominated convergence, using the growth bound above.
The target again returns $c_\gamma$ if simple. At a target of order $m>1$
the lower polynomial terms are smaller by $O_\gamma(1/R)$ relative to the
leading moment because $R+v\ge R$. The finite Gram argument now has
largest eigenvalue tending to $\int_0^1\phi^2\le1/(1-\delta)$, since
$\phi(v/w)e^{i\gamma(R+v)}$ have asymptotically orthogonal distinct
frequencies. Send $\delta\downarrow0$ to get the lower liminf $B$ in
the simple case. Any finite multiple zero forces divergence. This proves
the converse under (7), and the unrestricted lower assertion on WMH.

For the matching upper assertion on WMH the finite trigonometric sums
$g_V(u)=\sum_{|\gamma|<V}c_\gamma e^{i\gamma u}$ approximate $g$ in
Besicovitch mean square by the proof of
[trace (6)](trace-weak-mertens-nov18.md). Thus
$$
 \lim_{V\to\infty}\limsup_{X\to\infty}X^{-1}
 \int_0^X\big||g(u)|^2-|g_V(u)|^2\big|du=0
$$
by Cauchy–Schwarz. On $Y\le R\le2Y$, $w(R)\le R$, the exceptional
measure where the average of this error over $[R,R+w(R)]$ exceeds
$\epsilon$ is at most $C\epsilon^{-1}$ times its integral on $[Y,4Y]$,
by the Hardy–Littlewood maximal weak-$(1,1)$ inequality. The moving
means of each finite trigonometric square converge uniformly as the
width tends to infinity, to $\sum_{|\gamma|<V}|c_\gamma|^2$.
For $w(R)>R$ use the global mean $L(X)\sim BX$ directly, since
$(R+w)/w\le2$. Taking $V$ large proves convergence in density for every
measurable choice of diverging widths. Together with the lower bound it
gives the stated liminf.

### Sparse exceptions to the spacing bound

It is enough to require, for some $0<\eta<1$, that
$$
 \sum_{\gamma\ {\rm bad}}\frac{m_\gamma}{1+|\gamma|}<\infty .             \tag{8}
$$
Here the sum is over distinct ordinates of either sign on RH. Mark a zero
bad if it is multiple or if its distance to another distinct ordinate
is less than $\exp(-|\gamma|^{1-\eta})$. Bounded ordinates may all be
marked bad. Condition (8) allows arbitrarily small gaps at exceptional
heights. At good zeros the product bound used for (7) applies verbatim
with multiplicities counted in the remaining factors. For each fixed
target, take the two-atom factors at **every** other bad ordinate with
its multiplicity. Their support lengths have finite sum by (8).
The weak limit of their finite convolutions exists (equivalently, sum
independent bounded nonnegative random variables with summable upper
bounds); its entire transform retains the required zeros and equals one
at the target. Its transform on the left is bounded by one, and it
retains finite total support in the window. The preceding Gevrey
argument now applies to the good zeros alone after shifting, even if the
bad reciprocal derivatives have no uniform growth bound. Thus (8) in
place of (7) still gives the converse for every diverging width.

For example a dyadic bound of $O(T/(\log T)^{1+\delta})$, $\delta>0$,
on the bad count with multiplicity gives (8). It would already suffice
to prove this count at the much larger gap scale $1/(\log T)^2$.
A quantitative first-neighbor repulsion estimate
$O(T\log T\,u^3+T^{1-\epsilon})$ at the single normalized scale
$u=1/\log T$ would imply it, with no assumptions at smaller scales and
no higher correlation bounds. Ordinary fixed-scale pair correlation
does not supply that remainder. Under failure of WMH despite a cofinally
bounded physical test on arbitrary diverging widths, (8) must therefore
diverge for every choice of $\eta$.

## An unconditional numerical local floor

For the explicit compact width in the theta-truncation section the lower
liminf of the actual window means is **at least $0.02840244$**,
without assuming RH, simplicity or weak Mertens. Indeed the off-line
and multiple-zero cases force infinite liminf, and otherwise the
first 128 conjugate pairs alone force this floor. At 112 bits
python-flint 0.9.0 gives their residue sum
$0.0284024499442621162973690675848\ \pm 4.75\cdot10^{-32}$.
The following finite Arb computation uses a Taylor ball for the
derivative at each rigorously enclosed nontrivial zero.

~~~python
from flint import acb, acb_series, arb, ctx

ctx.prec = 112
ctx.cap = 2
total = arb(0)
for rho in acb.zeta_zeros(1, 128):
    derivative = acb_series([rho, 1]).zeta()[1]
    total += 2 / abs(rho * derivative)**2
assert total > arb("0.02840244")
~~~

A support constraint explains the double logarithm in the explicit
low-frequency annihilation method. If a measure of total variation at
most $A$ on an interval of length $w$ has transform one at zero, translate
its support to $[-w/2,w/2]$. Jensen's formula on the circle of radius
$2V$ bounds its number of transform zeros of modulus at most $V$, with
multiplicity, by $(\log A+wV)/\log2$. An exact annihilator of all other
critical ordinates up to height $V$ must have $\gg V\log V$ such zeros
on RH, by the Riemann–von Mangoldt formula. Thus uniformly bounded
variation forces $w\gg\log V$ in this exact-annihilator class. This
argument neither imposes a lower bound on the width needed for WMH nor
excludes alternative arithmetic tests.

## Both signs occur with unconditional positive mass in each compact window

With the explicit theta width $w=(\log\log R)(\log\log\log R)$, in fact
with any $w/\log\log R\to\infty$ and $w=o(R)$, one has
$$
 \liminf_{R\to\infty}\min_\pm\frac1w\int_R^{R+w}(\pm g(u))_+du
 \ \ge\ \frac1{2|\rho_1\zeta'(\rho_1)|}>0.04457076 ,
$$
where $\rho_1$ is the first positive-ordinate zero. Its simplicity and
the numerical lower bound follow from the same certified derivative
calculation above.

Off RH apply the [positive sparse-pole filter](detector-positive-isolation-nov18.md)
to $G(s)=1/(s\zeta(s))$. Its compact probability factors remove all
competing conjugate pairs to the right of the separating line, and its
positive Gevrey multiplier preserves the selected pair. The resulting
convolution has leading oscillation $e^{(\beta-1/2)u}u^{m-1}$ times a
nonzero real sinusoid for a selected zero of order $m$. The separating
line contributes an exponentially smaller error. The two opposite
phases in a fixed period then force each original signed $L^1$ mass
to grow exponentially on every sufficiently wide fixed window, exactly
as in the linked construction.

On RH use the theta-truncation argument at frequency zero with $m=0$,
that is, $K_0(z)=\xi(1/2+z)/\xi(1/2)$. Its normalized theta density is
positive: on the nonnegative axis every term of the classical theta
kernel has the factor $2\pi n^2e^{2v}-3>0$, and evenness gives the
other axis. All convolutions and the truncation normalization therefore
remain positive. The exact product with $G$ has no pole at zero.
Thus its final density $p_0$ has integral one, is supported on $[0,w]$,
equals $1/(w-S_0)$ on $[S_0,w-S_0]$ and gives
$\int g(R+v)p_0(v)dv=o(1)$, where $S_0=o(w)$. Also
$p_0\le1/(w-S_0)$ everywhere.

On the interior interval $[R+S_0,R+w-S_0]$, apply the nonzero-frequency
theta test at $\rho_1$ using mean radius $R+S_0$ and length
$w'=w-2S_0\sim w$. In its last convolution replace the long uniform
by a smooth density $q_\delta$ rescaled to $[0,w'-S_1]$, of integral
one, supremum at most $(1+\delta)/(w'-S_1)$ and Lipschitz constant
$O_\delta(1/(w'-S_1)^2)$. Here $S_1=o(w)$ is the earlier filter's
support length. The high-frequency decay comes from the short uniforms
and the left contour uses only mass one of this last factor, so the
extracted coefficient is still $c_{\gamma_1}+o(1)$. The preliminary
complex measure has total mass one, total variation $O_{\gamma_1}(1)$
and support length $S_1$. Its convolution differs uniformly from the
last smooth density by $O_{\delta,\gamma_1}(S_1/(w'-S_1)^2)$ by the
Lipschitz bound. Consequently the entire interior test has absolute
density at most $(1+\delta+o(1))/w$. It follows that
$\int |g|p_0\ge(|c_{\gamma_1}|-o(1))/(1+\delta+o(1))$.
The negligible signed mean against $p_0$ divides this absolute mass
equally between signs up to $o(1)$. The upper bound on $p_0$ transfers
each lower mass to ordinary normalized Lebesgue measure. Send
$\delta\downarrow0$ to complete the proof.

## Transferring the finite Ingham witnesses to every sufficiently late window

For every sufficiently large $X$, the interval
$$
 [X,\ X\exp((\log\log\log X)(\log\log\log\log X))]
$$
contains points $x_+,x_-$ with
$$
 M(x_+)/\sqrt{x_+}>1.82,\qquad M(x_-)/\sqrt{x_-}<-1.83 .                \tag{9}
$$
The numerical input is Hurst's published finite trigonometric witnesses;
we do not recompute his 14,400-term sums. The transfer below applies to
any nonnegative bandlimited smoothing kernel. It supplies no effective
starting value of $X$. [Hurst, Theorems 4.2 and 6.1](https://arxiv.org/abs/1610.08551)

Write $I_R=[R,R+w]$ with the explicit theta width. Suppose that on some
sequence $R\to\infty$ the function $g$ is bounded above by a fixed $D>0$
throughout $I_R$. If RH fails, the preceding positive-pole argument already
contradicts this. On RH the positive zero-mean test $p_0$ from the preceding
section gives $\int |g(R+v)|p_0(v)dv\le2D+o(1)$. Its flat core includes
the middle three quarters of $I_R$ for all large $R$, so on that core
$\int |g(u)|du=O_D(w)$.

Choose a single smooth nonnegative density $q_R$ of integral one inside
the middle half of $I_R$, by scaling and translating a fixed smooth compact
probability density. It has supremum $O(1/w)$ and Lipschitz constant
$O(1/w^2)$. At **each fixed real frequency** $\lambda$ use the
theta-truncation proof with target $1/2+i\lambda$, taking $m=0$ if it
is not a zero. Replace its final long uniform by $q_R$, with the
translation included in the outer exponential as in (6). The preliminary
compact measure has mass one, total variation $O_\lambda(1)$,
and support length $S_\lambda=o(w)$. Its convolution with $q_R$ differs
uniformly from $q_R$ by $O_\lambda(S_\lambda/w^2)$, and both are supported
in the middle three quarters for large $R$. The replacement therefore
changes the statistic by $o(1)$ on the putative bounded sequence, using
the core $L^1$ bound. In particular a multiple zero is impossible since
its target statistic would grow polynomially in $R$. With all zeros simple,
we have along this same sequence
$$
 \int g(u)e^{-i\lambda u}q_R(u)\,du\ \longrightarrow\
 c(\lambda)=
 \begin{cases}1/(\rho\zeta'(\rho)),&\rho=1/2+i\lambda\text{ a zero},\\
               0,&\text{otherwise}.
 \end{cases}                                                               \tag{10}
$$
The common densities are essential. Limits for each finite set of
frequencies follow on the original sequence; no countable enumeration
of all real frequencies is needed.

For clarity, view continuous almost periodic functions as continuous
functions on the Bohr compactification of $\mathbb R$. Equation (10)
defines a linear functional on the trigonometric polynomials bounded
in the supremum norm, by the uniform bound on $\int |g|q_R$.
By uniform approximation and the Riesz representation theorem it
corresponds to a finite real signed measure $\mu$ on that compact group,
with Fourier coefficients $c(\lambda)$ in the convention $e^{-i\lambda u}$.
Since $g\le D$ throughout the supports and $q_R\,du$ converges on each
trigonometric polynomial to normalized Haar measure $m_B$ (all nonzero
fixed Fourier coefficients tend to zero), $\mu\le Dm_B$. The inequality
extends to every nonnegative continuous function by uniform approximation.

For any nonnegative probability density $k$ on the real line with
compactly supported Fourier transform, push $k(u)du$ to the Bohr group
to obtain a probability $\nu$. Then $\mu*\nu\le Dm_B$, and its Fourier
coefficients $c(\lambda)\widehat k(\lambda)$ vanish outside a **finite**
set: the only nonzero ones are zero ordinates in a compact interval.
By uniqueness on trigonometric polynomials,
$$
 \mu*\nu=P_k\,m_B,\qquad
 P_k(y)=\sum_{\gamma} c(\gamma)\widehat k(\gamma)e^{i\gamma y}.
$$
Consequently $P_k(y)\le D$ on the entire group, hence for every real $y$.
The identical argument for $-g$ gives the lower version. Thus
$\liminf_{R\to\infty}\sup_{u\in I_R}g(u)\ge\sup_yP_k(y)$ and
$\limsup_{R\to\infty}\inf_{u\in I_R}g(u)\le\inf_yP_k(y)$ whenever the
relevant finite critical ordinates and residues have been identified.
The case distinctions above show that the resulting comparisons require
no assumed global zero location or simplicity.

For Hurst's kernel, $\widehat k(\gamma)=f(\gamma/\gamma_{14400})$ with
$f(v)=(1-|v|)\cos(\pi v)+\sin(\pi|v|)/\pi$ on $|v|\le1$ and zero
elsewhere. This is the normalized autocorrelation of
$\cos(\pi x)\mathbf1_{|x|\le1/2}$: integration of the two cosines
gives exactly the displayed formula. Thus it is the Fourier transform
of a nonnegative probability density after scaling. Hurst reports
explicit arguments with finite values approximately $1.826054$ and
$-1.837625$. Conjugating all coefficients just reflects $y$, leaving
the extrema unchanged. The conservative strict margins in (9) follow.

### A narrower interval for the two published witness levels

There is a fixed constant $A>0$ for which both inequalities (9) occur
throughout the range of sufficiently large starting values, in the
smaller interval
$$
       [X,\ A X(\log\log X)(\log\log\log X)].                             \tag{11}
$$
As in (9), this statement does not make the starting value or $A$
effective. We detail why one-sided caps can be tested with a shorter
window than the earlier square-mean comparison.

Use the real center of the physical window as coordinate origin for its
test densities. Take $R$ to be its left endpoint in the $u=\log x$
coordinate and take
$$
 L=\tfrac12(\log\log R+\log\log\log R)+C_0,\qquad V=(\log R)^4 .
$$
In the theta-truncation proof the error $\exp(-c_2e^{2L})$ must absorb
$\exp(C\log R\log V)$ times a polynomial in $V$. The constant $c_2>0$
can be the same for each fixed frequency: the original theta density
has a fixed double-exponential exponent, and each fixed number of
primitives and each normalization merely changes its prefactor after
decreasing that exponent once. Likewise (4) has an absolute exponent,
with each fixed frequency translation bounded by $V$ eventually.
Thus a sufficiently large fixed $C_0$ works for each fixed frequency in
(10). Use the same $k$ short uniforms, now symmetrically supported about
zero, of total length $s=k/\sqrt V=o(1)$. Their transform on the left
line costs at most $e^{s/4}$, and on the right line at most $e^{s/R}$.
The preceding frequency estimates are unaffected. Do not translate the
truncated theta kernel, so the combined preliminary density has support
in $[-L-s/2,L+s/2]$.

Suppose a cofinal one-sided cap holds along windows of length
$2L+s+J$ with $J\to\infty$ and $2L+s+J=o(R)$. In the centered coordinate
let $p_0$ be the convolution of the positive preliminary theta density
at frequency zero with the uniform probability on $[-J/2,J/2]$. Its
signed mean is again $o(1)$ by the same contour; possible exponential
growth from the two-sided supports on $\Re z=-1/4$ is absorbed by
$e^{-R/4}$. Thus $\int |g|p_0=O(1)$, with $g$ evaluated at the translated
coordinate. On $|v|\le J/3$ the density $p_0$ is at least $c/J$, since
the preliminary measure gives a fixed positive mass to $[-1,1]$.

As common test use a smooth probability $q$ on $[-J/8,J/8]$ with
Lipschitz constant $O(J^{-2})$, again a scaled fixed test. At frequency
$\lambda$ convolve it with the centered preliminary kernel to give
$p_\lambda$. The latter preliminary kernel has integral one and first
absolute moment $O_\lambda(1)$ uniformly in $R$: this follows by
integrating the absolute moment of the fixed theta density or its
primitives, and adding the $o(1)$ short-uniform width. Consequently
$\|p_\lambda-q\|_\infty=O_\lambda(J^{-2})$. On $|v|\le J/3$ this costs
$o(1)$ in the integral against $|g|$, since its integral there is $O(J)$.

On $|v|>J/3$ we have $q(v)=0$ and
$$
    |p_\lambda(v)|=o(1)p_0(v)
$$
uniformly, interpreting the inequality directly at zeros of the denominator.
Here are explicit bounds that permit $J$ to grow arbitrarily slowly.
Where the numerator is nonzero one has $|v|\le J/8+L+s/2$, and
$|p_\lambda(v)|\ll_\lambda
\exp[-c e^{2(|v|-J/8-1)}]$ by the absolute tail of its preliminary
kernel. In the denominator take the portion of the uniform probability
within distance one of $\operatorname{sgn}(v)J/4$. Its mass is $\gg1/J$.
Every argument of the underlying positive theta density in this portion,
including convolution with the short uniforms, has absolute value at most
$|v|-J/4+2<L$ for large $J$, so it was retained under truncation.
The even positive theta series, already its first term on the positive
axis, is bounded below by $c'\exp[-C'e^{2|u|}]$ for all real $u$.
Therefore $p_0(v)\gg J^{-1}\exp[-C'e^{2(|v|-J/4+2)}]$.
The ratio tends to zero uniformly on $|v|>J/3$ because the two exponential
arguments differ by $J/8-O(1)$. This proves the outer estimate; its
integral is $o(1)$ by the bound on $\int |g|p_0$.

The common-density limit (10) and the measure domination now hold on
these windows; the Fourier coefficients of $q$ away from zero tend to
zero because $J\to\infty$. Thus there is no sequence of such windows
on which either prescribed sign cap persists. If (11) failed for every
constant $A$, choose counterexamples with $A_j\to\infty$ and $X_j\to\infty$
sufficiently fast that their log widths are $o(\log X_j)$. Pass to one
of the two signs. Their surplus $J_j=\log A_j-2C_0-o(1)$ tends to
infinity, contradicting the preceding assertion. This proves (11).

Pintz's earlier effective two-sign theorem gives fluctuations beyond
$\pm\sqrt{x}/136000$ in every sufficiently late interval
$[Y\exp(-5(\log\log Y)^{3/2}),Y]$. His earlier unsigned theorem gives
$\max_{Y/(100\log Y)\le x\le Y}|M(x)|\ge\sqrt Y/17000$ effectively.
The present coefficients and window transfer use different hypotheses
on the test kernels; there is no worldwide priority claim.
[Pintz, Part I](https://doi.org/10.4064/aa-42-1-49-55) ·
[Pintz, Part III, theorem and Corollary 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa43/aa4323.pdf)

### Positive integrated excess above both numerical thresholds

For every $\epsilon>0$ take $w=(1+\epsilon)\log\log R$. There is
$c_\epsilon>0$ such that for all sufficiently large $R$,
$$
 \frac1w\int_R^{R+w}(g(u)-1.82)_+\,du\ge c_\epsilon,\qquad
 \frac1w\int_R^{R+w}(-g(u)-1.83)_+\,du\ge c_\epsilon .
$$
The corresponding multiplicative interval is
$[X,X(\log\log X)^{1+\epsilon}]$. This asserts a positive mean
overshoot without estimating its numerical value.

Indeed in the preceding narrow-window construction the surplus $J$
is now comparable to $w$. If the first normalized excess tended to
zero along a sequence, the positive $p_0$ has supremum at most
$1/J=O_\epsilon(1/w)$ and its signed mean is $o(1)$ on RH. Consequently
$\int |g|p_0\le2(1.82)+2\int (g-1.82)_+p_0+o(1)=O(1)$ exactly as
required for common-density replacement. For every fixed nonnegative
almost periodic test polynomial $Q$, the departure from the upper
measure inequality is at most
$\|Q\|_\infty\|q\|_\infty\int_I(g-1.82)_+=o(1)$.
Thus the same measure is dominated by $1.82m_B$, contradicting the
finite witness. Off RH the positive-pole argument gives divergence of
the positive excess directly. Apply the argument to $-g$ for the other
inequality. Nonnegativity implies the asserted strictly positive lower
limits.

In particular on weak Mertens both violation sets have strictly positive
lower logarithmic density in the original $x$ variable. Cover a dyadic
range of the log variable by disjoint successive windows of the stated
width, discarding a final interval of length $o(R)$. The integrated
excess is therefore $\gg R$. Cauchy–Schwarz and $\int_0^{2R}|g|^2=O(R)$
give measure $\gg R$ to each exceedance set there. The same proof gives
positive relative measure on individual windows where the normalized
square mean stays bounded, which holds in density for the present widths
under weak Mertens. No assertion about the existence of an ordinary
logarithmic density is needed here.
