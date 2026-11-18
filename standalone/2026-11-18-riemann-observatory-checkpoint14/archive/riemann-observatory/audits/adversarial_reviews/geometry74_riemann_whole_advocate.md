# Riemann's 1859 prime-counting memoir | Whole-work advocate review

Reviewer /root/geometry_corpus_64. Canonical work PAPER-S001. Scope is the complete printed memoir, compared with the complete Wilkins English translation and German transcription. The review reconstructs the analytic steps and identifies where later theorems are used. It does not adjudicate the independent review or change corpus status.

## Source and coverage

Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, *Monatsberichte der Königlichen Preussischen Akademie der Wissenschaften zu Berlin*, pp. 671–680. The original heading says session 3 November 1859, and p. 671 names Kummer as presenter and dates the cover letter to Encke at Göttingen on 19 October. The journal volume bears the later compilation imprint. Use the Academy session year for the paper and printed pages for citations. The first print is the controlling text in this review. Wilkins's German and English texts are secondary editions aligned to the 1892 collected printing. The CMI manuscript witness is a separate manifestation and is cited only for the established normalization comparison.

| First print | Wilkins numbered page | Reading and checked result |
|---|---|---|
| 671 | 1 | Presentation, thanks, context of Gauss and Dirichlet, Euler product and Dirichlet series. |
| 672 | 1–2 | \(\Pi\) integral, cut, orientation, continuation, trivial zeros, and start of deformation. |
| 673 | 2–3 | Residues and completed functional equation, Jacobi citation, theta split and symmetric representation. |
| 674 | 3–4 | Centered entire function, both cosine integrals, strip, root count, and conjecture. |
| 675 | 4–5 | Paired product, normalization at the center, half weights, Euler logarithm, Mellin transform. |
| 676 | 5–6 | Fourier argument and jump convention, substitution of logarithms and integration by parts. |
| 677 | 6–7 | Gamma expansion, constant transform, one-factor computation via a parameter derivative. |
| 678 | 7–8 | Branch choice in the transform and explicit formula including the printed constant. |
| 679 | 8–9 | Limiting order and rearrangement assertion, Möbius inverse, finite density and smooth terms, start of Gauss table discussion. |
| 680 | 9 | Numerical comparison and interpretation of density oscillations, suggestion for future tables, closing claim about \(f\). |

Local witness hashes are attached in [the receipt](../../sources/geometry74/riemann1859_witnesses.sha256). The OCR was used as a reading aid with the full German transcription. The first-print equations at pp. 673, 675 and 678 settle the edition or normalization points below. Whole-manuscript transcription and the historical count up to three million are outside this reading.

## Euler, Hankel, and the functional equation | pp. 671–673

For \(\Re s>1\), both the Dirichlet series and the Euler product are absolutely convergent. The log is the analytic branch given by \(\sum_{p,m}p^{-ms}/m\), real for \(s>1\) real, so the product is nonzero there. Integration of \(e^{-nx}x^{s-1}\), with absolute interchange for \(\Re s>1\), gives \(\Gamma(s)\zeta(s)=\int_0^\infty x^{s-1}/(e^x-1)\,dx\), since Riemann's \(\Pi(s-1)=\Gamma(s)\). The paper's ordinary convergence statement can be read in this natural domain of joint absolute convergence. No finer prime-product boundary claim is needed.

Let \(H(s)\) denote his contour integral with \(\log(-x)\) real for negative real \(x\), cut on the positive ray, and positive orientation around the origin and cut, with the small circular part inside \(|x|<2\pi\). With the small part fixed, \(H(s)\) is entire by exponential decay at the two ends and locally uniform integration. Shrinking the small part for \(\Re s>1\) gives the stated jump \(2\sin(\pi s)\Gamma(s)\zeta(s)=iH(s)\). Euler reflection yields \(\zeta(s)=i\Gamma(1-s)H(s)/(2\pi)\). Apparent poles at positive integers above 1 are removable by the established identity there. Subtracting \(x^{-1}\) near zero in the Mellin integral gives the simple pole at 1 and residue 1. The sine or reflection identity then explains continuation without spurious poles at other integers.

For \(\sigma=\Re s<0\), take outer rectangles with vertical sides \(\Re x=\pm(2M+1)\pi\) and horizontal sides \(\Im x=\pm(2M+1)\pi\), split where they meet the banks of the cut. On the horizontal segments \(|e^x-1|=1+e^{\Re x}\), and on the vertical segments the inverse denominator is bounded for large \(M\). The branch factor is \(O_s(R^{\sigma-1})\) and total outer length \(O(R)\). This supplies the vanishing estimate implicit in p. 672. The simple poles at \(\pm2\pi in\) contribute with the negative orientation displayed in the memoir. The sum is absolutely convergent, since \(\sum n^{\sigma-1}<\infty\). This gives
\[
iH(s)=(2\pi)^s\zeta(1-s)\bigl((-i)^{s-1}+i^{s-1}\bigr).
\]
With the stated logarithm determinations, Euler's gamma identities produce \(\Lambda(s)=\Lambda(1-s)\), where \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\). Its continuation also shows that the negative even zeros of \(\zeta\) are simple, since \(\Lambda(1+2n)\ne0\) and the gamma poles are simple.

## Theta, entire completion, and the zeros | pp. 673–675

Put \(\psi(x)=\sum_{n\ge1}e^{-\pi n^2x}\). Riemann cites Jacobi's *Fundamenta Nova*, p. 184, for the transformation of \(1+2\psi(x)\). The transformation can independently be supplied by Poisson summation for the Gaussian. Absolute integration on \(\Re s>1\), splitting at 1, and changing \(x\mapsto1/x\) on the transformed small part give
\[
\Lambda(s)=\frac1{s(s-1)}
+\int_1^\infty\psi(x)\bigl(x^{s/2-1}+x^{-(s+1)/2}\bigr)\,dx .
\]
In the *intermediate* split, \(\psi(1/x)x^{(s-3)/2}\) is integrated from 0 to 1, as appears on original p. 673 and collected p. 147. Both Wilkins texts instead print 1 to infinity for this term, before giving the correct final display. For instance the misprinted term diverges at \(s=2\). Wilkins English p. 5 likewise typesets \(ds\) in the elementary prime integrals in \(x\), where original p. 675 has \(dx\). The English closing paragraph's “in the first hundred thousand” should be “from the first hundred thousand onward” for German “schon vom ersten Hunderttausend an.” These readings concern the particular witness texts.

Use \(\xi_M(s)=\tfrac12s(s-1)\Lambda(s)\) and \(\Xi(t)=\xi_M(\tfrac12+it)\) for the memoir's \(\xi(t)\). The integral above yields the first cosine formula, evenness, and entire analyticity with an everywhere convergent even power series. Write \(G(y)=e^{y/4}\psi(e^y)\), \(y=\log x\). Jacobi's relation gives \(\psi'(1)=-(1+2\psi(1))/8\), so \(G'(0)=-1/8\). Double integration by parts gives
\[
\Xi(t)=\frac12-(t^2+\tfrac14)\int_0^\infty G(y)\cos(ty/2)\,dy
=\int_0^\infty(4G''(y)-G(y)/4)\cos(ty/2)\,dy.
\]
The last measure in \(x\) is \(4(x^{3/2}\psi'(x))'x^{-1/4}dx\), exactly the second cosine formula. Exponential decay in \(x\) justifies the integrations for all finite complex \(t\). Its density is positive for \(x\ge1\) because each differentiated term has the positive factor \(\pi n^2x-\tfrac32\). In particular \(\Xi(iu)>0\) for real \(u\), \(0<\Xi(0)<1/2\), and \(\Xi(i/2)=\xi_M(0)=1/2\).

The Euler product and evenness confine zeros to \(0\le\Re s\le1\), hence \(|\Im t|\le1/2\). The displayed endpoints on p. 674 are imaginary-axis coordinates. Excluding the strip boundary requires a separate input, established in the 1896 PNT proofs of Hadamard and de la Vallée Poussin. The argument principle counts multiplicity with a positively oriented contour avoiding boundary zeros. Riemann gives the first two asymptotic terms and a relative error phrased as a fraction of order \(1/T\). A modern precise version, at heights \(T\) other than zero ordinates, is
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}
+\frac78+S(T)+O(T^{-1}),
\quad S(T)=\pi^{-1}\arg\zeta(\tfrac12+iT),
\]
using continuous argument along \(2\to2+iT\to\tfrac12+iT\). The bounded-real-strip Stirling expansion produces the gamma terms, and the standard separate \(S(T)=O(\log T)\) bound (e.g. Jensen's formula applied to control horizontal argument variation) gives the usual additive \(O(\log T)\). The relative order agrees with the scale of the memoir. Exact boundary heights require a specified midpoint or one-sided convention. The memoir does not establish this argument bound on the upper edge or supply the rigorous first proof of the count. Von Mangoldt's 1895 paper states a rigorous count with the weaker additive \(O(\log^2 T)\) bound in its opening pages. His 1905 *Zur Verteilung der Nullstellen der Riemannschen Funktion \(\xi(t)\)*, *Mathematische Annalen* 60, 1–19, gives the sharper logarithmic scale.

The statement that one finds approximately as many real roots, and the statement that all are very likely real, are retrospective observation and explicitly open conjecture, respectively. P. 674 says why the search for a proof was set aside. Neither the product nor the explicit formula requires RH.

For the p. 675 product, the theta representation gives \(\log\max_{|t|\le R}|\Xi(t)|=O(R\log(R+2))\) by comparison of the integral to a gamma integral, hence entire order at most 1. The count gives \(\sum_{\alpha}|\alpha|^{-2}<\infty\). Hadamard factorization applied with multiplicities, followed by pairing \(\alpha,-\alpha\), cancels the genus-one exponentials. Evenness forces the residual linear exponent to vanish, and evaluation at \(t=0\) determines the constant. This yields
\[
\Xi(t)=\Xi(0)\prod_{\Re\alpha>0}(1-t^2/\alpha^2).
\]
Convergence is normal on compact sets. Logs require a continuous branch off the zeros. The first-print pp. 675 and 678 together settle the one-per-\(\pm\)-pair convention, including nonreal roots, and the symmetry \(\rho\leftrightarrow1-\rho\) must be kept distinct from conjugation. Riemann's indicated comparison of logarithmic growth calls for global control around the zeros. The modern proof uses the order-one factorization theorem and thereby supplies this step independently.

## Inversion and explicit formula | pp. 675–679

Let \(F(x)\) count primes strictly below \(x\) plus \(1/2\) when \(x\) is prime. Write \(J_0(x)=\sum_{m\ge1}F(x^{1/m})/m\) for his \(f(x)\). For fixed \(x>1\) the sum terminates once \(x^{1/m}<2\). Its jump at \(p^m\) is \(1/m\), and the value includes \(1/(2m)\). For \(\Re s>1\), termwise elementary integration of the absolutely convergent Euler log gives \(\log\zeta(s)/s=\int_1^\infty J_0(x)x^{-s-1}\,dx\). In \(u=\log x\), the function \(e^{-cu}J_0(e^u)\), extended by zero below zero, is integrable and of bounded variation for \(c>1\). Integrability follows from the Euler log or \(J_0(x)\ll x\), and the variation of its jump and continuous parts is finite by the same estimates. Fourier inversion in symmetric truncation therefore gives the Perron integral and exactly the midpoint values specified by Riemann. This supplies the interior and discontinuity hypotheses implicit in the general Fourier discussion.

At \(\Re s=c>1\) the integrated-by-parts boundary term is \(O_x(T^{-1})\) as \(|\Im s|=T\to\infty\), since the Euler log is uniformly bounded on this vertical line. The resulting integrand is \(-x^s(\log\zeta(s)/s)'/\log x\). The \(\tfrac{s}{2}\log\pi\) term drops after the derivative of the quotient. Euler's gamma limit similarly yields locally uniformly convergent differentiated terms after division by \(s\). The memoir explicitly notes failure of termwise convergence before integration by parts, and subsequent local convergence alone still does not justify exchange of the infinite zero product and the unbounded contour.

For a single factor the p. 677 differentiation satisfies
\[
\partial_\beta[\log(1-s/\beta)/s]=1/[\beta(\beta-s)].
\]
Taking the opposite sign as in the memoir, the vertical contour integral of the derivative is \(x^\beta/\beta\) for \(x>1\), \(\Re\beta<c\), by the elementary Perron or residue computation. Thus the factor transform is a primitive \(\operatorname{Ei}(\beta\log x)\) with the additive constant fixed by branch and limiting conditions. For real \(\beta<0\) normalize by decay to the left. For the pole \(\beta=1\), use \(\operatorname{Li}(x)=\operatorname{PV}\int_0^x du/\log u\), the mean of the two continuations. This matches the real branch of \(\log(s-1)\) for real \(s>1\) in the starting decomposition. For nonreal \(\beta\), take the horizontal primitive \(\int_{-\infty+i\Im\beta}^{\beta} e^{w\log x}\,dw/w\), equivalent to principal \(\operatorname{Ei}(\beta\log x)-i\pi\operatorname{sgn}\Im\beta\). The contours across \(u=1\) in the \(\operatorname{Li}\) representation differ by \(2\pi i\), and the offsets cancel under symmetric summation of conjugate zeros. For fixed \(x>1\) and bounded real \(\beta\), the horizontal primitive is \(O_x(1/|\Im\beta|)\). The trivial factors contribute the positive tail \(\int_x^\infty du/[u(u^2-1)\log u]\) by summing the absolutely convergent contributions \(-\operatorname{Ei}(-2n\log x)\).

There is a real constant from passing from the centered product to linear \(s\)-factors:
\[
1+(s-\tfrac12)^2/\alpha^2
=(1+1/(4\alpha^2))(1-s/\rho)(1-s/(1-\rho)),
\qquad \rho=\tfrac12+i\alpha .
\]
The sum \(D=\sum_{\Re\alpha>0}\log(1+1/(4\alpha^2))\), with compatible branches, equals \(\log(1/2)-\log\Xi(0)\) by the product at \(t=i/2\). One can fix the branches by continuing the centered factors from \(s=1/2\) to \(s=0\), pairing conjugates to obtain the real logarithm. A constant in \(\log\zeta\) contributes itself via \((2\pi i\log x)^{-1}\int_{(c)}Cx^s ds/s^2=C\). Thus the final constant is \(-\log2\), replacing printed \(+\log\Xi(0)\) on pp. 678 and 680. The equality between the Li sum times \(\log x\) and the centered-log contour displayed at the bottom of p. 678 also has the associated offset: the centered constants contribute \(-D\log x\) to that contour, whose sign is opposite the integrated-by-parts formula for \(J_0\). Genocchi already made the normalization correction in 1860, original pp. 57–58, eq. (11). The 1892 editorial note on p. 155 gives the corrected value as well. The manuscript witness also carries the old value, so this review does not endorse the later editorial conjecture that the mismatch was a typographical accident.

The remaining global limit is a substantive input. The paper says a more detailed discussion would show agreement between the integrated centered log and the sum ordered by magnitude, and remarks on rearrangements. The rigorous subsequent input is von Mangoldt, *Zu Riemann's Abhandlung “Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse”*, *J. reine angew. Math.* 114 (1895), 255–305, especially pp. 285–292 for the grouped remainder and pp. 299–301, eq. (64) and its interpretation, for the specialization to Riemann's midpoint prime-power function. With that input the modern formula is unconditional for \(x>1\):
\[
J_0(x)=\operatorname{Li}(x)-\lim_{T\to\infty}\sum_{|\Im\rho|\le T}E_\rho(x)
+\int_x^\infty\frac{du}{u(u^2-1)\log u}-\log2 ,
\]
where \(E_\rho\) is the chosen horizontal primitive above. Standard contour proofs take suitable heights and pass to all heights by the local zero count \(O(\log T)\) for a bounded window and the \(O_x(T^{-1})\) individual terms. The same observation gives agreement of magnitude and height orderings, since \(||\alpha|-\Re\alpha|=O(1/T)\) near the large cutoff by the strip bound. Conjugation closes the truncated sums in either ordering. This argument provides no general license to reorder the sum or differentiate it termwise. The memoir's assertion about arbitrary real rearranged values is separate and is not needed for the canonical formula. The 1892 note at pp. 154–155 identifies statements where the draft itself acknowledges omitted justifications, including the approximate real-zero count and this contour-limit comparison.

## Recovering prime counts and interpreting illustrations | pp. 679–680

The finite Möbius inversion \(F(x)=\sum_{m\ge1}\mu(m)J_0(x^{1/m})/m\) follows from \(\sum_{d\mid n}\mu(d)=\mathbf1_{n=1}\), with exactly the same endpoint conventions. It recovers prime counts and leaves the main distinction between prime and prime-power jumps visible. After a fixed finite zero truncation, differentiating the smooth surrogate gives \((1-2x^{-1/2}\sum_\alpha\cos(\alpha\log x))/\log x\), up to the derivative \(-1/[x(x^2-1)\log x]\) of the small tail. This is the density displayed on p. 679. At a fixed \(x\) the actual counting function is a staircase, with atomic distributional derivative. Complex \(\alpha\) are allowed and the real-valued combination comes from symmetry. Oscillation plots made with finitely many roots are smooth approximations rather than a termwise differentiable infinite identity.

For the nonoscillatory terms Möbius inversion yields the displayed \(\operatorname{Li}(x)-\tfrac12\operatorname{Li}(\sqrt x)-\tfrac13\operatorname{Li}(x^{1/3})-\cdots\), with signs from square-free exponents. The first subtraction is asymptotic to \(-\sqrt x/\log x\); this computation alone gives no bound at that scale for the sum of the zero terms and no permanent sign for \(\pi(x)-\operatorname{Li}(x)\). The wording on the order of \(x^{1/2}\) and the Gauss–Goldschmidt comparison up to \(3\,000\,000\) describe this heuristic and the reported numerical range. The final suggested study of local density oscillations is a research program. Its closing use of the same printed additive constant carries the normalization issue already isolated above.

The memoir thus supplies two reconstructible routes to the functional equation, an entire even completion, a prime-power inversion at jumps, and the structure of the explicit formula. The printed argument count, product and zero-sum interchange need the specified analytic inputs for modern proofs. The prime-counting identity with the historical correction is independent of the conjecture about zero locations. This whole-work review supports a coverage assessment only.

Original journal witness and aligned editions. [First print facsimile](https://upload.wikimedia.org/wikipedia/commons/d/d2/RiemannPrim1859.djvu) · [Wilkins German edition](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/Zeta.pdf) · [Wilkins English translation](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf)
