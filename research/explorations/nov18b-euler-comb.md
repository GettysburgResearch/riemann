# Weil coercivity on logarithms of integers

**Proposed unconditional theorem.** Take an integer \(N\ge2\), \(0<\omega\le\omega_0\) for a sufficiently small absolute constant \(\omega_0\), and \(w=\omega/N\). Every smooth \(g\) supported on
\[
 E_N=\bigcup_{n=1}^N [\log n,\log n+w]
\]
satisfies
\[
 W(g)\ge(\log(1/\omega)-C)\|g\|_2^2+(1-C\omega)\mathcal D_N(g).
 \tag{1}
\]
Here \(W\) is the classical Riemann-zeta Weil quadratic form in the [prime translation normalization](nov18b-weil-packets.md) and \(C\) is an absolute constant. The support diameter grows like \(\log N\). The functions on its \(N\) intervals may be chosen independently, with arbitrary complex phases, common modulation or variation within each interval. The same result holds after any common translation. In particular this is a strict lower bound at every \(N\) when \(\omega_0\) is sufficiently small. The full real-logarithm line, including the gaps between these intervals, is the remaining domain.

Write \(v_n(y)=g(\log n+y)\), \(0\le y\le w\), considered as vectors in \(L^2[0,w]\), and let \(a_n=\|v_n\|\). The term measuring differences under prime-power dilations is
\[
 \mathcal D_N(g)=\sum_{nr\le N}\Lambda(r)\left\|v_{nr}-\frac{v_n}{\sqrt r}\right\|^2 .
\]
Only \(r=p^k\ge2\) contribute. All scalars and norms below use Lebesgue measure in the log coordinate. Define \(\widehat g(t)=\int g(x)e^{itx}\,dx\). The explicit formula gives \(W=G-P+Z\), where
\[
 G=\int_{\mathbb R}\big[\Re\psi(1/4+it/2)-\log\pi\big]|\widehat g(t)|^2\,\frac{dt}{2\pi},\quad
 P=2\Re\sum_{r\ge2}\frac{\Lambda(r)}{\sqrt r}\int g(x+\log r)\overline{g(x)}\,dx,
\]
and \(Z=2\Re[\widehat g(i/2)\overline{\widehat g(-i/2)}]\). All three terms are retained.

## Exact arithmetic on the comb

Two intervals can meet under a translation by \(\log r\) only when their labels obey \(m=nr\). Indeed \(|\log(m/(nr))|\le w\) implies \(|m-nr|\le N(e^w-1)<1\) for \(\omega\) sufficiently small. The prime term therefore has the exact identity
\[
 P=\sum_{n\le N}\left(\log n+\sum_{r\le N/n}\frac{\Lambda(r)}r\right)a_n^2-\mathcal D_N(g).
 \tag{2}
\]
It follows by expanding the squared norms and using \(\sum_{r\mid m}\Lambda(r)=\log m\). The elementary estimate \(\sum_{r\le x}\Lambda(r)/r=\log x+O(1)\), uniform for \(x\ge1\), comes from \(\sum_{r\le x}\Lambda(r)\lfloor x/r\rfloor=\log(\lfloor x\rfloor!)\), Stirling and Chebyshev's \(\sum_{r\le x}\Lambda(r)\ll x\). Thus the diagonal in (2) is \(\log N+O(1)\). This leading term is attained to within \(O(1)\) by the vector \(v_n=v_1/\sqrt n\).

The same arithmetic controls concentration near the largest labels:
\[
 \sum_{m\le N}\frac mN\log(2m)a_m^2\ll \mathcal D_N(g)+\|g\|_2^2 . \tag{3}
\]
For the part \(\log m\), insert \(\sum_{r\mid m}\Lambda(r)\). Use \(a_{nr}^2\le2\|v_{nr}-v_n/\sqrt r\|^2+2a_n^2/r\). Since \(nr/N\le1\), the first part costs at most \(2\mathcal D_N\). The second is at most \(2\sum_n a_n^2(n/N)\sum_{r\le N/n}\Lambda(r)\ll\sum_n a_n^2\). The latter equals \(\|g\|_2^2\) because the cells are disjoint.

## Archimedean interactions and the two poles

The elementary integral formula for the digamma function gives
\[
 G=(\psi(1/4)-\log\pi)\|g\|_2^2+
 \int_0^\infty K(u)\big(\|g\|_2^2-\Re\langle g(\cdot+u),g\rangle\big)\,du,
 \qquad K(u)=\frac{2e^{-u/2}}{1-e^{-2u}}.
\]
For each separate cell the integrand is nonnegative, and its correlation vanishes for \(u>w\). Since \(K(u)=1/u+O(1)\) on \((0,1]\), the sum of the individual gamma forms is at least \((\log(1/w)-C)\sum_n a_n^2\).

For two distinct labels \(m>n\) the absolute cross contribution is at most \(Cw a_m a_n K(\log(m/n))\), by integration on the two cells and Cauchy–Schwarz on each. The kernel is comparable throughout the shifted interval of width \(2w\) about \(\log(m/n)\), because this logarithm is at least \(1/N\). For comparable labels \(m/2\le n\le2m\), its value is at most \(C n/|n-m|\), with row sum \(O(n\log(2n))\). For separated labels it is \(O(\sqrt{\min(n,m)/\max(n,m)})\) and has row sum \(O(N)\). Using \(2a_ma_n\le a_m^2+a_n^2\), (3) therefore bounds all gamma cross terms by \(C\omega(\mathcal D_N+\|g\|_2^2)\).

The pole term has absolute value at most
\[
 Cw\left(\sum_n a_n/\sqrt n\right)\left(\sum_n\sqrt n\,a_n\right).
\]
The first factor in parentheses is \(O(\sqrt{\log(2N)}\|g\|_2)\). For the second one apply Cauchy–Schwarz with the weights \((n/N)\log(2n)\) in (3). The complementary sum is \(N\sum_{n\le N}1/\log(2n)\ll N^2/\log(2N)\), by splitting at \(\sqrt N\). Hence \(|Z|\ll\omega(\mathcal D_N+\|g\|_2^2)\). Combining these bounds with (2) proves (1).

The proof uses the exact arithmetic transversality of the prime translations on these cells. On cells of width comparable to \(1/n\) near small labels, the possible offsets \(m-nr\ne0\) must also be controlled to use the same argument.
