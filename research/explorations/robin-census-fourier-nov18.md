# Mean square and Fourier coefficients of a natural Robin slab count

For $Y=e^t$ let $C(Y)$ count $n>5040$ such that
$$
 |\log n-Y|\le Y^{3/4}\log Y,\qquad
 B(n)=\log\frac{\sigma(n)}{e^{\gamma_E}n\log\log n}
       \ge -\frac{1}{\sqrt{\log n}\log\log n}.
$$
Write $S(t)=t e^{-3t/4}\log(1+C(e^t))$, $c_* =\pi\sqrt{2/3}$ and $b_*=3-2\sqrt2$. Then the mean square recovers the actual real-part supremum $\Theta$ unconditionally:
$$
 \lim_{T\to\infty}\frac1T\log\left(1+\int_1^T S(t)^2dt\right)=\Theta-\tfrac12.
 \tag{1}
$$
Under RH the mean square itself, after division by $T$, tends to $c_*^2 b_*$. If RH fails it grows exponentially, at the strictly positive rate in (1). Under RH its nonzero Fourier means determine each zeta ordinate and multiplicity. The conditional profile needed at the critical scale is the [natural-tolerance local census](robin-census-constant-nov18.md); the proof below of exponential mean-square growth when RH fails uses the signed LCM runs and paired prime choices.

## Growth when an off-line zero exists

For $1/2<\Theta<1$ the [entropy upper bound](robin-census-entropy-nov18.md) applies unchanged to the natural threshold. Its additional deficit allowance $O(Y^{-1/2}/\log Y)$ is smaller than the existing $O(Y^{\Theta-1}/\log Y)$ above the critical line. Summing the unit-bin bounds in the defining slab gives $S(t)\ll\exp((\Theta-1/2)t/2)$. For $\Theta=1$, counting all integers up to $\exp(Y+Y^{3/4}\log Y)$ gives $S(t)\ll t\exp(t/4)$. These estimates yield the upper bound in (1).

Fix $1/2<c<c'<\Theta$, $r=(1+c)/2$ and $0<\delta<\min(1-c,c-1/2,1/4)$. By the [contiguous-run theorem](robin-lcm-short-nov18.md), every sufficiently large $[X,C_0X]$, for an appropriate constant $C_0$, contains an interval $I$ of length $X^{1-\delta}$ throughout which $B(m_x)>x^{c'-1}$ for $m_x=\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)$. At each such $x$ put $h=x^r$ and $k=\lfloor h/(3\log x)\rfloor$. Take the $k$ closest primes $p^-_j\le x$ and the $k$ closest $p^+_j>x$, paired in order of distance on their respective sides. The classical prime number theorem in short intervals of fixed exponent above $7/12$ places all of them within $h$ of $x$, for all large $x$. Every $p^-_j$ occurs to exponent one in $m_x$. For any selected pairs divide $m_x$ by their $p^-_j$ and multiply by their $p^+_j$, producing distinct integers.

Each exchange reduces log abundancy by at most $O(h/x^2)$ and increases $\log n$ by $\log(p^+_j/p^-_j)=O(h/x)$. As $\psi(x)\sim x$, concavity of $\log\log y$ at $y=\psi(x)$ bounds the total loss in $B$ by $O(kh/x^2)=O(x^{c-1}/\log x)$. Thus every configuration is a strict exception for large $x$. Equip each of the $2^k$ choices with equal probability. The log sizes have mean
$$
 m(x)=\psi(x)+\tfrac12\sum_{j=1}^k\log(p^+_j/p^-_j)
$$
and variance $O(k(h/x)^2)=O(x)$ since $r<1$. For every $Y$ within $O(\log x)$ of $m(x)$, Chebyshev's inequality puts $1-o(1)$ of all the configurations in the slab at $Y$. In particular $S(\log Y)\gg X^{(c-1/2)/2}$.

For completeness the exceptional centers fill a long interval. The function $m(x)$ is nondecreasing with jumps $O(\log x)$ for large $x$. At a prime the two lists shift by one position. With $k$ fixed their net contribution to the jump of the half sum is $(\log p_{\rm new}^++\log p_{\rm old}^--2\log p)/2=O(h/x)$, dominated by the positive jump $\log p$ of $\psi$. An increase of $k$ adds one nonnegative half log ratio of size $O(h/x)$, including when it coincides with a prime. At any remaining prime power only the nonnegative $\psi$ increment enters. Between these events $m$ is constant. Also $0\le m(x)-\psi(x)\ll x^c/\log x=o(X^{1-\delta})$. The short-interval PNT across $I$ now gives a range of $m$ of length $\gg X^{1-\delta}$. Every intermediate center lies within $O(\log X)$ of an attained value. This supplies a log-center interval of length $\gg X^{-\delta}$ where the squared normalized count is $\gg X^{c-1/2}$.

Given large $T$, take $X=e^T/(3C_0)$ to keep this interval inside $[1,T]$ in log coordinates. Integration gives a lower exponential rate $c-1/2-\delta$ in (1). Let $\delta\downarrow0$ and $c\uparrow\Theta$. In particular the lower bound is on every sufficiently large terminal horizon.

## Conditional inversion at the critical line

Under RH the natural-scale tangent-cost and local partition formula give
$$
 S(t)=c_*\sqrt{b_*+f(t)}+o(1),\qquad
 f(t)=\sum_\rho \frac{e^{i\Im(\rho)t}}{|\rho|^2}.
$$
The sum runs over signed zeros with multiplicities. The exact zero sum $\sum_\rho|\rho|^{-2}=2+\gamma_E-\log(4\pi)<0.047$ is less than $b_*$. Thus the positive-part cutoff plays no role. In particular the normalization and square preserve every Fourier coefficient, including its phase. Define $A(t)=S(t)^2/c_*^2-b_*$; it equals $f(t)+o(1)$. Termwise averaging in the absolutely and uniformly convergent trigonometric series shows that for every real $\omega$,
$$
 \lim_{T\to\infty}T^{-1}\int_1^T A(t)e^{-i\omega t}\,dt
 =\begin{cases}
 m_\rho/(1/4+\omega^2),&\rho=1/2+i\omega\ \text{is a zero of multiplicity }m_\rho,\\
 0,&\text{otherwise}.
 \end{cases}
$$
At frequency zero this proves the mean-square assertion and the RH half of (1). Combined with the preceding unconditional alternative, boundedness of the Cesàro mean of $S^2$ characterizes RH. The test uses only a single arithmetic tolerance and width.

For a fixed frequency, suppose $|A(t)-f(t)|\le\varepsilon$ on a measurement interval of length $L$. Let $\Delta_\omega$ be the distance from $\omega$ to the closest *different* signed zero ordinate, excluding $\omega$ itself if it is an ordinate. The ordinates have no finite accumulation, so $\Delta_\omega>0$. Integrating each other exponential gives an absolute error at most
$$
 \varepsilon+\frac{2(2+\gamma_E-\log(4\pi))}{L\Delta_\omega}
$$
for the inferred coefficient. The corresponding multiplicity estimate is scaled by $1/4+\omega^2$: it rounds uniquely when the scaled error is less than $1/2$ and the tested ordinate is known exactly. This bound depends on a signal-approximation error and a local frequency separation. The asymptotic arithmetic estimate provides neither a uniform finite measurement horizon nor a height-uniform separation bound. When RH fails, (1) still recovers $\Theta$ but the critical-line Fourier inversion above has no asserted validity.


## Exponentially short relative intervals

Take any nonnegative width function $D(Y)=o(\sqrt Y)$ as in the [short-interval critical profile](robin-census-constant-nov18.md). Replace $C(Y)$ by the number obeying the same natural tolerance in $[e^Y,e^Y(1+e^{-D(Y)})]$. With this replacement the same growth formula (1), conditional Fourier coefficients and stability estimate hold. Under RH use the linked short-interval local profile. The upper bound if RH fails follows by containment in the previous slab.

For the lower bound retain the paired construction, choosing $\kappa$ with $1/2<\kappa<c$. Its log-size variance is $O(x)$, so $1-o(1)$ of configurations have log sizes within $x^\kappa/2$ of $m(x)$. The center function $m(x)+2x^\kappa$ is increasing with jumps $O(\log x)$, and its range across $I$ has length $\gg X^{1-\delta}$ as before. For every intermediate $Y$ select $x$ within $O(\log x)$ in center value. All the concentrated log sizes now lie in $[Y-3x^\kappa,Y-x^\kappa]$. Replace $n$ by $n'=n\lceil e^Y/n\rceil$. Then $e^Y\le n'<e^Y(1+e^{-x^\kappa})$, which lies in the required interval. Divisibility makes $\sigma(n')/n'\ge\sigma(n)/n$, and the increase of the denominator in $B$ is $O(x^{\kappa-1}/\log x)=o(x^{c'-1})$. The integers remain strict exceptions. Their possible multiplicity under rounding is at most $1+e^{3x^\kappa}$ since the multiplier determines the preimage at any output. Its logarithm is $o(k)$ as $\kappa<c<r$. Hence the pointwise logarithmic count on this entire interval of centers still exceeds a constant times $X^r/\log X$. The previous integration proves the lower bound in (1).
