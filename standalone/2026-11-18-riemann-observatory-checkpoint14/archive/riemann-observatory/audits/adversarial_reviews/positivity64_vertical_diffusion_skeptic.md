# Independent derivation of vertical-shift Gaussian limits

18 November 2026. The drift, local exponent limit and weak continuity in the reviewed note agree with an independent derivation from the shifted Hadamard product. The probability interpretation uses GRH for the underlying entire Selberg-class function. A separate sign issue in the compensated representation printed in Suzuki v2 §5.1 is recorded below. Publication priority is unassessed. [Reviewed vertical-shift note](uniform64_vertical_shift_diffusion.md) · [Suzuki arXiv:2209.12832v2](https://arxiv.org/pdf/2209.12832v2)

## Which translation stays in the class

For a pole-free Selberg-class function $F$, the translation $F_\tau(s)=F(s+i\tau)$, $\tau\in\mathbb R$, twists the ordinary Dirichlet coefficients and logarithmic Euler-product coefficients by $n^{-i\tau}$. Their bounds and support are preserved and the entire continuation stays entire of finite order. Fix the initial completion data $Q,\lambda_j$ and replace $\mu_j$ by $\mu_j+i\lambda_j\tau$. Then
$$
\Lambda_\tau(s)=Q^{-i\tau}\Lambda_0(s+i\tau),\qquad \omega_\tau=\omega_0Q^{-2i\tau}.
$$
Indeed conjugation of the constant in the completed function contributes the second factor $Q^{-i\tau}$ to the root number. Gamma shifts retain their allowed real parts and the degree $2\sum_j\lambda_j$ is unchanged. Under $s=1/2-iz$, the completed function is $E_\tau(z)=Q^{-i\tau}E_0(z-\tau)$. Thus the zero $\gamma$ moves to $\gamma+\tau$, with its original multiplicity. A critical-line zero at height $t_0>0$ has $\gamma=-t_0$ and becomes central at $\tau=t_0$. The functional equation gives $E_\tau(z)=\omega_\tau\overline{E_\tau(\bar z)}$, so a constant phase makes $E_\tau$ real entire. All logarithmic derivatives are independent of that phase. Ordinary nonzero vertical shifts of $\zeta$ fail the pole condition, because the pole moves to $1-i\tau$ and a power of $s-1$ cannot remove it.

## Drift from the logarithmic derivative

Assume $E_0(0)\ne0$. This is a choice of reference shift, since real shifts hitting a zero form a discrete set. Let $D_\tau$ be the regular part of $E'_\tau/E_\tau$ at zero, removing $m_0(\tau)/z$ when necessary. In Suzuki v2, $D_\tau$ is the Hadamard coefficient $B_\tau^{\rm H}$ of (2.5)–(2.6). The uncompensated $e^{itx}$ drift is $u_\tau=-D_\tau$ by (1.1). Independently, the one-sided transform sends $iu_\tau t$ to $-iu_\tau/z^2$, whereas the constant part of $z^{-2}(\Lambda_\tau'/\Lambda_\tau)(1/2-iz)$ is $iD_\tau/z^2$. This confirms the minus sign.

For a noncentral shift, substituting $-\tau$ in the initial Hadamard logarithmic derivative gives
$$
D_\tau=D_0+\sum_\gamma m_\gamma
       \left(\frac1\gamma-\frac1{\gamma+\tau}\right),\qquad
u_\tau=u_0+\sum_\gamma m_\gamma
       \left(\frac1{\gamma+\tau}-\frac1\gamma\right).
$$
These are sums of paired differences. At a crossing at $\tau_*=-\gamma_*$, put $m=m_{\gamma_*}$ and $\delta=\gamma_*+\tau$. In a neighborhood of $\tau_*$ the other zeros stay uniformly away from the origin. For $\delta\ne0$, write
$$
u_\tau=\frac{m}{\delta}+u_{\rm reg}(\tau),\qquad
u_{\rm reg}(\tau)=u_0-\frac m{\gamma_*}
   +\sum_{\gamma\ne\gamma_*}m_\gamma
      \left(\frac1{\gamma+\tau}-\frac1\gamma\right).
$$
On evaluating the Hadamard derivative at $z-\tau_*$, the distinguished term is $m/z+m/\gamma_*$. Subtracting $m/z$ gives $u_{\tau_*}=u_{\rm reg}(\tau_*)$. A simultaneous crossing of multiple copies of the same zero uses the total multiplicity $m$. Distinct zeros cannot cross zero at the same real shift. A zero with the same real coordinate and nonzero imaginary part remains away from zero. If the initial completion is central, choose a neighboring noncentral reference first and apply the same calculation.

## Local convergence of the full exponent

At $\delta\ne0$ the pair of distinguished terms is
$$
i\frac{m}{\delta}t+\frac{m}{\delta^2}(e^{-i\delta t}-1)
=\frac{m}{\delta^2}(e^{-i\delta t}-1+i\delta t).
$$
It extends at $\delta=0$ as $-mt^2/2$, with error at most $m|\delta||t|^3 e^{|\delta t|}/6$. Fix bounded $|\tau|\le M$ and $|t|\le T$. The remaining terms combine into
$$
m_\gamma\left[
 \frac{e^{-i(\gamma+\tau)t}-1}{(\gamma+\tau)^2}
 +it\left(\frac1{\gamma+\tau}-\frac1\gamma\right)\right].
$$
For $|\gamma|>2M+1$ the absolute value is bounded by $C_{M,T}m_\gamma/|\gamma|^2$, using $|\operatorname{Im}\gamma|\le1/2$. The translation derivatives obey the same majorant, by direct differentiation. The order-one product provides $\sum m_\gamma/|\gamma|^2<\infty$. The finitely many other nonresonant terms are smooth in the crossing neighborhood. This proves local uniform convergence and an $O_T(|\tau-\tau_*|)$ error there, without assuming GRH. There is no finite-interval assumption on zeros that was used to replace the analytic tail estimate.

Under GRH all zero coordinates are real. For $\delta\ne0$, take $K_\delta\sim{\rm Poisson}(m/\delta^2)$ independently of the other jump terms. The distinguished factor is the characteristic function of $-\delta(K_\delta-m/\delta^2)$. This factor has mean zero and variance $m$, and Lévy continuity gives its centered Gaussian limit. The ordinary compound Poisson rates of the remaining jumps are locally bounded, and the drift $u_{\rm reg}$ and their characteristic exponents converge. Thus the full family of laws is weakly continuous, with a Gaussian factor of variance $m$ at the crossing. The two signs of $\delta$ give the same limit. A global uniform exponent estimate would fail in general. At a fixed noncentral shift the real part of the exponent is bounded by twice the finite rate, whereas at the central shift it has an unbounded negative quadratic part. This does not affect local uniform convergence.

## The compensated drift and a printed sign

Use the truncation $h(x)=x/(1+x^2)$, so that the canonical compensated drift $c_\tau$ satisfies $u_\tau=c_\tau-\int h\,d\nu_\tau$. In the GRH measure each noncentral zero of coordinate $\eta=\gamma+\tau$ carries mass $m_\gamma/\eta^2$ at $x=-\eta$. Therefore
$$
c_\tau=-D_\tau-\sum_{\gamma+\tau\ne0}
              \frac{m_\gamma}{(\gamma+\tau)(1+(\gamma+\tau)^2)}.
$$
The distinguished atom adds $-m/[\delta(1+\delta^2)]$ to $\int h\,d\nu_\tau$, which cancels the divergent part of $u_\tau$ and leaves $m\delta/(1+\delta^2)\to0$. The jump rate and uncompensated drift diverge, while the compensated drift is continuous. More generally
$$
 c_\tau=c_0+\sum_\gamma m_\gamma
 \left[f(\gamma+\tau)-f(\gamma)\right],\qquad
 f(x)=\frac{x}{1+x^2}.
$$
This remains valid at crossings with $f(0)=0$. The paired summands converge normally on compact real shift intervals by the inverse-square bound. This formula also makes clear that the distinction between compensated and uncompensated drift is independent of the Gaussian factor.

In the rendered v2 PDF p. 6 §5.1, the displayed compensated formula uses $+iC_Ft$, the measure $\sum_\gamma m_\gamma\delta_{-\gamma}$ and $C_F=B_F+\sum_{\gamma\ne0}m_\gamma/[\gamma(1+\gamma^2)]$. With $B_F=D$ and those displayed choices, this coefficient is the negative of the one compatible with (1.1). Direct substitution of one atom verifies the sign. Its role inside the compensation integral is to add $+it\,m_\gamma/[\gamma(1+\gamma^2)]$ to the uncompensated jump term. The drift outside that integral must subtract the same contribution and start at $-B_F$. For the simple real-zero model $E(z)=z-\delta$, $B_F=-1/\delta$ and the required coefficient is $\delta/(1+\delta^2)$, while the p. 6 formula gives $-\delta/(1+\delta^2)$. This finite product checks the algebra without claiming it is Selberg-class data. Within the GRH family containing at least one zero, the exact series for $c_\tau$ has meromorphic continuation in $\tau$ with poles at $\tau=-\gamma\pm i$. The residue at each such pole is $m_\gamma/2$, since real $\gamma$ prevent any cross-sign collision. The paired form converges normally on compact sets avoiding the poles. Hence the canonical compensated drift is not identically zero across real shifts, so the opposite sign cannot hold uniformly along that family. This concerns the printed §5.1 coefficient, not the primary zero-side exponent (1.1) used in the reviewed note. This source-sign question remains unadjudicated pending a current journal-version and erratum check. [Rendered formula, Suzuki §5.1 p. 6](https://arxiv.org/pdf/2209.12832v2#page=6)

## A finite measure combining the Gaussian and jump coordinates

Under GRH and with the truncation $h(x)=x/(1+x^2)$, write $a_\tau=m_0(\tau)$ and let $\nu_\tau$ be the noncentral Lévy measure. The finite positive measure
$$
K_\tau(d\lambda)=a_\tau\delta_0(d\lambda)+\frac{\lambda^2}{1+\lambda^2}\nu_\tau(d\lambda)
=\sum_\gamma\frac{m_\gamma}{1+(\gamma+\tau)^2}\delta_{-\gamma-\tau}(d\lambda)
$$
includes the entire centered atom with weight $m_\gamma$ when $\gamma+\tau=0$. For any bounded continuous test function, each term of its integral against $K_\tau$ is continuous in $\tau$. The tails are uniformly dominated on compact $\tau$-intervals by a constant times $\sum m_\gamma/|\gamma|^2$. Thus $K_\tau$ is weakly continuous as a finite positive measure.

With the compensated drift $c_\tau$ derived from (1.1), its exponent is $i c_\tau t+\int k_t(\lambda)K_\tau(d\lambda)$, where
$$
 k_t(\lambda)=\frac{1+\lambda^2}{\lambda^2}
       \left(e^{it\lambda}-1-\frac{it\lambda}{1+\lambda^2}\right),
 \qquad k_t(0)=-t^2/2.
$$
For each fixed real $t$, this extension is continuous and bounded on the real line. Taylor expansion applies at zero, and the prefactor and integrand are bounded on the complement of any neighborhood of zero. The combination of weak continuity for $K_\tau$ and ordinary continuity of $c_\tau$ therefore gives another direct proof of weak continuity for the GRH probability laws, including every central crossing. This combines the Gaussian and jump parts of the same conditional construction. [Zero-side primary convention](https://arxiv.org/pdf/2209.12832v2)

## Degree-one check and comparison

For the entire primitive nonprincipal character $\chi_4$, the alternating odd-integer series gives $L(1/2,\chi_4)>0$. I independently recomputed the critical-line endpoint signs using the Hurwitz zeta difference and the degree-one completion at 180-bit Arb precision. At $6.02094890469$ and $6.02094890471$ the real completed values are enclosed respectively by balls centered at $3.4754220235137865933179335594030496977251\cdot10^{-13}$ and $-5.6744526728814886051532723468485211039951\cdot10^{-13}$, with radii below $4\cdot10^{-54}$. Since the completion is real along the critical line, these give a genuine nonzero critical ordinate with some multiplicity $m>0$. Moving it to the center preserves degree one and the Selberg axioms. The presence of the central quadratic term is unconditional in the zero-side formula. The entire law and its Gaussian variance interpretation remain conditional on GRH for $\chi_4$. No simplicity assumption is needed. [Existing endpoint certificate](director_finite_lower_round8.md)

Comparison with the mature note gives the same gamma shifts, ordinate sign, finite residual drift, tail controls and crossing law. Its local qualification is essential and its use of the convention in (1.1) is consistent. The compensated-drift formula above provides an additional check and a distinction from the separate printed representation in §5.1. No canonical files were edited.
