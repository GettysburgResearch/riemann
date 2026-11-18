# Independent review of the classical-norm Mertens shift

2026-11-17. I reconstruct the [candidate](../../proposals/independent_campaigns/mertens_shifted_q1_latest62_round5.md) below. The fixed shift \(\epsilon=A/\sqrt{L\log L}\), \(L=\log N\), works for **every fixed \(A>C\)** under RH, the stated Mertens bound with constant \(C\), and the cited Bui–Florea–Heycock reciprocal first moment. The classical norm is \(O((L\log L)^{-1/4})\) and inherits the exact ratio slope. The second Perron constant \(C_*\) need not be compared with \(A\). I found no fatal inequality. This is a scoped mathematical check with the stated inputs, with priority unassessed.

## Primary input and versions

1. [Balazard–de Roton, arXiv:0812.1689v1](../../sources/selberg_round2/balazard_roton.pdf), SHA-256 d22890fc5903bce4c8be302a35ff5b4d84f33c63a84e9799c04136e5fdf76311. Proposition 2 supplies \(J_\epsilon\ll\epsilon\), (12) exemplifies the vertical Perron recentering and (15) is the fixed-\(t\) twisted Abel identity. Proposition 13's printed (16) shows the power \(+1\) on the zeta term, while (17), the proof, and the definition of \(I_{N,\epsilon}\) use the reciprocal. I use (17) and its proof. It needs only Proposition 4(i), the convexity bound and the Montgomery–Vaughan mean square. It never invokes Proposition 14 or that proposition's larger lower threshold on \(\epsilon\).
2. [Bui–Florea–Heycock, arXiv:2610.27591v1](../../sources/recent_corpus_round5/2610.27591.pdf), SHA-256 471eef2f839d4e67f9018c58d8a7fd529dc7bd10271c4b008bfba541d046d555. Theorem 1.4 at \(k=1\) supplies the stated \(M(x)\) bound with some \(C>0\); it is an input here. The separate moment input is Theorem 1.2 (1.4), with fixed theorem parameter \(1/3\) and, for example, \(c=1/2\). At \(b(Y)=B_0/(\log Y\log\log Y)\), \(B_0\ge C_1(1/3)\) fixed, the lower cutoff holds and \(b(Y)\log Y=B_0/\log\log Y\ll(\log\log\log Y)^{-c}\). The bound is \(Y^{-1}\int_Y^{2Y}|\zeta(1/2+b(Y)+iv)|^{-1}\,dv\ll e^{(\log Y)^{1/3}}\). The shifted integrand has power one. Neither powers above one nor a short-window moment are imported. Section 8.1 is the antecedent for the untwisted dyadic Perron setup. The terminal connectors below are estimated directly.
3. [Bui–Florea, Negative moments](../../sources/latest62_q1_round5/bui_florea_publisher.pdf), SHA-256 0fa36e9efeeb3e96448191f814ec1ae42cbd4c355dad2863b7ba552b32127921. Despite the local filename, the repository cover labels this the **accepted author manuscript** of the [2024 journal paper](https://doi.org/10.1515/crelle-2023-0091). Lemma 2.2, internal pp. 8–9, equation (2.8) follows from Lemma 2.1 and coefficient bound (2.6), with the displayed logarithmic dependence on the small shift. In particular the coefficient proof uses powers \(e^{-2\pi j\Delta a}\) summed into \(-\log(1-e^{-2\pi\Delta a})\) and the uniformly bounded remainder in (2.6). For \(v\) large, \(w=\log |v|\), and \(a\log w=o(1)\), it yields
\[
\log |\zeta(1/2+a+iv)|^{-1}
\le \frac{w}{2\log w}\mathcal L(w,a)
+O\left(\frac w{\log w}+\frac{w\mathcal L(w,a)}{(\log w)^2}\right),\quad
\mathcal L(w,a)=\log\frac1{1-e^{-2a\log w}}.
\]
The proof's small-shift errors are uniform in the ranges used below. The estimate \(\mathcal L(w,a)=\log(1/a)-\log\log w+O(1)\) holds uniformly when \(a\log w\) is sufficiently small. To absorb the last error into an \(O(1)\) inside the leading bracket one also needs \(\mathcal L(w,a)\ll\log w\). The central-panel bound below retains the full formula where this auxiliary requirement might fail. The third case of Lemma 2.2, with fixed \(a=1/4\), gives \(\log|\zeta(3/4+iv)|^{-1}\le o(w)\). Conjugation gives the negative ordinates. Only RH is required for these uses of Lemma 2.2.

## Twisted Perron estimate at an arbitrary cutoff

Put \(U=\log X\), \(\phi(U)=\sqrt{U/\log U}\), and \(s=1/2+it\). The needed independent estimate is
\[
|\zeta(s)M_X(it)|\ll\sqrt X\bigl(|\zeta(s)|e^{C_*\phi(U)}
 +(1+|t|)^{1/2}e^{D_*\sqrt U/\log U}\bigr),\quad |t|\le X^{3/4}.
\tag{Q}
\]
The constants are uniform in this range of \(t\) and do not depend on the target shift \(\epsilon\).

**Endpoint and recentering.** Replace \(X\) in the Perron integral by \(X'=\lfloor X\rfloor+1/2\), which counts exactly the same set of integers. The usual error term on the line \(1+1/\log X'\) at height \(X'\) is \(O(\log X')\), uniformly in \(t\), because the coefficient moduli are \(\le1\). To see this directly, the Perron error for \(n\asymp X'\) is bounded by a constant times the sum of \(1/|n-X'|\), using the half-integer distance. For \(n\) outside \([X'/2,2X']\) use \(|\log(X'/n)|\gg1\) and \((X')^{1+1/\log X'}/X'=O(1)\). The latter terms sum to \(O(\log X')\) by the absolutely convergent majorant. After shifting \(z\) by \(it\), change the integration endpoints from \(t\pm X'\) to \(\pm X'\). On the short added segments the reciprocal is \(O(\log X')\), the denominator \(|z-it|\asymp X'\), and the total length is \(O(|t|)\). The combined error is \(O((1+|t|)\log X')\). Multiplying by the RH critical-line subpower bound, the ratio of that error to \(\sqrt X(1+|t|)^{1/2}\) tends to zero uniformly for \(|t|\le X^{3/4}\), taking for instance the zeta exponent \(1/12\). The half-integer replacement changes \(\log X\) by \(O(1/X)\). In the remainder of this argument I use \(X\) to denote that half-integer, with the original bound on \(t\) up to harmless endpoint constants.

**Original dyadic panels and far ordinates.** Let \(X_0=\exp(\phi(U))\) and run the central panel at \(b(X_0)\), then panels on \([Y,2Y]\), \(Y=2^jX_0\), and their reflections at \(b(Y)\), truncating the last at \(X\). All deformation points have real part \(>1/2\), so \(1/\zeta(z)\) has no pole there on RH. The pole of \((z-it)^{-1}\) is also left of the contour. The potential passage at \(z=1\) is harmless because the reciprocal has a zero. Whenever \(|v-t|\gg |v|\), a vertical panel costs at most \(O(\sqrt X e^{b(X_0)U+U^{1/3}})\) by the first reciprocal moment and the denominator \(O(1/Y)\); a truncated panel is bounded using its full panel's moment. Here \(b(X_0)U=O(\phi(U))\), and \(U^{1/3}=o(\phi(U))\). There are \(O(U)\) panels. For an old dyadic connector at \(v\asymp Y\), the shifts are comparable to \(b(Y)\). The abbreviated pointwise bound applies, since \(\log(1/b(Y))=\log\log Y+\log\log\log Y+O(1)\), and gives \(|\zeta|^{-1}\ll Y^{1/2+o(1)}\) uniformly. The connector length is \(\le1\). With the far denominator \(O(1/Y)\) the same first term of (Q) dominates. Negative ordinates are far when \(t\ge0\); the sign of \(t\) can be reversed by conjugation.

**Central panel and small t.** For \(|v|\le O(X_0)\) and shift comparable to \(b(X_0)\), the full bound gives the reciprocal at most \(e^{O(\phi(U))}\): for fixed large \(v_0\) and \(w'=\log|v|\ge\log v_0\), the logarithm of the reciprocal is bounded by a constant times \((w'/\log w')(\log (1/b(X_0))+1)\). Both \(a\log w'=o(1)\) and \(\log(1/b(X_0))=O(\log U)\) hold uniformly. The function \(w'/\log w'\) is increasing in this range and \(w'\le\phi(U)+O(1)\). On \(|v|\le v_0\), factorize about the finitely many zero locations in a slightly larger compact set. Away from their neighborhoods the reciprocal is bounded, and inside it is \(O(b(X_0)^{-m})\) for a finite maximum multiplicity \(m\). These give \(e^{O(\phi(U))}\) as well. The denominator integral over any interval of length \(O(X_0)\) is \(O(\log X_0+1)\) uniformly in \(t\) since the real part is \(\ge1/2\). Thus the central panel has the first size in (Q). If \(0\le t<4X_0\), integrate the finitely many possibly near panels and connectors through \(16X_0\) the same way. Beyond them the kernel is far.

**Near vertical for large t.** For \(4X_0\le t\le O(X^{3/4})\) choose dyadic joins \(a_1\in(t/4,t/2]\) and \(a_2\in[2t,4t)\), available before the terminal cut because \(4t<X\) for large \(X\). Replace the panels between those joins by a vertical at shift \(a=\min(U^{-1/2},w/(U\log w))\), \(w=\log t\). On this vertical \(\log v=w+O(1)\), \(w\ge\phi(U)+O(1)\), \(w\le U\), and \(\log w\asymp\log U\). The shift satisfies \(a\log w=o(1)\) and \(\log(1/a)=O(\log w)\) uniformly. Therefore the shortened pointwise form applies, with an \(O(1)\) change in its bracket if \(w\) replaces \(\log v\). The factor from the vertical denominator is \(O(1+w)\). After multiplying by the RH bound \(\log^+|\zeta(s)|\ll w/\log w\) and dividing by \(t^{1/2}\), the exponent is bounded by
\[
aU+\frac{w}{2\log w}
  \{\log(1/a)-\log\log w-\log w+O(1)\}.
\]
At \(a=w/(U\log w)\) this equals \(\frac{w}{2\log w}[\log(U/w^2)+O(1)]\), with positive part \(O(\sqrt U/\log U)\) by boundedness above of \(r\log(K/r^2)\) for \(r=w/\sqrt U>0\). At the capped \(a=U^{-1/2}\), one has \(w\ge\sqrt U\log w\), so the bracket is \(\le-2\log\log w+O(1)\); multiplication by \(w/(2\log w)\ge\sqrt U/2\) absorbs \(aU=\sqrt U\) for large \(U\). The vertical denominator factor \(O(1+w)\) has logarithm negligible on this scale. This proves the second part of (Q).

At the new joins \(a_1,a_2\) every intermediate shift \(\beta\) obeys \(\beta\log w=o(1)\), \(\beta U\ll\phi(U)+w/\log w\), and \(\log(1/\beta)\le\log w+O(\log\log U)\). For the last bound at the uncapped shift use \(U/w^2\ll\log U\), at the cap use \(w\ge\sqrt U\log w\), and at the old shift it follows from its definition. The shortened pointwise estimate then gives a reciprocal \(\le e^{(2/3)w}\) uniformly for large \(U\). Their kernel is \(O(1/t)\) because both joins are separated from \(t\) by \(\gg t\). The lost \(e^{-w/3}\) absorbs \(e^{O(w/\log w)}\), leaving the first part of (Q).

**Top and bottom connectors.** At \(v=\pm X\), the kernel is \(O(1/X)\), for the same fixed \(t\)-range. The last old shift \(b\asymp1/(U\log U)\) has a reciprocal bound \(\le e^{U/2+O(U/\log U)}\) by the shortened pointwise estimate. Write \(\xi=C_0(s)\zeta(s)\) temporarily for the completion multiplier. Its vertical Stirling ratio across bounded horizontal increments obeys \(|C_0(1/2+\alpha_2+iv)/C_0(1/2+\alpha_1+iv)|\ll X^{(\alpha_2-\alpha_1)/2}\) uniformly. On RH the product of paired factors of the shifted \(\xi\) is nondecreasing in positive real argument at fixed \(v\), so the reciprocal estimate transfers from \(\alpha_1\) to \(\alpha_2\) by at most this multiplier ratio. For \(b\le\alpha\le1/4\), the full top integrand \(X^{\alpha-1/2}|\zeta(1/2+\alpha+iv)|^{-1}\) is then at most \(X^{3/8+o(1)}\). For \(1/4\le\alpha\le1/2+1/U\), start at the fixed-quarter Bui–Florea estimate \(e^{o(U)}\); since \(X^{\alpha-1/2}\le e\), the upper bound is \(X^{1/8+o(1)}\). The connectors have bounded length. Their contribution is \(o(\sqrt X)\), prior to multiplication by \(|\zeta(s)|\), and fits the first term of (Q). This separate estimate avoids assuming any monotonicity of the entire approximate BFH terminal integrand. All parts of (Q) have now been bounded.

## Classical norm and independence of \(C_*\)

Let \(D_N(s)=1/\zeta(s+\epsilon)-P_N(s)\). The Mertens bound implies convergence of the ordinary Möbius Dirichlet series in every fixed half-plane \(\Re(s+\epsilon)>1/2\) by Abel summation, agreeing with the reciprocal by continuation from \(\Re(s+\epsilon)>1\). For the low-height estimate use
\[
D_N(s)=-M(N)N^{-s-\epsilon}+(s+\epsilon)\widehat g(t),\qquad
g(u)=\mathbf1_{u\ge L}e^{-(1/2+\epsilon)u}M(e^u).
\]
The integer cutoff has the correct endpoint \(-M(N)\), because it counts the coefficients up to and including \(N\). For \(U\ge L\), eventual concavity of \(\phi\) and \(\phi'(L)=\phi(L)(1-1/\log L)/(2L)\) imply \(\epsilon-C\phi'(L)\gg_{A,C}\epsilon\). Consequently
\[
\|g\|_2\ll_{A,C}\epsilon^{-1/2}e^{-(A-C)\phi(L)} .
\]
Plancherel, boundedness of \((s+\epsilon)/s\), and RH critical-line growth up to \(T_0=e^{B\phi(L)}\) give the same bound for the low-height integral after multiplication by at most \(e^{o(\phi(L))}\), for every fixed \(B\). The low-height endpoint term is bounded using \(\|\zeta/s\|_{L^2(dt)}<\infty\) and \(M(N)N^{-1/2-\epsilon}\ll e^{-(A-C)\phi(L)}\). This is the sole place where \(A>C\) is needed.

On \(T_0\le|t|\le N^{3/4}\), the twisted Abel identity is
\[
D_N(s)=-N^{-1/2-\epsilon}M_N(it)
 +(1/2+\epsilon)\int_N^\infty X^{-3/2-\epsilon}M_X(it)dX .
\]
Estimate it by (Q) for all \(X\ge N\), since \(|t|\le X^{3/4}\). For the first part of (Q), \(\phi(U)\le\phi(L)\sqrt{U/L}\) and \(C_*\sqrt{U/L}-(A/2)U/L\le C_*^2/(2A)\). Hence the endpoint plus integral in \(U=\log X\) is bounded by \(e^{B_1\phi(L)}|\zeta(s)|\) after absorbing the polynomial \(\epsilon^{-1}\) factor, for a fixed \(B_1\) independent of \(B\). Convexity with exponent \(3/8\) gives \(\|\zeta/s\|_{|t|\ge T_0}\ll T_0^{-1/8}\). Choosing \(B>8(B_1+1)\) makes this part \(e^{-\phi(L)}\), even if \(C_*>A\). The low-height estimate remains valid for this fixed \(B\).

For the second part of (Q), \(D_*\sqrt U/\log U\le (A/4)\phi(U)\) uniformly for \(U\ge L\) when \(L\) is large. The same concavity gives coefficient \(O((1+\epsilon^{-1})e^{-(3A/4)\phi(L)})\) multiplied by \((1+|t|)^{1/2}\). The weighted \(L^2\) cost of that latter factor over the middle range is \(O(\sqrt L)\), from integration of \(dt/t\). Both middle contributions are \(o(\sqrt\epsilon)\).

For completeness the high tail follows by applying the verified (17): on \(T\le |t|\le2T\), \(|s|^{-2}\ll T^{-2}\). Proposition 4(i) gives a ratio square mean \(\ll T^{1+\epsilon}\le T^{3/2}\). For the polynomial mean, \(|\zeta(s)|^2\ll T^{1/2}\) and Montgomery–Vaughan gives \((T+N)\sum_{n\le N}|\mu(n)|^2n^{-1-2\epsilon}\ll (T+N)\log N\) for \(N\ge2\), uniformly in \(0<\epsilon\le1/2\). Summing the displayed (17) on \(T=2^jN^{3/4}\) gives \(O(N^{-1/8}\log N)\), hence \(O(N^{-1/9})\), for the squared tail norm. It is \(o(\epsilon)\), independently of Proposition 14.

Thus \(\|\zeta D_N/s\|_{L^2(dt/(2\pi))}=o(\sqrt\epsilon)\). The norm triangle inequality gives
\[
|d_1(P_N)-\sqrt{J_\epsilon}|\le\|\zeta D_N/s\|_2=o(\sqrt\epsilon).
\]
Proposition 2 gives the rate \(d_1(P_N)=O((L\log L)^{-1/4})\). Using the separately checked [exact ratio slope](horizontal_ratio_slope_director_adjudication_round5.md) gives
\[
d_1(P_N)^2/\epsilon\ \longrightarrow\
\sum_{\gamma\ {\rm distinct}}\frac{m_\gamma\left(1-4^{-m_\gamma}\binom{2m_\gamma}{m_\gamma}\right)}
 {1/4+\gamma^2}.
\]
This conclusion is about the stated explicit polynomial sequence. It does not determine the optimal finite-degree distance, the shift edge \(A=C\), or priority.
