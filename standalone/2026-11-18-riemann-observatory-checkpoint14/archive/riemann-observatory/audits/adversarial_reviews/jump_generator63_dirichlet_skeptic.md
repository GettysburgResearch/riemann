# Independent check of the single-generator Dirichlet criteria

17 November 2026. Fix one Dirichlet character \(\chi\) and write \(F(s)=L(s,\chi)\). For an imprimitive character, GRH here concerns the nontrivial zeros of its inducing primitive character. I checked the source approximation hypothesis, the physical dilation spaces, the strong generator domain and the multiplicity argument. The conclusions are scoped, with classical zero-free and functional-equation facts as inputs. [Dimitrov–Oliveira, arXiv v1](https://arxiv.org/pdf/1608.07887v1) · [Manzur–Noor, arXiv v1](https://arxiv.org/pdf/2610.03568v1) · [Zeta generator check](jump_generator63_single_member_skeptic.md)

## Spaces and the strong generator

Let \(S\) be the complex unit-step subspace of \(L^2([1,\infty),dx/x^2)\), and extend elements by zero below 1. For integers \(n\ge1\), let \(U_n b(x)=b(x/n)\). It preserves \(S\) and has norm \(n^{-1/2}\). Write

\[
 f_\chi(x)=\sum_{n\le x}\chi(n),\qquad
 g_{\chi,k}=U_k f_\chi-k^{-1}f_\chi\quad(k\ge2),
 \qquad Mb(s)=\int_1^\infty b(x)x^{-s-1}\,dx.
\]

For a nonprincipal character the sum of a full period vanishes, so \(f_\chi\) is bounded and lies in \(S\). For a principal character modulo \(q\), \(f_\chi(x)=rx+O_q(1)\) with \(r=\varphi(q)/q>0\), so its norm diverges. Each \(g_{\chi,k}\) is bounded in both cases and is periodic with period \(qk\). In the principal case the latter follows directly from cancellation of the increments \(\varphi(q)\) and \(k\varphi(q)/k\) under translation by \(qk\).

The established jump group \(J_\tau\) multiplies the jump at \(n\) by \(n^{i\tau}\). For any bounded step vector \(b\), summation by parts yields

\[
 J_\tau b(x)=x^{i\tau}b(x)-i\tau\int_1^x t^{i\tau-1}b(t)\,dt .
\]

The difference quotient is dominated by \(2\|b\|_\infty\log x\), whose square is integrable against \(dx/x^2\). Pointwise convergence and dominated convergence in the squared norm prove \(b\in\mathcal D(G)\) for the strong generator \(G\). Its jump at \(n\) is \(i\log n\) times the old jump. As a sign check, for \(\Re s>1\) the Dirichlet series for \(sMb(s)\) is the sum of the jumps times \(n^{-s}\), so \(sM(Gb)(s)=-i(sMb(s))'\). Holomorphy extends the identity throughout \(\Re s>1/2\). Thus, with \(a_k(s)=k^{-s}-k^{-1}\),

\[
 sMf_\chi(s)=F(s)\quad(\chi\text{ nonprincipal}),\qquad
 sMg_{\chi,k}(s)=F(s)a_k(s),\qquad
 M(Gb)(s)=-\frac i s\frac{d}{ds}[sMb(s)].
\]

The first two identities follow by integration of the Dirichlet summatory series on \(\Re s>1\), and the principal pole in the second is removable. In particular \(Mg_{\chi,k}(1)=-r\log k/k\) for a principal character. [Exact step transport](director_manzur_noor_round8.md)

## Forward density in the intended closed spans

Put \(X_\chi=\overline{\operatorname{span}}^{S}\{U_n f_\chi:n\ge1\}\) for nonprincipal \(\chi\), and \(W_\chi=\overline{\operatorname{span}}^{S}\{g_{\chi,k}:k\ge2\}\) for either type. I checked Dimitrov–Oliveira Theorem 2, p. 3, and its supporting integer-approximation passages, pp. 14–17, in PDF SHA-256 `3ecbabfe36c9321c4c0695caa99bd92bdbc00d20a2e86c5c50c6cd289edad6ef`. At \(p=2\) its qualitative conclusion under zero-freeness in \(\Re s>1/2\) is \(\|(1-F(s)A_N(s))/s\|_{L^2(dt/(2\pi))}\to0\), with ordinary complex Dirichlet polynomials \(A_N\) and arbitrary integer indices. Theorem 3 describes a different interpolation problem and is unnecessary here. For nonprincipal \(\chi\), Mellin–Plancherel identifies these approximants with finite combinations of \(U_n f_\chi\) and the target with 1 in \(S\). Integer dilation invariance then gives every \(U_n1=\mathbf1_{[n,\infty)}\) in \(X_\chi\). Consecutive differences span the individual cells, proving \(X_\chi=S\) under GRH. [Primary theorem and proof](https://arxiv.org/pdf/1608.07887v1)

For the principal case, begin in the ambient space \(L^2((0,\infty),dx/x^2)\) with \(h_\chi(x)=f_\chi(x)-rx\). It equals \(-rx\) on \((0,1)\) and is bounded above 1. Its full Mellin transform is \(F(s)/s\) for \(0<\Re s<1\). Indeed the integral over \((0,1)\) is \(r/(s-1)\), and the integral over \([1,\infty)\) continues \(F(s)/s-r/(s-1)\) from \(\Re s>1\). For an ordinary polynomial \(A(s)=\sum c_n n^{-s}\), the unrestricted residual below 1 is \(rx A(1)\), whose norm on \((0,1)\) is \(r|A(1)|\). Hence every norm-approximating sequence from the qualitative theorem has \(A(1)\to0\). Subtracting \(A(1)h_\chi\) from its approximant changes the norm by at most \(|A(1)|\|h_\chi\|\) and gives exactly \(\sum c_n g_{\chi,n}\), with \(g_{\chi,1}=0\). This proves that \(1\in W_\chi\) under RH. The identity \(U_n g_{\chi,k}=g_{\chi,nk}-k^{-1}g_{\chi,n}\) then gives \(W_\chi=S\) by the same cell argument. This subtraction uses the actual pole term and the norm below 1. [Qualitative input](https://arxiv.org/pdf/1608.07887v1)

There is an independent finite-factor transfer directly on \(S\). If \(\chi^*\) induces \(\chi\), set \(E(U)=\prod_{p\mid q,\,p\nmid q^*}(I-\chi^*(p)U_p)\). Each factor is invertible by a norm-convergent Neumann series. The exact finite coefficient convolution gives \(f_\chi=E(U)f_{\chi^*}\) pointwise, and therefore \(g_{\chi,k}=E(U)g_{\chi^*,k}\), where the latter equality is an identity of bounded vectors even in the principal case. The inducing dilation spans are invariant under every \(U_p\); their closures are invariant under the factors and their inverses. Consequently \(X_\chi=X_{\chi^*}\) in the nonprincipal case and \(W_\chi=W_{\chi^*}\) in both cases, without a zero assumption. For principal \(\chi\), the inducing character has modulus 1 and Noor's Theorem 8 or Manzur–Noor (A) gives \(W_\zeta=S\) under RH after the unitary step conversion \(Bh_k=k g_{\zeta,k}\). This also allows the nonprincipal forward proof to invoke Dimitrov–Oliveira only for a primitive character. [Noor, Theorem 8](https://arxiv.org/pdf/1809.09577v4) · [Step conversion](director_manzur_noor_round8.md)

Direct cell controls confirmed the convolution and anchored periodicity for the principal character modulo 6, the real primitive character modulo 3 induced to modulus 6, and an order-four character modulo 5 induced to modulus 20. The checks covered cells 1–300 and anchors 2, 3 and 5, using the integer-scaled vectors \(k g_{\chi,k}\). The identities above prove these assertions for every fixed modulus and all cells.

## The single membership tests and the anchor obstruction

For any \(\rho\) with \(\beta=\Re\rho>1/2\), the functional \(\ell_{\rho,j}(b)=(Mb)^{(j)}(\rho)\) is continuous on \(S\). Cauchy–Schwarz gives norm at most \(\sqrt{(2j)!}/(2\beta-1)^{j+1/2}\) using the logarithmic Mellin integrand. Suppose \(1/2<\beta<1\) and \(\rho\) is a zero of exact order \(m\) of \(F\). Every Mellin transform from \(X_\chi\) in the nonprincipal case and from \(W_\chi\) in the principal case vanishes through order \(m-1\) at \(\rho\), because the generator transforms have a factor \(F\) and the jet evaluations pass to the closure. For the two selected vectors the exact failing evaluations are

\[
 \ell_{\rho,m-1}(G f_\chi)=-\frac{i}{\rho}F^{(m)}(\rho),\qquad
 \ell_{\rho,m-1}(G g_{\chi,k})=-\frac{i}{\rho}a_k(\rho)F^{(m)}(\rho).
\]

The relevant values are nonzero. For the second, \(|k^{-\rho}|=k^{-\beta}>1/k\). This includes real exceptional zeros and every finite multiplicity. It also gives a distance lower bound by dividing the modulus of the failing evaluation by the displayed norm bound. The Euler factors \(1-\chi^*(p)p^{-s}\) have zeros on \(\Re s=0\) and preserve open-strip multiplicities. The primitive functional equation and complex conjugation send a zero of \(\chi^*\) at \(\rho\) to a zero of the *same* \(\chi^*\) at \(1-\bar\rho\), preserving order. The two operations separately involve the conjugate character. Absolute convergence and classical nonvanishing on \(\Re s=1\) rule out further zeros to check on the right boundary, with the principal pole at \(1\) treated above.

It follows that for every fixed nonprincipal \(\chi\), \(G f_\chi\in X_\chi\) is equivalent to GRH for \(\chi\). For each principal \(\chi\) and every individually fixed \(k\ge2\), \(G g_{\chi,k}\in W_\chi\) is equivalent to RH. Only one vector and its first strong derivative are tested. The reverse directions require neither an invariant domain for all vectors nor a density estimate for progressions of zeros. The use of higher Mellin jets is essential when the selected zero is multiple. [Zeta precedent within the archive](jump_generator63_single_member_skeptic.md)

For a nonprincipal character, every \(b\in W_\chi\) satisfies \(Mb(1)=0\). Here \(F\) is regular at 1, and the exact strong derivative gives

\[
 M(Gg_{\chi,k})(1)=\frac{i\log k}{k}F(1)\ne0.
\]

So \(Gg_{\chi,k}\) is outside the anchored closure unconditionally, at distance at least \(|F(1)|\log k/k\) since the evaluation representer is the constant 1 of norm 1. In fact \(W_\chi=X_\chi\cap\ker M(\cdot)(1)\) without GRH. To approximate a vector in that intersection, project each finite unanchored approximant to the kernel along \(f_\chi\), whose evaluation is \(F(1)\). Its projected approximants lie in the span of the \(g_{\chi,n}\). Under GRH this is the entire evaluation kernel in \(S\), making the stated distance exact. [Hardy evaluation and principal pole contrast](director_imprimitive_anchor_round8.md)

These are closure assertions in the unit-step space. For example, \(Gf_\chi\) for a nonprincipal character has zero jump at 1 and jump \(i\chi(p)\log p\) at any prime \(p\) not dividing the modulus. A finite dilation combination matching its first jump must have zero coefficient on \(f_\chi\). Its jumps at primes beyond all its dilation indices are then zero. The same prime control applies to \(Gg_{\chi,k}\) with prime jump \(-i\chi(p)\log p/k\) for \(p>k\). Thus the criteria do not provide a finite-length representation or a convergence rate. No publication-priority claim is made.
