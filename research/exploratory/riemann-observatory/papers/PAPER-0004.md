# PAPER-0004 — A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Báez-Duarte, Luis |
| Year / stratum | 2003 / S5 |
| Venue | Atti Accad. Naz. Lincei, Cl. Sci. Fis. Mat. Nat., IX. Ser., Rend. Lincei, Mat. Appl. 14, No. 1, 5-11 (2003). |
| Identifiers | zbMATH [1097.11041](https://zbmath.org/?q=an:1097.11041) · arXiv [math/0202141](https://arxiv.org/abs/math/0202141) |
| MSC | 11M26 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:math/0202141v2 |
| Selection | score 4.8658, in-pool citations 32, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that RH is equivalent to the stronger Nyman-Beurling-type statement that \chi lies in the closed span B_nat of the integer dilates \rho_a, a\in\mathbb N, rather than all real a\ge1.

**Historical motivation.** Conjectured by several authors (Báez-Duarte, Vasyunin, Nikolski, Lee, van Frankenhuysen, etc.) that integer dilates suffice; the approximants F_n=sum mu(a) rho_a were known to be natural but divergent.

### Main results

- **THM-PAPER-0004-1** (Theorem 1.1, theorem, scope: global; Sec. 1, Thm 1.1; proof Sec. 2.2). In H=L^2(0,\infty), with \rho(x)=x-[x], \rho_a(x)=\rho(1/(ax)), \chi=1_{(0,1]}, B^{nat}=\overline{\mathrm{span}}\{\rho_a: a\in\mathbb N\}: RH \iff \chi\in B^{nat}.
- **THM-PAPER-0004-2** (Corollary 3.1, corollary, scope: global; Sec. 3). RH is equivalent to H-convergence of f_{\epsilon,n}=\sum_{a\le n}\mu(a)a^{-\epsilon}\rho_a as n\to\infty for all sufficiently small \epsilon>0.
- **THM-PAPER-0004-3** (Intermediate claim in Sec. 2.2, theorem (unconditional), scope: asymptotic; Sec. 2.2, eqs (2.4)-(2.9)). Unconditionally, for the pointwise (a.e.) limit f_\epsilon(x)=\frac{1}{x\zeta(1+\epsilon)}-\sum_{a\le1/x}\mu(a)a^{-\epsilon}\{1/(ax)\}... one has f_\epsilon\to-\chi in H as \epsilon\downarrow0, via Mellin transform M(X_\epsilon f_{2\epsilon})(\tau)=-\frac{\zeta(1/2-\epsilon+i\tau)}{\zeta(1/2+\epsilon+i\tau)}\frac{1}{1/2-\epsilon+i\tau} and Lemma 2.2; under RH f_\epsilon\in B^{nat}.

### Key definitions

- \rho(x)=x-[x]; \rho_a(x)=\rho(1/(ax))
- H=L^2(0,\infty); B closed span of \rho_a, a real >=1; B^nat span over a integer
- f_s(x)=\sum\mu(a)a^{-s}\rho_a(x)
- M(f)(\tau)=\int_0^\infty x^{-1/2+i\tau}f(x)dx, isometry H->K

### Principal lemmas

- **THM-PAPER-0004-L1** (Lemma 2.1 (Balazard-Saias, Lemme 2); Sec. 2.1). Let 1/2\le\alpha<1, \delta>0, \epsilon>0. If \zeta has no zeros in \Re s>\alpha, then for n\ge2 and \alpha+\delta\le\Re s\le1: \sum_{a\le n}\mu(a)a^{-s}=1/\zeta(s)+O_{\alpha,\delta,\epsilon}(n^{-\delta/3}(1+|\tau|)^{\epsilon}). — *Role:* quantitative Littlewood: uniform-in-tau convergence of Mobius partial sums under RH (imported)
- **THM-PAPER-0004-L2** (Lemma 2.2; Sec. 2.1). For 0\le\epsilon\le\epsilon_0<1/4 there is C(\epsilon_0) with |\zeta(1/2-\epsilon+i\tau)/\zeta(1/2+\epsilon+i\tau)|\le C(1+|\tau|)^{\epsilon}, for all real \tau; unconditional, by functional equation and Gamma asymptotics. — *Role:* gives K-domination of the Mellin transform uniformly in epsilon; makes epsilon->0 limit unconditional

### Proof architecture

Only 'if RH then chi in B^nat' needs proof (converse is trivial since B^nat subset B plus Nyman-Beurling). Assume RH. (1) f_{eps,n}=sum mu(a)a^{-eps}rho_a; Mellin-Plancherel isometry M:H->K=L^2(R,(2pi)^{-1/2}dt) with Titchmarsh identity -zeta(s)/s=int x^{s-1}rho_1. (2) M(X_eps f_{2eps,n}) is a Dirichlet partial sum times zeta(1/2-eps+itau)/(1/2-eps+itau). By Lemma 2.1 (alpha=1/2, delta=eps) plus Lemma 2.2 and Lindelof (a consequence of RH) at abscissa 1/2-eps, it is dominated by K_eps(1+|tau|)^{-1+2eps}, an L^2 function for eps<1/4, giving f_{eps,n}->f_eps in H, so f_eps in B^nat. (3) Mellin transform of f_eps is explicit; Lemma 2.2 gives uniform L^2 control, so f_eps converges in H as eps->0, and the pointwise limit -chi identifies it. Hence chi in B^nat.

Dependency edges: CAND-01182 → CAND-00760 (uses (modified NB criterion, lower bound (1.2), Selberg approximation)); CAND-01182 → Balazard-Saias 1998 Lemme 2 (imports)

**Imported results.** Nyman-Beurling criterion in L^2(0,infty) form (Nyman 1950, Beurling 1955; modified form in Báez-Duarte-Balazard-Landreau-Saias, Adv. Math. 149 (2000)); Littlewood: under RH sum mu(a)a^{-s} converges to 1/zeta(s) for Re s>1/2 (Titchmarsh Thm 14.25(A)); Balazard-Saias Lemma 2.1 (Notes 1, Adv. Math. 139 (1998), Lemme 2); Titchmarsh (2.1.5): -zeta(s)/s=\int_0^\infty x^{s-1}\rho_1(x)dx, 0<Re s<1; Lindelof hypothesis follows from RH; Gamma asymptotics (Rademacher (21.51),(21.52))

**Techniques.** Mellin/Plancherel isometry; summability (Dirichlet-series damping a^{-eps}) of the natural Mobius approximation; Balazard-Saias quantitative Littlewood lemma; functional equation and Gamma-function asymptotics; Lindelof as consequence of RH

## Context and interpretation

**Importance and obstacle overcome.** Shrinks the approximating family from a continuum to integers (a countable, arithmetic family), making numerics (Landreau-Richard) and the Báez-Duarte distance sequence d_N meaningful. Obstacle: raw Mobius approximants F_n diverge in L^2; overcome by Abel-type regularization a^{-eps} and an eps->0 limit.

**Relation to prior work.** Strengthens Nyman-Beurling (B -> B^nat); contrasts with Báez-Duarte 1993 (convergence a.e./L^1 on (0,1)) and with Conrey-Myerson mollification attempts; supersedes unproved conjecture of the earlier IJMMS preprint approach.

**Limitations and open questions.** Author notes the proof gives a new proof of Nyman-Beurling bypassing Hardy-space methods, suggests extension to L^p (zero-free half-plane Re s>1/p), and suggests studying other summability methods and subsequences. The n-dependence in Lemma 2.1 is unused and seems tied to slowness of approximation (1.2) \|F-\chi\|\ge C/\sqrt{\log N}. F_n=\sum_{a\le n}\mu(a)\rho_a diverges in H (refs [2],[3]) so summation is essential.

## Research potential

- **Hypotheses that might be weakened.** RH used only through Lemma 2.1 (zero-free half-plane Re s>1/2 with polynomial-in-tau control) and Lindelof at 1/2-eps; replacing 1/2 by alpha could give an L^p / zero-free half-plane version (author's remark, p=1/alpha-type).
- **Generalizations.** L^p Nyman-Beurling (Re s>1/p); Dirichlet L-functions or Selberg class with mu replaced by Dirichlet-inverse coefficients; other summability kernels (Riesz means vs a^{-eps}).
- **Candidate connections.** Báez-Duarte's later d_N^2 -> 0 criterion (arithmetic version, arXiv 2001 IJMMS); Burnol's lower bound; Landreau-Richard numerics; Vasyunin biorthogonal system; Bagchi Hardy-space proof.
- **Reusable lemmas.** Lemma 2.2 (unconditional ratio bound), and formula (2.7) Mellin transform of eps-damped Mobius partial sums.
- **Possible experiments.** Compute \|f_{eps,n}+\chi\|_H via the Mellin side for varying eps,n with certified quadrature of the explicit tau-integral, to see the n- and eps-rates; test Lemma 2.2 constant numerically.
- **Risks / barriers.** Finite computations of distance to chi cannot decide RH; the 1/sqrt(log N) barrier means approximations converge extremely slowly.

## Audit notes (Level 1 reader)

Typos in inspected text: Sec. 2.2 defines K:=L^2((\infty,\infty),...) where (-\infty,\infty) intended; proof of Lemma 2.2 displays a ratio of Gamma(1/4+eps/2+i tau/2) over the identical expression (should be Gamma(1/4-eps/2 +... ) type numerator/denominator pair with pi^{-eps}); Lemma 2.1 uses 'Littlewood' for convergence only for Re s>1/2. Statement (2.9) uses f_{2eps,n}(x)<<1/x for x>1 and factor X_eps>1 on (0,1) to pass between X_eps f and f; not detailed. Reference [3] listed as 'submitted' (later published as IJMMS 2003). The converse direction (chi in B^nat implies RH) is treated as 'clear' via B^nat subset B and the Nyman-Beurling criterion [4], not re-proved.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01182`; harvest queries: kw_RH_any, kw_nyman, msc_11M26, arxiv_nyman_beurling, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Strengthened Nyman-Beurling criterion with natural integer dilations.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
