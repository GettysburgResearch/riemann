# Abandoned, refuted and stalled approaches to the Riemann Hypothesis

```text
Status: EXPLORATORY / HISTORICAL SYNTHESIS (archive layer). The file combines imported literature statements
        with findings already made inside this archive:
          - campaign C3 (failure anatomy) and its independent skeptic review;
          - the Level-2/3 audits F1 (Yakaboylu), F5 (Connes Thm 5), F6 (Farmer Table 4.1) and F7 (BTY constant).
        No new theorem is claimed. RH is open. No case below is evidence for or against RH beyond the exact
        statement of the theorem cited for it.
Scope: 16 case sections, classical zeta unless stated. Each case has one of four kinds:
          - REFUTED: a statement stronger than RH, or sufficient for it, was shown false.
          - FAILED: a proof attempt has an identified invalid step.
          - CLOSED: a theorem shows the hoped-for route cannot work.
          - STALLED: the mathematics is correct, but its remaining step is RH-equivalent or out of reach.
        Annexes cover repaired explicit constants, a re-check log against C3, and items deliberately left
        uncharacterized.
Exact sources or dependencies:
        corpus/bibliography.jsonl (every PAPER-#### id below was looked up there).
        theorems/theorems.jsonl: THM-PAPER-0004, -0005, -0006, -0007, -0024, -0026, -0034, -0036, -0045, -0046,
          -0064, -0071, -0083, -0087, -0095, -0114, -0115, -0133, -0145, -0147.
        papers/PAPER-0064.md, PAPER-0004.md, and the L0/L0+ records named in the text.
        proposals/independent_campaigns/C3-failure-anatomy/REPORT.md and SKEPTIC_REVIEW.md
          (data manifest: experiments/results/C3-failure-anatomy/manifest_C3.json).
        audits/L2_flag_audits/: F1-yakaboylu.md, F5-connes-thm5.md, F6-farmer-table.md, F7-bty-constant.md,
          F8-dbn-claims.md, and F3-yang-constant.md (used only to exclude it).
        audits/claims_2026/CRIT23/DOSSIER.md.
        frontiers/ledger.jsonl: LED-ARITH-1, 7, 8, 9, 20; LED-CRIT-5, 8, 9, 17; LED-OPS-13, 14, 17, 18, 19;
          LED-POS-16, 18.
        frontiers/research_programs.md (sections ARITH, CRIT, DBN, OPS, POS).
        history/recent_developments_2024_2026.md.
        Primary texts re-opened for this file, from cached arXiv text layers:
          - Farmer arXiv:2008.07206v2 (Secs. 1, 2, 4.1-4.2, Table 4.1);
          - Conrey-Li arXiv:math/9812166 (Secs. 1 and 4, Sarnak's remark, reference list);
          - Bellissard arXiv:1704.02644 (pp. 1-3);
          - Platt-Trudgian arXiv:1507.01340 (Sec. 1);
          - Banks-Ford-Tao arXiv:1908.08613 (Secs. 1.1-1.2, 2.5);
          - Radziwill arXiv:1207.6583v3 (Sec. 1);
          - Bettin-Chandee-Radziwill arXiv:1411.7764 (Sec. 1).
What was actually run: reading and cross-checking only. No zeta value was newly computed. A few elementary
        constants are marked "derived here" in the text: (2 + gamma - log 4 pi)/log N, 2 e^{-gamma},
        1/2 + 1/(2 theta), T^2 for T = 3,000,175,332,800, and 1/zeta(1/2). They were evaluated by hand or in
        double precision with python3 -I. Every certified number is quoted from the archive file named next to
        it, and keeps that file's rigour label.
Smallest remaining gap:
        (i) Several primary texts are known here only at L0/L0+ (index or review level): Stieltjes 1885,
            Mertens 1897, Polya 1919, Turan 1948, Haselgrove 1958, Lehman 1960, Montgomery 1983, Maier 1985,
            Odlyzko-te Riele 1985, de Branges 1986/1992/1994, Lax-Phillips 1976, Berry-Keating 1999,
            Farmer 1993, Conrey 1989, Endres-Steiner 2010 (the last is not in the corpus).
        (ii) The following were not audited and are not characterized: arXiv:0807.0090 v5-v10 (2024-2025),
            de Branges' post-2004 manuscripts, and the 2026 quasi-RH claims (active, not abandoned).
        (iii) The countermodel and "proves-too-much" tests in Sec. 20 are methodological heuristics, not theorems.
        (iv) The one substantive correction made here to C3 is in Sec. 14: the theta = infinity hypothesis is
            itself RH-strength (Bettin-Gonek). It rests on the L1 reading of PAPER-0064 already in this archive.
            The journal text was not re-opened in this pass.
```

## 0. Conventions

### Claim-status labels

Every cited statement carries one of these labels.

| Label | Meaning |
|---|---|
| THEOREM | Proved in a refereed publication. |
| THEOREM (unrefereed) | A complete proof in a preprint that has not been refereed. |
| CONDITIONAL | Proved under a stated hypothesis. |
| HEURISTIC | A statement from a model, a semiclassical argument or a numerical pattern. |
| COMPUTATION (rigorous) | Interval (Arb) or exact-integer arithmetic. |
| COMPUTATION (non-rigorous) | Floating point, or high precision without an enclosure (methodology §8). |
| WITHDRAWN | Withdrawn by the author. |
| AI-DISCOVERED, UNREFEREED | AI provenance disclosed by the authors. |
| OBSERVATORY FINDING | Produced inside this archive, either by C3 plus its independent skeptic or by an L2 audit plus an L3 adjudication. It has not been externally refereed. |

### Fairness rule

This file follows methodology §6. An error is described only when at least one of the following holds, and each case file names which:

- **(a)** the author published a correction or a withdrawal;
- **(b)** a published or public critique identifies the failing step, and the identification can be checked against the text;
- **(c)** an Observatory finding supplies an explicit witness, produced independently of the agent that first raised the issue.

Some programmes contain no identified error: Berry–Keating, Bender–Brody–Müller, Connes, Lax–Phillips, Nyman–Beurling and Jensen. They are described as stalled, conditional or closed, never as wrong. Annex C lists the items deliberately left uncharacterized.

### Failure-mode tags

The tags F1–F15 come from C3-TAX. They are tags, not a partition (skeptic correction). One case can carry several.

| Tag | Failure mode |
|---|---|
| F1 | Uses only properties shared with a countermodel. |
| F2 | A hypothesis is never used ("proves too much"). |
| F3 | A hidden RH-equivalent step. |
| F4 | An over-strong sufficient condition that is false. |
| F5 | Extrapolation from finite data to an infinite statement. |
| F6 | Non-uniform limits. |
| F7 | A gap in domain, self-adjointness or normalizability. |
| F8 | A support of measure zero. |
| F9 | An undefined or inconsistent object. |
| F10 | An inequality used in the wrong direction. |
| F11 | Arguments that use factorization only. |
| F12 | A heuristic model treated as a law. |
| F13 | A density statement read as "all". |
| F14 | Bookkeeping errors in explicit constants. |
| F15 | Revision instability. |

## 1. Summary

| § | Approach | Kind | Decisive source | Tags |
|---|---|---|---|---|
| 3 | Mertens: $\lvert M(x)\rvert<\sqrt x$ for $x>1$ (1897) | REFUTED | Odlyzko–te Riele 1985 (PAPER-0199) | F4, F5 |
| 3 | Stieltjes: $M(x)=O(\sqrt x)$ (1885) | open; expected false | Ingham 1942 (PAPER-0071) | F4 |
| 4 | Pólya: $L(x)\le0$ for $x\ge2$ (1919) | REFUTED | Haselgrove 1958 (PAPER-0489); Lehman 1960 (PAPER-0772) | F4, F5 |
| 4 | Turán: $T(x)=\sum_{n\le x}\lambda(n)/n>0$ for large $x$ | REFUTED | Haselgrove 1958; Borwein–Ferguson–Mossinghoff 2008 (PAPER-0616) | F4, F5 |
| 5 | Turán: $\zeta_N$ has no zero in $\sigma>1$ for all large $N$ | REFUTED | Spira 1968; Montgomery 1983 (PAPER-0660); Platt–Trudgian 2016 | F4 |
| 6 | de Branges positivity for $E(z)=\xi(1-iz)$ | REFUTED (the conditions are false) | Conrey–Li 2000 (PAPER-0779) | F4 |
| 7 | Jensen polynomials of $\Xi$ as a route to RH | STALLED (meta-negative analysis) | Farmer 2022 (PAPER-0686) | F1, F5 |
| 8 | Heat flow with room to spare ($\Lambda<0$) | CLOSED | Rodgers–Tao 2020 (PAPER-0036) | none |
| 9 | Nyman–Beurling (and Li) numerics as evidence | STALLED | Báez-Duarte–Balazard–Landreau–Saias 2000 (PAPER-0216); Burnol 2002 (PAPER-0606) | F5 |
| 10 | Berry–Keating $H=xp$ | HEURISTIC; no realization with RH content | Endres–Steiner 2010 (via LED-OPS-17) | F7 |
| 11 | Bender–Brody–Müller 2017 | CONDITIONAL programme with an unfilled gap | Bellissard 2017 (PAPER-0813) | F7 |
| 12 | Yakaboylu 2024 | Stage-II claim is a verified error | audit F1 (L2 + L3) | F1, F3, F7 |
| 13 | Connes's trace formula; Lax–Phillips | STALLED (the theorems are correct) | audit F5; Conrey–Li §1 | none |
| 14 | Mollifier methods as a route to RH | CLOSED as a route to RH; active as a density method | structure of Levinson's method; Bettin–Gonek 2017 (PAPER-0064) | F13 |
| 15 | Cramér's random model read as a law | REFUTED as a law | Maier 1985 (PAPER-0205) | F12 |
| 16 | X.-J. Li 2008 proof | FAILED; the 2008 text was WITHDRAWN | author's v4; public comments by Tao and Connes | F3, F7, F8 |
| 17 | Atiyah 2018 proof | FAILED | C3-A1 (Observatory) | F1, F2, F9 |
| 18 | Oliva 2018, Queme 2020, Micheas 2026 | FAILED; withdrawn or self-flagged | authors; C3-O1, C3-Q1, C3-M1 | F2, F6, F10, F11 |

## 2. Obstructions that recur

### 2.1 The Davenport–Heilbronn countermodel

Sources: PAPER-0417 for the function, Spira 1994 (PAPER-0880) and Balanzario–Sánchez-Ortiz 2007 (PAPER-0683) for its zeros, and Bombieri–Ghosh 2011 (PAPER-0114) for its structure.

**The function.** Let $f(s)=\sum_{n\ge1}a(n)n^{-s}$, where $a$ has period 5 with $(a(1),\dots,a(5))=(1,\kappa,-\kappa,-1,0)$ and
$$\kappa=\frac{\sqrt{10-2\sqrt5}-2}{\sqrt5-1}=0.2840790438\ldots$$

**Functional equation.** Put $\Lambda(s)=(5/\pi)^{s/2}\Gamma(\tfrac{s+1}2)f(s)$. Then $\Lambda(s)=\Lambda(1-s)$ (Titchmarsh §10.25, as cited in C3; the C3 skeptic checked it numerically at three points).

**An off-line zero.** $f$ vanishes at
$$\rho_{DH}=0.80851718245663738555\ldots+85.69934848537759217193\ldots i.$$
This is a COMPUTATION (rigorous): C3-D14 certified it with Arb and Krawczyk, and the skeptic re-certified it with Arb and Rouché.

**More generally.** Nontrivial linear combinations of Dirichlet $L$-functions have infinitely many zeros in $\sigma>1$. Saias–Weingartner (PAPER-0846) prove this; Farmer 2026 (PAPER-0145, Principles 13.1–13.2) cites it.

**Consequence.** Consider an argument that uses only the functional equation, the gamma factor, analytic continuation and a Hadamard product, and never uses the Euler product in a way that $f$ fails. Such an argument proves a falsehood.

### 2.2 Ingham's theorem (1942)

Source: PAPER-0071, read at L1. THEOREM.

- **(i)** Suppose any one of $M(x)<Kx^{1/2}$, $M(x)>-Kx^{1/2}$, $L(x)<Kx^{1/2}$ or $L(x)>-Kx^{1/2}$ holds for all large $x$. Then RH holds and all zeros are simple.
- **(ii)** Suppose the positive ordinates $\gamma_n$ satisfy no $\mathbb Z$-linear relation, or only finitely many independent ones. Then $\limsup x^{-1/2}M(x)=+\infty$ and $\liminf x^{-1/2}M(x)=-\infty$, and the same holds for $L$.

The tools are a Fejér-weighted Tauberian comparison (Theorem 1) and Kronecker's theorem.

Consequence: sign and size conjectures at the $\sqrt x$ scale are stronger than RH, and they are expected to fail. Ingham-type arguments are how they were refuted.

### 2.3 Spectral realization is cheap; positivity is the content

- THEOREM: Connes 1999 (PAPER-0026, Thm 1) realizes the zeros on the critical line, and only those, as the spectrum of an operator on a Sobolev-type space.
- THEOREM: Meyer 2005 (PAPER-0074) realizes all zeros, in a setting that is not a Hilbert space (OPS frontier §1).

Unconditional spectral realizations therefore exist, so a realization alone carries no RH information.

The OPS frontier (frontiers/research_programs.md, OPS §3) finds that every operator route it surveys ends at the same kind of RH-equivalent positivity. It appears in five forms:
- Weil positivity;
- Hermite–Biehler (de Branges) membership of the function built from $\xi$ and $\xi'$;
- the boundary behaviour of a canonical system;
- Lax–Phillips decay;
- positivity of an intertwiner $W$.

### 2.4 Finite and density statements

No finite computation proves an infinite statement (methodology §8). A density statement, even with density one, does not exclude $o(N(T))$ exceptions. Both points are elementary; Sections 3–5, 9 and 14 show how much work preceded each being taken seriously.

---

# Part I. Arithmetic sign and size conjectures

## 3. Stieltjes and Mertens

**Kind.** Mertens: REFUTED. Stieltjes: open. **Fairness basis:** (b), published refutations.

**Claims.** Write $M(x)=\sum_{n\le x}\mu(n)$.
- Stieltjes (1885; *C. R. Acad. Sci. Paris* 101, 153–154; L0, not in the corpus) announced that $M(x)x^{-1/2}$ is bounded.
- Mertens (1897; PAPER-0432; L0) conjectured that $\lvert M(x)\rvert<\sqrt x$ for every $x>1$.

By Ingham's corollary (§2.2) each claim implies RH and the simplicity of all zeros.

**Failure of Mertens.**
- THEOREM (Odlyzko–te Riele 1985, PAPER-0199). We hold this at L0; the C3 skeptic checked zbMATH review 0544.10047. The theorem states
  $$\limsup_{x\to\infty}\frac{M(x)}{\sqrt x}>1.06,\qquad \liminf_{x\to\infty}\frac{M(x)}{\sqrt x}<-1.009.$$
  The proof is non-constructive. It evaluates Ingham-type kernels at points found by lattice reduction on high-precision zero data.
- Later Ω-bounds (LED-ARITH-8, checked against full texts):

  | Year | Authors | Bounds | Note |
  |---|---|---|---|
  | 2006 | Kotnik–te Riele (PAPER-0783) | $1.218$ and $-1.229$ | |
  | 2015 | Best–Trudgian | $\pm1.6383$ | |
  | 2018 | Hurst (PAPER-0585) | $1.826054$ and $-1.837625$ | Refereed and stated as a theorem. The archive files the final kernel evaluation as non-rigorous because the paper documents no enclosure. |

- Upper bounds for the first counterexample (LED-ARITH-9). No counterexample is explicitly known.

  | Year | Authors | Bound |
  |---|---|---|
  | 1987 | Pintz (PAPER-0775) | $\exp(3.21\cdot10^{64})$ |
  | 2006 | Kotnik–te Riele | $\exp(1.59\cdot10^{40})$ |
  | 2014 | Saouter–te Riele | $\exp(1.004\cdot10^{33})$ |
  | 2023 | Rozmarynowycz–Kim (unrefereed) | $\exp(1.017\cdot10^{29})$ |
  | 2025 | Kim–Nguyen (PAPER-0786) | $\exp(1.96\cdot10^{19})$, with kernel values enclosed in Arb |

- Finite data.
  - $\lvert M(x)\rvert<\sqrt x$ for every $1<x\le10^{16}$ (Hurst 2018; LED-ARITH-7).
  - Over the large-$x$ part of that range, the extreme ratio is $0.571$, at $x=7{,}766{,}842{,}813$. Small $x$ give larger ratios, for example $\lvert M(5)\rvert/\sqrt5\approx0.894$.
  - C3's exact sieve to $10^9$, reproduced by the skeptic with a different exact algorithm (COMPUTATION, rigorous), gives $\max_{10^4\le x\le10^9}\lvert M(x)\rvert/\sqrt x=0.46416$, at $x=179{,}919{,}749$.

**Stieltjes's bounded form is not refuted.** This corrects a common premise (C3-D6). By Ingham's Theorem A, boundedness would force RH, simple zeros, and infinitely many independent $\mathbb Z$-linear relations among the ordinates. The question is open, and the bound is generally expected to fail.

HEURISTIC: Kotnik–van de Lune 2004 (PAPER-0782) proposed that the extremes of $M(x)/\sqrt x$ grow like $\sqrt{\log\log\log x}$. The Kim–Nguyen bound falsifies the first-counterexample location $\exp(5.15\cdot10^{23})$ that was extrapolated from this law. It does not falsify the law itself (LED-ARITH-9, notes).

**Salvage.**
- The RH-equivalent statement $M(x)=O_\varepsilon(x^{1/2+\varepsilon})$ is untouched.
- The Ingham–Odlyzko–te Riele method lasts as a tool for Ω-results: the explicit formula plus Diophantine approximation, now done with BKZ reduction and pruned enumeration.

**Lesson.**
- F4: a fixed constant at the square-root scale is stronger than RH, and Ingham's theorem predicts that it fails if the ordinates are independent, as expected.
- F5: the data agree with Mertens up to $10^{16}$, while the first failure lies somewhere below $\exp(1.96\cdot10^{19})$.

## 4. Pólya's conjecture and Turán's $T(x)$

**Kind:** REFUTED. **Fairness basis:** (b), published refutations, plus explicit counterexamples.

**Claims.** Let $\lambda$ be Liouville's function, $L(x)=\sum_{n\le x}\lambda(n)$ and $T(x)=\sum_{n\le x}\lambda(n)/n$.
- Pólya (1919; PAPER-0488; L0+): $L(x)\le0$ for every $x\ge2$. This implies RH and simple zeros (§2.2).
- Turán: $T(x)>0$ for all large $x$, which would imply RH. The attribution and the implication are as reported in C3-D7 and in the zbMATH review of Haselgrove's paper (L0+). The usual source is Turán 1948 (PAPER-0434), which was not read here.

**Failure.**
- THEOREM (Haselgrove 1958, PAPER-0489; L0+ via zbMATH 0085.27102). Both conjectures are false. The proof is non-constructive: it feeds computed values at the zeros into Ingham's inequalities.
- Explicit counterexamples:
  - $L(906{,}180{,}359)=+1$ (Lehman 1960, PAPER-0772);
  - the smallest counterexample to Pólya is $906{,}150{,}257$ (Tanaka 1980, Zbl 0446.10004; not in the corpus);
  - the smallest $n$ with $T(n)<0$ is $72{,}185{,}376{,}951{,}205$ (Borwein–Ferguson–Mossinghoff 2008, PAPER-0616; zbMATH 1198.11090, checked by the C3 skeptic);
  - BFM also prove $L(n)>0.061867\sqrt n$ for infinitely many $n$.
- Archive replay (COMPUTATION, rigorous; C3-D7, reproduced by the skeptic with a different exact sieve):
  - $L(x)\le0$ for $2\le x<906{,}150{,}257$, and $L(906{,}150{,}257)=1$;
  - $L(x)>0$ for exactly $305{,}426$ integers $x\le10^9$, the last of which is $906{,}488{,}079$;
  - $T(x)\ge1.42\cdot10^{-6}>0$ for all $1\le x\le10^9$, with an exact fixed-point certificate.

**Why the sign pattern looks persistent.** The following is derived here from the Liouville case of Ingham's generating function, $\zeta(1+2s)/((\tfrac12+s)\zeta(\tfrac12+s))$. The pole at $s=0$ contributes the constant $1/\zeta(\tfrac12)\approx-0.685$ to $L(x)/\sqrt x$. So under RH, $L(x)/\sqrt x$ is a negative constant plus an oscillating sum over zeros. Haselgrove's theorem shows that the oscillation eventually overcomes the bias.

**Salvage.** The Ingham–Haselgrove oscillation method.

**Lesson.**
- F5: Pólya's inequality holds for every $x<9.06\cdot10^8$, and Turán's for every $x<7.2\cdot10^{13}$.
- F4: a biased almost-periodic quantity can look one-signed for a very long range. Ingham's theorem says it cannot stay one-signed unless the ordinates are dependent.

## 5. Turán's partial-sum hypothesis

**Kind:** REFUTED. **Fairness basis:** (b).

**Claim.** Turán (1948, PAPER-0434; L0), as stated by Platt–Trudgian (read here): if, for all sufficiently large $N$, the partial sum $\zeta_N(s)=\sum_{n\le N}n^{-s}$ has no zero in $\sigma>1$, then RH holds.

**Failure.**
- **Spira 1968** (*Math. Comp.* 22, 163–173; not in the corpus). $\zeta_N$ has zeros in $\sigma>1$ for $N=19$, $22$–$27$ and $29$–$50$. Spira also showed, adapting Bohr's theorems (as cited by Platt–Trudgian), that one zero of $\zeta_N$ in $\sigma>1$ forces infinitely many.
- **THEOREM (Montgomery 1983, PAPER-0660).** We hold this at L0; the statement is as quoted by Platt–Trudgian. Let $\psi_N=\sup\{\sigma:\zeta_N(\sigma+it)=0\}$. Then
  $$\psi_N=1+\Big(\frac4\pi-1-o(1)\Big)\frac{\log\log N}{\log N},$$
  and the constant $4/\pi-1$ is best possible. Hence $\zeta_N$ has zeros in $\sigma>1$ for every large $N$.
- **Monach** (thesis). Per Platt–Trudgian, Monach made this explicit for all $N>30$.
- **THEOREM (Platt–Trudgian 2016,** *LMS J. Comput. Math.* 19; arXiv:1507.01340, Thm 1.1**).** $\zeta_N$ has no zero in $\sigma>1$ exactly when $1\le N\le18$ or $N\in\{20,21,28\}$. For every other $N$ it has infinitely many.
- **Archive witness** (COMPUTATION, rigorous; C3-D5, re-certified by the skeptic using Rouché). $\zeta_{19}$ has a zero at
  $$1.0010955115364762904215\ldots+600884.2034277757127423\ldots i,$$
  and its real part is certified to exceed $1$.

**Salvage.** A truncation should respect the functional equation.

Gonek's reflected finite Euler products $\zeta_X$ (PAPER-0006) illustrate the point:
- THEOREM (THM-PAPER-0006-5): every zero of $\zeta_X$ in the strip above a fixed height lies on the critical line. The proof is that $P_X$ never vanishes and $\lvert\chi(s)\rvert=1$ only on the line.
- CONDITIONAL on RH (THM-PAPER-0006-8): the zeros of $\zeta_X$ converge to those of $\zeta$.

This RH-like property belongs to the approximant. It does not transfer to $\zeta$.

**Lesson.** F4: approximants do not inherit RH. Plain truncation breaks the functional equation, and almost-periodicity in $\sigma>1$ then produces zeros.

---

# Part II. Positivity, polynomial and heat-flow routes

## 6. de Branges positivity and Conrey–Li

**Kind:** REFUTED (the positivity conditions are false for $\zeta$). **Fairness basis:** (b), a published refutation, and (c), reproduced twice in this archive.

**Claim.** De Branges proposed an approach to GRH through positivity conditions on Hilbert spaces of entire functions. His papers are:
- *Bull. AMS* 15 (1986), PAPER-0320;
- *J. Funct. Anal.* 107 (1992), "The convergence of Euler products";
- *J. Funct. Anal.* (1994), PAPER-0302;
- the underlying theory is in his book, PAPER-0394.

Conrey–Li (IMRN 2000, PAPER-0779; arXiv:math/9812166, re-read here) state the mechanism as two theorems that are "essentially due to de Branges".

- **Theorem 1.** Let $E$ be entire with no real zeros, and suppose:
  - $\lvert E(\bar z)\rvert<\lvert E(z)\rvert$ for $\operatorname{Im}z>0$;
  - $E^{\#}(z)=\varepsilon E(z-i)$ with $\lvert\varepsilon\rvert=1$;
  - $\lvert E(x+iy)\rvert$ is strictly increasing in $y>0$.

  If $\operatorname{Re}\langle F(z),F(z+i)\rangle_{\mathcal H(E)}\ge0$ for every $F\in\mathcal H(E)$ with $F(z+i)\in\mathcal H(E)$, then all zeros of $E$ lie on $\operatorname{Im}z=-1/2$.
- **Theorem 2.** If $\operatorname{Re}\langle F,TF\rangle_{\mathcal F(W)}\ge0$ for all $F$, then $W$ extends to $\operatorname{Im}z>-1/2$ with $\operatorname{Re}\{W(z)/W(z+i)\}\ge0$.

**The intended application.** Take $E(z)=\xi(1-iz)$ with $\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$. Every hypothesis except positivity holds unconditionally, and the conclusion is RH. Positivity has two necessary consequences:
- at every zero $\rho$, $-\operatorname{Re}\{\xi'(\rho)\,\xi(1+\rho)\}\ge0$;
- for $W(z)=1/\xi(1-iz)$, $\operatorname{Re}\{\xi(s)/\xi(s+1)\}\ge0$ whenever $\operatorname{Re}s>1/2$.

**Failure.**
- THEOREM / COMPUTATION (Conrey–Li 2000).
  - At $\rho_{34}=\tfrac12+111.0295355431696745\ldots i$, $-\operatorname{Re}\{\xi'(\rho)\xi(1+\rho)\}=-5.389100507182945\ldots\times10^{-69}<0$. So condition (3.1) fails.
  - $\operatorname{Re}\{\xi(1+282i)/\xi(2+282i)\}=-0.000131957\ldots<0$. So condition (3.3) fails.
  - The analogues for $L(s,\chi_{-4})$ also fail:
    - $-2.310349004993483\ldots\times10^{-45}$ at the zero $\tfrac12+67.63692086354607\ldots i$;
    - $-0.000422340607$ at $t=8714.2$.
- THEOREM (Sarnak, in a remark in Conrey–Li). The $\mathcal F(W)$ condition fails for $\zeta$ and for every Dirichlet $L$-function. The proof uses no computation: it uses the density of the values of $\log\zeta(s)$ in $\tfrac12<\operatorname{Re}s<2$.
- Archive status. Conrey–Li's values are Mathematica floating point. C3 recomputed all four as Arb balls at 192 bits; for example the first is $[-5.389100507182945181443852872\times10^{-69}\pm3.1\times10^{-121}]$, and the $\chi_{-4}$ zero was Krawczyk-certified. The skeptic reproduced the four values independently in mpmath, and LED-OPS-13 confirms them against the full text.

**How often the necessary condition fails.** OBSERVATORY FINDING: the counts are rigorous; the mechanism is as corrected by the skeptic.
- The condition $-\operatorname{Re}\{\xi'(\rho_n)\xi(1+\rho_n)\}\ge0$ fails at 195 of the first 2000 zeros (9.75%) and at 2724 of the first 20000 (13.62%). The first failures are at $n=34,71,106,127,\dots$.
- The scan assumes the zeros lie on the line and are simple. This is justified by the verification of RH far beyond $\gamma_{20000}\approx18047$ (PAPER-0001).
- Mechanism. On the line, $-\operatorname{Re}\{\xi'(\rho)\xi(1+\rho)\}=-\Xi'(\gamma)\operatorname{Im}\xi(\tfrac32+i\gamma)$. Since $\Xi'$ alternates in sign at consecutive simple zeros, the condition requires $\operatorname{sign}\operatorname{Im}\xi(\tfrac32+i\gamma_n)$ to alternate in lockstep.
- Gram-type phase condition. The skeptic showed this is a condition on the phase $\vartheta(\gamma_n)+\arg\zeta(\tfrac32+i\gamma_n)$, where $\vartheta$ is the Riemann–Siegel theta function. Let $u_n=\vartheta(\gamma_n)/\pi-n$; in mpmath's indexing, Gram's law reads $u_n\in[-2,-1)$. Binned by $u_n$, the failures are:

  | Gram offset $u_n$ | Failures / zeros |
  |---|---|
  | $u_n<-1.5$ | 0/995 |
  | $[-1.5,-1.25)$ | 5/645 |
  | $[-1.25,-1)$ | 127/297 |
  | $u_n\ge-1$ | 63/63 |

- The condition therefore fails essentially at Gram-law irregularities, which are classical (cf. Trudgian, PAPER-0608, L0+).
- No published count of these failures was located. The statistic is possibly new; the idea is not.

**Salvage.** Only these specific positivity conditions are dead. The Hermite–Biehler and de Branges-space framework remains active, and parts of it are unconditional.
- THEOREM (Lagarias 2005, PAPER-0672, as corrected in LED-OPS-14):
  - the structure function built from $\xi(h+s)$ is a de Branges function unconditionally for $h\ge1/2$, and for every $h>0$ under RH;
  - for $\lvert h\rvert\ge1/2$, the associated functions $A_{h,\theta}$ and $B_{h,\theta}$ have only critical, simple, interlacing zeros.
- THEOREM (Lagarias 2006, PAPER-0275; known here only through the zbMATH review): the function $E_\chi=A_\chi-iB_\chi$ built from $\xi_\chi$ and $\xi_\chi'$ is a de Branges function if and only if RH holds for $L(s,\chi)$.
- Explicit canonical systems for $\xi$-type functions have been constructed (Suzuki, PAPER-0812 and later; see the OPS frontier).

Conrey–Li's own conclusion is: "It is possible that these positivity conditions are too strong."

De Branges's later unrefereed manuscripts (for example PAPER-0883, 2004) were not audited. Whether they depend on the refuted conditions is open in this archive (Annex C).

**Lesson.**
- F4: a sufficient condition for RH can be unconditionally false. (The skeptic corrected C3's wording "strictly stronger than RH", which has content only if RH is true.)
- Test the necessary consequences of a proposed positivity at the first few thousand zeros before building on it. Here the 34th zero is enough.
- Conditions that force a rigid sign pattern from one zero to the next conflict with Gram-law irregularities.

## 7. Jensen polynomials (Farmer)

**Kind:** STALLED; meta-negative. There is no error in the positive theorems. **Fairness basis:** published analysis (Farmer), plus an Observatory adjudication of one table (audit F6).

**Background.** For a real entire function $f(z)=\sum_{j\ge0}\alpha(j)z^j/j!$ of order less than 2, the Jensen polynomials are
$$J^{d,n}_f(z)=\sum_{j=0}^d\binom dj\alpha(j+n)z^j.$$
$f$ has only real zeros if and only if $J^{d,n}_f$ is real-rooted for all $d$ (equivalently, for all $d$ and $n$). See Jensen (PAPER-0487), Pólya (PAPER-0440) and Farmer §2. Applied to $\Xi$, this gives an equivalent of RH.

Recent theorems about the Jensen polynomials of $\Xi$:
- THEOREM (Griffin–Ono–Rolen–Zagier 2019, PAPER-0024): for each $d$, the polynomial is hyperbolic for all sufficiently large shifts $n$. For $d\le8$ it is hyperbolic for every $n$; this part rests on computations for small $n$.
- THEOREM (Griffin–Ono–Rolen–Thorner–Tripp–Wagner 2022, PAPER-0087): the polynomial is hyperbolic for all $n$ beyond an explicit threshold exponential in $d$. The exponent differs between the arXiv and journal versions, according to the POS frontier critique. Their Theorem 1.2, after Chasse, says that RH verified to height $T$ implies hyperbolicity for $d\le T^2$.

Farmer's abstract notes that these results "have been suggested to give evidence for the Riemann Hypothesis".

**Why the route fails.** Farmer 2022 (PAPER-0686; arXiv:2008.07206v2, re-read here) makes three points.

1. **Universality forgets the zeros.** Ki (2006) proved that, suitably rescaled, $\Xi^{(2n)}$ tends to $\cos$ (Farmer, Thm 2.1). The analogue holds in the extended Selberg class (Gunns–Hughes), which "includes many examples that do not satisfy the analogue of the Riemann Hypothesis". It also holds for random functions with Poisson zero statistics. So hyperbolicity at large shift is evidence neither for RH nor for GUE statistics.
2. **The information is dispersed.**
   - Chasse (PAPER-0871): if RH holds to height $T$, then $J^{d,0}$ is real-rooted for $d<T^2$.
   - Farmer's model $X_j$ is the cosine with the pairs of zeros nearest $\pm j$ moved to $\pm j\pm i$. It has non-real zeros, yet $J^{d,0}_{X_j}$ stays real-rooted far beyond the degree at which the plain Taylor polynomial already detects the violation (Table 4.1).
   - From the graph of $X_{10}$, Farmer observes that all zeros of $X_{10}'$ are real. So $J^{d,n}_{X_{10}}$ is real-rooted for every $n\ge1$, even though "RH" fails for $X_{10}$.
3. **A taxonomy of equivalences** (Farmer §4.1). An equivalence can be a subset or superset of a known one, a repackaging, or a translation. It is useful only if it concentrates information rather than dispersing it, or if it brings in new tools. Robin's and Lagarias's criteria are his examples of dispersal.

Farmer's conclusion (abstract): Jensen polynomials, "as well as a large class of related polynomials, are not useful for attacking the Riemann Hypothesis". He says explicitly that this is not a proof that the equivalence cannot be used.

**The adjudicated issue in Table 4.1** (audit F6). Classification: `verified_error`, minor; public wording allowed.

Two of the four classical thresholds are wrong for the functions as defined. All values were certified as follows:
- real-rootedness, by counting sign changes in Arb;
- non-real roots, by a root-distance bound;
- a hereditary lemma, $J^{d-1,0}=J^{d,0}-(z/d)\,J^{d,0\,\prime}$, which preserves real-rootedness. It makes a pair "$D$ real-rooted, $D+1$ not" decisive for all $d$.

| $j$ | printed maximal $d$ | certified maximal $d$ | note |
|---|---|---|---|
| 10 | 118 | **119** | $J^{119,0}_{X_{10}}$ is certified real-rooted (59 of 59 sign changes); the first non-real case is $d=120$. |
| 20 | 749, with "4 first zeros real" | **477**, with 5 first zeros real | The printed values are exact for moving $9\pi/2$ and $11\pi/2$, not the zeros $11\pi/2$ and $13\pi/2$ that the definition selects. |
| 40 | 1897 | 1897 | confirmed |
| 60 | 4242 | 4242 | confirmed |

The recommended public wording (F6) is:

> "Table 4.1 of Farmer (2020/22) contains two minor numerical slips: the $j=10$ threshold is 119 rather than 118, and the $j=20$ entries correspond to moving the zeros $9\pi/2,11\pi/2$ rather than the two closest to 20 (for which the threshold is 477 and 5 real zeros come first). The $j=40,60$ entries are exact. The paper's conclusions are unaffected."

- With the corrected values, $d_{\max}/j^2\approx1.19,\ 1.19,\ 1.19,\ 1.18$. The thresholds are still 6 to 24 times the Taylor thresholds 20, 60, 118 and 175.
- The Taylor row was not audited, because the paper does not define "detects".
- The cause of either slip cannot be determined, and no cause is suggested here.

Propagation note: the archive's own POS frontier text and LED-POS-18 quote "$d=118$". Both should read 119.

**Salvage.**
- The positive theorems stand, as theorems about Jensen polynomials.
- Farmer calls Hermite universality "interesting and surprising". He suggests it may be a new universal law refining Berry's cosine attractor.
- Finite-height Jensen statements are corollaries of zero verification.
- Ono 2026 (PAPER-0429, unrefereed) proves an asymptotic Jensen–Pólya criterion for GRH. The POS frontier records that the GORTTW paper and Ono both remark that such partial results give no zero-free region.

**Lesson.**
- Before calling an equivalence a route to RH, measure on a model with a known violation how many coefficients the criterion needs to see it, and compare with a naive detector. This is the dispersal test.
- F1: regimes in which the object converges to a universal limit (large shift, cosine or Hermite limits) are shared with functions that violate RH.

## 8. Heat flow with room to spare (de Bruijn–Newman)

**Kind:** CLOSED. **Fairness basis:** a published theorem.

**Setting.** Define
$$H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad \Phi(u)=\sum_{n\ge1}\big(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\big)\exp(-\pi n^2e^{4u}).$$
$H_0$ is a rescaling of Riemann's $\Xi$. The de Bruijn–Newman constant $\Lambda$ is characterized by: all zeros of $H_t$ are real if and only if $t\ge\Lambda$. RH is equivalent to $\Lambda\le0$.
- De Bruijn (PAPER-0409) showed $\Lambda\le1/2$.
- Newman (PAPER-0223) introduced $\Lambda$ and conjectured $\Lambda\ge0$: if RH is true, it is only barely true.

The hope this conjecture opposed was a proof of RH with room to spare, obtained by showing that $H_t$ is real-rooted for some $t<0$.

**Closure.** THEOREM (Rodgers–Tao 2020, PAPER-0036, Thm 1): $\Lambda\ge0$. Hence RH is equivalent to $\Lambda=0$, and there is no slack at negative time.

The mechanism (THM-PAPER-0036-7) runs as follows:
- assume $\Lambda<0$, which implies RH;
- the zeros of $H_t$ then repel each other under the heat-flow dynamics;
- this forces almost all gaps at time $0$, at height about $T\log T$, to be asymptotically equal;
- that contradicts the small-gap theorem of Conrey–Ghosh–Goldston–Gonek–Heath-Brown.

Related results:
- Dobner 2021 (PAPER-0333; title level) proves the analogue of Newman's conjecture for the extended Selberg class.
- Upper bounds: $\Lambda\le0.22$ (Polymath 2019, PAPER-0083) and $\Lambda\le0.2$ (Platt–Trudgian 2021, PAPER-0001, Cor. 2).
- An unrefereed 2026 claim, $\Lambda<0.156821$ (Planat–Raymond, arXiv:2611.06245), passed an L2 audit with no issue found in the inspected portion. Its full certificate was not replayed (audit F8).

**Salvage.**
- The upper-bound technology (the barrier criterion, Polymath Thm 1.2) is still valuable. It turns zero verification into upper bounds for $\Lambda$; Polymath's heuristic is that verification to height $T$ should give $\Lambda=O(1/\log T)$.
- Farmer 2026 (PAPER-0145, Principle 12.1 and §12.1) notes that "barely true" phenomena, such as Lehmer pairs and $\Lambda\ge0$, are mirrored by characteristic polynomials of random unitary matrices, for which the RH analogue holds. So they are not evidence against RH.

**Lesson.** A deformation argument that needs RH to hold with slack fails if the object sits exactly at the boundary. First ask whether the target is a boundary case of a one-parameter family.

## 9. Numerical use of the Nyman–Beurling (and Li) criteria

**Kind:** STALLED as numerics. The criteria themselves are correct theorems. **Fairness basis:** published lower bounds.

**The criterion.** THEOREM (Nyman 1950, PAPER-0181; Beurling 1955, PAPER-0475; natural-number form by Báez-Duarte 2003, PAPER-0004, read at L1). Work in $H=L^2(0,\infty)$ with $\rho_a(x)=\{1/(ax)\}$ and $\chi=\mathbf 1_{(0,1]}$. Then RH holds if and only if $\chi\in\overline{\operatorname{span}}\{\rho_a:a\in\mathbb N\}$.

Write $d_N=\operatorname{dist}(\chi,\operatorname{span}\{\rho_a:a\le N\})$, so that RH is equivalent to $d_N\to0$. The hope was to compute $d_N$ for growing $N$ and watch it tend to zero, or to find good explicit approximants.

**Why the numerical route stalls.**
- **The natural approximants diverge.** $F_n=\sum_{a\le n}\mu(a)\rho_a$ diverges in $H$. Báez-Duarte needs the damped sums $\sum_{a\le n}\mu(a)a^{-\varepsilon}\rho_a$ followed by the limit $\varepsilon\to0$ (PAPER-0004 record).
- **A logarithmic lower bound.** THEOREM (Báez-Duarte–Balazard–Landreau–Saias 2000, PAPER-0216; Burnol 2002, PAPER-0606; LED-POS-16 and LED-ARITH-20, confirmed against Burnol's text). Unconditionally,
  $$\liminf_{N\to\infty}d_N^2\log N\ \ge\ \sum_{\operatorname{Re}\rho=1/2}\frac{m_\rho^2}{\lvert\rho\rvert^2},$$
  where $m_\rho$ is the multiplicity. BBLS had proved the bound with $\sum1/\lvert\rho\rvert^2$ over distinct critical zeros.
  - Under RH with simple zeros, the right side equals $2+\gamma-\log4\pi=0.0461914\ldots$.
  - Unconditionally, the right side is at least this value minus a negligible tail, by the zero verification (LED-ARITH-20, note).
- **The bound is sharp.** CONDITIONAL (Bettin–Conrey–Farmer 2013, PAPER-0291; LED-POS-16). Assume RH and $\sum_{\lvert\gamma\rvert\le T}\lvert\zeta'(\rho)\rvert^{-2}\ll T^{3/2-\delta}$. Then the choice $V_N(s)=\sum_{n\le N}(1-\log n/\log N)\mu(n)n^{-s}$ gives $d_N^2\sim(2+\gamma-\log4\pi)/\log N$, so Burnol's bound is sharp.
- **An RH upper bound.** Balazard–de Roton (*IJNT* 6 (2010); zbMATH, via LED-ARITH-20): under RH, $d_N^2\ll(\log\log N)^{5/2+\delta}/\sqrt{\log N}$.

Consequence (derived here):
- Asymptotically, $d_N^2\gtrsim0.0462/\log N$ whether or not RH is true. That is about $1.67\cdot10^{-3}$ at $N=10^{12}$ and $1.0\cdot10^{-3}$ at $N=10^{20}$.
- A table of $d_N$ therefore shows only the logarithmic decay that the critical zeros force.
- The archive holds no quantitative lower bound for $\lim d_N$ when RH fails. Without one, finite-$N$ values cannot separate the two alternatives.

**The same structure for Li coefficients.**
- THEOREM (Li 1997, PAPER-0193): RH holds if and only if $\lambda_n\ge0$ for all $n$.
- Voros 2006 (PAPER-0005, L1):
  - RH holds if and only if $\lambda_n\sim\tfrac n2(\log n-1+\gamma-\log2\pi)$;
  - if RH fails, $\lambda_n\sim\sum_k\big(\tfrac{\tau_k+i/2}{\tau_k-i/2}\big)^n+\text{c.c.}$, an oscillation that grows exponentially.
- HEURISTIC (Voros's uncertainty argument; the POS frontier labels it heuristic). An off-line zero $\tfrac12+t+iT$ affects $\lambda_n$ only for $n\gtrsim T^2/\lvert t\rvert$.
- RH is verified to height $T_0=3{,}000{,}175{,}332{,}800$ (PAPER-0001). Since $\lvert t\rvert<1/2$, any off-line zero would show only for $n\gtrsim T_0^2/\lvert t\rvert\ge1.8\cdot10^{25}$ (derived here). Direct computation of $\lambda_n$ is therefore empty as a test of RH.

**Robin and Lagarias.** Farmer (PAPER-0686, §4.1) uses these criteria as his example of dispersal. A violation of $\pi(x)=\operatorname{Li}(x)+O(x^{1/2+\varepsilon})$ at $x$ produces a Robin violation only at an integer "enormously larger than $x$". The certified Robin range $5040<n\le10^{10^{13.11485}}$ (Morrill–Platt 2021, PAPER-0590; LED-ARITH-1) is in substance a corollary of zero verification (ARITH frontier §3).

**Salvage.** The criteria are correct, and they are useful bridges between problems.
- Feldmann's critique of Yakaboylu's follow-up reduces a completeness condition there to the Nyman–Beurling criterion (LED-OPS-19).
- Bagchi gives a Hilbert-space reformulation (PAPER-0561).
- The constant $2+\gamma-\log4\pi$ from Burnol and Bettin–Conrey–Farmer is a sharp benchmark for testing code.

**Lesson.** F5: before computing, estimate the detection threshold, meaning the $N$ or $n$ at which a hypothetical violation could first become visible. Two kinds of criterion cannot be probed numerically beyond what zero verification already gives:
- a quantity that tends to zero at a logarithmic rate;
- a sequence whose violations can appear only at index $\gtrsim T^2$.

---

# Part III. Spectral (Hilbert–Pólya) realizations

## 10. The Hilbert–Pólya idea and Berry–Keating $xp$

**Kind:** a HEURISTIC programme; no realization with RH content exists. **Fairness basis:** proved spectral facts. No error is attributed to Berry–Keating, who proposed a heuristic.

**The idea.** Find a self-adjoint operator whose eigenvalues are the ordinates $\gamma_n$; self-adjointness would then give RH. The attribution to Hilbert and Pólya is folklore, and this archive holds no primary source for it.

Statistical support exists: Montgomery's pair correlation (PAPER-0091), Odlyzko's spacing computations (PAPER-0023), and Katz–Sarnak (PAPER-0017). All of it concerns distributions; none of it shows that such an operator exists.

**The Berry–Keating claim** (PAPER-0196, PAPER-0500; L0 here, content via LED-OPS-17). The classical Hamiltonian $H=xp$ with phase-space cut-offs gives, semiclassically, the smooth zero count
$$\bar N(E)=\frac E{2\pi}\Big(\log\frac E{2\pi}-1\Big)+\frac78.$$
This is HEURISTIC. Connes 1999 obtains the smooth term with the opposite sign, which he reads as absorption (PAPER-0026, eq. (43), per LED-OPS-17).

**Where it stops.**
- THEOREM (Endres–Steiner 2010; abstract level via LED-OPS-17; not in the corpus): $H_{BK}=-i\hbar(x\,d/dx+1/2)$ on $L^2(\mathbb R_{>0})$ has purely continuous spectrum. So this quantization is not a Hilbert–Pólya operator.
- The same fact was derived independently in audit F1 (§2, F1): under $x=e^u$, the dilation generator is unitarily equivalent to $-i\,d/du$ on $L^2(\mathbb R)$.
- The regularizations reproduce at most the average zeros (LED-OPS-17): Sierra (PAPER-0664, PAPER-0810), Sierra–Townsend (PAPER-0636), and Sierra–Rodríguez-Laguna 2011. No model reproduces the fluctuating term $S(T)$ without inserting $\zeta$ or the primes.
- Sierra 2019 (PAPER-0562): a zero is a bound state only when a boundary parameter is fine-tuned, and this is shown only as a necessary condition. His RH argument "assumes the convergence of some mathematical series" (LED-OPS-17, checked against arXiv:1601.01797).

**Salvage.** The following are genuine results, but they are neutral on RH (all via LED-OPS-17):
- semiclassical matching of $\bar N(E)$;
- realizations on quantum graphs with trace formulae (Endres–Steiner);
- Srednicki's spectral proof of an archimedean "local RH".

**Lesson.** F7: matching the smooth counting function is a weak test, because the gamma factor fixes it, and Davenport–Heilbronn-type functions share it. A real candidate needs five things:
- a Hilbert space;
- a domain;
- self-adjointness;
- discrete spectrum;
- the fluctuating term $S(T)$.

## 11. Bender–Brody–Müller (2017)

**Kind:** a CONDITIONAL programme with an unfilled gap; no proof was claimed. **Fairness basis:** a public critique whose facts the authors' reply concedes.

**Claim** (PRL 118 (2017) 130201; PAPER-0502; arXiv:1608.03679). The operator
$$\hat H=(1-e^{-i\hat p})^{-1}(\hat x\hat p+\hat p\hat x)(1-e^{-i\hat p})$$
has formal eigenfunctions $\psi_z(x)=-\zeta(z,x+1)$ (Hurwitz zeta), and the boundary condition $\psi_z(0)=0$ holds if and only if $\zeta(z)=0$. The authors write: "If the analysis presented here can be made rigorous to show that $\hat H$ is manifestly self-adjoint, then this implies that the Riemann hypothesis holds true." Their reply quotes the PRL: "We are not able to prove that the eigenvalues of $\hat H$ are real."

**The gap.**
- **Bellissard's comment** (2017, PAPER-0813; arXiv:1704.02644, read here). These are standard operator-theoretic facts:
  1. On $L^2(0,\infty)$ with the Dirichlet condition, $\hat p$ is symmetric with deficiency indices $(n_+,n_-)=(1,0)$. So it has no self-adjoint extension, and "the argument proposed in the paper cannot be used".
  2. $\psi_z$ is not an eigenvector for $\operatorname{Re}z=1/2$: Bellissard finds that its norm integral converges only for $\operatorname{Re}z>3/2$.
  3. In a weighted space $L^2(x^\alpha dx)$ the dilation generator becomes $A_\alpha=ix\,d/dx+i(\alpha+1)/2$, and the eigenvalue problem no longer selects $\operatorname{Re}z=1/2$.
- **The BBM reply** (arXiv:1705.06767) says these points were "already discussed", and that the relevant inner product is biorthogonal or pseudo-Hermitian. No such inner product is constructed.
- **Archive check** (C3-D4). COMPUTATION in Arb, reproduced by the skeptic with mpmath and Euler–Maclaurin sums. The ratio $\lvert\zeta(\rho_1,x+1)\rvert\,\lvert\rho_1-1\rvert/\sqrt x$ takes the values $1.00332,\ 1.000025,\ 1.00000025,\ 1.0000000025$ and $1.000000000025$ at $x=10^2,10^4,10^6,10^8,10^{10}$, matching the asymptotics of DLMF 25.11.43. Hence $\int_0^X\lvert\psi_{\rho_1}\rvert^2\sim X^2/(2\lvert\rho_1-1\rvert^2)$, and $\psi_{\rho_1}\notin L^2(0,\infty)$.
- **Unrefereed follow-up** (K. Liu, arXiv:2607.19067; read at abstract level only). Completing $C_c^\infty$ in BBM's metric $\eta=\sin^2(p/2)$ gives a space unitarily equivalent to $L^2(\mathbb R_+)$, on which the dilation spectrum is purely absolutely continuous. The $\psi_z$ with $\operatorname{Re}z=1/2$ do not belong to it.

**The exact remaining gap.** To our knowledge (literature searched in C3 and LED-OPS-18), no Hilbert space has been exhibited in which both of the following hold:
- $\hat H$, or a closed extension of it, is self-adjoint;
- the $\psi_z$ with $\zeta(z)=0$ are eigenvectors.

The formal eigen-equation holds for every complex $z$. All of the RH content sits in the missing inner product.

**Salvage.** Heuristic value only: the PT-symmetric viewpoint, and the link to Berry–Keating. Müller (arXiv:1704.04705, abstract only) announces a rigorous construction of a related operator.

**Lesson.** F7: a boundary condition that "selects the zeros" carries no weight until five things are written down: the space, the domain, the adjoint domain, the deficiency indices, and a proof that the eigenvectors lie in the space.

## 12. Yakaboylu (2024)

**Kind:** the published Stage-II claim is a verified error. RH was not claimed. **Fairness basis:** (c), an Observatory L2 audit plus an independent L3 adjudication (audit F1), with explicit witnesses. The author's own later revision is reported separately.

**Claim** (E. Yakaboylu, *J. Phys. A* 57 (2024) 235204; PAPER-0095; arXiv:2309.00405 v1–v6).
- **Stage I.** Let $\hat H=\hat S\hat H_{BK}\hat S^{-1}$, with $\hat H_{BK}=(\hat x\hat p+\hat p\hat x)/2$ and $\hat S=t^{\hat N}e^{\alpha\hat x}/(1+e^{\hat x})$. The eigenfunctions are $\Psi_s=\hat S\phi_s$ with $\phi_s=x^{s-1}/\sqrt{2\pi}$, and $\Psi_s(0)\propto(1-2^{1-s})\Gamma(s)\zeta(s)$.
- **Stage II.** The paper asserts that a similarity transformation exists, with the Mellin-space weight (18)
  $$\omega'(z,y)=\frac{1/z}{1+e^{y/z}}+\frac{1/y}{1+e^{z/y}},$$
  under which the operator is "self-adjoint on the domain specified by the condition (17), and hence admits only real eigenvalues". It also states that condition (17) "corresponds to" $\Psi_s(0)=0$.
- **The hedge.** The Discussion says: "If the formal argument presented in this manuscript can be rigorously established, our approach holds the potential to imply the validity of the RH."

**Failure** (audit F1: `verified_error`, scoped to Stage II). Write $F=\Gamma\eta$, where $\eta$ is the alternating zeta function.
1. **The weight is indefinite.** The quadratic form of (18) has Fourier symbol $2\operatorname{Re}F(\tfrac12+i\tau)$, which is negative in places; for example it equals $-0.004682$ at $\tau=4$. The test vector $u'(z)=z^{-1/2+4.8i}\exp(-(\ln z)^2/18)$ gives $\langle U|U\rangle=-0.0231346$; a 2-D quadrature and the spectral formula agree to 8 digits, and the corresponding $\ell^2$ state is legitimate. So (18) is not of the form $S'^\dagger S'$ for any bounded $S'$. Symmetry with respect to an indefinite (Krein) form does not imply a real spectrum.
2. **Condition (17) is not the Dirichlet condition.** For $u'=z^{s-1}$, condition (17) is equivalent to $G(s):=F(s)+F(1-s)=0$. A spurious solution on the line is $s^*=\tfrac12+3.70362373148i$, where $\zeta(s^*)\ne0$.
3. **A certified non-real eigenvalue inside the zeta setting** (the adjudicator's witness). $G$ has a zero at
   $$s_0=0.88106174137852\ldots+63.45282508476655\ldots i,$$
   certified with Arb at 256 bits and Rouché's theorem on $\lvert s-s_0\rvert=10^{-10}$. There $\zeta(s_0)=2.5645-0.7873i\ne0$. The function $z^{s_0-1}$ satisfies (17), with the non-real eigenvalue $63.45282508-0.38106174i$.
4. **Davenport–Heilbronn control.** The Stage-II steps use only properties (14) and (15). These hold for any real symmetric kernel that is homogeneous of degree $-1$. Take the positive analytic function $W_{DH}$ whose Mellin transform is $\Gamma(s)f_{DH}(s)$. The same argument would then place $\rho_{DH}=0.808517\ldots+85.699348\ldots i$ on the critical line, which is false (F1).

Secondary findings:
- Appendix B's normalization assumes $\operatorname{Re}\rho=1/2$, so it is circular.
- The prefactor zeros $1+2\pi ik/\log2$ give $L^2$ Dirichlet eigenfunctions with non-real eigenvalues. This is classified *missing hypothesis*, because the paper excludes these points by convention.
- The series in Eq. (9) diverges factorially (*suspected gap*).

All values except the certified $s_0$ are non-rigorous high precision.

**The author's later revision** (reported separately from the Observatory findings). The follow-up is arXiv:2408.15135.
- v11 (2025) claimed that all simple zeros lie on the line.
- v17 (18 Aug 2026) retreats to a symmetric operator $W$ "whose positivity is equivalent to the Riemann Hypothesis" (LED-OPS-19).

An unrefereed critique of v14 by N. Feldmann (Zenodo 10.5281/zenodo.19353727) argues that the transformed Dirichlet domain is not dense, and reduces the needed completeness to the Nyman–Beurling criterion.

**Public wording (F1).**

> "The paper's Stage-II argument (Sec. II, Eqs. 13–18) does not establish a self-adjoint similarity transform with real spectrum. The proposed weight (18) is indefinite, and the boundary condition (17) admits eigenfunctions with non-real eigenvalues (for example $s\approx0.8811+63.4528i$, where $\zeta\ne0$). The identical argument would also place an off-line Davenport–Heilbronn zero on the critical line. The paper does not claim a proof of RH, and the author's later work (arXiv:2408.15135 v17) reformulates the remaining step as a positivity condition equivalent to RH."

Do not say that the paper claimed to prove RH.

**Salvage.**
- The Stage-I identity, a boundary value proportional to $(1-2^{1-s})\Gamma(s)\zeta(s)$, is a correct formal computation.
- The positivity statement of v17 is an honest RH-equivalent reformulation.

**Lesson.**
- F7: pseudo-Hermitian quantum mechanics gives a real spectrum only for a *positive* metric. A metric that is merely symmetric is a Krein form.
- F3: if the positivity needed is equivalent to RH, the scheme is a restatement of RH.
- F1: always run the Davenport–Heilbronn control.

## 13. Correct theorems in stalled programmes: Connes's trace formula and Lax–Phillips

**Kind:** STALLED. There is no error. **Fairness basis:** audit F5 (`correct_but_misinterpreted`); for Lax–Phillips, the introduction of Conrey–Li.

**Connes 1999** (*Selecta Math.* 5, 29–106; PAPER-0026).

What is proved:
- a spectral realization of the *critical* zeros on a $\delta$-Sobolev space (Thm 1, Cor 2);
- local and $S$-local trace formulae (Thms 3 and 4);
- a rewriting of Weil's explicit formula (Thm 6);
- Theorem 5: for global fields of *positive characteristic*, the global trace formula (16) is equivalent to RH for all Grössencharakter $L$-functions. In that setting RH is Weil's theorem, so Theorem 5 is unconditional there.

What is not proved:
- For number fields the global statement is only sketched, via prolate functions on p. 47.
- Audit F5 found no issue in Theorem 5 as stated. It also gave an independent witness that the theorem's literal form cannot carry over: for any field with an archimedean place, the subspace $B_\Lambda$ is $\{0\}$ (by Paley–Wiener). Connes himself notes the underlying obstruction on p. 46.

Misreadings:
- The abstract and introduction state the equivalence without the positive-characteristic qualifier.
- Some later citations turn it into a proved statement about classical RH. One, Tamburini (arXiv:2503.09644, math.GM), asserts that "Connes' trace formula therefore applies and forces every … zero … to lie on the critical line". Connes 1999 contains no such theorem.
- These are misreadings by others, not errors by Connes.

Current state of the programme (OPS frontier; IMPORTED). In the Connes–Consani–Moscovici line, three concrete gaps remain:
- simplicity and evenness of the lowest eigenvalue of the semilocal Weil forms, for windows that contain primes;
- convergence of the ground states in norms that control the Mellin transform on the closed strip;
- removal of the assumed positivity $QW_\lambda\ge0$ from the convergence estimates.

Andrews–Connes–La Gatta (arXiv:2611.13129; PAPER-0544; unrefereed) say their conditional estimates "do not give a proof" (Remark 7.4, per the OPS frontier).

**Lax–Phillips** (PAPER-0387; L0). Their scattering theory for automorphic functions yields an RH-equivalent decay criterion. Conrey–Li's introduction, re-read here, states: "In Appendix 2 to Section 7, Lax and Phillips explained the difficulty of approaching the Riemann hypothesis by using the scattering theory." De Branges related his own approach to theirs.

**Lesson.**
- Correct theorems can sit inside stalled programmes. The stall is the positivity (§2.3).
- Before citing a programme as having reduced RH to something computable, read its scope qualifiers: which characteristic, whether only the critical zeros are realized, and whether a statement is a theorem or a sketch.

---

# Part IV. Density and probabilistic methods

## 14. Mollifier methods and their ceilings

**Kind:** CLOSED as a route to RH, by design; active as a density method. There is no error. **Fairness basis:** the structure of the published theorems.

**The chain of results.** Here $\kappa$ is the lower density of zeros on the critical line, counted with multiplicity, and $\kappa^*$ counts simple zeros only.
- **Hardy–Littlewood 1921** (PAPER-0115, Thm A): $N_0(T)>KT$. Infinitely many critical zeros, but proportion zero.
- **Selberg 1942** (PAPER-0413): a positive proportion.
  - Selberg's sign-change method alone gives $\kappa_0>0.0678190$ (Pearce-Crump, arXiv:2609.15329 v2; unrefereed). Version 1 said 7%; the author corrected it.
  - The same paper corrects Zhuravlev's 1974 constant $2/21$ to $2/(3\pi^2e)\approx0.02485$ (LED-CRIT-17).
- **Levinson 1974** (PAPER-0133): more than $1/3$; the proof gives $0.34$.
- **Conrey 1989** (PAPER-0191, PAPER-0322): with a mollifier of length $T^\theta$, $\theta=4/7-\varepsilon$, he obtains $\kappa>0.4088$.
- **Bui–Conrey–Young 2011** (PAPER-0034): $\kappa\ge0.4105$ and $\kappa^*\ge0.4058$.
- **Feng 2012** (PAPER-0046): $\kappa\ge0.4128$. Its history (LED-CRIT-5):
  - Feng's arXiv v1 claimed $0.4173$, with every mollifier piece of length $4/7$.
  - After Conrey queried this, Feng reduced the pieces to length $1/2$ (an author correction).
  - PRZZ report that "a gap was found in Feng's argument which reduces the size to 3/7".
  - Pratt–Robles 2018 (PAPER-0076) proved length $6/11$, "validating Feng's claim", and obtained $\kappa\ge0.41491637$.
- **Pratt–Robles–Zaharescu–Zeindler 2020** (PAPER-0045): $\kappa\ge0.417293962>5/12$ and $\kappa^*\ge0.407511457$. Their §5.1 proves what PRZZ call Feng's "unproved claim" about the terms with non-square-free indices.

**The mechanism.** The Levinson–Conrey method, as stated by BCY (THM-PAPER-0034-2), uses $V(s)=Q(-\tfrac1L\tfrac{d}{ds})\zeta(s)$ with $L=\log T$, the line $\sigma_0=\tfrac12-\tfrac RL$, and a mollifier $\psi$:
$$\kappa\ \ge\ 1-\frac1R\log\Big(\frac1T\int_1^T\lvert V\psi(\sigma_0+it)\rvert^2\,dt\Big)+o(1).$$
- This follows from Littlewood's lemma and the concavity of the logarithm.
- The method counts zeros of an auxiliary combination to the right of $\sigma_0$, then converts that count into critical zeros of $\zeta$.
- Hardy–Littlewood and Selberg count sign changes of $Z(t)$ instead (the skeptic's correction to C3-D9).
- No version of either method ever excludes an individual off-line zero.

**The ceilings.**
1. **Length.** The analytic input is a twisted second moment $\int\lvert\zeta A\rvert^2$, where $A$ has length $T^\theta$. Bettin–Chandee–Radziwiłł 2017 (PAPER-0244, §1, re-read here) record:
   - for Conrey's coefficients, $\theta<4/7$ is available;
   - for arbitrary coefficients $a_n\ll n^\varepsilon$, the asymptotic is proved for $\theta<17/33$ and fails in general for $\theta>1$;
   - if $\theta=1-\varepsilon$ were allowed, the Lindelöf Hypothesis would follow.
2. **Output at $\theta=1$.**
   - CONDITIONAL (Feng, Cor. 1): if his mean-value lemma held for all $\theta=\theta_1<1$, then $\kappa\ge0.6107$.
   - In families where $\theta=1$ is available on average, Conrey–Iwaniec–Soundararajan show that at least $14/25$ of the zeros of Dirichlet $L$-functions are simple and critical (LED-CRIT-8).
3. **Output at $\theta=\infty$.** CONDITIONAL (Farmer 1993, PAPER-0550, L0+; content via PAPER-0064 and Radziwiłł). Farmer's "$\theta=\infty$ conjecture" says the mollified mean square keeps its main term for every fixed $\theta$. If so, Levinson's method gives $\kappa=1$, that is $N_0(T)\ge(1-o(1))N(T)$. Density one still allows $o(N(T))$ off-line zeros, so *the counting step* can never yield RH.
4. **The input itself is as strong as RH.** This corrects C3-D9, after checking against the L1 record of PAPER-0064.

   THEOREM (Bettin–Gonek 2017, *Mathematika* 63, 29–33). Let
   $$M_N(s)=\sum_{n\le N}\mu(n)n^{-s}\Big(1-\frac{\log n}{\log N}\Big),\qquad I_N(T_1,T_2)=\int_{T_1}^{T_2}\lvert M_N\zeta(\tfrac12+it)\rvert^2\,dt.$$
   If $I_N(0,T)\ll_\varepsilon T^{1+\varepsilon}$ uniformly for $2\le N\le T^\theta$, then $\zeta$ has no zeros in $\operatorname{Re}s>\tfrac12+\tfrac1{2\theta}$. If this holds for arbitrarily large $\theta$, RH follows.
   - The proof isolates a hypothetical off-line zero by a Pintz-type Mellin argument. It does not count zeros.
   - So the $\theta=\infty$ conjecture is at least as hard as RH.
   - The conclusion has content only for $\theta>1$. For $\theta\le1$, the half-plane $\operatorname{Re}s>\tfrac12+\tfrac1{2\theta}$ lies in $\operatorname{Re}s\ge1$, where $\zeta$ has no zeros anyway (derived here).
5. **Mollification can never be perfect.** THEOREM (unrefereed; Radziwiłł, arXiv:1207.6583v3, Thm 1). Take any $\theta>0$ and any $M_\theta(s)=\sum_{n\le T^\theta}a(n)n^{-s}$ with $a(n)\ll n^\varepsilon$ and $a(1)=1$. Then
   $$I(M_\theta)=\frac1T\int_T^{2T}\lvert1-\zeta M_\theta(\tfrac12+it)\rvert^2\,dt\ \ge\ \frac c\theta.$$
   This limits Selberg-type mollification. It does not directly bound the Levinson proportion (LED-CRIT-9, correction).
6. **2026: a different mechanism with its own ceiling.** AI-DISCOVERED, UNREFEREED.
   - Alpöge–Furman (arXiv:2608.13637, PAPER-0486) carry the comment "Proof discovered autonomously by Claude (Anthropic); verified and communicated by the listed authors".
     - They prove that at least $2/3$ of the zeros are simple and critical, or $0.6725$ with the Montgomery–Taylor window.
     - The method is a rank–trace inequality on a finite compression of Weil's Hermitian form.
   - Lamzouri (arXiv:2609.02882, PAPER-0533; human, unrefereed) gives an independent proof.
   - The archive's exploration-level audit found no error that affects a stated result (audits/claims_2026/CRIT23/DOSSIER.md).
   - The authors state, and the archive has not audited, that every "bandwidth-one" certificate is capped at $0.6818287$ (AF §7.2). Such certificates use two trace moments with Fourier support in $[-1,1]$.
   - B. Wang (arXiv:2609.24167, unrefereed) improves the bound by $\delta_0=6.66624\cdot10^{-8}$ and comments that a new method is needed.

**Salvage.** All of it. These are theorems about the density of critical zeros, with applications to simplicity, moments and families. They were never routes to RH except under the misreading "100% means all".

**Lesson.**
- F13: a density, even density one, is not RH.
- More usefully, when a method hits a ceiling, ask whether its analytic *input* would be enough through a different argument, as Bettin–Gonek did. Effort then goes into the input rather than the counting step.

## 15. Cramér's random model

**Kind:** REFUTED as a law about the primes; as a model it is a heuristic. **Fairness basis:** a published theorem (Maier).

**Claim** (Cramér 1936, PAPER-0147, L1).
- **The model.** Each integer $n$ belongs to the random set $\mathcal C$ independently, with probability $1/\log n$.
- **Theorem about the model.** Almost surely,
  $$\limsup_n\frac{P_{n+1}-P_n}{(\log P_n)^2}=1.$$
- **Cramér's suggestion.** "Obviously we may take this as a suggestion that, for the particular sequence of ordinary prime numbers $p_n$, some similar relation may hold" (quoted in Banks–Ford–Tao §1.1).
- **The model is compatible with RH.** It satisfies $\pi_{\mathcal C}(x)=\int_2^x dt/\log t+O(x^{1/2+\varepsilon})$ almost surely, and "the analogous statement for primes" is equivalent to RH (BFT §1.1).

**Failure.**
- **Maier's theorem.** THEOREM (Maier 1985, PAPER-0205; L0 here; statement as in BFT §2.5, read here). For every fixed $A>1$,
  $$\liminf_{x\to\infty}\frac{\pi(x+(\log x)^A)-\pi(x)}{(\log x)^{A-1}}<1<\limsup_{x\to\infty}\frac{\pi(x+(\log x)^A)-\pi(x)}{(\log x)^{A-1}}.$$
- **What the model predicts.** The ratio tends to 1 almost surely whenever $y/\log^2x\to\infty$, which here means $A>2$. This is BFT (2.1); C3 gave a proof sketch by Chernoff bounds and Borel–Cantelli, which the skeptic re-derived.
- **The cause** (BFT §1.1).
  - $\mathcal C$ is equidistributed modulo every prime $p$, while the primes avoid the class $0\bmod p$.
  - For example, the model predicts about $x/\log^3x$ triples $n,n+1,n+2$ in $\mathcal C$, although no triple of consecutive integers can all be prime.
- **Repairs.**
  - Granville's sieved model (1995, PAPER-0881) predicts maximal gaps at least $2e^{-\gamma}\log^2x=1.1229\ldots\log^2x$ almost surely (BFT (1.3)). This exceeds the Cramér-model value 1.
  - Pintz 2007 (PAPER-0884) discusses the model's flaws.
  - Banks–Ford–Tao 2023 (*Invent. Math.* 233; arXiv:1908.08613) propose new models.
  - The "Cramér conjecture" $G(x)=O(\log^2x)$ remains open.

**Salvage.** Probabilistic models corrected for local structure modulo small primes remain the standard heuristic source for statistics of primes and zeros.

**Lesson.**
- F12: a model can be right on average, and even compatible with RH, yet wrong at the scale that matters.
- Predictions from random models or random matrix theory are hypotheses about statistics. They are not evidence about individual zeros. Test them against Ω-theorems.

---

# Part V. Proof claims that failed

## 16. X.-J. Li (2008)

**Kind:** FAILED; the 2008 text was WITHDRAWN. **Fairness basis:** (a), the author's withdrawal "due to mistake on page 29"; and (b), public expert comments that identify the failing steps. These comments are held at L0+ (blog pages and arXiv metadata); the C3 skeptic re-located each quotation.

**Claim.** arXiv:0807.0090.
- v1 (1 July 2008) asserted that all nontrivial zeros lie on $\operatorname{Re}s=1/2$.
- v2–v3 (2–3 July 2008) asserted a proof of Bombieri's refinement of Weil positivity (cf. PAPER-0090), by Fourier analysis on number fields. The argument adapts Connes's trace formula (PAPER-0026) and goes through Li's criterion (PAPER-0193).

**Failure.**
- **(a) T. Tao, comment of 2 July 2008.** The decomposition claimed in (6.9) on p. 20 "is, in fact, impossible; it would endow the function $h$ … with an extremely strong dilation symmetry which it does not actually obey". This was fixed in v2/v3, as Tao agreed on 4 July.
- **(b) A. Connes, quoted on Woit's blog.** In Theorem 7.3 (p. 29), $h$ is extended "from ideles to adeles by 0 … and then using Fourier transform … This cannot work and ideles form a set of measure 0 inside adeles". Tao located it: "The first concrete error here arises in the equation after (7.13)", a change of variables on the idele class group in which $u$ is integrated over the adeles.
- **(c) Tao, revision of 7 July 2008.**
  - p. 18 needs "certain invertibility properties of E which fail if there is a zero off of the critical line";
  - a decomposition treats a subspace that is "merely dense" as if it were the whole space.
- **(d) v4 (6 July 2008):** "withdrawn by author, due to mistake on page 29".

**Status nuance.** The same arXiv identifier now also carries v5–v10 (4 Oct 2024 to 12 Oct 2025). These versions contain a new argument, via traces of integral operators, for positivity in Li's criterion.
- They have no journal reference.
- No published critique of them was located.
- They were **not audited**.

"Withdrawn" applies only to the 2008 text.

**Salvage.** Li's criterion (Li 1997; Bombieri–Lagarias 1999, PAPER-0195) and the Weil–Bombieri positivity target (PAPER-0090) are untouched.

**Lesson.**
- F8: a support of measure zero (ideles inside the adeles).
- F3: an invertibility that holds only if RH does.
- F7: a dense subspace taken to be closed.

## 17. Atiyah (2018)

**Kind:** FAILED.

**Fairness basis:**
- (c), the Observatory theorem C3-A1, which has a complete proof and was checked independently by the skeptic;
- a public, non-refereed critique (Lipton–Regan blog, 2018).

The preprint was never published as a refereed article. C3 found no zbMATH or Crossref record of it; the skeptic could not re-check that absence.

**Claim** (M. F. Atiyah, "The Riemann Hypothesis", a 5-page preprint from 2018; C3 read Sections 2–3 at L1).
- A function $T$ is postulated with property 2.6: $T\{[1+f][1+g]\}=T\{1+f+g\}$ for power series $f,g$ without constant term. Property 2.5 gives it a limit of about 137 on the critical line.
- Assume a zero $b$ off the line, and set $F(s)=T\{1+\zeta(s+b)\}-1$, so that $F(0)=0$ (3.2).
- "Take $f=g=F$ in 2.6". This gives $F=2F$, so $F\equiv0$ (3.3).
- "$T$ is not the zero polynomial and so it is invertible". Hence $\zeta\equiv0$, a contradiction.

**Failure.**

THEOREM (C3-A1; OBSERVATORY FINDING). Let $h$ be analytic at $0$, and suppose $h(u+v+uv)=h(u+v)$ as formal power series for all $u,v\in s\mathbb C[[s]]$. (This is property 2.6 with $h(w)=T(1+w)$.) Then $h$ is constant.

*Proof.* Put $u=v=s$, so that $h(2s+s^2)=h(2s)$. Write $h(w)=\sum c_kw^k$. The coefficient of $s^m$ in the difference is
$$\sum_{m/2\le k\le m-1}c_k\binom{k}{m-k}2^{2k-m}.$$
Its top term is $(m-1)2^{m-2}c_{m-1}$, and the other terms involve only $c_k$ with $k<m-1$. Induction on $m\ge2$ gives $c_{m-1}=0$. $\square$

The skeptic checked this independently: the triangular integer system for $c_1,\dots,c_{59}$ has a nonzero Bareiss determinant.

Consequences:
1. **Literal reading.** Read literally, 2.6 forces $T\equiv1$ near $1$. Then:
   - $F\equiv0$ holds for every function, so it says nothing about $\zeta$;
   - the step "$T$ invertible $\Rightarrow\zeta\equiv0$" is invalid;
   - constancy contradicts 2.5, given that $T$ is said to be a polynomial on compact convex sets.
2. **Approximate reading.** Atiyah remarks that 2.6 is "just the linear approximation". Under that reading, (3.3) does not follow.
3. **The argument proves too much.** Steps (3.1)–(3.3) never use $\operatorname{Re}b\ne1/2$. Applied verbatim at the on-line zero $\rho_1=\tfrac12+14.134725\ldots i$, they would show that $\zeta$ has no nontrivial zeros at all.

**Salvage.** None identified.

**Lesson.**
- F9: exhibit a model of every new object's axioms before using them. Here a two-line formal power-series check is enough.
- F2: locate where $\operatorname{Re}b\ne1/2$ is used.

## 18. Three self-withdrawn arXiv claims (2018–2026)

**Kind:** FAILED; withdrawn or self-flagged. **Fairness basis:** (a), the authors' own statements; and (c), explicit mechanisms in C3, each upheld by the skeptic. They are included only as compact illustrations of failure modes.

| Claim | Author's status | Mechanism of failure (Observatory) | Tags |
|---|---|---|---|
| Oliva, arXiv:1807.06447. v1: a proof of RH via Nicolas's criterion at primorials. v2: a disproof via the same criterion. | v3: "Withdrawn for expected critical errors in both versions" | C3-O1 (a proof sketch, re-derived by the skeptic). Step (3) of v1 is $(1-1/p)\log\log N_{n+1}\ge\log\log N_n$, where $N_n$ is the primorial and $p=p_{n+1}$. The function involved decreases in $\log N_{n+1}$, so substituting Dusart's *lower* bound runs the wrong way, and (4) does not imply (3). To first order, (3) says $\theta(p)-p\lesssim\tfrac12\log p$. Littlewood's $\Omega_+$ theorem makes this fail infinitely often, yet it holds for every $p\le2\cdot10^7$. | F10, F6, F5, F3, F15 |
| Queme, arXiv:2004.00460 | v2: "This paper contains an irrecoverable error paragraph 6 page 4". The footnote in v1 invited readers to find the error. | C3-Q1 (THEOREM). If $f$ is analytic on $D(\rho+v,v)$ and has a pole at $\rho$, then $\sum_k(-v)^kf^{(k)}(\rho+v)/k!$ diverges. (The radius of convergence is exactly $v$; then apply Abel's theorem.) So the termwise limit $\varepsilon\to0$ in step 6 is illegitimate. The same steps would also exclude the on-line zero $\rho_1$. | F6, F2 |
| Micheas, arXiv:2607.04338 | v2: "Mistakes in main approach. Withdrawn" | C3-M1 (THEOREM). Theorem 1 of v1 says that any increasing $\tau_n$ with $\lvert\tau_n-t_n\rvert\le b_n\downarrow0$ and $\sum\tau_n^{-2}<\infty$ gives $\tfrac12\prod(1-s(1-s)/(\tfrac14+\tau_n^2))=\xi(s)$. This is false: $\tau_n=t_n-1/(2n)$ is admissible, but the product does not vanish at $s_0=\tfrac12+it_1$. Product formulas take the zeros as input and cannot locate them. | F11, F2 |

Not audited and not characterized here: Oliva's v2 (the disproof version), and the archive's other Hadamard-product item (D. Liu, arXiv:2404.06306, an unrefereed disproof claim).

---

# Part VI. Synthesis

## 19. What the failures have in common

- **Refuted conjectures (§§3–6).** Each was either a sufficient condition stronger than RH or a condition that is false outright. All of them fell to explicit-formula arguments of Ingham type, or to explicit numerics at small height (de Branges fails at the 34th zero).
- **Failed proofs (§§16–18).** They share three faults:
  - a hypothesis that is never used (Atiyah, Queme, Micheas);
  - an error of support or domain (Li);
  - an inequality used in the wrong direction, or a limit taken at the boundary of convergence (Oliva, Queme).
- **Spectral programmes (§§10–13).** All of them stop at the same point: the existence of a *positive* inner product, which is equivalent to RH. Realizations alone are cheap (§2.3).
- **Density and numerical programmes (§§7, 9, 14).** The mathematics is correct, but it disperses or dilutes the information. Its RH content appears only at infinite height, or in a limit with logarithmic rate. In one case, the strongest form of the input is itself RH-strength (Bettin–Gonek).
- **Heuristic models (§15).** They are right on average and wrong at the scale that matters.

## 20. Reusable lessons and quick tests

This list incorporates the skeptic's corrections to C3-CHECKLIST.

1. **State the exact claim.** If it is a sufficient condition, check whether it is false outright. Test its necessary consequences at the first few thousand zeros (§6), and compare it with Ingham's theorem (§2.2). [F4]
2. **Countermodel test.** Run each step on the Davenport–Heilbronn function ($\rho_{DH}\approx0.80851718+85.69934848i$), on $\zeta_{19}$ (which has a zero with real part $1.0010955\ldots$), and on Epstein zeta functions. If every step survives, the argument is invalid. [F1]
3. **Proves-too-much test.** Mark where $\operatorname{Re}\rho\ne1/2$ is used. Rerun the argument at $\rho_1=\tfrac12+14.1347\ldots i$, on $1/(z-\rho)$, and on a perturbed zero set. [F2, F11]
4. **Positivity audit.** Name the Hilbert space; the inner product, which must be positive and not merely symmetric; the domain and the adjoint domain; and the deficiency indices. Check that the eigenvectors lie in the space and that supports have positive measure. [F7, F8]
5. **Circularity audit.** Test every invertibility, density or propagation lemma against a single hypothetical off-line pair of zeros. [F3]
6. **Quantifiers and limits.** "For fixed $b$, eventually in $x$" does not cover $b\sim x$. Name the theorem behind every interchange of limits. Never evaluate a power series on the boundary of its disc of convergence. [F6]
7. **Monotonicity.** Check which way each substituted bound moves the target. [F10]
8. **New objects.** Exhibit a model of every new object's axioms. [F9]
9. **Dispersal.** On a model with a known violation, measure how much data the criterion needs before it sees the violation (Farmer's $X_j$, Burnol, Voros). Compare that with what zero verification already gives. [F5]
10. **Finite ranges.** Estimate the Skewes-type scale of a first failure. [F5] For reference:

    | Conjecture | Holds up to | First failure |
    |---|---|---|
    | Mertens | $\lvert M(x)\rvert<\sqrt x$ for $1<x\le10^{16}$ | below $\exp(1.96\cdot10^{19})$ |
    | Pólya | every $x<906{,}150{,}257$ | $906{,}150{,}257$ |
    | Turán $T(x)$ | every $x<72{,}185{,}376{,}951{,}205$ | $72{,}185{,}376{,}951{,}205$ |

    C3-CHECKLIST item 13 stated "$\lvert M\rvert/\sqrt x<0.571$ up to $10^{16}$" with no lower limit. That is false for small $x$; for example $\lvert M(5)\rvert/\sqrt5\approx0.894$. Over $200\le x\le10^9$ the maximum is $0.5657$, attained at $x=200$.
11. **Density.** A proportion, even $1-o(1)$, is not RH. Also check whether the analytic input of a density method would give a zero-free region on its own (Bettin–Gonek). [F13]
12. **Models.** Predictions from random models and random matrix theory are hypotheses. Test them against Ω-theorems (Maier). [F12]
13. **Constants.** Re-derive imported explicit lemmas and test them on extremal examples, such as the Kusmin–Landau bound (Annex A). [F14]
14. **Rigour labels.** State whether each number is a certified ball, an exact integer, or floating point. High precision is not certification.
15. **Versions.** If a revision reverses the conclusion, the method does not discriminate (Oliva). A version count by itself is not a failure mode. [F15]
16. **Search for published obstructions before investing.** Conrey–Li, Ingham, Montgomery, Odlyzko–te Riele, Haselgrove, Maier, Farmer, Rodgers–Tao, Burnol, Bettin–Gonek.

---

## Annex A. Repaired explicit constants (an adjacent genre)

These are not abandoned approaches. They are documented errors with documented repairs, and they carry lesson 13.

| Item | Error and repair | Basis |
|---|---|---|
| Turing 1953 (PAPER-0474) | "Turing's paper contains several errors, which are fortunately corrected by Lehman" (Trudgian 2011, PAPER-0594; Lehman 1970, PAPER-0613). Lehman also corrected Titchmarsh's explicit error term in the Riemann–Siegel formula. | published; the C3 skeptic re-located Trudgian's sentence |
| Cheng–Graham 2004 (PAPER-0678), Lemma 2 | The Kusmin–Landau bound was stated as $1/(\pi\theta)+1$. The sharp constant is $2/\pi$; Landau's bound $\cot(\pi\theta/2)$ is attained. Hiary–Patel–Yang (PAPER-0242): "The incorrect constant 1/π has impacted all published explicit subconvex bounds". Hiary's bound $0.63\,t^{1/6}\log t$ becomes $0.77\,t^{1/6}\log t$, and HPY recover $0.618\,t^{1/6}\log t$ for $t\ge3$. C3-CG1 gives an explicit smooth counterexample (Arb, $\theta=0.02$): $\lvert S\rvert=31.59808527\ldots$, which exceeds $1/(\pi\theta)+1=16.9155\ldots$ and stays below $\cot(\pi\theta/2)=31.8205\ldots$ | published (HPY; the error was reported by K. Ford and J. Arias de Reyna), plus an Observatory witness |
| Ford 2002 (PAPER-0051) | The author's corrections appear in arXiv:1910.08205 v2–v5 (2022–2025). Theorem 4 changes from $1/(8.463\log\lvert t\rvert)$ to $1/(8.464\log\lvert t\rvert)$. Theorems 1 and 5 are unchanged. | author |
| Feng 2012 (PAPER-0046) | A gap reduced the admissible $\theta_F$ to $3/7$ (PRZZ). Pratt–Robles 2018 repaired it with $\theta_F=6/11$; see §14. | published |
| Pearce-Crump 2026 (arXiv:2609.15329) | v1 said "7%"; v2 says "6.78%", with the comment "Corrected proportion". | author |
| Bellotti–Trudgian–Yang 2026 (PAPER-0159) | The Table 1 entry $m_5=0.00735709$ is not a lower bound for the stated polynomial. An Arb witness gives the value $0.0073564919\ldots$ at $x=1.6495243\ldots$. With $m_5$ corrected, $\sum(\log p)m_p=0.2354513>0.23545$, so Theorem 1 (the zero-free region $\sigma>1-1/(4.896\log t)$) still holds. | Observatory L2/L3 (audit F7; public wording allowed) |
| Farmer 2022, Table 4.1 | See §7. | Observatory (audit F6) |

## Annex B. Re-check log: where this file departs from C3 or from other archive text

| Item | C3 or archive text | This file | Basis |
|---|---|---|---|
| C3-D9, ceiling item 2 | "Even Θ = ∞ gives only $N_0(T)\ge(1-o(1))N(T)$, which allows $o(N(T))$ off-line zeros" | This is true of Levinson's *counting output*. But the θ = ∞ *hypothesis* implies RH (Bettin–Gonek 2017). | PAPER-0064 (L1), THM-PAPER-0064-1 |
| C3-D9, ceiling item 3 | All three methods count via Littlewood's lemma. | Only Levinson–Conrey does. Hardy–Littlewood and Selberg count sign changes of $Z(t)$. | skeptic |
| C3-D9, ceiling item 1 | "$\kappa(\theta)<1$ for every proven θ" | Dropped, as a tautology. | skeptic |
| C3-D9 | Radziwiłł's lower bound is not discussed. | Added, flagged as unrefereed and as not bounding the Levinson proportion. | arXiv:1207.6583v3; LED-CRIT-9 |
| C3-D1 | "a sufficient condition strictly stronger than RH" | "a sufficient condition for RH that is false outright" | skeptic |
| C3-D1-scan | "phase-locking has no arithmetic reason to hold" | The failures are Gram-law-type irregularities. The scan assumes simple zeros on the critical line. | skeptic |
| C3-D4 | Weighted spaces shift the generator "by $i(\alpha+1)/2$". | The constant term is $i(\alpha+1)/2$, which is a shift of $i\alpha/2$ relative to $\alpha=0$. | skeptic; Bellissard p. 3, re-read here |
| C3-CHECKLIST item 13 | "$\lvert M\rvert/\sqrt x<0.571$ up to $10^{16}$" | Needs a lower limit (§20, item 10). | skeptic; LED-ARITH-7 |
| C3-TAX, F15 | Listed arXiv:2209.01890v58 as an example of a failure mode. | Removed: it is a version count only, and no error has been identified. | skeptic; methodology §6(iv) |
| Farmer Table 4.1, as quoted in the POS frontier and LED-POS-18 | "$d=118$" | 119. The $j=20$ column refers to a different function. | audit F6 |
| LED-OPS-14 draft (Lagarias 2005) | the structure-function property stated for $\lvert h\rvert\ge1/2$ | Lemma 2.1 gives $h\ge1/2$ unconditionally and $h>0$ under RH. The $\lvert h\rvert\ge1/2$ statement is Theorem 2.1, about $A_{h,\theta}$ and $B_{h,\theta}$. | the LED-OPS-14 verifier's correction |

## Annex C. Deliberately not characterized

- **Yang, arXiv:2301.03165** (audit F3). Classified `suspected_gap`, with public characterization **not** allowed. This file makes no statement about it.
- **arXiv:0807.0090 v5–v10** (2024–2025). Not audited.
- **De Branges's post-2004 manuscripts** (for example PAPER-0883). Not audited against Conrey–Li.
- **D. Liu, arXiv:2404.06306**, and **Oliva's v2**. Not audited.
- **Unrefereed claims that κ = 1**, recorded in LED-CRIT-20. No audit, so they are not characterized here.
- **Fayed, arXiv:2209.01890** (58 versions). The only fact recorded is the version count.
- **The 2026 quasi-RH claims** (zero-free half-planes $\operatorname{Re}s>7/8$ and $\operatorname{Re}s>11/12$) and **the Siegel-zero claims**. These are active and partially audited (audits/quasi_rh/DOSSIER.md; audits/claims_2026/SIEGEL/). They are not abandoned approaches and are outside this file.
- **Planat–Raymond, $\Lambda<0.156821$** (audit F8). No issue was found in the inspected portion, but the certificate was not replayed.

