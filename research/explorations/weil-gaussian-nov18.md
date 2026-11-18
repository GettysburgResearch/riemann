# Frequency-local Weil matrices with a quantitative negative margin

**Status.** Proposed refinement of [the finite matrix criterion](weil-sampling-nov18.md). All constants are absolute and unevaluated. A Gaussian centered at the search height controls the norm of the witness. The argument gives a finite resolution criterion and does not establish positivity of its arithmetic matrices.

## The local matrix

Fix a center $X\ge100$ and a resolution $0<d<1/2$. Set $H=(1+\log(1/d))\log X$. Assume $H/X$ is smaller than an absolute positive constant and $X$ is sufficiently large. With sufficiently large absolute $C,C'$ set
$$
 S=X/(2\pi)+C\sqrt{XH},\qquad L=\tfrac12\log S,\qquad
 J=\{k\in\mathbb Z:|k\pi/L-X|\le C'\sqrt{XH}\}.
$$
Use the preceding trial functions $g_k=(2L)^{-1/2}\chi(x)e^{-ik\pi x/L}$ for $k\in J$, with the same smooth cutoff supported in $(-L,L)$ and equal to one through $L-2/S$ in absolute value. Let $A_{jk}=W(g_k,g_j)$.

**Theorem.** If there is a zeta zero at height $T$ with $|T-X|\le\sqrt{XH}$ and displacement $\delta\ge d$, then
$$
 \lambda_{\min}(A)\le -\exp(-C_0 H)
$$
for some absolute $C_0>0$. Thus a lower bound strictly greater than this threshold would exclude all such defects. The dimension is $O(\sqrt{XH}\log X)$ and the prime-power cutoff is $S$. For fixed displacement resolution the required absolute eigenvalue accuracy is polynomial in $X$. This is an existence estimate for the precision exponent.

## 1. A source that decays on both sides of the search frequency

Take $h=(H/X)^{1/2}$, $\theta=\pi/4-h$ and define the entire source
$$
 F(z)=e^{\pi z/4-(z-X)^2/X}\Xi(z)
 =e^{hX+Xh^2/4}\, e^{-(z-X-Xh/2)^2/X}\,F_\theta(z).
$$
Use the two cluster circles from the [contour proof](weil-contour-nov18.md), at the hypothetical defect. On both circles $|F(v)|^{-1}\le e^{C_1H}$: the reciprocal gamma exponential cancels against $e^{\pi\Re v/4}$, while $|\Re v-X|\le\sqrt{XH}+1$. On the whole real line
$$
 |F(t)|\ll(2+|t|)^B e^{-(t-X)^2/X}
$$
by Stirling and polynomial growth of zeta. The cluster projector $f_\infty$ formed from the inverse Fourier source of $F$ thus obeys
$$
 |\widehat f_\infty(t)|\ll e^{C_1H}(2+|t|)^B e^{-(t-X)^2/X}.
 \tag{1}
$$
Indeed every real $t$ is outside both disks, its distance to each contour is at least $\delta/2$, and each contour length is at most $\pi\delta$. Integrating the divided difference as in the contour proof gives (1) even at frequencies very close to $T$. In particular the exact projector has squared $L^2$ norm $\le e^{C_2H}$.

## 2. Spatial tail of the source

Write $\Psi$ for the inverse Fourier transform of $F$. Completing the square as above expresses $\Psi$ as the convolution of $\Phi_\theta$ with a modulated Gaussian of absolute value $\sqrt{X/(4\pi)}e^{-Xv^2/4}$, times $e^{hX+Xh^2/4}$. For $j=0,1,2$ the shifted theta series gives the global bound
$$
 |\Phi_\theta^{(j)}(y)|\le C h^{-B'}e^{B'|y|}\exp(-\pi\sin(2h)e^{2|y|}).
$$
Indeed, with $s=\sin(2h)e^{2|y|}$, the sum of $n^{B''}e^{-\pi(n^2-1)s}$ is $O(1+s^{-B'''})$, and $s\gg h$. Evenness and analytic continuation give the negative-real-direction bound.

Put $x_0=L-2/S$ and $b=\pi\sin(2h)e^{2x_0}$. For $|x|\ge x_0$ use the convex tangent inequality
$$
 e^{2|x-v|}\ge e^{2x_0}[1+2(|x|-x_0)-2\operatorname{sgn}(x)v].
$$
After differentiating the theta factor in the convolution, this gives
$$
 |\Psi^{(j)}(x)|\ll h^{-B'}\exp\!\left(hX+Xh^2/4-b+
 B'|x|-2b(|x|-x_0)+O((b+1)^2/X)\right).
 \tag{2}
$$
Here the Gaussian exponential moment absorbs $B'|v|+2b\,\operatorname{sgn}(x)v$. The bound holds on the entire unbounded physical tail; it uses one tangent point $x_0$ throughout.

At $S=X/(2\pi)+C\sqrt{XH}$,
$$
 b=hX+2\pi C H+O(Xh^3+C H h^2+1).
$$
First choose $C$ large, then require $H/X$ sufficiently small in terms of this fixed constant. This ensures $b\le2hX$, the $O((b+1)^2/X)$ cost in (2) is $O(H)$ with an absolute constant independent of $C$, and $b-hX\ge \pi C H$. Also $Xh^2=H$, $|\log h|+\log(1+S)=O(H)$, and $b\to\infty$. Consequently, even after paying the reciprocal contour factor $e^{C_1H}$, (2) yields a tail at $x_0$ of size $O_M((1+S)^{-M})$ for any fixed $M$ by making the choices in this order. Beyond $x_0$ there is exponential decay at rate at least $b$. Integrating $\Psi^{(j)}(x\pm t)e^{\pm ivt}$ over $t\ge0$ for the two divided-difference formulas preserves these estimates, since $|\Im v|\le3/4$.

The Gaussian convolution has all two-sided exponential moments at each fixed $X,h$ (both factors do), so its Fourier transform is entire. The divided-difference identity, cluster evaluations, and their multiplicities therefore hold exactly as in the original projector.

## 3. Sampling, cutoff, and ordinary eigenvalue

Periodize $f_\infty$ on $[-L,L]$ and keep only the modes $k\in J$. By (2), the noncentral copies cost $O_M((1+S)^{-M})$ in the first two derivatives. By (1), omitting the frequencies beyond $C'\sqrt{XH}$ costs the same. To see the latter, retain half the Gaussian for summability against any fixed polynomial in $|k|\pi/L$, and use the other half to gain $\exp(-C'^2 H/2)$. Gaussian lattice sums of fixed polynomial degree cost at most a fixed power of $2+X+L$, absorbed by taking $C'$ large. Multiplication by $\chi$ now gives $g=\sum_{k\in J}a_k g_k$ with evaluation error on the full zero multiset at most $1/4$ in $\ell^2$, by the same weighted two-derivative argument as in the fixed matrix proof. Hence $W(g)\le-2m+2\sqrt{2m}/4+1/16\le-1$ for $m\ge1$.

The actual coefficient vector satisfies
$$
 a_k={1\over\sqrt{2L}}\widehat f_\infty(k\pi/L),\qquad
 \sum_{k\in J}|a_k|^2\le e^{C_0H}.
$$
This follows directly from (1), the number of modes and $H\ge\log X$; it needs no lower frame bound for the cutoff functions. Dividing the negative value by this upper bound proves the assertion about the ordinary eigenvalue of $A$.

**Remaining arithmetic question.** The matrix uses modulations close to $X$ and the stated prime-power cutoff. A rigorous lower bound for its smallest eigenvalue to this precision, uniformly in $X$ and at every displacement resolution, would be new arithmetic input.
