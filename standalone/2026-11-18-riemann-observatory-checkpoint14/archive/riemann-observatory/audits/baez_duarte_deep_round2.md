# Technical audit: Báez-Duarte math/0205003v1

**Subsequent dependency update:** the shrinking-epsilon estimate left incomplete in this initial audit has now been reconstructed by the original Perron route, with RH-only constants tracked, in [baez_uniform_dependency_round2.md](baez_uniform_dependency_round2.md). References below to that estimate as uncompleted describe the earlier audit checkpoint, not a surviving suspected gap. Whole-paper promotion awaits the parent’s independent adjudication.

Auditor: equivalences agent.2026-11-17. Stable work ID PAPER-E001. Scope: complete nine-page preprint read again, main theorem reconstructed in detail, every displayed step checked for domains and limit order, corollary reconstructed, quantitative proposition separated from its external uniform input. Independent reviewer: audits/adversarial_reviews/baez_fixed_epsilon_skeptic.md. No RH proof or disproof, historical novelty, or material error in the main theorem is claimed.

**Audit decision:** retain whole-work Level1. Theorem1.1 and Corollary3.1 receive scoped Level2 technical reconstruction, conditional on the explicitly listed standard external analytic inputs. Proposition3.1's shrinking-epsilon Möbius estimate is not fully independently verified from its original antecedent. Therefore a complete-paper Level2 promotion would overstate this audit.

## Sources, versions and access

- Inspected source: https://arxiv.org/abs/math/0205003v1, submitted2002-05-01, manuscript dated28March2002,9 printed pages. Private PDF/text: sources/equivalences/baez_duarte.pdf/.txt. Existing source hash is in PAPER-E001 record. Line references below use that existing `pdftotext -layout` file and are auxiliary to printed page/equation references.
- Related earlier version: https://arxiv.org/abs/math/0202141v2, submitted15Feb2002 and revised18Feb2002. Downloaded here for version comparison, not counted as a second work. Its original theorem is the same strengthening; the later0205003 adds the quantitative construction.
- Published identity verified from BDIM/Geodesic metadata: **A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis**, Rendiconti Lincei, serie9,14(2003),no.1,5–11, MR2057270. Canonical notice: https://geodesic.mathdoc.fr/item/RLIN_2003_9_14_1_a0/. Direct published-PDF attempts at the BDIM links returned503/timeouts in this run. No assertion about corrections in the journal PDF is made.
- Correct original antecedent: Balazard–Saias, **Notes sur la fonction zeta de Riemann,1**, Adv.Math.139(1998),310–321, DOI10.1006/aima.1998.1760. Its pp.315–316 Lemmas1–2 and Perron proof were inspected in the reproduced primary text at https://www.academia.edu/114375539/Notes_sur_la_fonction%CE%B6de_Riemann_1. The direct Elsevier PDF/API endpoints were inaccessible. The mirror's equations were partially garbled; the quoted statement is independently confirmed in Báez-Duarte Lemma2.1 and Burnol Theorem1.4.
- **Source identity correction:** sources/selberg_round2/balazard_saias.pdf is ESI623, **The Nyman–Beurling equivalent form for the Riemann hypothesis**, later Expo.Math.18(2000),131–138. It is not the Adv.Math.139 antecedent containing Lemma2. It must not be used as evidence that the latter proof was downloaded.
- Burnol math/0202166v1, **On an analytic estimate ... and a theorem of Báez-Duarte**, was read in sources/selberg_round2/burnol_analytic.txt, especially §§2–4. It confirms the distinction between unconditional gamma-ratio estimates and the conditional identification of the pointwise f_epsilon with an L² Mellin inverse.
- Balazard–de Roton0812.1689v1, selected propositions only, supplies later quantitative support; its entire proof is not audited here.

## Exact objects and theorem

Use H=L²((0,infinity),dx), complex scalars, rho_a(x)={1/(ax)}, a>=1, chi=1_(0,1], and B_nat the finite linear span of rho_n for positive integersn. The closure in Theorem1.1 is the H-norm closure. The theorem is

RH iff chi belongs to closure_H(B_nat).

Changing the value at an endpoint does not alter H elements, but the author's choice of chi at1 matches the pointwise Möbius identity exactly. Each rho_a is in H: near0 it is bounded by1, while forx>1/a it equals1/(ax), so both square integrals converge.

For epsilon>0 define finite sums f_(epsilon,n)=sum_(a<=n)mu(a)a^(-epsilon)rho_a. At each fixedx>0 the infinite sum defining f_epsilon is absolutely convergent: for sufficiently largea, rho_a(x)=1/(ax), and the remaining tail is bounded by x^(-1)sum a^(-1-epsilon). Its pointwise expression is

f_epsilon(x)=1/[x zeta(1+epsilon)]-sum_(a<=1/x)mu(a)a^(-epsilon)floor(1/(ax)).

This pointwise function is not automatically an H element for0<epsilon<1/2. H membership is one of the assertions proved using RH.

## Proof dependency tree and audit status

1. Algebraic floor decomposition and Euler product in Re(s)>1 → pointwise n-limit and epsilon-limit (pp.2–4,Eqs1.3,2.3–2.5; textlines100–117,178–198). Independently checked.
2. Mellin integral of fractional part in0<Re(s)<1 + Mellin Plancherel → Eq2.7 (p.4,lines202–224). Independently derived below; one normalization typo repaired.
3. RH → zero-free half-plane Re(s)>1/2 → Balazard–Saias partial Möbius estimate (Lemma2.1,p.3,lines138–146). Fixed-distance Perron mechanism checked against original pp.315–316; the subpolynomial inverse-zeta input is a standard external theorem, not proved from scratch here.
4. Functional equation + conjugation + uniform gamma Stirling → Lemma2.2 (p.3,lines150–165). Independently checked, including common zero ordinates.
5. Items2–4 + RH⇒Lindelöf at fixed distance → weighted H convergence as n→infinity with epsilon fixed (p.5,Eq2.8,lines229–260). Independently reconstructed with a corrected/free exponent choice. No interchange of limits.
6. Tail formula + contraction on(0,1) → unweighted H convergence and f_epsilon in closure(B_nat) (p.5,Eq2.9,lines262–274). Independently checked; a subscript/exponent typo repaired.
7. Lemma2.2 uniform for epsilon<=epsilon0<1/2 → a.e. dominated convergence of the analytic ratio kernels as epsilon↓0 → weighted H limit; conditional identification from item5 is retained (pp.5–6,lines276–293). Independently checked.
8. Explicit unweighting on(0,1) + tail coefficient tending to0 → f_epsilon→-chi in H under RH. Closure gives forward theorem. Independently checked.
9. Easy converse via a bounded H-functional at an off-line zero → RH. Reconstructed below without importing the full Nyman–Beurling theorem.
10. Corollary3.1 converse via H membership for an epsilon sequence and Mellin analyticity → zero accumulation contradiction. Independently reconstructed below; also consistent with Burnol§4.
11. Proposition3.1: Plancherel error split + a near-zero ratio estimate J_epsilon + a **uniform shrinking-epsilon** Möbius input I_(n,epsilon). Error split and J estimate reconstructed; the original uniform Möbius input is not independently completed. It cannot be inferred merely from fixed-epsilon Lemma2.1.

## Pointwise identities and convergence

For finite sums, {y}=y-floor(y) gives Eq2.3 directly. Oncea>1/x, the floor term vanishes, so the sum of floor terms is finite even as n→infinity. Absolute convergence of sum mu(a)/a^(1+epsilon)=1/zeta(1+epsilon) proves Eq2.4 with no RH.

As epsilon↓0, its first term tends to0 because1/zeta(1+epsilon)→0. In the finite second sum, coefficients tend to1. For every realy>=1,

sum_(a<=y)mu(a)floor(y/a)=sum_(k<=y)sum_(a|k)mu(a)=1.

It is0 for0<y<1. Taking y=1/x gives the exact pointwise limit-chi. No claim of H convergence follows from this pointwise argument alone.

## Mellin strip, normalization, and Eq2.7

For0<sigma<1,

integral_0^infinity {1/x}x^(s-1)dx=integral_0^infinity {u}u^(-s-1)du=-zeta(s)/s.

Absolute convergence holds because {u}=u near0 and is bounded at infinity. To verify the zeta identity, start in sigma>1 with zeta(s)=s integral_1^infinity floor(u)u^(-s-1)du and continue the resulting integral of{u} to sigma>0. Add its explicitly integrated(0,1) portion. Scalingx→ax supplies the factor a^(-s).

For the unnormalized transform M f(t)=integral f(x)x^(-1/2+it)dx, Mellin Plancherel is

||f||²_H=(1/(2pi))integral_R|M f(t)|²dt.

The PDF onp.4 instead prints the K measure(2pi)^(-1/2)dt while calling M an isometry. This is a constant normalization typo, verified visually in the PDF. An exact witness is chi: Mchi=1/(1/2+it), whose squared integral is2pi. The correct measure isdt/(2pi); the printed measure gives squared normsqrt(2pi). All convergence statements are unchanged by a fixed positive normalization, and the proposition's later2pi identity uses the correct normalization.

Let X_epsilon f=x^(-epsilon)f. At fixed0<epsilon<1/2, X_epsilon rho_a is square integrable: near0 its square is bounded byx^(-2epsilon), and at infinity it is O(x^(-2-2epsilon)). Applying the absolutely convergent Mellin identity at s=1/2-epsilon+it to the **finite** sum gives Eq2.7 exactly:

M(X_epsilon f_(2epsilon,n))(t)
 =-zeta(1/2-epsilon+it)/(1/2-epsilon+it)
   *sum_(a<=n)mu(a)/a^(1/2+epsilon+it).

No infinite-sum/Mellin interchange is used at this step.

## Lemma2.2: unconditional modulus estimate and zero conventions

Write s_minus=1/2-epsilon+it and s_plus=1/2+epsilon+it. The functional equation and conjugation give, away from zeros,

|zeta(s_minus)/zeta(s_plus)|
 =pi^(-epsilon)|Gamma(1/4+epsilon/2+it/2)/Gamma(1/4-epsilon/2+it/2)|.

Uniform Stirling on the fixed gamma strip gives an upper bound C_(epsilon0)(1+|t|)^epsilon for0<=epsilon<=epsilon0<1/2. Smallt is handled by continuity and compactness; the real parts of both gamma arguments stay positive. The statement is about the **modulus**, not the complex ratio itself.

If zeta(s_plus)=0 at a realt, reflection and conjugation give a numerator zero of the same multiplicity. For that fixed epsilon, the quotient as a local meromorphic function oft has a removable singularity. Alternatively, values at this discrete set may be defined arbitrarily for L² purposes. No RH assumption is required for this modulus bound. Joint continuity in(epsilon,t) at a critical-line zero is neither asserted nor needed.

## The flagged p.5 majorant: resolved without a theorem-level gap

The printed majorant(1+|t|)^(-1+2epsilon) has square-integrable tail only for epsilon<1/4. At epsilon=1/4 its squared tail is proportional to1/t and diverges. Therefore that displayed power alone does not justify the following sentence over the entire printed range epsilon0<1/2. Simply restricting to sufficiently small epsilon already proves the main theorem, whose proof only needs such values.

A stronger repair checks every fixed0<epsilon<1/2. Keep the free growth exponent eta in Lemma2.1 separate from the distance epsilon. Under RH,

S_(n,epsilon)(t)-1/zeta(s_plus)
 =O_(epsilon,eta)(n^(-epsilon/3)(1+|t|)^eta).

Functional equation plus the fixed-distance Lindelöf consequence of RH gives

|zeta(s_minus)|<=C_(epsilon,eta)(1+|t|)^(epsilon+eta).

The denominator|s_minus| is comparable to1+|t| with a constant depending on this fixed epsilon. Hence the **difference** between Eq2.7 and its limiting ratio is bounded by

C_(epsilon,eta)n^(-epsilon/3)(1+|t|)^(-1+epsilon+2eta).

Choose0<eta<(1/2-epsilon)/2. This is L² and gives weighted H convergence, even a fixed-epsilon error O_(epsilon,eta)(n^(-epsilon/3)). The limiting ratio itself is L² by Lemma2.2. This proves the convergence for every fixed epsilon<1/2.

Constants may blow up as epsilon↓0; this step does not claim uniformity in epsilon. The subsequent epsilon-limit uses a different, genuinely uniform gamma-ratio majorant. The source's compressed wording should not be read as producing a common n/effect-of-epsilon bound from O_epsilon notation.

Classification: repairable imprecision in a displayed integrability argument, with a verified stronger reconstruction; **no material gap in Theorem1.1 found**. Independent reviewer confirms this repair.

## Identifying the weighted H limit and removing the weight

By Mellin Plancherel, the finite weighted functions converge in H to someg. Their pointwise limits are x^(-epsilon)f_(2epsilon)(x), by the algebra already proved. H convergence admits an a.e. convergent subsequence, so g agrees with that pointwise expression a.e. This supplies the conditional Mellin-transform identification rather than assuming it.

On0<x<1, multiplication byx^epsilon is a contraction, so weighted convergence gives ordinary convergence there. Onx>1, the exact tail formula is

f_(2epsilon,n)(x)=x^(-1)sum_(a<=n)mu(a)/a^(1+2epsilon).

The PDF's Eq2.9 prints1+epsilon instead of1+2epsilon. The corrected tail identity follows immediately from the definition; its scalar coefficient converges absolutely to1/zeta(1+2epsilon). The unweighted tail error squared is exactly the squared difference of those coefficients. Thus f_(2epsilon,n)→f_(2epsilon) in H and the limit lies in closure(B_nat).

## The epsilon-limit is analytic-unconditional, but function identification retains RH

Define the analytic ratio kernel

G_epsilon(t)=-zeta(s_minus)/[zeta(s_plus)s_minus].

For epsilon<=epsilon0<1/2, Lemma2.2 gives the common L² majorant C_(epsilon0)(1+|t|)^(-1+epsilon0). At everyt where zeta(1/2+it) is nonzero, G_epsilon→-1/(1/2+it). At a critical-line zero of multiplicitym, the horizontal numerator/denominator ratio instead tends to(-1)^m. This discrete exceptional set is measure zero; a.e. convergence is exactly what dominated convergence requires.

The family G_epsilon therefore converges in the critical-line L² space **without assuming RH**. However, identifying it with M(X_epsilon f_(2epsilon)) was proved under RH in the preceding n-limit. The author's phrase about proceeding without RH at this stage must not be turned into an unconditional claim that the original pointwise f_epsilon converge in H. Such a claim would already imply RH, as the corollary argument below shows. This is a logical-dependency clarification, not a contradiction in the conditional proof.

Under RH we now have x^(-epsilon)f_(2epsilon)→-chi in H. On(0,1), write

f_(2epsilon)+chi=x^epsilon[x^(-epsilon)f_(2epsilon)+chi]+(1-x^epsilon)chi.

The first term tends to0 in H by contraction; the second by elementary dominated convergence. Onx>1, f_(2epsilon)=1/[x zeta(1+2epsilon)], whose squared tail norm tends to0. Thus f_(2epsilon)→-chi in H. Renaming2epsilon proves the ordered-limit claim. Since all those functions are closure elements, so is chi.

## Easy converse independently checked

For1/2<Re(s)<1 define the bounded functional on H

L_s(f)=integral_0^1 f(x)x^(s-1)dx
       +(1/(1-s))integral_1^infinity f(x)x^(-1)dx.

Cauchy–Schwarz bounds its norm by(2Re(s)-1)^(-1/2)+|1-s|^(-1). On each rho_a the tail equals1/(ax), and the Mellin identity gives L_s(rho_a)=-a^(-s)zeta(s)/s. At an off-line right-half-strip zero s=rho this vanishes on B_nat and its closure, but L_rho(chi)=1/rho is nonzero. Consequently chi in the closure rules out every zero with Re(rho)>1/2. The functional equation rules out corresponding left zeros, proving RH. No unbounded Mellin evaluation on arbitrary H functions was used.

## Corollary3.1: exact quantifiers and converse

The statement means: there exists epsilon_*>0 such that for every0<epsilon<epsilon_* the sequence f_(epsilon,n) converges in H as n→infinity. The previous proof gives this under RH. In fact a sequence of epsilon-values tending to0 suffices for the converse.

If such H convergence holds, the pointwise limit f_epsilon belongs to H. Its tail is c_epsilon/x with c_epsilon=1/zeta(1+epsilon). For Re(s)>1, absolute integration of the finite-floor decomposition gives

integral_0^1 f_epsilon(x)x^(s-1)dx
 =c_epsilon/(s-1)-zeta(s)/[s zeta(s+epsilon)].

The left side is analytic for Re(s)>1/2 by H membership and Cauchy–Schwarz. Analytic continuation therefore forces zeta(s)/[s zeta(s+epsilon)] to have no poles there except possibly the known pole at1. If a zero rho had Re(rho)>1/2, every sufficiently small epsilon in the sequence would force rho-epsilon also to be a zero, to cancel the denominator at s=rho-epsilon. These distinct zeros accumulate at rho, impossible for a nonzero analytic function. This proves RH and checks the corollary without assuming the weighted H convergence it is meant to imply.

## Proposition3.1: checked portion and uncompleted uniform input

Let s=1/2+it and M_n(s+epsilon)=sum_(a<=n)mu(a)a^(-s-epsilon). With the corrected Plancherel normalization, the source's error split is

2pi||f_(epsilon,n)+chi||²
 <=2integral|zeta(s)|²|M_n(s+epsilon)-1/zeta(s+epsilon)|² dt/|s|²
   +2integral|zeta(s)/zeta(s+epsilon)-1|² dt/|s|².

This is an exact triangle-square inequality; no conditional convergence is hidden in the finite-sum side. Call the two integrals I_(n,epsilon),J_epsilon.

**J_epsilon reconstruction under RH.** Burnol's uniform ratio bound gives |zeta(s)/zeta(s+epsilon)|<=C|s|^(epsilon/2) for0<epsilon<=1/2. An independent derivation uses the even Hadamard product for xi(1/2+z) under RH: each conjugate zero-pair factor has modulus nondecreasing as Re(z) moves from0 to a positive value. Thus |xi(s)/xi(s+epsilon)|<=1; the polynomial and gamma factors give the stated bound uniformly. Hadamard factorization, the functional equation and uniform Stirling are standard external inputs; the factor monotonicity is directly checked by

|(epsilon+it)²+gamma²|²=(gamma²-t²)²+2epsilon²(gamma²+t²)+epsilon^4.

For small epsilon, split the t-line by distance delta from zero ordinates. Away from zeros, the classical local logarithmic-derivative formula and N(t+1)-N(t-1)=O(log(2+|t|)) give |zeta'/zeta|<=C delta^(-1)log(2+|t|) throughout the short horizontal segment. Integrating and exponentiating, if epsilon/delta is sufficiently small, gives |zeta(s)/zeta(s+epsilon)-1|<=C(epsilon/delta)(1+|t|)^(1/4). Its weighted squared integral is O(epsilon²/delta²).

On the union of intervals |t-gamma|<=delta, the uniform Burnol ratio bound makes the weighted squared integrand O((1+|t|)^(-3/2)) for epsilon<=1/2. The union integral is O(delta sum_gamma(1+|gamma|)^(-3/2))=O(delta); this sum converges by the classical zero count. Taking delta=epsilon^(2/3) proves J_epsilon=O(epsilon^(2/3)). Constants can be fixed for sufficiently small epsilon; extending to a fixed larger compact epsilon interval requires only a coarse uniform bound. This verifies the source's near-zero integration mechanism.

**I_(n,epsilon) input not completed.** The source invokes a stronger form of Balazard–Saias:

M_n(1/2+epsilon+it)=1/zeta(1/2+epsilon+it)
 +O(n^(-epsilon/3) exp(b log(|t|+3)/loglog(|t|+3)))

uniformly when c/loglog n<=epsilon<=1/2, for suitable fixed constants. This is materially stronger than the fixed-epsilon Lemma2.1 because its O-constant must not explode as epsilon shrinks with n. The original fixed-distance Perron proof was inspected and reconstructed, but its distance-dependent inverse-zeta constants have not been tracked sufficiently to prove this uniform version. Treating fixed-epsilon O notation as uniform would be invalid.

If this uniform input holds, RH bounds for zeta on the critical line absorb into exp(O(log|t|/loglog|t|)); the weighted integral of that subpower factor converges. Hence I_(n,epsilon)=O(n^(-2epsilon/3)). Choosing epsilon=c/loglog n and taking square roots yields the claimed norm O((loglog n)^(-1/3)). All exponents and square-root conversions check.

Later support: Balazard–de Roton0812.1689v1 pp.4–5 explicitly records these two antecedent estimates and improves them. Its Proposition3 and proof in§7 give I_(n,epsilon)<<n^(-epsilon/2) when epsilon is at least a constant times(loglog n)^(5/2+eta)/(log n)^(1/2), which is eventually smaller than c/loglog n. This later theorem would recover the constructive bound, but its deep proof is not independently audited here and does not close the original-input verification gap.

## Findings and exact limits of this audit

- Main Theorem1.1: independent technical reconstruction succeeds after harmless normalization/index repairs and a stronger fixed-epsilon majorant. No material issue found in the inspected proof.
- Corollary3.1: independently reconstructed with exact quantifiers; its converse can be verified through analytic Mellin continuation and zero accumulation.
- Printed p.5 exponent: insufficient over its whole stated range, but repaired for every fixed epsilon<1/2. This should not be described as a failed theorem.
- Plancherel measure and Eq2.9 tail exponent: verified local preprint typos; journal-version comparison unavailable. Their corrections do not change the theorem or its norm limits.
- Analytic ratio convergence is unconditional; its identification with the pointwise f_epsilon retains the earlier RH assumption. Forgetting that dependency would create a false purported proof of RH, not an error established in the source's conditional proof.
- Proposition3.1: conclusion consistent with later results; original shrinking-epsilon uniform Möbius input remains a targeted verification task. Whole-work Level2 is withheld.

Next papers/tasks: obtain accessible primary PDF of Balazard–Saias Adv.Math.139 pp.315–316 and track its inverse-zeta constants as the half-plane distance decreases; inspect the published2003 Báez-Duarte PDF for local corrections; deeply audit Burnol's uniform ratio theorem and the later Balazard–de Roton quantitative input if a complete dependency audit is required. Preserve a single work identity across0202141,0205003 and the journal version.

## Additional boundary/context checks

- The assertion that the continuous-dilation closure is larger than the integer-dilation closure has a direct witness. Sety=1/x, giving measurey^(-2)dy. Every integer-dilation combination is affine on each cell(k,k+1), with common slopeA; on(0,1) it equalsAy. Convergence in the weighted H norm fixesA via that first cell, and on each later cell the constant offsets also converge. Thus the closure retains this affine-cell property. The continuous dilationa=3/2 has a jump inside the cell(1,2) at y=3/2, so it cannot equal such an affine function a.e. on that cell. It lies outside the integer-dilation closure. This verifies the structural claim rather than relying only on the word "thin".
- The lower-bound discussion around Eq1.2 concerns largeN. A literal claim withC/sqrt(log N) for everyN>=1 would be undefined atN=1 and cannot be uniform asN↓1; the source's asymptotic-approximation context is essential. This observation is not a challenge to Burnol's asymptotic lower bound.
- Raw Möbius-truncation divergence in H, mentioned in the historical introduction, remains an explicitly cited antecedent result; its original proof is not independently reproduced in this audit. It is not used to prove Theorem1.1.
- The parameter epsilon in the exponent of Lemma2.1 is a free growth allowance. Identifying it with the distance-to-boundary epsilon in the main proof is optional and unnecessarily restrictive; keeping two names is what resolves the flagged integrability range.
- No direct lower bound on|zeta(1/2+epsilon+it)| uniform as epsilon↓0 is assumed. Such a bound would be false near critical zeros. The final argument instead uses the symmetric functional-equation modulus identity and an a.e. limit.
