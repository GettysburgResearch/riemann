# Explicit Abel substitution in Gonek's Lemma 8

18 November 2026. Fiori–Jaskari's unconditional explicit prime number theorem gives a numerical bound for replacing \(d\psi(u)\) by \(du\) in the shifted von Mangoldt convolution used in Gonek's Lemma 8. This isolates one constant in that proof. [Pinned Fiori–Jaskari v2](../../sources/prime122_frontier_pending/2609.23222.pdf) · [Gonek source and Lemma 8 reconstruction](geometry88_gonek_whole_advocate.md)

Let \(\psi(u)=\sum_{n\le u}\Lambda(n)\) and \(r(u)=|\psi(u)-u|/u\) for \(u\ge1\). Theorem 1.1 on PDF p. 4 of the Fiori–Jaskari 50-page preprint arXiv:2609.23222v2 takes \(x\ge x_0\ge e^3\). Its table gives \(L(e^3)=0.2390\) and its exponential coefficient is \(D=0.1982767\ldots\). The introductory \(E_\psi\) is written with a sign. Theorem 5.2 and the proof in §5.1 on PDF pp. 44–45 give the asserted bound for the absolute error. Taking \(x_0=e^3\), this yields
\[
 r(u)\le0.2390\exp\left[-D
 \left(1+\frac{\log\log\log u}{15\log\log u}\right)
 (\log u)^{3/5}(\log\log u)^{-1/5}\right],\qquad u\ge e^3 .
\]
The conditional half-plane transfer in Theorems 1.4 and 5.3 is independent of this use.

For \(v=\log u\ge3\), the logarithmic correction is nonnegative. The elementary inequality \(\log v\le\sqrt v\) follows by checking the minimum of \(\sqrt v-\log v\) at \(v=4\). Consequently \(r(e^v)\le0.239\exp(-0.198\sqrt v)\). For \(1\le u\le e^3\), the inequalities \(\Lambda(n)\le\log n\) and \(\lfloor u\rfloor\le u\) give \(r(e^v)\le1+v\). These two estimates give the uniform bound \(r(u)\le4\) and
\[
 \int_1^\infty r(u)\frac{du}{u}
 \le\int_0^3(1+v)\,dv+0.239\int_0^\infty e^{-0.198\sqrt v}\,dv
 =\frac{15}{2}+\frac{0.478}{0.198^2}<20.
\]
The second integral uses \(v=z^2\) and \(\int_0^\infty ze^{-\lambda z}dz=\lambda^{-2}\).

For every real \(x>1\), integer \(m\ge0\) and real \(|\delta|\le1/2\), put \(L=\log x\) and \(f(u)=u^{i\delta-1}(\log(x/u))^m\), with the log-power convention 1 when \(m=0\). Abel summation for the right-continuous \(E(u)=\psi(u)-u\) gives
\[
 \sum_{n\le x}\frac{\Lambda(n)n^{i\delta}}n
           (\log(x/n))^m
 -\int_1^x u^{i\delta-1}(\log(x/u))^m\,du
 =E(x)f(x)-E(1)f(1)-\int_1^x E(u)f'(u)\,du .
\]
The right endpoint includes its possible prime-power jump. The upper boundary vanishes if \(m>0\), and is bounded by \(r(x)\le4\) if \(m=0\). The lower endpoint has \(E(1)=-1\), hence contributes at most \(L^m\). For \(m>0\),
\[
 |f'(u)|\le u^{-2}
 \left[\sqrt{1+\delta^2}\,(\log(x/u))^{m}
        +m(\log(x/u))^{m-1}\right].
\]
The \(m=0\) derivative has only the first term. Since \(\sqrt{1+\delta^2}\le\sqrt5/2\), the error in the Abel comparison is bounded by
\[
 \boxed{31 L^m+20m L^{m-1}},
\]
with the second term absent when \(m=0\). The coefficient 31 covers \(4+1+10\sqrt5<31\), including the \(m=0\) upper endpoint. For \(m>0\) the inequality is conservative.

In Gonek's Lemma 8 the exponent is \(m=\mu+\kappa+1\), so \(m>0\), and the beta-integral main term follows from the displayed integral by \(v=\log u/\log x\). The bound above makes the prime-to-integral substitution explicit uniformly on the required \(|\delta|\le1/2\). It does not allocate constants to the divisor-convolution error, contour analysis or final derivative moment. It therefore gives no full numerical derivative-tail bound or new enclosure for \(C_2\). [Gonek 1984 PDF](../../sources/classical63_lfunctions/gonek1984.pdf) · [Fiori–Jaskari, source pp. 4, 44–45](../../sources/prime122_frontier_pending/2609.23222.pdf)
