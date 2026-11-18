# De Roton 2006, Proposition 5.1 and the phase tail

I checked the rendered published pp. 432–433 (PDF pp. 16–17), SHA-256 6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445. Proposition 5.1, equation (12), asserts both \(\varphi(x)=O(x^{-(1+1/d)/2})\) and \(\Phi(x)=O(x^{-(1+1/d)/2})\), where \(\varphi=U_F\chi\), \(\chi=\mathbf1_{(0,1)}\), and \(\Phi=x\varphi'\). The paper uses the asserted \(L^2\) membership of \(\Phi\) to invoke the operator representation (18). Its estimate for \(\Phi\) and that route into (18) fail in a degree-one source example. A separate integral representation for the required jets uses only \(\varphi\). [Primary PDF](https://www.numdam.org/item/10.24033/bsmf.2516.pdf)

## Exact degree-one counterexample

Take \(F=L(\cdot,\chi_4)\), where \(\chi_4\) is the real primitive odd character modulo four. This is a Selberg-class function of degree \(1\) with no pole at 1 and real root number \(+1\). Its complementary function equals \(-\sum_{n\le1/t}\chi_4(n)\) and is bounded and supported in \((0,1]\), so the source's \(L^2\) premise holds unconditionally. Proposition 5.1 precedes the zero-free assumption of §6.1.

The normalization in (2) has \(Q=2/\sqrt\pi\), \(\Delta(s)=\Gamma((1+s)/2)\), and
\[
 \frac{U_F(s)}s
 =\frac{(4/\pi)^{s-1/2}\Gamma((1+s)/2)}
       {(1-s)\Gamma(1-s/2)}
 =\frac{(2/\pi)^s\Gamma(s)\sin(\pi s/2)}{1-s}.
\]
The second equality follows by reflection for \(\Gamma(s/2)\Gamma(1-s/2)\) and duplication for \(\Gamma(s/2)\Gamma((s+1)/2)\). Put \(a=\pi/2\) and \(g(x)=(1-\cos(ax))/(ax)\). For \(0<\Re s<1\), its Mellin transform is
\[
 \frac1a\int_0^\infty x^{s-2}(1-\cos(ax))\,dx
 =\frac1{1-s}\int_0^\infty x^{s-1}\sin(ax)\,dx
 =\frac{a^{-s}\Gamma(s)\sin(\pi s/2)}{1-s}.
\]
The first integral is absolutely convergent. Integration by parts has vanishing endpoint terms, and the sine integral converges by oscillation. The sine Mellin formula follows from exponential damping and taking the limit in this strip. Since \(g\in L^2(dx)\) and the critical-line Mellin multiplier of \(U_F\chi\) is \(U_F(s)/s\), Mellin Plancherel identifies \(\varphi=g\) almost everywhere. With the smooth representative provided by this formula,
\[
 \Phi(x)=xg'(x)=\sin(ax)-g(x).
\]
At \(x=4n+1\), it tends to 1. On disjoint intervals of fixed positive length centered there, the sine is uniformly bounded below, and \(g=O(x^{-1})\). Hence \(\Phi\notin L^2(dx)\) and does not satisfy (12). The \(\varphi\) part of (12) holds in this example.

## Where the phase estimate loses a power

The printed Bessel term \(H_k\) on p. 433 is \(d^{-1}x^{A_k}J_{\nu_k}(a_F x^{1/d})\), where \(A_k=-1/2+(k-1)/d+i\theta\) and \(a_F\) is the paper's Bessel scale. The source writes \(G_k=-xH_k'\). Its chain-rule term is
\[
 -\frac{a_F}{d^2}x^{A_k+1/d}J'_{\nu_k}(a_Fx^{1/d}).
\]
The displayed calculation on p. 433 keeps \(x^{A_k}\) instead. The correct real-argument Bessel bound gives \(O(x^{-1/2+(2k-1)/(2d)})\) for this term. For \(k=1\) this allows a bounded oscillatory derivative at \(d=1\), exactly as in the witness above. For \(k=0\) it still gives \(O(x^{-\kappa})\) with \(\kappa=(1+1/d)/2\). The \(H_0\) term decays faster, (17) gives a faster remainder by choosing small fixed \(\varepsilon\), and the \(x^{-1}\) residue is acceptable for \(d\ge1\). Thus the \(\varphi\) bound used below follows from the \(k=0\) part of the same calculation. The near-zero bound \(\varphi=O_\varepsilon(x^{-\varepsilon})\) is already given by Lemma 4.

## Boundary jet continuation using \(\varphi\)

For \(\Re w<1/2\), with values at a single endpoint irrelevant, direct integration gives the \(L^2\) identity
\[
 \psi_{w,0}(x)=\chi(x)+w\int_0^1 v^{-w-1}\chi(x/v)\,dv.
\]
This is a Bochner integral since \(\|\chi(\cdot/v)\|_2=\sqrt v\,\|\chi\|_2\). The locally uniform integrability of additional powers of \(|\log v|\) gives holomorphy and differentiation in \(L^2\). The unitary Mellin multiplier \(U_F\) commutes with all dilations and can act inside this integral. With \(t=x\), its representative is
\[
 \phi_{w,0}(t)=\varphi(t)+w t^{-w}\int_t^\infty\varphi(y)y^{w-1}\,dy .
\]
For \(\Re w<1/2\) the pointwise integral agrees almost everywhere with the Bochner integral, by absolute convergence on compact \(t\)-intervals away from zero and the weighted dilation bound. The pointwise formula extends holomorphically to \(0<\Re w<\kappa\) and its \(k\)th \(w\)-derivative continues \(\phi_{w,k}=U_F\psi_{w,k}\). For \(t\ge1\), the same formula written with \(y=t/v\) is \(O(t^{-\kappa})\) after \(k\) differentiations, locally uniformly in that strip. This follows from \(\int_0^1 v^{\kappa-\Re w-1}|\log v|^j\,dv<\infty\) for \(j\le k\).

The Mellin transform of \(\varphi\) is absolutely convergent in \(0<\Re w<\kappa\) by the small- and large-\(t\) bounds. On the critical line it agrees with \(U_F(w)/w\) by the unitary multiplier identity and continuity. The identity theorem extends the agreement to the strip, where the gamma quotient is analytic. Splitting the last integral at zero consequently gives
\[
 \phi_{w,0}(t)=U_F(w)t^{-w}
   +\varphi(t)-w\int_0^1v^{w-1}\varphi(tv)\,dv .
\]
For a fixed compact \(w\)-set with \(\varepsilon<\Re w<\kappa\), the last two terms and all fixed \(w\)-derivatives are \(O_\varepsilon(t^{-\varepsilon})\) on \(0<t<1\). This follows from the near-zero bound for \(\varphi\) and integrable weights \(v^{\Re w-\varepsilon-1}|\log v|^j\). Thus the needed estimates of Proposition 6.3 follow without \(\Phi\) or the assumption required by the source's use of (18).

## Lower-bound scope

Apply the corrected Hardy expansion with the factor \((1-w)^{-L}\) inside the derivative, as checked separately. On a compact neighborhood of any critical-line \(w\), the large-\(t\) Hardy iterates retain \(O(t^{-\kappa})\) if \(d>1\), or gain fixed log powers over \(O(t^{-1})\) if \(d=1\). The small-\(t\) expansions give local domination below 1. Therefore the \(Q_\lambda\)-cutoff allows dominated convergence in \(L^2\) for the boundary jets and yields the same \(\partial_s^k[V_F(s)t^{-s}]\) expression in Proposition 6.5.

The exact support orthogonality uses only the unitary phase and the supported pole-removed complementary function. The Gram step then uses the highest log terms of the same cutoff jets. The target pairing also uses only the small-\(t\) and large-\(t\) bounds of \(\varphi\) and its Hardy iterates. In particular the finite-window lower coefficient remains \(m_\rho^2/|\rho|^2\). The repair replaces the published use of (18) in producing these jets. It does not establish that (18) holds in the counterexample, and the failure of Proposition 5.1's \(\Phi\) estimate does not refute Theorem 2. [Hardy derivative audit](witness62_deroton2006_prop64.md)
