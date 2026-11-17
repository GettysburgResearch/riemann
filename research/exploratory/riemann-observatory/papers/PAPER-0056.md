# PAPER-0056 — The Weyl bound for Dirichlet \(L\)-functions of cube-free conductor

| Field | Value |
|---|---|
| Authors | Petrow, Ian; Young, Matthew |
| Year / stratum | 2020 / S6 |
| Venue | Ann. Math. (2) 192, No. 2, 437-486 (2020). |
| Identifiers | zbMATH [1460.11111](https://zbmath.org/?q=an:1460.11111) · DOI [10.4007/annals.2020.192.2.3](https://doi.org/10.4007/annals.2020.192.2.3) · arXiv [1811.02452](https://arxiv.org/abs/1811.02452) |
| MSC | 11M06, 11F66, 11F72 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1811.02452 |
| Selection | score 4.5533, in-pool citations 13, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove a Weyl-exponent subconvex bound |L(1/2+it,chi)| << q^{1/6+eps}(1+|t|)^{1/6+eps} for Dirichlet L-functions of cube-free conductor, extending the Conrey-Iwaniec cubic-moment method (quadratic characters of odd squarefree conductor) to arbitrary non-quadratic characters, and in particular improving Burgess 3/16 for all prime conductors.

**Historical motivation.** Weyl 1916 exponent 1/6 for zeta; Burgess 1963 gave 3/16 for Dirichlet L-functions; Conrey-Iwaniec 2000 achieved 1/6 for quadratic characters of odd squarefree conductor via cubic moment; Milicevic did sub-Weyl for prime power moduli with large exponent. The gap was all non-quadratic characters of prime conductor.

### Main results

- **THM-PAPER-0056-1** (Theorem 1.1, theorem, scope: asymptotic; Sec 1.1, eq (1.3)). Let q be cube-free, chi primitive mod q and not quadratic. Then for some B>2, $\sum_{m|q}\sum_{|t_j|\le T}\sum_{f\in H_{it_j}(m,\chi^2)}L(1/2,f\otimes\chi)+\int_{-T}^{T}|L(1/2+it,\chi)|^6\,dt\ll_\varepsilon T^{B}q^{1+\varepsilon}$.
- **THM-PAPER-0056-2** (Theorem 1.2, theorem, scope: asymptotic; Sec 1.1, eq (1.4)). Same hypotheses, and T >> q^delta for some delta>0: $\sum_{m|q}\sum_{T\le t_j<T+1}\sum_f L(1/2,f\otimes\chi)+\int_T^{T+1}|L(1/2+it,\chi)|^6dt\ll_{\varepsilon,\delta}T^{1+\varepsilon}q^{1+\varepsilon}$.
- **THM-PAPER-0056-3** (Corollary 1.3, corollary, scope: asymptotic; eq (1.5)). If chi has cube-free conductor q (any primitive chi, quadratic case from Conrey-Iwaniec/earlier work): $|L(1/2+it,\chi)|\ll_\varepsilon q^{1/6+\varepsilon}(1+|t|)^{1/6+\varepsilon}$.
- **THM-PAPER-0056-4** (Corollary 1.4, corollary, scope: asymptotic; eq (1.6)). p odd prime, F Hecke-Maass newform of level p^2, trivial central character, not twist-minimal (F=f otimes chi): $L(1/2,F)\ll_\varepsilon (p(1+|t_F|))^{1/3+\varepsilon}$.
- **THM-PAPER-0056-5** (Theorem 1.5, theorem, scope: asymptotic; eq (1.7)-(1.8)). Holomorphic analogue, q cube-free: $\sum_{m|q}\sum_{\kappa\le T}\sum_{f\in H_\kappa(m,\chi^2)}L(1/2,f\otimes\chi)^3\ll_\varepsilon T^{B}q^{1+\varepsilon}$ for some B>2, and << T^{1+eps}q^{1+eps} for the unit-window sum if T>>q^delta.
- **THM-PAPER-0056-6** (Theorem 6.9, theorem, scope: asymptotic; Sec 6.4; proved in Sec 9 (9.1 prime via Deligne/Katz trace functions; 9.2 q=p^2 elementary)). For $g(\chi,\psi)=\sum_{t,u\bmod q}\chi(t)\chi(t+1)\chi(u)\chi(u+1)\psi(ut-1)$ with chi primitive mod q and q=p or q=p^2: $|g(\chi,\psi)|\ll q$.
- **THM-PAPER-0056-7** (Theorem 4.1, theorem, scope: asymptotic; Sec 4). Cubic moment M(q,chi) (even-parity spectral sum of L(1/2,f otimes chi)^3 plus Eisenstein contribution) << T^B q^eps for cube-free non-quadratic chi; implies Thm 1.1 via nonnegativity L(1/2,f otimes chi)>=0 (Waldspurger/Guo) and L(1/2,E otimes chi)=|L(1/2+it,chi)|^2 * (analogous), after normalization by Petersson norms.

### Principal lemmas

- **THM-PAPER-0056-L1** (Proposition 4.3; Sec 4). If the dual sums S_{N1,N2,N3,C}^{\pm} << T^B q^eps for N1<<(qT)^{1+eps}, N2N3<<d^{-2}(qT)^{2+eps}, q<<C<<(qT)^{100}, then Theorem 4.1 holds. — *Role:* Reduction of cubic moment, after approximate functional equation, Kuznetsov/Petersson and Poisson summation, to a bound for dual Kloosterman-type sums.
- **THM-PAPER-0056-L2** (Lemma 8.1; Sec 8). For q cube-free, Z=Z_0+Z_1 with Z_0 meromorphic/analytic as stated with Z_0<<q^eps for Re s_j>1, and $\int_{-T}^{T}|Z_1(\sigma+it,\sigma+it,\sigma+it,\sigma-it)|dt\ll q^{3/2+\varepsilon}T^{1+\varepsilon}$ for T>>1 (Z_1 analytic for Re s_j>=1/2). — *Role:* Analytic continuation/fourth-moment type Dirichlet series control; remarked essentially equivalent to [PY1, Prop 3] (fourth moment of Dirichlet L-functions, q^{1+eps}).
- **THM-PAPER-0056-L3** (Lemma 9.1 / Lemma 9.2; Sec 9.1). For nontrivial chi, psi mod p, the trace function of the sheaf G is the cohomological (Katz affine) transform of F_1 with kernel K: t_G(x)=-sum_y t_{F1}(y)t_K(x,y); the sheaf G_e is geometrically irreducible/Fourier-type enough to give square-root cancellation. — *Role:* Proof of |g(chi,psi)|<<q for q=p via Deligne's Riemann Hypothesis (Katz, Fouvry-Kowalski-Michel trace function formalism).
- **THM-PAPER-0056-L4** (Lemma 6.4/6.5/6.7/6.8, Conjectures 6.6 and 8.2; Sec 6-8, Remark in Sec 1.2). Evaluation of Gauss/Ramanujan-type sums H(psi^,chi,m1,m2,m3,r) for prime powers; vanishing unless psi trivial when some m_j=0; Conjecture 6.6 proved here only for k=2,j=1 (q=p^2). — *Role:* Local arithmetic of the dual sum; the unproved Conjectures 6.6 and 8.2 for q=p^k, k>=3 were later proved in Petrow-Young [PY2] (remark of 28 Aug 2019).
- **THM-PAPER-0056-L5** (Lemmas 10.1-10.5, 11.1-11.3; Sec 10-11). Archimedean analysis: bounds for weight functions V_j and Bessel-transform kernels J^{\pm}(x,.), oscillatory and non-oscillatory cases of the integral transform in the dual sum. — *Role:* Make the Poisson/Kuznetsov dual sums tractable with polynomial dependence T^B on spectral parameter.

### Proof architecture

Cubic moment of GL2 twists: since f tensor chi is self-dual of level q^2 with nonnegative central value (Waldspurger/Guo), sum over Hecke-Maass newforms of level m|q, central character chi^2, of L(1/2,f x chi)^3 dominates the sixth moment of L(1/2,chi) through Eisenstein series. Steps: (i) approximate functional equation for L(1/2,f x chi)^3 (smooth weights G_1=e^{2s^2}, G_2=e^{4s^2}); (ii) Kuznetsov/Petersson formula with twisted Kloosterman sums S_chi(m,n;c) and Atkin-Lehner-Li newform decomposition; (iii) Poisson summation in the three variables; (iv) dual sum reduces to character sum g(chi,psi) times 4th moment sum_psi |L(1/2,psi)|^4 g(chi,psi); (v) |g|<<q (Deligne via Katz trace functions for q=p; elementary for q=p^2; multiplicativity for squarefree/cube-free), giving q^{1+eps} with T^B; (vi) hybrid T-aspect by Young's earlier archimedean analysis; (vii) positivity gives Thm 1.1, which implies 1/6 bound via the integral of |L|^6 over unit window (convexity-free: sixth moment << q^{1+eps} gives |L|^6 << q^{1+eps} by Gallagher/Sobolev-type argument). Imported results: Deligne RH for varieties, Katz/FKM trace function bounds, Waldspurger/Guo nonnegativity, fourth-moment bound for Dirichlet L-functions (Heath-Brown), Iwaniec/Hoffstein-Lockhart Petersson norm bounds.

Dependency edges: CAND-01822 → Conrey-Iwaniec 2000 (cubic moment, quadratic characters) (generalizes); CAND-01822 → Burgess 1963 (improves); CAND-01822 → Petrow-Young [PY2] (arbitrary conductor) (extended_by)

**Imported results.** Deligne, Weil II (Riemann hypothesis over finite fields), via Katz/Fouvry-Kowalski-Michel trace function bounds; Waldspurger/Guo: L(1/2,f x chi)>=0 for self-dual twists; Heath-Brown/Young: fourth moment of Dirichlet L-functions << q^{1+eps}; Iwaniec, Hoffstein-Lockhart: bounds for Petersson norms; Young [Y1] archimedean analysis for the hybrid T-aspect

**Techniques.** cubic moment of GL2 twists; Kuznetsov/Petersson formula with twisted Kloosterman sums; approximate functional equation; Poisson summation; Deligne Weil conjectures and l-adic trace functions (Katz, FKM); elementary Gauss-sum evaluation for p^2; positivity of central values (Waldspurger/Guo); Atkin-Lehner-Li theory; fourth moment of Dirichlet L-functions

## Context and interpretation

**Importance and obstacle overcome.** First improvement over Burgess for all prime-conductor Dirichlet L-functions, reaching the Weyl-exponent barrier (q-aspect analogue of 1/6). Obstacle: Conrey-Iwaniec used positivity/quadratic structure; for non-quadratic chi one needs the cubic moment over twists f x chi with central character chi^2, and a uniform bound |g(chi,psi)|<<q on the resulting character sum, obtained through Deligne's RH on sheaves (q=p) and elementary arguments (q=p^2). Fails to extend naively to p^3, where |g|>>q p^{1/2} for many psi (eq 1.11).

**Relation to prior work.** 

**Limitations and open questions.** Restricted to cube-free q; for q=p^3 the character sum g has bad psi of size q p^{1/2}, which would give only q^{7/36}>3/16; later removed in Petrow-Young [PY2] for arbitrary q (Conjectures 6.6/8.2 of this paper). The bound is only Weyl, not sub-Weyl, and the T-aspect in Thm 1.1 is weak (T^B, B>2 unspecified) though sharp for T<<q^eps. Does not address GRH/Lindelof (exponent 1/6 vs 0).

## Research potential

- **Hypotheses that might be weakened.** Cube-free condition (already removed in PY2 via Conjectures 6.6, 8.2); non-quadratic restriction (quadratic case in Conrey-Iwaniec / separate); value of B>2 in the T-aspect could be made explicit.
- **Generalizations.** Other GL2/GL1 families with self-dual twists and nonnegativity (Petrow-Young: Weyl bound for GL2 twists, Hecke characters over number fields); function field analogues where Deligne is the only ingredient; sub-Weyl via moments beyond the cubic one.
- **Candidate connections.** Zero-density near the critical line for Dirichlet L-functions (Weyl bound feeds log-free zero-density in q aspect); Lindelof-on-average consequences; explicit versions feed explicit zero-free regions for Dirichlet L-functions (see Simonic/Johnston-Yang style explicit programmes) but constants here are ineffective-free? (not tracked).
- **Reusable lemmas.** Theorem 6.9 (|g(chi,psi)|<<q for q=p,p^2) and the trace-function Lemmas 9.1-9.2 give a template for Kloosterman-type sums with square-root cancellation; Proposition 4.3 reduction is reusable for any twisted cubic moment.
- **Possible experiments.** Numerically compute g(chi,psi) mod p^3 for primitive psi to locate the 'bad' psi with |g|~q p^{1/2} (eq 1.11) and test the conjectural structure behind Conjecture 6.6; compute cubic moment sum numerically for small primes p to check size q^{1+eps}.
- **Risks / barriers.** Weyl exponent 1/6 is a natural barrier for the cubic-moment method; sub-Weyl requires new input (Milicevic uses p-adic stationary phase in depth aspect only). No implication for RH itself.

## Audit notes (Level 1 reader)

Introduction states the cubic moment bound with T^B for unspecified B>2; Cor 1.3 for all |t| relies on Thm 1.2 (hybrid) sketched in Sec 13, not fully proved here (relies on Young [Y1]). In (1.10) Remark: 'the fourth moment is O(q^{1+eps})' is cited, not proved. Sections 5-13 not read in detail. Nothing else noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01822`; harvest queries: kw_RH_any, msc_11M06.
- Triage decision: include — Weyl-strength subconvexity for Dirichlet L-functions in general conductor.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
