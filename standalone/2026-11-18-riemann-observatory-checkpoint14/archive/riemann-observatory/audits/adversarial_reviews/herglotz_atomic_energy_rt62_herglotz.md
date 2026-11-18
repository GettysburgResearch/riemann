# Independent Poisson-deficit proof of the Herglotz energy slope

Reviewer rt_repair_62. This proves the stated general positive Herglotz-measure formula from its representation. The finite-measure argument below was derived independently of the [parallel finite-measure proof](witness62_herglotz_atomic_energy.md). The scope is the analytic boundary-energy identity.

Let \(a\ge0\), \(b\in\mathbb R\), and \(\mu\) be positive with \(\int (1+\gamma^2)^{-1}\mu(d\gamma)<\infty\). For \(\Re w>0\), put
\[
 G(w)=aw+ib+\int\left(\frac1{w-i\gamma}-\frac{i\gamma}{1+\gamma^2}\right)\mu(d\gamma),
 \qquad H_\varepsilon(w)=\exp\left(-\int_0^\varepsilon G(w+r)\,dr\right).
\]
The compensated integrand is \((1-i\gamma w)/[(w-i\gamma)(1+\gamma^2)]\), bounded on each compact subset of the right half-plane by a constant times \((1+\gamma^2)^{-1}\). This gives absolute locally uniform convergence and holomorphy, without splitting possibly divergent imaginary integrals. Its real part is \(\Re w/|w-i\gamma|^2\), so \(\Re G\ge0\) and \(H_\varepsilon\) is Schur. It is a translation cocycle, \(H_{\varepsilon+\delta}(w)=H_\varepsilon(w)H_\delta(w+\varepsilon)\).

Fix \(x>0\), and write \(dP_x(t)=x\,dt/(\pi(x^2+t^2))\). By the bounded analytic Fatou theorem and bounded harmonic Poisson representation (equivalently, apply them via the disk), \(H_\varepsilon(it)\) is defined for almost every \(t\), and its \(P_x\)-integral is \(H_\varepsilon(x)\). Thus the exact identity is
\[
 E_\varepsilon:=\int|1-H_\varepsilon(it)|^2\,dP_x
 =2\Re(1-H_\varepsilon(x))-\int(1-|H_\varepsilon(it)|^2)\,dP_x. \tag{1}
\]
In particular \(E_\varepsilon\le 2\Re(1-H_\varepsilon(x))\). Local analyticity gives \(2\Re(1-H_\varepsilon(x))/\varepsilon\to2\Re G(x)\). These facts hold for the compensated general measure and every positive submeasure. Each boundary identity uses almost-everywhere representatives at the given \(\varepsilon\); a common exceptional set for uncountably many \(\varepsilon\) is unnecessary.

## Finite measures and atomic nonlinear energy

Suppose first \(\mu\) is finite, with no support restriction and with \(a,b\) retained. Twice the real part of the increment at \(s+it\), \(s>0\), is
\[
 2a(\varepsilon s+\varepsilon^2/2)+
 \int \log\frac{(s+\varepsilon)^2+(t-\gamma)^2}{s^2+(t-\gamma)^2}\,\mu(d\gamma).
\]
Here the boundary linear-factor modulus squared is \(e^{-a\varepsilon^2}\), a correction of order \(\varepsilon^2\), irrespective of its oscillatory phase. The nonnegative kernel in the integral has \(L^1(dt)\)-mass \(2\pi\varepsilon\) for any \(s\ge0\), by integrating \(2r/(r^2+t^2)\) in \(r\) and then in \(t\). As \(s\downarrow0\) it converges pointwise away from zero to \(K_\varepsilon(t)=\log(1+\varepsilon^2/t^2)\). Equality of masses and nonnegativity give \(L^1\) convergence. Convolving with finite \(\mu\) preserves this \(L^1\) convergence. A subsequence converges almost everywhere, where the actual bounded analytic boundary values already exist. Hence
\[
 |H_\varepsilon(it)|^2=e^{-a\varepsilon^2}\exp(-u_\varepsilon(t)),
 \qquad u_\varepsilon=K_\varepsilon*\mu,
\]
almost everywhere. The factor \(e^{-a\varepsilon^2}\) changes the integrated modulus deficit by at most \(a\varepsilon^2\). Both the compensation and \(ib\) are pure phase contributions and never enter the modulus. This computation controls all interaction with \(aw\) in (1), without a separate cross-term limit.

Set \(F(u)=u-1+e^{-u}\) for \(u\ge0\). Then \(0\le F(u)\le u^2/2\), \(F\) is 1-Lipschitz, and
\[
 0\le F(u+v)-F(u)-F(v)
    =(1-e^{-u})(1-e^{-v})\le uv.
\]
The rescaled kernels satisfy \(K_\varepsilon(t)=K_1(t/\varepsilon)\), with \(K_1\in L^1\cap L^2\). By scaling and dominated convergence,
\(\varepsilon^{-1}\int u_\varepsilon\,dP_x\to2\pi\int P_x(\gamma)\mu(d\gamma)\).
This cancels exactly the measure part of \(2\Re G(x)\) in (1), so it remains to evaluate \(\varepsilon^{-1}\int F(u_\varepsilon)\,dP_x\).

For finite positive \(\nu\),
\[
 \frac1\varepsilon\|K_\varepsilon*\nu\|_2^2
 =\iint C((\gamma-\gamma')/\varepsilon)\nu(d\gamma)\nu(d\gamma'),
 \quad
 C(y)=\int K_1(v)K_1(v+y)\,dv .
\]
The autocorrelation is bounded by \(\|K_1\|_2^2\) and tends to zero as \(|y|\to\infty\), by approximating \(K_1\) in \(L^2\) by bounded compactly supported functions. Dominated convergence proves that a nonatomic \(\nu\) contributes \(o(\varepsilon)\) to this squared norm, including singular continuous measures. Its contribution to \(F\) is also \(o(\varepsilon)\): use \(F(v)\le v^2/2\) and the cross bound \(\int uv\le\|u\|_2\|v\|_2\), with the finite remaining measure giving \(\|u\|_2=O(\sqrt\varepsilon)\). A finite list of distinct atoms has cross-products \(o(\varepsilon)\) by the same autocorrelation at nonzero displacements. Countably many atoms are handled by finite lists first, because the 1-Lipschitz property gives a normalized weighted error at most \(2\pi\|P_x\|_\infty\) times the omitted mass.

For a single atom of mass \(\alpha>0\) at \(\gamma\), substitute \(t=\gamma+\varepsilon v\) and dominate \(F(\alpha K_1)\) by \(\alpha K_1\). The resulting contribution is \(P_x(\gamma)\int F(\alpha K_1(v))\,dv\). Integrating by parts on the positive half-line and substituting \(v^2\) shows
\[
 \int_{\mathbb R}\left[1-\left(\frac{v^2}{1+v^2}\right)^\alpha\right]\,dv
 =4\alpha\int_0^\infty \frac{v^{2\alpha}}{(1+v^2)^{\alpha+1}}\,dv
 =2\alpha B(\alpha+1/2,1/2).
\]
The integrated boundary terms vanish at zero and infinity. Subtract this from \(\int\alpha K_1=2\pi\alpha\). Combining with (1) yields the finite-measure slope
\[
 2ax+\sum_{\gamma}\frac{2x\alpha_\gamma}{x^2+\gamma^2}
 \left[1-\frac{\Gamma(\alpha_\gamma+1/2)}{\sqrt\pi\,\Gamma(\alpha_\gamma+1)}\right],
 \qquad \alpha_\gamma=\mu\{\gamma\}>0. \tag{2}
\]
In particular the linear term alone has slope \(2ax\), the imaginary constant alone has slope zero, and a unit atom alone has slope \(x/(x^2+\gamma^2)\). The formula for \(aw\) follows from the interior term of (1). Its boundary attenuation is \(o(\varepsilon)\), so energy from the oscillatory phase is already included.

## Infinite mass and order of limits

Keep \(aw+ib\) in the core and restrict its measure to \(|\gamma|\le R\). The compensated tail transform has nonnegative real part, so \(H_\varepsilon=H_{\varepsilon,R}H_{\varepsilon,\mathrm{tail}}\) and both factors are Schur. This equality holds for their almost-everywhere boundary values. Write \(\|\cdot\|_x=\|\cdot\|_{L^2(dP_x)}\). Then
\[
 \left|\frac{\|1-H_\varepsilon\|_x}{\sqrt\varepsilon}
        -\frac{\|1-H_{\varepsilon,R}\|_x}{\sqrt\varepsilon}\right|
 \le\frac{\|1-H_{\varepsilon,\mathrm{tail}}\|_x}{\sqrt\varepsilon},
 \qquad
 \limsup_{\varepsilon\downarrow0}
 \frac{\|1-H_{\varepsilon,\mathrm{tail}}\|_x}{\sqrt\varepsilon}
 \le\sqrt{2\Re G_{\mathrm{tail}}(x)}
\]
by (1). The last real part is \(\int_{|\gamma|>R}x/(x^2+\gamma^2)\,\mu(d\gamma)\to0\) by the weighted integrability assumption. Each term in (2) lies between zero and \(2x\alpha_\gamma/(x^2+\gamma^2)\) because \(0\le F(u)\le u\). The atomic series therefore converges, and finite-core slopes tend to (2). At fixed \(R\) take \(\varepsilon\downarrow0\), then \(R\to\infty\) in the norm inequalities, then square the common limit. This controls the infinite tail without requiring a pointwise boundary formula for its uncompensated Cauchy transform.

## Linear Wiener cross-check

For finite \(\mu\), the uncompensated boundary increment is \(L_\varepsilon*\mu\), where \(L_\varepsilon(t)=\int_0^\varepsilon(r+it)^{-1}dr\) almost everywhere. Its Fourier multiplier on one half-axis is \(2\pi(1-e^{-\varepsilon|\xi|})/|\xi|\) with the convention \(\widehat f(\xi)=\int e^{-it\xi}f(t)dt\). Plancherel gives \(\|L_\varepsilon\|_2^2=4\pi\varepsilon\log2\), since \(\int_0^\infty[(1-e^{-u})/u]^2du=\int_{[0,1]^2}(a+b)^{-1}da\,db=2\log2\). The same autocorrelation argument works for \(|L_1|\in L^2\), since \(L_\varepsilon(t)=L_1(t/\varepsilon)\). Thus a continuous part is negligible, distinct atomic cross terms vanish, and each finite atom contributes \(4\pi\log2\,\alpha_\gamma^2 P_x(\gamma)\) to the normalized Poisson-weighted squared norm. The omitted masses are controlled in normalized norm by \(\|P_x\|_\infty^{1/2}\|L_1\|_2\) times their sum. This confirms the corresponding weighted linear constant and agrees with the finite-measure nonlinear profile by expanding the gamma ratio at small \(\alpha\).

The result concerns the stated positive Herglotz representation. No novelty claim or inference about zeros of the Riemann zeta-function is made.
