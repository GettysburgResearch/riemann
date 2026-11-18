# The evolution of methods in Riemann-hypothesis research, 1859–2026

```text
Status: EXPLORATORY / SYNTHESIS. A historical-analytical essay; it states no new theorem and makes
        no claim about RH, which remains open. Every cited result carries a status label (below).
Scope: methods and conceptual transitions in RH research from Riemann (1859) to 2026-11-17, for
       zeta(s) and, where the method demands it, Dirichlet/Hecke/automorphic L-functions and
       function-field zeta functions.
Exact sources or dependencies: corpus/bibliography.jsonl (PAPER ids, years, audit levels);
       theorems/theorems.jsonl (Level-1 statements with locations); the per-paper limitation notes in
       the discovery file papers_compact.jsonl; frontiers/ledger.jsonl (LED ids),
       frontiers/records_ledger.md, frontiers/research_programs.md;
       history/recent_developments_2024_2026.md;
       proposals/independent_campaigns/C3-failure-anatomy/REPORT.md; audits/quasi_rh/DOSSIER.md;
       audits/claims_2026/SIEGEL/ARCHITECTURE.md; audits/L2_flag_audits/F1, F4, F5, F6, F7.
What was actually run: selective reading of those files (grep/python); PAPER-id lookups by author,
       title and arXiv id, with a script check that every cited id exists in the corpus. No
       computation, proof check or Lean build was done for this essay.
Smallest remaining gap: many cited works sit at evidence level L0/L0+ in the corpus (index data
       only). Where this essay describes their content, it relies on standard literature knowledge,
       marked [std]. All 2026 claims are unrefereed. The Observatory audits cited for them were done
       by AI agents and are not human expert review.
```

**Status labels.**
- **[T]**: refereed theorem, unconditional.
- **[T|RH]**, **[T|GRH]**: refereed theorem conditional on the named hypothesis.
- **[H]**: heuristic or conjecture.
- **[N]**: finite computation. It is rigorous only where called certified.
- **[U]**: unrefereed human preprint.
- **[AI-U]**: AI-generated or AI-discovered claim, unrefereed.
- **[std]**: content described from standard knowledge, not from a reading recorded in this archive.

Works are cited by corpus id (PAPER-####). Works outside the corpus get a full citation or an arXiv number.

---

## 0. Thesis

RH research since 1859 is a sequence of **changes of representation**. RH has been read in turn as a statement about:
- the zeros of an entire function;
- the error term for primes;
- the growth of $|\zeta|$;
- mean values of Dirichlet polynomials;
- positivity of a quadratic form;
- an operator spectrum;
- intersection theory on a surface.

Each representation made one obstacle tractable. Each also produced a characteristic **ceiling** short of $\Re s=\tfrac12$.

Two diagnostics recur throughout.
1. **Davenport–Heilbronn.** A Dirichlet series with a Riemann-type functional equation but no Euler product can have zeros off the line (Davenport–Heilbronn 1936, PAPER-0417; Bombieri–Ghosh, PAPER-0114). The archive's failure-anatomy campaign certified one such zero at $0.80851718\ldots+85.69934848\ldots i$ (C3-D14).
2. **Locality.** Finite or local zero information reaches no global statement without a further theorem.

"Where is multiplicativity used in a way the Davenport–Heilbronn function cannot imitate?" therefore separates methods that could in principle prove RH from those that cannot.

---

## 1. 1859–1900: from Euler product to entire function

**What changed.** Euler (PAPER-0468) and Chebyshev (PAPER-0747, PAPER-0748) treated $\zeta$ as a function of a real variable. Riemann's memoir (PAPER-0469; L0, content [std]) made it meromorphic in $\mathbb C$. The memoir contains:
- the functional equation, via theta;
- the entire function $\xi$;
- the count $N(T)\approx\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}$;
- an explicit formula expressing prime counts as a sum over zeros;
- the remark that all roots of $\Xi$ are "very probably" real.

Siegel's study of the Nachlass (PAPER-0415) later showed that Riemann had computed zeros with what is now the Riemann–Siegel formula [std].

**Obstacle overcome.** Riemann's product and explicit formulas were heuristic. Later work made them theorems:
- **Hadamard (1893, PAPER-0137)** related coefficient decay to order and genus, which gave $\xi$ a convergent product over its zeros (THM-PAPER-0137-1…4).
- **Von Mangoldt** proved the explicit formula (PAPER-0077, THM-PAPER-0077-5). In 1905 he proved the count with explicit constants, $|N(T)-(\tfrac{T}{2\pi}\log\tfrac{T}{2\pi}-\tfrac{T}{2\pi})|<0.432\log T+\dots$ (PAPER-0136, THM-PAPER-0136-1).
- **Hadamard and de la Vallée Poussin (1896)** proved $\zeta(1+it)\ne0$ and hence the prime number theorem (PAPER-0009, THM-PAPER-0009-1; PAPER-0044). Hadamard's argument applies to any Euler-type product whose logarithm has nonnegative coefficients (THM-PAPER-0009-2). It is an early prototype of the positivity arguments that recur below.

**Both directions became explicit.**
- De la Vallée Poussin (1899, PAPER-0078) proved a zero-free region $1-\sigma\ge\rho_0/(\log\beta+\eta_0)$ with $\rho_0=0.03282\ldots$ (THM-PAPER-0078-2), i.e. $R\approx30.47$ in the normalisation $1-1/(R\log t)$, with error term $x\exp(-c\sqrt{\log x})$.
- Von Koch (1900, PAPER-0030) proved $\mathrm{RH}\Rightarrow\pi(x)=\mathrm{Li}(x)+O(\sqrt x\log x)$ (THM-PAPER-0030-4) [T|RH].

**Left open.** Hadamard wrote "nous sommes bien loin d'avoir démontré l'assertion de Riemann–Stieltjes" (we are very far from having proved it; discovery notes on PAPER-0009). The basic dichotomy was now visible:
- regions near $\sigma=1$ are reachable;
- the line $\sigma=\tfrac12$ is not.

---

## 2. 1900–1940: growth, oscillation, and the first zeros on the line

**What changed.** Attention moved to the *location and statistics* of zeros, studied through the *growth and mean values* of $\zeta$ in the strip.

- **Growth.** Lindelöf (1908, PAPER-0142) used the Phragmén–Lindelöf principle (PAPER-0749) to prove the convexity bound and define $\mu(\sigma)$. He asked whether $\zeta(\tfrac12+it)\ll t^\varepsilon$ (THM-PAPER-0142-3, -5).
- **Zeros on the line.** Hardy (1914, PAPER-0146) proved that infinitely many zeros lie on the line. His argument was a theta-derived moment identity for $\Xi$ plus a sign-change contradiction (THM-PAPER-0146-1). Hardy–Littlewood (PAPER-0115) improved this to $N_0(T)>KT$ (THM-PAPER-0115-1). Bohr–Landau (PAPER-0392) showed that almost all zeros lie near the line [std].
- **Oscillation.** Schmidt and Littlewood (PAPER-0143, THM-PAPER-0143-1) and Hardy–Littlewood (PAPER-0120, Thm 2.241) gave $\psi(x)-x=\Omega_\pm(\sqrt x)$. So RH is the *optimal* error-term statement.
- **Mean values.** The mean-value method begins here:
  - $\int|\zeta(\tfrac12+it)|^2\sim T\log T$ (PAPER-0120, Thm 2.41);
  - $\int_0^T|\zeta(\tfrac12+it)|^4=\frac{1}{2\pi^2}T\log^4T+O(T\log^3T)$ (Ingham, PAPER-0121, Thm B);
  - the approximate functional equation (PAPER-0148);
  - Atkinson's formula (PAPER-0124).
- **Value distribution.** Bohr–Courant (PAPER-0134) opened the probabilistic study of values. Voronin's universality theorem (PAPER-0138) is its best-known descendant, and it approximates only non-vanishing targets.
- **Zero density.** Carlson (PAPER-0444) proved a power-saving bound for $N(\sigma,T)$ [std]. "Few zeros far from the line" became a theorem decades before "a positive proportion on the line".

**Obstacle overcome.** Before 1914 only finitely many zeros were known to lie on the line, from computation (§10). Hardy's trick and the mean-value machinery converted the question into estimable integrals.

**Left open.**
- **Proportion.** $KT$ is proportion zero against $N(T)\asymp T\log T$.
- **Moments.** Only the second and fourth moments have asymptotics, still true in 2026. Above the fourth moment there are only power bounds (Heath-Brown's twelfth moment, PAPER-0702; MOM frontier).

---

## 3. 1920–2026: exponential sums, zero density and large values

**What changed.** The growth of $\zeta$ and the density of zeros were reduced to cancellation in $\sum n^{-it}$ and to **large values of Dirichlet polynomials**. The tools were imported:
- Weyl differencing (PAPER-0719) and van der Corput's method (PAPER-0445, PAPER-0730);
- Vinogradov's method (PAPER-0443, PAPER-0447; Korobov, PAPER-0448);
- the large sieve (Linnik, PAPER-0731; Bombieri, PAPER-0450; Montgomery–Vaughan, PAPER-0451, PAPER-0357);
- later, decoupling (PAPER-0743, PAPER-0463) and efficient congruencing (PAPER-0741).

**Record lines** (ZFR and ZDE frontiers; [T] unless marked):
- **Zero-free regions.** The shape went from de la Vallée Poussin to Vinogradov–Korobov (1958). That shape has not changed in any refereed work for 68 years. The classical constant $R$ went:
  - 30.47 (1899);
  - 8.463 (Ford 2002, PAPER-0051; corrected to 8.464);
  - 5.558691 (Mossinghoff–Trudgian–Yang 2024, PAPER-0010);
  - 4.896 (Bellotti–Trudgian–Yang, PAPER-0159) [U]. Audit F7 found two printed intermediate steps wrong as written, with the conclusion still valid.
- **Subconvexity.** $1/6\to9/56$ (Bombieri–Iwaniec, PAPER-0130) $\to13/84$ (Bourgain, PAPER-0089, via decoupling).
- **Zero density.** In $N(\sigma,T)\le T^{A(\sigma)(1-\sigma)+o(1)}$:
  - $\sup A$ went 4 (Carlson) → 3 (Ingham, PAPER-0441) → $12/5$ (Huxley, PAPER-0213) → $30/13$ (Guth–Maynard, PAPER-0054, Ann. of Math. 2026; THM-PAPER-0054-2).
  - The density hypothesis $A\le2$ was proved for $\sigma\ge4/5$ (Montgomery, PAPER-0210), then $11/14$ (Jutila, PAPER-0663), then $25/32$ (Bourgain, PAPER-0312).
  - Tao–Trudgian–Yang's machine optimisation (PAPER-0466) moved neither $\sup A$ nor $25/32$.

**The Guth–Maynard transition.** Their large-value bound is
$$R\le T^{o(1)}\bigl(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}\bigr)$$
for 1-bounded coefficients (THM-PAPER-0054-1). It was the first improvement at $\sigma=3/4$ since Ingham. Corollaries: primes in all intervals $[x,x+x^{17/30+\varepsilon}]$ and in almost all intervals of length $x^{2/15+\varepsilon}$ (THM-PAPER-0054-3, -4).

The idea is additive energy of large-value sets, imported from harmonic analysis. It requires $\ell^\infty$ coefficient control. Bourgain's counterexample to the $\ell^2$-normalised Montgomery conjecture shows that some such coefficient condition is necessary.

**Barriers.**
- **Binding point.** After Guth–Maynard the binding point is $\sigma=7/10$, where the mean-value bound and their bound are tangent. Below $7/10$ the mean-value theorem has never been beaten.
- **Kakeya.** Montgomery's $\ell^q$ large-values conjecture implies Kakeya in all dimensions (Guth's survey, via the ZDE frontier).
- **Vinogradov–Korobov shape.** Improving it needs cancellation in $\sum_{n\sim N}n^{-it}$ for $N=\exp((\log t)^{2/3+\delta})$, which no method provides.
- **Additive structure is necessary.** Beurling systems with regular integer counts can have zeros arbitrarily close to $\sigma=1$ (Diamond–Montgomery–Vorhauer, PAPER-0581; Broucke, arXiv:2507.13780). Any progress must use additive structure.
- **Structural limit.** Density and zero-free regions measure *how far* zeros can stray. The density hypothesis is the sharp uniform target, since $A(1/2)=2$. Neither yields "no zeros off the line".

---

## 4. 1942–2020: mollifiers and the critical line

**What changed.** Selberg (1942, PAPER-0413; [std]) proved that a **positive proportion** of zeros lie on the line. He multiplied $\zeta$ by a short Dirichlet polynomial approximating $\zeta^{-1/2}$, a *mollifier*, so that mean values could detect sign changes.

Levinson (PAPER-0133) changed the counted object. He applied Littlewood's lemma to $G=\zeta+\zeta'/(f'(s)+f'(1-s))$ to the right of the line (THM-PAPER-0133-3, -4) and obtained $\kappa>1/3$ (THM-PAPER-0133-1).

**Record and decay** (CRIT frontier; LED-CRIT-4).
- $\kappa$ went:
  - 0.3474 (Levinson);
  - 0.4088 (Conrey 1989, PAPER-0191, with mollifier length $\theta=4/7-\varepsilon$ via Deshouillers–Iwaniec Kloosterman bounds, PAPER-0452);
  - 0.4105 (Bui–Conrey–Young, PAPER-0034);
  - 0.41492 (Pratt–Robles, PAPER-0076);
  - 0.417293962 (PRZZ, PAPER-0045, THM-PAPER-0045-1) [T].
- Feng's 0.4128 (PAPER-0046) contained a gap, closed only later (C3-D13(d)).
- The total gain after 1989 was $+0.0085$ in 31 years.

**Barriers.**
- **Length.** The twisted second moment allows $\theta<4/7$ for structured coefficients and $\theta<17/33$ for arbitrary ones (Bettin–Chandee–Radziwiłł, PAPER-0244). Even a conditional $\theta=1$ gives only 0.6107.
- **Error floor.** The mollified error is $\ge c/\theta$ (Radziwiłł, arXiv:1207.6583).
- **The limit case.** Farmer's $\theta=\infty$ conjecture (PAPER-0550) gives 100%, but Bettin–Gonek proved that it implies RH (PAPER-0064, THM-PAPER-0064-1, -2).
- **What is counted.** Even 100% allows $o(N(T))$ off-line zeros. The method counts zeros of an auxiliary function and never excludes an individual zero (C3-D9; failure category F13).

**Left open.** By 2020 the proportion of simple zeros on the line had plateaued near 0.4075. Under RH, the proportion of simple zeros was $19/27$ (PAPER-0049 with GLH; Bui–Heath-Brown, PAPER-0070, with RH alone).

---

## 5. 2026: pair correlation as a counting device (Alpöge–Furman, Lamzouri)

**Background.** Montgomery (1973, PAPER-0091) proved $F(\alpha)$ for $|\alpha|<1$ under RH (THM-PAPER-0091-1) and deduced that at least $2/3$ of zeros are simple (THM-PAPER-0091-3) [T|RH]. Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (PAPER-0053) made Montgomery's theorem unconditional by summing over all complex zeros (THM-PAPER-0053-1) [T].

**What changed.** Alpöge–Furman (PAPER-0486) proved unconditionally that at least $2/3$ of zeros are simple and on the line, and $0.6725007\ldots$ with the Montgomery–Taylor window. They also proved that at least $5/6$ (0.83625) are distinct (LED-CRIT-1) [AI-U; Lean formalisation claimed, not replayed here]. The arXiv comment says the proof was "discovered autonomously by Claude (Anthropic)" and verified by the authors. Verification inside the producing company is not independent.

**Mechanism.**
1. Restrict Weil's explicit-formula Hermitian form to about $N$ modulated windows.
2. On-line zeros give rank-one positive blocks. Off-line pairs give signature-$(1,1)$ blocks (Sylvester inertia).
3. The trace is $(1+o(1))N$. The Hilbert–Schmidt norm squared is $(R(\psi)+o(1))N$, from the unconditional Montgomery second moment.
4. A rank–trace inequality gives $N_0^s\ge(2-R(\psi)-o(1))N$.

No mollifier, density estimate or zero-free region is used.

**Corroboration.**
- Lamzouri gave an independent human proof (PAPER-0533) [U].
- Arias de Reyna (arXiv:2610.24612) reconstructed the proof. He judged one boundary step of v2 wrong as written, and repairable. The ledger verifier located a plausible candidate for the step and agrees it looks repairable.
- Knausgård (PAPER-0166; AI-assisted; Lean with three extra axioms) reached $0.67353820$ and $0.83900460$ [U].

**Obstacle overcome.** The mollifier-length barrier is bypassed: 0.6725 exceeds even the conditional $\theta=1$ output. Historically, the positivity object of §7 is here used not to prove positivity but as a **counting device**. Its inertia separates on-line from off-line contributions.

**Left open: a ceiling as sharp as the mollifier's.**
- **Bandwidth one.** Any certificate using only two trace moments with Fourier support in $[-1,1]$ is capped at $p_0\le0.6818287$ (interval-certified; LED-CRIT-10).
- **Higher traces.** These need prime-pair correlations, i.e. $F(\alpha)$ for $\alpha>1$, which Goldston–Montgomery (PAPER-0200) link to primes in short intervals.
- **Insensitivity.** The inputs are insensitive to $o(N)$ off-line zeros and hold for Davenport–Heilbronn and Epstein functions, so neither 100% nor RH is reachable without new arithmetic.
- **Conditionally,** the pair-correlation conjecture alone gives 100% (Goldston–Lee–Schettler–Suriajaya, arXiv:2503.15449).
- **Method exhausted.** B. Wang (arXiv:2609.24167) gains about $10^{-7}$ and writes that a new method is needed.

---

## 6. 1936–2026: statistical and random-matrix viewpoints

**What changed.** Probability entered through:
- primes (Cramér, PAPER-0147);
- values (Bohr–Jessen, PAPER-0363; Selberg's central limit theorem, PAPER-0356; Radziwiłł–Soundararajan, PAPER-0766);
- from 1973, zeros: Montgomery's $F(\alpha)$ matched the GUE pair correlation of Dyson's random-matrix theory (PAPER-0494) [std].

It became predictive:
- **Spacings.** Odlyzko found GUE spacings near zero number $10^{12}$, together with significant long-range structure (PAPER-0023, THM-PAPER-0023-1…4) [N].
- **$n$-level correlations** for $\sum|\xi_i|<2$ (Rudnick–Sarnak, PAPER-0112, PAPER-0014; THM-PAPER-0014-2) [T|RH].
- **Monodromy and symmetry types** in function fields (Katz–Sarnak, PAPER-0017, PAPER-0171; THM-PAPER-0017-2, -3) [T]. Tested for low-lying zeros under GRH with restricted support (Iwaniec–Luo–Sarnak, PAPER-0019; THM-PAPER-0019-1, -2).
- **Moment conjectures.** Keating–Snaith (PAPER-0013, THM-PAPER-0013-1), CFKRS (PAPER-0011) and the ratios conjectures (PAPER-0022, PAPER-0021) [H].

The moment conjectures organised the rigorous theory:
- **Upper bounds:** under RH, Soundararajan (PAPER-0012, THM-PAPER-0012-1) and Harper's sharp bounds (PAPER-0462) [T|RH]; unconditionally for $k\le2$ (Heap–Radziwiłł–Soundararajan, PAPER-0246) [T].
- **Lower bounds** for all $k>0$ (PAPER-0249, PAPER-0744) [T].
- **Short-interval maxima:** the Fyodorov–Hiary–Keating maxima (PAPER-0482, PAPER-0106), largely proved by Arguin–Bourgade–Radziwiłł (PAPER-0484) and Arguin–Hamdan (PAPER-0539).

**Obstacle overcome.** RMT supplied quantitative, falsifiable targets, such as the unproved sixth-moment constant 42 (Conrey–Ghosh, PAPER-0256). It also gave a structural reason to expect RH: an analogy with self-adjointness.

**What it cannot reach.**
- **Alternative Hypothesis.** Lagarias–Rodgers (PAPER-0103, THM-PAPER-0103-1) built a half-integer-gap sequence that reproduces *all* band-limited GUE correlations. So known correlation data cannot even force a normalised gap below $1/2$.
- **Models are not laws.** Maier's theorem refutes Cramér's model in short intervals (C3-D8, F12).
- **No implication for RH.** The predicted structures are consistent with RH but do not imply it.

---

## 7. 1916–2026: positivity criteria and reformulations

**What changed.** RH was recast as the non-negativity, closure or real-rootedness of an explicit object:
- **Arithmetic growth criteria:**
  - Riesz (PAPER-0118, THM-PAPER-0118-1, -2);
  - Franel–Landau (PAPER-0149, THM-PAPER-0149-1, -4);
  - Robin (PAPER-0206) and Lagarias (PAPER-0490);
  - Nicolas (PAPER-0232, PAPER-0008).
- **Weil's explicit-formula positivity** (PAPER-0473), sharpened by Bombieri (PAPER-0090, THM-PAPER-0090-1…3).
- **Li's criterion** (PAPER-0193; PAPER-0195; Voros, PAPER-0005).
- **Nyman–Beurling closure** (PAPER-0181, PAPER-0475), reduced by Báez-Duarte to integer dilations (PAPER-0004, THM-PAPER-0004-1).
- **Laguerre–Pólya and Jensen hyperbolicity** (PAPER-0438, PAPER-0440, PAPER-0487, PAPER-0152; Csordas et al., PAPER-0583, PAPER-0303). Griffin–Ono–Rolen–Zagier (PAPER-0024, THM-PAPER-0024-1, -2) [T] proved:
  - for each $d$, hyperbolicity for all large $n$;
  - for $d\le8$, hyperbolicity for all $n$.
- **De Bruijn–Newman heat flow:**
  - $\Lambda\le1/2$ (de Bruijn, PAPER-0409) [std];
  - Newman's conjecture $\Lambda\ge0$ (PAPER-0223) [std];
  - $\Lambda\ge0$ (Rodgers–Tao, PAPER-0036, THM-PAPER-0036-1; Dobner, PAPER-0333);
  - $\Lambda\le0.22$ (Polymath, PAPER-0083) and $\Lambda\le0.2$ (Platt–Trudgian, PAPER-0001, THM-PAPER-0001-3) [T, computer-assisted].

**Obstacle overcome.** These reformulations brought in Hilbert-space approximation, total positivity, real-rooted polynomials and heat-flow dynamics. They made partial RH quantitative: $\Lambda\in[0,0.2]$, with RH $\Leftrightarrow\Lambda=0$.

**What they left open.** Every unconditional result lies in one of three regimes, none of which touches RH (POS frontier):
1. **Archimedean-only windows** containing no prime. Weil positivity is proved only for support in $[2^{-1/2},2^{1/2}]$ (Yoshida; Connes–Consani, PAPER-0099, THM-PAPER-0099-1, -2). Zhu's certified window 0.8, where 2 and 3 enter, is [U] (arXiv:2608.24827).
2. **Corollaries of zero verification,** scaling like $T^2$. Examples are Li's $\lambda_n\ge0$ and Jensen hyperbolicity up to about $T_0^2$.
3. **Asymptotic tails** that have "forgotten" the zeros.

The negative results are sharp:
- **Heat flow.** $\Lambda\ge0$: RH, if true, holds only barely, and no heat-flow argument can start from negative time. Polymath's heuristic: RH verified to height $T$ gives at best $\Lambda\lesssim C/\log T$ [H].
- **Jensen tails** hold for RH-violating functions (Farmer, PAPER-0686; Kim–Lee 2022). Audit F6 found two minor numerical errors in Farmer's table that do not affect the conclusion.
- **Li coefficients** detect an off-line zero at height $T$ only for $n\gtrsim T^2$ (Voros, Exp. Math. 2020).
- **Nyman–Beurling** approximations converge no faster than $(C/\log N)^{1/2}$ (Burnol, PAPER-0606).
- **Stronger sufficient conditions are false:**
  - Mertens's conjecture (PAPER-0432), refuted by Odlyzko–te Riele (PAPER-0199), as Ingham's analysis anticipated (PAPER-0071, THM-PAPER-0071-1, -2);
  - Pólya's conjecture (PAPER-0488), refuted by Haselgrove (PAPER-0489);
  - Turán's partial-sum hypothesis, refuted by Montgomery (PAPER-0660).

  These are the archetypes of C3's failure categories F4 and F5.

The common lesson is that each criterion needs uniform cancellation in the prime comb $\sum\Lambda(n)n^{-1/2}\hat g(\log n)$, which is as hard as zero information.

---

## 8. 1949–2026: spectral, operator and noncommutative-geometric programmes

**What changed.** The Hilbert–Pólya idea, folklore with no reliable primary source, acquired rigorous models in neighbouring settings.
- **Selberg's trace formula** (PAPER-0353; Hejhal, PAPER-0187, PAPER-0646) gives zeta functions whose zeros are spectral. They satisfy an RH analogue apart from finitely many zeros coming from small eigenvalues [std].
- **Hecke's converse theory** (PAPER-0151) carries a warning: for $\lambda>2$ the functional equation has infinitely many independent solutions (THM-PAPER-0151-1). A functional equation without arithmetic determines nothing.

Programmes for $\zeta$ itself:
- **Lax–Phillips scattering** (PAPER-0387), whose RH criterion its authors judged thrown back onto number theory;
- **de Branges spaces** (PAPER-0394, PAPER-0320);
- **$H=xp$** (Berry–Keating, PAPER-0500, PAPER-0196);
- **the Bender–Brody–Müller operator** (PAPER-0502);
- **canonical systems** (Lagarias, PAPER-0275; Suzuki, PAPER-0812, PAPER-0101);
- **Connes's noncommutative geometry:**
  - the adelic trace formula, PAPER-0345, PAPER-0026;
  - the Bost–Connes system, PAPER-0499;
  - the arithmetic and scaling sites, PAPER-0111, PAPER-0086;
  - $\zeta$-cycles, PAPER-0117;
  - prolate operators, PAPER-0109, PAPER-0545;
  - Weil-form ground states, PAPER-0144, PAPER-0544.

**Obstacle overcome: unconditional spectral realisations.**
- Connes realises the critical zeros as an absorption spectrum (THM-PAPER-0026-1, -2).
- Meyer realises all zeros in non-Hilbert spaces (PAPER-0074).
- Connes–Consani realise the critical zeros on $\zeta$-cycles (THM-PAPER-0117-2).
- Connes–van Suijlekom (CMP 2025; THM-PAPER-0144-1) proved: if the lowest eigenvalue of a finite-window Weil form is simple, isolated and even, then its ground state's Mellin transform has only real zeros. Finite windows reproduce low zeros numerically (PAPER-0544).

**What they cannot yet reach.** Realisations exist without RH, so they carry RH content only when positivity is added. The OPS frontier finds that every route ends in one RH-equivalent positivity, in one of five guises:
- Weil positivity;
- Hermite–Biehler membership;
- canonical-system boundary behaviour;
- Lax–Phillips decay;
- positivity of an intertwiner.

Closed routes:
- **De Branges.** His positivity conditions fail for $\xi$ (Conrey–Li, PAPER-0779). C3 Arb-replicated the failure at the 34th zero and found failures at 13.62% of the first 20,000 zeros (C3-D1).
- **Bender–Brody–Müller.** The operator has deficiency indices $(1,0)$ (Bellissard; C3-D4).
- **Yakaboylu** (PAPER-0095). Audit F1: `verified_error`.
- **Connes's 1999 Theorem 5.** The trace-formula equivalence is proved only in positive characteristic (audit F5).

The remaining gaps in the Weil-ground-state programme:
1. simplicity and evenness of the ground state for windows containing many primes;
2. convergence of ground states to $\xi$ in Mellin-controlling norms;
3. a non-circular lower-bound form of estimates that currently assume $Q_W\ge0$.

At fixed window the agreement fails near height $t\approx3100$ (Andrews–Connes–La Gatta §7.3, per the OPS frontier).

---

## 9. 1924–1980: function-field geometry and the transfer problem

**What changed.**
- Artin (PAPER-0154) introduced zeta functions of quadratic function fields (THM-PAPER-0154-1, -2).
- Hasse proved RH for elliptic curves (PAPER-0407, PAPER-0396, PAPER-0139). The decisive fact is that the degree is a positive-semidefinite quadratic form on endomorphisms (THM-PAPER-0139-1, -2).
- Weil proved RH for all curves (announced PAPER-0397, PAPER-0375; proofs PAPER-0176, PAPER-0421) [std]. The proof uses positivity of an intersection form on $C\times C$. He then stated the Weil conjectures (PAPER-0414).
- Dwork proved rationality (PAPER-0508, PAPER-0141).
- Grothendieck supplied the cohomological frame (PAPER-0509). His standard conjectures (PAPER-0715), after Serre's Kähler analogue (PAPER-0824), would derive RH from a Hodge-type positivity.
- Deligne proved the Weil conjectures (PAPER-0496, PAPER-0515) by monodromy and a tensor-power argument, bypassing the standard conjectures [std].
- Stepanov's method, presented by Bombieri (PAPER-0131, THM-PAPER-0131-1, -2), gave an elementary proof for curves. It uses auxiliary polynomials forced by Frobenius to vanish to high order.

**What transferred.**
- **Exponential sums.** Weil's Kloosterman bound (PAPER-0403) and Deligne's bounds became analytic inputs. Through Deshouillers–Iwaniec (PAPER-0452) they fed the mollifier lengths of §4.
- **Ramanujan.** Ramanujan's conjecture followed from the Weil conjectures (PAPER-0829).
- **Statistics.** Katz–Sarnak carried the statistical side over to number fields as conjectures (§6).
- **Families.** Function-field family conjectures became testable (Andrade–Keating, PAPER-0128; audit F4: `correct_but_misinterpreted`).

**The transfer problem.** Weil and Deligne use three things that $\operatorname{Spec}\mathbb Z$ lacks:
1. Frobenius on a finite-dimensional cohomology;
2. the surface $C\times C$;
3. a Castelnuovo–Severi / Hodge-index positivity on it.

Connes's programme seeks substitutes:
- the adele class space for the curve;
- the scaling flow for Frobenius;
- the arithmetic site, $\mathbb F_1$-geometry and the Riemann–Roch strategy for the surface and its positivity (PAPER-0119, PAPER-0116, PAPER-0501, PAPER-0080).

The Weil-form ground states of §8 are the analytic face of the missing positivity. No substitute for item 3 exists. Where the global trace-formula equivalence is a theorem, it is in positive characteristic.

---

## 10. 1903–2026: computation, certification and formalisation

**Four steps.**
1. **Isolation.** Gram (PAPER-0408, PAPER-0412) and Backlund (PAPER-0752, PAPER-0364) located zeros. The Riemann–Siegel formula (PAPER-0415; Titchmarsh, PAPER-0261; Gabcke, PAPER-0188) reached higher.
2. **Completeness.** Turing's method (PAPER-0416, PAPER-0474), corrected by Lehman (PAPER-0613) and improved by Trudgian (PAPER-0594), certifies that *all* zeros to a height have been found. It still underlies every complete verification: 75,000,000 zeros (Brent, PAPER-0088, THM-PAPER-0088-1) and $1.5\times10^9$ (PAPER-0047, THM-PAPER-0047-1).
3. **Amortisation.** Odlyzko–Schönhage (PAPER-0214) enabled Odlyzko's statistics (PAPER-0023, PAPER-0198) and Gourdon's $10^{13}$ zeros (PAPER-0481) [N, floating point]. Hiary's $t^{4/13}$ algorithm (PAPER-0647) reached windows near zero number $10^{36}$ (PAPER-0767).
4. **Certification.**
   - Rigorous computation (Rosser–Yohe–Schoenfeld, PAPER-0372) and ball arithmetic (Johansson, PAPER-0674).
   - Platt's isolation of $1.04\times10^{11}$ zeros (PAPER-0577).
   - GRH for $q\le400{,}000$ to moderate height (PAPER-0040, THM-PAPER-0040-1, -2).
   - **RH for $0<\gamma\le3{,}000{,}175{,}332{,}800$** (Platt–Trudgian, PAPER-0001, THM-PAPER-0001-1), at about $7.5\times10^6$ core-hours [N, certified].
   - No exceptional zeros for $q\le10^{10}$ (Lu–Zaman–Zhao, PAPER-0855).

**A fifth step: formalisation.**
- Mathlib contains $\zeta$, Dirichlet $L$-functions and a formal statement of RH (Loeffler–Stoll, PAPER-0552). PNT+ formalises prime-number-theorem technology (PAPER-0904).
- In 2026 Lean proofs were claimed for the Alpöge–Furman theorem, the 7/8 half-plane and Kimura's Siegel constant. The Observatory replayed none.

**Obstacle overcome.** Evidence became theorems about finite ranges, which feed explicit number theory. For example, RH to $H$ gives Schoenfeld-strength bounds up to about $H^2$ (THM-PAPER-0001-2) and enters the bounds on $\Lambda$.

**What computation cannot reach.**
- No finite height implies RH. $S(t)$ is unbounded, and its large values lie beyond rigorous reach.
- Cost is linear in $H$.
- No certificate is cheaper to check than the run, and the $3\times10^{12}$ run has no independent replication.
- Published constants carry errors:
  - Turing's errors, corrected by Lehman;
  - Cheng–Graham's $1/\pi$ for the sharp $2/\pi$, for which C3 certified a counterexample (C3-CG1), repaired by Hiary–Patel–Yang (PAPER-0242);
  - Ford's 8.463 → 8.464;
  - audit F7's findings.

  Explicit-constant chains need machine-checkable provenance (C3-D13, F14).

---

## 11. 2026: the AI-era developments

Two autumn-2026 claims change the frontier of **zero-free regions**. Both are AI-generated and unrefereed, and neither bears on the critical line.

### 11.1 Quasi-RH via cubic theta and a quadratic large sieve

**Claims.**
- **11/12.** OpenAI's "The Quasi-Riemann Hypothesis" (5 Oct 2026, PAPER-0161; human-edited; not formalised) claims that every finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$, hence every Dirichlet $L$-function and $\zeta$, is zero-free in $\Re s>11/12$ [AI-U].
- **7/8.** A 199-page companion (PAPER-0528) claims $7/8$. It comes with a Lean comparator statement `riemannZeta s ≠ 0` for $7/8<\Re s$ [AI-U; not replayed].

**Mechanism of the 11/12 proof** (DOSSIER §1.1, §4). The load-bearing estimate is a sextic-twisted Möbius mean square,
$$\sum_{N(u)\le D^{1+\vartheta}}|A_u(D)|^2\ll D^{2+\vartheta+\varepsilon},\qquad A_u(D)=\sum\mu(\mathfrak n)\nu(\mathfrak n)\big(\tfrac{u}{\mathfrak n}\big)_6W(N\mathfrak n/D).$$
It is proved in four steps:
1. Poisson duality turns the sum into sextic Gauss sums.
2. The Gauss–Jacobi identity eliminates $\mu$, leaving cubic Gauss sums. These are Fourier coefficients of Patterson's cubic theta function (as transcribed in Dunn–Radziwiłł, PAPER-0960).
3. Cubic-theta automorphy, with the Kubota multiplier, reflects the problem into a *quadratic* family, where an optimal quadratic large sieve applies (Goldmakher–Louvel).
4. A two-Poisson transfer and a finite induction finish the proof.

An extraction lemma converts the mean square into $\beta\le\frac12+\frac{h(n-1)}{2n}$, which is $11/12$ at $n=6$, $h=1$.

**Obstacle overcome.**
- **Parity without a sieve.** The estimate is parity-sensitive, so no sieve can give it. Parity information enters through an algebraic identity and automorphy instead. The DOSSIER compares this to Heath-Brown and Patterson's treatment of cubic Gauss sums at primes (J. reine angew. Math. 310, 1979), run in reverse.
- **Euler product.** Multiplicativity is used at four load-bearing points, so there is no conflict with Davenport–Heilbronn.
- **The jump.** A 68-year-frozen region shape becomes a fixed half-plane.

**Status.**
- **Audits of 11/12.** Observatory Level-2 section audits (AI agents) of every line of the 11/12 proof found no verified error and about 35 harmless presentation items. They settled the Kubota-multiplier sign numerically. Patterson's coefficient formula and Goldmakher–Louvel were imported, not re-proved.
- **7/8** is unaudited here.
- **Follow-ups.** All improvements below 7/8 import the 7/8 paper's inputs:
  - Liu, PAPER-0156: 0.874957…;
  - Liu, PAPER-0157: 0.874886647… over every number field, also resting on another unreviewed OpenAI preprint;
  - Xu–Sang, PAPER-0158;
  - Chang–Wang, PAPER-0163.

  The one independent route is Ji's quartic argument over $\mathbb Q(i)$ (PAPER-0155). It gives only $599/600$ and itself rests on an unrefereed density estimate.
- **Reception.** Secondary reports say experts "largely agree" the 11/12 proof is correct. Sarnak withholds "Theorem" status.

**What it leaves open.**
- **Floors.**
  - In the 11/12 architecture the large-sieve barrier forces $h\ge1$, so $11/12$ is the floor for sextic rows. Orders $n<6$, which would give better floors, are those with no known automorphic substitute.
  - The 7/8 comparison system $B(\ell)=11/12-\ell/4$, with $\ell<1-|b|$, has a floor strictly above $2/3$. Liu's optimality theorems are optima of a fixed system.
  - Generic sieves give nothing.
  - Reaching $1/2$ needs GRH-strength family inputs.
- **Consequences if correct** (DOSSIER §3, partly the dossier's own derivations):
  - effective $\psi(x)=x+O(x^\Theta\log^2x)$;
  - effective Siegel–Walfisz;
  - Lindelöf to the right of $\Theta$;
  - $n(p)\ll(\log p)^{1/(1-\Theta)+\varepsilon}$.
- **Not implied:**
  - RH or GRH;
  - density on $(1/2,\Theta]$;
  - better short-interval or Bombieri–Vinogradov exponents;
  - anything for GL(2).

### 11.2 Landau–Siegel exclusion via interpolation determinants

**Claim.** OpenAI's "Uniform exclusion of Landau–Siegel zeros" (PAPER-0529) claims that there is an absolute $c>0$ with $(1-\beta)\log q\ge c$ for every real zero $\beta$ of every primitive real $L(s,\chi)$ [AI-U; Lean claimed, not replayed]. Its proof is independent of QRH. The statement would also follow trivially from 7/8, with $c=(\log3)/8$.

**Mechanism** (SIEGEL §2–3). All four proofs share three layers:
1. **Analytic.** A real zero near 1 forces inert primes ($\chi(p)=-1$) to carry almost all of $\sum\log p/p$ up to $q^A$.
2. **Arithmetic: unconditional, and new.** Frobenius at an inert prime acts on $\mathbb Z[\sqrt d]$ as conjugation. This forces high divisibility of one of three objects:
   - an interpolation determinant (OpenAI);
   - a pigeonholed auxiliary function controlled by Masser's zero estimate (Kerr, PAPER-0164);
   - a lattice index (Guo, PAPER-0165).

   So inert primes carry at most a fraction $\kappa<1$ of the mass: $\kappa=13/16$, $39/40$ or $11/20$ respectively.
3. **Comparison.** The two layers contradict each other.

**Obstacle overcome.** The classical de la Vallée Poussin–Landau method cannot remove a single real zero, for an intrinsic reason (Zhang 2022, PAPER-0852, §1). Siegel's theorem (PAPER-0720) is ineffective. The best effective bound was $h(-d)\gg\log|d|$ (Goldfeld, PAPER-0135; Gross–Zagier, PAPER-0835). The missing input came from transcendence methods. Our own reading [interpretation] is that this continues the Stepanov–Bombieri use of Frobenius to force vanishing or divisibility (§9).

**Corroboration.** Human re-proofs give explicit constants:
- Banks (PAPER-0160): $3.0\times10^{-3}$;
- Guo: $1/100$, with no complex analysis;
- Kimura (arXiv:2610.21511): $5.8\times10^{-4}$, Lean, as reported;
- Green (PAPER-0547): "arguments all due to ChatGPT".

The Observatory's architecture audit found no gap. It also derived, on its own and not from the sources, $L(1,\chi)\ge0.00767/\log q$ for $q\ge10$: an effective Siegel theorem.

**What it leaves open.** The result is a gap at $s=1$, not GRH. It does not lower Linnik's $L=5$. Conditional "illusory-world" theorems, such as Heath-Brown's twin-prime result under Siegel zeros (PAPER-0685), become vacuous.

### 11.3 The epistemic change

1. **Old tools, new targets.** Metaplectic theta functions and transcendence determinants had been studied extensively but not aimed at these problems.
2. **Formal verification as primary evidence.** A replay would certify the zeta and Dirichlet 7/8 statements independently of the exposition, but not the 11/12 argument (DOSSIER §1.3).
3. **A new verification regime.** Bulk release, crowd re-proof, AI-agent audits and press reception all preceded refereeing. The archive treats them as evidence of plausibility and adoption, not as review.

---

## 12. Patterns

- **Every method bounds something other than "zeros off the line".**
  - Zero-free regions bound the rightmost zero.
  - Density bounds the number of zeros far out.
  - Mollifiers and rank–trace count a proportion.
  - Criteria test finite windows.
  - Computation verifies a finite height.

  The passage from "few", "most" or "up to $T$" to "none" has never been made. C3's failure categories F13, F5 and F4 name the corresponding mistakes.
- **Ceilings are now theorems about methods.** Examples:
  - the mollifier error $c/\theta$;
  - the cap $0.6818$;
  - the tangency at $7/10$;
  - Kakeya-hardness of the $\ell^q$ large-values conjecture;
  - the $h\ge1$ floor;
  - $\Lambda\ge0$;
  - the compatibility of the Alternative Hypothesis with all band-limited correlation data.

  This method-limit literature is the decade's most distinctive development.
- **The Euler-product test discriminates.** Functional-equation-only arguments, Jensen tails, generic sieves and the current rank–trace inputs all pass the Davenport–Heilbronn function, and so cannot prove RH. The 2026 quasi-RH proof uses multiplicativity *and* automorphy.
- **Geometry proved an RH, over $\mathbb F_q$.** The positivity that made it work has no arithmetic substitute.

---

## 13. What each method can and cannot reach

| Method (era) | Representative works | Best reach (status) | Cannot reach / documented barrier |
|---|---|---|---|
| Complex-analytic foundations: continuation, Hadamard product, explicit formula (1859–1905) | PAPER-0469, 0137, 0077, 0136, 0030 | Exact zeros ↔ primes dictionary; $N(T)$ with $O(\log T)$ error; RH ⇒ $\pi(x)=\mathrm{Li}(x)+O(\sqrt x\log x)$ [T] | Locates no zero. Product formulas take zeros as input (C3-M1, F11). The functional equation is compatible with off-line zeros (PAPER-0417; Hecke PAPER-0151). |
| Zero-free regions via positivity and exponential sums (1896–2026) | PAPER-0009, 0044, 0078, 0447, 0448, 0051, 0010, 0159 | VK shape [T]; $R=5.558691$ [T]; $4.896$ [U] | Shape frozen 68 years; needs cancellation for $N=\exp((\log t)^{2/3+\delta})$; Beurling examples cap Euler-product-only arguments at dlVP; no fixed $\sigma<1$ by these means. |
| Mean values and moments (1918–2026) | PAPER-0120, 0121, 0124, 0359, 0702, 0012, 0462, 0246, 0249 | Asymptotics $k=1,2$ [T]; order of magnitude: lower all $k>0$, upper $k\le2$ [T], all $k$ [T\|RH] | $k>2$ upper bounds need a Lindelöf-strength anchor; sixth moment needs ternary additive divisor sums (PAPER-0110); all moments $\ll T^{1+\varepsilon}$ ⇔ Lindelöf. |
| Exponential sums, large values, zero density (1921–2026) | PAPER-0444, 0441, 0213, 0312, 0130, 0089, 0054, 0466 | $\sup A=30/13$; DH for $\sigma\ge25/32$; $\mu(\frac12)\le13/84$; primes in $[x,x+x^{17/30+\varepsilon}]$ [T] | DH is the sharp target, so density never gives RH; tangency at $7/10$; $\ell^2$ counterexample; $\ell^q$ conjecture ⇒ Kakeya. |
| Mollifiers on the critical line (1942–2020) | PAPER-0413, 0133, 0191, 0034, 0046, 0076, 0045, 0244 | $\kappa>0.417293962$ [T] | $\theta<4/7$ (structured), $17/33$ (arbitrary); error $\ge c/\theta$; $\theta=\infty$ ⇒ RH (PAPER-0064); 100% ≠ RH. |
| Pair correlation / rank–trace on Weil's form (1973; 2024–2026) | PAPER-0091, 0053, 0486, 0533, 0166 | 2/3 simple [T\|RH, 1973]; 0.6725 simple and critical unconditionally [AI-U + U, two proofs]; 0.67354 [U] | Bandwidth-one cap 0.6818; higher traces need $F(\alpha)$ for $\alpha>1$; blind to $o(N)$ off-line zeros; holds for Davenport–Heilbronn/Epstein. |
| Random-matrix / statistical models (1936–2026) | PAPER-0147, 0494, 0023, 0112, 0014, 0017, 0013, 0011, 0484 | Precise conjectures [H]; $n$-level correlations, $\sum\|\xi\|<2$ [T\|RH]; function-field symmetry [T]; FHK maxima [T] | Models are not laws (Maier vs Cramér); band-limited data compatible with AH (PAPER-0103); nothing about individual zeros. |
| Weil / Li / Bombieri positivity (1952–2026) | PAPER-0473, 0090, 0193, 0195, 0005, 0099 | Weil positivity on the prime-free window [T]; $\lambda_n\ge0$ for $n\lesssim T_0^2$ via verification | Prime-containing windows need comb cancellation equivalent to zero information; certificates cost doubly exponentially in the window (Zhu [U]); Li sees height $T$ only for $n\gtrsim T^2$. |
| Nyman–Beurling / Báez-Duarte (1950–2013) | PAPER-0181, 0475, 0004, 0606, 0291 | Exact Hilbert-space equivalence [T] | $d_N\gtrsim(\log N)^{-1/2}$ (Burnol): slow convergence; finite $d_N$ certifies nothing. |
| Jensen / Laguerre–Pólya (1913–2026) | PAPER-0440, 0487, 0583, 0024, 0087, 0686, 0429 | All large $n$ for each $d$; all $n$ for $d\le8$ [T] | Tails hold for RH-violating functions; $n=0$ for all $d$ is the RH-critical regime. |
| De Bruijn–Newman (1950–2026) | PAPER-0409, 0223, 0036, 0333, 0083, 0001 | $0\le\Lambda\le0.2$ [T]; $\approx0.15$ [U]; $\le0.14$ conditional on 7/8 [U] | $\Lambda\ge0$ leaves no slack; verification gives $\Lambda\lesssim C/\log T$ [H]; $\Lambda=0$ is RH. |
| Arithmetic criteria: Robin, Mertens, Pólya, Turán (1897–2026) | PAPER-0206, 0490, 0590, 0432, 0199, 0071, 0489, 0660, 0786 | Robin verified to $10^{10^{13.11}}$ [N]; Mertens refuted [T] | Finite only; stronger sufficient conditions false (F4); Skewes-scale first failures (F5). |
| Spectral / operator / NCG (1956–2026) | PAPER-0353, 0387, 0394, 0779, 0500, 0026, 0074, 0117, 0109, 0144, 0544 | Unconditional spectral realisations; Selberg-zeta RH analogue up to small eigenvalues [std]; finite-window ground-state real-rootedness given simplicity [T] | No RH content without positivity; de Branges conditions false; BBM not self-adjoint; trace formula ⇔ RH only in char $p$ (F5); ground-state convergence and lower bounds missing. |
| Function-field geometry (1924–1980) | PAPER-0154, 0139, 0176, 0414, 0509, 0715, 0496, 0515, 0131 | RH for curves and smooth projective varieties over $\mathbb F_q$ [T] | Transfer problem: no Frobenius cohomology, no $\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z$, no Hodge-index positivity; statistics transfer, positivity does not. |
| Computation and certification (1903–2026) | PAPER-0474, 0613, 0088, 0047, 0214, 0481, 0577, 0001, 0040, 0855 | RH to $\gamma\le3.0\times10^{12}$ [N, certified]; GRH $q\le4\times10^5$ (moderate height); no exceptional zero for $q\le10^{10}$ | Finite only; linear cost; no cheap certificate or replication; constant errata (C3-D13). |
| Formalisation (2024–2026) | PAPER-0552, 0904; Lean claims for PAPER-0486, 0528, Kimura | Formal RH statement; claimed kernel-checked 2026 proofs (not replayed) | Checks against definitions, not their fidelity (e.g. custom Hecke `LFunction`, DOSSIER §1.3); extra axioms escape the kernel (Knausgård). |
| Metaplectic quasi-RH (2026) | PAPER-0161, 0528, 0156, 0157, 0158, 0163, 0155, 0960 | $\Re s>11/12$ (audited here, no error found), $7/8$, $\approx0.8749$ [AI-U; follow-ups U, conditional] | Floor 11/12 (sextic, $h\ge1$); 7/8-system floor $>2/3$; no substitute for $n<6$; generic sieves useless; $1/2$ needs family GRH; silent near $\Re s=\frac12$. |
| Interpolation-determinant Siegel exclusion (2026) | PAPER-0529, 0160, 0164, 0165, 0547 | $(1-\beta)\log q\ge c$, $c$ up to $1/100$ [AI-U + four human re-proofs, U] | Gap at $s=1$ only; not GRH; Linnik's $L=5$ unchanged. |

---

*Limitations.*
- Topics thinly represented in the corpus are compressed: sieve theory, functoriality, and the Selberg class beyond the degree classification (PAPER-0033, PAPER-0192, PAPER-0670).
- Content attributed to L0/L0+ works rests on standard knowledge [std]. These include Riemann, Selberg 1942, Carlson, de Bruijn, Newman, Weil's curve proof, Deligne's Weil I/II and Turing.
- Press quotations are secondary and come from the archive's notes.
- Nothing here upgrades the status of any 2026 claim.

