# Independent review of the weighted BGSTB density condition

2026-11-17. I checked the [proposal](../../proposals/independent_campaigns/threshold62_weighteddensity_bgstb.md), both pending theorem records, the earlier horizontal-denominator reconstruction, and arXiv:2306.04799v1 (2.5), (4.1)–(4.2), Lemmas 6–7, and §§6–7. I find the weighted condition, the far-pair bound and the stated conditional 61.7% simple-zero consequence valid on those inputs. I also give a closed endpoint in the height reduction and a separate implication using the authors’ later horizontal-multiplicity argument. These checks establish neither historical priority nor a finding about the journal issue copy. [Primary preprint](../../sources/analytic/2306.04799.pdf)

## Independent pair bound

Take \(L=\log T\), and regard the zeros with \(0<\gamma\le T\) as a multiset. For each ordered far pair \((\rho,\rho')\), label a member of maximal \(m=L|\beta-1/2|\) as the outer zero, and write \(d=L|\beta-\beta'|\), \(v=L(\gamma-\gamma')\). The cutoff is \(d\ge1\), so \(1\le d\le2m\le L\); in particular the outer zero satisfies \(m\ge1/2\), including equality. The absolute value of \(w(\rho-\rho')\) is uniformly bounded since the real part of \(4-(\rho-\rho')^2\) is at least \(3+(\gamma-\gamma')^2\). Lemma 6(b) thus yields a majorant \(C e^d/(d^2+v^2)\).

With \(q=2m-d\ge0\), one has \(m/d\le(1+q)/2\). For nonnegative \(v^2\), the ratio \((1+m^2+v^2)/(d^2+v^2)\) is bounded by the larger of \(1\) and \((1+m^2)/d^2\), hence by \(1+(1+q)^2/4\). Multiplying by \(e^{-q}\) gives a uniform constant. Thus the replacement \(C e^{2m}/(1+m^2+v^2)\) is valid before summation.

For each labeled outer copy, (2.5) puts \(O(L)\) partners within \(|\gamma-\gamma'|<1\), with uniform treatment near \(0\) and \(T\) by intersecting with the allowed window. A two-sided unit shell \(j\le|\gamma-\gamma'|<j+1\) has \(O(L)\) partners and denominator at least \(L^2j^2\). The total for a fixed outer zero is therefore
\[
\sum_{\gamma'}\frac1{1+m^2+L^2(\gamma-\gamma')^2}
\ll \frac{L}{1+m^2}+\frac1L
\ll\frac{L}{1+m^2}.
\]
The last absorption uses \(m\le L/2\). Ordered pairs can map at most two-to-one to an outer copy and a partner copy. The reflection \(\beta+i\gamma\mapsto1-\beta+i\gamma\) preserves \(m\), \(\gamma\) and multiplicity, so after partner extension the left outer sum equals the right outer sum. Both multiplicity factors are preserved. Absolute convergence is automatic for the finite sums. This gives \(|S(T)|\ll L\,M_T\), where \(M_T=\int e^{2y}/(1+y^2)\,d\mu_T(y)\) and \(\mu_T\) is the inclusive right-side counting measure. No step replaces unit-window control by microscopic occupancy.

## Endpoint and quantifier tests

Put \(a=1/2\) and \(B=L/2\) and \(G(y)=e^{2y}/(1+y^2)\). For a single atom \(x\in[a,B]\),
\[
G(x)=G(a)+\int_a^B G'(y)\mathbf1_{\{y\le x\}}\,dy.
\]
The indicator includes equality, which changes no Lebesgue integral. It does matter for the value \(D_T(a)\) multiplying \(G(a)\). Summing the identity proves \(M_T=G(a)D_T(a)+\int_a^B G'(y)D_T(y)\,dy\). An atom at \(a\) contributes solely to the first term; a hypothetical atom at \(B\) contributes through both terms and requires no extra boundary term. The actual zeros have \(\beta<1\), so \(B\) has no mass.

Write \(r_T(y)=e^{2y}D_T(y)/T\). The boundary coefficient is exactly \(1/(1+a^2)=4/5\). For \(y\ge a\),
\[
G'(y)e^{-2y}=\frac{2-2y/(1+y^2)}{1+y^2},
\qquad
1\le 2-\frac{2y}{1+y^2}\le2.
\]
It follows with explicit constants that
\[
\tfrac45 r_T(a)+\int_a^B \frac{r_T(y)}{1+y^2}\,dy
\ \le\ M_T/T\ \le\
\tfrac45 r_T(a)+2\int_a^B \frac{r_T(y)}{1+y^2}\,dy.
\]
This is necessity and sufficiency for the displayed nonnegative majorant to be \(o(TL)\). For \(S(T)\) itself it is only a sufficient condition. No lower bound on the actual signed sum is used.

Under the original uniform little-o up to \(y_*=(\sigma_*-1/2)L\), the expression below \(y_*\) tends to zero because the weight is integrable. Above \(y_*\) the stated uniform upper bound gives \(O(1/L)\). Fixed-\(\sigma\) little-o does not control a moving \(\sigma=1/2+y/L\). If \(D_T(a)=o(T)\), then \(r_T(y)\le e^{2R}D_T(a)/T\) for \(y\in[a,R]\). Thus weighted tail tightness is exactly the remaining condition after imposing the inclusive boundary count. A global polynomial envelope of degree \(p<1\) suffices with pointwise decay in the scaled variable, by extension by zero beyond \(B\) and dominated convergence.

The proposal’s atomic tests pass.

- An atom of mass \(\lfloor T\rfloor\) at \(a\) contributes order \(T\) to \(M_T\) while the integral vanishes.
- Set \(Y=L^{1/4}\) and put \(\lfloor T e^{-2Y}(1+Y^2)\rfloor\) atoms at \(Y\). Then \(r_T(y)=e^{2y}D_T(a)/T\) for \(a\le y\le Y\), and zero above. It tends to zero uniformly on fixed compact sets of \(y\), and at every fixed real part \(1/2<\sigma\le1\) the profile is eventually empty. The unweighted integral divided by \(L\) is \(O((1+Y^2)/L)\). Nevertheless \(M_T/T\to1\).
- Reducing that atom count to \(\lfloor T e^{-2Y}\rfloor\) gives \(M_T/T\to0\) while \(r_T(Y)\to1\). This separates the weighted premise and the uniform little-o among counting profiles. It does not prove the two conjectural assertions different for the actual zeta zeros.

[Guth–Maynard Theorem 1.2 and (1.4)](../../sources/analytic/2405.20552.pdf) count the inclusive region at both signs of height. Symmetrizing the abstract profile across height signs changes only a constant. Both exponents are \(>1+c\) throughout the occupied right-side region \(1/2\le\sigma\le1/2+Y/L\), for some fixed \(c>0\) when \(T\) is large. Above that range the profile vanishes. One may fill past the \(o(T)\) exceptional count with line mass to match \(N(T)\asymp T\log T\). At \(\sigma=3/4\) the exponents are \(5/9\) and \(15/26\), respectively, compared to \(1/2\), with gaps \(1/18\) and \(1/13\). The first gap alone would not show failure of the weighted inference, but the moving profile does. It is a test of the inequalities and supplies no simultaneous, all-height zeta distribution or example contradicting Lemma 7.

## Height and partner refinements

For the optional height localization use precisely the uniform \(N(\sigma,X)\ll X^{2(1-\sigma)}\) input on \(\sigma_*\le\sigma\le1\), with \(\sigma_*=25/32+\eta<1\). It is the weaker big-O form of what v1 asserts as (6.5). Bourgain's [journal record](https://doi.org/10.1155/S107379280000009X) and [rendered article](https://www.scribd.com/document/816345203/On-large-values-estimates-for-Dirichlet-polynomials-and-the-density-hypothesis-for-the-Riemann-zeta-function), pp. 133 and 145–146, confirm the stated threshold, with the argument in the new range reducing to separated-ordinate bounds. I did not re-audit every reduction in Bourgain's proof. A bound stated with a strict ordinate cutoff transfers to the inclusive count by \(X\mapsto X+1\). If a source estimate uses a strict real-part threshold, \(\sigma\mapsto\sigma-1/\log X\) keeps a fixed margin for large \(X\) and only costs a constant in this power bound. This argument needs a uniform constant in a slightly larger fixed-margin range. Neither the full weighted criterion nor the high-window condition conditional on this input depends on proving such uniformity anew.

With \(X=T^\theta\), the low-height first block in fact satisfies the stronger bound
\[
O(X\log X\cdot G(y_*))
=O\!\left(T^{\theta+2\sigma_*-1}/L\right).
\]
Indeed \(G\) is monotone and \(y_*\asymp L\). This makes the argument valid also at \(\theta=2(1-\sigma_*)\), where the bound is \(O(T/L)\). For the second block use the exact lower-endpoint term at \(y_*\) and the same layer integral. Each is bounded by \(C T L^{-2}e^{-2(1-\theta)(B-y)}\) at the corresponding \(y\), and the integral is \(O(T/L^2)\) for fixed \(\theta<1\). If \(\beta=\sigma_*\), assign it to either block or harmlessly overcount it in both. The proof can therefore remove positive ordinates \(\gamma\le T^\theta\) for \(0<\theta\le2(1-\sigma_*)\). For \(\theta=3/8\) this even includes \(\eta=1/32\). The original strict-\(\theta\) record is valid as stated.

For the optional partner model use \(u=\sqrt{1+m^2}/L\). In the ball of radius \(u\) the denominator reciprocal is at most \((1+m^2)^{-1}\). In the annulus \(2^{j-1}u<|\Delta\gamma|\le2^ju\), it is at most \(4\cdot2^{-2j}/(1+m^2)\). Thus the proposal's dyadic occupancy majorant is correct with all endpoints covered. Unit-window control gives \(Z_T(\gamma,r)\ll L(1+r)\), and \(\sum_{j\ge0}2^{-2j}(1+2^ju)\ll1\) as \(u\ll1\). A small occupancy bound would need further information. The model includes copies at equal height and includes all partners after extending the charged far pairs.

## Direct simple-zero consequence, and a separate horizontal consequence

Lemma 7 and near-pair positivity yield
\[
\limsup\frac{\sum_{\rho\ {\rm distinct}} m_\rho^2}{N(T)}
\le C_K=\frac{\widehat K(0)+2\int_0^1\alpha\widehat K(\alpha/(2\pi))\,d\alpha}{2\pi K(0)}.
\]
Every distinct zero of order \(m_\rho\) supplies \(m_\rho^2\) coincident ordered pairs. Applying \(\mathbf1_{\{m=1\}}\ge 2m-m^2\) gives a simple-zero fraction anywhere in the strip of at least \(2-C_K\) in the liminf. The Montgomery–Taylor numerical input from §7 gives \(2-C_K\approx0.61748\), so for sufficiently large \(T\) the conditional bound is at least 61.7%. The source’s last printed digits vary slightly from independent quadrature, without affecting 61.7%. The original diagonal argument says nothing on its own about the count on \(\beta=1/2\) or the intersection of simplicity and critical-line location. The count of simple OR critical-line zeros is a different union and must not be described as the count of simple zeros.

There is a separate stronger consequence with additional use of horizontal grouping, as in [BGSTB follow-up v3 §§2, 6](../../sources/witness62_bgstb_followup/2501.14545v3.pdf). Under the full weighted premise, the inclusive endpoint count gives \(D_T(a)=o(T)\). By reflection, the good strip \(|\beta-1/2|<1/(2L)\) contains \(N_{\rm good}(T)=N(T)-2D_T(a)=N(T)-o(T)\) copies. If the premise is imposed only at high heights, apply the checked height reduction first. For each height \(g\), let \(H_{\rm good}(g)\) be the number of good copies at that height. Any two good copies at the same height form a near pair, and (4.2), with nonnegative \(j(\alpha)\operatorname{sech}\alpha\), gives \(K(iu)\ge K(0)\) by \(\cos(iu\alpha)=\cosh(u\alpha)\). Hence \(\sum_g H_{\rm good}(g)^2\le(C_K+o(1))N(T)\). A group with \(H_{\rm good}=1\) is necessarily simple and critical by reflection invariance and retention of every copy at a good point, even when other, out-of-strip zeros share its ordinate. Thus there are at least \(2N_{\rm good}-\sum_g H_{\rm good}(g)^2\) simple critical points. This separately transfers the \(2-C_K\) bound to the intersection.

In the union count, a good copy outside the union is an off-line multiple copy, forcing \(H_{\rm good}\ge4\) because its reflected point is also good and has the same order. The number of good copies missing from the union is at most \(\sum_{H_{\rm good}\ge4}H_{\rm good}\le(\sum_g H_{\rm good}^2-N_{\rm good})/3\). The union, counted with multiplicity, then has conditional asymptotic lower bound \((4-C_K)/3\approx0.87249\). These last two deductions use the authors’ horizontal-grouping method plus the checked weighted premise; they are distinct from the statement of the original §7 argument and from the separate finite-window 88.93% union results.

## Repository version check

The [Kyushu repository PDF rendering](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7377443/7377443.pdf) has a cover giving the 2024 Acta Arithmetica citation, but its author-layout first page carries the actual arXiv:2306.04799v1 stamp dated 7 June 2023. Its internal pp. 9–10 reproduce the original v1 §6 displays. It is not evidence about typeset journal pp. 357–376. Direct local download of that endpoint returned an empty body; the indexed PDF rendering displayed the cover, stamp and formulas. No hash of a journal version is claimed.
