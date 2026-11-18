# Combined weighted-density frontier

The global fixed-slab saving reaches every compact interval inside \((3/4,1)\) using Palomar's separate density curve. Pintz Corollary 4 independently covers fixed compact intervals inside \((7/8,1)\). Ye adds a short-height result. With a separate near-one input, the combined estimates give an \(o(T)\) weighted sum over a single interval of length \(T^b\) at height comparable to \(T\) for every fixed \(2/3\le b<13/15\). The corresponding full-height moment is still open under these inputs. Two sequences in one all-height counting model give distinct failures of the global implication. A separate model reaches the short-window endpoint. This is a reconstruction from the specified source inequalities and the locally compiled Palomar declarations. [Pintz source](../../sources/latest62_analytic2/2310.04544.pdf) · [Ye source](../../sources/latest62_density_frontier/2610.15989.pdf) · [Palomar build log](../../sources/palomar_formal62/solution_build_20261117T221703875104Z.log)

## Weighted criterion and the fixed global region

Use \(L=\log T\), \(a_0=1/2\), \(B=L/2\) and \(G(y)=e^{2y}/(1+y^2)\). Let \(\mu_T\) be the positive counting measure of right-hand zero copies with \(0<\gamma\le T\) and \(y=L(\beta-1/2)\in[a_0,B]\). Its inclusive tail is \(D_T(y)=\mu_T([y,B])\). Define \(r_T(y)=e^{2y}D_T(y)/T\) and \(M_T=\int G\,d\mu_T\). The retained-horizontal-denominator reduction bounds the absolute BGSTB far-pair contribution by \(O(L M_T)\) using the source unit-window \(O(L)\) bound and same-height reflection. Summing \(G(x)=G(a_0)+\int_{a_0}^xG'(y)\,dy\) over copies gives
\[
\frac{M_T}{T}=\frac45r_T(a_0)+
\int_{a_0}^B \left[2-\frac{2y}{1+y^2}\right]\frac{r_T(y)}{1+y^2}\,dy.
\]
The bracket is in \([1,2]\). Thus the endpoint term and weighted tail are exactly the requirements for this nonnegative majorant. The signed far-pair sum may have further cancellation. A contribution assigned to a slab means the selected zero of maximal horizontal displacement lies in its reflection or in the slab itself. [BGSTB source, §6](../../sources/analytic/2306.04799.pdf) · [Weighted criterion review](director_weighted_density_round6.md)

For a fixed compact interval \(J=[u,v]\subset(1/2,1)\), suppose a source gives inclusive counts \(N(\sigma,T)\ll_{\sigma,\varepsilon}T^{E(\sigma)+\varepsilon}\) at all fixed thresholds in \(J\), and put
\[
\Delta_J=\inf_{\sigma\in J}\{2(1-\sigma)-E(\sigma)\}.
\]
When \(\Delta_J>0\), partition \(J\) into a fixed finite mesh of width at most \(\varepsilon/4\). At any cell \([s,t]\), the count at \(s\), with loss \(\varepsilon/2\), times the maximum weight at \(t\) gives
\[
\ll_{J,\varepsilon}L^{-2}T^{E(s)+2t-1+\varepsilon/2}
\ll_{J,\varepsilon}L^{-2}T^{1-\Delta_J+\varepsilon}.
\]
A singleton uses its own threshold. The constant is the sum of finitely many admissible constants, chosen before \(T\). This includes real-part endpoints and requires no continuum of uniform bounds. It also works with the pointwise minimum of finitely many known exponents on their ranges by selecting the estimate at each mesh point.

- Pintz Corollary 4 has \(E_P(\sigma)=(1-\sigma)/(4\sigma-3)\) for \(3/4<\sigma<1\). With \(\eta=1-\sigma\), the gap is \(\eta(1-8\eta)/(1-4\eta)\), positive exactly for \(0<\eta<1/8\). At \(7/8\) the displayed exponent equals \(2(1-\sigma)\), so Pintz alone gives no endpoint power saving. [Reconstructed Pintz estimate](prefix_formula62_pintz_bgstb_slab.md)
- Palomar's compiled \(\texttt{full_curve}\) and \(\texttt{uniform_away_boundary}\) have \(E_R(\sigma)=3(1-\sigma)/(2\sigma)\) strictly above \(3/4\). The gap is \((1-\sigma)(4\sigma-3)/(2\sigma)>0\) on that open interval. The right branch can be used at \(7/8\), where it gives \(3/14<1/4\). The separate uniform \(39/17\) coefficient has no strict density-hypothesis gap. The exact curve value at \(3/4\) is \(9/16\) and the Guth–Maynard value there is \(5/9\). Both exceed \(1/2\). Taking a threshold to the right of \(3/4\) omits zeros exactly at the join. [Palomar source and count semantics](latest62_palomar39_density_semantics.md) · [Compiled scope](formal62_palomar39_compiled_statement_scope.md) · [Guth–Maynard source](../../sources/analytic/2405.20552.pdf)

Pintz can give a stronger quantitative saving within the common right-hand range. The two exponents agree at \(\sigma=9/10\), since \(1/(4\sigma-3)=3/(2\sigma)\) there. Palomar's right branch is smaller below \(9/10\) and Pintz's is smaller above it. The two eps-loss inequalities by themselves only remove fixed compact slabs. Even a uniform positive-\(\varepsilon\) inequality does not by itself permit an unquantified \(\varepsilon(T)\) at a moving boundary.

Either of the following separately stated inputs extends the removal to all \(\beta\ge 3/4+\delta\) for every fixed \(\delta>0\).

1. If the uniform no-power-loss bound \(N(\sigma,T)\ll T^{2(1-\sigma)}\) on \([25/32+\eta,1]\) is taken from the stated BGSTB (6.5), with fixed \(\eta>0\), the layer formula starting at \(y_*=(25/32+\eta-1/2)L\) gives \(M_{\beta\ge 25/32+\eta}/T\ll 1/L\). The fixed slab below \(25/32+\eta\) uses the preceding mesh. This uses the no-power-loss reading of the published input as quoted by v1. The full underlying Bourgain derivation has its separate review scope. [Upper-input audit](ratio62_weighteddensity_bgstb.md)
2. Take the classical uniform near-one estimate \(N(1-\eta,T)\ll T^{A\eta^{3/2}}L^C\) from Halász–Turán as quoted in Pintz (1.14), and the Vinogradov–Korobov width \(\nu(T)=cL^{-2/3}(\log L)^{-1/3}\) as stated in Guth–Maynard §13.1. Choose a fixed \(\eta_0>0\) in the validity range of the former with \(A\sqrt{\eta_0}\le1\), so for \(\nu(T)\le\eta\le\eta_0\), \(r_T((1/2-\eta)L)\ll L^C e^{-\eta L}\). The tail vanishes beyond the zero-free boundary. The squared denominator is \(\gg L^2\) throughout this piece. Its boundary and integrated terms are \(O(L^{C-2}e^{-\nu(T)L})=o(1)\), since the integral of \(e^{-\eta L}\) with respect to \(y\) is \(O(e^{-\nu(T)L})\). Cover the interval up to \(1-\eta_0\) by the fixed mesh. The uniform log-loss form of the classical result supplies the moving-threshold estimate. [Pintz (1.14)](../../sources/latest62_analytic2/2310.04544.pdf) · [Guth–Maynard §13.1](../../sources/analytic/2405.20552.pdf)

## What Ye's windows add

Let a short interval start at real \(U\asymp T\). Use the same weight with scale \(L=\log T\). Theorem 1.1 with a fourth moment gives a strict threshold count in a \(U^a\) window, for fixed \(0<a\le1\) and \(3/5\le\sigma<1\), with exponent
\[
F_a(\sigma)=(1-\sigma)\max\left\{\frac{15a}{3+5\sigma},\,2\max(a,2/3)\right\}.
\]
For \(a=3/5\) the layer \(2\sigma-1+F_a(\sigma)\) increases on \([3/5,1)\). It equals \(2\sigma-1+9(1-\sigma)/(3+5\sigma)\) through \(3/4\), with derivative \(2-72/(3+5\sigma)^2\ge0\), and equals \(1-2(1-\sigma)/3\) above \(3/4\). The low range through \(3/5+1/L\) costs \(O(T^{4/5}/L)\) by the unit-window count and the maximum weight. In the remaining range use a mesh of width \(1/L\) and a strict threshold one mesh step below the left endpoint. The uniform estimate and the Lipschitz exponent cost a bounded factor in the exponent. The number of cells is \(O(L)\), and the squared denominator is \(\gg L^2\). Thus for fixed \(v\in[3/4,1)\), the same upper cutoff as in the earlier review has the sharper bound
\[
M_{[U,U+U^{3/5}],\,\beta\le v}(T)
\ll_{v,\varepsilon} T^{4/5}/L+T^{1-2(1-v)/3+\varepsilon}/L.
\]
In particular the same bound summed over \(O(T^k)\) such windows is \(o(T)\) for \(k<2(1-v)/3\). Pintz covers \([v,1-d]\) across all heights for fixed \(v>7/8\) and \(1-d\ge v\). Palomar allows any fixed \(v>3/4\). The same transition covers endpoints by overlap or strict-threshold shift. [Ye Theorem 1.1 and prior window review](director_ye_corollaries_round8.md)

For \(2/3\le b\le1\) use Ye Theorem 1.2 directly on a \(U^b\) interval. Below any fixed \(v\in(3/4,4/5)\), write its exponent as \(b\mathcal B(\sigma)\), with
\[
\mathcal B(\sigma)=
\begin{cases}
3(1-\sigma)/(2-\sigma),&1/2\le\sigma\le7/10,\\
15(1-\sigma)/(3+5\sigma),&7/10\le\sigma\le v.
\end{cases}
\]
The expressions agree at \(7/10\). The first weighted branch \(2\sigma-1+b\mathcal B(\sigma)\) is increasing since \(2-3b/(2-\sigma)^2>0\) there, and the second is convex since \(\mathcal B''(\sigma)>0\). Its maximum on \([1/2,v]\) is therefore
\[
E_b(v)=\max\left\{\frac25+\frac{9b}{13},\;2v-1+\frac{15b(1-v)}{3+5v}\right\}.
\]
At \(v=3/4\), the second term is \(1/2+5b/9\), equal to \(53/54\) at \(b=13/15\). For each fixed \(b<13/15\) one can choose a sufficiently small fixed \(v-3/4>0\) so that \(E_b(v)<1\). A fixed sufficiently fine mesh gives \(O(T^{E_b(v)+\varepsilon})\) for the cutoff sum. Use a strictly lower real-part counting threshold in each cell and the Lipschitz modulus of \(\mathcal B\) to absorb it in the exponent budget. A first cell near \(1/2\) uses the total local count \(O(T^b L)\) and an arbitrarily small fixed weight exponent, which fits the same budget since \(E_b(v)\ge b\). This covers closed real-part endpoints and arbitrary comparable starts. It also permits \(O(T^k)\) windows whenever \(k+E_b(v)<1\). Adding the all-height upper tail \(\beta\ge v\) from either separate input above gives unrestricted \(o(T)\) on one such interval, or on a union with the same restriction on \(k\). With just the fixed-slab estimates the same statement holds below \(1-d\) for each fixed \(d>0\). [Ye Theorem 1.2](../../sources/latest62_density_frontier/2610.15989.pdf)

Covering a whole dyadic block costs \(O(T^{1-b})\) windows. From Theorem 1.2 the resulting count exponent is \(1-b+b\mathcal B(\sigma)\), minimized at \(b=1\) because \(\mathcal B(\sigma)\le1\). The branch exponent is at least \(2(1-\sigma)\) for \(\sigma\le3/4\), including its join at \(7/10\). Theorem 1.1's direct fourth-moment bound cannot improve this covering conclusion. In \([3/5,1)\), \(1-a+F_a(\sigma)\) is the maximum of affine functions of \(a\) with nonpositive slopes and is minimized at \(a=1\). There the slope multiplying \(1-\sigma\) is at least 2. In particular a bound that is \(o(T)\) uniformly per window cannot be summed over all windows without a stronger, summable error or an estimate on their aggregate. The right-tail inputs supply neither a gain over the whole lower strip nor weighted tightness as \(y\) leaves fixed compact sets.

## Simultaneous all-height counting controls

The following is a single positive counting measure on a zero-like multiset at all heights. Its purpose is to test implications of density inequalities, including their uniform start and height quantifiers. Set a large fixed \(t_0\). For \(t\ge t_0\) define two right-hand real-part curves and their counting rates by
\[
\begin{split}
\beta_c(t)&=1/2+(\log t)^{-3/4},&
\lambda_c(t)&=(1+(\log t)^{1/2})e^{-2(\log t)^{1/4}},\\
\beta_j(t)&=3/4+1/\log t,&
\lambda_j(t)&=(e^{-2}/32)t^{-1/2}(\log t)^2 .
\end{split}
\]
For each \(i\in\{c,j\}\), put one simple right-hand point at \(\beta_i(t)+it\) whenever \(\int_{t_0}^t\lambda_i(u)du\) crosses a positive integer. Add its same-height reflected point and their negative-height conjugates. Choose \(t_0\) so that \(\beta_c(t_0)<0.55\), \(\beta_j(t_0)<0.77\) and both rates are decreasing and less than 1. Then each sequence has at most two integer crossings per closed unit interval. Critical-line fillers at distinct ordinates within the successive unit intervals can make the positive-ordinate count
\[
T(2\pi)^{-1}\log(T/(2\pi))-T(2\pi)^{-1}+O(\log T).
\]
Indeed the difference of consecutive integer parts of the displayed main term grows like \((2\pi)^{-1}\log n\), eventually exceeding the total prescribed count of reflected and right-hand copies in each interval. Choose fillers to attain that increment, adjusting a bounded initial count if needed. Thus the unit-window estimate and the overall counting scale both hold. The off-line count is \(o(T)\) and all points can be simple, so the model also meets the separately reported lower bounds on critical-line and simple proportions as numerical count conditions.

The near-line sequence respects Ye's strict counts for \(\sigma\ge3/5\) automatically. In a window \([U,U+U^a]\) it has at most \(1+U^a\lambda_c(U)\) right copies. If \(1/2<\sigma\le\beta_c(U)\), then
\[
\mathcal B(\sigma)=1-\frac{2(\sigma-1/2)}{3/2-(\sigma-1/2)}
\ge1-\tfrac32(\log U)^{-3/4},
\]
so \(1+U^a\lambda_c(U)\ll U^{a\mathcal B(\sigma)}\). The same applies to Ye's strict threshold \(1/2\) since the line fillers are omitted. For its full-height inclusive count at \(\sigma>1/2\), let \(X\) be the smaller of \(T\) and the last height allowed by \(\beta_c(X)\ge\sigma\), with zero count when the constraint has no solution. The count is \(O(X\lambda_c(X))\), since \((t\lambda_c(t))'\sim\lambda_c(t)\). The same estimate at \(a=1\) gives \(O(X^{\mathcal B(\sigma)})\), which extends to \(T\) by \(X\le T\) and positivity of the exponent. This matches Palomar's first branch and the quoted Guth–Maynard and uniform-\(39/17\) bounds. At \(\sigma=1/2\) the inclusive \(O(T\log T)\) count fits every fixed positive power loss.

The right-join sequence has at most \(1+O(U^{a-1/2}(\log U)^2)\) right copies per window. At an occupied threshold \(\sigma\le\beta_j(U)\), Ye's Theorem 1.2 has \(\mathcal B(\sigma)\ge 5/9-O(1/\log U)\). The first branch of the maximum in Theorem 1.1 also supplies at least \(5a/9-O(1/\log U)\) on its applicable thresholds. Since \(a-1/2\le 5a/9-1/18\) for \(a\le1\), both local envelopes hold with their prescribed constants. In the inclusive global count take \(X\) to be the smaller of \(T\) and the last height allowed by \(\beta_j(X)\ge\sigma\). The count is \(O(X^{1/2}(\log X)^2)\). On the allowed thresholds the exact Palomar exponent is at least \(1/2-O(1/\log X)\), including the interval strictly to the right of \(3/4\). Thus this sequence meets even a single \(C_\varepsilon\) for the full piecewise curve, since \((\log X)^2\ll_\varepsilon X^\varepsilon\). On its occupied range the uniform \(39/17\) and both Guth–Maynard exponents are bounded below by \(1/2\) for \(t_0\) sufficiently large. Both sequences give zero at all thresholds \(\sigma\ge25/32\). In particular they satisfy the separately cited high-range bound on its range. For Pintz Corollary 4, the count vanishes for \(\sigma\ge0.77\) and its exponent is above \(1/2\) on \((3/4,0.77)\), where only the join sequence can occur.

Their contributions have sharp nonzero limits. For fixed \(T\), the cumulative counts of the right-hand marks differ from \(\int_{t_0}^t\lambda_i\) by at most 1. Integration by parts against the decreasing weight \(G(L(\beta_i(t)-1/2))\) bounds the discretization error by \(O(G(L(\beta_i(t_0)-1/2)))=o(T)\). Both sequences lie above \(a_0/L\) in displacement for \(t\le T\) and \(T\) large. The early range \(t\le\sqrt T\) is \(o(T)\) for the near-line sequence by its size and \(\beta_c(t_0)<0.55\). For the join sequence its count there is \(O(T^{1/4}L^2)\) and its weight is \(O(T^{1/2+2/\log t_0})\), again giving \(o(T)\). On \(\sqrt T\le t\le T\) substitute \(t=uT\). The near-line integrand after division by \(T\) is
\[
\frac{1+(\log t)^{1/2}}{1+L^2(\log t)^{-3/2}}
\exp\bigl(2(L-\log t)(\log t)^{-3/4}\bigr).
\]
It tends to 1 at every fixed \(u>0\). The fraction is at most 1 and the exponential is at most \(u^{-1/2}\) for all large \(T\) in this range. For the join sequence the integrand after substitution and division by \(T\) tends to \((1/2)u^{-1/2}\). Indeed the squared denominator is asymptotic to \(L^2/16\), \(e^{2L/\log t}\to e^2\) and \((\log t)/L\to1\). Uniformly on the retained range this integrand is \(O(u^{-1/2})\). Dominated convergence gives 1 from each sequence, hence \(M_T/T\to2\). The contribution from \(\beta_c\) escapes in scaled displacement near \((\log T)^{1/4}\), though \(D_T(a_0)=o(T)\) and \(r_T\to0\) uniformly on fixed compact intervals. The join sequence escapes through \(\beta=3/4+O(1/\log T)\) on the right of the strict join. Replacing that sequence by \(\beta_j=3/4\) and removing the factor \(e^{-2}\) in \(\lambda_j\) gives the same limit at the exact endpoint, with even weaker counting requirements. The models do not impose the explicit formula, the signed pair kernel asymptotic or any Dirichlet-sum trigger.

The same inequalities permit a single-window failure at the exponent \(b=13/15\). For this separate profile put \(X_n=4^n\) and distribute \(\lfloor X_n^{3/5}(\log X_n)^2/25\rfloor\) equally spaced right copies at \(\beta=7/10\) in \([X_n,X_n+X_n^{13/15}]\). Use the same reflection and line-fill procedure. A window \([U,U+U^a]\) meets at most a bounded number of comparable blocks and the count from each is
\[
O\left(1+(\log U)^2\min\{U^{3/5},U^{a-4/15}\}\right).
\]
For \(a\le13/15\) one has \(a-4/15\le9a/13\), and for \(a\ge13/15\) one has \(3/5\le9a/13\). For every occupied threshold, both applicable Ye envelopes are at least \(9a/13\), leaving room for the logarithm under their fixed positive power loss. The global count is \(O(T^{3/5}(\log T)^2)\), which fits all the displayed global envelopes on the occupied thresholds. The high-range inequalities have empty counts. At \(T=X_n+X_n^{13/15}\), the weight in that single window is asymptotic to \(25X_n^{2/5}/(\log X_n)^2\), so the window moment divided by \(T\) tends to 1 along this subsequence. Thus the threshold \(13/15\) is sharp as an implication of the displayed count envelopes, including their logarithm-absorbing loss.

## Remaining arithmetic input and the separate proportion theorem

With an accepted upper-tail input, choose a fixed small \(\delta>0\) and put \(Y_\delta=(1/4+\delta)L\). It suffices to study the measure restricted to \(a_0\le y<Y_\delta\), with its own inclusive tail \(D_T^{<}(y)\) and \(r_T^{<}(y)=e^{2y}D_T^{<}(y)/T\), extended by zero above the cutoff. A concrete sufficient next lemma is \(D_T^{<}(a_0)=o(T)\) plus the bound
\[
\frac1Y\int_Y^{2Y}r_T^{<}(y)\,dy\ll Y^{1-\kappa}
\quad (Y\ge1)
\]
for some fixed \(\kappa>0\), with a constant independent of \(Y,T\). The contribution of \([Y,2Y]\) to the weighted integral would be \(O(Y^{-\kappa})\). Summing over dyadic \(Y\) gives uniform tail decay and the endpoint condition gives local compact decay. A direct arithmetic proof of the weighted tail, or an independent signed far-pair argument, would also close this particular gap. The combined estimates above do not furnish the dyadic bound.

Dong–Wang–Wang–Zhang supply a pointwise inverse implication from a large specific Dirichlet sum to a positive local zero count. It contributes no upper-density inequality for this argument. The separately inspected Simple673 theorem has an actual-zeta simple-critical-line numerator and a denominator counted with multiplicity. Its proof wrapper uses the window and Gram-energy layers and the eight-point local inequality. The BGSTB weighted-density premise is absent from that route. The local-window and model conclusions here do not alter the Simple673 count or its recorded proof and replay scope. [Dong inverse audit](witness62_dong_inverse_phase.md) · [Actual-count scope](839_statement_grounding_round2.md) · [Simple673 source](../../sources/formal_round2/839-v1/lean/Simple673/Main.lean)
