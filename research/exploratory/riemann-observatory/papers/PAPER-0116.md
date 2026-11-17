# PAPER-0116 — The Riemann-Roch strategy. Complex lift of the scaling site

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2019 / S6 |
| Venue | Chamseddine, Ali (ed.) et al., Advances in noncommutative geometry. Based on the noncommutative geometry conference, Shanghai, China, March 23 -- April 7, 2017. On the occasion of Alain Connes' 70th Birthday. Cham: Springer. 53-125 (2019). |
| Identifiers | zbMATH [1458.11108](https://zbmath.org/?q=an:1458.11108) · DOI [10.1007/978-3-030-29597-4_2](https://doi.org/10.1007/978-3-030-29597-4_2) · arXiv [1805.10501](https://arxiv.org/abs/1805.10501) |
| MSC | 11G99, 11M06, 58B34, 14T25 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1805.10501 |
| Selection | score 4.1139, in-pool citations 3, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can one adapt Weil's proof of RH for curves (Mattuck-Tate/Grothendieck Riemann-Roch strategy) to the square of the Scaling Site, and, as a new step, construct a complex-analytic lift of the Scaling Site / adele class space of Q (parabolic Q-lattices, triangular elliptic curves modulo isogeny) and use a 'tropical descent' (Jensen tropicalization plus Bohr-Jessen-Tornehave) to obtain the existence part of Riemann-Roch in characteristic one from complex geometry? Strategy and geometric construction paper; no proof of RH and no Riemann-Roch theorem on the square is claimed.

**Historical motivation.** Weil's proof of RH for curves via Riemann-Roch on C x C (Mattuck-Tate, Grothendieck), the Connes trace formula/adele class space, the Arithmetic and Scaling Sites, and the earlier tropical Riemann-Roch on periodic orbits [26]; Borchsenius-Jessen results on zeros of zeta(z)-x motivate almost periodic technology.

### Main results

- **THM-PAPER-0116-1** (Eq. (12)-(14), Sect. 3.1, recalled equivalence / heuristic, scope: conditional; Sect. 3.1, eqs (12)-(14)). RH (Bombieri-Lagarias form): $\mathrm{RH}\iff s(f,f)\le 0$ for all real compactly supported $f$ on $\mathbb R_+^*$ with $\int f(u)\,d^*u=\int f(u)\,du=0$, where $s(f,g)=N(f\star\tilde g)$, $\tilde g(u)=u^{-1}g(u^{-1})$, $N(h)=\sum_{n\ge1}\Lambda(n)h(n)+\int_1^\infty\frac{u^2h(u)-h(1)}{u^2-1}d^*u+c\,h(1)$, $c=\tfrac12(\log\pi+\gamma)$. Interpreted (via explicit formulas, ref [22]) as $s(f,f)=D\bullet D$ with $D=\int f(\lambda)\Psi_\lambda d^*\lambda$ on the square of the Scaling Site; the strategy is to assume $s(f,f)>0$, use a (missing) Riemann-Roch to make $D$ or $-D$ effective and contradict degree/codegree zero. *Conditional on:* existence of a Riemann-Roch formula on the square of the Scaling Site (not available), definition of H^1 as idempotent-monoid cohomology (open).
- **THM-PAPER-0116-2** (Theorem 3.1 / Theorem 3.2 (tropicalization), theorem (classical, recast), scope: global; Sect. 3.2.1-3.2.2, Theorems 3.1-3.2, eqs (16)-(17)). For $f$ holomorphic on an annulus $A(r_1,r_2)$, with $\tau(f)(x)=\frac1{2\pi}\int_0^{2\pi}\log|f(e^{-x+i\theta})|d\theta$, the values $-\log|z_i|$ of the zeros are the tropical zeros (with multiplicity) of the convex piecewise affine integral-slope function $\tau(f)$ on $(-\log r_2,-\log r_1)$; $\tau(fg)=\tau(f)+\tau(g)$ and $\tau(f(z^n))(x)=\tau(f)(nx)$ (compatibility with the $\mathbb N^\times$ action). Non-archimedean analogue (Thm 3.1) via Newton polygons.
- **THM-PAPER-0116-3** (Theorem 4.2 (Jessen-Tornehave [36, Thm 25]), imported theorem, scope: global; Sect. 4, Theorem 4.2). A real function $\varphi(\sigma)$ on $\alpha<\sigma<\beta$ is the Jensen function of an almost periodic analytic function on the strip iff $\varphi$ is convex and on each compact $I\subset(\alpha,\beta)$ there is a finite $\mathbb Q$-linearly independent $F\subset\mathbb R$ and $C<\infty$ with slope jumps $\varphi'(\sigma_2)-\varphi'(\sigma_1)=\sum_{\mu\in F}r(\mu)\mu$, $r(\mu)\in\mathbb Q$, $\sum r(\mu)^2\le C|\varphi'(\sigma_2)-\varphi'(\sigma_1)|^2$.
- **THM-PAPER-0116-4** (Theorems 4.3, 4.4 (Jessen-Tornehave [36, Thms 11, 12]), imported theorems, scope: global; Sect. 4, Theorems 4.3-4.4). 4.3: the asymptotic distribution function $\mu(\sigma)$ of a real almost periodic sequence $U(k)$ is constant on an open interval iff $U$ takes no value there, and then that constant is a rational number in $\frac1{2\pi}M_U$. 4.4: for a dense subgroup $M\subset\mathbb R/2\pi\mathbb Z$, a distribution function is the asymptotic distribution of an almost periodic sequence with exponents in $M$ iff it has compact support and its values on constancy intervals lie in $\frac1{2\pi}M$.
- **THM-PAPER-0116-5** (Lemma 4.1 and Corollary 4.1, lemma (native), scope: global; Sect. 4, Lemma 4.1, Cor. 4.1). For a prime $p$ there is a unique sequence $U:\mathbb Z\to\mathbb R$ with $U(\sum a_jp^j)=\sum a_jp^{-j-1}$ (digit reversal), $|U(x+np^m)-U(x)|\le p^{-m}$, almost periodic with modul $2\pi H_p$ and distribution function $\mu(\sigma)=\sigma$ on $[0,1]$. Corollary 4.1: for $h\in C[0,1]$, $h(U(n))$ is almost periodic with $d\mu=h_*(\text{Lebesgue})$; for any strictly increasing continuous $\mu$ on $[\alpha,\beta]$ with $\mu(\alpha)=0,\mu(\beta)=1$, $\mu$ is the distribution function of $h(U)$ with $h=\mu^{-1}$.
- **THM-PAPER-0116-6** (Theorem 5.2, theorem (native), scope: global; Sect. 5, Theorem 5.2). Let $C=\int f(\lambda)\delta_\lambda d\lambda$ be a continuous divisor on $\mathbb R_+^*$ with compact support. Then there exist finitely many graphs $G_j^\pm$ of maps $g_j^\pm:D_j^\pm\to\mathbb R_+^*$, $D_j^\pm\subset\hat{\mathbb Z}\subset G$, such that the leafwise discrete divisor $D=\sum\pm G_j^\pm$ is a lift of $C$ (proof reduces to Lemma 4.2 of the almost-periodic construction).
- **THM-PAPER-0116-7** (Theorem 6.1, theorem (native), scope: global; Sect. 6.3, Theorem 6.1, Prop. 6.2). Two parabolic 2-dim Q-lattices $(\Lambda_j,\phi_j)=(\alpha_j^{-1}\Lambda_0,\alpha_j^{-1}\rho_j)$, $\rho_j\in P(\hat{\mathbb Z})$, $\alpha_j\in P^+(\mathbb R)$, are commensurable iff there is $g\in P^+(\mathbb Q)$ with $\rho_2=g\rho_1$, $\alpha_2=g\alpha_1$; hence the space of parabolic Q-lattices up to commensurability is canonically isomorphic to the quotient $C_{\mathbb Q}^o$ (eq. 65). Together with Prop. 6.2 the map from parabolic Q-lattices to 2-dim Q-lattices up to scale is injective except in degenerate cases.
- **THM-PAPER-0116-8** (Theorem 6.2, Definition 6.3, Props 6.3-6.5, theorem/definition (native), scope: global; Sect. 6.4-6.6, Theorem 6.2, Def. 6.3-6.4). For an elliptic curve $E$ with $(\xi,\eta)\in TE\times TE$ (total Tate module), $\xi\ne0$, the associated Q-lattice lies in the range of $\theta$ iff $\langle\xi^\perp,\eta\rangle=\hat{\mathbb Z}$ where $\langle\xi^\perp,\eta\rangle=\{T(\chi)(\eta):\chi\in\xi^\perp\}$. A triangular structure is such a pair; points of $C_{\mathbb Q}$ correspond to triangular elliptic curves modulo the equivalence generated by isogenies (Def. 6.4, Prop. 6.3), and the complex structure of the moduli of triangular curves agrees with that on $C_{\mathbb Q}$ from the right action of $P(\mathbb R)$ (Sect. 6.6).
- **THM-PAPER-0116-9** (Proposition 7.1, proposition (native), scope: global; Sect. 7.1, Prop. 7.1, eqs (93)-(95)). With $W$ the Witt-type ring of characteristic-one lift, characters $\chi_\lambda:W\to\mathbb C$ ($\chi_\lambda([x])=x^\lambda$), holomorphy of $W$-valued $f$ on a $P^+(\mathbb R)$-orbit defined by $(\lambda X+iY)\chi_\lambda(f)=0\ \forall\lambda$, the Frobenius correspondences $\mathrm{Fra}_\mu(f):=\theta_\mu(R(\mu^{-1})(f))$ preserve this holomorphy condition (uses $[Y,X]=X$).

### Key definitions

- Tropicalization $\tau(f)(x)=\frac1{2\pi}\int\log|f(e^{-x+i\theta})|d\theta$ (Def 3.2)
- Parabolic 2-dimensional Q-lattice (Def 6.1) and commensurability (Def 6.2)
- Triangular structure on an elliptic curve: $(\xi,\eta)\in TE^2$, $\xi\ne0$, $\langle\xi^\perp,\eta\rangle=\hat{\mathbb Z}$ (Def 6.3)
- Isogeny of triangular elliptic curves (Def 6.4); degenerate triangular structure (Def 6.5)
- Scaling Site $[0,\infty)\rtimes\mathbb N^\times$

### Principal lemmas

- **THM-PAPER-0116-L1** (Lemma 2.1-2.3 and Theorem 2.1 / 2.2; Sect. 2.2-2.3). Topological lemmas on $\mathbb Z(+\infty)$ and an action of $\mathbb Q_+^*$ on a locally compact metrizable space; Thm 2.2: the space of points of the topos $[0,\infty)\rtimes\mathbb N^\times$ is canonically isomorphic to the (sector of the) adele class space of Q (recalled from [25]). — *Role:* Identifies the Scaling Site's points with the adele class space; the starting geometry for the lift.
- **THM-PAPER-0116-L2** (Lemma 5.1; Sect. 5.1). $u(q)=-\log|q|$ on $D^*$ extends to a geometric morphism $D^*\rtimes\mathbb N^\times\to[0,\infty)\rtimes\mathbb N^\times$ of toposes. — *Role:* Gives the first complex lift (ringed topos with sheaf of analytic functions).
- **THM-PAPER-0116-L3** (Proposition 5.4; Sect. 5, Prop. 5.4). The classical orbit $\Gamma_{\mathbb Q,cl}\simeq G\times\mathbb R_+^*=\varprojlim H/n\mathbb Z$ is canonically isomorphic to the pro-etale cover $\tilde D^*=\varprojlim(E_n,p_{n,m})$ of the punctured disk, $E_n=D^*$, $p_{n,m}(z)=z^a$ for $m=na$. — *Role:* Links adelic leaf to analytic pro-etale cover of the punctured disk.
- **THM-PAPER-0116-L4** (Lemma 5.2 and de Rham computation (v); Sect. 5, proof of Lemma 5.2(v)). On $G=\mathbb A_{\mathbb Q}/(\mathbb Q,+)$ with foliation flow W, $d_W(e_q)=2\pi i q\,e_q$; kernel is 1-dim, cokernel given by Haar measure, so foliated de Rham cohomology is 1-dim in degrees 0 and 1 and zero above. — *Role:* Computes cohomology of the leafwise structure (a substitute H^1 input).
- **THM-PAPER-0116-L5** (Lemma 6.3-6.5; Sect. 6.3-6.4). Q-lattice parametrization via $(\Lambda,\phi)$, parabolic specialization and a description of $\xi^\perp=\mathbb Z\chi$ for primitive character $\chi$ of $E$ when $\xi\neq0$ (Lemma 6.5). — *Role:* Used in the proof of Theorem 6.2 (triangular structure criterion).

### Proof architecture

Not a single-theorem paper. (i) Sect. 1-2: motivation; RH reformulated through E(f)(v)=sum f(nv) and the two geometric models (adele class space via Q_+^*, Scaling Site topos [0,inf) x| N^x). (ii) Sect. 3: the Riemann-Roch strategy: RH iff s(f,f)<=0, s(f,f)=D.D on the square of the Scaling Site; the missing existence part of Riemann-Roch (sheaf H^1 in char. 1 fails due to null elements, Example 6.5 of [50]) is to be obtained by tropical descent from analytic geometry via tropicalization tau (Jensen formula, Thm 3.2). (iii) Sect. 4: Bohr-Jessen-Tornehave theory (Thm 4.2-4.4, imported) plus a new explicit almost periodic sequence U (Lemma 4.1) to realize arbitrary convex Jensen functions / distribution functions. (iv) Sect. 5: complex lift as foliated pro-etale D~* and lift of continuous divisors by leafwise discrete divisors (Thm 5.2). (v) Sect. 6: arithmetic of the lift: parabolic Q-lattices up to commensurability = C_Q (Thm 6.1), geometric meaning via triangular elliptic curves modulo isogeny (Thm 6.2, Def 6.3-6.4), degenerate cases (Sect. 6.8). (vi) Sect. 7: Frobenius correspondences lost by passing to char. 0 are restored by Witt construction in char. 1 (Prop. 7.1). Imported: Jensen formula, Jessen-Tornehave almost-periodic results, Borchsenius-Jessen, Bombieri-Lagarias criterion, Connes-Marcolli Q-lattice dictionary.

Dependency edges: CAND-02083 → Connes trace formula (Selecta 1999) (builds_on); CAND-02083 → Connes-Consani Scaling Site [25,26] (builds_on); CAND-02083 → Jessen-Tornehave almost periodic theory (imports); CAND-02083 → Bombieri-Lagarias criterion (imports)

**Imported results.** Jensen formula (Rudin RCA Thm 15.15); Jessen-Tornehave almost periodic theorems [36, Thm 11, 12, 25]; Bombieri-Lagarias positivity criterion for RH [9]; Borchsenius-Jessen [10] on zeros of zeta(z)-x; Connes-Marcolli Prop 3.38 (Q-lattices vs elliptic curves with Tate module data); Baker-Norine / Gathmann-Kerber tropical Riemann-Roch [2,29]

**Techniques.** tropicalization (Jensen formula, Newton polygons); almost periodic functions (Bohr, Jessen, Tornehave); Q-lattices and GL(2)-system; moduli of elliptic curves with Tate-module data; topos theory (Scaling Site, pro-etale covers); Witt construction in characteristic one; foliated de Rham cohomology

## Context and interpretation

**Importance and obstacle overcome.** Provides the first complex-analytic (characteristic 0) model whose tropicalization recovers the Scaling Site, and a moduli interpretation (triangular elliptic curves modulo isogeny) that opens modular-form technology. Obstacle addressed: realizing arbitrary convex distribution functions as tropicalizations (Jessen-Tornehave) and recovering the Frobenius lost when lifting from char. 1 to char. 0 (Witt construction). The central obstacle (Riemann-Roch on the square, in particular H^1) is not overcome.

**Relation to prior work.** Builds on Connes 1999 trace formula, Connes-Consani Arithmetic Site/Scaling Site papers [23-26], their homological algebra in char. 1 [27], and Witt construction [18-20]. Replaces attempted direct definition of H^1 by an existence-oriented descent from complex geometry. Cites Bombieri-Lagarias [9] for the RH criterion.

**Limitations and open questions.** The authors state that the key problem remains open: a definition of sheaf cohomology H^1 (as idempotent monoid) on the square of the Scaling Site; the Riemann-Roch formula with topological side (1/2) D.D is not proved, so the strategy does not currently yield RH. The paper only constructs the complex lift at the adelic level and its moduli interpretation; passing from existence results via tropical descent to the actual Riemann-Roch inequality needed for D or -D effective is not carried out.

**Ideas in remarks/appendices/abandoned paths.** Remark in intro on Borchsenius-Jessen: zeros of zeta(z)-x accumulate at Re z=1/2 with density going to infinity, suggesting almost periodic densities phi''(alpha) as a replacement of the zero-cycle (Sect. 1); Sect. 7.2 links the complex lift to quantization (not read in detail).

## Research potential

- **Hypotheses that might be weakened.** Thm 4.4 needs M dense (torsion-free M gives connected dual so no gaps); the almost periodic exponent-module restriction on slopes in Thm 4.2 is what limits which divisors lift; relaxing from compactly supported continuous divisors in Thm 5.2 to the distributions N(u) actually appearing in s(f,f) is the unaddressed step.
- **Generalizations.** Thm 6.1/6.2 for GL(2)-system suggest extension to other levels and number fields; Lemma 4.1 digit-reversal sequence extends to any base/profinite digit expansions; tropical descent could be tested on finite graph Riemann-Roch (Baker-Norine) where existence of r(D) is known.
- **Candidate connections.** Link H^1 problem to cohomology of the foliated pro-etale cover (Lemma 5.2(v) gives 1-dim H^0, H^1); link to the later Weil-positivity/Sonin-space operator program of CAND-01965 (the same quadratic form s(f,f)); modular-form function theory on the moduli of triangular curves.
- **Reusable lemmas.** Lemma 4.1 / Cor 4.1 (explicit almost periodic sequence with prescribed distribution, usable in equidistribution-type constructions); Thm 3.2 + eq (17) tropicalization compatible with f(z)->f(z^n); Prop 7.1.
- **Possible experiments.** Numerically tropicalize truncations of zeta-type Dirichlet polynomials sum_{n<=N} n^{-z} via Jensen function and compare with the predicted convex phi from Thm 4.2; compute isogeny classes of triangular curves with small level and test injectivity of Thm 6.1 numerically; check s(f,f)=N(f*f~) sign on explicit test f to see what effectivity statement would be required.
- **Risks / barriers.** H^1 on the square of the Scaling Site is unsolved; existence of effective representative of D (Riemann-Roch inequality) is essentially RH-strength; no positivity input is produced by the lift itself; Witt-lift holomorphy (Prop 7.1) does not by itself give intersection theory.

## Audit notes (Level 1 reader)

none noticed in inspected portion (the claims are explicitly labelled as strategy; proofs of Sect. 5-7 only skimmed, not verified).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02083`; harvest queries: kw_RH_any, kw_zeta_zeros, msc_11M06.
- Triage decision: include — Connes-Consani Riemann-Roch strategy for RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
