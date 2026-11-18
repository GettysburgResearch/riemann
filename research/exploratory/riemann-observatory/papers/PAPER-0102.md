# PAPER-0102 — Critical zeros of lacunary \(L\)-functions

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Iwaniec, H. |
| Year / stratum | 2020 / S6 |
| Venue | Acta Arith. 195, No. 3, 217-268 (2020). |
| Identifiers | zbMATH [1451.11092](https://zbmath.org/?q=an:1451.11092) · DOI [10.4064/aa180813-11-11](https://doi.org/10.4064/aa180813-11-11) · arXiv [1607.03288](https://arxiv.org/abs/1607.03288) |
| MSC | 11M20, 11M26, 11M41 |
| Families | B, G |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1607.03288 |
| Selection | score 4.312, in-pool citations 5, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** If a quadratic field discriminant D is 'epsilon-exceptional' (L(1,chi)log|D|<=epsilon, i.e. a Siegel-zero-like situation), how many zeros of the degree-2 'lacunary' L-functions L(s,psi) (and of zeta itself, since L(s,psi_0)=zeta(s)L(s,chi)) are simple and on the critical line, using Levinson's method with a mollifier? Does conditional existence of an exceptional sequence force 100% of zeta zeros on the line (and simple)?

**Historical motivation.** Heath-Brown posed at AIM 1996 whether under lacunarity zeros would behave 'evenly spaced' contrary to Montgomery's pair correlation; Conrey-Iwaniec 2002 related spacing of zeros of Hecke L-functions to class numbers and exceptional discriminants. Here they test the Levinson method in the hypothetical lacunary regime to learn what '100% on the line and simple' structure would imply.

### Main results

- **THM-PAPER-0102-1** (Theorem 2.1, theorem, scope: asymptotic; Sec.2, eq.(2.2)-(2.3), p.5). Let $L(s,\psi)$ be the class group L-function of $K=\mathbb Q(\sqrt D)$ (psi a character of Cl(K)), $N_{00}(T)$ the number of simple zeros $\rho=1/2+i\gamma$, $\gamma\sim T$ (i.e. $T<\gamma\le2T$), and $N(T)$ the total number of zeros in $0<\beta<1$, $\gamma\sim T$ with multiplicity. Then $N_{00}(T)=N(T)+O\big(T\log|D|+(L(1,\chi)\log T)^{1/4}T\log T\big)$ with absolute implied constant. With $\varepsilon=\varepsilon(D)=L(1,\chi)\log|D|$: $N_{00}(T)=\{1+O(\delta)\}N(T)$ for any $\delta\ge\varepsilon^{1/5}$ and every $T$ with $|D|^{1/\delta}\le T\le|D|^{\delta^4/\varepsilon}$.
- **THM-PAPER-0102-2** (Definition 1.1 / 2.2, definition, scope: conditional; Sec.1, (1.5), (1.10); Sec.2 (2.4)). chi is eps-exceptional if $L(1,\chi)\log|D|\le\varepsilon$; an infinite sequence of discriminants is exceptional if $\varepsilon(D)=L(1,\chi)\log|D|\to0$. Class group L-function $L(s,\psi)$ is then eps-lacunary: $\sum_{Q^4<n\le Q^{4A}}|\lambda(n)|n^{-1}\le\varepsilon A$ for all $A\ge1$, $Q=\sqrt{|D|}/2\pi$.
- **THM-PAPER-0102-3** (Corollary 2.3, corollary, scope: conditional; Sec.2, p.6). As $\varepsilon=\varepsilon(D)\to0$ over an exceptional sequence, for every $\psi\in\widehat{\mathrm{Cl}(K)}$ the critical simple zeros of $L(s,\psi)$ of height $\sim T$ comprise 100% of all zeros of height $\sim T$ for any $T$ with $|D|^{-\log\varepsilon}\le T\le|D|^{-\varepsilon^{-1}\log\varepsilon}$ (as printed; sign conventions of the exponents appear garbled in extraction). *Conditional on:* existence of an exceptional sequence of discriminants (Siegel-zero-like).
- **THM-PAPER-0102-4** (Corollary 2.4, corollary, scope: conditional; Sec.2, p.6). Along an exceptional sequence ($\varepsilon(D)\to0$) and $T$ in the range above, the number of simple critical zeros of $\zeta(s)$ of height $\sim T$ that differ from zeros of $L(s,\chi)$ is asymptotic to the number of all zeros of $\zeta(s)$ of height $\sim T$ (zeta and L(s,chi) zeros counts $\frac T{2\pi}\log T+O(T)$, $\frac T{2\pi}\log|D|T+O(T)$ sum to N(T)). *Conditional on:* existence of an exceptional sequence of discriminants.

### Principal lemmas

- **THM-PAPER-0102-L1** (Lemma 3.1; Sec.3). For $T\ge M^2\ge Q^8$, $0<a\le1/2$: $I_a(T)\le T^{4a}(I(T)+O(T^{7/8}))$ where $I_a(T)=\int_T^{2T}|F(\tfrac12-a+it)|dt$ and $I(T)=\int_T^{2T}|F(\tfrac12+it)|dt$. — *Role:* Moves the Levinson integral from the line Re s=1/2-a to the critical line via contour shift with kernel H(z)=2a(4-a^2)T^{4z}/((z^2-a^2)(z^4-4)).
- **THM-PAPER-0102-L2** (Lemma 3.2; Sec.3). For $T\ge M^2\ge Q^8$: $N_{00}(T)>N(T)-4I(T)\log T+O(T)$ with $F(s)=G(s)M(s)-1$, $G(s)=L(s)+L'(s)/\log N$ (Levinson's inequality from Prop. A of Conrey-Iwaniec-Soundararajan [CIS13], optimal shift a=1/(4 log T)). — *Role:* Reduces counting simple critical zeros to an L^1 mean value of the mollified function G M - 1.
- **THM-PAPER-0102-L3** (Sec.3 mollifier (3.10)-(3.13); Sec.3, p.9-10). $M(s)=\sum_{m\le M}\rho(m)g(m)m^{-s}$ with $\rho$ multiplicative, $\rho(p)=-\lambda(p)$, $\rho(p^2)=\chi(p)$ (coefficients of $L(s)^{-1}$), cropping $g(m)=(1-\log m/\log M)^r$ with $r$ large (r=32 works), M<=T^{1/2}; $\rho(m)=\mu(m)\lambda(m)$ for squarefree m, $|\rho(m)|\le\lambda_0(m)$. — *Role:* Mollifier approximating 1/G; high-order vanishing at endpoint needed to exploit sifting from lacunarity.
- **THM-PAPER-0102-L4** (Proposition 4.1; Sec.4). Approximate functional equation / decomposition for $s$ in critical strip: $G(s)=A(s)+X(s)B(s)+X(s)R(s)+R_f(1-s)(1-s)^{-2}$ with $R=L(1,\chi)$ residue term when psi trivial. — *Role:* Expression of G(s) as sum of two Dirichlet-type pieces plus remainder, used to compute mean square-ish quantity I(T).
- **THM-PAPER-0102-L5** (Sec.6-12 (diagonal terms; Lemma 7.1-7.3, 9.1, 10.1); Secs.6-12). Estimates of diagonal terms of the mollified mean value, using lacunarity bound sum_{Q^4<n<=Q^{4A}} |lambda(n)|/n <= eps A, sieve of small dimension, sums of Mobius-type function; conclusion in lower bound (12.1) for N_00(T). — *Role:* Shows main diagonal contribution gives error O(eps^{1/4} log factor) relative to N(T).
- **THM-PAPER-0102-L6** (Proposition 14.1 / Props 15.1, Lemmas 16.1-21.4; Secs.13-23). Off-diagonal terms: convolution sums B(h) (14.1) equal predicted main term plus error R(h) (Prop 14.1), evaluation of special series S(h), phi(z), k*(y), J*(u,v), lambda-functions, estimates E_ab, E (Secs.13-23), adapting Conrey-Iwaniec [CI02] 'Spacing of zeros of Hecke L-functions and the class number problem'. — *Role:* Bounds off-diagonal contribution K_{\ne}(T) by a quantity not exceeding existing error term in (12.1).

### Proof architecture

Levinson method (Conrey 1989; CIS13): count simple critical zeros via N_00(T)>N(T)-4I(T)log T with F=GM-1, G=L+L'/log N (Lemma 3.2 using contour shift Lemma 3.1). Lacunarity (small epsilon from exceptional chi) makes mollifier M of length M<=T^{1/2} behave nearly perfectly: a sifting of small dimension along n in [Q^4,Q^{4A}]. Sec.4-12: expand I(T)-type mean values; diagonal terms handled by Lemmas 7.x, 9.x, 10.x (squarefree reductions, Mobius sums) giving lower bound (12.1). Sec.13-23: off-diagonal terms via shifted convolution sums and Kuznetsov/Voronoi-type technology adapted from Conrey-Iwaniec 2002, split into pieces estimated uniformly (22.11, 22.13, 23.10). Sec.24: finishing; remaining part K_1(T) claimed to contribute no more than K^*(T) 'without repeating many of the same arguments' -- i.e. a portion is argued only by sketch.

**Imported results.** Levinson inequality: Proposition A of Conrey-Iwaniec-Soundararajan 2013 (Critical zeros of Dirichlet L-functions, Crelle 681) ; Conrey 1989 (two fifths); Conrey-Iwaniec 2002 'Spacing of zeros of Hecke L-functions and the class number problem' (off-diagonal technology); convexity bounds for L(s,psi) and functional equation; Siegel's theorem L(1,chi)>>|D|^{-theta} (ineffective) as reason sequences are hypothetical; Iwaniec-Kowalski formula (22.109) for sum lambda_0(n)/n

**Techniques.** Levinson's method with mollifier; lacunary (sifting) structure from exceptional character / Siegel-zero scenario; shifted convolution (off-diagonal) sums, adapted from Conrey-Iwaniec 2002; Dirichlet series of 1/L as mollifier coefficients; contour shift kernel to move Levinson integral onto the critical line

## Context and interpretation

**Importance and obstacle overcome.** Shows that if a sequence of discriminants with L(1,chi) log|D|->0 existed (a strong Siegel-zero/exceptional-character hypothesis), then Levinson's method with a near-perfect mollifier gives 100% of zeros of L(s,psi), and hence of zeta(s), on the critical line and simple. Authors explicitly say such L-functions probably do not exist in reality (RH would imply L(1,chi)>>1/log log|D|), so it is mainly an exercise in technique and in what the exceptional-character scenario forces. Obstacle: controlling off-diagonal terms with mollifier length up to T^{1/2} while exploiting sifting; the root factor does not interfere.

**Relation to prior work.** Parallel to Conrey-Iwaniec-Soundararajan 2013 (critical zeros of Dirichlet L-functions: asymptotically 100% of zeros on the line in the family of L(s,chi) with weights), Conrey 1989 (two fifths), Conrey-Iwaniec 2002; relates to Heath-Brown AIM 1996 question about evenly spaced zeros and Siegel zeros (Montgomery pair correlation contradiction scenario: Montgomery pair correlation would predict small gaps whereas lacunary case would predict evenly spaced).

**Limitations and open questions.** Conditional on the (probably counterfactual) existence of a sequence of exceptional discriminants; T-range |D|^{1/delta}<=T<=|D|^{delta^4/eps} is extremely narrow relative to D; only degree-2 (quadratic field) class-group L-functions treated; authors remark the argument does not cover degree>2 even under very strong lacunarity. Section 24: the proof of the K_1(T) piece is sketched rather than completed. The statement for zeta (Cor 2.4) concerns zeros at heights in a window depending on D, not all heights T->infty.

## Research potential

- **Hypotheses that might be weakened.** The exceptional hypothesis eps(D)->0 could be weakened to L(1,chi) << (log|D|)^{-2015}, where they say simpler arguments would suffice; or weakened to any rate of eps(D) that lets the T-window cover heights needed. The extremely thin range T<=|D|^{delta^4/eps} is the main limitation.
- **Generalizations.** Twists by Dirichlet characters chi_1 (they note L(s,chi_1)L(s,chi chi_1) case generalizes Cor 2.4 to Dirichlet L-functions L(s,chi_1)); other Hecke L-functions of imaginary/real quadratic fields; general lacunary degree-2 L-functions satisfying (1.5) (Section 1 setup is general, only quadratic case worked out).
- **Candidate connections.** Siegel zeros and RH: a 'conditional' statement of type 'exceptional characters => nicer zero statistics for zeta' (Landau-Page type phenomena: Siegel zero repels zeros / forces pair correlation changes); contradiction with Montgomery pair correlation (positive proportion small gaps) -- a 'proof by exceptional-character' scenario suggests testing consistency of Heath-Brown-type results (Conrey-Iwaniec 2002 class number); relation to Rodgers-Tao Lambda>=0 (small gaps at 100% zeros in window); Deuring-Heilbronn zero repulsion.
- **Reusable lemmas.** Lemma 3.1/3.2 (Levinson inequality with contour shift and optimal shift a=1/(4 log T)); mollifier choice (3.10)-(3.13) with cropping (log m/log M)^r, r=32; the formal framework of epsilon-lacunary L-functions (1.5).
- **Possible experiments.** Numerical check of the structure: compute L(1,chi) log|D| for known smallest values to see how far from 'exceptional'; test via actual computed L(s,psi) zeros the Levinson-type ratio I(T)/T as function of epsilon to see the predicted epsilon^{1/4} scaling; check whether the off-diagonal term in Sec.22-23 is as small as claimed for moderate epsilon.
- **Risks / barriers.** Hypothesis likely vacuous (RH implies L(1,chi)>>1/log log|D|, and Siegel's ineffective bound only gives |D|^{-theta}); results can not give unconditional information about zeta. Presentation: some steps (K_1(T)) sketched; off-diagonal analysis very heavy (~25 pages) and not independently simplified.

## Audit notes (Level 1 reader)

Sec.24 (p.48): the contribution of K_1(T) is handled by the statement 'Without repeating many of the same arguments we claim that K_1(T) contributes no more than K^*(T)' -- the proof of this piece is sketched, not given in full in this arXiv v1; also the extracted ranges of T in Cor 2.3 ('|D|^{-log eps} <= T <= |D|^{-eps^{-1} log eps}') and Thm 2.1 exponent '|D|^{delta^4/eps}' are from a garbled PDF extraction and should be checked against the published version. Also the abstract-level (triage) claim 'assuming a sequence of exceptional discriminants, 100% of zeta zeros are on the critical line and simple' is accurate only for T in the narrow window depending on D, not for all T. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01971`; harvest queries: kw_RH_any, msc_11M20, msc_11M26, arxiv_critical_line, arxiv_zeta_zeros.
- Triage decision: include — Conditional on Siegel-zero-like discriminants, 100% critical zeros; striking.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
