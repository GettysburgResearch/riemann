# PAPER-0043 — Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Chandee, Vorrapan; Littmann, Friedrich; Milinovich, Micah B. |
| Year / stratum | 2017 / S6 |
| Venue | J. Reine Angew. Math. 725, 143-182 (2017). |
| Identifiers | zbMATH [1362.11078](https://zbmath.org/?q=an:1362.11078) · DOI [10.1515/crelle-2014-0078](https://doi.org/10.1515/crelle-2014-0078) · arXiv [1406.5462](https://arxiv.org/abs/1406.5462) |
| MSC | 11M06, 11M26 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1406.5462 |
| Selection | score 4.5695, in-pool citations 16, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, give optimal admissible (Fourier-supported in [-1,1]) majorants/minorants of the indicator of $[-\beta,\beta]$ with respect to the pair-correlation measure $d\mu=(1-(\sin\pi x/\pi x)^2)dx$, hence sharp bounds from Montgomery's formula for $N(T,\beta)$ for all $\beta>0$; solve the associated two-delta problem and a de Branges-space extremal problem.

**Historical motivation.** Montgomery 1973 pair correlation; Gallagher 1985 bounds for beta in (1/2)N; Montgomery-Taylor one-delta problem (proportion of simple zeros); Beurling-Selberg/Littmann extremal problems; use of de Branges spaces in extremal problems (Holt-Vaaler, Carneiro-Littmann).

### Main results

- **THM-PAPER-0043-1** (Theorem 1, theorem, scope: conditional; Section 1.1, eq. (1.10)). Assume RH. For every $\beta>0$ and admissible $R_\beta^\pm$ (i.e. $\hat R^\pm_\beta$ supported in $[-1,1]$, $R_\beta^-\le\chi_{[-\beta,\beta]}\le R_\beta^+$): $\frac12M(R_\beta^-)\le L(\beta)\le U(\beta)\le\frac12M(R_\beta^+)$, where $M(R)=\int R(x)(1-(\sin\pi x/\pi x)^2)dx$, $U(\beta)=\limsup N(T,\beta)/N(T)$, $L(\beta)=\liminf N(T,\beta)/N(T)$; the lower bound holds under the additional assumption $N^*(T)/N(T)\to1$ (almost all zeros simple), (1.11). *Conditional on:* RH, (1.11) for lower bound.
- **THM-PAPER-0043-2** (Theorem 2, theorem, scope: asymptotic; Section 1.2, eq. (1.17), p.4). For $\beta>0$ and the Beurling-Selberg functions $r_\beta^\pm$ (eqs. (1.15)-(1.16)): $\frac12M(r_\beta^\pm)=\beta\pm\frac12-\frac12... $ in the paper's form: $\frac12M(r^\pm_\beta)=\beta\mp\frac12... $ -- exact formula (1.17): $\tfrac12 M(r_\beta^{\pm})=\beta\pm\tfrac12-\tfrac12+\tfrac1{2\pi^2\beta}\cdots$ as printed with sine and sum terms; asymptotically $\frac12M(r_\beta^\pm)=\beta-\frac12\pm\frac12+\frac1{2\pi^2\beta}+O(\beta^{-2})$ (i.e. $\beta+\frac1{2\pi^2\beta}+O(\beta^{-2})$ for the majorant and $\beta-1+\frac1{2\pi^2\beta}+O(\beta^{-2})$ for the minorant), valid for all $\beta>0$; extends Gallagher's $\beta\in\frac12\mathbb N$ formula (1.12).
- **THM-PAPER-0043-3** (Theorem 3, theorem, scope: global; Section 1.3, eq. (1.20)). The Hilbert space $\mathcal H=B_2(\pi,\mu)$ of entire functions of exponential type $\le\pi$ with $\int|f|^2d\mu<\infty$ (norm equivalent to Paley-Wiener norm) has reproducing kernel $K(w,z)=f(w,z)+c(w)g(z)+d(w)h(z)$ with explicit $f,g,h,c,d$ (eqs. (1.19)-(1.20)); at $w=\pm1/(\pi\sqrt2)$ interpreted as a limit.
- **THM-PAPER-0043-4** (Theorem 4, theorem, scope: global; Section 1.3, eqs. (1.18), (1.21)). For $\beta>0$ let $\Delta(\beta)=\inf\{M(R):R\ge0\text{ admissible},R(\pm\beta)\ge1\}$. Then $\Delta(\beta)=\frac{2}{K(\beta,\beta)+|K(\beta,-\beta)|}=2\big(1-\frac{\sin2\pi\beta}{2\pi\beta}\big)+O(\beta^{-2})$ (as printed with $|\sin 2\pi\beta/2\pi\beta|$ in the discussion). Extremals: if $K(\beta,-\beta)=0$, $R(z)=K(\beta,\beta)^{-2}(c_1K(\beta,z)+c_2K(-\beta,z))\overline{(c_1K(\beta,\bar z)+c_2K(-\beta,\bar z))}$, $|c_1|=|c_2|=1$; if $K(\beta,-\beta)\ne0$, $R(z)=\frac{\big(\frac{K(\beta,-\beta)}{|K(\beta,-\beta)|}K(\beta,z)+K(-\beta,z)\big)^2}{K(\beta,\beta)+|K(\beta,-\beta)|}$-type formula as in paper (squared modulus form).
- **THM-PAPER-0043-5** (Theorem 5, theorem, scope: global; Section 1.4.3, p.9-10). For a Hermite-Biehler function $E$ with (P1)-(P4) (bounded type, no real zeros, $E(iz)$ real entire, $A,B\notin\mathcal H(E)$) and $\beta>0$, define $\Lambda^\pm_E(\beta)=\inf/\sup M_E(R_\beta^\pm)$ over $R^\pm$ of exponential type $\le2\tau(E)$ with $R^-\le\chi_{[-\beta,\beta]}\le R^+$ ($M_E(R)=\int R|E|^{-2}dx$). Then: if $\beta\in\{a_i\}$ (zeros of $A$): $\Lambda^+_E(\beta)=\sum_{A(\xi)=0,|\xi|\le\beta}1/K(\xi,\xi)$, $\Lambda^-_E(\beta)=\sum_{A(\xi)=0,|\xi|<\beta}1/K(\xi,\xi)$; same with $B$ if $\beta\in\{b_i\}$; if $b_k<\beta<a_{k+1}$: $\Lambda^\pm_E(\beta)$ given by $\sum(\xi^2+\gamma_\beta^2)/K_\beta(\xi,\xi)$ over zeros of $A_\beta$ with $|\xi|\le\beta$ (resp. $<\beta$), $\gamma_\beta=\beta B(\beta)/A(\beta)$, $E_\beta(z)=E(z)(\gamma_\beta-iz)$; case $a_k<\beta<b_k$ analogously with $B_\beta$, $\gamma_\beta=-\beta A(\beta)/B(\beta)$.
- **THM-PAPER-0043-6** (Corollary 6, corollary, scope: conditional; Section 1.4.3, eq. (1.34)). Assume RH and (1.11). Then $U(\beta)-L(\beta)\le\frac1{K(\beta,\beta)+|K(\beta,-\beta)|}=1-\frac{\sin2\pi\beta}{2\pi\beta}+O(\beta^{-2})$. *Conditional on:* RH, (1.11).
- **THM-PAPER-0043-7** (Theorem 7, theorem, scope: conditional; Section 1.5 (proof in Section 5)). Assume RH and (1.11). Then $N(T,0.606894)\gg N(T)$ (i.e. a positive proportion of zeros have a neighbour within $0.606894$ times the mean spacing; implies infinitely often consecutive gap $<$ mean spacing). Improves Montgomery's 0.6695... (stated 0.68) and Goldston-Gonek-Ozluk-Snyder's 0.6072.... *Conditional on:* RH, (1.11).
- **THM-PAPER-0043-8** (Theorem 8 / Corollary 9, theorem, scope: conditional; Section 2, eqs. (2.1)-(2.2), Corollary 9). Assume RH. For $\beta=\beta(T)>0$ with $\beta\sqrt{\log\log T}/\log T\to0$ (as printed: $(\log\log T/\log T)^{1/2}$ condition): $\frac12M(r_\beta^-)+\frac12(1-N^*(T)/N(T))+o(1)\le N(T,\beta)/N(T)\le\frac12M(r_\beta^+)+\frac12(1-N^*(T)/N(T))+o(1)$ (Theorem 8, printed form; $N^*(T)=\sum_{0<\gamma\le T}m_\gamma$). Corollary 9 (RH only, using Montgomery's $N^*(T)\le(4/3+o(1))N(T)$): $\beta-\frac76+\frac1{2\pi^2\beta}+O(\beta^{-2})+o(1)\le N(T,\beta)/N(T)\le\beta+\frac1{2\pi^2\beta}+O(\beta^{-2})+o(1)$. *Conditional on:* RH.
- **THM-PAPER-0043-9** (Theorem 18, theorem, scope: conditional; Section 7 (statement at lines ~2080 of text)). Assume GRH for Dirichlet L-functions, $\varepsilon>0$. For $\beta>0$: $\limsup_{Q\to\infty}N_\Phi(Q,\beta)/N_\Phi(Q)\le\beta-\frac14+\varepsilon+\frac1{2\pi^2\beta}+O(\beta^{-2})$; if in addition $N^*_\Phi(Q)\sim N_\Phi(Q)$, then $\liminf\ge\beta-\frac34-\varepsilon+\frac1{2\pi^2\beta}+O(\beta^{-2})$ (family-pair-correlation analogue for primitive Dirichlet L-functions, using Chandee-Lee-Liu-Radziwill large sieve evaluation of the q-analogue of Montgomery's $F(\alpha)$). *Conditional on:* GRH.

### Key definitions

- $N(T,\beta)=\#\{0<\gamma,\gamma'\le T:0<\gamma'-\gamma\le2\pi\beta/\log T\}$
- admissible function: $R\in L^1(\mathbb R)$ with $\hat R$ supported in $[-1,1]$
- $M(R)=\int R(x)\big(1-(\sin\pi x/\pi x)^2\big)dx$
- $U(\beta)$, $L(\beta)$ as limsup/liminf of $N(T,\beta)/N(T)$
- $N^*(T)=\sum_{0<\gamma\le T}m_\gamma$ (with multiplicity)
- de Branges space $\mathcal H(E)$, Hermite-Biehler $E$, companions $A,B$, kernel $K$

### Principal lemmas

- **THM-PAPER-0043-L1** (Lemma 11 (cf. [16, Thm 2]); Section 3 (line ~1254 of text)). Uncertainty-principle (Donoho-Stark/Folland-Sitaram type) inequality for $f\in L^2$, $\|f\|_2=1$ and measurable sets $T,W$ (statement as printed in Section 3). — *Role:* Shows that the measure $\mu$ and Lebesgue measure give equivalent norms on exponential-type-$\le\pi$ functions, so $\mathcal H=B_2(\pi,\mu)$ is a Hilbert space.
- **THM-PAPER-0043-L2** (Lemma 12; Section 3). Entire $f\in B_2(\pi)$ iff $f\in B_2(\pi,\mu)$, with comparable norms ($c>0$ constant). — *Role:* Used to show $A,B\notin\mathcal H(E)$ (property P4) and the identification $\mathcal H=\mathcal H(E)$.
- **THM-PAPER-0043-L3** (Lemma 13; Section 3 (line ~1438 of text)). Abstract Hilbert space lemma (statement as printed in Section 3, concerning minimization over a Hilbert space with given vectors $v_1,v_2$). — *Role:* Abstract two-point (two-delta) minimization used to derive Theorem 4 from the reproducing kernel.
- **THM-PAPER-0043-L4** (Corollary 14 (cf. Montgomery-Taylor [36]); Section 3). Let $R\ge0$ be admissible with $R(0)\ge1$. Then $M(R)\ge\ldots$ (one-delta bound: lower bound for the proportion of simple zeros; exact value as in paper). — *Role:* One-delta analogue; gives $N^*(T)/N(T)$ bounds referenced in the Remark after Corollary 9.
- **THM-PAPER-0043-L5** (Lemma 15 / Lemma 16; Section 4). Lemma 16: an entire $F$ of exponential type $\le2\tau(E)$ with $F\ge0$ on $\mathbb R$ and a suitable integrability condition factors as $|G|^2$ with $G\in\mathcal H(E)$-type representation (de Branges / Krein factorization used for the extremal problem). Lemma 15 concerns an interpolation property for $\beta\in$ ... (statement partly read). — *Role:* Reduction of the majorant/minorant extremal problem to quadrature (Gaussian-type) formulas at zeros of A or B, giving the sums in Theorem 5.
- **THM-PAPER-0043-L6** (Lemma 17; Section 5 (line ~1862 of text)). Assume RH and fix $A>1$. As $T\to\infty$, a lower-bound asymptotic for a second moment of Montgomery's pair-correlation weight (as printed in Section 5); used to improve Montgomery's small-gap threshold in Theorem 7. — *Role:* Second Montgomery-formula application with a different test function; feeds Theorem 7.
- **THM-PAPER-0043-L7** (Proposition 20 (Appendix A); Appendix A, line ~2154). The entire function $E(z)=L(i,z)/L(i,i)^{1/2}$ defined by (1.26) satisfies the Hermite-Biehler property (1.22) and $L(w,z)=E(z)E^*(w)-E^*(z)E(w)$ (1.27). — *Role:* Identifies the Hilbert space $B_2(\pi,\mu)$ with a de Branges space $\mathcal H(E)$, key identity (1.28).

### Proof architecture

Montgomery's formula (1.5) under RH gives for admissible R (Fourier transform supported in [-1,1]) lim (1/N(T)) sum R((gamma'-gamma) log T/2pi) w = R(0)+M(R). Inequality (1.8)-(1.9) with R^+ >= chi >= R^- yields Theorem 1: (1/2)M(R^-) <= L <= U <= (1/2)M(R^+) (lower bound needs almost-simple zeros). Optimization: (i) explicit Beurling-Selberg functions r^pm_beta give closed form M(r^pm) (Theorem 2, Section 2), extending Gallagher beyond beta in (1/2)N; (ii) for the exact optimum, the Hilbert space H=B_2(pi,mu) is shown to equal B_2(pi) as a set (Lemmas 11-12), its reproducing kernel K is computed explicitly (Theorem 3) and used with an abstract Hilbert-space lemma (Lemma 13) to solve the two-delta problem Delta(beta) (Theorem 4); (iii) H is identified with a de Branges space H(E) with E=L(i,.)/L(i,i)^{1/2} (Proposition 20, (1.26)-(1.28)) with properties (P1)-(P4); (iv) the majorant/minorant problem for chi_{[-beta,beta]} in L^1(|E|^{-2}dx) is solved in general (Theorem 5) via interpolation at zeros of A, B (or modified A_beta, B_beta from E_beta=E(z)(gamma_beta - iz)) and Lemma 16 (nonnegative exponential-type functions are |G|^2); Sections 5-6 use Montgomery's formula twice with two test functions to prove Theorem 7; Section 7 transfers to GRH-families (Theorem 18). Proofs in Sections 2-7 were skimmed (statements read, not verified).

Dependency edges: CAND-01810 → Gallagher 1985 (extends); CAND-01810 → Montgomery 1973 pair correlation (uses Montgomery's formula (RH)); CAND-01810 → Littmann (Beurling-Selberg for chi_[-beta,beta]) (uses); CAND-01810 → CAND-01416 (supplies small-gap input (Theorem 7) relevant to Radziwill's m(eps)>0 hypothesis)

**Imported results.** Montgomery's formula (1.5) (derivation in Gallagher's appendix); Beurling-Selberg majorants H^pm (Beurling; Selberg); Littmann's solution of the chi_{[-beta,beta]} L^1 problem; de Branges' theory (Theorems 19, 23 of de Branges' book; Krein's theorem); Montgomery: N*(T)<=(4/3+o(1))N(T) under RH; Fujii: N(T,beta)=N(T)beta+O(N(T)) unconditionally for beta=O(log T); Chandee-Lee-Liu-Radziwill large-sieve asymptotics (family case)

**Techniques.** Montgomery's pair correlation formula under RH; Beurling-Selberg extremal majorants/minorants; reproducing kernel Hilbert spaces of entire functions (Paley-Wiener with pair-correlation weight); de Branges spaces and Hermite-Biehler functions, Krein factorization; Gaussian-type quadrature at zeros of A, B for extremal functions; two-delta (Gallagher) / one-delta (Montgomery-Taylor) variational problems; large sieve for Dirichlet L-function families (Chandee-Lee-Liu-Radziwill)

## Context and interpretation

**Importance and obstacle overcome.** Provides the optimal (in the pair-correlation measure) majorant/minorant bounds for N(T,beta) for every beta>0, extending Gallagher's work from beta in (1/2)N, and pins down exactly what Montgomery's formula can and cannot deliver. Obstacle: for general beta the weighted measure dmu lacks the orthogonality Gallagher used; overcome by explicit reproducing-kernel formula and de Branges-space theory.

**Relation to prior work.** Extends Gallagher [19]; improves Montgomery [35] (0.6695) and Goldston-Gonek-Ozluk-Snyder (0.6072) under RH and simple zeros for small gaps; uses Littmann [32] solution of Beurling-Selberg for chi_{[-beta,beta]} and Holt-Vaaler / Carneiro-Littmann de Branges-space technology; family version via Chandee-Lee-Liu-Radziwill.

**Limitations and open questions.** All bounds on N(T,beta) are conditional on RH (and lower bounds on almost-all-simple zeros or the cruder N*<=4/3 N). The pair-correlation method cannot reach Montgomery's asymptotic: the gap between upper and lower bounds is at least (1/2)Delta(beta) approx 1 - sin(2 pi beta)/(2 pi beta) > 0; so only bounds, not asymptotics. The sharp de Branges majorants do not give a closed form in beta (nodes solve transcendental equations); only the Beurling-Selberg functions yield explicit asymptotics. Theorem 7's threshold 0.606894 is not optimal for small gaps in general (e.g. GRH-conditional results of GGOS are stronger); the small-gap threshold lambda_1 < 0.606894 vs conjectured 0 remains open.

## Research potential

- **Hypotheses that might be weakened.** Lower bounds need (1.11) or the crude 4/3 bound on N*/N (Montgomery); sharpening N*/N (Cheer-Goldston, Montgomery-Taylor) improves the lower bound in Corollary 9. The growth condition (2.1) on beta(T) ('may be possible to weaken slightly') is a technical error-term condition.
- **Generalizations.** The reproducing-kernel/de Branges method applies to other measures arising from families of L-functions (the authors cite [28,29]); Theorem 18 is the Dirichlet-family case under GRH; pair correlation of zeros of other degree-d L-functions where Montgomery's formula (with support in [-1,1] scaled) is available.
- **Candidate connections.** Radziwill (CAND-01416): Theorem 7 under RH + simple zeros gives m(eps) positive for eps>=0.606894 threshold, which feeds the quantitative Farmer-Ki / Soundararajan program; the optimal-majorant machinery could be combined with Fourier support widening if the Montgomery formula were extended beyond support [-1,1] (Rudnick-Sarnak/higher support for families).
- **Reusable lemmas.** Theorem 3 (explicit reproducing kernel for the pair-correlation weight) and Theorem 5 (general de Branges extremal-majorant theorem) are reusable for any Hermite-Biehler E with (P1)-(P4).
- **Possible experiments.** Numerically evaluate (1/2)M(R^pm_beta) for the exact de Branges extremals (Theorem 5 plus (1.20)) and compare with Odlyzko's zero statistics at T near 1e22 for N(T,beta)/N(T) over beta in (0,3); compute the smallest beta for which (1/2)M(R^-_beta)>0 from the exact extremal (Theorem 5) to see whether it beats 0.606894 (the paper reports 0.8163 for Beurling-Selberg minorants and 0.606894 from the two-test-function argument, Theorem 7).
- **Risks / barriers.** Method intrinsically limited by Fourier support [-1,1] in Montgomery's formula: gap U-L>=(1/2)Delta(beta) is not removable; any improvement needs correlation beyond support 1 (conjectural, as in Rudnick-Sarnak) or a different approach.

## Audit notes (Level 1 reader)

My transcription of Theorem 2's closed form is incomplete: extraction scrambled eq. (1.17); I give only the asymptotic (1.17b) as printed: (1/2)M(r^pm_beta) = beta - 1/2 pm 1/2 + 1/(2 pi^2 beta) + O(beta^{-2}), which I could only partially resolve from garbled text ('beta - 1/2 pm 1/2 + 1/(2pi^2 beta)' appears printed as beta - (1/2) +- ... ); the extract shows 'beta - 1/2 +- 1/2 + 1/(2 pi^2 beta) + O(1/beta^2)' consistent with Gallagher (1.12). In the record I wrote a messy placeholder for the exact form of Theorem 2 -- the asymptotic part is trustworthy, the 'exact formula' text is not (see paper eq. (1.17)). Similarly, the Theorem 4 extremal formula in case (ii) is only paraphrased. Theorem 4 statement mixes '2(1 - sin 2 pi beta/2 pi beta)' with a '|...|' in the commentary; I did not resolve whether the absolute value appears in (1.21) (extraction shows no absolute value in (1.21) but one in the prose). Corollary 14's explicit bound was not read.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01810`; harvest queries: kw_RH_any, kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_pair_corr, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — RH-conditional bounds on pair correlation via Hilbert-space extremal functions.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
