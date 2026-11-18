# Independent whole-work skeptic review of Riemann’s 1859 memoir

**Work** PAPER-S001, Bernhard Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Größe*, Berlin Academy November 1859 report, pp. 671–680. The first page records Kummer’s presentation at the 3 November session and Riemann’s 19 October communication to Encke. The bound-volume dating reported by the archive can differ from the session year. These are manifestations of one work.

I read the original German print on all ten page images and compared the complete German transcription and consulted the relevant Wilkins preliminary English passages, using the original print as controlling evidence. The translation and standalone transcription each have a title page and nine numbered text pages. The 1892 edition and Genocchi were checked at the relevant correction passages as separate primary sources. This is an independent whole-work review with a modern reconstruction. It neither changes canonical records nor adjudicates a level.

| Source | Exact SHA-256 |
| --- | --- |
| Original ten-page journal scan, `sources/history_round4/riemann1859_original.djvu` | `9e2b9cd404dd8d054689607ef4b7c49734fd0d6648a272244451f6ae9a5f9b4c` |
| Wilkins German PDF, December 1998, `sources/history_round4/riemann_german_transcription.pdf` | `ba7fd13614b373798f9d953cee4bb7b4aa7764067edddaa7561e835a6a3331a2` |
| Wilkins English PDF, December 1998, `sources/spectral/riemann.pdf` | `6b24341e3406d165baeb7ab1e00cfa0a544d0399e2b33175dfa71480bdddd24f` |
| 1892 collected works, Vol. PDF, printed pp. 145–155 relevant | `55f149d350e4541d0c536222b4a26d74ce5f751a2f0ef97c3b8d3559894de358` |
| Genocchi 1860 printed pp. 52–59 extraction | `60c40a680b855cf36b17a588b94e70692d019416ce05654d895a82f149b5a35c` |

The exact original page-image hashes and URLs are in `sources/history_round4/source_manifest.json`. The Clay images are separate manuscript evidence. This review uses the journal print for the memoir's mathematical wording. [Journal scan](https://upload.wikimedia.org/wikipedia/commons/d/d2/RiemannPrim1859.djvu) · [German transcription](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/Zeta.pdf) · [English translation](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf)

## Coverage and disposition

| Original pages | Mathematical content | Original proof status and present check |
| --- | --- | --- |
| 671–672 | Euler product, gamma Mellin integral, Hankel germ and continuation | Valid with absolute convergence in the starting half-plane, the indicated logarithm and meromorphic removal of apparent integer poles. |
| 672–673 | Residues at \(2\pi i n\), functional equation, Jacobi transform | Two genuinely different routes. The Hankel argument's growing-circle estimate and the theta route's compact uniform convergence are supplied below. Jacobi's identity is cited in the memoir. |
| 673–674 | Entire even completed function and two cosine formulas | Both formulas check, including the finite boundary term in the integration by parts. |
| 674 | Strip, zero-count main terms, evidence about real zeros and RH | Euler product and symmetry give the closed strip. The count is sketched and the critical-line count claim is unsupported in print. RH appears expressly as a conjecture. |
| 675 | Paired product and its logarithm, midpoint count, prime-power weights | Modern growth and Hadamard justify the paired product. The original quotient-growth argument is compressed. The endpoints check exactly. |
| 675–677 | Mellin/Fourier inversion, integration by parts, gamma factors | Fourier inversion applies to the sum of the split pieces with the midpoint convention. Product substitution and a displayed residue sign require local textual corrections in the original print. |
| 677–679 | Recovery of logarithmic integrals, constant and zero-series limit | Branches are essential. The printed constant is corrected below. The finite-height-to-ordinary-zero-series equality is asserted with the detailed proof omitted in print. |
| 679–680 | Möbius inversion, finite density model, comparison with counts | The inversion is exact. The differentiated finite zero model and the numerical comments do not assert a distribution-free pointwise theorem for the prime density. |

## Continuation, completion and zeros

Use \(\Pi(z)=\Gamma(z+1)\). For \(\Re s>1\), absolute Euler and gamma sums establish \(\Gamma(s)\zeta(s)=\int_0^\infty x^{s-1}/(e^x-1)\,dx\). On the Hankel contour with positive orientation around zero and a cut along the positive \(x\)-axis, take \(\log(-x)\) real for negative \(x\). The two banks give \(e^{-\pi i s}-e^{\pi i s}\). This yields the printed \(2\sin(\pi s)\Gamma(s)\zeta(s)=iH(s)\). With a fixed nonzero detour around 0, \(H\) is entire in \(s\), and \(i\Gamma(1-s)H(s)/(2\pi)\) gives the continuation. Agreement on the initial half-plane removes the apparent poles at integers \(\ge2\). At \(s=1\), the detour residue gives \(H(1)=2\pi i\) and the residue of \(\zeta\) is 1.

For \(\sigma=\Re s<0\), close the truncated contour on circles \(R=(2m+1)\pi\). The radii stay uniformly separated from the nonzero poles. The reciprocal of \(e^x-1\) is uniformly bounded on those arcs, using distance from the poles in a bounded real-part band and the simple estimates on either side. The power and arc length give an \(O_s(R^\sigma)\) bound. The clockwise residues at \(\pm 2\pi i n\) yield the printed sum, absolutely convergent for \(\sigma<0\), and the gamma identities yield invariance of \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) under \(s\mapsto1-s\). In particular the negative even integers are simple trivial zeros because \(\Lambda(1+2n)\ne0\) and the gamma pole is simple.

The independent Jacobi route takes \(\psi_\theta(x)=\sum_{n\ge1}e^{-\pi n^2x}\) and uses \(2\psi_\theta(x)+1=x^{-1/2}(2\psi_\theta(1/x)+1)\), cited as *Fundamenta*, p. 184. Splitting at 1 gives
\[
\Lambda(s)=\frac1{s(s-1)}+\int_1^\infty\psi_\theta(x)\bigl(x^{s/2-1}+x^{-(s+1)/2}\bigr)\,dx.
\]
The tail integral is entire by exponential decay uniformly on compact sets. In the intermediate step the second term is \(\int_0^1\psi_\theta(1/x)x^{(s-3)/2}dx\), as printed on 673 and 1892 p. 147. Both Wilkins standalone PDFs p. 3 put \(1\) and \(\infty\) on this one integral. At \(s=2\), its incorrect integrand tends to \(1/2\), proving the literal standalone display fails. Its next equality is the correct one.

Let \(\xi_*(s)=s(s-1)\Lambda(s)/2\) and \(\Xi_R(t)=\xi_*(1/2+it)\). For \(K(u)=e^{u/2}\psi_\theta(e^{2u})\), the first p. 674 cosine identity becomes
\[
\Xi_R(t)=\tfrac12-2(t^2+\tfrac14)\int_0^\infty K(u)\cos(tu)\,du.
\]
Jacobi's identity gives \(\psi_\theta'(1)=-(2\psi_\theta(1)+1)/8\), hence \(K'(0)=-1/4\). Twice integrating by parts gives \(\Xi_R(t)=2\int_0^\infty(K''-K/4)\cos(tu)du\), equivalent to the second printed display. The kernel's rapid decay justifies termwise even Taylor development. On every bounded real interval in \(u\) it is finite, and for large \(u\) it has a majorant \(C e^{Cu-c e^{2u}}\). This also gives \(\log\max_{|t|\le R}|\Xi_R(t)|=O(R\log(2+R))\).

The Euler product and symmetry give \(0\le\Re\rho\le1\) for completed zeros. The p. 674 proof by itself leaves the boundary lines open. The later Hadamard p. 199–203 proof closes the 1-line, with the other boundary following by symmetry. The real axis of \(s\) gives no completed zero, since \(\xi_*(0)=\xi_*(1)=1/2\), the alternating eta series gives \(\zeta(s)<0\) for real \(0<s<1\), and Euler/symmetry deal with the exterior. Thus the paired parameters \(\alpha\) can be chosen with \(\Re\alpha>0\), with multiplicities, and \(\rho=1/2+i\alpha\) runs through positive-ordinate zeros. The partner \(1-\rho\) has negative ordinate even when RH is false.

Riemann's smooth count main terms on p. 674 can be recovered by a modern argument principle. For nonzero ordinates avoided at the top of the rectangle, symmetry reduces the count to \(\pi^{-1}\Delta\arg\xi_*\) on the path \(2\to2+iT\to1/2+iT\). The polynomial factor contributes \(\pi\), and Stirling gives the two printed main terms. For the horizontal \(\zeta\) argument, the real crossings are zeros of \(g_T(z)=(\zeta(z+iT)+\zeta(z-iT))/2\). At \(z=2\) it is bounded below by \(2-\zeta(2)>0\), and on a fixed larger disk it has polynomial growth by Euler–Maclaurin. Jensen bounds the number of crossings on \([1/2,2]\) by \(O(\log T)\). The argument on each interval between crossings changes by at most \(\pi\). The 2-line has bounded argument by the same positive-real-part inequality. This proves the modern \(O(\log T)\) count remainder and the local \(O(\log(2+T))\) bound on unit-height intervals, with one-sided endpoints taken by limits. These estimates replace a sketch on p. 674, which gives no uniform avoidance or argument calculation. Its “Bruchtheil” qualifier of order \(1/T\) should not be read as an absolute \(O(1/T)\) error in a continuous approximant to an integer-valued step count.

The observation about finding roughly as many real \(t\)-zeros as the total is distinct from the argument-principle count. The 1892 editors p. 154 quote Riemann's draft letter identifying this real-root assertion and the zero-series/contour limit as the two conclusions reliant on an unpublished development. The contemporary explanation supports recording those proofs as omitted. The original says a rigorous proof of the reality conjecture would be desirable and that its search was set aside. [Hadamard primary source](https://www.numdam.org/article/BSMF_1896__24__199_1.pdf) · [1892 collected edition](https://archive.org/download/gesammeltemathem00riemuoft/gesammeltemathem00riemuoft.pdf)

## Product, inverse Mellin and local print corrections

Evenness and the growth estimate imply the entire function \(w\mapsto\Xi_R(\sqrt w)\) has order at most \(1/2\). Hadamard's genus-zero factorization in \(w\) gives \(\Xi_R(t)=\Xi_R(0)\prod_{\Re\alpha>0}(1-t^2/\alpha^2)\). The local count also gives \(\sum |\alpha|^{-2}<\infty\). Equal zeros with multiplicities, a holomorphic logarithm of the quotient and a global complex growth bound are important here. A continuous real-axis logarithmic difference of subquadratic growth would not alone enforce constancy. The modern product proof supplies the omitted analytic ingredients. All logarithmic identities are branch statements on an appropriate cut domain.

The memoir's \(F\) is \(\pi_0(x)=\#\{p<x\}+\tfrac12\mathbf1_{x\text{ prime}}\). Its \(f\) is \(J_0(x)=\sum_m\pi_0(x^{1/m})/m\). For a prime power \(p^m\), the jump of \(J_0\) is \(1/m\) and the value at the jump includes only \(1/(2m)\). The integral for \(\log\zeta(s)/s\) with \(\log\zeta\) fixed by its Euler expansion follows by absolute summation when \(\Re s>1\). In \(y=\log x\) it is a Laplace transform. The exponentially tilted cumulative step function is integrable and of bounded variation, so symmetric Fourier inversion returns midpoint values. The separated cosine and sine inverses actually yield \(\pi(H(y)+H(-y))\) and \(\pi(H(y)-H(-y))\), with \(H(y)=e^{-ay}h(e^y)\). Their sum gives the required \(2\pi H(y)\). For the particular prime count, \(y>0\) implies \(H(-y)=0\), but the memoir's general wording need not have that auxiliary support property. This is the point of the 1892 note (2), pp. 154–155.

The integral replacement for each prime-power term on p. 675 prints the correct differential \(dx\). The standalone German and English Wilkins versions p. 5 print \(ds\) in that preliminary line but restore \(dx\) in the following transform. This is a separate, local transcription slip.

On p. 676 the original displayed substitution for \(\log\zeta\) prints one \(\log(1+(s-1/2)^2/\alpha^2)\) without the summation. The product on p. 675 and the zero-summed integral on pp. 678–679 specify the intended sum. The 1892 typesetting and both standalone Wilkins versions show it. On p. 677 the original line immediately below the parameter derivative displays
\[
\frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}\frac{x^s}{(\beta-s)\beta}\,ds
=\frac{x^\beta}{\beta},\qquad a>\Re\beta.
\]
For \(x>1\), \(\beta\ne0\), the residue at \(s=\beta\) is **negative**, so the printed left side equals \(-x^\beta/\beta\). For \(\beta=-2\), the left is \(+x^{-2}/2\), and the printed right is \(-x^{-2}/2\). The 1892 and Wilkins versions insert the minus before the integral. The adjacent \(\beta\) derivative \(\partial_\beta[s^{-1}\log(1-s/\beta)]=1/[\beta(\beta-s)]\) is correct. The subsequent p. 678 expression has the minus from integration by parts and gives the displayed positive primitive derivative when the preceding sign is corrected. These two textual slips are separate from the known final constant correction and require no changed mathematics in the surrounding formulas.

At finite symmetric height, integration by parts has a boundary term. Before splitting \(\log\zeta\), the Euler logarithm is bounded on \(\Re s=a>1\), so the boundary term is \(O_{x,a}(1/T)\) when \(x>1\). Riemann explicitly warns that splitting the original integral into its separate infinite log terms is invalid. Integrating by parts removes some problems but does not on its own justify a subsequently growing sum over zeros.

## Reconstructing the explicit formula and the ordinary height limit

In modern notation, use \(y=\log x>0\) and the branch-complete convention \(\operatorname{Li}(x^\rho)=\operatorname{Ei}(\rho y)\). At positive real argument \(\operatorname{Ei}\) is the symmetric principal value. For nonreal \(\rho\), the argument is \(\rho y\) itself. Composing ordinary \(\operatorname{Li}\) with a principal logarithm of the complex number \(x^\rho\) would fold the argument and change the value.

The constant issue can already be seen in the product. For each selected \(\alpha\) with \(\rho=1/2+i\alpha\),
\[
\frac{1+(s-1/2)^2/\alpha^2}{1+1/(4\alpha^2)}
=(1-s/\rho)(1-s/(1-\rho)).
\]
Thus anchoring the two linear factors at \(s=0\) changes the constant to
\[
\log\Xi_R(0)+\sum_{\Re\alpha>0}\log\bigl(1+1/(4\alpha^2)\bigr)
=\log\xi_*(0)=-\log2.
\]
Use the paired branches continued from the product and real total on the real axis. The distinction is between the centered value \(\Xi_R(0)=\xi_*(1/2)\) and \(\xi_*(0)=\Xi_R(i/2)=1/2\). The first p. 674 cosine formula at \(t=0\) makes the two values strictly different, since the subtracted theta integral is positive. The original 678 display gives \(+\log\Xi_R(0)\) and p. 680 repeats it in the numerical comparison. Genocchi pp. 57–58 explicitly restores the constants and gets \(-\log 2\) in (11). The 1892 editors p. 155 state the same correction and speculate about how the older display arose. The correction is established separately from their speculation.

Here is a reconstruction that handles both inversion and ordinary convergence. Fix \(a>1\), write \(s=a+it\), and put
\[
L_\rho(s)=\log(s-\rho)-\log\rho+i\pi\,\operatorname{sgn}(\Im\rho).
\]
This is the normalized log of \(1-s/\rho\) on the right half-plane. For height-symmetric pairs the imaginary branch constants cancel. The gamma Euler product and the normalized zero product give
\[
\log\zeta(s)=\tfrac{s}{2}(\log\pi+\gamma_E)-\log(s-1)-\log2
 +\sum_{\alpha}\bigl(L_\rho(s)+L_{1-\rho}(s)\bigr)
 +\sum_{n\ge1}\left(\log(1+s/(2n))-s/(2n)\right).
\]
The absolute sum of the paired terms on the vertical line is \(O_a((1+|t|)\log^2(2+|t|))\). For \(|\alpha|\le C(1+|s|)\), each log is \(O_a(\log(2+|s|))\), using positive horizontal separation. The complementary paired tail is \(O_a(\sum |s|^2/|\alpha|^2)=O_a(|s|\log(2+|s|))\). The gamma terms with their linear subtractions obey the same sufficient bound by splitting at \(n\asymp |s|\). Divide this identity by \(s^3\), the transform of the two successive primitives of \(J_0(e^y)\), and invert absolutely with summation under the integral. The two derivatives on \(y>0\) are then taken distributionally. The linear terms of the unsmoothed logarithm give only boundary distributions at zero. The identity
\[
\int_0^\infty e^{-sy}\operatorname{Ei}(\rho y)\,dy
=\bigl(\log\rho-\log(s-\rho)\bigr)/s
\]
follows first from the \(\gamma_E+\log(\rho y)\) expansion for small \(\rho\) and then by continuation in the appropriate half-plane. The real positive pole term gives \(\operatorname{Ei}(y)\). Direct real integration gives inverse \(-\operatorname{Ei}(-2ny)\) for \(\log(1+s/(2n))/s\), and the sum is \(\int_x^\infty du/[u(u^2-1)\log u]\).

For ordinary zero-height convergence, use the logarithmic derivative of the same normalized identity and invert \(-\zeta'/\zeta(s)/s\). For any \(\beta\) left of the line write \(P_T(\beta)=(2\pi i)^{-1}\int_{a-iT}^{a+iT}x^s/(s-\beta)\,ds\). Each term \(1/[s(s-\rho)]\) has inverse \((P_T(\rho)-P_T(0))/\rho\). Shift the integration variable by \(\Im\rho\), then integrate its oscillatory tails by parts. For \(|\Im\rho|\le T\) the error in \(P_T(\rho)-x^\rho\) is bounded by a constant times \((1+T-|\Im\rho|)^{-1}+(1+T+|Im\rho|)^{-1}\). For \(|\Im\rho|>T\), \(P_T(\rho)\ll_x(1+|Im\rho|-T)^{-1}\). Constants can be chosen locally uniform for \(x>1\). Summing with \(\rho^{-1}\) by unit intervals and using the local \(O(\log(2+T))\) count bounds the growing kernel errors by \(O_x(\log^2(2+T)/T)\). The \(P_T(0)\) terms group into \(1/\rho+1/(1-\rho)=O(|\rho|^{-2})\); their cutoff and Perron errors tend to zero. The gamma derivative produces \(1/[2n(s+2n)]\); its truncated inversion error sums to \(O_x(\sum_{n\ge1}1/[n(T+n)])\), by the same tail integration with horizontal distance \(a+2n\). This is \(O_x(\log(2+T)/T)\).

The unsplit Perron inversion is the midpoint von Mangoldt sum \(\psi_0(x)\), by bounded-variation Fourier inversion. Its finite-height inversions are uniformly bounded on compact positive \(y\)-intervals because the exponentially tilted step function has finite total variation and the integral of the sine Dirichlet kernel is uniformly bounded. These estimates give ordinary pointwise convergence of \(\sum_{|\Im\rho|\le T}x^\rho/\rho\) to a midpoint representative plus continuous terms. Finally, on positive compact \(y\)-intervals,
\[
\operatorname{Ei}(\rho y)-i\pi\operatorname{sgn}(\Im\rho)
=\frac{e^{\rho y}}{\rho y}+O_y(|\Im\rho|^{-2}).
\]
For example integrate by parts in \(-\int_0^\infty e^{\rho y-v}/(v-\rho y)\,dv\). Opposite imaginary signs cancel the constants; the residual series converges absolutely and locally uniformly. Thus the zero series recovered from twice-smoothed inversion has the ordinary pointwise height-ordered representative, and represents midpoint values even at every prime power. The convergence and local bound also justify matching the distributional and pointwise formulas. Ordering by \(|\alpha|\) in the paired list has the same limit as ordering by \(\Re\alpha\). The difference involves only a bounded-width window because \(|\Im\alpha|\le1/2\), and its contributions are \(O_x(\log T/T)\). An arbitrary series permutation has no such justification. Riemann's stronger rearrangement assertion is not proved in the memoir and is not needed here.

Consequently the corrected formula for every \(x>1\), with multiplicities and symmetric zero heights, is
\[
J_0(x)=\operatorname{Li}(x)-\lim_{T\to\infty}
\sum_{|\Im\rho|\le T}\operatorname{Ei}(\rho\log x)
-\log2+\int_x^\infty\frac{du}{u(u^2-1)\log u}.
\]
The local proof of the growing kernel estimates is comparable to von Mangoldt 1895 pp. 283–292. The reconstruction here does not depend on claiming the memoir printed those estimates. [Genocchi 1860](https://doi.org/10.1007/BF03198027) · [von Mangoldt 1895](https://doi.org/10.1515/crll.1895.114.255)

## Endpoint and historical numerical checks

The inverse relation is \(\pi_0(x)=\sum_{m\ge1}\mu(m)J_0(x^{1/m})/m\). It is a finite sum at each fixed \(x\), because terms with \(x^{1/m}<2\) vanish. Reindex by \(k=mn\) and use \(\sum_{m\mid k}\mu(m)=\mathbf1_{k=1}\). The half-jump at \(x=2\) is \(\pi_0(2)=J_0(2)=1/2\). At \(x=4\), \(J_0(4)=9/4\) and \(J_0(4)-J_0(2)/2=2\), giving the correct prime count with the square contribution removed. The inverse formula with its separately singular terms is stated for \(x>1\). The arithmetical step functions are zero for \(0<x<2\).

Differentiating a finite zero truncation gives the printed cosine term with coefficient \(-2x^{-1/2}/\log x\), plus the elementary main density and trivial-zero tail. A complex \(\alpha\) gives a complex cosine and can add growth in \(x\); the conjugate-completed truncation is real. This is a smooth model of the distributional derivative of the step count, and no estimate for derivatives of growing truncations at the jumps follows. The finite Möbius combination begins with \(\operatorname{Li}(x)-\operatorname{Li}(\sqrt x)/2\) in its nonoscillating terms. That negative correction and the Gauss–Goldschmidt range through three million do not control the sign of all later prime-count errors. The closing phrase about agreement on average in the first hundred is descriptive, with no defined averaging theorem.

**Disposition.** The original supplies continuation, symmetry, the entire completed function, the prime-power Mellin transform and inversion, and the arithmetic inversion. Its product and zero count are mathematically recoverable with the stated modern analytic arguments. The zeta explicit formula is recoverable with corrected normalization and growing-limit control. The original publication's omitted proof details, local print slips, known constant correction, and later transcription-only theta error are distinct findings. No proof of a critical-line zero asymptotic or RH is attributed to the memoir.
