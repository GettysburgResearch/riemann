# Priority review of the two-scale tightness lemma

18 November 2026. The full upper modulus follows from the classical Garsia–Rodemich–Rumsey inequality after interpolation and a row-dependent choice of gauge. The lower bound is a rescaling of the shrinking-triangle example already given by Billingsley. The literature passages checked here give both ingredients. The explicit two-parameter equivalence for arbitrary deterministic grids is a useful formulation for the arithmetic application, but this targeted search establishes neither an earlier verbatim statement of that equivalence nor priority for its formulation. [Proposed lemma](uniform85_two_scale_tightness_lemma.md) · [Independent proof audit](analytic86_two_scale_skeptic.md)

## Upper modulus from the original GRR inequality

Garsia and Rodemich reproduce the original Garsia–Rodemich–Rumsey result in Theorem 1.2, p. 70, with gauge hypothesis (1.3) on p. 69 and equations (1.7) and (1.8) on p. 70. For a continuous function on the unit interval, the power case of (1.8) bounds an increment of length \(r\) by a constant depending only on \(p\) times
\[
 B^{1/p}\int_0^{r}u^{-2/p}\,dg(u),\qquad
 B=\iint\left|\frac{f(x)-f(y)}{g(|x-y|)}\right|^p dx\,dy.
\]
The gauge is continuous, positive and strictly increasing away from zero, and the displayed integral must converge. The almost-everywhere formulation in the paper yields a bound everywhere for a continuous path by continuity. Section 5 of the same work gives an improved power-case inequality, but Theorem 1.2 already suffices for the two-scale rates. [Garsia and Rodemich, *Monotonicity of certain functionals under rearrangement* (1974), Theorem 1.2](https://www.numdam.org/item/10.5802/aif.507.pdf#page=5)

Fix one row, abbreviate \(w=(\epsilon/A)^{1/b}\) and \(\lambda=\epsilon/w\), and let \(a'=\min(a,p)\), \(b'=\min(b,p)\). The grid-to-polygonal interpolation proof in Uniform85 supplies continuous-time increments satisfying \(E|Z(t)-Z(s)|^p\ll H(|t-s|)\), where
\[
 H(u)=u^{a'}+\epsilon\min\{1,(u/w)^{b'}\}.
\]
Put \(J(d)=\int_0^d (H(u)/u)^{1/(p+1)}\,du/u\) and define
\[
 g(u)^p=u^{1+1/(p+1)}H(u)^{p/(p+1)},\qquad g(0)=0.
\]
The gauge is continuous and strictly increasing, locally absolutely continuous, and its derivative satisfies \(g'(u)\ll g(u)/u\) almost everywhere with a row-independent constant. This follows from \(0\le u H'(u)\le \max(a',b')H(u)\) away from the corner at \(w\). The two integrands satisfy
\[
 \frac{H(u)}{g(u)^p}=\left(\frac{H(u)}u\right)^{1/(p+1)}\frac1u,
 \qquad
 u^{-2/p}g'(u)\ll\left(\frac{H(u)}u\right)^{1/(p+1)}\frac1u .
\]
They are integrable at zero for each row because \(a',b'>1\).

Partition \([0,1]\) into \(N=\lfloor1/\delta\rfloor\) intervals of common length \(d=1/N\), so that \(\delta\le d\le2\delta\). For a block \(I\), let \(B_I\) be the double integral of the normalized increments over \(I^2\) in the original coordinates. Tonelli gives \(E B_I\ll d J(d)\), so the energy is finite almost surely. Applying GRR to the block rescaled to \([0,1]\) uses normalized energy \(d^{-2}B_I\) and gauge \(g(du)\). The integration kernel contributes \(d^{2/p}\) after substitution, which cancels the normalization. Thus \(\operatorname{osc}(Z,I)\ll B_I^{1/p}J(d)\). Any pair at separation at most \(\delta\) can be joined using at most two block oscillations. Summing their \(p\)-th moments and using \(Nd=1\) gives
\[
 \|\omega(Z,\delta)\|_p\ll J(d)^{1+1/p}.
\]
The integral from the \(u^{a'}\) term is \(O(d^{(a'-1)/(p+1)})\) at scale \(d\). For the second term, \(H(u)/u\) contributes \(\lambda(u/w)^{b'-1}\) below \(w\) and \(\lambda w/u\) above \(w\). Both powers integrate geometrically toward \(w\). Substituting \(d\le 2\delta\) and absorbing fixed scale factors proves the same estimate as Uniform85,
\[
 \|\omega(Z,\delta)\|_p\ll
 \delta^{(a'-1)/p}+\lambda^{1/p}\min\{1,(\delta/w)^{(b'-1)/p}\}.
\]
The GRR argument uses the deterministic interpolation first. The pointwise grid estimate alone is not a continuous-time GRR energy hypothesis. The audited dyadic proof is shorter and avoids the gauge construction.

## Billingsley’s criterion and spike

The 1968 first edition of Billingsley’s *Convergence of Probability Measures* gives the required tightness criterion for continuous laws in Theorem 8.2, p. 55. Tight values at zero and vanishing modulus probabilities in the \(\delta\downarrow0\), \(\limsup_n\) order are exactly what the upper estimate supplies when \(\lambda_n\to0\). Theorem 12.3, pp. 95–96, instead assumes a common continuous nondecreasing clock \(F\) and a power exponent \(q>1\) in a tail bound whose time dependence is \(|F(t)-F(s)|^q\). Its direct moment specialization with a linear clock applies when a common power bound is available. There is no such direct reduction from the scalar envelope throughout the two-scale tightness regime. For example, let \(w_n=e^{-n^2}\), \(\epsilon_n=w_n/n\), and \(A_n=\epsilon_n/w_n^b\), disregarding finitely many rows to ensure \(A_n\ge1\). Then \(\lambda_n=1/n\), while \(\epsilon_n/w_n^q\to\infty\) for every \(q>1\). Even a common nonlinear clock cannot dominate this full scalar envelope by a fixed power: summing over disjoint intervals of length \(w_n\) would require clock variation at least a constant times \(\lfloor1/w_n\rfloor\epsilon_n^{1/q}\), which diverges. This comparison is about scalar domination at all distances. An individual process may satisfy stronger bounds. [Billingsley, first edition, pp. 55 and 95–96](https://djvu.online/file/vaaIHv9IWlVeK)

In §12, Problem 9, p. 103, Billingsley places a unit triangle on one of \(n\) equally likely disjoint subintervals of length \(1/n\). The resulting continuous paths are not tight, and the example shows failure at the critical time exponent 1. The two-scale adaptation chooses grid pitch \(d_n\asymp w_n\) with \(d_n\ge w_n\) along any subsequence where \(\lambda_n\ge c>0\). A zero grid with one uniformly chosen spike of height \(v\) has every fixed pair’s increment moment \(O(v^p w_n)\). Both grid envelopes are at least \(\epsilon_n\) at those pair spacings. Taking \(v\) sufficiently small for the prescribed \(C>0\) and using \(w_n\le\epsilon_n/c\) verifies both bounds. The spike’s fixed height and shrinking width prevent tightness. For \(b\le p\), this example can even be imposed at all continuous times by interpolation: at most four spike indices affect an increment, and their slopes are bounded by \(v/d_n\). This gives \(O(v^p d_n\min(1,(h/d_n)^p))\), which is bounded by a constant times both envelopes after reducing \(v\). For \(b>p\), the all-continuous-time analogue of the fine bound would instead force each row to be constant by subdivision and Minkowski. The stated grid obstruction still applies for that range. [Billingsley, first edition, §12, Problem 9](https://djvu.online/file/vaaIHv9IWlVeK)

## Scope and source access

- With positive fixed \(C\), the equivalence quantifies over all deterministic grids and laws satisfying the hypotheses for a given parameter sequence. Failure of \(A_n\epsilon_n^{b-1}\to0\) supplies a counterexample even on a vanishing-mesh grid, with zero finite-dimensional limit. This gives no necessity for a particular process or prescribed grid.
- The polygonal result allows arbitrary deterministic meshes. A continuous limit for the associated steps additionally needs mesh tending to zero or maximum adjacent jumps tending to zero in probability for the transfer used here. Tightness itself supplies no finite-dimensional law comparison.
- The exact-expression and near-term searches covered additive-error Kolmogorov bounds, two increment bounds, grid interpolation and generalized GRR. Hahn and Klass’s *Sample-Continuity of Square-Integrable Processes* is a relevant lead, but the theorem pages were unavailable through the journal/archive links attempted here. The 1970–71 GRR journal preview exposed its introduction only. The theorem attribution above uses the full 1974 archival paper, which explicitly restates the original result, and the 1968 monograph’s actual theorem and exercise passages. These are targeted passage readings. [Hahn and Klass journal entry](https://doi.org/10.1214/aop/1176995797) · [GRR journal preview](https://iumj.s3-us-west-2.amazonaws.com/abstracts/20046_abs.pdf)

## Internal correction record

Prime94's Round 13 review found that the initial gauge used exponent \(1+2/p\) on \(u\) in \(g(u)^p\). The pre-correction file SHA-256 was `f491b58cd7e77fd1f3b256d995dc2e9afa6b587ddad4d415e747c8d17c585e96`. With \(g(u)^p=u^\gamma H(u)^{p/(p+1)}\), the energy density is \(H(u)^{1/(p+1)}u^{-\gamma}\), and the modulus integrand is bounded by a constant times \(H(u)^{1/(p+1)}u^{(\gamma-2)/p-1}\). Equating the powers of \(u\) gives \(\gamma=1+1/(p+1)\), establishing the two integrand comparisons used above. The correction is to this note's application of GRR. The source theorem, its attribution and the independent dyadic proof of the grid modulus are unaffected.
