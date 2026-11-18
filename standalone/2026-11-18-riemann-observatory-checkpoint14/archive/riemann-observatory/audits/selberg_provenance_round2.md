# Fixed Selberg coefficients: provenance, exact status, and multiplicity obstruction

TASK004, independent reviewer. Access/search cutoff: 2026-11-17. This report distinguishes source statements from independent reconstructions. It makes no allegation that RH is false, that multiple zeros exist, or that Ehm's Gram-kernel calculations fail.

## Finding

For V_N(s)=Σ_{n≤N} μ(n)(1−log n/log N)n^(−s), define the **prescribed-family** error

η_N²=(1/(2π))∫_R |1−ζ(1/2+it)V_N(1/2+it)|² dt/(1/4+t²).

This is not the optimized Nyman–Beurling distance d_N², which takes an infimum over all length-N coefficient vectors.

The following arrows are established in the inspected primary literature:

* RH ⇔ d_N→0, for arbitrary optimizing/approximating coefficient arrays.
* RH ⇒ convergence of specific *shifted* Möbius arrays n^(−ε), with ordered limits N→∞ followed by ε↓0, or suitable explicitly selected diagonals ε=ε_N.
* RH **plus** the inverse-derivative-moment hypothesis Σ_{|Im ρ|≤T}|ζ′(ρ)|^(−2)≪T^(3/2−δ), δ>0, ⇒ η_N²∼(2+γ−log(4π))/log N. This is Bettin–Conrey–Farmer Theorem 1, not an RH-alone theorem.
* η_N→0 ⇒ RH **and all nontrivial zeros are simple**. This is prior published mathematics: Wei–Wu, Proposition 1.9 (2022), independently reconstructed below.

The reverse implication RH⇒η_N→0 is explicitly **Problem 1** in Wei–Wu (2022), following Balazard–Saias Question 4 (1998). No later primary proof resolving this reverse implication was located in the searches performed through the cutoff. That negative search is not an exhaustive certification of the entire 2022–2026 literature.

Ehm arXiv:2405.06349v2, p.1, correctly describes Bettin–Conrey–Farmer's extra hypothesis. Immediately after Proposition 1.1 it asserts that RH is equivalent to convergence of the fixed-coefficient quadratic form to q. For q=1, that statement requires the unresolved arrow RH⇒η_N→0; Proposition 1.1 alone does not supply it. Under the BCF extra hypothesis the asserted fixed-array convergence is justified. The appropriate finding is an **unresolved source-context gap / unstated stronger hypothesis in the claimed reverse implication**, not a verified false mathematical statement. A proof of that reverse implication would, by Wei–Wu, also prove that RH implies simplicity.

## Primary-source evidence map

| Work/version inspected | Exact passage | What it establishes or asks |
|---|---|---|
| Balazard–Saias, ESI Preprint 623 (1998), later *Expo. Math.* 18(2) (2000), 131–138 | §5, Question 4, printed p.7 | Under RH, does precisely η_N² tend to zero? Explicitly presented as open. Question 2 concerns arbitrary discrete coefficient arrays; Question 3 the unsmoothed μ(n) array. These are different questions. |
| Conrey–Myerson, arXiv:math/0002254v1 (2000) | Introduction pp.1–2; Proposition 1 p.2; Theorem 1 and Remark 1 pp.5–6 | Defines the same V_N. Reports an RH+zero-separation result as Conrey–Farmer work in preparation. Proves the reciprocal fractional-part norm identity and unconditional uniform convergence of W_N(u)=Σ b_{n,N}{nu}/n to −sin(2πu)/π. Remark 1 isolates the interval 0<u<1/N and its contribution C_N²/N; uniform pointwise convergence does not solve the weighted norm problem. |
| Báez-Duarte, arXiv:math/0205003v1 (2002) | Theorem 1.1 pp.1–2; §2 pp.4–6; Corollary 3.1 and Proposition 3.1 pp.6–8 | Strong discrete closure criterion; fixed-positive-ε arrays μ(n)n^(−ε), then ε↓0. Proposition 3.1 supplies μ(n)exp(−c log n/log log N), a different diagonal. The logarithmic Selberg approximation S_N is discussed as an attempted mollification on p.2. Formula (3.1) proposes *linear* Cesàro weights (1−n/N) together with n^(−ε), not the fixed logarithmic array. |
| Burnol, arXiv:math/0202166v1 (2002), published 2003 | Theorems 1.3–1.4 p.2; §2 p.3 | Under RH, uniform ζ(s)/ζ(s+A) estimates; then N→∞ at fixed ε>0 and ε↓0. No theorem removing ε while fixing Selberg coefficients. |
| Balazard–de Roton, arXiv:0812.1689v1 | Main theorem p.3; §2 Propositions 1–3 pp.4–5 | Under RH, d_N²≪δ(log log N)^(5/2+δ)(log N)^(−1/2). Explicitly works with μ(n)n^(−ε), choosing ε=25(log log N)^(5/2+δ)(log N)^(−1/2). This proves an upper bound for an admissible shifted family and hence the infimum, not for fixed Selberg weights. |
| Bettin–Conrey–Farmer, arXiv:1211.5191v1 | Theorem 1 p.2; discussion pp.2–3 | Exact prescribed V_N asymptotic under RH plus the inverse derivative moment. The source explicitly notes that the extra hypothesis entails simplicity and is needed in their proof to control infinitely many zero residues. |
| Wei–Wu, institutional manuscript, published *Expositiones Mathematicae* 40(4) (2022), 961–993, DOI 10.1016/j.exmath.2022.07.004 | Problem 1 pp.6–7; Proposition 1.9 p.7; proof pp.27–28; Remark 5.8 p.29; Theorem 1.10 p.7 | η_N→0 implies RH and simple zeros; RH-alone reverse is an open problem in that source. Theorem 1.10 instead proves RH iff convergence on **every fixed shifted vertical line** Re(s)=τ′>1/2, and proves boundedness of η_N suffices for RH. Neither conclusion gives η_N→0 on the boundary line. |
| Ehm, arXiv:2405.06349v2 (13 May 2024) | Introduction p.1, equations (1)–(3), Proposition 1.1 and following sentence; proof §7.1 p.9 | Mixed term converges unconditionally; from expansion this makes fixed quadratic-form convergence equivalent to fixed η_N→0. It does not make that fixed-family convergence equivalent to RH without the missing reverse implication. |

All page references above are printed manuscript pages in the specific downloaded versions, not inferred journal-page mappings. This track did not read every page of each listed work. See records for exact inspected scope.

## Exact logical issue in the quadratic-form sentence

Write F_n and G_mn for Ehm's q=1 kernels. Ehm's expansion is

η_N²=1−2Σ_n λ_{n,N}F_n+Q_N,

where Q_N=Σ_{m,n}λ_{m,N}λ_{n,N}G_mn. Proposition 1.1 proves Σ_n λ_{n,N}F_n→1 unconditionally. Hence

Q_N→1 ⇔ η_N→0.

The criterion for the infimum only gives RH⇔inf_{a_1,…,a_N} error→0. Replacing the infimum with the particular array λ_{n,N} requires a theorem about that array. BCF supplies such a theorem under the extra derivative-moment hypothesis. The closure theorem, mixed-term limit, and an arbitrary optimizer upper bound do not supply it under RH alone.

This issue affects the interpretation of the fixed array. It does not invalidate Ehm's independently derived formulas for the Gram kernels, their reciprocal series, or Proposition 1.1's elementary Möbius moment calculation.

## Independent reconstruction of the prior simplicity implication

The proof below was derived before locating Wei–Wu Proposition 1.9; it agrees with the published argument and is **not a new result**.

Put b_{n,N}=μ(n)(1−log n/log N), C_N=Σ_{n≤N}b_{n,N}, and W_N(u)=Σ_{n≤N}b_{n,N}{nu}/n. On H=L²((0,∞),du/u²), use the Mellin transform M f(s)=∫_0^∞ f(u)u^(−s−1)du at Re(s)=1/2. Plancherel identifies H with L² on that line with measure |ds|/(2π).

Let χ_f(s)=2^s π^(s−1)sin(πs/2)Γ(1−s), so ζ(s)=χ_f(s)ζ(1−s) and |χ_f(1/2+it)|=1. The subscript distinguishes the functional-equation factor from interval indicators. For g(u)=−sin(2πu)/π,

M W_N(s)=−ζ(s)V_N(1−s)/s,   M g(s)=−χ_f(s)/s.

Both Mellin integrals converge in the strip 0<Re(s)<1; the second formula follows from the elementary sine–Gamma integral. The boundary operator

(Uf)(s)=χ_f(s)(1−s)f(1−s)/s

is unitary, since reflection preserves the boundary measure and the multiplier has modulus one. Direct substitution therefore gives the **exact error identity**

η_N²=∫_0^∞ |W_N(u)+sin(2πu)/π|²du/u².

It refines the norm-only identity in Conrey–Myerson Proposition 1. The source's unconditional uniform limit is an alternative route to the same limiting conclusion, but is not needed for this identity.

For 0<u<1/N, every {nu}=nu, hence W_N(u)=u C_N. Since |g(u)|≤2u, the local triangle inequality yields

|C_N|/√N ≤ η_N+2/√N.

Thus η_N→0 implies C_N=o(√N). Set Ψ(x)=Σ_{n≤x}μ(n)log(x/n). Then Ψ(N)=C_N log N=o(√N log N). For N≤x<N+1, the difference Ψ(x)−Ψ(N)=log(x/N)Σ_{n≤N}μ(n) is O(1), so the same little-o estimate holds for real x→∞.

For Re(s)>1, absolute convergence and termwise integration give

∫_1^∞ Ψ(x)x^(−s−1)dx=1/[s²ζ(s)].

The little-o bound makes the integral analytic for Re(s)>1/2. It therefore excludes zeros of ζ in that half-plane. By the functional equation, RH follows.

If ρ=1/2+iγ were a zero of order m≥2, then

lim_{ε↓0} ε^m/[ (ρ+ε)²ζ(ρ+ε) ]=m!/[ρ²ζ^(m)(ρ)]≠0.

On the other hand Ψ=o(√x log x) gives

ε² ∫_1^∞ Ψ(x)x^(−ρ−ε−1)dx→0.

For completeness, split the integral at a large fixed A where |Ψ(x)|≤δ√x log x for x≥A. The finite initial integral multiplied by ε² tends to zero, while the remaining absolute value is at most δ ε²∫_1^∞log x·x^(−ε−1)dx=δ. Let δ↓0. This contradicts a pole of order at least two. All critical-line zeros must be simple.

Wei–Wu's proof pp.27–28 follows precisely the unitary-transform/small-interval/Mertens-pole architecture. Its Remark 5.8 gives a second proof through a reciprocal Möbius tail and the prime-counting mean-square estimate.

## Quantitative corollaries checked in this track

These are elementary consequences of the same argument; no literature novelty is claimed. They concern **η_N, the prescribed error**, not optimized d_N.

1. Taylor's estimate |sin x−x|≤|x|³/6 gives the finite-N lower bound

η_N ≥ |C_N+2|/√N − [4π²/(3√5)] N^(−5/2).

2. If a critical-line zero ρ has order m≥2, then

limsup_{N→∞} η_N/(log N)^(m−2) ≥ m/[|ρ|² |ζ^(m)(ρ)|].

To see this, suppose the limsup is a finite D. The local bound implies |Ψ(x)|≤(D+o(1))√x(log x)^(m−1). Multiplying its Mellin integral by ε^m, taking absolute values, and using ε^m∫_1^∞(log x)^(m−1)x^(−ε−1)dx=(m−1)!, bounds the pole coefficient m!/[|ρ|²|ζ^(m)(ρ)|] by D(m−1)!. Let the limsup slack decrease to zero. If the assumed limsup is infinite the inequality is automatic. For a double zero this gives limsup η_N≥2/[|ρ|²|ζ″(ρ)|]>0; for m≥3 it forces limsup η_N=∞.

3. If ζ has a zero with real part greater than 1/2, then limsup η_N=∞. Otherwise η_N bounded would give Ψ(x)=O(√x log x), making 1/[s²ζ(s)] analytic in Re(s)>1/2, a contradiction. This agrees with the boundedness implication in Wei–Wu Theorem 1.10(2).

The main simplicity implication has exact prior attribution. The displayed quantitative constants were independently derived here; they have not undergone a complete priority search or formal proof-assistant validation.

## Extension to Ehm’s q=2 norm (independent derivation; review pending)

The same necessary simplicity condition extends to the prescribed family in every integer q≥1 norm, including Ehm’s q=2. Write η_(q,N)=||(1−ζV_N)/s^q|| on the full critical line. The unitary boundary operator

(U_q f)(s)=χ_f(s)[(1−s)/s]^q f(1−s)

and the Hardy integration operator (Jf)(u)=∫_0^u f(v)dv/v give

η_(q,N)=||J^(q−1)(W_N−g)||_H.

Indeed M(Jf)(s)=Mf(s)/s. The operator J is bounded on H by the classical Hardy inequality (norm at most2), so the identity is valid in H as well as for these explicit functions. For u<1/N, J^(q−1)W_N(u)=C_Nu because J(u)=u. Also |J^(q−1)g(u)|≤2u, by induction from |g(u)|≤2u. Thus

|C_N|/√N≤η_(q,N)+2/√N.

Consequently prescribed q=2 convergence also implies RH and simplicity by the preceding pole argument. Merely adding powers of |s| in the denominator does not remove this fixed-coefficient multiplicity obstruction. This derivation has been submitted for independent parent review and is not yet an independently validated archive finding at this checkpoint; no priority claim is made. It concerns the fixed family, not the optimized q=2 criterion.

## Anchoring and interval conventions

Let y=1/x, e_n(y)={y/n}, and H_y=L²((0,∞),dy/y²). The physical-space error corresponding to η_N is

h_N(y)=1_[1,∞)(y)+Σ_{n≤N}b_{n,N}e_n(y).

Define anchored generators r_n(y)=floor(y/n)−floor(y)/n={y}/n−{y/n}, and g_N^a=Σ_{n≤N}b_{n,N}r_n. Since r_1=0, adding or omitting n=1 in that anchored sum has no effect. Set A_N=Σ b_{n,N}/n. Then exactly

1_[1,∞)−g_N^a=h_N−A_N{y}.

The anchored error vanishes on 0<y<1. Moreover A_N→0 unconditionally: Ehm §7.1 uses Σ_{n≤N}μ(n)/n→0 and Σ_{n≤N}μ(n)log n/n→−1, yielding A_N∼1/log N. Since {y}∈H_y, fixed-array convergence in anchored L²((1,∞),dy/y²) is equivalent to the full unanchored convergence defining η_N. Merely changing to these anchored generators does not remove the simplicity obstruction. With the opposite sign convention for anchored generators, the target sign must change accordingly.

This equivalence applies to the stated fixed family and vanishing anchor coefficient. It does not license replacing full norms by a moving truncated prefix without controlling the omitted tail.

## Cesàro, Riesz, and shifted arrays must remain distinct

* The logarithmic Selberg factor is (log(N/n))/log N, a first logarithmic Riesz mean of the sharp partial sums.
* Báez-Duarte's proposed Cesàro factor on p.6 is (1−n/N), accompanied by n^(−ε). It is not the same factor.
* The proved n^(−ε) approximants require an ordered two-parameter limit or a proved choice ε_N. Sending ε→0 arbitrarily with N is not authorized by fixed-ε convergence.
* Balazard–de Roton's explicit ε_N is of order (log log N)^(5/2+δ)/√log N. It does not make n^(−ε_N) equal to the Selberg coefficient profile.
* Fixed shifted vertical-line convergence Re(s)=τ′>1/2 in Wei–Wu Theorem 1.10 is also different from boundary convergence at Re(s)=1/2. Uniformity as τ′↓1/2 is the missing step in an attempted endpoint passage.

## Search and quality limits

Primary sources were downloaded rather than audited from abstracts. New sources in this track are recorded as full-text accessed but partially read, with conservative whole-work audit level 0; inspected portions have technical reconstruction. The already-read Báez-Duarte, BCF and Ehm records are reused for source identity rather than counted again as newly read works.

Focused searches covered exact titles, Selberg approximation/weights, Balazard–Saias Question 4, Wei–Wu Proposition 1.9, later 2024–2026 references, and Ehm's claim. Later search results included numerical/partial-probe work and optimizing/shifted-array claims, which do not resolve the exact fixed-boundary-norm question. No complete forward-citation crawl or exhaustive correction search was performed. Consequently the archive should say “unresolved in the inspected primary chain; no later resolution located,” rather than certify a global current open-problem status solely from this search.

## Concrete continuation tasks

1. Complete a forward-citation/version search for Wei–Wu Proposition 1.9 and Ehm v2, checking for a corrected formulation or a genuine proof of RH⇒η_N→0.
2. Independently audit BCF's inverse-derivative-moment input and identify which weaker condition would still prove mere convergence instead of the sharp constant.
3. Test higher logarithmic Riesz orders under allowed zero multiplicities. The same local/pole argument suggests that order k permits at most multiplicity k if its fixed-family norm tends to zero; this needs a separately documented general theorem before use.
4. Formalize the elementary small-interval and Abelian-pole lemmas; their role is to prevent an unjustified endpoint or fixed-array substitution in future research.
