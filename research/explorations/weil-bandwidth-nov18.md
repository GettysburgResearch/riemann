# The local Weil test with polylogarithmically many modes

**Status.** Proposed analytic bandwidth refinement. This note uses the complete proofs of the [Gaussian projector](weil-gaussian-nov18.md) and the [exterior estimate](weil-local-complement-nov18.md). All constants are absolute and unevaluated. In particular this is not an implemented certification algorithm.

Let $X\ge100$ be large, $0<d<1/2$, $H=(1+\log(1/d))\log X$. Let $K$ be sufficiently large and select a bandwidth
$$
 K H\le B\le \sqrt{XH}.
$$
Use
$$
 S=X/(2\pi)+CXH/B,\qquad L=\tfrac12\log S,\qquad
 J=\{k\in\mathbb Z: |k\pi/L-X|\le C'B\}.
$$
Define the same arithmetic matrix in the normalized modulated cutoff basis, taking the rescaled convolution cutoff from the exterior estimate with its width set to $H/B$ (and $m=\lceil H\rceil$). The constants are chosen in the order specified below.

**Theorem.** A zeta defect of displacement at least $d$ with $|T-X|\le B$ forces an eigenvalue $\le-\exp(-C_0H)$. Conversely, for any prescribed fixed $a>0$ there exists a fixed $D>0$ such that, if all zeros with $|T-X|\le DB$ have displacement at most $\epsilon$, then
$$
 \lambda_{\min}(A)\ge -e^{-aH}-C_D\epsilon^2 e^{2\epsilon L}L^3 B\log X.
$$
The matrix dimension is $O(B\log X)$ and the arithmetic cutoff is $S$. For fixed $d$ and any fixed $\tau>0$, choosing $B=K_\tau H$ with $K_\tau$ sufficiently large gives $L\le\frac12\log(X/(2\pi))+\tau$ and dimension $O_{d,\tau}((\log X)^2)$. If $H=o(X)$, one can instead let $B/H\to\infty$ arbitrarily slowly subject to the displayed bandwidth range; then the additive excess radius tends to zero.

## Proof of the changes of scale

Put $V=B^2/H$ and $h=B/X$. Replace the Gaussian in the projector by
$$
 F(z)=\exp\!\left(\pi z/4-(z-X)^2/V\right)\Xi(z).
$$
The reciprocal on either circle is $\le e^{C_1H}$, since $(|T-X|+1)^2/V=O(H)$. The real-frequency projector bound is
$$
 |\widehat f_\infty(t)|\ll e^{C_1H}(2+|t|)^{C_2}\exp(-(t-X)^2/V).
$$
Consequently the exterior lattice frequencies $|t-X|>C'B$ cost $\exp(-C'^2H/2)$ times polynomial factors, and the squared norm of the retained coefficients is at most $\exp(C_0H)$ just as before. Both estimates are uniform in $B$.

Set $\theta=\pi/4-h$. Completing the square extracts the prefactor $\exp(hX+Vh^2/4)$ times the shifted theta source convolved against a modulated Gaussian of absolute value $\sqrt{V/(4\pi)}e^{-Vv^2/4}$. The differentiated convolution estimate in the Gaussian proof becomes
$$
 |\Psi^{(j)}(x)|\ll h^{-C_2}\exp\!\left(hX+Vh^2/4-b+
 C_2|x|-2b(|x|-x_0)+O((b+1)^2/V)\right)
$$
for $|x|\ge x_0=L-3H/(4B)$, where $b=\pi\sin(2h)e^{2x_0}$. The choice of $x_0$ is the beginning of the cutoff's plateau transition. The same tangent inequality and Gaussian moment prove this estimate for every $j\le2$.

Here $hX=B$ and $Vh^2=B^4/(HX^2)\le H$. More explicitly,
$$
 b=\big(B+2\pi C H\big)\big(1+O(h^2)\big)\exp(-3H/(2B)).
$$
Choose $C$ sufficiently large to pay the fixed polynomial losses and contour reciprocal. Then choose $K$ sufficiently large compared with $C$. The conditions $B\ge K H$ and $B^2\le XH$ imply $H/X\le K^{-2}$, $h\le K^{-1}$, $C H/B$ small and $B h^2=B^3/X^2\le H$. The expansion above yields $B+\pi C H\le b\le2B$, with an absolute implied constant in the Gaussian cost $(b+1)^2/V\ll H$ independent of $C$. Also $\log(1/h)+\log(1+S)\ll H$. These are precisely the decay estimates needed for the weighted cutoff error and the noncentral periodization copies. They make the sampled trial vector's zero evaluation error at most $1/4$ in $\ell^2$. The sign and coefficient argument gives the claimed eigenvalue. The choices of $C',C_0$ can be fixed independently of $a$ in the exterior estimate.

Finally the cutoff transform still has the $m$ box factors. With width $w=H/B$ the ratio $m/(w|t-t_k|)$ is $O(B/|t-t_k|)$, the only dependence on bandwidth needed in the exterior proof. Its derivative bounds $O_j(w^{-j})$ are at most fixed powers of $X$. Repeating that proof with $D$ chosen for the desired $a$ gives the stated lower bound from the enlarged local zero census.

**Remaining burden.** Even for fixed $d$, uniform lower eigenvalue bounds for the actual prime matrices across all centers $X$ are unknown. Small matrix dimension does not bound the work of evaluating the prime-power sum or certify the sign.
