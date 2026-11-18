# The arithmetic energy of Laguerre prime coefficients

Proposed mean-square results for the [fixed-center detector](laguerre-prime-detection-nov18.md). Write $L_n(x)$ for the ordinary Laguerre polynomial and $D_n(x)=L_n^{(-1)}(x)=L_n(x)-L_{n-1}(x)$ for $n\ge1$. Put
$$
 b_n(k)=-\Lambda(k)k^{-2}D_n(3\log k),\quad
 c_n(t)=\sum_{k\ge2} b_n(k) k^{-it}.
$$
The series converges absolutely for each fixed $n$. It is the $n$th coefficient of $(\zeta'/\zeta)(2+it+3w/(1-w))$. All results below use these ordinary von Mangoldt coefficients.

## An asymptotically five-diagonal Gram matrix

Let $G_{nm}=\sum_k b_n(k)b_m(k)$. Uniformly as $\min(n,m)\to\infty$,
$$
 9G_{nm}= \begin{cases}
 6n & m=n,\\
 -(4n+2)&m=n+1,\\
 n+1&m=n+2,\\
 0&m>n+2
 \end{cases}\quad+o(1)\qquad(m\ge n).
$$
Symmetry supplies the other entries. In particular the actual diagonal is $2n/3+o(1)$.

To prove this, let $\mu=\sum_{k\ge2}(\Lambda(k)^2/k)\delta_{\log k}$. The classical quantitative PNT and partial summation imply
$$
 \mu([0,v])=v^2/2+C+O((1+v)^C e^{-c\sqrt v})
$$
for some constants, with the same letter $C$ allowed to be enlarged in the polynomial error. Indeed partial summation of $d\vartheta(x)$ with weight $\log x$ gives $\sum_{k\le x}\Lambda(k)^2=x\log x-x+O(x(1+\log x)^C e^{-c\sqrt{\log x}})$ after accounting for prime powers, whose total is $O(\sqrt{x}(1+\log x)^3)$. A second partial summation with $1/x$ gives the assertion; equivalently the cumulative discrepancy from $v\,dv$ tends to a constant with integrable error.

Set $h_n(x)=e^{-x/2}D_n(x)$. Both $h_n$ and $h_n'$ are uniformly bounded on $x\ge0$, by the classical Fejér bound $|e^{-x/2}L_j(x)|\le1$ and $D_n'(x)=-L_{n-1}(x)$. For each fixed $x>0$ they tend to zero by the fixed-positive-argument Laguerre asymptotic for $L_n$. Integrate $h_n(3v)h_m(3v)$ against $d\mu-v\,dv$ by parts, subtracting the limiting constant from the cumulative discrepancy. There is no lower-end term because $D_n(0)=0$. The integrand in the resulting ordinary integral is uniformly dominated by the integrable discrepancy bound and tends to zero. The error is consequently $o(1)$, also for sequences of pairs with minimum tending to infinity. The remaining integral is
$$
 G_{nm}=\tfrac19\int_0^\infty x e^{-x}D_n(x)D_m(x)\,dx+o(1).
$$
Laguerre orthonormality in $e^{-x}dx$ and $xL_n=(2n+1)L_n-(n+1)L_{n+1}-nL_{n-1}$ give the entries. [Laguerre bounds](https://dlmf.nist.gov/18.14) · [Fixed-argument asymptotics](https://dlmf.nist.gov/18.15#iv)

The time average $T^{-1}\int_T^{2T}c_n(t)\overline{c_m(t)}dt$ differs from $G_{nm}$ by $O((1+n)(1+m)2^{n+m}/T)$. Indeed the generating function of $D_n$ is $\exp[-xw/(1-w)]$, so Cauchy's bound at $0<r<1$ gives $|D_n(x)|\le r^{-n}e^{xr/(1+r)}$. Take $r=n/[2(n+1)]$. Then $\sum k|b_n(k)|^2\ll 4^n(1+n)^2$ using $\sum\Lambda(k)^2/k^{1+\delta}\ll1+\delta^{-2}$ by the same prime estimate. The mean-value inequality of Montgomery and Vaughan in its bilinear form proves the error bound by truncation. Thus, for each fixed $0<\epsilon<1$, orders at most $(1-\epsilon)\log T/\log4$ give the displayed Gram asymptotic with $o(1)$ error when both orders grow. This is an unconditional actual-source estimate over a moving frequency interval. It does not supply the estimate at all orders needed below.

## One exponential rate gives the zero abscissa

Remove zeta's known pole and define
$$
 F(s)=\frac{\zeta'}{\zeta}(s)+\frac1{s-1},\qquad
 d_n(t)=[w^n]F(2+it+3w/(1-w)).
$$
In arithmetic terms this is the coefficient of the continuous main term minus the prime measure: $d_n(t)=c_n(t)+\int_1^\infty v^{-2-it}D_n(3\log v)\,dv$. For any positive sequence $T_n\to\infty$ with $\log T_n=o(n)$ let
$$
 V_n=\frac1{2T_n}\int_{-T_n}^{T_n}|d_n(t)|^2dt,\qquad
 \Theta=\sup_\rho\Re\rho .
$$
Then
$$
 \limsup_{n\to\infty} V_n^{1/(2n)}=\frac{1+\Theta}{2-\Theta}.
$$
When RH fails the full limit exists and is strictly greater than one. Under RH there is the stronger direct bound $V_n\ll\log^2(2+T_n+n)$. These claims do not import a density hypothesis or require a rightmost zero.

**Upper bound.** For fixed $r<(2-\Theta)/(1+\Theta)$ the circle $|w|=r$ maps into a fixed real-part strip with left boundary $2-3r/(1+r)>\Theta$. The classical local partial-fraction estimate for $\zeta'/\zeta$, the unit-interval zero count and the positive distance to every nontrivial zero give $|F(s)|\ll_r\log(2+|\Im s|)$ there, including a compact neighborhood of the removed pole. Cauchy's estimate gives $V_n^{1/2}\ll_r r^{-n}\log(2+T_n)$. Send $r$ to the stated boundary.

**Lower bound.** The zero $\rho=\beta+i\gamma$ yields a pole at $w_\rho(t)=(\rho-2-it)/(\rho+1-it)$. Its modulus at $t=\gamma$ is $(2-\beta)/(1+\beta)$. Suppose first $\Theta>1/2$. Given $r$ strictly between $(2-\Theta)/(1+\Theta)$ and 1, choose $\rho$ and a bounded interval of $t$ on which $|w_\rho(t)|<r$. At any generic point in this interval there is a unique distinct nearest pole. Indeed only finitely many poles fall in any closed subdisk of radius less than one, uniformly on compact $t$ sets. Equalities of radii between distinct off-line zeros are isolated unless the rational functions $|w_\rho(t)|^2$ coincide identically. For zeros inside the disk, their minima occur at $t=\gamma$ and uniquely determine $\beta$ via the displayed ratio, excluding this degeneracy. Shrink to a closed interval of positive length around a generic point, retaining the same simple pole of the logarithmic derivative as the unique closest pole and choosing a single circle that uniformly separates it from all others. Its residue as a function of $w$ is $m_\rho/s'(w_\rho)$, continuous and nonzero there. Subtracting this principal part and applying Cauchy's estimate on the separating circle proves $|d_n(t)|\gg r^{-n}$ uniformly on the smaller interval for all sufficiently large $n$. Since its length is fixed and $T_n^{1/n}\to1$, this proves the full liminf bound by letting $r$ decrease.

If RH holds and the limsup were less than one, there would be $r>1$ with $\sum_n r^{2n} V_n T_n<\infty$. On any fixed bounded interval in $t$, Tonelli then gives, for almost every $t$, a coefficient series analytic throughout $|w|<r$. But each nontrivial zero gives a pole at a point $|w_\rho(t)|=1$ distinct from $w=1$. Local analytic continuation from inside the unit disk contradicts that pole. For the stronger RH upper bound use the positive real part of $\xi'/\xi$ in $\Re s>1/2$, by the symmetric product over critical-line zeros. Carathéodory's coefficient estimate bounds the nonconstant coefficients of its disk composition by $2\Re(\xi'/\xi)(2+it)\ll\log(2+|t|)$. The remaining terms of $F$ are elementary and a multiple of the digamma function, holomorphic on $\Re s>1/2$ and of size $O(\log(2+|t|+n))$ on $|w|=n/(n+1)$ by Stirling and the map. Cauchy on that circle costs at most $e$. This finishes the proof.

One may fix $T_n=n$, for example. In this regime the preceding unconditional mean-value error grows exponentially. The subexponential upper bound for the **centered** arithmetic energy $V_n$ is the unresolved assertion equivalent to RH.

## Which part of the uncentered energy comes from the pole?

The actual arithmetic coefficients $c_n$ have two unconditional regimes. Uniformly for $1\le T\le e^n$,
$$
 \int_{-T}^T |c_n(t)|^2dt
 \sim \frac{3\sqrt{3\pi}}{2}\frac{4^n}{\sqrt n}.
$$
The large value is caused by the pole of zeta at 1. At the other end, for $T\sqrt n/4^n\to\infty$,
$$
 \frac1{2T}\int_{-T}^T |c_n(t)|^2dt\sim 2n/3 .
$$
The positive first-coordinate statistic without the continuous subtraction therefore has a substantial region where its size is prescribed by the known pole, irrespective of RH.

For the first assertion the subtracted coefficient is exactly
$$
 r_n(t)=d_n(t)-c_n(t)=-\frac{3}{(1+it)^2}\left(-\frac{2-it}{1+it}\right)^{n-1}.
$$
The squared modulus has a unique maximum at zero, where it equals $9\cdot4^{n-1}$. Since $\log[(4+t^2)/(1+t^2)]=\log4-3t^2/4+O(t^4)$ there, elementary Laplace asymptotics give the displayed equivalent for the integral of $|r_n|^2$ even when restricted to $[-1,1]$. Its complement outside that interval is $O((5/2)^n)$ by its remaining integrable factor $(1+t^2)^{-2}$.

To bound the centered term let $R(b)=(1+b)/(2-b)$ and let $b_t$ be the maximum of $1/2$ and the real parts of zeros whose ordinates lie within $20(n+1)$ of $t$. On the Cauchy circle whose image has leftmost real part $b_t+1/n$, the entire image is within $10(n+1)$ of $2+it$ for $n\ge4$ (use radius $1/R(b_t+1/n)$). For $\Re s\le2$ on the circle, each zero in the unit-height partial-fraction expansion is at horizontal distance $\ge1/n$. For $\Re s>2$ use the absolutely convergent Dirichlet series; at $\Re s=2$ it is uniformly bounded as well. The cancellation at $s=1$ in $F$ takes care of the compact low-height region. Thus
$$
 |d_n(t)|\ll n\log(2+T+n) R(b_t)^n .
$$
The constant is absolute: $\log R(b+1/n)-\log R(b)=O(1/n)$ on the indicated interval. This bound is needed only for $|t|\le T\le e^n$.

The measure of $t$ in this interval with $b_t>s$ is at most $O(n N(s,T+20(n+1)))$, counting both signs and allowing endpoints, as well as at most $2T$. For $s\ge0.52$ use the uniform corrected Ramaré estimate $N(s,H)\ll H^{(8/3)(1-s)}\log^5 H$ in KLN equation (1.5). The Vinogradov–Korobov region and compact nonvanishing on the one-line imply $1-b_t\gg n^{-2/3}(\log(2n))^{-1/3}$ in this range. Partition the possible $b_t$ into bins of length $1/n$. Use the lower endpoint minus $1/n$ in the strict density count (or take its left limit). Rounding endpoints changes the exponential bounds by only a fixed factor. The part $b_t\le0.53$ has squared integral $\ll\mathrm{poly}(n)\exp(n[1+2\log R(0.53)])$, smaller than $4^n$ by a fixed exponential factor. For the other bins, the exponent for the squared integral divided by $n$ is at most
$$
 2\log R(s)+\tfrac83(1-s)+O(\log n/n).
$$
Here $T+20(n+1)\le2e^n$ for large $n$. Since $2(\log R)'(u)=6/[(1+u)(2-u)]$ is increasing on $[1/2,1]$, its average over $[s,1]$ is at least its average over $[1/2,1]$, namely $2\log4>8/3$. Consequently every bin saves at least $(2\log4-8/3)(1-s)n$ from the exponent $n\log4$ before polynomial factors. The zero-free region absorbs these factors and the number of bins. This proves $\int_{-T}^T|d_n(t)|^2dt=o(4^n/\sqrt n)$ uniformly. The triangle inequality for the two $L^2$ norms proves pole domination. [Uniform density input, including correction footnote](https://arxiv.org/pdf/2101.12263)

For the second regime one can sharpen the length factor in the mean-value theorem:
$$
 \sum_k k|b_n(k)|^2\sim \frac{9\sqrt3}{8\sqrt\pi}\sqrt n\,4^n .
$$
Indeed against the measure $d\mu(v)$ above the squared weight is $e^{-2v}D_n(3v)^2$. The generating function at $|w|=1/2$ gives $|e^{-v}D_n(3v)|\le2^n$. Differentiating in $v$ on that same circle costs at most 4 as a multiplicative constant in the bound. Integration by parts against the same integrable cumulative discrepancy therefore gives error $O(4^n)$ on replacing $d\mu$ by $v\,dv$. For $\lambda$ near 2, Plancherel gives
$$
 I(\lambda)=\int_0^\infty e^{-\lambda v}D_n(3v)^2dv
 =\frac9{2\pi}\int_{\mathbb R}
 \frac{((3-\lambda/2)^2+t^2)^{n-1}}{((\lambda/2)^2+t^2)^{n+1}}dt .
$$
This follows by Laplace transforming the generating function (for the identity at fixed $n$ one can also integrate its polynomial coefficient directly). The desired integral is $-I'(2)$. At $\lambda=2$, $I(2)\sim (3\sqrt3/(4\sqrt\pi))4^n/\sqrt n$ by the preceding Gaussian calculation. The negative logarithmic derivative of the integrand divided by $n$ is bounded uniformly in $t,n$ at $\lambda=2$ and tends to $3/2$ near the mass concentrated at $t=0$. Thus $-I'(2)\sim3nI(2)/2$. Applying the mean-value bound with this sharper length factor and $G_{nn}\sim2n/3$ proves the claimed high-$T$ regime.

More generally a uniform density exponent $D(s)$ gives the exponent bound $2\log R(s)+\alpha D(s)$ for the bins at $T=e^{\alpha n}$. For example the classical density hypothesis $D(s)=2(1-s)$, with arbitrary positive power slack on fixed strips, would extend pole domination to each fixed $\alpha<\log4$: away from 1 the margin is then fixed, and sufficiently near 1 one would additionally need a uniform estimate with a small enough log-free exponent loss there (e.g. the same $2(1-s)$ bound with only logarithmic factors). The displayed unconditional regimes leave a gap. Neither gives the subexponential centered energy on $T_n=n$ required for RH.

## A local limiting energy on RH

In the [centered zero-abscissa formula](#one-exponential-rate-gives-the-zero-abscissa)
the full root limit also exists under RH. More precisely, for each bounded
interval $I$ of positive length, RH gives
$$
 \lim_{n\to\infty}\int_I |d_n(t)|^2dt
 =\int_I\sum_{\gamma\ {\rm distinct}}
       \frac{9m_\gamma^2}{((3/2)^2+(t-\gamma)^2)^2}\,dt>0.
$$
Here both signs of the ordinate are included, with $m_\gamma$ the multiplicity.
For the completed logarithmic derivative use the Hadamard partial fractions
of $\xi$ and put $a_\gamma(t)=(\rho-2-it)/(\rho+1-it)$. For $n\ge1$ the
contribution of the pole to its composed Taylor coefficient is exactly
$$
 -\frac{m_\gamma(1-a_\gamma)^2}{3a_\gamma}\,a_\gamma^{-n}.
$$
This follows by expanding $m_\gamma/(s_t(w)-\rho)$, with the constant
Hadamard correction affecting only degree zero. On RH, $|a_\gamma|=1$
and $|1-a_\gamma|=3/|\rho+1-it|$. Thus the amplitudes are absolutely
summable, with tails uniform on every compact $t$-interval by the zero
count. This also justifies coefficient extraction from the partial fractions.

The remaining terms in the centered $F$ are
$-1/s+(\log\pi)/2-\psi(s/2)/2$. For $t$ in a compact set, their disk
compositions on $w=re^{i\theta}$ have modulus bounded uniformly in $r<1$
by $C_I(1+\log^+(1/|\sin(\theta/2)|))$: use $\Re s>1/2$,
$|s|\ll_I 1+1/|1-w|$ and Stirling's estimate in the right half-plane.
This majorant is square integrable. Parseval on circles, then $r\uparrow1$,
gives a uniform bound on the sum of squared coefficients for each $t$.
Consequently these individual coefficients go to zero pointwise, and in
$L^2(I)$ by domination.

In a finite partial sum of zero contributions every pair of distinct
ordinates has a nonconstant phase difference. Indeed
$a_\gamma/a_{\gamma'}$ is a rational function of $t$ whose distinct
zero and pole locations prevent it from being constant when
$\gamma\ne\gamma'$. Its angular derivative has only finitely many zeros
on $I$. Excise arbitrarily small intervals around those critical points,
then integrate by parts on the remaining intervals to obtain vanishing
cross integrals. The uniform absolute tail permits passage to the full
series and proves the displayed local limit. In particular the numerator
of $V_n$ stays bounded below on a fixed interval; $T_n^{1/n}\to1$ and the
preceding RH upper bound give $V_n^{1/(2n)}\to1$.

## The physical prime window carrying the exponential rate

Fix $0<\delta<1/3$ and write $a=4/3-\delta$, $b=3/2+\delta$.
In the formula for $d_n(t)$ retain just $an<\log v\le bn$
in the continuum integral and just ordinary primes $e^{an}<p\le e^{bn}$
in the sum, with weights $-(\log p)p^{-2-it}D_n(3\log p)$.
Denote this centered window by $S_n(t)$. For every $T_n\to\infty$ with
$\log T_n=o(n)$,
$$
 {\rm RH}\quad\Longleftrightarrow\quad
 \limsup_n\left(\frac1{2T_n}\int_{-T_n}^{T_n}|S_n(t)|^2dt
          \right)^{1/(2n)}\le1 .
$$
If RH fails this root has full limit $R(\Theta)=(1+\Theta)/(2-\Theta)$.
In fact one can replace $(a,b)$ in the RH-failure conclusion by any
fixed positive endpoints straddling
$$
 \ell_\Theta=\frac{3}{(2-\Theta)(1+\Theta)} .
$$

To see this write $P(v)=e^v-1-\psi(e^v)$ for $v\ge0$ and
$H(v)=e^{-(2+it)v}D_n(3v)$. Then $d_n=\int H\,dP$.
For each $\epsilon>0$ the classical explicit-formula PNT bound gives
$P(v)\ll_\epsilon e^{(\Theta+\epsilon)v}$; for $\Theta=1$ Chebyshev
suffices. On each fixed Cauchy circle $0<r<1$ the generating function
gives
$$
 |H(v)|+\frac{|H'(v)|}{1+|t|}
 \ll_r r^{-n}\exp[(-2+3r/(1+r))v].
$$
Differentiation in $v$ introduces only the bounded circle factor
$3w/(1-w)$ in addition to $2+it$. For $\Theta>1/2$ put
$r_*=(2-\Theta)/(1+\Theta)<1$. For a fixed boundary ratio $h$
the exponential rate in the integrated endpoint estimate is
$$
 E_h(r)=-\log r+h(\Theta-2+3r/(1+r)),\qquad
 E_h(r_*)=\log R(\Theta),\qquad
 E_h'(r_*)=\frac1{r_*}(h/\ell_\Theta-1).
$$
For $h=a<\ell_\Theta$ choose $r>r_*$ close enough to make
$E_a(r)<\log R(\Theta)$, and for $h=b>\ell_\Theta$ choose
$r<r_*$ with the same strict saving. Take $\epsilon>0$ small enough
to preserve both savings and the negative sign of
$\Theta+\epsilon-2+3r/(1+r)$ in the second case. Partial summation
now bounds the lower tail $[0,an]$ and upper tail $(bn,\infty)$
each by $O((1+|t|)e^{(\log R(\Theta)-c)n})$ for some $c>0$.
The ordinary integrals after partial summation are dominated by their
finite endpoints because the exponent of $v$ is respectively positive
and negative. The initial boundary vanishes as $P(0)=0$.

On the retained window all prime powers of exponent at least two cost
$O_b(1+n)$ in absolute value, uniformly in $t$. Indeed Fejér's bound
gives $|H(\log k)|\le2k^{-1/2}$, and $\sum_{p\le e^{bn/2}}\log(p)/p
=O_b(1+n)$; the higher exponents have convergent total. For $\Theta>1/2$
these errors and the two tails have strictly smaller root rate than the
full centered norm. The preceding full-limit theorem proves the asserted
window rate. Under RH partial summation on $[an,bn]$ with
$P(v)\ll_\epsilon e^{(1/2+\epsilon)v}$ and Fejér's bounds on
$e^{-x/2}D_n(x)$ and its derivative instead gives
$S_n(t)\ll_{a,b,\epsilon}(1+|t|)(1+n)e^{b\epsilon n}+O_b(1+n)$.
Letting $\epsilon$ decrease proves the stated conditional upper bound.
The intervals $(4/3-\delta,3/2+\delta)$ cover $\ell_\Theta$ for every
possible $\Theta$. The centered prime estimate inside this physical
window remains open.

The lower endpoint can in fact be $a=4/3$ exactly, since
$\ell_\Theta>4/3$ for every $\Theta>1/2$. On this window the radial
Laguerre weight has one sign: $(-1)^nD_n(3v)>0$ for $v\ge4n/3$.
Indeed $D_n(x)=-(x/n)L_{n-1}^{(1)}(x)$ and the largest root of
$L_{n-1}^{(1)}$ lies below $4n$. The symmetric Jacobi matrix of size
$n-1$ has diagonal $2j+2$ and off-diagonal $\sqrt{(j+1)(j+2)}$
for $0\le j<n-1$ where present; every absolute row sum is below
$4n$. The degree-zero case is immediate. Thus with this endpoint
the arithmetic test compares two positive radial weights twisted
by the same factor $e^{-itv}$.
