# PAPER-0135 — The class number of quadratic fields and the conjecture of Birch and Swinnerton-Dyer

| Field | Value |
|---|---|
| Authors | Goldfeld, Dorian M. |
| Year / stratum | 1976 / S3 |
| Venue | Ann. Sc. Norm. Super. Pisa, Cl. Sci., IV. Ser. 3, 623-663 (1976). |
| Identifiers | zbMATH [0345.12007](https://zbmath.org/?q=an:0345.12007) |
| MSC | 11M20, 11G40, 11R11, 11R29 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — http://www.numdam.org/item/ASNSP_1976_4_3_4_623_0.pdf |
| Selection | score 3.5172, in-pool citations 22, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can one obtain an effective lower bound for L(1,chi) of real primitive characters (hence for class numbers of imaginary quadratic fields), by twisting the L-function of an elliptic curve with CM and zero of order g at s=1 (the Birch-Swinnerton-Dyer situation) by chi and Liouville's function, so that growing rank implies growth of h(-d)?

**Historical motivation.** Siegel's bound L(1,chi)>c(eps)d^{-eps} is ineffective; effective lower bounds were known only via Heegner-Stark-Baker for class numbers 1 and 2 (giving L(1,chi)>3 pi/sqrt d for d>427). Siegel zeros contradict GRH; Goldfeld proposes using a BSD-type zero of high order as a substitute.

### Main results

- **THM-PAPER-0135-1** (Theorem 1, theorem (conditional on existence of a CM elliptic curve over Q with analytic order of vanishing g), scope: conditional; Sec. 1, p.624). Let $E/\mathbb{Q}$ be an elliptic curve with conductor $N$ with complex multiplication, and suppose $L_E(s)$ has a zero of order $g$ at $s=1$. Then for every real primitive Dirichlet character $\chi \pmod d$ with $(d,N)=1$ and $d>\exp\exp(c_1 N g^3)$, $$L(1,\chi) > \frac{c_2}{g^{40g}N^{13}}\cdot\frac{(\log d)^{g-\mu-1}\exp\!\big(-21 g^{3/2}(\log\log d)^{1/2}\big)}{\sqrt d},$$ where $\mu\in\{1,2\}$ is chosen so that $\chi(-N)=(-1)^{g-\mu}$, and $c_1,c_2>0$ are effectively computable and independent of $g,N,d$. (Exact exponent of g in the denominator is read from a low-resolution page image; verify.) *Conditional on:* existence of a CM curve with analytic rank g (known only for small g at the time).
- **THM-PAPER-0135-2** (Theorem 5, theorem (stronger form), scope: conditional; Sec. 4, p.643). Under the hypotheses of Theorem 1, $$L(1,\chi)\gg \frac{g^{-40g}N^{-13}(\log d)^{g-\mu-1}}{\sqrt d\,(\log\log d)^{g-\mu+6}}\prod_{\substack{\chi(p)\ne -1\\ p<(\log d)^{8g}}}(1+p^{-1/2})^{-4}$$ with effective implied constant independent of g,N,d (displayed exponents read from a page image). *Conditional on:* ord_{s=1} L_E = g.
- **THM-PAPER-0135-3** (Theorem 2 (Deuring, imported), imported theorem, scope: global; Sec. 2, p.628). For E/Q with CM by an imaginary quadratic field K, $L_E(s)=L(s,\psi)$ for a primitive Grossencharakter $\psi$ of K.
- **THM-PAPER-0135-4** (Introduction, remark, remark, scope: conditional; Sec.1, p.624-625). Theorem 1 also holds for non-CM curves if $L_E$ comes from a cusp form of $\Gamma_0(N)$ (Weil's conjecture); more generally for products of Euler factors of elliptic-curve type with zero of order g at s=1 and zero of order related to Tate's conjectures at s=2. *Conditional on:* Weil modularity conjecture (as of 1976).
- **THM-PAPER-0135-5** (Sec.1 p.626, consequence remark, scope: conditional; Sec.1, p.626). If for Wiman's curve (CM, rank at least 4) one could prove $L_E$ has a zero of order $4$ at $s=1$, then $h(-d)\to\infty$ effectively and the class number problem $h(-d)=\text{const}$ would be effectively solvable.

### Key definitions

- Grossencharakter of an imaginary quadratic field with conductor f
- twisted function L_E(s,chi) with functional equation sign (-1)^{g}
- G(s,chi) measuring deviation of chi(n) from lambda(n)

### Principal lemmas

- **THM-PAPER-0135-L1** (Lemma 1; Sec.2, p.629-630). For $n\le x$ coefficients of the Dirichlet series of the twisted/Liouville-modified function agree with those of $G(s,\chi)q^{-2s}$, where $G$ measures the deviation of $\chi(p)$ from $\lambda(p)=-1$ (statement garbled in OCR). — *Role:* links smallness of L(1,chi) to chi(p)=-1 for most small p
- **THM-PAPER-0135-L2** (Theorem 3 / Theorem 4; Sec.3, p.631-637). Asymptotic expansions of the Dedekind zeta function $\zeta_K(s)L(s,\chi)$ of imaginary (Thm 3, d>4, chi(-1)=-1) and real (Thm 4, chi(-1)=+1) quadratic fields as sums over reduced forms of discriminant -d / d via Epstein zeta functions (Iseki; Hecke). — *Role:* explicit evaluation of sums of the coefficients $\nu_n$ of $\zeta(s)L(s,\chi)$
- **THM-PAPER-0135-L3** (Lemma 4; Sec.3, p.637-638). For d>4, $\sum_{n<\sqrt d/ 4}\nu_n n^{-1/2}$ is bounded in terms of $L(1,\chi)$ via the class number formula. — *Role:* upper bound feeding Lemma 9
- **THM-PAPER-0135-L4** (Lemmas 5-8; Sec.3, p.639-643). Partial-sum estimates of $\nu_n$ with errors expressed via $L(1,\chi)$; Lemma 7: for $x>d>\tfrac14\sqrt d$ and $10<y<\tfrac14\sqrt d$, $\sum n^{-1/2}\sum_{m|n,m\le y}\nu_m\nu_{n/m}\le 1500(L(1,\chi)^2xy^{-1/2}+L(1,\chi)x^{1/2})(\log y)^3$. — *Role:* controls second-moment of nu_n
- **THM-PAPER-0135-L5** (Lemma 9; Sec.4, p.643-644). Let $d>\exp(500g^3)$. Then either $L(1,\chi)>(\log d)^{g-\mu-1}d^{-1/2}$ or $P=\prod_{\chi(p)\ne-1,\,p<(\log d)^{8g}}(1+p^{-1/2})^{-4}<\exp(20g^{1/2}(\log\log d)^{1/2})$. — *Role:* reduces Theorem 1 to Theorem 5: small L(1,chi) forces chi(p)=-1 for almost all small p, a dichotomy
- **THM-PAPER-0135-L6** (Lemmas 10, 11; Sec.4, p.646-647). Lavrik-type approximate functional-equation expansion differentiated K times at s=1/2 splits into T1, T2; Lemma 10: if K<=g, d>exp(500g^3) then |T2|<1; Lemma 11 gives either the target lower bound or a bound on T1. — *Role:* main analytic step; zero of order g at s=1/2 of phi(s) kills the first g derivatives
- **THM-PAPER-0135-L7** (Lemma 12; Sec.5, line ~1566 of text). Statement about primitive Grossencharakter psi of conductor f (used for Sec.5); not read in detail. — *Role:* conductor bookkeeping

### Proof architecture

Twist L_E(s) by chi and by Liouville's function lambda to build phi(s)=L(s+1/2,E x chi)-type function with functional equation, and key function G(s,chi)=zeta(s)L(s,chi)/zeta(2s)-style Euler product comparison. (1) If L(1,chi) is small then chi(p)=-1 for most small primes p, so chi behaves like Liouville's lambda and G is near 1. (2) Theorems 3-4 and Lemmas 4-8 express partial sums of the Dirichlet coefficients of zeta_K(s) in terms of L(1,chi). (3) Lavrik's approximate functional equation for the twisted L-function L(s,E x chi), differentiated K<=g times at the center s=1/2 where ord=g, yields: either L(1,chi) is large (lower bound) or a contradiction from the main term; the parity sign delta=1+(-1)^K chi(-N) forces choice of mu. Deuring (Thm 2) supplies Hecke Grossencharakter structure and the functional equation for CM curves.

Dependency edges: CAND-00433 → Deuring: L-function of CM elliptic curve is Hecke L (uses); CAND-00433 → Lavrik 1966 (uses method); CAND-00433 → Goldfeld-Schinzel 1975 On Siegel's zero (builds on)

**Imported results.** Deuring: L of CM curve is Hecke L (Thm 2); Hecke functional equation for Grossencharakter L-functions (Hecke 1920); Lavrik 1966 functional equations of Dirichlet functions; Weil 1967 converse-type principle; Ogg 1969; Tate 1965 conjectures (remarks); Dirichlet class number formula

**Techniques.** Lavrik approximate functional equation; twisting by chi and Liouville function; Epstein zeta / Iseki-Hecke expansions of zeta_K L; Mellin transforms; differentiation at the central point to exploit a zero of order g; Deuring: L_E = Hecke L(s,psi)

## Context and interpretation

**Importance and obstacle overcome.** First effective lower bound for L(1,chi) growing with d in terms of a high-order zero at s=1 of an L-function of an elliptic curve, bypassing the Siegel zero ineffectivity by using extra zero order at the central point. It turned the Gauss class number problem into an existence question for elliptic curves with analytic rank 3 (later Gross-Zagier, outside this paper).

**Relation to prior work.** Builds on Goldfeld-Schinzel (Siegel's zero, Annali SNS 1975), Goldfeld-Chowla (twisting Epstein zeta), Stark and Baker, Iseki; uses Lavrik's method.

**Limitations and open questions.** Needs analytic rank g curve (g=3 not available at the time; Stephens' curve only shown to have odd order >1). Bound degrades with g (exp(-21 g^{3/2}(log log d)^{1/2}) and g^{-40g}) and requires d>exp exp(c1 N g^3). The paper does not settle whether such curves exist with g>=3 (later resolved in the literature outside this source).

## Research potential

- **Hypotheses that might be weakened.** Require ord_{s=1}L_E=g exactly; try only an inequality ord >= g (the argument differentiates K<=g times at s=1/2, Lemmas 10-11, so >= may suffice) and replace CM by modular (remark p.624).
- **Generalizations.** Other L-functions with zero of order g at the central point and a functional equation; sign and mu choice generalize to Rankin-Selberg twists.
- **Candidate connections.** Siegel zero vs central high zero: the same dichotomy (small L(1,chi) forces chi(p)=-1) is the pretentious-multiplicative-function viewpoint; link to Deuring-Heilbronn repulsion.
- **Reusable lemmas.** Lemma 9 dichotomy and Lemma 7-8 second-moment bounds on nu_n.
- **Possible experiments.** Numerically tabulate the product P over primes p<(log d)^{8g} for known fundamental discriminants with smallest L(1,chi) to test Lemma 9 dichotomy; compute theorem 1 lower bound constants for g=3 explicit CM curve.
- **Risks / barriers.** Extremely large threshold d>exp exp(...) makes the result non-computational for classical class number problems; constants c1,c2 not explicit in this paper.

## Audit notes (Level 1 reader)

Two small oddities in inspected portion: Theorem 1 as printed gives g^{40g} in the intro display? image reads g^{40} N^{13} in the denominator (I could only read at 80 dpi). The OCR text of formulas is unreliable; the Theorem 1, 5 and Lemma 9 statements here were checked on page images, other displays not. Otherwise none noticed in inspected portion. Sec.5 (proof of Theorem 5) not read closely.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00433`; harvest queries: msc_11M20, citation_expansion.
- Triage decision: include — Goldfeld: class number lower bounds via L-function zero of Birch-Swinnerton-Dyer type; route to effective Siegel-zero treatment.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
