# Source and priority map for the Herglotz boundary-energy slope

2026-11-17. The [finite-measure proof](witness62_herglotz_atomic_energy.md) and [independent review](threshold62_herglotz_atomic_energy_review.md) establish the nonlinear boundary-energy coefficient. The full weighted Herglotz statement under comparison uses
\[
G(w)=aw+ib+\int_{\mathbb R}\left(\frac1{w-i\gamma}-\frac{i\gamma}{1+\gamma^2}\right)d\mu(\gamma),
\qquad
H_\epsilon(w)=\exp\!\left(-\int_0^\epsilon G(w+r)\,dr\right),
\]
with \(a\ge0\), \(\mu\) positive and \(\int(1+\gamma^2)^{-1}d\mu<\infty\). For \(P_x(t)=x/(\pi(x^2+t^2))\), the matching assertion is the first-order coefficient of \(\int |1-H_\epsilon(it)|^2P_x(t)dt\). The checked material supplies definite antecedents for its Herglotz normalization, its semigroup realization, and the finite-measure *linear* Wiener step. It does not give the same nonlinear coefficient
\[
2ax+\sum_{\alpha_\gamma>0}\frac{2x\alpha_\gamma}{x^2+\gamma^2}
  \left(1-\frac{\Gamma(\alpha_\gamma+\frac12)}
                  {\sqrt\pi\,\Gamma(\alpha_\gamma+1)}\right),
\qquad \alpha_\gamma=\mu\{\gamma\}.
\]
The priority of that combined formula remains open.

## Exact source precedents

- **Lagarias, Acta Arith. 89 (1999), 217–234.** Equation (1.3) groups the complex conjugate zeros \(\rho,\bar\rho\), (1.5) is the positivity criterion for \(\Re(\xi'/\xi)(s)\) to the right of \(1/2\), and Theorem 1.1 plus the proof in §2 establishes the correspondence between location of the zeros and positive real logarithmic derivative. The primary article and the 2005 correction were consulted. The correction adds the \(t=0\) equality case to Lemma 3.1 and reverses the sign on \(1/(s-1)\) in (3.8). The Herglotz input from (1.3), (1.5), and §2 is separate from those corrections. [Article](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8932.pdf) · [Correction](https://doi.org/10.4064/aa116-3-5)
- **Suzuki, JLMS 108 (2023), *Aspects of the screw function*.** Equations (1.6)–(1.7) give \(Q_\xi(z)=i(\xi'/\xi)(1/2-iz)\), Nevanlinna under RH, with \(Q_\xi(iy)/y\to0\). Equation (2.6) and its proof give the subtracted Hadamard expansion, locally absolutely convergent, and cancel its residual constant at \(s=1/2\) using the functional equation. Under RH rotate \(z=iw\) and pair the ordinates \(\pm\gamma\). The \(1/\gamma\) compensators of (2.6) and the \(\gamma/(1+\gamma^2)\) compensators above both cancel in pairs. Thus in the displayed right-half-plane convention the exact data are \(a=b=0\) and \(\mu=\sum_{\gamma\ {\rm distinct}}m_\gamma\delta_\gamma\), both signs included. Absolute convergence of the paired formula follows from \(\sum m_\gamma/(1+\gamma^2)<\infty\). In particular this is an infinite-total-mass example, so it needs the full weighted theorem. Integrating \(G\) horizontally identifies \(H_\epsilon\) with the completed \(\xi\)-ratio on the open half-plane. The prior reconstruction still handles the replacement by the uncompleted \(\zeta\)-ratio. [Published §2.2 and Introduction](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12785) · [Earlier ratio proof and source comparison](../horizontal_ratio_slope_priority_ratio62.md)
- **Elliott, JFA (2009), *Adjoints of composition operators on Hardy spaces of the half-plane*.** Theorem 2 and equation (1) give the upper-half-plane positive harmonic representation \(cy+\int P_y\,d\sigma\) with \(\int(1+t^2)^{-1}d\sigma<\infty\), and explicitly call \(cy\) a mass at infinity. Rotating and setting \(\sigma=\pi\mu\) gives exactly the real part of the displayed \(G\). The imaginary constant is fixed by the value at one positive real center. This is the normalization needed for the boundary slope. Elliott's own operator results use Aleksandrov–Clark measures and adjoints. [Primary arXiv PDF](https://arxiv.org/pdf/0810.2184)
- **Schulte, arXiv:2005.05212v1.** Definition 3.1 and Theorem 3.9(1),(4) cover the ergodic scaled frequency measure proportional to \(((1-e^{-u})/u)^2du\) on \(u>0\). This yields the finite-measure linear limit \(4\pi\log 2\sum_\gamma\alpha_\gamma^2\) after Plancherel, as previously verified. The nonlinear energy instead has a nonquadratic atomic factor for fixed \(\alpha\). [Schulte PDF](../../sources/witness62_herglotz/2005.05212.pdf)

## Nearby results and the tested differences

| Primary source | Formula checked and point of comparison |
| --- | --- |
| [Gallardo–Gutiérrez, Siskakis, Yakubovich, arXiv:2110.05247](https://arxiv.org/pdf/2110.05247) | Eqs. (2.1)–(2.5) and Theorem 2.1 distinguish a multiplicative cocycle, its weighted composition semigroup and its generator \(Vf'+gf\). Eq. (2.4) is exactly the exponential integral representation along the flow. It does not evaluate the boundary-energy first variation on a reproducing kernel. |
| [Bracci, Contreras, Díaz-Madrigal, arXiv:math/0701834](https://arxiv.org/pdf/math/0701834) | Proposition 1.2 and Theorem 1.3 prove weak-* differentiability of the Aleksandrov–Clark measures \((\mu_{t,\tau}-\delta_\tau)/t\to-\lambda\delta_\tau+\mu\) for a composition flow at a boundary regular fixed point. These are the measures of a Cayley-transformed self-map at a Clark parameter. The present cocycle need not be a composition flow, and the squared defect is not that derivative. |
| [Elliott–Jury, composition operators on half-plane Hardy spaces](https://people.clas.ufl.edu/mjury/files/halfplane.pdf) | Proposition 2.1 is the positive-kernel criterion and the main theorem gives the exact operator norm in terms of the angular derivative at infinity. It applies to the translation component with angular derivative one. An operator norm and the boundary-energy slope of a fixed orbit are different data. |
| [Efraimidis, Llinares, MacDonald, Uriarte-Tuero, Vukotić, arXiv:2611.06877v1](https://arxiv.org/pdf/2611.06877v1), 4 November 2026 | Theorem 1 and Corollary 1.1 give a Cauchy law for the imaginary Herglotz boundary phase of a finite atomic singular inner function on the disk. The law depends on the total mass alone. The shift-integrated phase in \(H_\epsilon\) is accompanied by an attenuation at an atom. The Cauchy phase law does not supply that attenuation term or its gamma ratio. |
| [Poltoratski, arXiv:math/9601206](https://arxiv.org/pdf/math/9601206) | §3, (3.1)–(3.3), treats the exponential of a Cauchy transform in rank-one spectral shift and gives the Aronszajn–Krein-type resolvent relation. Its perturbation is a coupling parameter in a Möbius transform of a resolvent, rather than integration of positive real parts along horizontal translations. Classical high-level Cauchy tail laws can detect singular continuous mass, whereas the finite-measure horizontal energy here detects only atoms. |
| [Suzuki, screw line, arXiv:2209.04658](https://arxiv.org/pdf/2209.04658) and [Weil quadratic form, arXiv:2606.09096](https://arxiv.org/pdf/2606.09096) | The former's Theorem 1.1 and its proof give \(L^2\) norms of the screw line from a de Branges construction. The latter's §§1–2 concern a self-adjoint operator attached to the screw kernel and its smallest eigenvalue. These use the same \(\xi\)-spectral geometry while their variables, norms and increments differ from the Poisson-weighted horizontal ratio. |
| [Chevrié–Malti–Farges–Sabatier, IFAC fractional transfer-function norms](https://skoge.folk.ntnu.no/prost/proceedings/ifac2014/media/files/1458.pdf) | The paper computes \(H_2\) norms of elementary powers \((s+\lambda)^{-\nu}\) and estimates approximating such models. A single-atom profile here gives \(1-(s/(1+s))^\alpha\), an affine difference with a boundary branch point. The inspected formulas do not give this energy, or localization across general Herglotz measures. |

The November singular-inner result is a particularly useful control. If \(\Re G(it)=0\) a.e., as for a singular representing measure, then \(e^{-\epsilon G}\) is inner. The ordinary Poisson identity gives its squared defect exactly as \(2\Re(1-e^{-\epsilon G(x)})\). In that model the slope is \(2\Re G(x)\), including singular continuous mass. This formula concerns the pointwise exponential \(e^{-\epsilon G}\). It cannot replace the integrated increment in the horizontal cocycle, even when \(G\) is singular and has finite total mass.

## Actionable links and convergence conventions

**Compactified linear defect.** For the disk map \(\phi_x(w)=(w-x)/(w+x)\), the disk Herglotz measure of \(\Re G(\phi_x^{-1}(\cdot))\) is the pushforward of
\[
ax\,\delta_\infty+\frac{x}{x^2+\gamma^2}\mu(d\gamma)
\]
under \(\phi_x\), with \(\phi_x(\infty)=1\). This follows by transforming the Poisson kernel. At a finite ordinate the multiplier is \(x/(x^2+\gamma^2)\); at infinity the disk kernel is \(\Re w/x\). The positive boundary measures
\[
\epsilon^{-1}(1-\Re H_\epsilon(it))P_x(t)\,dt
\]
converge against continuous tests on that compactification to this linear Herglotz measure, before using a finite-atom nonlinear limit. Indeed their total masses are \(\Re(1-H_\epsilon(x))/\epsilon\to\Re G(x)\), and Poisson transforms converge at each disk interior point by the locally uniform limit \((1-H_\epsilon)/\epsilon\to G\). Compactness and uniqueness of Poisson representation identify the weak limit. The quadratic energy is bounded as a measure by twice the linear defect. Its finite-atom gamma factor and any disappearance of diffuse mass require the separate energy calculation.

**Weighted composition orbit.** With boundary \(dt\) as the unnormalized norm, the normalized Hardy kernel is \(k_x(w)=\sqrt{x/\pi}/(w+x)\), so \(|k_x(it)|^2=P_x(t)\). Define \(W_\epsilon f(w)=H_\epsilon(w)f(w+\epsilon)\). The cocycle identity gives a contraction semigroup: right translations contract on half-plane Hardy space and multiplication by \(H_\epsilon\) contracts by its Schur bound. Strong continuity follows from strong continuity of Hardy translations and dominated convergence of \(H_\epsilon(it)\to1\) a.e. The latter holds by local boundary integrability of the increment, using the weighted tail subtraction and the finite mass on compact intervals. Since \(\|k_x(\cdot+\epsilon)-k_x\|_2=O(\epsilon)\), the difference between \(\|(I-W_\epsilon)k_x\|_2\) and \(\|1-H_\epsilon\|_{L^2(P_xdt)}\) is \(O(\epsilon)\). Thus the energy limit is precisely the coefficient of the squared displacement of this Hardy orbit. If that coefficient is \(E_x\), evaluation at the kernel center gives
\[
\langle W_\epsilon k_x,k_x\rangle
=H_\epsilon(x)\frac{2x}{2x+\epsilon},
\qquad
\lim_{\epsilon\downarrow0}\frac{1-\|W_\epsilon k_x\|_2^2}{\epsilon}
=\frac1x+2\Re G(x)-E_x.
\]
This reformulation turns the theorem into a norm-loss diagnostic for a concrete semigroup. An exact positive \(E_x\) also rules out \(k_x\) belonging to the generator domain, because a domain vector has displacement \(O(\epsilon)\). A zero coefficient alone does not establish domain membership.

**Escape and test classes.** For \(G(w)=aw+ib\), the scalar identity is
\[
\int |1-H_\epsilon(it)|^2P_x(t)dt
=1+e^{-a\epsilon^2}-2e^{-a\epsilon^2/2-ax\epsilon}\cos(b\epsilon).
\]
It follows from the Cauchy characteristic function and gives the slope \(2ax\). For \(a>0\) the measures tend vaguely to zero on the real line, yet their total mass tends to \(2ax\). Hence they cannot converge weakly to a finite measure on \(\mathbb R\) against all bounded continuous tests. On the compactification, this is exactly mass at infinity. Even a bounded continuous oscillatory test can fail to have a limit: with \(b=0\), \(W(t)=\cos(\tau\log(1+|t|))\), substitute \(v=\epsilon t\) in the quadratic energy. The rescaled density converges in \(L^1(dv)\) to \(x|1-e^{-iav}|^2/(\pi v^2)\) by dominated convergence. The oscillatory coefficient tends, after removing the phase \(e^{-i\tau\log\epsilon}\), to the Mellin transform of that integrable density at \(i\tau\), which is nonzero for small enough \(\tau>0\) by continuity at zero. Choosing different phase subsequences gives distinct limits. The finite-\(\mu\) unweighted \(C_b\) convergence in the earlier proof is weak convergence, with no assertion of total-variation convergence to a nonzero atomic measure.

## Coverage

I searched formulations involving Hardy norms of horizontal translates, outer ratios with boundary zeros, integrated Herglotz transforms, singular-inner phases, half-plane Clark measures, weak first variations of holomorphic flows, Wiener diagonal detection, and fractional single-atom transfer functions. I checked the indicated passages in author or journal PDFs, and included the fresh November 2026 singular-inner result. [Source URL, access and hash records](../../sources/ratio62_herglotzpriority/retrieval.tsv) preserve the checked versions. No conclusion about exhaustive priority, general composition flows or a Carlson norm follows from the search.
