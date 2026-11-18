# The disputed growing sum: a local reconstruction

Agent `/root/corpus`,2026-11-17. Source: von Mangoldt1894 extract, actually read in Laugel's1896 French translation, printed61–78, all18pages and all displayed formulas inspected. Canonical work record PAPER-H405. German1894 text and full1895 version have not yet been compared. This note reconstructs the grouped-limit step on translation72 using the local zero count explicitly cited there. It does **not** accept de la Vallée Poussin's1896 appendix70 allegation as an independently verified error.

## 1. An exact abstract lemma

Fix x>1 and real r. Let α_j=γ_j+iη_j, counted with multiplicity, satisfy γ_j≥γ0>0, |η_j|≤1/2, and

\[
 \#\{j:m\le\gamma_j<m+1\}\le C\log(2+m)\quad(m\ge0). \tag{M1}
\]

Choose a>0 with a+r>1, and put

\[
 \beta_{j,\pm}=\tfrac12-r\pm i\alpha_j,
 \quad
 P_h(\beta)=\frac1{2\pi i}\int_{a-ih}^{a+ih}\frac{x^s}{s-\beta}\,ds,
 \quad
 J_h(\beta)=\frac1{2\pi i}\int_{a-ih}^{a+ih}\frac{x^s}{s(s-\beta)}\,ds.
\]

All β have real part in [−r,1−r], strictly left of the contour; none equals0 since |Im β|=γ_j≥γ0. The identity

\[
 J_h(\beta)=\frac{P_h(\beta)-P_h(0)}{\beta}
\]

is exact. Let

\[
 W_j(x,r)=\sum_{\pm}\frac{x^{\beta_{j,\pm}}-1}{\beta_{j,\pm}},
 \qquad
 I_h=\sum_j\bigl[J_h(\beta_{j,+})+J_h(\beta_{j,-})\bigr].
\]

For finite h the sum defining I_h converges absolutely and uniformly under the finite integral. Indeed

\[
 \frac1{s-\beta_{j,+}}+\frac1{s-\beta_{j,-}}
 =\frac{2(s+r-1/2)}{(s+r-1/2)^2+\alpha_j^2}
\]

is O_h(γ_j^−2) on that finite contour for all sufficiently large j, and (M1) gives Σγ_j^−2<∞. The finitely many remaining terms cause no difficulty.

Then, as h→∞ through arbitrary positive heights,

\[
 \sum_{\gamma_j\le h}W_j(x,r)-I_h
 =O_{x,a,r,C,\gamma_0}\!\left(\frac{\log^2(2+h)}h\right). \tag{M2}
\]

Thus if I_h has a finite limit, the increasing-height paired zero series converges to that same limit. This is the exact implication needed for the source's grouped-limit step. The limit of I_h in the application is obtained separately from the logarithmic derivative, elementary/trivial-zero terms and pointwise Perron inversion; it is not supplied merely by (M1).

## 2. Uniform kernel bounds, not individual summand limits

Write u=log x>0. For β=b+iγ the substitution s−β=z gives

\[
 P_h(\beta)=\frac{x^\beta}{2\pi}
 \int_{-h-\gamma}^{h-\gamma}
 \frac{e^{u(a-b+it)}}{a-b+it}\,dt.
\]

Here a−b belongs to the fixed compact positive interval [a+r−1,a+r]. Integration by parts on either ray gives a uniform bound C/(1+v) for the oscillatory tail beyond v≥0. One can verify this directly: for v≥1, differentiate1/(a−b+it), whose derivative is O(t^−2), and use the boundary term O(v^−1); for0≤v≤1, the bounded central interval plus the same ray bound gives O(1). The full infinite vertical integral equals1 before multiplication by x^β, by elementary contour closure to the left; equivalently it is source equations16/18 after the shift.

Consequently, with constants independent of j,h,

\[
 |P_h(\beta)-x^\beta|
 \le C_x\left[\frac1{1+h-|\gamma|}+\frac1{1+h+|\gamma|}\right]
 \quad(|\gamma|\le h), \tag{M3}
\]

and

\[
 |P_h(\beta)|\le\frac{C_x}{1+|\gamma|-h}
 \quad(|\gamma|>h). \tag{M4}
\]

For γ<0 reflect the integration interval; the same estimates hold. Also P_h(0)=1+O_x(1/h). These bounds remain bounded even when h lies extremely close to a zero ordinate, because the contour's real separation a−b stays positive. Replacing1+|h−γ| by |h−γ| would destroy that necessary uniformity.

## 3. Sum the entire remainders

For γ_j≤h, subtract W_j from the two J terms. By (M3), |β_j,±|≥γ_j and P_h(0)=1+O(1/h), the sum of absolute errors is bounded by a constant times

\[
 \sum_{\gamma_j\le h}\frac1{\gamma_j}
 \left[\frac1{1+h-\gamma_j}+\frac1{1+h+\gamma_j}+\frac1h\right].
\]

From (M1), Σ_(γ≤h)1/γ=O(log²(2+h)). For γ≤h/2, the bracket is O(1/h). For h/2<γ≤h, use1/γ≤2/h, split into unit intervals of h−γ and use (M1). The resulting harmonic sum is O(log h), multiplied by the local O(log h) count. Thus this whole below-h error is O(log²h/h).

For γ_j>h, handle the P_h(β)/β terms by (M4). Their absolute sum is bounded by

\[
 C\sum_{\gamma_j>h}\frac1{\gamma_j(1+\gamma_j-h)}.
\]

For h<γ≤2h, (M1) and a harmonic sum give O(log²h/h). For γ>2h, compare with Σ_(γ>2h)γ^−2=O(log h/h). The remaining P_h(0)/β terms **must be paired** before summation:

\[
 \frac1{\beta_{j,+}}+\frac1{\beta_{j,-}}
 =\frac{1-2r}{(1/2-r)^2+\alpha_j^2}=O_r(\gamma_j^{-2}).
\]

Their tail is O(log h/h). This proves(M2). The proof tracks all growing sums; it does not infer their limit from individual summand limits. Any tie within an equal ordinate contributes at most O(log h/h), since |W_j|=O_(x,r)(1/γ_j) and the local multiplicity is O(log h), so increasing-index order within such ties has the same limiting sum.

## 4. Relation to the historical claim

The source's §I theorem2, translation66–67, bounds the number of α_j with real parts in [h−k,h+k] by k log h for tan1≤k≤h−4. Taking a fixed k=2 implies (M1) for large heights; finitely many low zeros are harmless. The completed-zeta symmetry bounds |η_j|≤1/2, and the source even provides a positive lower γ bound. Its equations14–16 give the kind of oscillatory kernel estimates used above. The printed72 sentence explicitly invokes both sets of inputs to control the grouped terms.

Therefore de la Vallée Poussin's printed70 assertion that the extract merely forgot H is **not confirmed by this reading**. There is a rigorous local reconstruction from the very inputs that the extract cites. A compressed announcement may omit estimates that are required for a fully expanded proof; that differs from an invalid implication. The German1894 wording still requires comparison, and the entire explicit-formula proof is not declared independently verified here. Subsequent original-source inspection of the full1895 article is recorded below.

The bound(M2) is a derived reconstruction with novelty unassessed, provided for independent adversarial review. It is not a newly discovered error or a claim that every interchange elsewhere in either historical paper is justified. Fixed x>1 is essential in this proof; no uniform convergence across prime-power jumps is inferred. Pointwise Perron inversion gives half-weights at jumps and can converge to a discontinuous function.


## 5. Original1895 proof inspected after reconstruction

Only after deriving(M2), original German282–292 were inspected, along with255,280,305. PAPER-H406 gives identity/hash and partial-reading scope. The author asks on285 whether sum and limit can be interchanged; Eq49 on286 gives the exact grouped decomposition. On287 he bounds a partial sum independently of H. On288–289 local-zero-count partitions control the finite sum Σ_(βν≤h)1/[βν(b+h−βν)] by O(log²h/h); on290–291 the corresponding upper tail Σ_(βν>h)1/[βν(b+βν−h)] is bounded similarly. The conclusion is on292. Thus the full publication contains precisely the grouped estimates whose absence would invalidate a naive termwise argument.

Source notation is αν=βν+iγν, bν=a+r−1/2+γν. Since |γν|≤1/2, the separation belongs to[a+r−1,a+r], strictly positive. For uniform denominator estimates use b_*=a+r−1. The audit's compact-positive-interval assumption makes this dependence explicit, without an allegation that historical shorthand invalidates the argument.

The last page305 dates the work2June1894; first-page footnote255 links the extract published19July1894. The full1895 publication predates Vallée1896. It is not a later repair responding to that criticism. Current evidence: compressed announcement citing analytic inputs; full expanded proof published before the accusation; no confirmed growing-sum error in the inspected portion. No whole51-page technical-audit claim.


## 6. Original1894 announcement checked

The original German891–892 is now available in `sources/history_round4/mangoldt1894_german_pp883-896.pdf` (articlePDF9–10). Both pages were read visually. The displayed remainder identity is on891; on892 the text explicitly invokes formulas14–16 and the second theorem of SectionI to show that each grouped term, except the first, vanishes. This agrees with the French translation72. Thus no later translator insertion explains away the source citation: it was in the1894 announcement itself. The announcement compresses the estimates; the full1895 publication gives them before the1896 accusation. The original German full14pages are not claimed read.

Bibliographic correction from original896: issue/session19July1894, presentation14June, actual distribution footer26July. Earlier records treating19July as an exact publication day are superseded by this distinction. Original14-pageextract/hash and bound-source provenance are retained; no new mathematical work is counted for the extra language manifestation.


## Independent review checkpoint

`/root/analytic_frontier/semantic_skeptic` independently challenged(M2)–(M4), including complexα, fixed positive contour margin, cutoff ties and the four growing-sum pieces; no failure found under the stated assumptions. Their scoped review is `audits/adversarial_reviews/mangoldt_grouped_remainder_semantic_round4.md`. Selected originalGerman1894, Frenchtranslation and original1895passages were also visually checked. This validates the local reconstruction, not all input proofs or the entire historical papers.
