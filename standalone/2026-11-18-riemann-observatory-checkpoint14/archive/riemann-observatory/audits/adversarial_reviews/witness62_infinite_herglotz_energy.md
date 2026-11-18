# General positive-real generator and Poisson-weighted energy

Independent advocacy draft. The finite-measure result extends to positive Herglotz measures of possibly infinite mass. This is an application of the finite atomic calculation, standard Hardy boundary theory, and a Poisson estimate for the truncated tail. The result remains pending review. [Finite-measure proof](witness62_herglotz_atomic_energy.md)

Let \(a\ge0\), \(b\in\mathbb R\), and \(\mu\) be a positive Borel measure on \(\mathbb R\) with
\[
 \int_{\mathbb R}\frac{d\mu(\gamma)}{1+\gamma^2}<\infty.
\]
For \(\Re w>0\), set
\[
 G(w)=a w+i b+\int_{\mathbb R}
   \left(\frac{1}{w-i\gamma}-\frac{i\gamma}{1+\gamma^2}\right)d\mu(\gamma),
 \qquad
 H_\varepsilon(w)=\exp\left(-\int_0^\varepsilon G(w+r)\,dr\right)
 \quad (\varepsilon>0).
\]
For each fixed \(x>0\), let \(P_x(t)=x/(\pi(x^2+t^2))\). With \(\alpha_\gamma=\mu\{\gamma\}\), the proposed identity is
\[
 \lim_{\varepsilon\downarrow0}
   \frac{\int_{\mathbb R}|1-H_\varepsilon(it)|^2 P_x(t)\,dt}{\varepsilon}
 =2ax+\sum_{\alpha_\gamma>0}
      \frac{2x\alpha_\gamma}{x^2+\gamma^2}
      \left(1-\frac{\Gamma(\alpha_\gamma+1/2)}
                        {\sqrt\pi\,\Gamma(\alpha_\gamma+1)}\right). \tag{1}
\]
Boundary values in (1) are the nontangential limits almost everywhere. The atomic series converges even if the masses are unbounded as \(|\gamma|\to\infty\).

## Compensated generator and boundary normalization

The combined kernel equals
\[
 \frac{1-i\gamma w}{(w-i\gamma)(1+\gamma^2)}.
\]
On a compact subset of \(\Re w>0\), it is bounded by \(C/(1+\gamma^2)\) uniformly in \(w\) and \(\gamma\). For \(|\gamma|\) large this follows from \(|w-i\gamma|\ge|\gamma|/2\), and for \(\gamma\) bounded one uses the positive lower bound on \(\Re w\). Thus the combined integral is absolutely and locally uniformly convergent and defines a holomorphic function. The compensator is pure imaginary, so for \(\Re w>0\)
\[
 \Re G(w)=a\Re w+\int_{\mathbb R}
        \frac{\Re w}{(\Re w)^2+(\Im w-\gamma)^2}\,d\mu(\gamma)\ \ge0.
\]
In particular no separately integrated compensation is required on the full measure or its tails. At \(w=1\) the integrand is purely real, so \(b=\Im G(1)\). Also \(a=\lim_{x\to\infty}G(x)/x\). To see the latter, divide the combined kernel by \(x\). For \(x\ge1\) its modulus is at most \(2/(1+\gamma^2)\), since \((1+x|\gamma|)/(x\sqrt{x^2+\gamma^2})\le2\). Pointwise in \(\gamma\) it tends to zero.

The standard upper-half-plane normalization can be read from Nedic, arXiv:2012.05532v1, Theorem 2.1 and (2.1)–(2.3) at \(n=1\), where the upper kernel is \(1/(t-z)-t/(1+t^2)\) and the measure is accompanied by \(1/\pi\). To rotate it, put \(q(z)=iG(-iz)\), \(z=iw\), and \(t=-\gamma\). Dividing the upper representation by \(i\) gives the signed compensator above. Our \(\mu\) is the reflected upper measure divided by \(\pi\). The real upper constant rotates into the imaginary drift and the linear slope keeps its coefficient. [Nedic, primary PDF](../../sources/witness62_herglotz/2012.05532.pdf) [Publisher record](https://doi.org/10.1007/s11785-021-01155-x)

Every factor obtained by restricting \(\mu\) to a Borel set is also Schur after exponentiating its negative increment. So is the affine factor because \(a\ge0\). They admit nontangential boundary limits by the bounded analytic Fatou theorem. The Poisson representation of a bounded harmonic function on the half-plane applies to their real parts. Equivalently, use the unit-disk theorem after \(w\mapsto(w-x)/(w+x)\), which sends \(x\) to zero and maps normalized Haar measure to \(P_x(t)\,dt\). Infinity corresponds to a single circle point of measure zero. For all finite products used below, the boundary limits give the same factorization almost everywhere. This justifies the products without needing boundary values of \(G\) itself.

## Fixed compact truncation

Fix \(R>0\) and let \(\mu_R=\mu|_{[-R,R]}\). It is a finite measure. Define \(G^{[R]}\) by replacing \(\mu\) with \(\mu_R\) and retaining the original \(a,b\). Set \(c_R=b-\int_{[-R,R]}\gamma/(1+\gamma^2)\,d\mu(\gamma)\), a finite real number for this fixed \(R\). The cocycle of \(G^{[R]}\) factors into a phase \(e^{-i\varepsilon c_R}\), the Gaussian factor
\[
 Q_\varepsilon(w)=e^{-a\varepsilon w-a\varepsilon^2/2},
\]
and \(B_\varepsilon(w)\), the finite-measure cocycle of \(\mu_R\) with the uncompensated Cauchy kernel. Write \(\|\cdot\|_x=\|\cdot\|_{L^2(P_x(t)\,dt)}\) on the boundary. The change in the defect caused by multiplication by the phase is at most \(\varepsilon|c_R|\) in this norm, since all the other factors have modulus at most one. It is negligible after division by \(\sqrt\varepsilon\) at fixed \(R\). No bound on \(c_R\) as \(R\to\infty\) is needed.

The Gaussian calculation is exact. Since \(|Q_\varepsilon(it)|^2=e^{-a\varepsilon^2}\), its Poisson average gives
\[
 \|1-Q_\varepsilon\|_x^2
   =1+e^{-a\varepsilon^2}-2e^{-a\varepsilon x-a\varepsilon^2/2},
 \qquad \lim_{\varepsilon\downarrow0}\varepsilon^{-1}\|1-Q_\varepsilon\|_x^2=2ax.
\]
The Gaussian defect has \(O_{a,M}(\varepsilon)\) norm on every fixed interval \([-M,M]\), by its exponential formula. The first-order energy from this factor therefore lies outside each fixed interval. For the measure factor, take \(M=R+1\). When \(|t|>M\),
\[
 \left|\int_0^\varepsilon\int_{[-R,R]}\frac{d\mu(\gamma)\,dr}{r+i(t-\gamma)}\right|
       \le\frac{\varepsilon\mu_R(\mathbb R)}{|t|-R}\le \varepsilon\mu_R(\mathbb R).
\]
The contraction estimate on the exponential gives \(\|1-B_\varepsilon\|_{x,\{|t|>M\}}=O_R(\varepsilon)\). Its full norm is \(O_{R,x}(\sqrt\varepsilon)\) by the finite-measure slope theorem.

The product defect decomposes as
\[
 1-Q_\varepsilon B_\varepsilon
   =(1-Q_\varepsilon)+Q_\varepsilon(1-B_\varepsilon).
\]
The mixed inner product is \(O_{R,x,a}(\varepsilon^{3/2})\), by Cauchy–Schwarz on \(|t|\le M\) using the Gaussian's compact bound, and on \(|t|>M\) using the finite-measure factor's exterior bound. The squared norm of the second term is exactly \(e^{-a\varepsilon^2}\|1-B_\varepsilon\|_x^2\). It follows that the slope for \(G^{[R]}\) is \(2ax\) plus the finite-measure slope for \(\mu_R\).

## Positive tail and the limiting quantifiers

Let \(G_{\rm tail}^{[R]}=G-G^{[R]}\), the compensated integral over \(|\gamma|>R\), and \(J_\varepsilon^{[R]}\) its Schur cocycle. Write \(H_\varepsilon^{[R]}\) for the cocycle of \(G^{[R]}\). The factorization \(H_\varepsilon=H_\varepsilon^{[R]}J_\varepsilon^{[R]}\) and the Schur bound imply
\[
 \frac{\left|\|1-H_\varepsilon\|_x-\|1-H_\varepsilon^{[R]}\|_x\right|}
      {\sqrt\varepsilon}
 \le \frac{\|1-J_\varepsilon^{[R]}\|_x}{\sqrt\varepsilon}.
\]
For every Schur \(J\), the elementary estimate \(|1-J|^2\le2(1-\Re J)\) and the harmonic Poisson identity imply
\[
 \|1-J_\varepsilon^{[R]}\|_x^2
       \le2(1-\Re J_\varepsilon^{[R]}(x)).
\]
At the fixed interior point \(x\), for each fixed \(R\),
\(J_\varepsilon^{[R]}(x)=1-\varepsilon G_{\rm tail}^{[R]}(x)+o_{R,x}(\varepsilon)\) by continuity of the generator and differentiability of the exponential. This yields
\[
 \limsup_{\varepsilon\downarrow0}
 \frac{\left|\|1-H_\varepsilon\|_x-\|1-H_\varepsilon^{[R]}\|_x\right|}
      {\sqrt\varepsilon}
   \le\left(2\int_{|\gamma|>R}
                    \frac{x}{x^2+\gamma^2}\,d\mu(\gamma)\right)^{1/2}. \tag{2}
\]
The right side goes to zero as \(R\to\infty\) because the kernel is bounded by \(C_x/(1+\gamma^2)\).

Each atomic integral profile satisfies \(0\le I_\alpha\le2\pi\alpha\), either from its gamma formula or the finite one-atom Poisson estimate. Consequently
\(\sum_\gamma P_x(\gamma)I_{\alpha_\gamma}\le 2\int x/(x^2+\gamma^2)\,d\mu(\gamma)<\infty\). Compacts exhaust all atoms and the truncated slopes therefore tend to the right side of (1), denoted \(S\). For each fixed \(R\), the limit of the truncated scaled norm is the square root of its truncated slope. The triangle inequality bounds the limsup of the absolute difference between the full scaled norm and \(\sqrt S\) by the right side of (2) plus the difference between the two slope square roots. Sending \(R\to\infty\) proves convergence of the full scaled norm to \(\sqrt S\), and squaring gives (1). This order of argument uses no estimates in \(\varepsilon\) uniform in \(R\).

## Checks and scope

- A pure imaginary drift has zero slope by the phase bound. The pure Gaussian case gives \(2ax\) exactly at first order.
- Lebesgue measure on \(\mathbb R\), an infinite-mass atomless example, obeys the weighted growth condition. At every positive real \(x\) its compensated transform has real part \(\pi\) and imaginary part zero by oddness of the combined imaginary part. Analytic uniqueness gives \(G(w)=\pi\) on the half-plane for \(a=b=0\), so the energy is \((1-e^{-\pi\varepsilon})^2=o(\varepsilon)\).
- For a conditional \(\xi\) representation under RH, the paired ordinates supply a measure with finite weighted mass by \(N(T)=O(T\log T)\). Applying (1) still requires the separate identification of the logarithmic derivative with this positive-real generator. The theorem provides no implication toward RH without those hypotheses.
- The standard sources checked here identify the Herglotz normalization and the finite-measure argument's weighted Wiener antecedent. They do not establish priority for the particular nonlinear slope formula. [Schulte, Theorem 3.9](../../sources/witness62_herglotz/2005.05212.pdf)
