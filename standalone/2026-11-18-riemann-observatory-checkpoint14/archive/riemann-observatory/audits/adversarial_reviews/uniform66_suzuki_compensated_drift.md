# Suzuki §5.1 compensated drift in current arXiv v2

18 November 2026. The compensated representation in the rendered arXiv:2209.12832v2, p. 6 §5.1, has a sign discrepancy in its displayed exterior drift coefficient when read with the same paper's (1.1), (2.5)–(2.6), signed atoms and truncation. An exact example in the extended Selberg class satisfies the stated GRH premise and has nonzero discrepancy. The required correction changes only a linear imaginary term, so the screw kernel and the real-part sign test are unaffected. The journal formula was inaccessible beyond the first-page preview. No flags or canonical changes are made. [Current arXiv source](https://arxiv.org/pdf/2209.12832v2)

## Sign and finite-measure calculation

Write \(E(z)=\xi_F(1/2-iz)\), and group distinct zeros \(\gamma\) with multiplicities \(m_\gamma\). The p. 3 product in §2.2 contains \(e^{A_F+B_F z}\), the central factor \(z^{m_0}\), and the genus-one noncentral factors. Equation (2.5) follows since \((\xi'_F/\xi_F)(1/2-iz)=iE'(z)/E(z)\), and (2.6) reads
\[
 B_F=\lim_{z\to0}\left(E'(z)/E(z)-m_0/z\right)\in\mathbb R.
\]
The reality follows from the functional equation, after a constant phase makes \(E\) real entire. Equation (1.1) then defines
\[
 g_F(t)=-iB_Ft-\tfrac12m_0t^2+
      \sum_{\gamma\ne0}\frac{m_\gamma}{\gamma^2}(e^{-i\gamma t}-1).
\]
Thus the uncompensated shift in the \(e^{itx}\) convention is \(b=-B_F\). Equation (3.2) independently fixes this sign, since the one-sided transform of \(t\) is \(-1/z^2\), so \(-iB_Ft\) gives \(iB_F/z^2\).

Assume GRH as in the printed §5.1. Set
\[
 \nu=\sum_{\gamma\ne0}\frac{m_\gamma}{\gamma^2}\delta_{-\gamma},
 \qquad h(x)=\frac{x}{1+x^2}.
\]
The Lévy measure is finite by inverse-square summability and discreteness at zero. For an exterior \(+ict\) and compensated integral \(\int(e^{itx}-1-it h(x))\,d\nu(x)\), the location change is
\[
 c=b+\int h\,d\nu
   =-B_F-\sum_{\gamma\ne0}\frac{m_\gamma}{\gamma(1+\gamma^2)}.
\]
Indeed the integrand at atom \(x=-\gamma\) adds \(+it\,m_\gamma/[\gamma(1+\gamma^2)]\) to the uncompensated jump term. The absolutely convergent sum of these corrections must be subtracted from the exterior drift. The exact same \(B_F\), the negative sign in the atom location, and the minus sign in the compensating integrand are printed on the relevant pages. The displayed §5.1 value \(C^{\rm print}_F=B_F+\sum m_\gamma/[\gamma(1+\gamma^2)]\) is the negative of \(c\). Keeping the printed formula for \(C^{\rm print}_F\) instead requires exterior \(-i C^{\rm print}_F t\). A change of overall Fourier convention would also change the exponential and the locations, which are fixed in the display, so it cannot reconcile just the displayed drift.

Precisely, let \(\tau_F=\sum_\gamma m_\gamma\delta_{-\gamma}\), including the central mass. Its finite reweighting and canonical representation are
\[
 K_F(dx)=\frac{\tau_F(dx)}{1+x^2}
     =m_0\delta_0(dx)+\frac{x^2}{1+x^2}\nu(dx),
 \qquad
 g_F(t)=ict+\int_{\mathbb R}
      \frac{1+x^2}{x^2}\bigl(e^{itx}-1-it h(x)\bigr)\,K_F(dx).
\]
The kernel extends continuously at zero with value \(-t^2/2\). Taylor's formula gives this value and boundedness near zero. At infinity, \((1+x^2)/x^2\) is bounded and \(h(x)=O(1/x)\), giving boundedness for fixed \(t\). Hence the integral is a finite-measure integral in the ordinary sense and includes precisely the central Gaussian variance. This is the same measure as the source gives, merely reweighted. It does not offer another drift convention once \(h\) is fixed.

A useful independent check is evaluation at \(z=i\) in the Hadamard derivative:
\[
 \Re\frac{E'(i)}{E(i)}
  = B_F+\sum_{\gamma\ne0} \frac{m_\gamma}{\gamma(1+\gamma^2)}
  = C_F^{\rm print}.
\]
For real \(\gamma\), the relevant real part is \(-\gamma/(1+\gamma^2)+1/\gamma\), and \(m_0/i\) has zero real part. Therefore the representation of (1.1) requires \(c=-\Re(E'/E)(i)\).

## Exact witness inside the stated class

Take the Dirichlet polynomial \(F(s)=1+2i\,4^{-s}\) and choose \(\xi_F(s)=2^s F(s)=2^s+2i\,2^{-s}\), with \(m_F=0\), no Gamma factors, \(Q=2\), and root number \(i\). This is an entire function of finite order with an absolutely convergent Dirichlet series. Direct substitution gives
\[
 i\,\overline{\xi_F(1-\bar s)}
 =i(2^{1-s}-2i\,2^{s-1})=\xi_F(s).
\]
Thus it satisfies the extended Selberg axioms (S1)–(S3) as printed in §2.1. If \(F(s)=0\), taking moduli gives \(4^{-\Re s}=1/2\), hence \(\Re s=1/2\). The entire exponential factor \(2^s\) does not alter the zeros. Here \(F(1/2)=1+i\) and \(\xi_F(1/2)=\sqrt2(1+i)\), so this example needs no central regularization. It satisfies the GRH premise of §5.1 outright and claims only membership in the extended class used there.

For \(u=\log2\), one has
\[
 E(z)=\sqrt2\,(e^{-iuz}+i e^{iuz}),\qquad
 \frac{E'(i)}{E(i)}=u\,\frac{-2i-1/2}{2+i/2}.
\]
Its real part is \(-8\log2/17\). Thus the current arXiv coefficient gives \(C_F^{\rm print}=-8\log2/17\), while the exterior \(+iC_Ft\) representation requires \(c=+8\log2/17\). The two exponents differ by \(-16it\log2/17\) when taking printed minus required, for every real \(t\). This proves the discrepancy on an actual member of the stated class without any conjectural premise or numerical root information.

For comparison, the earlier one-zero finite-product witness \(E(z)=z-\delta\) has \(B_F=-1/\delta\), with required \(c=\delta/(1+\delta^2)\) and printed coefficient its negative. It checks the algebra, but the Dirichlet polynomial above also checks all stated functional hypotheses. A real self-dual even completion can have zero drift and therefore conceal the sign.

The difference is a change in the deterministic translation of the Lévy law, not in its Lévy measure or Gaussian part. A term \(i\beta t\) cancels identically in \(g(t-u)-g(t)-g(-u)+g(0)\) and has zero real part. Thus this calculation does not refute the screw-kernel or eventual real-part assertions. It isolates the §5.1 equality for the specific \(g_F\) defined by (1.1).

## Source verification

I checked the entire relevant sequence in the PDF, including §1 (1.1), the class definitions in §2.1, the Hadamard product and (2.5)–(2.6), the transform (3.2), and the complete rendered §5.1 on p. 6. The unsuffixed arXiv PDF retrieved again on 18 November 2026 hashes to c706479044babf3618fff6910ce28238faf1bb321c7ffee9f73f1ee765f34232, identical to v2. The official arXiv history lists only v1, 14 September 2022, and v2, 25 March 2025. The earlier v1 §5.1 p. 5 contains the same sign pattern, with multiplicities additionally omitted from that correction sum. The earlier version comparison checked the actual rendered pages. [arXiv history](https://arxiv.org/abs/2209.12832) · [v1](https://arxiv.org/pdf/2209.12832v1) · [Version ledger](uniform64_vertical_diffusion_priority.md)

The publisher DOI identifies *Int. J. Number Theory* 21(8), 1815–1823. Publisher full-text routes returned 403 and the World Scientific preview shows only p. 1815. The author's publication list has no erratum link on this title, and the current Crossref DOI record showed no update relation. The author's separately linked erratum is attached to another paper. These checks establish the current public arXiv wording, with no assertion that the same display persists in the unseen journal text. The algebra above is independently derived. No canonical action was taken. [Publisher DOI](https://doi.org/10.1142/S1793042125500885) · [Author bibliography](https://sites.google.com/view/msuzuki/home/articles)
