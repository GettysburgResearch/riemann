# A full-zeta positive wave and a moving-shift twisted moment

This note provides two auxiliary estimates for the [Jensen transition problem](jensen-mollified-transition-nov18.md). They apply in the band where the former Dirichlet cutoff creates a loss. Both estimates use the full zeta function in a right half-plane.

## The real positive wave

Use the preceding notes' $P_d$, $s=1/2+iy$, $\tau=y^2/(8d)$, $M_0$, $\alpha=(\log M_0)'$, and $M=M_0(s)e^{\tau\alpha(s)^2}$. Write $a=\Re\alpha(s)$, $b=\Im\alpha(s)$, $c=2\tau a$, $L=\log U\asymp\log y$. On the present band $1\ll cL\ll\log L$. With a standard Gaussian density $g_\tau(v)=(4\pi\tau)^{-1/2}e^{-v^2/(4\tau)}$ of variance $2\tau$, set
$$
 A_+(y)= e^{\tau b^2}\int_0^\infty c\,g_\tau(c(x-1))e^{ibc(x-1)}\zeta(1/2+cx+iy)\,dx .
$$
Uniformly on this band,
$$
 P_d(y)/(8|M|)=2\Re\{e^{i\arg M}A_+(y)\}+O(y^{-1/5}).                 \tag{1}
$$
Indeed the [heat comparison](jensen-heat-nov18.md) approximates $P_d(y)$ by $\mathcal H_\tau(y)$ with error $O(y^{-1/4}\log^3 y)$ after this normalization. The bilateral Fourier integral and the real Gaussian moment give
$$
 \mathcal H_\tau(y)=\int_{\mathbb R}g_\tau(v)\xi(s+v)\,dv
 =2\Re\int_0^\infty g_\tau(v)\xi(s+v)\,dv .
$$
Absolute convergence follows from the double-exponential decay of the theta kernel. The second equality follows from the functional equation and conjugation. In Polymath's convention $\xi(s+v)=8 M_0(s)e^{\alpha(s)v}\zeta(s+v)(1+O(1/y))$ for $0\le v\le1/8$, uniformly by Stirling and $\alpha'(s+v)=O(1/y)$. The factor 8 converts his $H_0(2y)=\xi(s)/8$ normalization. Completing the square in the real exponential and substituting $v=cx$ yields (1). The error from Stirling is $O(y^{-3/4+o(1)})$ after normalization by the convexity bound in $\Re s\ge1/2$. Both tails $v>1/8$ are $O_A(y^{-A})$ in that normalization for every fixed $A$. In fact $\tau\ll\log L/L^2$, and Stirling and the elementary polynomial zeta bounds give
$$
 |\xi(s+v)|\ll e^{-\pi y/4}y^{O(1)}\exp(O(v\log(y+v+2)))
$$
there. Here $y\arctan((v+1/2)/y)\le v+1/2$ controls the angular gamma factor. The Gaussian beats this majorant uniformly outside the retained range.

On any enlarged dyadic interval $y\asymp Y$, let $h$ be the minimum of $c$ there. Then $c\asymp h$, $\tau\asymp h/L$, and the weight in $x$ has absolute value at most $C\sqrt{hL}\exp(-c_1hL(x-1)^2)$ for positive constants $C,c_1$. Because the integral is in the positive variable $x$, every twist $\delta(y)=xc(y)$ stays positive; there is no moving indicator. The full Gaussian mass including its phase, with $x$ extended to the entire real axis, equals 1 after the factor $e^{\tau b^2}$. Cutting to $x>0$ changes that mass by $O(e^{-c_2hL})$. On each enlarged dyadic interval one may also truncate the $x$-integral at $1/(8\max c)$ at a cost $O_A(Y^{-A})$, since the excluded $v$ are bounded below by a fixed positive constant there. [D. H. J. Polymath, definitions (7)–(10)](https://arxiv.org/abs/1904.12438)

## A positive-weight twisted upper estimate

Let $W(y)$ be a nonnegative smooth weight supported on $[Y/2,3Y]$, with $W^{(j)}\ll_jY^{-j}$. Let $0<\delta(y)\le1/8$ be real with $\delta^{(j)}\ll_j Y^{-j}(\log Y)^{C_j}$ for $j\ge1$. Set $\sigma(y)=1/2+\delta(y)$ and
$$
 B(y)=\sum_{m\le K}a_m(y)m^{-iy},\qquad K\le Y^{1/100},\qquad a_1=1.
$$
Suppose $|a_m|\ll m^{-1/2+1/100}$ and $|a_m^{(j)}|\ll_j m^{-1/2+1/100}Y^{-j}(\log Y)^{C_j}$. Then, for some absolute $\epsilon>0$ and the indicated fixed derivative bounds,
$$
 \frac1Y\int W|\zeta(\sigma+iy)B-1|^2dy
 \le \frac1Y\int W\sum_{k\ge2}k^{-2\sigma}
       \left|\sum_{m|k,\ m\le K}a_m(y)m^\sigma\right|^2dy + O(Y^{-\epsilon}).       \tag{2}
$$
Thus the ordinary Euler diagonal controls the full-zeta error even when $\delta\log Y$ is bounded. The error constant stays bounded as $\inf\delta\downarrow0$ for fixed derivative bounds. The Euler diagonal itself can diverge at the limit.

For the first moment $Y^{-1}\int W(\zeta(\sigma+iy)B-1)\,dy=O(Y^{-\epsilon})$, take $X=\lceil Y^6\rceil$ in the elementary Euler summation
$\zeta(s)=\sum_{n\le X}n^{-s}+X^{1-s}/(s-1)+O((|s|+1)X^{-\sigma})$.
Except for $mn=1$, every integrated phase has frequency $|\log(mn)|\ge\log2$. Repeated integration by parts beats the polynomial total length and the logarithmic derivative losses. The displayed integral correction has frequency $\log(Xm)$ and satisfies the same argument.

For the second moment use the product approximate functional equation, obtained by shifting a Mellin contour with the even test $G(z)=e^{z^2}$. Write $\gamma(s)=\pi^{-s/2}\Gamma(s/2)$ and
$$
 D_{\delta,y}(z)=\frac{\gamma(\sigma+iy+z)\gamma(\sigma-iy+z)}
                        {\gamma(\sigma+iy)\gamma(\sigma-iy)},\qquad
 X_\delta(y)=\left|\frac{\gamma(1-\sigma-iy)}{\gamma(\sigma+iy)}\right|^2 .
$$
The first piece is the sum of $(ab)^{-\sigma}(b/a)^{iy}$ smoothed by the Mellin transform $G(z)D_{\delta,y}(z)(ab)^{-z}/z$. The other piece has $\delta$ replaced by $-\delta$ and is multiplied by $X_\delta$. The crossed poles of the completed factors at heights $\pm y$ are exponentially small. The gamma ratio and $G$ allow truncation to $ab\le Y^{1+1/20}$ at cost $O_A(Y^{-A})$. Repeated moving-$y$ differentiation of each smooth kernel costs $O_j(Y^{-j}(\log Y)^{C'_j})$, allowing a harmless factor $Y^{1/100}$ in undifferentiated bounds by using the Mellin line $\Re z=1/100$. These facts follow from differentiated Stirling for $|\Im z|\le(\log Y)^2$ and the Gaussian tail elsewhere.

After twisting, the phase is $y\log(bn/(am))$. If $am$ and $bn$ are comparable they are each $O(\sqrt{abmn})=O(Y^{0.535})$. If distinct, their logarithmic ratio has absolute value $\gg Y^{-0.535}$. All other off-diagonal ratios are bounded away from one. Repeated integration by parts therefore makes the sum of all off-diagonal contributions $O_A(Y^{-A})$ after normalization. This only needs short twists.

On the diagonal let $g=(m,n)$ and write $a=nr/g$, $b=mr/g$. The Mellin sum over $r$ in the first piece gives $\zeta(1+2\delta+2z)$; the second gives $\zeta(1-2\delta+2z)$. Move both lines to $\Re z=-1/4$, first taking the second line to the right of $\delta$. The residues at $z=-\delta$ and $+\delta$ cancel exactly, since $G$ is even and $D_{\delta,y}(-\delta)=X_\delta(y)D_{-\delta,y}(\delta)$. Both residues have the same additional factor $(mn/g^2)^{-1/2}$. The new contours are uniformly $O(Y^{-\epsilon})$ after all twists: the gamma ratio is $O(Y^{-1/4})$ times an integrable polynomial-Gaussian majorant on the line, $X_\delta\ll1$, and summing the worst extra $(mn/g^2)^{1/4}$ against $|a_m a_n|$ costs at most $O(K^{1.52})$. The remaining two $z=0$ residues are
$$
 \zeta(1+2\delta)\sum_{m,n}a_m\overline{a_n}(g^2/(mn))^{1/2+\delta}
 +X_\delta\zeta(1-2\delta)\sum_{m,n}a_m\overline{a_n}(g^2/(mn))^{1/2-\delta}.       \tag{3}
$$
The first term is the complete ordinary Dirichlet-series diagonal. The second is nonpositive pointwise. Indeed $\zeta(1-2\delta)<0$ and $g^{1-2\delta}=\sum_{e|g}J_{1-2\delta}(e)$ with $J_v(e)=e^v\prod_{p|e}(1-p^{-v})\ge0$ for $v>0$. After the separable powers of $m,n$ are absorbed, each divisor contributes a nonnegative multiple of a squared modulus. Integrating against $W\ge0$, then using the first moment to subtract the constant coefficient, proves (2).
