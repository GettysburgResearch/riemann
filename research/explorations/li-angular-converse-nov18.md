# A finite-index Li converse from angularly localized positive weights

**Status.** Proposed analytic theorem. The only zeta inputs beyond the symmetric Li identity are the critical strip, the functional equation and the classical local zero count $N(t+1)-N(t)\ll\log(2+t)$. The argument allows every other zero and all multiplicities. The absolute constants are not evaluated. Prior literature on finite Li criteria includes Francis Brown, *Li's criterion and zero-free regions of L-functions* (2005); this note makes no claim about priority or the correctness of other proofs. [Brown](https://doi.org/10.1016/j.jnt.2004.07.016)

## 1. Statement

If there is an off-line zero, put
$$a=\max_\rho \log|1-1/\rho|>0,\qquad \ell=\log(2/a).$$
Then $\lambda_n<0$ for some integer $1\le n\le C a^{-1}\ell^2$, for an absolute $C$. In particular, if $\lambda_1,\ldots,\lambda_N\ge0$, each zero $\rho=\beta+i\gamma$ satisfies
$$
 |\beta-1/2|\ll (1+\gamma^2){\log^2(2N)\over N}.
$$
A finite run excludes defects beyond the indicated displacement resolution.

Write $z_\rho=1-1/\rho=r_\rho e^{i\theta_\rho}$ with the principal argument. Reflection pairs $r$ with $1/r$. The squared moduli give $|\log r_\rho|\le |\beta-1/2|/\gamma^2\le 1/(2\gamma^2)$; they also give $|\log r_\rho|\ge|\beta-1/2|/(1+\gamma^2)$ by $\log(1+v)\ge v/(1+v)$. Thus the maximum is attained if positive. We may use $|\gamma|\ge 14$ from the established first zero, so $0<a<1/2$. Let $\theta_*$ be the argument of one zero attaining the maximum.

**Published predecessor.** Nea Palojärvi, Theorem 3.1, gives a finite converse for a broader class of functions and $\tau$-Li coefficients, with explicit constants and a sparse set of tested indices. Specializing to zeta and $\tau=1$, its transform is $\rho/(\rho-1)$, the reciprocal of ours, which has the same multiset of moduli and real power sums by the zeta symmetries. For $R=e^a\downarrow1$, its prescribed integer $N_0$ is of order $a^{-1}\log(1/a)$ by the negative Lambert $W$ branch in its formula. It tests multiples of $N_0$ in $[N_0,5N_0^2(A_F\log N_0+M_F)]$, whose largest index is $O(a^{-2}\log^3(1/a))$. The bound proved here concerns the largest index for zeta, with unevaluated constants; the indices in our angular filter occupy short blocks, and need not be multiples of one specified integer. Palojärvi distinguishes Brown's existing finite converse (Theorem 3) from the issue with Brown's Theorem 2 in the opposite direction. [Palojärvi, pp. 1–2 and Theorem 3.1](https://arxiv.org/pdf/1807.01506)

## 2. A power sum with a one-sided, angularly decaying lower bound

Choose integers $D=\lceil1/a\rceil$, $K=\lceil C_1\ell\rceil$, $m=\lceil C_2\ell/a\rceil$, with absolute constants chosen in that order and $m\ge2D$. Define
$$
 B_D(z)=D^{-2}\Big(\sum_{s=0}^{D-1}z^s\Big)\Big(\sum_{s=0}^{D-1}z^{-s}\Big),\quad
 F(z)=B_D(z)\sum_{j=1}^{K}\left(1-{j\over K+1}\right)z^{mj}.
$$
Though $B_D$ is Laurent, $F(z)=\sum c_nz^n$ is an ordinary polynomial with $c_n\ge0$, supported on $m-D+1\le n\le Km+D-1$. Its coefficient sum is $K/2$. Let $d(\theta)$ denote distance to $2\pi\mathbb Z$.

For $0<|z|\le1$ we claim
$$
 \Re F(z)\ge {-C_3\over(1+Dd(\arg z))^2}.
 \tag{1}
$$
Write $z=e^{-u+i\theta}$, $u\ge0$. The unit-circle value $B_D(e^{i\theta})$ is nonnegative and at most $C(1+Dd(\theta))^{-2}$. Moreover for $0\le u\le1$,
$$
 |B_D(e^{-u+i\theta})-B_D(e^{i\theta})|
 \le {C D u\, e^{D u}\over(1+Dd(\theta))^2}.
 \tag{2}
$$
To verify this, write $b(v)=B_D(e^v)=(\sinh(Dv/2)/(D\sinh(v/2)))^2$. The finite Laurent sum bounds $|b(v)|\le e^{D|\Re v|}$ everywhere. If $d(\Im v)\ge1/D$, then $|\sinh(v/2)|\ge|\sin(\Im v/2)|\gg d(\Im v)$ and $|\sinh(Dv/2)|\le e^{D|\Re v|/2}$. Combining these gives $|b(v)|\ll e^{D|\Re v|}(1+Dd(\Im v))^{-2}$. Cauchy's derivative estimate on a circle of radius $1/(2D)$ preserves this bound up to an absolute constant and a factor $D$. Integrating along $[-u,0]+i\theta$ proves (2), in fact for every $u\ge0$.

The real part of $\sum_{j=1}^K(1-j/(K+1))w^j$ is at least $-1/2$ for $|w|\le1$, by the Fejér identity and harmonic extension. Apply this with $w=z^m$ and the nonnegative *unit-circle* value of $B_D$. The error from replacing $B_D(z)$ by that value is bounded by (2) times $\sum_{j\ge1}e^{-mju}$. For $u>0$ the extra scalar $Du e^{Du}/(e^{mu}-1)$ is absolutely bounded, since $m\ge2D$. At $u=0$ there is no error. This proves (1).

Set
$$Q(z)=F(z)+\tfrac12F(e^{i\theta_*}z)+\tfrac12F(e^{-i\theta_*}z)
 =\sum c_n(1+\cos(n\theta_*))z^n.$$
Its coefficients are nonnegative and sum to at most $K$. For the selected $z_\rho e^{-a}=e^{i\theta_*}$, the last summand contributes $F(1)/2=K/4$. Each other summand and all summands for all the other normalized roots have the lower bound (1) with the corresponding angular translate.

## 3. At most logarithmically many competing phases per angular cell

Call the ordinates with $|\gamma|\le a^{-1/2}$ the low set. It contains the extremal root by $a\le1/(2\gamma^2)$. For $\gamma>0$,
$$
 \theta_\rho=\arctan(\beta/\gamma)+\arctan((1-\beta)/\gamma)
 =1/\gamma+O(\gamma^{-3}).
$$
For negative $\gamma$ conjugate the identity. In particular $1/|\theta_\rho|=|\gamma|+O(1/|\gamma|)$ and $|\theta_\rho|\gg\sqrt a$ on the low set. Angles of the same sign in an interval of length $1/D$ therefore correspond to ordinates in an interval of bounded length: the difference of their reciprocal angles is at most $1/(D c^2 a)=O(1)$. The local count gives $O(\ell)$ zeros, with multiplicities, per such cell. Splitting signs handles a cell meeting zero. These arguments are within the principal angular interval; periodically indexing cells makes the same conclusion valid for translates.

Summing the inverse-square angular bound cell by cell consequently gives, for each shift $\alpha=0,\pm\theta_*$,
$$
 \sum_{\rm low}(1+Dd(\theta_\rho-\alpha))^{-2}\ll \ell.
$$
It follows that $\sum_{\rm low}\Re Q(e^{-a}z_\rho)\ge K/4-C_4\ell$. The positive target contribution is retained once; dropping it from an otherwise lower-bounded sum can only save its allocated lower-bound cost. Choose $C_1$ large enough that the displayed lower bound is at least $K/8$.

## 4. Middle and infinite tails, including the Li subtraction

Let $n_+=Km+D$ and $Y=(n_++2/a)^2$. For $a^{-1/2}<|\gamma|\le Y$, $|e^{-a}z_\rho|\le e^{-a/2}$. Since the minimum nonzero index of $Q$ is at least $m-D$,
$$
 |Q(e^{-a}z_\rho)|\le K e^{-a(m-D)/2}.
$$
The real subtraction per zero is $Q(e^{-a})\le K e^{-a(m-D)}$. Applying the latter bound to **all** zeros through $Y$, the total cost of the middle contributions and those subtractions is $\ll K e^{-a(m-D)/2}Y\log(2Y)$.

On the infinite tail $|\gamma|>Y$, take real contributions before summing, as in the symmetric Li formula. Since $|\theta_\rho|\ll1/|\gamma|$ and $|\log r_\rho|\le1/(2\gamma^2)$,
$$
 |1-\Re z_\rho^n|\ll (n+n^2)\gamma^{-2}
 \quad(1\le n\le n_+,\ |\gamma|>Y).
$$
Indeed use $|1-r^n|\le n|\log r|e^{n|\log r|}$ and $0\le1-\cos(n\theta)\le n^2\theta^2/2$. The tail $\sum_{|\gamma|>Y}\gamma^{-2}\ll \log(2Y)/Y$ follows by dyadic summation. Thus the contribution of this whole tail to the weighted Li sum is absolutely at most
$$
 C_5 K e^{-a(m-D)} n_+^2\,\log(2Y)/Y.
$$
After $C_1$ is fixed, take $C_2$ sufficiently large. Both tail costs together are then at most $K/16$ uniformly for $0<a<1/2$: $Y\ll(1+C_1)^2(1+C_2)^2\ell^4/a^2$, whereas the factor $e^{-a(m-D)/2}\ll (a/2)^{C_2/2}$ absorbs the powers, logarithms, and fixed constants even at the upper endpoint.

Finally the weighted sum is
$$
 \sum_n c_n(1+\cos(n\theta_*)) e^{-an}\lambda_n
 =\sum_\rho \left(Q(e^{-a})-\Re Q(e^{-a}z_\rho)\right)<0.
$$
The infinite right side is grouped by conjugation, as justified above. The left weights are nonnegative. Therefore some $\lambda_n<0$ within the asserted range. If the first $N$ are nonnegative, $N<C a^{-1}\log^2(2/a)$ whenever $a>0$. If $a\le1/N$ the stated zero bound is immediate, and otherwise $\log(2/a)\le\log(2N)$, giving the result.

**Scope.** The argument does not give exact critical-line membership from finite positive coefficients. Relative to the single-defect heuristic, the possible coherent competitors in one angular cell cost a logarithmic factor.
