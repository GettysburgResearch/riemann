# Vertical shifts and the central-zero Gaussian factor

18 November 2026. An entire positive-degree Selberg-class function admits vertical shifts within the class without changing degree. In the zero-side screw exponent, a real zero crossing the center contributes a diverging compound Poisson rate and an opposite compensating drift. The combined exponent has a continuous limit, and under GRH the limiting law has a Gaussian factor with variance equal to the central multiplicity. The sign of the drift below is fixed against the primary Hadamard convention. Publication priority is unassessed.

## Selberg axioms and translation of the completed zeros

Let \(F\in\mathcal S\) be entire, so the pole-removal exponent \(m_F\) in (S2) is zero. Let
\[
 \Lambda_F(s)=Q^s\prod_j\Gamma(\lambda_js+\mu_j)F(s),
 \qquad
 \Lambda_F(s)=\omega\,\overline{\Lambda_F(1-\bar s)} .
\]
For real \(\tau\), set \(F_\tau(s)=F(s+i\tau)\). Its Dirichlet coefficients are \(a_F(n)n^{-i\tau}\), and its logarithmic Euler-product coefficients are \(b_F(n)n^{-i\tau}\). Thus (S1), (S4) and (S5) retain their convergence, size and support conditions. Its translation stays entire of finite order, giving (S2). In (S3) retain \(Q,\lambda_j\) and use \(\mu_j+i\lambda_j\tau\). The real parts of the gamma shifts are unchanged and the completed function satisfies
\[
 \Lambda_{F_\tau}(s)=Q^{-i\tau}\Lambda_F(s+i\tau),
 \qquad \omega_\tau=\omega Q^{-2i\tau}.
\]
Both constant factors have modulus one, and the degree \(2\sum_j\lambda_j\) is unchanged. This also shows
\[
 E_\tau(z):=\Lambda_{F_\tau}(1/2-iz)=Q^{-i\tau}E_0(z-\tau).
\]
Thus the zero \(\gamma\) in this coordinate moves to \(\gamma+\tau\), with its multiplicity. GRH of this family, when assumed, is preserved. A global unimodular phase does not alter any logarithmic derivative. One can choose the functional-equation phases continuously to normalize \(E_\tau\) to a real entire function, since the involution in the \(z\)-variable is complex conjugation. An ordinary translate \(\zeta(s+i\tau)\) with \(\tau\ne0\) fails (S2), since its pole is at \(1-i\tau\) and cannot be removed by a power of \(s-1\). The valid degree-one examples come from primitive nonprincipal Dirichlet \(L\)-functions, which are entire. [Selberg axioms in Suzuki, §2.1](../../sources/suzuki_model63_positivity/suzuki_selberg.pdf) · [Suzuki, arXiv:2209.12832v2, (2.1)–(2.3)](https://arxiv.org/pdf/2209.12832v2)

## Drift convention and the translation formula

Assume initially \(E_0(0)\ne0\). Write the zeros of \(E_0\) as distinct \(\gamma\) with multiplicities \(m_\gamma\). They satisfy \(\sum m_\gamma/|\gamma|^2<\infty\) from the order-one completion. In Suzuki's equations (2.5)–(2.6), the Hadamard constant \(B_\tau^{\rm H}\) is the regular part
\[
 B_\tau^{\rm H}=\lim_{z\to0}\left(\frac{E'_\tau(z)}{E_\tau(z)}-\frac{m_0(\tau)}z\right),
\]
where \(m_0(\tau)\) is the central multiplicity. The functional equation gives a real value for this constant. In equation (1.1) Suzuki uses the linear term \(-i B_\tau^{\rm H}t\). Denote the drift in the convention \(e^{itx}\) by \(b_\tau=-B_\tau^{\rm H}\). With this notation the screw exponent is
\[
 g_\tau(t)=i b_\tau t-\frac{m_0(\tau)t^2}{2}
 +\sum_{\gamma+\tau\ne0}m_\gamma
       \frac{e^{-i(\gamma+\tau)t}-1}{(\gamma+\tau)^2}.
\]
The derivative relation \((\Lambda'_{F_\tau}/\Lambda_{F_\tau})(1/2-iz)=iE'_\tau(z)/E_\tau(z)\) independently confirms the drift sign by the one-sided transform \(\int_0^\infty t e^{izt}dt=-1/z^2\). Using \(B_\tau^{\rm H}\) itself with a positive \(i\) in the exponent would give the opposite drift.

From the genus-one logarithmic derivative of \(E_0\), if \(E_\tau(0)\ne0\),
\[
 B_\tau^{\rm H}
 =B_0^{\rm H}+\sum_\gamma m_\gamma\left(\frac1\gamma-\frac1{\gamma+\tau}\right),
 \qquad
 b_\tau
 =b_0+\sum_\gamma m_\gamma\left(\frac1{\gamma+\tau}-\frac1\gamma\right).
\]
These are sums of differences and converge absolutely. They do not assign separate values to the two sums of reciprocals. At a central crossing \(\tau_0=-\gamma_0\) of multiplicity \(m=m_{\gamma_0}\), subtraction of the new residue \(m/z\) in the regular part gives
\[
 b_{\tau_0}
 =b_0-\frac{m}{\gamma_0}
    +\sum_{\gamma\ne\gamma_0}m_\gamma
        \left(\frac1{\gamma+\tau_0}-\frac1\gamma\right).
\]
Indeed the original pair of logarithmic-derivative terms for \(\gamma_0\), evaluated at \(z-\tau_0\), is \(m/z+m/\gamma_0\). With \(\gamma_0\ne0\), this gives the displayed finite drift shift as well as the pole term. [Suzuki, arXiv:2209.12832v2, (1.1), (2.5)–(2.6), (3.2)](https://arxiv.org/pdf/2209.12832v2)

## Regularization and continuity

For real \(t\) define the entire function of \(w\)
\[
 \mathcal R(w,t)=\frac{e^{-iwt}-1+iwt}{w^2},\qquad
 \mathcal R(0,t)=-t^2/2 .
\]
Then the single expression
\[
 g_\tau(t)=i b_0 t+\sum_\gamma m_\gamma
        \left(\mathcal R(\gamma+\tau,t)-\frac{it}{\gamma}\right)
\]
holds both at and away from central crossings. The inner difference must be kept paired when summing. Away from a crossing this follows by adding the drift formula to the jump exponent. At a crossing it gives the calculated regular drift and the central quadratic term.

For \(|\tau|\le M\) and \(|t|\le T\), the summands with \(|\gamma|>2M+1\) are \(O_{M,T}(m_\gamma/|\gamma|^2)\): for the displayed combination use the split into \((e^{-i(\gamma+\tau)t}-1)/(\gamma+\tau)^2\) and \(it(1/(\gamma+\tau)-1/\gamma)\). The modulus of the exponential is bounded by the zero strip and the compact time interval, and the reciprocal difference is at most \(2M/|\gamma|^2\). The finitely many remaining terms are continuous after filling the removable points. This proves locally uniform convergence and continuity in \((\tau,t)\); the analytic statement does not require GRH. For the same large zeros, the translation derivative is \(O_{M,T}(m_\gamma/|\gamma|^2)\) as well, by differentiating the exponential quotient and the reciprocal. In a neighborhood of a crossing, the other finitely many terms stay away from zero denominators. Thus the nonsingular part is locally Lipschitz in \(\tau\) on every compact \(t\)-interval, with a constant depending on the function and neighborhood.

Writing \(\delta=\gamma_0+\tau\), the distinguished summand is
\[
 m\left[\frac{e^{-i\delta t}-1+i\delta t}{\delta^2}-\frac{it}{\gamma_0}\right].
\]
The difference from \(-mt^2/2-imt/\gamma_0\) is at most \(m|\delta||t|^3e^{|\delta t|}/6\) by Taylor's integral remainder. This gives an explicit compact-time error for the crossing summand and, with the nonsingular derivative bound, \(g_\tau-g_{\tau_0}=O_T(|\tau-\tau_0|)\) near the crossing. There is no uniform claim over all \(t\).

## Exact factor of the probability law

Assume GRH for \(F\), so every \(\gamma\) is real. At a noncentral \(\tau\), all jumps \(-(\gamma+\tau)\) have finite total rate \(\sum m_\gamma/(\gamma+\tau)^2\), since the zero set is discrete and the tail is inverse-square summable. The characteristic function \(e^{g_\tau}\) is that of a finite compound Poisson variable plus deterministic shift \(b_\tau\). At a central point the noncentral jumps still have finite total rate and the law adds an independent \(N(0,m_0(\tau))\) factor.

More precisely, near \(\tau_0\) the law for \(\delta\ne0\) is the convolution of its nonsingular compound Poisson part and the law of
\[
 -\delta\bigl(K_\delta-m/\delta^2\bigr),
 \qquad K_\delta\sim{\rm Poisson}(m/\delta^2),
\]
together with the deterministic drift
\[
 b_0-\frac{m}{\gamma_0}+
   \sum_{\gamma\ne\gamma_0}m_\gamma
      \left(\frac1{\gamma+\tau}-\frac1\gamma\right).
\]
The compensating shift \(m/\delta\) was factored into the centered Poisson variable and is excluded from this remaining drift. The centered factor has mean zero, variance \(m\), and the characteristic exponent in brackets after removing \(-imt/\gamma_0\). Its limit from either side is \(N(0,m)\) by the explicit Taylor bound and Lévy continuity. The nonsingular factor and the finite drift also converge by the same uniform sums. Accordingly the full family is weakly continuous at the crossing and, by the same local argument, at every other finite \(\tau\). This argument uses convergence of the characteristic exponents at every fixed \(t\) and continuity at \(t=0\). The individual jump rates and uncompensated drifts do not converge at the crossing. The central variance calculation is the ordinary compensated Poisson diffusion limit, here attached to an exact translation of a completed zero.

## Degree-one witness and scope

For a concrete entire degree-one \(F\), take the primitive real \(\chi_4\), with \(F(s)=L(s,\chi_4)\). Its alternating odd-integer series is positive at \(s=1/2\), so the initial completion is nonzero there. The archive already brackets a critical zero; I replayed the opposite endpoint signs at 192-bit Arb precision using
\[
 F(s)=4^{-s}\big[\zeta(s,1/4)-\zeta(s,3/4)\big],\qquad
 \Lambda_F(s)=(4/\pi)^{(s+1)/2}\Gamma((s+1)/2)F(s).
\]
At \(s=1/2+it\), \(t=6.02094890469\) and \(6.02094890471\), the real completion balls have definite opposite signs, with respective midpoints \(3.4754220235137866\cdot10^{-13}\) and \(-5.6744526728814886\cdot10^{-13}\). Continuity gives a nonzero critical ordinate, and reflection gives both choices of sign in the \(z\)-coordinate. The shift that places either chosen zero at the center remains in the degree-one Selberg class unconditionally. At nearby shifts, the designated real-zero summand alone has rate \(m/\delta^2\) and the explicit compensating drift. Thus degree alone gives neither a uniform bound on those uncompensated data nor exclusion of a central quadratic term. Identification of the full exponent with an infinitely divisible law, and weak continuity *as probability laws*, are conditional on GRH for the underlying Dirichlet \(L\)-function. No simplicity of the chosen root is required. [Existing critical-zero certificate](director_finite_lower_round8.md)

The Suzuki source checked is arXiv:2209.12832v2, SHA-256 c706479044babf3618fff6910ce28238faf1bb321c7ffee9f73f1ee765f34232. The derivation uses the zero-side equation (1.1) and the Hadamard equations. It does not rely on the real-axis zero assumption in Suzuki's converse sign criterion. No canonical records changed.
