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
