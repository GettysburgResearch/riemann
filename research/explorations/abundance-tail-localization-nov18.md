# Wrong signs of the limiting abundance-tail estimate on every proportional threshold window

Suppose RH fails. Fix $1/2<c<\Theta$ and $0<\eta<1$. For either limiting arithmetic distribution in the [abundance-tail criterion](abundance-curvature-nov18.md), every sufficiently large real interval $[(1-\eta)T,T]$ contains thresholds $t_+,t_-$ satisfying
$$
 \mathcal E_Z(t_+)> y(t_+)^c,\qquad \mathcal E_Z(t_-)<-y(t_-)^c,
 \qquad y(t)=\exp(t e^{-\gamma_E}).
$$
Here $\mathcal E_Z$ is the signed remainder in Weingartner's Theorem 2. In particular, the eventual search for one of the two signs can be restricted to windows of a fixed relative width at arbitrarily sparse thresholds. The result uses no assumption that the supremum of real parts is attained.

## Removing logarithmic branches from the smoothing calculation

First work with $D(s)=W_\phi(s)-W_*(s)$ and $G(z)=\int_1^\infty s^{-z-1}D(s)ds$ on $\Re z>1$. Use (2)–(4) in the [Mellin proof](abundance-curvature-nov18.md), retaining $B=3/4$ for the cutoff denoted there by $T$ and $A(t)=\pi t/\sin(\pi t)$. In its initial strip replace $P(z+t)$ by $-\int_0^\infty P'(z+t+v)dv$. After interchanging the two real integrals,
$$
 G(z)=\frac{1}{z(z-1)\Gamma(z)}
   \int_0^\infty H(z,r)P'(z+r)dr+E_1(z),\quad
 H(z,r)=-\mathbf1_{r<B}r^{z-1}A(r)+\int_0^{\min(r,B)}t^{z-1}A'(t)dt .
 \tag{1}
$$
The remaining $E_1$ is holomorphic on $1/2<\Re z<2$ apart from a possible simple pole at 1, from the division used in passing from curvature to values. The full expression has no real pole at 1 by the derivative anchor and $D=o(s)$, as proved in the linked note. The function $P'$ is meromorphic on $\Re z>1/2$, with residue $m_\rho$ at a zeta zero of multiplicity $m_\rho$, and no pole at 1. Thus the $r$ integrands have ordinary poles, with no branch choices at the nontrivial zeros. For large $r$ the original formula for $P'(z+r)$ decreases exponentially in $r$ on compact $z$ sets.

## A Gaussian isolates a conjugate pair in the leading asymptotic

Let $\lambda(z)=z+\epsilon z^2$, with $\epsilon>0$. Gaussian averaging of $D(e^v)\mathbf1_{v\ge0}$ at center $u$ and variance $2\epsilon u$ equals
$$
 \frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}G(z)e^{u\lambda(z)}dz ,
 \qquad a=3/2 .
$$
This follows directly by Fourier inversion of the Gaussian and absolute convergence on the original line. Fix a zero $\rho_0$ with $\beta_0>c$. Choose $c<b<\beta_0$ and then $\epsilon$ sufficiently small that $\Re\lambda(\rho_0)> b+\epsilon b^2$. Take a fixed height $K>|\Im\rho_0|$ off all zero ordinates so $a+\epsilon a^2-\epsilon K^2<b$. The omitted original-line tails cost $O(e^{bu})$. The rectangle of bounded height permits all subsequent constants to depend on $K$.

With (1), move each $z$ integral for fixed $r$ to $\Re z=b$. Values of $r$ where a pole lies on that line form a finite set of measure zero. All horizontal boundary contributions are $O(e^{bu})$. The new vertical integrals together cost $O(e^{(b+\epsilon b^2)u})$. To justify the latter bound, at an intersection $z+r=\rho$ the local singularity in the two integration variables $r,\Im z$ is $O(1/|z+r-\rho|)$, locally integrable in two real dimensions. One may choose $b$ avoiding the finitely many real parts of zeros inside the rectangle so these intersections are away from $r=0$. The factor $r^{b-1}$ there is integrable. Contributions for $r>B$ pose no singularity on the rectangle since $b+B>1$. Terms from $z=1$ cancel on summing the $r$ integral and $E_1$ by the removability just noted.

The remaining contributions are a finite sum over zeros with $b<\beta<1$, $|\gamma|<K$, of
$$
 m_\rho\int_0^{\beta-b}\frac{H(\rho-r,r) e^{u\lambda(\rho-r)}}
 {(\rho-r)(\rho-r-1)\Gamma(\rho-r)}dr .
$$
Here $\beta-b<B$, and $H(\rho-r,r)=-r^{\rho-1}(1+O_\rho(r|\log r|))$ at zero. The real exponential decreases away from zero since $\Re(1+2\epsilon\rho)-\epsilon r>0$. Endpoint Laplace integration gives the asymptotic contribution
$$
 \frac{m_\rho e^{u\lambda(\rho)}u^{-\rho}}
 {\rho(1-\rho)(1+2\epsilon\rho)^\rho}\,(1+O_\rho(\log u/u)).
$$
The complex power uses the log in the right half-plane. The formula follows by $r=v/u$, exponential domination, and $\int_0^\infty v^{\rho-1}e^{-(1+2\epsilon\rho)v}dv=\Gamma(\rho)/(1+2\epsilon\rho)^\rho$.

Maximize $A=\Re\lambda(\rho)$ over this finite list and then minimize $\beta$ among maximizing terms. The latter select a single conjugate pair: fixed $A$ and $\beta$ determine $|\gamma|$ uniquely. Its coefficient is nonzero. All other terms are little-oh on the corresponding $e^{Au}u^{-\beta}$ scale. The leading phase has derivative $\Im\lambda(\rho)-\gamma/u$ tending to a nonzero constant. Therefore both signs with fixed proportional amplitude occur in bounded distances from every sufficiently large Gaussian center.

## Returning to ordinary thresholds

Choose $\delta>0$ sufficiently small that $c(1+\delta)<\beta_0$, and subsequently $\epsilon$ sufficiently small that $A>c(1+\delta)$. Truncating each Gaussian to $|v-u|\le\delta u$ costs $o(1)$ on making $\epsilon$ smaller still: $D(e^v)=O(e^v)$ for $v\ge0$, and completing the square bounds the cost by $O(\exp(u[1+\epsilon-(\delta-2\epsilon)^2/(4\epsilon)]))$. Positivity of the remaining measure of mass at most one gives ordinary moment values of either sign exceeding $e^{cv}$ in absolute value. Choosing the Gaussian centers strictly inside any prescribed log-power window and $\delta$ small compared with its relative width gives both signs on every sufficiently large $s\in[S^{1-\eta},S]$. The same holds for the divisor-sum moment since its difference from the totient moment is $O(\sqrt{s/\log s})$.

To transfer the claim to the tails, work temporarily in the $y$ coordinate, where a proportional threshold window is $[Y^{1-\eta},Y]$. Choose a strict interior power window for $s$ and a small fixed $\eta_1>0$ so that $[s^{1-\eta_1},s^{1+\eta_1}]\subset[Y^{1-\eta},Y]$ for every $s$ in this interior window. If $\mathcal E_Z\le y^c$ throughout the larger window, the upper moment-integral comparison in the proof of (5) of the linked note applies on this central $y$ range, with its two outside tails negligible by the same unconditional estimates. It gives $D_Z(s)\le O(s^{c(1+\eta_1)}+\log s)$ on the whole interior. The reverse one-sided assumption gives $D_Z(s)\ge-O(s^{c(1+\eta_1)}+\log s)$ by integrating only near the model saddle. The model differs from the published remainder by $O(1)$. Choose $\eta_1$ so $c(1+\eta_1)<\Theta$ and apply the ordinary moment conclusion with a strictly larger exponent below $\Theta$. This excludes either one-sided assumption at every sufficiently large scale, as claimed.
