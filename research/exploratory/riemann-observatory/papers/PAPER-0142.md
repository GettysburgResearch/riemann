# PAPER-0142 — Quelques remarques sur la croissance de la fonction \(\zeta(s)\)

| Field | Value |
|---|---|
| Authors | Lindelöf, E. |
| Year / stratum | 1908 / S2 |
| Venue | Darb. Bull. (2) 32, 341-356 (1908). |
| Identifiers | zbMATH [39.0488.01](https://zbmath.org/?q=an:39.0488.01) |
| MSC | 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/download/s2bulletindessci32fran/s2bulletindessci32fran_djvu.txt |
| Selection | score 2.6524, in-pool citations 10, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give simple, self-contained derivations of the growth of zeta(s) in the critical strip: a Phragmen-Lindelof-type lemma and its application show that log-convexity of the exponent of growth mu(sigma) (convexity bound), obtain lower bounds for the growth, and discuss the question whether |zeta(1/2+it)| stays below t^epsilon (the Lindelof hypothesis) and what follows under RH. (Basis includes OCR gaps; partial text.)

**Historical motivation.** Following Mellin, Landau and Phragmen-Lindelof (1908 Acta Math.), the question was how fast zeta can grow in the critical strip, a question tied to the zero distribution and to the Riemann hypothesis (RH implies growth t^epsilon for sigma>1/2). Lindelof formulated the unproven bound |zeta(1/2+it)|=O(t^epsilon).

### Main results

- **THM-PAPER-0142-1** (Section 1 (preliminaries), proposition, scope: asymptotic; Part I, section 1, pp. 341-344). For \sigma\ge1+\varepsilon, |\zeta(\sigma+it)| lies between finite positive limits (Euler product); via the functional equation \zeta(s)=\ldots\zeta(1-s), for \sigma\le-\varepsilon one has |\zeta(\sigma+it)|=h\,|t|^{1/2-\sigma}; in the critical strip |\zeta(\sigma+it)| grows less than a finite power of |t| (Euler summation, eq. (4)); and (Mellin 1900) \zeta'/\zeta-type expressions (6) are bounded on the lines \sigma=1 and \sigma=0 up to log factors: |\zeta(1+it)|=O(\log|t|), |\zeta(it)|=O(|t|^{1/2}\log|t|) (Landau 1908 refinements are cited in a footnote).
- **THM-PAPER-0142-2** (Lemma of section 2 (Phragmen-Lindelof), lemma, scope: global; Part I, section 2, pp. 344-345). Let f(s) be single-valued analytic in the half-strip-type domain \sigma_1\le\sigma\le\sigma_2, |t|\ge t_0, regular at all finite points of the domain, with |f|\le M on the two boundary lines (or bounded by a finite quantity), and with |f(s)|\le C|t|^{\mu}-type growth (condition 3: |f(s)|\,/\,|t|^{\alpha} bounded for some finite \alpha). Then the bound proved on the boundary persists in the interior. (Particular case of the Phragmen-Lindelof theorem established with Phragmen in a recent Acta Math. memoir; proof sketched via e^{\varepsilon i s}f(s) and the maximum principle.)
- **THM-PAPER-0142-3** (Section 3 theorem (convexity bound), theorem, scope: asymptotic; Part I, section 3, p. 346). For every \varepsilon>0, \zeta(\sigma+it)=O\big(|t|^{(1-\sigma)/2+\varepsilon}\big)... precisely, with h as defined in the paper, the expression \frac{|\zeta(\sigma+it)|}{|t|^{\,(1-\sigma)/2}\ldots} stays below a finite limit in the domain 0\le\sigma\le1, |t|\ge t_1>1. (Printed form: 'L'expression ... 1-sigma ... reste au-dessous d'une limite finie dans le domaine 0<=sigma<=1, |t|>=t_1>1.' It is the convexity bound \mu(\sigma)\le(1-\sigma)/2 on [0,1] with logarithmic factors; exact power is a reconstruction since the display is garbled.) Note: the paper states it with greater precision than previous bounds (Mellin's \zeta(\sigma+it)=O(t^{(1-\sigma)/2+\ldots}), Landau 1908).
- **THM-PAPER-0142-4** (Section 4-5 (lower bound results), theorem, scope: asymptotic; Part I, sections 4-5, pp. 347-350). As an application of the lemma (section 4, via F(s)=s^{?}\ldots\sin(\pi s/2)\Gamma(1-s)\,\ldots and f(s)=\zeta(s)/F(s)): the growth exponent \mu(\sigma) (for suitable definition) is nonincreasing/convex, and the expression |\zeta(\sigma+it)|\,|t|^{-\,a} does not tend to zero for any \sigma in the critical strip for a below a computed value; in particular, for every \varepsilon>0 and \sigma in the stated interval \ |\zeta(\sigma+it)|\,/\,t^{\,\ldots-\varepsilon} does not tend to 0 (Section 5, p. 349-350, 'limite inferieure de la croissance').
- **THM-PAPER-0142-5** (End of Part I (pp. 354-356), the question, conjecture, scope: conditional; pp. 354-356). Does |\zeta(1/2+it)|\,|t|^{-\varepsilon} stay bounded for every \varepsilon>0, or more generally does |\zeta(\sigma+it)| stay bounded for every \sigma>1/2? If so one obtains 'relatively simple results' about the growth of \zeta: \mu(\sigma)=0 for \sigma\ge1/2 (hence \mu(\sigma)=1/2-\sigma for \sigma\le 0 and 1/2-\sigma/... piecewise linear by convexity and functional equation). Also stated (p. 355): if one admits with Riemann that \zeta(s)\neq0 for \sigma>1/2 then \zeta(\sigma+it) for \sigma>1/2 stays below a finite limit up to \sigma'-\varepsilon, i.e. RH \Rightarrow Lindelof hypothesis (the printed claim: 'on peut demontrer que ... reste inferieur a une limite finie' for \sigma\ge\sigma'+\varepsilon). This is the first statement of the Lindelof hypothesis.

### Principal lemmas

- **THM-PAPER-0142-L1** (Section 2 lemma; Section 2, pp. 344-345). Phragmen-Lindelof principle on a half-strip: if f is regular and of finite order in \sigma_1\le\sigma\le\sigma_2,|t|\ge t_0 and satisfies |f|<M on the boundary lines then |f|<M in the interior (with the e^{\varepsilon i s} trick). — *Role:* Engine for convexity bounds and for the function mu(sigma) log-convex.
- **THM-PAPER-0142-L2** (Section 6 lemma (harmonic function in an angle); Section 6, pp. 351-353). Let u(x,y) be harmonic, finite and continuous in the domain \sigma_0\le\sigma, a sector of opening < pi, regular inside, with r^{-\nu}|u| bounded for \nu<\lambda. If \limsup_{r\to\infty}u\le0 on each bounding ray then u<\varepsilon in the interior sector for r large; and dually for liminf. (Proved by conformal mapping onto a disc and Poisson's integral/Schwarz.) — *Role:* Tool for the lower bound argument: show that if |zeta| were too small on one boundary, one gets a contradiction on the real axis, so that mu is a convex function and the growth limits are sharp.
- **THM-PAPER-0142-L3** (Section 1, equation (6) (Mellin); Section 1, pp. 343-344). The expressions \zeta(1+it)\,/\,\log|t| and \zeta(it)/(|t|^{1/2}\log|t|)-type are bounded for |t|\ge t_0 (Mellin, Acta Soc. Sc. Fennicae 29, 1900, pp. 4-49; refined by Landau, Bull. SMF 33 (1905)). — *Role:* Boundary values on sigma=0,1 for the Phragmen-Lindelof lemma.

### Proof architecture

Section 1 recalls: Euler product estimates for sigma>1, functional equation for sigma<0, Euler-Maclaurin for polynomial growth in the strip, and Mellin's boundary bounds on sigma=0,1. Section 2 proves the Phragmen-Lindelof-type lemma. Section 3 applies it to F(s)^{-1}zeta(s) (F=gamma-factor with explicit asymptotics (10)-(11)) in the strips 0<=sigma<=1 to get the convexity bound with log factors. Sections 4-5 derive lower bounds (zeta cannot be too small in the strip) from the same lemma in the opposite direction, using the harmonic-function lemma of section 6 on log|f| in angular domains (section 7). The second part discusses the question |zeta| bounded for sigma>1/2 and obtains results under the assumption RH. Imported: Mellin 1900, Landau 1905/1908, Phragmen-Lindelof 1908, Euler-Maclaurin, functional equation.

**Techniques.** Phragmen-Lindelof principle; Poisson integral / conformal mapping for harmonic functions in an angle; functional equation with Gamma-factor asymptotics; Euler summation for polynomial growth; convexity of log-growth exponent

## Context and interpretation

**Importance and obstacle overcome.** Source of the Lindelof hypothesis and the clear formulation of the growth exponent mu(sigma) of zeta and its convexity; unified Phragmen-Lindelof argument replacing earlier ad hoc estimates. Obstacle overcome: obtaining growth control inside the critical strip from control on the boundary lines using only convexity, without any estimate of zeta on Re s=1/2.

**Relation to prior work.** Cites Mellin (Acta Soc. Sci. Fenn. 1900), Landau (Bull. SMF 33, 1905; Rend. Palermo 26, 1908), Phragmen-Lindelof memoir (Acta Math. 31, 1908), Riemann 1859, Euler; builds on his own book 'Le calcul des residus' (1905).

**Limitations and open questions.** Only the Phragmen-Lindelof convexity bound is proved, not any improvement (mu(1/2)<=1/4). The Lindelof hypothesis mu(1/2)=0 is posed as a question. Open (still): Lindelof hypothesis; the implication RH => LH is asserted but the details of the second part were not read.

## Research potential

- **Hypotheses that might be weakened.** Mellin's boundary bound |zeta(it)|=O(|t|^{1/2}log|t|) may be replaced by modern subconvexity inputs (Weyl exponent 1/6 at sigma=1/2) in the same Phragmen-Lindelof lemma to get explicit mu(sigma) piecewise-linear bounds; the angular harmonic lemma of Section 6 is a one-line template for Phragmen-Lindelof in sectors of opening<pi.
- **Generalizations.** The same lemma yields convexity bounds for Dirichlet L-functions, Dedekind zeta and general degree-d L-functions (mu(1/2)<=1/4 -> (d)/4 convexity); the lower bound argument of section 4-5 extends to any Dirichlet series with functional equation.
- **Candidate connections.** LH <=> moment conjectures and zero-density estimates N(sigma,T+1)-N(sigma,T)=o(log T); with RH (Koch, CAND-00002) it gives the polylog-size consequences; Littlewood (CAND-00161) used the same Phragmen-Lindelof circle of ideas to bound zeta on the line and under RH.
- **Reusable lemmas.** The Phragmen-Lindelof lemma of section 2 with explicit bound statement; the angular harmonic lemma of section 6.
- **Possible experiments.** Numerically compute mu-function proxies: fit log|zeta(sigma+it)|/log t on t up to 10^6 for sigma in [0,1] and compare against the convexity line (1-sigma)/2 and the Lindelof line 0 for sigma>=1/2 (sanity of the exponent definition used in the paper).
- **Risks / barriers.** Convexity alone cannot give mu(1/2)<1/4; any LH progress needs exponential-sum input (Weyl, van der Corput, Bourgain), not this paper's method.

## Audit notes (Level 1 reader)

Basis: partial OCR text (Bulletin vol. 32, part 1, Melanges, pp. 341-356). Heavy OCR corruption, so precise exponents in the convexity statement (section 3) and the final Lindelof formulation could not be verified from the text; the Part-II statements (pp. 354-356) were not read in full. The paper mentions that the result 'comporte une plus grande precision que ceux obtenus jusqu'a present' (Landau 1908 refinements are cited as footnote). The triage description ('source of the Lindelof hypothesis') is consistent with the statement of the question at the end of Part I, but the printed hypothesis is a question rather than a formal conjecture. The footnote crediting Landau with sharper inequalities for zeta on sigma=1 (Bull. SMF 1905) agrees with standard references. No inconsistency noticed in the inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00149`; harvest queries: msc_11M06.
- Triage decision: include — Lindelof's growth analysis in the critical strip, origin of the Lindelof hypothesis.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
