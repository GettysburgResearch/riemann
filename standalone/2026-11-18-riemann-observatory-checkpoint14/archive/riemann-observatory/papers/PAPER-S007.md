# PAPER-S007 — Hardy,1914: infinitely many critical-line zeros

**Identity.** G. H. Hardy, *Sur les zéros de la fonction ζ(s) de Riemann*, Comptes rendus hebdomadaires des séances de l'Académie des sciences158(1914),1012–1014; séance du6avril1914. Note transmitted by J. Hadamard. Footnote2,p1012, records prior communication to the London Mathematical Society on12March1914. DOI not established in this track. Original language:French.

**Primary source actually read.** Original printed-page facsimiles, Internet Archive item `comptesrendusheb158acad`: https://archive.org/download/comptesrendusheb158acad/page/n1019.jpg (printed1012), https://archive.org/download/comptesrendusheb158acad/page/n1020.jpg (printed1013), https://archive.org/download/comptesrendusheb158acad/page/n1021.jpg (printed1014; Hardy's note ends before the following chronometry article). All three originals visually read completely on2026-11-17. Bibliographic page numbers were verified from the printed page headers, not assumed from digital leaf indices. Full item: https://archive.org/details/comptesrendusheb158acad . Wikisource facsimile-linked transcription is a discovery aid, not the controlling mathematical text: https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_séances_de_l’Académie_des_sciences,_tome_158,_1914.djvu/1014 .

**Audit scope.** Level0 verified, Level1 whole three-page original read. Local Level2 reconstruction below checks contour normalization, the endpoint limit by a modern theta argument, the eventual-sign limit passage and final moment contradiction. No full historical audit of the cited Cahen/Mellin and Bohr–Marcel Riesz summability sources; no independent Level3 of the whole paper. Do not count this as a complete paper-wide Level2 orLevel3 audit.

## Exact main theorem and limits

There are infinitely many distinct real t such that ζ(1/2+it)=0. Equivalently, for every T>0 there exists t>T on the critical line with ζ(1/2+it)=0 (using conjugation and unboundedness of isolated zeros). The theorem is unconditional. It does not give positive limiting proportion, a linear lower bound for N_0(T), simplicity of the zeros, or RH. Those require later work.

The source uses ξ(s)=s(s−1)Γ(s/2)π^(−s/2)ζ(s)/2 and Ξ(t)=ξ(1/2+it), real and even for realt. Its moment variable is Ξ(2t), so factor2 must be preserved.

## Original proof architecture

1. **Inverse Mellin and theta series(p1012).** Begin with exp(−y)=(2πi)^(−1)∫_(k−i∞)^(k+i∞)Γ(u)y^(−u)du, Re y>0,k>0. Summing at n²y with k>1/2 gives the theta function F(y)=1+2∑n≥1exp(−n²y). The printed exponent in the short formula resembles `n`; the integration-variable reading y^(−u) is required by the formula and is made explicit here rather than propagated as a new mathematical assertion.
2. **Contour move(p1012,eq1).** Shift from Reu=k>1/2 to Reu=1/4, crossing the ζ(2u) pole at u=1/2 and no gamma pole. Its residue gives sqrt(π/y). Using the completed xi function produces

       F(y)=1+sqrt(π/y)−(2/π)∫_R(π/y)^(1/4+it) Ξ(2t)/(1/4+4t²)dt.

   The branch has |argy|<π/2. Gamma decay beats the vertical factor y^(−it), justifying the move with standard polynomial ζ bounds; these bounds are explicit dependencies.
3. **Angular parameter(p1012–1013,eq2).** Put y=πexp(iα), |α|<π/2, q=exp(−y). Evenness of Ξ gives

       I_0(α)=∫_0∞(e^(αt)+e^(−αt)) Ξ(2t)/(1/4+4t²)dt
             =πcos(α/4)−(π/2)e^(iα/4)F(y).

4. **Even moments(p1013,eq3).** Differentiate2p times inα, p≥0 integer, retaining t^(2p) on the left:

       I_p(α)=∫_0∞(e^(αt)+e^(−αt))t^(2p) Ξ(2t)/(1/4+4t²)dt
             =(-1)^p π/4^(2p) cos(α/4)−d^(2p)/dα^(2p)[(π/2)e^(iα/4)F(y)].

   The source scan explicitly contains t^(2p); the Wikisource formula encountered in this execution omitted it. This is a transcription-quality issue, not an error in Hardy's printed equation.
5. **Theta boundary lemma(p1013,§2).** As α↑π/2, q→−1 on the specified tangent path. The theta term and every fixed derivative needed ineq3 tend0. Hardy invokes Bohr–Marcel Riesz summability and the analytic function(1−2^(1−2s))ζ(2s), whose negative-integer values vanish. The underlying summability theorem is not proved in this three-page note and was not read in this track.
6. **Assume eventual sign(p1013–1014,§3).** If Ξ(2t)>0 for t>T>1, the finite interval converges by dominated convergence and the nonnegative tail by monotone convergence asα↑π/2. Thus the endpoint moment exists and

       I_p(π/2)=(-1)^p π16^(−p)cos(π/8).

   This endpoint equality is deduced *under the eventual-sign hypothesis*. It must not be casually quoted as an unconditionally convergent improper integral.
7. **Contradiction(p1014,eq4–6).** Take podd so the total moment is negative. The positive tail is at most K T^(2p), where K is independent ofp. But continuity and positivity on[2T,2T+1] give a lower bound δK_1(2T)^(2p), with δ,K_1>0 independent ofp. Division byT^(2p) contradicts arbitrarily large oddp. If the eventual sign is negative use evenp and reverse the sign. Finitely many real zeros would imply eventual constant sign, so there must be infinitely many.

## Independent check of the endpoint theta lemma

This is a modern replacement of the cited summability step, not a claim that Hardy wrote this derivation. Let ε=π/2−α>0 and w=y−iπ=π[sinε+i(cosε−1)]. Then Rey>0, Rew>0 and

    F(y)=∑_(n∈Z)(−1)^n e^(−wn²)
        =sqrt(π/w)∑_(m∈Z) exp[−π²(m+1/2)²/w]

by Poisson summation for the complex Gaussian. Use the analytic square root inRew>0. Along this path

    Re(1/w)=cot(ε/2)/(2π) ~1/(πε).

The smallest |m+1/2| is1/2. Every fixed number ofw orα derivatives produces at most additional powers ofε^(−1) and summation-index factors. The transformed Gaussian still supplies exp(−c/ε), so every required derivative tends0. Standard locally uniform convergence of the transformed Gaussian series justifies differentiation. This checks the analytically delicate boundary limit without pretending a termwise substitution q=−1 is allowed in the original theta series.

## Reuse, obstacles and concrete follow-up

The proof turns endpoint-flatness of a transform into an alternating sequence of moments, incompatible with eventual sign. This is a rigorous oscillation mechanism. A natural transfer project is to specify another completed L-function with a theta/Mellin representation and determine whether an analogous boundary-flatness point exists. The necessary statement is explicit: prove that a chosen boundary deformation kills all fixed derivatives of the nontrivial theta term while leaving alternating moments with a finite compact-support growth bound. Functional-equation symmetry alone does not supply such a point.

The principal barrier to a quantitative zero count is that arbitrarily high moments only contradict eventual sign; they do not locate sign changes in uniformly controlled short intervals. A meaningful incremental next step is a localized kernel with a proved tail bound and sign control, not simply repeating the high-moment argument at largerp.
