# A classical-norm endpoint via a locally shifted Perron contour

17 November 2026. **Proof candidate for independent review.** Assume RH and the Bui–Florea–Heycock Mertens bound \(|M(x)|\ll\sqrt{x}e^{C\phi(\log x)}\), where \(\phi(U)=\sqrt{U/\log U}\). The candidate obtains the same shift as in the \(q>1\) argument for every fixed \(A>C\):
\[
L=\log N,\qquad \epsilon=\frac{A}{\sqrt{L\log L}},
\qquad P_N(s)=\sum_{n\le N}\mu(n)n^{-s-\epsilon}.
\]
In the normalized classical norm \(d_1(P)^2=(2\pi)^{-1}\int_{\mathbb R}|1-\zeta(s)P(s)|^2dt/|s|^2\), \(s=1/2+it\), it gives \(d_1(P_N)=O((L\log L)^{-1/4})\). The route needs the reciprocal first moment and a pointwise estimate, in addition to the Mertens bound. Its source-input proofs and priority have not been independently audited.

## 1. Source inputs and the obstruction to using the envelope alone

Balazard–de Roton Proposition 2 gives the classical ratio error \(J_\epsilon=O(\epsilon)\). Their Proposition 13 gives the squared truncation error on \(|t|\ge N^{3/4}\) as \(O(N^{-1/9})\), uniformly for \(0<\epsilon\le1/2\). The proof uses the ratio bound and a Dirichlet polynomial mean value there. The low-height proof in Proposition 14 has a larger shift hypothesis and does not apply directly. The printed (16) drops the inverse on \(\zeta(s+\epsilon)\), but (17), its proof and the definition of \(I_{N,\epsilon}\) all use \(1/\zeta(s+\epsilon)\). The application here is to the latter integrand. [Balazard–de Roton, Propositions 2, 13 and 14](https://arxiv.org/pdf/0812.1689v1)

Bui–Florea–Heycock Theorem 1.2 (1.4) provides a normalized first reciprocal moment on \([Y,2Y]\) at shift \(b(Y)=B_0/(\log Y\log\log Y)\) with \(B_0\ge C_1(1/3)\). Its upper bound is \(\exp((\log Y)^{1/3})\). Their §8.1 already controls the corresponding untwisted Perron contour, including the high horizontal endpoints in (8.3). At this shift Theorem 1.1 has a lower threshold \((\log\log\log Y)^{-c}\) above \(b(Y)\log Y\), and its powers are strictly below the first reciprocal moment. Theorem 1.3 requires larger shifts for powers above one. No short-window first or second reciprocal moment is assumed below. [Bui–Florea–Heycock, Theorems 1.1–1.3 and §8.1](https://arxiv.org/pdf/2610.27591v1)

The needed pointwise input is published Bui–Florea Lemma 2.2 (2.8). For \(v\to\infty\), \(w=\log v\), \(0<a=o(1/\log w)\), it gives
\[
\log |\zeta(1/2+a+iv)|^{-1}
\le \frac{w}{2\log w}\log\frac1{1-e^{-2a\log w}}
   +O\!\left(\frac w{\log w}+\frac w{(\log w)^2}
                 \log\frac1{1-e^{-2a\log w}}\right).
\tag{1}
\]
For the small shifts below, the logarithm here is \(O(\log w)\). In this range (1) is bounded above by
\[
\frac w{2\log w}\{\log(1/a)-\log\log w+O(1)\}.
\tag{2}
\]
Use \(1-e^{-y}\asymp y\) for \(y=o(1)\). Both bounds are uniform over the indicated ranges, using the source's coefficient proof on pp. 8–9. Critical-line RH growth gives \(\log^+|\zeta(1/2+it)|=O(\log |t|/\log\log |t|)\). [Published Bui–Florea PDF, Lemma 2.2](https://pure.manchester.ac.uk/ws/portalfiles/portal/280630528/BuiFlorea_negative_moments.pdf) · [Balazard–de Roton, Proposition 14](https://arxiv.org/pdf/0812.1689v1#page=19)

An envelope-only Fourier estimate with a norm bound uniform over all admissible functions is false. For fixed \(L,\lambda,E>0\), take a nonnegative bump \(\psi\) supported in a small interval within \([L,L+1]\) with \(|\hat\psi|\) bounded below on \([-1,1]\). Use \(g_T(u)=e^{-E-\lambda}e^{iTu}\psi(u)\) with \(0\le\psi\le1\). Its envelope and unweighted \(L^2\) size are uniform in \(T\), but the classical mean square of zeta ensures that \(\int_{T-1}^{T+1}|\zeta(1/2+it)|^2dt\) is unbounded along a sequence of \(T\). Thus \(\|\zeta\widehat g_T\|_2\) is unbounded. The following contour treats the actual arithmetic transform, for which the additive modulation is unavailable.

## 2. A twisted bound with two separate contributions

For \(x\) sufficiently large put \(U=\log x\), and write \(M_x(it)=\sum_{n\le x}\mu(n)n^{-it}\). The proposed estimate, uniformly for \(|t|\le x^{3/4}\), is
\[
|\zeta(1/2+it)M_x(it)|
 \ll \sqrt{x}\big\{|\zeta(1/2+it)|e^{C_*\phi(U)}
          +(1+|t|)^{1/2}e^{D_*\sqrt U/\log U}\big\}.
\tag{3}
\]
The constants \(C_*,D_*\) may be unrelated to \(C\). The first term will be integrated starting at a large height, so it will not impose \(A>C_*\).

Choose a half-integer endpoint \(x'=\lfloor x\rfloor+1/2\), preserving the coefficients in the sum. Below the symbols \(x,U=\log x\) may be taken at this half-integer, with all original ranges unchanged up to absolute constants. Truncated Perron at height \(x'\) on \(\Re z=1+1/\log x'\) gives the integral of \((x')^{z-it}/[\zeta(z)(z-it)]\) initially at ordinates \(t\pm x'\). The error is \(O(\log x')\), by the usual Perron truncation bound for coefficients of absolute value at most one and distance at least \(1/2\) to integers. Changing the ordinates to \(\pm x'\) costs \(O(|t|\log x')\), since \(|z-it|\asymp x'\) on the added segments and \(1/|\zeta(z)|\le\zeta(1+1/\log x')\ll\log x'\) there. This is the same recentring as (12) of Balazard–de Roton. The product with \(|\zeta(1/2+it)|\) of the resulting error is absorbed by the second term of (3): for \(1\le |t|\le O(x^{3/4})\), \(|t|^{1/2}/\sqrt x\ll x^{-1/8}\) and RH gives \(|\zeta|\ll_\eta(1+|t|)^\eta\). Here and below RH puts all reciprocal poles strictly to the left of the deformed contour, and \(z=it\) is to its left as well.

Use the dyadic contour of Bui–Florea–Heycock §8.1 with central cutoff \(x_0=\exp(\phi(U))\), shift \(b(x_0)\) at \(|v|\le x_0\), and shifts \(b(Y)\) on dyadic panels \([Y,2Y]\) in positive and negative ordinates \(v=\Im z\). On regions with \(|v-t|\gg |v|\), the sum of absolute contour integrals is \(O(\sqrt x e^{C_*\phi(U)})\) by the same estimates as §8.1, since the new kernel is dominated by the old. Specifically, on a vertical panel the first reciprocal moment gives cost at most \(\sqrt x\exp(b(x_0)U+U^{1/3})\), times the ratio of the available kernel bound to \(1/Y\). The ratio is bounded on the region under discussion. There are \(O(U)\) panels. The original dyadic connectors use the pointwise bound \(Y^{1/2+\eta}\) and length at most 1. For the two top connectors \(|v|\asymp x\), the kernel remains \(O(1/x)\) and the original §8.1 estimates apply. The top connectors also have a direct bound. Under RH, the paired \(\xi\)-product shows that \(|\xi(1/2+\alpha+iv)|\) is nondecreasing for \(\alpha>0\) at fixed \(v\), and Stirling bounds the completion-factor ratio between two shifts \(\alpha_1\le\alpha_2\) in a fixed bounded range by \(O(|v|^{(\alpha_2-\alpha_1)/2})\). Let \(b\) be the last dyadic shift, so \(b\asymp 1/(U\log U)\). At \(|v|=x'\), (2) gives \(|\zeta(1/2+b+iv)|^{-1}\le e^{U/2+O(U/\log U)}\). For \(b\le\alpha\le1/4\), monotonicity and Stirling therefore give
\[
x^{\alpha-1/2}|\zeta(1/2+\alpha+iv)|^{-1}
\ll \exp(3\alpha U/2+O(U/\log U))\ll x^{3/8+o(1)}.
\]
At \(\alpha=1/4\), the third case of the published Bui–Florea Lemma 2.2 gives \(|\zeta(3/4+iv)|^{-1}=e^{o(U)}\) as an upper bound. For \(1/4\le\alpha\le1/2+1/U\), apply the same monotonicity ratio starting at \(1/4\); because \(x^{\alpha-1/2}\le e\), this gives \(x^{1/8+o(1)}\). These bounds yield the terminal-connector estimate.

The entire central panel can be bounded separately: the pointwise reciprocal estimate (8.1) gives \(e^{O(\phi(U))}\) there at the central shift. On a fixed compact set of low ordinates the same estimate follows from finite zero multiplicity and local factorization, with cost polynomial in the reciprocal shift. For \(\Re z\ge1/2\), \(\int_{-x_0}^{x_0}|z-it|^{-1}dv\ll 1+\log x_0\) uniformly in \(t\). These factors fit the first term. If \(|t|<4x_0\), the first finitely many adjacent panels, up to \(16x_0\), also admit the same absolute bound using (2) at their panel shifts and the same kernel integral. Outside them the kernel is again \(O(1/|v|)\). Symmetry permits \(t\ge0\) below.

For \(t\ge4x_0\), choose dyadic endpoints \(a_1,a_2\) with \(t/4<a_1\le t/2\), \(2t\le a_2<4t\), and replace the positive-ordinate panels from \(a_1\) to \(a_2\) by a single vertical at shift
\[
a=\min(U^{-1/2},\, w/(U\log w)),\qquad w=\log t.
\tag{4}
\]
The endpoints exist on the baseline contour, since \(t/4\ge x_0\) and \(4t<x'\) for large \(x'\). The negative panels need no replacement. On \(a_1\le v\le a_2\), \(\log v=w+O(1)\). Here \(w\ge\phi(U)+O(1)\), \(w\le U\), and thus \(\log w\asymp\log U\). Also \(a\log w=o(1)\) and \(\log(1/a)=O(\log w)\), since \(U^{-1/2}\) and \(w/(U\log w)\) lie between inverse powers of \(U\). Therefore (2) applies uniformly at (4), also with \(w\) substituted for \(\log v\) by absorbing the \(O(1)\) change.

After including the critical-line \(\zeta\) factor and dividing the right-side exponent by the target \(t^{1/2}\), the local exponent is at most
\[
aU+\frac w{2\log w}
       \{\log(1/a)-\log\log w-\log w+O(1)\}.
\tag{5}
\]
If \(a=w/(U\log w)\), this becomes \(\frac{w}{2\log w}(\log(U/w^2)+O(1))\). The positive part is \(O(\sqrt U/\log U)\) because \(r\log(K/r^2)\) is bounded above on \(r>0\), with \(r=w/\sqrt U\) and fixed \(K\). If \(a=U^{-1/2}\), then \(w\ge\sqrt U\log w\). The bracket in (5) is at most \(-2\log\log w+O(1)\), which absorbs \(aU=\sqrt U\) for sufficiently large \(U\). Finally \(\int_{a_1}^{a_2}|z-it|^{-1}dv\ll 1+w\), a factor absorbed by \(e^{D_*\sqrt U/\log U}\). This proves the second term of (3) for the new vertical.

For the two new horizontal connectors, the shifts run between \(a\) and an old \(b(Y)\) with \(Y\asymp t\). Every connecting shift \(\beta\) then satisfies \(\beta\log w=o(1)\) and \(\log(1/\beta)\le\log w+O(\log\log U)\). For the last inequality at shift \(a=w/(U\log w)\), use \(w\ge\phi(U)\) to obtain \(U/w^2\le \log U\); at the cap and at \(b(Y)\) the inequality follows directly. Thus (2) bounds \(|\zeta(1/2+\beta+iv)|^{-1}\) by \(e^{(2/3)w}\) for large \(U\). Also \(\beta U\le C'\phi(U)+w/\log w\) since \(b(Y)U\ll\phi(U)\) and \(aU\le w/\log w\). Their kernels are \(O(1/t)\) because their ordinates are separated from \(t\) by \(\gg t\). Their length is bounded, so the two absolute contributions are \(O(\sqrt x e^{C_*\phi(U)})\) and fit the first term. This completes the bound (3).

## 3. Transfer to the full classical norm

Write \(D_N(s)=1/\zeta(s+\epsilon)-P_N(s)\). For low heights, use the untwisted Abel representation from the \(q>1\) argument,
\[
D_N(s)=-M(N)N^{-s-\epsilon}+(s+\epsilon)\widehat g(t),\quad
g(u)={\bf1}_{u\ge L}e^{-(1/2+\epsilon)u}M(e^u).
\]
Its Plancherel estimate is \(\|\widehat g\|_2\ll \epsilon^{-1/2}e^{-(A-C)\phi(L)}\). Fix a large \(B>0\) independent of \(N\), and set \(T_0=\exp(B\phi(L))\). RH gives \(\sup_{|t|\le T_0}|\zeta(s)|=e^{o(\phi(L))}\) for any such fixed \(B\). Hence \(\|\zeta D_N/s\|_2\) restricted to this range is \(e^{-c\phi(L)}\) for some \(c>0\); the endpoint term is separately bounded with the full norm \(\|\zeta/s\|_2<\infty\).

On \(T_0\le |t|\le N^{3/4}\), apply the twisted Abel identity (Balazard–de Roton (15))
\[
D_N(s)=-N^{-1/2-\epsilon}M_N(it)
 +(1/2+\epsilon)\int_N^\infty x^{-3/2-\epsilon}M_x(it)\,dx .
\]
Bound both terms using (3), which is eligible throughout \(x\ge N\). For its first term, set \(r=U/L\ge1\) and note \(\phi(U)\le\phi(L)\sqrt r\). Completing the square gives
\[
C_*\phi(U)-\epsilon U\le \frac{C_*^2}{2A}\phi(L)-\tfrac12\epsilon U .
\]
Thus the first contribution to \(|\zeta D_N|\) is bounded by \(e^{B_1\phi(L)}|\zeta(s)|\) with some finite \(B_1\) depending on \(A,C_*\). The classical convexity bound yields \(\|\zeta/s\|_{2,\,|t|\ge T_0}\ll T_0^{-1/8}\), for example. Choose \(B>8(B_1+1)\). The cost is exponentially small in \(\phi(L)\), independently of any comparison between \(C_*\) and \(A\). This choice is compatible with the low-height bound.

For the second term in (3), \(D_*\sqrt U/\log U\le \eta\phi(U)\) for all \(U\ge L\) and sufficiently large \(N\), with \(\eta=A/4\). Concavity and \(\epsilon-\eta\phi'(L)\asymp\epsilon\) bound the resulting integral and endpoint by \(O((1+\epsilon^{-1})e^{-(A-\eta)\phi(L)}(1+|t|)^{1/2})\). Its \(L^2(dt/(2\pi |s|^2))\) norm on this range incurs only \(O(\sqrt L)\), since \(\int_1^{N^{3/4}}dt/t=O(L)\). This is also exponentially small. Finally Proposition 13 covers the two tails \(|t|\ge N^{3/4}\). The combined truncation is \(o(\sqrt\epsilon)\). Minkowski and \(J_\epsilon=O(\epsilon)\) prove the candidate \(q=1\) rate. The off-line-zero Hardy witness remains the converse.

## Review targets

The main review targets are the uniformity of (1) with two independent height scales, the recentred Perron truncation and the absolute contour bounds. The two terminal connectors have both the source comparison to §8.1 and the direct product-monotonicity check above. The interior contour argument uses the reciprocal **first** moment only away from \(v\approx t\); the replacement near \(t\) is pointwise. It therefore avoids substituting a small-window or second reciprocal moment outside the source regime. The argument does not establish priority or the optimal classical distance.
