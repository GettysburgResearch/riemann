# Exactly how much decay of the compressed translation detects a zeta zero

**Proposed theorem for review.** Write $\Theta=\sup_\rho\Re\rho$ over the nontrivial zeros of the Riemann zeta function. Use the right Hardy half-plane $\mathcal H=H^2(\Re z>0)$, with boundary measure $dy/(2\pi)$. Form the meromorphic inner function and its model space
\[
 I(z)=\frac{\xi(z-1/2)}{\xi(z+3/2)},\qquad K=\mathcal H\ominus I\mathcal H.
\]
Let $P$ project orthogonally onto $K$ and $M_f$ denote multiplication. For $t,\alpha\ge0$ set
\[
 D_\alpha(t)=\left\|P M_{e^{-tz}(2+z)^{-\alpha}}\big|_K\right\|.
\]
The principal branch gives the power. Then
\[
 \boxed{\displaystyle\lim_{t\to\infty}\frac{-\log D_\alpha(t)}t
       =\min\{\alpha,\,3/2-\Theta\}.}                                      \tag{1}
\]
In particular $D_0(t)=1$ for every $t$. For every $t>0$ the adjoint of the unsmoothed compressed translation has the entire closed unit disk as its approximate point spectrum. Yet for $\alpha=1$ the bound $D_1(t)\ll_\epsilon e^{-(1-\epsilon)t}$ for every $\epsilon>0$ is equivalent to RH. The norm in (1) concerns the actual xi quotient. The last bound remains open.

Suzuki studied this quotient as the $\omega=1$ member of his family, including innerness and the Jordan totient kernel. His results supply that input here. In our coordinates innerness also follows by taking modulus ratios in the paired Hadamard product of the even entire function $X(z)=\xi(1/2+z)$: the numerator zeros are $1+\rho-1/2$, each denominator zero is the reflection of one of them across the imaginary axis, the boundary modulus is one, and the exponential factor at positive real infinity has zero mean type. The innerness theorem alone suffices below. [Suzuki, §§2–4](https://arxiv.org/abs/1204.1827)

## How small the quotient is on an interior vertical line

The zeros of $I$ in the half-plane are precisely $\lambda=1/2+\rho$. Write $d_*=3/2-\Theta$, their infimum of real parts by symmetry. There is no cancellation because $\xi(z+3/2)$ is zero-free there. Using the functional equation to reflect the numerator gives
\[
 |I(x+iy)|=\left|\frac{\xi(3/2-x-iy)}{\xi(3/2+x+iy)}\right|.
\]
For every fixed $0<x<1/2$, both zeta factors here have absolutely convergent Euler products. Stirling's estimate therefore gives
\[
 |I(x+iy)|\asymp_x(1+|y|)^{-x}.                                      \tag{2}
\]
For every $0<d<d_*$ and $\eta>0$ it also gives, uniformly on $0\le x\le d$,
\[
 |I(x+iy)|^{-1}\ll_{d,\eta}(1+|y|)^{x+\eta}.                         \tag{3}
\]
For detail on the zeta factor in (3), take $\sigma_0=3/2-d>\Theta$. At large $|y|$, use concentric disks centered at $2+iy$ of radii $r_0<r_1<r_2<r_3<2-\Theta$, with $r_0<1$, $r_1>2-\sigma_0$, and all radii fixed. Normalize the logarithm of $\zeta$ by its Dirichlet series at the center. It is bounded on the smallest disk. On the largest disk the real part of the logarithm is $O(\log |y|)$ by polynomial growth of zeta on fixed strips. Borel–Carathéodory on radius $r_2$ and the three-circles theorem on radius $r_1$ give $|\log\zeta|\ll (\log |y|)^q$ with a fixed $q<1$. This implies the subpower reciprocal bound used in (3). On bounded ordinates use continuity of the completed quotient in this closed strip, including the removable values of $\xi$.

## Two independent lower bounds on the norm

At a zero $\lambda$ of $I$, the ordinary Hardy reproducing kernel lies in $K$ and is an eigenvector of the adjoint compressed multiplier with eigenvalue $\overline{e^{-t\lambda}(2+\lambda)^{-\alpha}}$. Thus the decay exponent in (1) has upper limit at most $d_*$, also when the infimum is unattained.

A second obstruction comes from high ordinates and uses no zeros individually. Let $k_s$ be the unit Hardy kernel at $s=x+iy$, so $\|(1-P)k_s\|=|I(s)|$. For $f=e^{-tz}(2+z)^{-\alpha}$ one has $P M_f=P M_f P$ by invariance of $I\mathcal H$. Testing on $k_s$ therefore gives
\[
 D_\alpha(t)\ \ge\ |f(s)|-|I(s)|\,\|f k_s\|_2.                      \tag{4}
\]
For $0\le\alpha\le1$, Poisson integration and concavity of $u^\alpha$ bound
\[
 \|f k_s\|_2\le
 \left[\frac{2+x}{2((2+x)^2+y^2)}\right]^{\alpha/2}.
\]
Indeed the square of the norm is the Poisson average of $(4+v^2)^{-\alpha}$ at $x+iy$, and the Poisson average of $(4+v^2)^{-1}$ is the quantity in brackets. Fix $0<x<1/2$ and put $y=L e^t$, with $L$ large depending on $x,\alpha$. By (2) the second term on the right of (4) is at most half the first for all large $t$. This yields $D_\alpha(t)\gg_{x,\alpha}e^{-(x+\alpha)t}$. Let $x\downarrow0$. For $\alpha>1$ the zero bound already suffices since $d_*\le1$.

For fixed $t>0$, $x\in(0,1/2)$, and $y\to\infty$, the vectors $Pk_s$ have norm tending to one. Applying the adjoint compressed translation to them differs from multiplication by $e^{-t\bar s}$ by at most $2|I(s)|$. In fact (2) extends to $I(x+iy)\to0$ at every fixed $x>0$: by the Riemann–von Mangoldt estimate there are $\gg\log |y|$ zeros in $[y-R,y+R]$ for a sufficiently large absolute constant $R$. To see this subtract the two counts with errors $O(\log |y|)$ and then choose $R$ to dominate those constants. Each corresponding half-plane Blaschke factor at $x+iy$ has modulus at most a fixed $q(x,R)<1$ because the zero's real part is between $1/2$ and $3/2$. Schwarz's lemma applied successively to this finite list bounds $|I(x+iy)|$ by their product. Choosing $y$ in an arithmetic progression realizes every desired phase of $e^{-t\bar s}$. Varying $x>0$ and taking closure proves the whole-disk assertion and hence $D_0(t)=1$. At $t=0$ the latter is immediate.

## An explicit holomorphic approximation for the reverse bound

Assume $\alpha>0$ and take $0<b<d<\min(\alpha,d_*)$. Choose a smooth real $\chi(x)$ equal to one on $x\le b$ and zero on $x\ge d$. Define $h_0=\chi f/I$ on $x<d$, and set it to zero on $x\ge d$. It is bounded by (3). Its $\bar\partial$ derivative is supported on $b\le x\le d$ and satisfies, for some $\nu>0$,
\[
 |\bar\partial h_0(x+iy)|\ll e^{-bt}(1+|y|)^{-\nu}.                  \tag{5}
\]
Here take $\nu=\alpha-d-\eta>0$. Extend the derivative by zero outside that strip. Its planar Cauchy transform $u$ solves $\bar\partial u=\bar\partial h_0$ in the half-plane and $\|u\|_\infty\ll e^{-bt}$. For the uniform bound, the part within unit distance of the evaluation point uses local integrability of $1/|z|$. The remaining part within unit vertical distance is over bounded area and has kernel at most one. On larger vertical separations use Hölder in the ordinate, with $p>\max(1,1/\nu)$ for the weight and its conjugate exponent for $|v|^{-1}\mathbf1_{|v|>1}$. These estimates are uniform in the center and $t$.

Consequently $h=h_0-u$ is bounded and holomorphic. We have
\[
 f-Ih=(1-\chi)f+Iu,\qquad \|f-Ih\|_\infty\ll e^{-bt}.
\]
The compression of $M_{Ih}$ vanishes. Thus $D_\alpha(t)\ll_b e^{-bt}$, proving the matching lower limit in (1).

## The arithmetic entering this operator

Gamma recurrence in the unreflected quotient gives exactly
\[
 I(z)=2\pi\frac{z-3/2}{(z+3/2)(z+1/2)}
              \frac{\zeta(z-1/2)}{\zeta(z+3/2)}.
\]
For $\Re z>3/2$ the last ratio is $\sum J_2(n)n^{-3/2-z}$, where $J_2(n)=\sum_{d\mid n}\mu(d)(n/d)^2$. By partial fractions, the inverse Laplace kernel at $u\ge0$, $X=e^u$, is
\[
 i(u)=2\pi X^{-3/2}\sum_{d\le X}\mu(d)\lfloor X/d\rfloor(\lfloor X/d\rfloor+1)
                             (1/2-\{X/d\}).                          \tag{6}
\]
At jumps use the right limit. Indeed the two terms of the partial fraction are $3/(z+3/2)-2/(z+1/2)$. Summing their inverse transforms for $m\le X/d$ uses $3\sum m^2-2(X/d)\sum m=\lfloor X/d\rfloor(\lfloor X/d\rfloor+1)(1/2-\{X/d\})$. The time evolution with this kernel is fully specified by ordinary integers. Equation (1) answers which decay would suffice. Obtaining that decay from (6) without a right-hand zero-free hypothesis is the unresolved arithmetic step.
