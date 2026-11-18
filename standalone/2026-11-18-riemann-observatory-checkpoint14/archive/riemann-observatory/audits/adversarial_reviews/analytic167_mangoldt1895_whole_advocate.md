# PAPER-H406 — Whole-source advocate reconstruction of von Mangoldt 1895

Hans von Mangoldt, *Zu Riemanns Abhandlung „Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse“*, Journal für die reine und angewandte Mathematik 114 (1895), 255–305, DOI [10.1515/crll.1895.114.255](https://doi.org/10.1515/crll.1895.114.255). Pinned [original article scan](../../sources/history_round4/mangoldt1895_pp255-305.pdf), SHA-256 `4a75707d429a2ba3c310e0150bfd00d0c79a2c0d8b94df6eb2fd0a8cc071c3e6`, 51 pages. Article PDF index 1–51 corresponds to print 255–305 and bound-volume physical 262–312. The closing date is Aachen, 2 June 1894. The first-page footnote identifies the 1894 announcement, PAPER-H405. PAPER-H406 is its expanded companion in WORK-MANGOLDT-1894-1895. The earlier [catalog scope](../../papers/PAPER-H406.md) was targeted, with whole-work reading false. I read the complete printed article in the original renders, with the cached OCR as a navigation aid, and reconstructed its two proof sections. The OCR aggregate's headings are shifted by one in places. The ledger uses visible printed pagination. This is an independent advocate audit, with no source promotion.

## I. Counting zeros, pp. 257–274

Use \(\Xi(z)=\xi(1/2+iz)\), with \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\). The paper writes \(\Xi\) as \(\xi(t)\), \(\log\) as \(l\), and \(\Gamma(z+1)\) as \(\Pi(z)\). The positive-real-part zeros \(\alpha_\nu=\beta_\nu+i\gamma_\nu\) of \(\Xi\) are listed with multiplicity in nondecreasing \(\beta_\nu\). Thus \(\beta_\nu\) is a positive zeta ordinate and \(|\gamma_\nu|\le1/2\), rather than the usual real part of a zeta zero. Reality on the axes and evenness give \(\alpha\mapsto-\alpha,\bar\alpha,-\bar\alpha\). There are no zeros on the imaginary \(z\)-axis, as also follows from the Riemann cosine integral with positive kernel evaluated at imaginary \(z\). The infinite product (1),
\[
 \Xi(z)=\Xi(0)\prod_{\nu\ge1}(1-z^2/\alpha_\nu^2),\qquad
 \sum_\nu|\alpha_\nu|^{-2}<\infty,
\]
is the Hadamard input, not a result the article undertakes to prove from scratch. The introduction also acknowledges Piltz's antecedent route, described there as depending on assumed zero distribution.

**Angular counting.** On the segment \(z=\tau-3i/2\), \(a\le\tau\le b\), every linear zero factor contributes a positive continuous argument increment. The paired product permits summing the increments because of reciprocal-square convergence, or by integrating the locally uniformly convergent paired logarithmic derivative. Any zero with real part in \([a,b]\) sees the segment under an angle at least \(\arctan((b-a)/2)\): its transverse distance is between 1 and 2 and the endpoint configuration minimizes the angle at the maximum distance. Thus \(A\arctan((b-a)/2)<\Phi\), with \(A\) the inclusive count and \(\Phi\) the full change of argument. With no zero in the interval, the intermediate strict inequality (3) reads \(0<0\); the geometric inequality there is weak and the needed (4) is strict because other zeros contribute positive angles. This has no effect on any count.

**Gamma and Euler factors.** The segment is the line \(\Re s=2\). Equation (6) takes the continuous logs real at \(\tau=0\), not repeated principal arguments of \(\Xi\). At \(\tau>0\), (7)–(16) give
\[
 F(\tau)=\tfrac{\tau}{2}\log(\tau/2)+\arctan(\tau/2)+\arctan\tau
 +\tfrac\pi4-\tfrac{\tau}{2}(1+\log\pi)+E(\tau),
 \quad -\log\zeta(2)-\tfrac1{3\tau}<E(\tau)<\log\zeta(2).
\]
Here \(F\) is the imaginary part of that continuous log, \(F(0)=0\), \(F(-\tau)=-F(\tau)\), and \(\Phi=F(b)-F(a)\). The bounds use the absolutely convergent Euler log on \(\Re s=2\) and the cited Stieltjes \(\log\Gamma\) remainder. For the Stieltjes integral displayed on p. 262, at \(i\tau/2\) each reciprocal denominator has negative imaginary part because its two factors have nonnegative real parts and the product has positive imaginary part. The source therefore obtains the one-sided bound without a \(\tau^{-1}\) loss above, and uses \(1/(3\tau)\) below. The Stieltjes expansion itself is a classical cited input.

**Four outcomes.** On \([-12,12]\) any nonzero inclusive count is at least two by symmetry. Inequality (17) would then require \(12\log6+2\arctan6+\pi/2+2E(12)>12(1+\log\pi)\). Retaining the \(n=2,3\) terms in the Euler log and bounding the remaining positive-weight sine corrections by their absolute envelope gives \(E(12)<-0.15125\), and the left side is below \(25.581\) while the right side exceeds \(25.736\). Thus there are no zeros with \(0<\beta_\nu\le12\). The comparison for 13 merely says that this numerical exclusion no longer follows there. The Jensen figures on p. 264 are historical comparisons.

For \(\kappa=\tan1\le k\le h-4\), apply (4) on \([h-k,h+k]\) and (16). The derivative of \(\tau\log(\tau/2)/2+\arctan(\tau/2)+\arctan\tau\) at the intermediate point is less than \(\frac12\log h+0.658824\) by \(h-k\ge4\) and \(h+k<2h\). The increment of \(E\) is less than \(2\log\zeta(2)+1/12<1.07874\). With \(\arctan k\ge1\) these give the printed local bound \(A<k\log h\), since \(1+\log\pi-1.317648-1.07874/\kappa>0\). A fixed \(k=\kappa\) supplies \(O(\log(2+h))\) on any fixed-length ordinate interval.

For the inclusive global count \(H=N(h)=\#\{\beta_\nu\le h\}\), (18) gives
\[
 \Phi=h\log(h/(2\pi))-h+5\pi/2+O(1),\qquad |\text{error}|<1.548\quad(h>12).
\]
Equations (19)–(22) express the same argument change as \(2\pi H-2S_1+2S_2\). With \(d_\nu=3/2+\gamma_\nu\in[1,2]\), the \(S_1\) terms for \(\beta_\nu\le h\) are \(\arctan(d_\nu/(h+\beta_\nu))+\arctan(d_\nu/(h-\beta_\nu))\), using \(\pi/2\) at a tie. The \(S_2\) terms for \(\beta_\nu>h\) are the difference of arctangents with denominators \(\beta_\nu-h,\beta_\nu+h\). The factor 2 in (22) uses reflection about the imaginary axis and preserves the imaginary coordinate in each reflected term. In \(S_1\), the first contribution is bounded by \(2H/h\); the rest is bounded by block-count times a harmonic sum plus \(O(\log h)\) at the endpoint. For \(S_2\), the first block contributes \(O(\log h)\). After that use \(\arctan u\le u\) and \(\arctan u\ge u-u^3/3\), giving an upper summand \(\ll h/[(\beta_\nu-h)(\beta_\nu+h)]+(\beta_\nu+h)^{-3}\). On \(h<\beta_\nu\le2h\) this gives a harmonic sum of size \(O(\log^2 h)\), and the rest is \(O(\log h)\) by \(\sum_{\beta_\nu>2h}\log\)-density against \(\beta_\nu^{-2}\).

The printed numerical refinement bounds \(S_1\) by \(2H/h+\log^2h+(\pi\kappa/2)\log h\) and \(S_2\) by \(\log^2h+(\gamma_E+\pi\kappa/2+1/\kappa)\log h+2.256\), using intervals of length \(2\kappa\), harmonic sum versus integral, and separate tail integrals in (25)–(26). Inserting the bounds into the signed relation, keeping the \(S_1,S_2\) errors with their opposite signs, gives (27):
\[
 H=\frac h{2\pi}\log\frac h{2\pi}-\frac h{2\pi}+\frac54
 +\eta\bigl(0.34(\log h)^2+1.35\log h+1.33\bigr),\qquad |\eta|\le1 .
\]
In the last simplification the printed \(6/(6\pi-1)\) is about \(0.336143\), the combined linear coefficient is below \(1.3392\), and its constant bound has margin below \(1.33\). The introduction absorbs \(5/4\) into \(2.58\). The \(5/4\) is a choice of center for an explicit inequality, not a claimed resolved asymptotic constant. In particular the global error here is \(O(\log^2h)\), distinct from the fixed-width local estimate and from [von Mangoldt's 1905 \(O(\log h)\) count](geometry85_mangoldt1905_whole.md). Differencing (27) proves the stated density for window length \(k=o(h)\), \(k/(\log h)^2\to\infty\), with main term \(k\log(h/(2\pi))/(2\pi)\).

Finally \(H(53)\ge1\): if \(H=0\), then \(S_1=0\) and \(\Phi=2S_2\), whereas the symbolic bounds give respectively \(\Phi>66.3239\) and \(2S_2<65.147\). The displayed decimal \(66.3243\) differs slightly from direct evaluation of the displayed symbolic lower bound \(66.3239685\ldots\); the gap more than covers it. At 52 this test alone does not exclude \(H=0\). This is an enclosure for the first ordinate, not a demonstration of simplicity or of a zero lying on the critical line.

## II. Ordered explicit formulas, pp. 274–305

### Midpoint kernel and parameterized logarithmic derivative

Put \(K_h(g,u)=(2\pi i)^{-1}\int_{g-ih}^{g+ih}e^{us}\,ds/s\) for \(g>0\), with straight upward lines. The (28) half-line segment estimate follows by one integration by parts: for \(0\le c<d\), \(u\ne0\) and \(g\ne0\), the integral on \(g+i[c,d]\) is \(O(e^{ug}/(|u|(|g|+c)))\). The symmetric estimate (29) follows from \(c=0\) and reflection. This works for \(g<0\) as well, needed when closing to the left. In (30)–(34) the pole at zero is inside the left rectangle for \(u>0\); closing to the right for negative \(u\) misses it. The remote edge vanishes and the horizontal pair is bounded by \(3e^{ug}/(2\pi h|u|)\). The immediate \(u=0\) limit comes from the arctangent. Thus (35)–(37) give respectively \(1,0,1/2\).

With \(L(n)=\Lambda(n)\), real \(r\), fixed \(x>1\) and fixed \(a>0,\ a+r>1\), the Dirichlet series for \(-\zeta'/\zeta(s+r)\) converges absolutely on the integration line. In (38) the tail \(n>G>x\) is uniformly \(O(h^{-1})\) for fixed \(G\) by the negative-\(u\) bound and \(\sum\Lambda(n)n^{-a-r}<\infty\). The finite prefix gives
\[
 \Lambda_0(x,r)=\sum_{n\le x}'\Lambda(n)n^{-r}
  =-\lim_{h\to\infty}\frac1{2\pi i}
    \int_{a-ih}^{a+ih}\frac{\zeta'(s+r)}{\zeta(s+r)}\,\frac{x^s}{s}ds.
\]
Here prime powers carry \(\log p\) and a prime-power endpoint gets half its jump. The apparent extension to noninteger \(x\) from integer arithmetic is part of the Perron argument.

Taking the logarithmic derivative of the paired product and the gamma factors gives (39). Its paired zero series converges absolutely and uniformly along each fixed finite contour. The pole term in (40) gives \((1-x^{1-r})/(r-1)\), with \(\log x\) at \(r=1\) from (40a). The gamma factors yield \(\sum_{m\ge1}[\frac12\log(m/(m+1))+1/(s+r+2m)]\). In (41) use the Euler constant to subtract \(1/(2m)\), shift the single resolvents, and use (29) for the part \(m>G\). Its tail is \(O(\sum_{m>G}(r+2m)^{-2})\) uniformly in height, because the exponential from the shifted line cancels its prefactor. Hence \(G\) can be chosen before \(h\). At \(r=-2m\) the apparent quotient is replaced by \(1/(2m)-\log x\), using the same double-pole kernel as at \(r=1\). Equation (42) identifies the limit of the entire finite-height zero kernel with the arithmetic sum and these explicit factors.

### Grouped zero limit and the resulting first formula

Set \(d=r-\tfrac12\). Equations (43)–(46) resolve each zero kernel into a coefficient times \(K_h(a,\log x)\) and two shifted vertical integrals for \(\rho_\pm=\frac12\pm i\alpha_\nu\). The shifted real parts are \(a+r-\Re\rho_\pm\in[a+r-1,a+r]\). For fixed \(\nu\) their two shifted endpoints go to opposite infinities and each normalized integral tends to 1 by cutting out a symmetric segment and applying (28),(30). Its limiting paired contribution is
\[
 W_\nu(x,r)=\frac{2d-2x^{-d}(d\cos(\alpha_\nu\log x)-\alpha_\nu\sin(\alpha_\nu\log x))}
                    {d^2+\alpha_\nu^2}.
\]
For \(x>1\), (47)–(49) compare the full finite-height contour sum against \(\sum_{\beta_\nu\le h}W_\nu\). The exact difference has the ordinary Perron error times the bounded paired coefficient sum, two growing shifted-end errors for \(\beta_\nu\le h\), and the full tail for \(\beta_\nu>h\). The growing terms in (50) are majorized, after using the fixed margin \(b_*=a+r-1>0\), by a constant times
\[
 \sum_{\beta_\nu\le h}\frac{1}{\beta_\nu(h+\beta_\nu)}
 +\sum_{\beta_\nu\le h}\frac{1}{\beta_\nu(b_*+h-\beta_\nu)}.
\]
For the second sum, split at \(h/2\) and absorb the larger denominator into \(h^{-1}\), leaving either reciprocal-ordinate or shifted endpoint harmonic sums over fixed-length cells. Both are \(O(\log^2h/h)\). For the infinite tail (51)–(54), the paired reciprocal squares converge, and the remaining shifted integrals are bounded by
\[
 C\sum_{\beta_\nu>h}\frac{1}{\beta_\nu(b_*+\beta_\nu-h)}.
\]
The portion \(h<\beta_\nu\le2h\) is \(O(\log^2h/h)\) by the same harmonic sum, and the remainder is \(O(\log h/h)\) by integrability of \(\log v/v^2\). A tie at \(h\) is harmless because \(b_*>0\). These arguments reproduce the source estimates at the level needed for convergence. The companion estimates may use conjugacy of the **whole sums** since the \(\beta_\nu\)-cutoff is invariant under \(\alpha_\nu\mapsto\bar\alpha_\nu\). A single term generally is not its companion's conjugate for complex \(\alpha_\nu\). The tails and finite sums thus all tend to zero. This is the growing-\(H\) control alleged absent in the older controversy. It is present explicitly on pp. 286–292, and the full article predates the 1896 allegation. [Scoped historical comparison](../mangoldt_grouped_remainder_corpus_round4.md)

Equation (55) is
\[
 \Lambda_0(x,r)=\frac{1-x^{1-r}}{r-1}
 -\tfrac12(\log\pi+\gamma_E)
 +\sum_{m\ge1}\frac{r+2m x^{-r-2m}}{2m(r+2m)}
 -\sum_\nu^{\mathrm{ord}}W_\nu(x,r).
\]
The real-parameter exceptions are the removable terms already identified. A reexpression at nonexceptional real \(r\) has the familiar terms \(x^{1-r}/(1-r)-\sum_\rho^{\mathrm{ord}}x^{\rho-r}/(\rho-r)+\sum_m x^{-2m-r}/(r+2m)-\zeta'(r)/\zeta(r)\). At \(r=1/2\), \(W_\nu=2\sin(\alpha_\nu\log x)/\alpha_\nu\); at \(x=1\) the terms vanish, and replacing \(x\) by \(1/x\) gives convergence for \(0<x<1\). Formula (57) subtracts the leading \(2x^{-d}\sin(\alpha_\nu\log x)/\alpha_\nu\) from general \(W_\nu\), leaving absolutely summable \(O_{x,r}(\beta_\nu^{-2})\) terms. This proves ordered convergence for all real \(r\), \(x>0\); the stated formula for the arithmetic side remains for \(x>1\). A partial block at a tied ordinate changes the partial series by \(O_{x,r}(\log h/h)\), so arbitrary tie breaking in the prescribed nondecreasing order is allowed. Formula (56) shows a logarithmic blow-up as \(x\downarrow1\) in the limiting sine sum even though its terms at 1 vanish. At prime powers its limiting arithmetic piece jumps. Therefore uniform convergence on sets that straddle such a point is excluded. The source's broad p. 293 wording about uniform convergence of the **absolute remainder** is safely read locally in \(x\). A literal global claim on the whole positive axis would be false: at \(r=0\), each remainder summand contains a nonzero \(\sqrt{x}\) times a sinusoidal combination of the complex carriers and is unbounded as \(x\to\infty\). For a real carrier this follows by periodicity in \(\log x\); for a nonreal carrier one exponential dominates and its coefficient is nonzero since \(\Re\alpha_\nu>12\). Uniform convergence would require the summands to tend uniformly to zero. Local uniformity by \(\beta_\nu^{-2}\) majorization and uniformity for \(r\) on compact intervals at fixed \(x\) suffice for the subsequent steps.

At \(r=0\), use \(\zeta(0)=-1/2,\ \zeta'(0)=-\frac12\log(2\pi)\) to combine the constants. Equation (58) is the ordered Chebyshev formula
\[
 \psi_0(x)=x-\sum_\rho^{\mathrm{ord}}\frac{x^\rho}{\rho}
              -\log(2\pi)-\tfrac12\log(1-x^{-2}).
\]
The printed footnote about the sign of \(\zeta(0)\) in the collected-works commentary is distinct from the explicit-formula constant correction on p. 299.

### Integrated prime powers and the Li branch

The second weighted function is \(f(x,r)=\sum_{p^m\le x}'p^{-mr}/m\), with the same midpoint convention. At fixed \(x>1\), \(-\partial_r f(x,r)=\Lambda_0(x,r)\). Equations (59)–(60) integrate (55) on finite \(r\)-intervals. Equation (57) gives uniform convergence there by extracting the common convergent sine sum. For the upper limit \(+\infty\) in (61), the two remaining zero-integral pieces after extracting that sine sum are dominated by reciprocal squares or cubes times integrable polynomials in \(r\) multiplied by \(x^{-r}\). Indeed \(|(r-\tfrac12)^2+\alpha_\nu^2|\gg (r-\tfrac12)^2+\beta_\nu^2\) uniformly for real \(r\), since \(|\gamma_\nu|\le1/2\) and \(\beta_\nu>12\). That is a direct justification of this interchange.

The first line of (61) integrates the real function
\[
 A_x(v)=\frac{x^{1-v}}{1-v}+\sum_{m\ge1}\frac{x^{-v-2m}}{v+2m}-\frac{\zeta'(v)}{\zeta(v)}.
\]
Its apparent singularities cancel: at 1 the meromorphic derivative has the pole residue \(-1\), and at a negative even integer it has the zero residue \(+1\). The paired spectral integral equals \(-\sum_\nu [\operatorname{Ei}((\rho_+-r)\log x)+\operatorname{Ei}((\rho_--r)\log x)]\) in the branch defined below. The real non-spectral integral is evaluated in three regimes. For \(r>1\), use the absolutely convergent elementary integrals in \(y\ge x\) and \(\log\zeta(r)\), giving (62). For \(-2<r\le1\), on \([r,a]\) with \(a>1\) remove the pole by \(\log((v-1)\zeta(v))\), real since the product is positive there after filling the pole, and then Frullani's integral for \(\log(a-1)\). This gives (63), and the limit is valid at \(r=1\). For \(r\le-2\), \(-2(\lambda+1)<r\le-2\lambda\), use in (65) the real positive function
\[
 Z(v)=\frac{(v-1)\zeta(v)}{(v+2)\cdots(v+2\lambda)}
\]
on \([r,\infty)\) with all the indicated simple zeros removed. Positivity follows from reality, nonvanishing after cancellations, and positivity for \(v>1\). The series left after subtracting the first \(\lambda\) trivial factors has kernel \(y^{-r-2\lambda-1}/((y^2-1)\log y)\) on \(y\ge x\). The finite subtractions produce integrals of \((e^{-(r+2m)u}-e^{-u})/u\) over \((0,\log x)\), and the logarithm contributes \(\log Z(r)\). These are (66)–(67), with no logarithm of an uncancelled zero even at \(r=-2\lambda\).

For \(r=0\), (64) on **printed p. 299** gives the corrected constant \(-\log2\), obtained from \(\log((r-1)\zeta(r))\), alongside the compensating trivial-zero kernel and the ordered pair of trigonometric integrals. On p. 300 the nonzero leading integral is identified with the Cauchy principal value \(\int_{-\infty}^{\log x}e^u\,du/u=\operatorname{Li}(x)\). On pp. 300–301 the variable for the complex continuation is \(w=\rho\log x\) in \(\mathbb C\setminus(-\infty,0]\). It is not the principal logarithm of the point \(x^\rho\) after exponentiating. For \(\Im w>0\), the horizontal primitive from \(-\infty+i\Im w\) to \(w\) of \(e^z/z\) takes \(+i\pi\); for \(\Im w<0\) it takes \(-i\pi\); and at \(w>0\) it takes the real principal value. An indentation or boundary-value computation supplies the signs. The constants cancel for \((\frac12+i\alpha_\nu)\log x\) and \((\frac12-i\alpha_\nu)\log x\), since the imaginary arguments have opposite signs even if \(\alpha_\nu\) is complex. Expanding the paired horizontal integrands and substituting \(u=-v\log x\) gives precisely the two trigonometric integrals in (64), with their common increasing-index order. Consequently for every \(x>1\),
\[
 J_0(x)=\operatorname{Li}(x)-\sum_\nu^{\mathrm{ord}}
      [\operatorname{Ei}((\tfrac12+i\alpha_\nu)\log x)
       +\operatorname{Ei}((\tfrac12-i\alpha_\nu)\log x)]
 +\int_x^\infty\frac{dy}{y(y^2-1)\log y}-\log2 .
\]
Here \(J_0=f(x,0)\), a weighted prime-power count, from which midpoint prime counts follow by finite Möbius inversion at the same endpoint convention. Equation (64)'s footnote explicitly calls its printed \(-\log 2\) replacement for Riemann's \(\log\Xi(0)\) an already known correction. This is consistent with the prior Genocchi record. No historical priority for a new correction follows. [Riemann whole advocate comparison](analytic144_riemann1859_whole_advocate.md)

## Closing logical scope

The memoir proves the ordered zero count and explicit formulas unconditionally, taking the Hadamard factorization and classical analytic inputs as dependencies. No RH, simplicity, unweighted arbitrary permutation, or uniformity over jump locations is used or obtained. The closing pp. 304–305 discuss the conditional prospect of \(\psi_0(x)\sim x\) under RH or under a fixed narrowing of the zero strip, and describe why the author considers Cahen's rectangle argument insufficient. A modern proof of the stated conditional consequence can shift a once-integrated Perron contour to a fixed line strictly between the postulated zero bound and 1, then remove the smoothing by positivity. Merely taking \(x\to\infty\) term by term in the pointwise ordered (58) would be insufficient. The article does not claim an unconditional PNT. The objections to the distinct Cahen paper are recorded as von Mangoldt's historical assertions and would require separate primary comparison before attributing a particular error to Cahen.

## Printed-page reading ledger

| Printed page | Main step read and checked |
| --- | --- |
| 255 | Title, 1894 extract footnote, Hadamard input and Riemann's two leading count terms. |
| 256 | Global count bound and promise of convergence of the ordered paired Li series. |
| 257 | RH open, Piltz acknowledgement, imaginary-axis exclusion and multiplicity ordering. |
| 258 | Paired product (1), argument principle, setup of displaced line. |
| 259 | Positive angular increments and rectangle endpoint angle. |
| 260 | Angle lower bound (4), right-line factorization and continuous logs. |
| 261 | Stieltjes \(\log\Gamma\) expansion, branch and remainder. |
| 262 | Argument \(F\), Euler log and signed gamma error. |
| 263 | Reduction of the no-zero-through-12 assertion to (17). |
| 264 | Numerical exclusion, comparison at 13 and Jensen. |
| 265 | Local inclusive count and differentiated main argument. |
| 266 | Completion of the local bound and statement of global count. |
| 267 | Exact paired arctangent expansion and the inclusive \(H\) split. |
| 268 | \(S_1,S_2\), (22), bins at the ordinate endpoint. |
| 269 | Harmonic bound by fixed-width local counts. |
| 270 | \(S_1\) completion and near-tail \(S_2\) setup. |
| 271 | \(S_2\) summand bound, splitting its near and far parts. |
| 272 | \(S_2\) tail integral and combination of all argument errors. |
| 273 | (27), density corollary and first-ordinate upper enclosure. |
| 274 | Enclosure completion and kernel lemma (28)–(29) setup. |
| 275 | Oscillatory segment estimates and first Perron bound. |
| 276 | Residue and horizontal estimates for the left rectangle. |
| 277 | Right rectangle and three Perron limits, definition of \(L(n)\). |
| 278 | Dirichlet insertion and uniform prime-series tail bound. |
| 279 | Midpoint \(\Lambda_0(x,r)\) and gamma/zero log differentiation. |
| 280 | (39)–(40a), pole exception and gamma telescoping. |
| 281 | (41), shifted gamma tails with cutoff before height. |
| 282 | Gamma limit and \(r=-2m\) removable term. |
| 283 | (42) and the two shifted resolvents in (43). |
| 284 | Fixed-index limits and explicit \(W_\nu\) in (46). |
| 285 | Ordered convergence theorem and exact partial sum (47). |
| 286 | Four remainder pieces in (49). |
| 287 | Paired coefficient bound and the two near sums of (50). |
| 288 | Fixed-width bins and endpoint block. |
| 289 | Harmonic upper integrals, companion by conjugation, tail opening. |
| 290 | Reciprocal-square and shifted remote estimate. |
| 291 | Shifted tail near and far sums and conjugation. |
| 292 | Ordered parametric formula (55), \(r=1/2\) specialization. |
| 293 | (56)–(57), \(x=1\) behavior and local uniformity issue. |
| 294 | \(\zeta(0),\zeta'(0)\), Chebyshev formula (58), Cahen comparison begins. |
| 295 | Fixed-\(x\), compact-\(r\) uniformity and midpoint definition of \(f(x,r)\). |
| 296 | Integration and recombination (59)–(60). |
| 297 | Integrating to infinity in (61) and \(r>1\) evaluation. |
| 298 | (62), pole cancellation and Frullani step for \(-2<r\le1\). |
| 299 | (63)–(64), exact \(-\log2\) and historical footnote. |
| 300 | Real principal value and choice of slit continuation variable. |
| 301 | Explicit three branch prescriptions and pair identity. |
| 302 | Completion of the Riemann comparison and cancellation polynomial \(Z\). |
| 303 | Individual integrals and regrouping (66). |
| 304 | General last regime (67), conditional asymptotics and Cahen opening. |
| 305 | Specific contour objection and dated closing. |
