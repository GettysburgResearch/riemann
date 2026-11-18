# Boundary energy slope for finite positive Cauchy measures

Let \(\mu\) be a finite positive compactly supported Borel measure on \(\mathbb R\), \(x>0\), and
$$
 G_\mu(w)=\int_{\mathbb R}\frac{d\mu(\gamma)}{w-i\gamma},\qquad
 A_\varepsilon^\mu(w)=\int_0^\varepsilon G_\mu(w+r)\,dr,\qquad
 H_\varepsilon^\mu(w)=e^{-A_\varepsilon^\mu(w)}
$$
on \(\Re w>0\). Write \(P_x(t)=x/(\pi(x^2+t^2))\) and \(\alpha_\gamma=\mu\{\gamma\}\). The atomic slope is
$$
 \lim_{\varepsilon\downarrow0}\frac1\varepsilon
       \int_{\mathbb R}|1-H_\varepsilon^\mu(it)|^2 P_x(t)\,dt
 =
 \sum_{\alpha_\gamma>0}\frac{2x\alpha_\gamma}{x^2+\gamma^2}
       \left[1-\frac{\Gamma(\alpha_\gamma+1/2)}
       {\sqrt\pi\,\Gamma(\alpha_\gamma+1)}\right].
$$
All boundary quantities in this statement are specified almost everywhere. The proof handles singular continuous measures and dense or accumulating atoms. It uses only finiteness, so compact support can also be dropped for this Cauchy-transform formulation.

## Boundary values and the linear estimate

For \(\Re w>0\), \(\Re G_\mu(w)\ge0\), so \(\Re A_\varepsilon^\mu(w)\ge0\) and \(|H_\varepsilon^\mu(w)|\le1\). Additivity of the increment integral gives \(H_{\varepsilon+\delta}^\mu(w)=H_\varepsilon^\mu(w)H_\delta^\mu(w+\varepsilon)\). For almost every \(t\),
$$
 \int_{\mathbb R}\int_0^\varepsilon
     \frac{dr\,d\mu(\gamma)}{\sqrt{r^2+(t-\gamma)^2}}<\infty.
$$
Indeed, the inner integral is \(\operatorname{arsinh}(\varepsilon/|t-\gamma|)\), locally integrable in \(t-\gamma\), and bounded outside \([-1,1]\). Its integral over any fixed bounded \(t\)-interval is bounded independently of \(\gamma\). Fubini thus establishes almost everywhere finiteness, and dominated convergence in the double integral gives the horizontal boundary limits of \(A_\varepsilon^\mu\) and \(H_\varepsilon^\mu\). This uses the same majorant for \(\Re w>0\) because increasing the nonnegative real part increases the denominator modulus. The resulting boundary \(A_\varepsilon^\mu\) has nonnegative real part.

Take the angular-frequency convention \(\widehat\mu(\xi)=\int e^{i\xi\gamma}\,d\mu(\gamma)\). For \(s>0\), the Laplace identity and Fubini give
$$
 A_\varepsilon^\mu(s+it)=\int_0^\infty e^{-it\xi}e^{-s\xi}
            \frac{1-e^{-\varepsilon\xi}}{\xi}\widehat\mu(\xi)\,d\xi.
$$
The multiplier without \(e^{-s\xi}\) is in \(L^2(d\xi)\), since \(|\widehat\mu|\le\mu(\mathbb R)\) and \((1-e^{-\varepsilon\xi})/\xi\le\min(\varepsilon,\xi^{-1})\). Therefore Plancherel and \(s\downarrow0\) give an \(L^2(dt)\) boundary limit agreeing almost everywhere with the preceding pointwise limit. In particular, writing \(g(u)=((1-e^{-u})/u)^2\) for \(u>0\),
$$
 \frac{\|A_\varepsilon^\mu(i\,\cdot)\|_{L^2(dt)}^2}{\varepsilon}
 =2\pi\int_0^\infty g(u)|\widehat\mu(u/\varepsilon)|^2\,du.
$$
Here
$$
 \int_0^\infty g(u)\,du
    =\int_0^1\int_0^1\frac{da\,db}{a+b}=2\log2.
$$
This follows by squaring \((1-e^{-u})/u=\int_0^1e^{-au}da\) and using Tonelli.

Expanding \(|\widehat\mu|^2\) as an integral over \(\mu\otimes\mu\), the \(u\)-integral associated with \((\gamma,\gamma')\) is the Fourier transform of \(g\,1_{(0,\infty)}\) at \((\gamma-\gamma')/\varepsilon\). It tends to zero away from the diagonal by the Riemann–Lebesgue lemma, equals \(2\log2\) on the diagonal, and is bounded by \(2\log2\) everywhere. Dominated convergence and \((\mu\otimes\mu)\{\gamma=\gamma'\}=\sum_\gamma\alpha_\gamma^2\) prove the weighted Wiener identity
$$
 \lim_{\varepsilon\downarrow0}\frac{\|A_\varepsilon^\mu\|_2^2}{\varepsilon}
     =4\pi\log2\sum_\gamma\alpha_\gamma^2. \tag{1}
$$
In particular, this uses no pointwise decay of \(\widehat\mu\), which need not hold for singular continuous measures.

For \(a,b\) in the closed right half-plane, integrating the derivative of the exponential on the line segment gives \(|e^{-a}-e^{-b}|\le|a-b|\). Let \(\nu\) be any positive submeasure of \(\mu\) and use the norm \(\|\cdot\|_x\) in \(L^2(P_x(t)\,dt)\). With \(D_\varepsilon^\mu=1-H_\varepsilon^\mu\), it follows that
$$
 \big|\|D_\varepsilon^\mu\|_x-\|D_\varepsilon^\nu\|_x\big|
 \le \|D_\varepsilon^\mu-D_\varepsilon^\nu\|_x
 \le \|P_x\|_\infty^{1/2}\|A_\varepsilon^{\mu-\nu}\|_2. \tag{2}
$$
Thus the scaled norm difference tends to zero for a nonatomic difference. Omitting the small atoms gives a scaled norm error bounded in the limit by a constant times the square root of the sum of their squared masses. Positivity keeps the exponential contractive even when a pointwise linear approximation is invalid near an atom.

## The nonlinear profile at one atom

At mass \(\alpha>0\) and scaled coordinate \(v=(t-\gamma)/\varepsilon\), the boundary profile is
$$
 h_\alpha(iv)=\exp\!\big(\alpha(\operatorname{Log}(iv)-\operatorname{Log}(1+iv))\big),
 \qquad h_\alpha(w)=\exp\!\big(\alpha(\operatorname{Log} w-\operatorname{Log}(1+w))\big).
$$
Both logarithms take the analytic right-half-plane branches real on the positive real axis, followed by boundary limits. At \(v=0\) the profile is continuously zero. To evaluate \(I_\alpha=\int_{\mathbb R}|1-h_\alpha(iv)|^2dv\), consider the bounded harmonic function \(U(w)=\Re(1-h_\alpha(w))\ge0\). Bounded harmonic Poisson representation and monotone convergence give
$$
 \int_{\mathbb R}U(iv)\,dv
  =\lim_{R\to\infty}\pi R U(R)=\pi\alpha,
$$
since \(\pi R P_R(v)=R^2/(R^2+v^2)\) increases to one and \(R[1-(R/(1+R))^\alpha]\to\alpha\). The modulus loss is integrated by parts, with the endpoint terms \(v[1-(v^2/(1+v^2))^\alpha]\) vanishing at zero and infinity. Thus
$$
 \int_{\mathbb R}(1-|h_\alpha(iv)|^2)\,dv
 =4\alpha\int_0^\infty\frac{v^{2\alpha}}{(1+v^2)^{\alpha+1}}\,dv
 =2\alpha B(\alpha+1/2,1/2).
$$
The identity \(|1-h|^2=2\Re(1-h)-(1-|h|^2)\) now gives
$$
 I_\alpha=2\pi\alpha
       \left[1-\frac{\Gamma(\alpha+1/2)}{\sqrt\pi\,\Gamma(\alpha+1)}\right].
$$
It is finite and strictly positive. By (1) or the exponential inequality applied at this atom, \(I_\alpha\le4\pi\log2\,\alpha^2\). The gamma ratio has derivative \(-2\log2\) at \(\alpha=0\), from the digamma duplication identity. Consequently \(I_\alpha=4\pi\log2\,\alpha^2+O(\alpha^3)\). Equivalently, the bracket in the stated slope is \(2\log2\,\alpha+O(\alpha^2)\).

## Localization and passage to all atoms

For a finite atomic \(\nu\), enclose each atom in a disjoint open interval of fixed radius small enough that its distance from every other atom is positive. On each interval all other atoms' contributions to \(A_\varepsilon^\nu\) are uniformly \(O(\varepsilon)\), by the phase-distance bound on the reciprocal denominator. Thus the difference between \(D_\varepsilon^\nu\) and the single-atom \(1-h_\alpha(i(t-\gamma)/\varepsilon)\) there has \(\|\cdot\|_x\)-norm \(O(\varepsilon)\). Outside these finitely many intervals the entire \(D_\varepsilon^\nu\) has norm \(O(\varepsilon)\) by the same distance bound and \(\int P_x=1\). On an individual interval the substitution \(t=\gamma+\varepsilon v\) and dominated convergence yield the single contribution \(P_x(\gamma)I_\alpha\). The disjoint interval norms add in squares, proving the slope for finite atomic measures.

Let \(\nu_N\) consist of its first \(N\) atoms in any enumeration of the atoms of \(\mu\). Equations (1)–(2) give
$$
 \limsup_{\varepsilon\downarrow0}
 \frac{|\|D_\varepsilon^\mu\|_x-\|D_\varepsilon^{\nu_N}\|_x|}{\sqrt\varepsilon}
 \le
 \left(4\pi\log2\,\|P_x\|_\infty\sum_{\gamma\notin\nu_N}\alpha_\gamma^2\right)^{1/2}.
$$
The right side tends to zero because \(\sum_\gamma\alpha_\gamma\le\mu(\mathbb R)<\infty\). The finite slopes converge to the asserted series by \(I_\alpha\le4\pi\log2\,\alpha^2\). Taking the limit of the scaled norms and then squaring proves the result. The order of limits uses separation only within a finite list, so there is no uniform spacing hypothesis on the atoms. A Cantor probability measure has slope zero by (1)–(2) with \(\nu=0\), while a densely supported atomic measure still has only the listed single-atom contributions.

## Antecedent and scope

Eike Schulte's *On Wiener’s lemma for locally compact abelian groups*, arXiv:2005.05212v1, §3 Definition 3.1 and Theorem 3.9(1), (4), provides the exact abstract antecedent for (1). Normalize \(g(u)\,du\) by \(2\log2\), then push it forward under \(u\mapsto u/\varepsilon\). Along any sequence \(\varepsilon\downarrow0\), these probability measures are ergodic in Schulte's sense because their nontrivial character averages vanish by Riemann–Lebesgue. The direct proof above is the corresponding Fubini argument. This comparison is to the weighted linear atom-detection step. The search located no checked exact antecedent for the nonlinear gamma profile and cocycle slope together, and does not establish novelty. No linear term at infinity or infinite-mass Herglotz representation is used. [Schulte, primary PDF](../../sources/witness62_herglotz/2005.05212.pdf)
