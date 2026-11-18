# Gonek 1984 | Whole-work advocate review

PAPER-LF63-GONEK1984, S. M. Gonek, *Mean values of the Riemann zeta-function and its derivatives*, *Inventiones Mathematicae* 75(1) (1984), 123–141, DOI 10.1007/BF01403094. The original journal PDF has 19 pages without an inserted cover. SHA-256 dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3. I read all pages, including the ten-item bibliography and the closing received/revised line (11 September 1982 and 29 September 1983). Key displays were checked on the rendered journal pages. This supports a complete original-source Level 1 reading event. A single advocate review does not automatically change the canonical record or adjudicate higher audit levels. [Pinned PDF](../../sources/classical63_lfunctions/gonek1984.pdf) · [Source URL](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf) · [DOI](https://doi.org/10.1007/BF01403094)

## Coverage ledger

| Printed pages | Content inspected and reconstructed |
|---|---|
| 123–125 | §1. Continuous comparisons (1)–(3), unconditional mixed Theorem (4), kernel \(H\), RH Corollaries 1–2 and normalized-gap Corollary 3. |
| 125–127 | §2. Functional equations (8)–(11), Stirling/digamma, good-height sequence, local logarithmic derivative (16)–(19), derivative bounds (20). |
| 127–129 | §3. Residue rectangle (21), upper/lower contour bounds, reflected conjugate right-edge reduction (22)–(23). |
| 129–133 | Lemmas 1–5, saddle reduction, near-endpoint control, logarithmic amplitude, summable coefficient errors, dyadic assembly. Lemma 6, differentiated gamma factor. |
| 133–136 | Lemmas 7–10, divisor convolution and beta integral, twisted von Mangoldt convolution via PNT, logarithmic weighting and finite binomial identity. |
| 136–140 | §5. Fixed ordinate displacement, differentiated functional equation, three right-edge contributions (38)–(42), uniform kernel and height removal (43). |
| 140–141 | §6. Gap argument and numerical test, references and source chronology. |

## Exact theorem and assumptions

For fixed integers \(\mu,\nu\ge0\), put \(L_T=(2\pi)^{-1}\log(T/(2\pi))\), and take \(\alpha\in\mathbb R\), \(|\alpha|\le L_T/2\). The main theorem is unconditional:
\[
\sum_{1\le\gamma\le T}\zeta^{(\mu)}(\rho+i\alpha/L_T)
                   \zeta^{(\nu)}(1-\rho-i\alpha/L_T)
=\frac{(-1)^{\mu+\nu}T(\log T)^{\mu+\nu+2}}{2\pi}
 \left[\frac1{\mu+\nu+1}-H(\mu,\nu,2\pi\alpha)-H(\nu,\mu,-2\pi\alpha)\right]
+O_{\mu,\nu}(T(\log T)^{\mu+\nu+1}).
\]
Here \(\rho=\beta+i\gamma\) runs over all nontrivial zeros with **multiplicity**. The error is uniform in the indicated real \(\alpha\) range. Multiplicity is forced by the residue of \(\xi_*'/\xi_*\), with \(\xi_*(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\), and does not require simple zeros. An equivalent form, before replacing the logarithm in the prefactor, uses \(\ell_T=\log(T/(2\pi))\). The kernel is
\[
H(\mu,\nu,c)=\mu!\sum_{j\ge0}
 \frac{(ic)^j}{(j+\mu+1)!(j+\mu+\nu+2)}
=\int_0^1\int_0^1 x^{\mu+\nu+1}(1-y)^\mu e^{icxy}\,dy\,dx.
\]
The beta integral proves the equality. The integral gives uniform boundedness, and bounded derivatives of any fixed order in real \(c\). The theorem itself uses a single real displacement \(\delta=\alpha/L_T\), \(|\delta|\le1/2\); neither a two-independent-complex-shift remainder nor an estimate uniform in the derivative orders follows.

Corollary 1 inserts RH to identify \(1-\rho=\bar\rho\), giving the critically sampled product of a shifted derivative and the conjugate of the other. For \(\mu=\nu\) this is the square modulus. At \(\alpha=0,\mu=\nu\) its coefficient in the brackets is
\[
\frac1{2\mu+1}-\frac{2}{(\mu+1)(2\mu+2)}
=\frac{\mu^2}{(2\mu+1)(\mu+1)^2}.
\]
For \(\mu=\nu=1\) it is \(1/12\), hence under RH
\[
A(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2
=\frac{T(\log T)^4}{24\pi}+O(T(\log T)^3).
\]
There are no ordinates in \((0,1)\). A multiple zero contributes zero at \(\mu=1,\alpha=0\); at shifted or higher-derivative tests one must still count multiplicities. Dividing by the Riemann–von Mangoldt count changes the log exponent from four for the prefix to three for the average per zero. For all \(\mu\ge1\), comparison to the continuous same-order moment in (3) gives the stated average factor \((\mu/(\mu+1))^2\). Corollary 2 uses \(H(0,0,c)=\int_0^1(1-v)e^{icv}\,dv\), so \(H(0,0,c)+H(0,0,-c)=[\sin(c/2)/(c/2)]^2\), with value one at zero. This is the RH shifted-zeta-square formula, uniformly throughout the same real shift range.

## Contour, good heights and effectivity

Take fixed \(1<a<2\), eventually \(a=5/4\), and the rectangle with vertical lines \(\Re s=a,1-a\), lower height 1 and upper height \(T\). Integrate \((\xi_*'/\xi_*)(s)\zeta^{(\mu)}(s+i\delta)\zeta^{(\nu)}(1-s-i\delta)/(2\pi i)\). The shifted poles of the zeta factors stay outside the rectangle, since \(|\delta|\le1/2\) and the lower edge is at 1. There are no vertical edge zeros by the standard strip placement and the choice of \(a\). The residue counts multiplicity.

The good-height sequence has a representative in each integer interval a distance \(\gg1/\log T\) from all ordinates. Derive this by discarding sufficiently short neighborhoods around the \(O(\log T)\) ordinates in a fixed-width window. The constants in this construction may be made effective. The local logarithmic derivative formula from Davenport p. 99 then gives \(\zeta'/\zeta=O(\log^2T)\) on a good line in the required strip. The gamma and elementary terms transfer this to \(\xi_*'/\xi_*\). The bottom edge is bounded. Convexity/differentiation estimates (20) give a product at most \(T^{a-1/2+\epsilon}\) after absorbing logarithms on the top. The left edge is **the complex conjugate** of \(I_1(\nu,\mu,\delta)\), since (11) reverses \(\xi_*'/\xi_*\), then reality under conjugation exchanges the two derivative slots. The overbar is clearly printed in (23) and (37); preserving it gives the negative sign of the second \(H\) argument. No RH is used in this reduction.

On the right line \(\xi_*'/\xi_*(a+it)=O_a(\log^2(2+|t|))\), and the entire gamma part can be isolated explicitly. Change variables \(s\mapsto s+i\delta\). The two small endpoint integrals are \(O(1)+O_{\mu,\nu}(T^{a-1/2+\epsilon})\) by (19)–(20), uniformly in the displacement. At the end, for any \(T\) choose \(T'\) good with \(|T'-T|\le O(1)\), **keep \(\delta\) fixed** and put \(\alpha'=\delta L_{T'}\). Convexity bounds the added or removed terms, including a height exactly at a zero, by \(O(T^{1/2+\epsilon}\log T)\), using the local count and multiplicity. The \(\ell_T\)-prefactor changes by \(O((\log T)^{\mu+\nu+2})\); the change of \(H\) is harmless by its real derivative bound and \(|\delta|\,|\ell_T-\ell_{T'}|\ll1/T\). This makes the printed height-removal step explicit, also at the two extreme permitted shifts. The theorem's error is unconditional and in principle effective, using the classical effective zeta PNT remainder, effective local counts and standard uniform analytic estimates. The paper does not give an explicit useful threshold or numerical constants for that purpose.

## Lemmas 1–10 and main coefficient

**Lemmas 1–3.** Functional-equation Stirling phase on the \(a+it\) line is \(-\pi/4+t\log(t/(2\pi e))\), with amplitude \((t/(2\pi))^{a-1/2}\). Multiplying by \(n^{-it}\) centers the saddle at \(r=2\pi n\). In Lemma 1, \(t=r(1+x)\) with fixed small \(|x|\le c\). After the factor \(e^{-ir}\), the phase is \(F(x)=(1+x)\log(1+x)-x=x^2/2+O(x^3)\). The analytic signed square root \(u=\sqrt{2F(x)}=x+O(x^2)\) normalizes the saddle. Writing the resulting analytic amplitude as \(1+u\,g_1(u)\) and integrating the second term by parts gives \(O(1/r)\) in the rescaled integral. The truncated Fresnel integral is \(\sqrt{2\pi/r}e^{i\pi/4}+O(1/r)\), giving the stated main term and \(O(r^{a-1/2})\) error. In Lemma 2 the endpoint denominator for an interval \([A,B]\), \(B\asymp A\), is \(|A-r|+\sqrt A\) or \(|B-r|+\sqrt B\), with numerator \(A^{a+1/2}\) or \(B^{a+1/2}\). Within an endpoint \(\sqrt A\)-zone, the second-derivative bound gives \(O(A^a)\), also for a saddle just outside the interval. Outside these zones, integration by parts using \(\log(t/r)\) gives the claimed denominator decay. Lemma 3 adds \((\log(t/(2\pi)))^m\): integrate against the smooth weight using Lemma 2 on subinterval endpoints. The saddle indicator produces its value at \(r\); the derivative of the weight and the integrated endpoint losses are bounded by the stated error with the log power. One can equivalently apply the same stationary/nonstationary estimates to this slowly varying amplitude.

**Lemmas 4–5.** The endpoint error sums reduce to \(\sum n^{-a+\epsilon}(|C-2\pi n|+\sqrt C)^{-1}\ll C^{-1}\) for fixed \(a>1\) and sufficiently small \(\epsilon<a-1\). For \(n\asymp C\) the weight is \(O(C^{-a+\epsilon})\) and the denominator reciprocals sum to \(O(\log C)\). For smaller or larger \(n\) use the denominator \(\gg C\) or \(\gg n\). Absolute summation and this uniform estimate justify the saddle evaluation over \([T/2,T]\). The Stirling \(O(1/t)\) remainder costs \(O(T^{a-1/2}(\log T)^m)\). The saddle phase \(e^{-2\pi in}\) is one, and the amplitude constants cancel, yielding the coefficient sum through \(T/(2\pi)\). Summing dyadic errors geometrically and retaining a bounded initial interval gives (26). The constants depend on the divisor-type envelope of the coefficients, not on the location of the saddle.

**Lemma 6.** Logarithmic differentiation of the functional-equation factor gives \(\chi'/\chi(1-s)=-\log(|t|/(2\pi))+O(1/|t|)\), and all its fixed positive derivatives are \(O(1/|t|)\) by Cauchy and uniform digamma Stirling. Induction by Leibniz gives (31) with error \(O(|t|^{a-3/2}(\log |t|)^{\nu-1})\) for large \(|t|\). The compact portion is bounded separately, so the argument need not use vanishing powers of \(\log |t|\) near 1.

**Lemmas 7–9.** The coefficients of \(\zeta^{(\mu)}(s)\zeta^{(\kappa)}(s)\) are \((-1)^{\mu+\kappa}\sum_{dr=n}(\log d)^\mu(\log r)^\kappa\). The hyperbola partition, single power-log sums and integrals give \(x(\log x)^{\mu+\kappa+1}\mu!\kappa!/(\mu+\kappa+1)!\), with an error lower by a log and the indicated sign. In Lemma 8, convolution by \(-\Lambda(d)d^{i\delta}\) gives the leading integral
\[
 \int_1^x u^{i\delta}(\log(x/u))^{\mu+\kappa+1}\frac{du}{u}.
\]
The classical effective \(\sum_{d\le u}\Lambda(d)=u+O(u e^{-c\sqrt{\log u}})\) allows this replacement by partial summation. Differentiation of \(u^{i\delta}\) costs \(|\delta|\), bounded in the actual use \(|\delta|\le1/2\). Expanding the exponential after \(u=x^v\), then integrating \(v^j(1-v)^{\mu+\kappa+1}\), gives
\[
\sum_{n\le x} B_n(\mu,\kappa,\delta)
=(-1)^{\mu+\kappa+1}\mu!\kappa!x(\log x)^{\mu+\kappa+2}
 \sum_{j\ge0}\frac{(i\delta\log x)^j}{(j+\mu+\kappa+2)!}
 +O(x(\log x)^{\mu+\kappa+1}).
\]
Uniformity concerns bounded real displacements, not arbitrary \(\delta\to\infty\). The beta integral is bounded uniformly before expansion for real \(\delta\). This controls any fixed logarithmic weighting by Abel summation, including exponent zero and the complex oscillating kernel actually used. Thus no extension of the literal real-power statement of Lemma 9 by coefficientwise bounds on the potentially large Taylor series is needed.

**Lemma 10 and closure.** The finite identity is
\[
 \sum_{\kappa=0}^\nu (-1)^\kappa{\nu\choose\kappa}\frac{\kappa!}{(\lambda+\kappa)!}
 =\frac1{(\nu+\lambda)(\lambda-1)!}.
\]
Integrating \(\sum(-1)^\kappa{\nu\choose\kappa}y^\kappa=(1-y)^\nu\) with the beta weight proves it. After the displacement change on the right edge, differentiate the functional equation for \(\zeta^{(\nu)}(1-s)\) with respect to \(1-s\). Each term is \((-1)^\kappa{\nu\choose\kappa}\zeta^{(\kappa)}(s)\chi^{(\nu-\kappa)}(1-s)\). In \(\xi_*'/\xi_*(a+it-i\delta)\) the leading three pieces are \(\zeta'/\zeta(a+it-i\delta),\,\tfrac12\log(t/(2\pi)),\,i\pi/4\). The first yields the negative convolution and the \(H\) term (40). The second gives the rational half-diagonal term (41). The third is one log power lower (42). The gamma derivative gives \((-1)^{\nu-\kappa}\) and the logarithmic powers needed to align the first two terms. Lemma 10 gives
\[
 I_1(\mu,\nu,\delta)=(-1)^{\mu+\nu}\frac{T}{2\pi}
 \ell_T^{\mu+\nu+2}\left[\frac1{2(\mu+\nu+1)}
                 -H(\mu,\nu,\delta\ell_T)\right]
 +O(T(\log T)^{\mu+\nu+1})
\]
at \(a=5/4\), where the power-saving analytic errors are absorbed. Adding the reflected conjugate gives the theorem. This derivation distinguishes the finite differentiations in (38) from trying to differentiate an asymptotic known only for one real variable.

## Gap application and local textual findings

The p. 125 definition is \(\lambda=\limsup(\gamma_n-\gamma_{n-1})\log\gamma_n/(2\pi)\). Corollary 3 there **prints \(\lambda\ge1.9\)** under RH. Integrating Corollary 2 for \(-b/2\le\alpha\le b/2\), for fixed \(b>\lambda\), gives the sum of interval integrals of \(|\zeta(1/2+it)|^2\) over windows of radius \(b/(2L_T)\) centered at the ordinates and asymptotic \(F(b)T\log T\), where \(F(b)=\int_{-b/2}^{b/2}[1-(\sin(\pi x)/(\pi x))^2]\,dx\). To justify the covering lower bound uniformly, work on \([\epsilon T,(1-\epsilon)T]\) with fixed \(\epsilon>0\). There \(\log\gamma_n/\ell_T=1+O_\epsilon(1/\log T)\) for neighboring ordinates and eventually the actual gaps are strictly smaller than the full window length, since \(b>\lambda\). The endpoint windows are present for sufficiently large \(T\). Nonnegativity and the continuous second moment give \(F(b)\ge1-2\epsilon\); let \(\epsilon\downarrow0\). There is no need to assert \(F(b)>1\) merely from an asymptotic lower bound. Numerical evaluation gives \(F(1.9)=0.99726619997764485\ldots\), as reported in the source, and the unique positive solution of \(F(b)=1\) is approximately \(1.90274111752\). Continuity therefore also gives a strict \(>1.9\) mathematical consequence, even though the printed corollary uses \(\ge\). This is Mueller's application presented by Gonek.

The following local findings are visible in the pinned print and do not alter the proved derivative prefix.

- **p. 123, contextual equation (2).** The mixed continuous-moment formula displays a positive term without the needed \((-1)^{\mu+\nu}\). A direct check for \(\mu=1,\nu=0\) uses differentiated functional equation on the critical line to give \(2\Re(\zeta'(s)\zeta(1-s))=(\chi'/\chi)(s)|\zeta(s)|^2\). The factor is \(-\log(t/(2\pi))+O(1/t)\). Then Hardy–Littlewood (1) and partial summation give a negative leading real part \(-T\log^2T/2\), opposite the printed positive formula. The same-order square in (3) is unaffected. The contextual attribution is not a claim of a defect in Ingham's original paper.
- **p. 129, Lemma 1.** Its intermediate printed \(f(x)=(1+x)\log(1+x)-(1+x)\) has \(f(0)=-1\), contrary to the following double-zero expansion. Add \(1\) once \(e^{-ir}\) is taken outside; the lemma and all subsequent uses have the intended phase. The heading “§3. Lemmas” is also repeated despite the earlier §3 and the surrounding references to those lemmas as §4.
- **p. 140, gap display.** The line defining \(b>\lambda\) prints \(2\pi/\log\gamma_n\) rather than the p. 125 normalization. The window argument uses the latter. The above truncated interval proof also supplies the implicit endpoint repair.

## Dependencies and strict-tail reuse

The references are each legible in the journal. Hardy–Littlewood [2] and Ingham [3] provide the continuous context, with [2] used in the gap comparison. Davenport [1] provides the local logarithmic derivative and standard analytic number theory context; the effective zeta PNT with remainder is a named external input to Lemma 8. Whittaker–Watson [10] supplies the gamma Stirling apparatus, and Titchmarsh [9] supplies the strip bound and second-derivative oscillatory estimate. Levinson [4] is the explicit antecedent of Lemmas 1–2. Montgomery [5] and Selberg [8] supply historical gap context. Mueller [6]–[7] supplies the gap application. This review reconstructs their uses rather than re-auditing the whole upstream works.

The unshifted \(A(t)\) holds at arbitrary large heights including endpoints. Under RH, \(|\rho|^{-2}=(t^2+1/4)^{-1}\). Partial summation on the **strict** positive tail gives
\[
\sum_{\gamma>Y}\frac{|\zeta'(\rho)|^2}{|\rho|^2}
=-\frac{A(Y)}{Y^2+1/4}
  +\int_Y^\infty\frac{2tA(t)}{(t^2+1/4)^2}\,dt
=\frac{(\log Y)^4}{24\pi Y}+O\!\left(\frac{(\log Y)^3}{Y}\right).
\]
The endpoint subtracts one leading copy and the integral supplies two. Symmetry doubles it for the two-sided strict tail. No increases in precision at exceptional ordinates, derivative-order uniformity, inverse-moment upper bound, arithmetic prime-phase law, or growing Dirichlet-polynomial twist follows from this source alone. With a shifted statistic, using a fixed displacement throughout a tail requires taking \(\alpha_t=\delta L_t\) in each prefix; freezing a normalized \(\alpha\) in all prefixes would change the observable. The unshifted proof avoids that issue and supplies the denominator used by current tail comparisons, without an auxiliary Dirichlet GRH or simplicity.

**Disposition.** Whole source read and main arithmetic proof reconstructed. The three substantive textual points above are local, with corrections available from the same proof or an elementary check. No canonical promotion or source error adjudication made here.
