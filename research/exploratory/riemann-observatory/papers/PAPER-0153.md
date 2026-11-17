# PAPER-0153 — Some properties of the Eigenfunctions of the Laplace-operator on Riemannian manifolds

| Field | Value |
|---|---|
| Authors | Minakshisundaram, S.; Pleijel, Åke |
| Year / stratum | 1949 / S2 |
| Venue | Can. J. Math. 1, 242-256 (1949). |
| Identifiers | zbMATH [0041.42701](https://zbmath.org/?q=an:0041.42701) · DOI [10.4153/CJM-1949-021-5](https://doi.org/10.4153/CJM-1949-021-5) |
| MSC |  |
| Families | D |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://doi.org/10.4153/CJM-1949-021-5 |
| Selection | score 2.0381, in-pool citations 17, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** For a compact Riemannian manifold V (with or without boundary, Dirichlet or Neumann conditions), what is the analytic continuation in s of the Dirichlet series $\sum \phi_m(P)\phi_m(Q)\lambda_m^{-s}$, $\sum\phi_m(P)^2\lambda_m^{-s}$ and (closed case) $\sum\lambda_m^{-s}$, where do they have poles, what are the residues and values at non-positive integers, and what asymptotics for eigenfunction sums and eigenvalue counting follow?

**Historical motivation.** Carleman (1934/36) studied $\sum\phi_m(P)\phi_m(Q)\lambda_m^{-s}$ for Euclidean domains in dimension 2 to get asymptotics of eigenfunctions; Minakshisundaram extended to higher-dimensional Euclidean domains and the sphere ('zeta functions on the sphere'); this paper generalizes to Riemannian manifolds, producing the spectral zeta function of the Laplacian.

### Main results

- **THM-PAPER-0153-1** (Theorem (section 5, p.252), theorem, scope: global; section 5, pp.251-253 (formulas (31)-(35) and the Theorem)). Assume $V$ is a sufficiently regular (e.g. analytic) $N$-dimensional manifold, $\lambda_0>0$, $P$ interior. The Dirichlet series $f(s,P)=\sum_{m}\phi_m(P)^2\lambda_m^{-s}$ continues to the left of its abscissa of absolute convergence. With the heat-parametrix coefficients $U_\nu(P,P)$ one has, for $N$ odd, $f(s,P)=\frac{1}{(2\sqrt\pi)^N}\sum_{\nu=0}^{n}\frac{U_\nu(P,P)}{\Gamma(s)(s-\frac N2+\nu)}+R_n(s,P)$, and for $N$ even the analogous formula with a pole structure at $s=\frac N2-\nu$ ($\nu$ up to $N/2-1$) (formulas partly garbled in the text extraction); $R_n(s,P)$ is regular for $\Re s>\frac N2-n-2$. Consequently, $f(s,P)$ has simple poles at $s=\frac N2-\nu$, $\nu=0,1,2,\dots$, for N odd and at $s=\frac N2,\frac N2-1,\dots,1$ for N even; for non-positive integers $s$ in the range, $f(s,P)=0$ if $N$ odd and $f(s,P)$ is an explicit multiple of $U_{N/2-s}(P,P)$ if $N$ even. If $\lambda_0=0$ the same holds for $\sum_{m\ge1}$ with $f(0,P)=-1/V$ ($N$ odd), resp. $\frac{U_{N/2}(P,P)}{(2\sqrt\pi)^N}-\frac1V$ ($N$ even), $V$ the volume.
- **THM-PAPER-0153-2** (Corollary (section 5, p.253), corollary (Tauberian), scope: asymptotic; p.253). By Ikehara's theorem, $\sum_{\lambda_m\le T}\phi_m(P)^2\sim\dfrac{T^{N/2}}{(2\sqrt\pi)^N\,\Gamma(\frac N2+1)}$ as $T\to\infty$ (the quotient tends to 1), where the right side is $\frac{T^{N/2}}{(4\pi)^{N/2}\Gamma(N/2+1)}$ (Carleman's local Weyl law).
- **THM-PAPER-0153-3** (Theorem (section 6, pp.253-254), theorem, scope: global; section 6, pp.253-254, (36)-(41)). For $P\ne Q$ interior points, $\lambda_0>0$, the Dirichlet series $\sum_m \phi_m(P)\phi_m(Q)\lambda_m^{-s}$ (finite abscissa) continues analytically to a regular function $f(s,P,Q)$ for $\Re s>\frac N2-2n-3$ [as printed], and $f(s,P,Q)=0$ for every non-positive integer $s$ in that half-plane. For $\lambda_0=0$ (sum from m=1) the same holds except that $f(0,P,Q)=-1/V$ (value garbled in extraction).
- **THM-PAPER-0153-4** (Theorem (section 7, p.255), theorem, scope: global; section 7, p.255 (also stated in Introduction p.243: poles at $s=\frac N2-\nu$ for N odd and $s=\frac N2,\dots,1$ for N even)). If $V$ is closed, the zeta function $\sum_{m\ge1}\lambda_m^{-s}$ continues analytically to the left of its abscissa of convergence; for $N$ odd it equals $\frac{1}{(2\sqrt\pi)^N}\sum_{\nu=0}^n\frac{\int_V U_\nu(P,P)\,dV}{\Gamma(s)(s-\frac N2+\nu)}+R_n(s)$ (and an analogous formula for $N$ even), with $R_n(s)$ regular for $\Re s>\frac N2-n-2$. At $s=0$ its value is $-1$ if $N$ odd, and $\frac{\int_V U_{N/2}(P,P)dV}{(2\sqrt\pi)^N}-1$ if $N$ even; at negative integers $s$ the value is $0$ for $N$ odd and, for $N$ even, $\frac{\Gamma(1-s)...}{(2\sqrt\pi)^N}\int_V U_{N/2-s}(P,P)\,dV$ (exact form garbled in extraction).
- **THM-PAPER-0153-5** (Corollary (section 7, p.256), corollary (Weyl law), scope: asymptotic; p.255-256 and Introduction p.243-244). For a closed manifold, $N(\lambda_m<T)\sim\dfrac{V\,T^{N/2}}{(2\sqrt\pi)^N\,\Gamma(\frac N2+1)}$ as $T\to\infty$ (Ikehara), with $V$ the volume; with boundary the method does not give the analogous complete result for $\sum\lambda_m^{-s}$.

### Key definitions

- Minakshisundaram-Pleijel zeta function $\sum_m\lambda_m^{-s}$ and the pointwise eigenfunction Dirichlet series (4), (5)
- Heat parametrix coefficients $U_\nu(P,Q)$ (Minakshisundaram-Pleijel coefficients) defined by transport equations with $U_0(P,P)=1$
- Regular part $\gamma_n$ of the Green's function and parametrix $\Gamma_n(P,Q;-\xi)=\eta_R(r_{PQ})K_n(P,Q;-\xi)$

### Principal lemmas

- **THM-PAPER-0153-L1** (Section 1, (8)-(10); section 1, pp.244-245). Hadamard-type parametrix of the heat equation $H_n(P,Q;t)=\frac{1}{(2\sqrt{\pi t})^N}e^{-r^2/4t}(U_0+U_1t+\dots+U_nt^n)$ (as the text prints: $r^2/4t$ form), with $U_\nu$ determined by transport equations $r\,\partial_rU_\nu+\frac r2\partial_r\log\sqrt g\,U_\nu+\nu U_\nu=\Delta U_{\nu-1}$, finite at $P=Q$, $U_0(P,P)=1$; and via Laplace transform a parametrix $K_n(P,Q;-\xi)$ of $\Delta u-\xi u=0$. — *Role:* Local construction giving the Minakshisundaram-Pleijel coefficients $U_\nu(P,P)$ (heat kernel coefficients).
- **THM-PAPER-0153-L2** (Section 2, (11)-(15); section 2, pp.246-247, (12),(15)). Writing $G(P,Q;-\xi)=\Gamma_n(P,Q;-\xi)-\gamma_n(P,Q;-\xi)$ with cutoff parametrix $\Gamma_n=\eta_R(r_{PQ})K_n$, the regular part satisfies the variational characterization $\gamma_n(P,P;-\xi)=E(\gamma_n;\Gamma_n)-\int\Gamma_n(\Delta\Gamma_n-\xi\Gamma_n)dV$ and the two-sided bound ($u=0$ admissible; completing the square) gives $|\gamma_n(P,P;-\xi)|<\text{const}\cdot\xi^{N/2-n-2}$ [as OCR shows: const $\xi^{...}$]. — *Role:* Estimate of the regular part of the resolvent kernel on the diagonal for $\xi\to+\infty$; controls the remainder $R_n(s,P)$.
- **THM-PAPER-0153-L3** (Section 3, (17)-(22); section 3, pp.247-248). Bessel-function bounds ($K_0(z)$ asymptotics, estimates of $|\Gamma_n|$, $|\Delta\Gamma_n-\xi\Gamma_n|$ near the diagonal) yield estimates (22) for the integrals (13),(14). — *Role:* Technical estimates for the variational bound.
- **THM-PAPER-0153-L4** (Section 4, (23)-(30); section 4, pp.248-251). Iterating the resolvent identity $G(P,Q;-\xi)-G(P,Q;-\xi_0)=-(\xi-\xi_0)\int G(P,\Pi;-\xi)G(\Pi,Q;-\xi_0)dV_\Pi$ gives (23), (24); passing to $Q\to P$ and taking finite parts yields the expansion (28),(29) of $\sum_m\phi_m(P)^2/((\lambda_m+\xi)\lambda_m^{\rho+1})$ in terms of $M_n(\xi,P)$, $\gamma_n(P,P;-\xi)$ and a polynomial in $\xi$; with $M_n$ computed via Bessel functions $K_\zeta$ (formulas (26) for N odd, (27) for N even with digamma terms). Case $\lambda_0=0$ handled in (30). — *Role:* Exact identity from which analytic continuation follows by Mellin-Barnes/contour integration in $\xi$.
- **THM-PAPER-0153-L5** (Section 5, contour step (31); section 5, pp.251-253). Multiplying (29) by $\frac{1}{2\pi i}(-\xi)^{-s}$ and integrating over a keyhole contour around the positive real axis gives $\sum\phi_m^2\lambda_m^{-s}=\frac{\sin\pi s}{\pi}\int\frac{M_n(\xi,P)-\gamma_n(P,P;-\xi)}{\xi^s}d\xi+(\text{entire})$, regular for $\Re s>N/2-n-2$ by the bound on $\gamma_n$; the explicit integral of $M_n$ yields the displayed poles and the zeros at non-positive integers. — *Role:* Converts the resolvent identity into analytic continuation (Mellin transform of the resolvent).

### Proof architecture

Following Carleman, (i) build a Hadamard-style local parametrix of the heat equation and, by Laplace transform, of $(\Delta-\xi)u=0$ (section 1), noting that Hadamard's convergence proof for the infinite series fails here so only finite sums to order n (with n>N/2-2) are used; (ii) cut off to get a global parametrix $\Gamma_n$ and write the Green function as $\Gamma_n-\gamma_n$, estimating $\gamma_n(P,P;-\xi)$ as $\xi\to+\infty$ by a Dirichlet-principle (variational) argument (sections 2-3); (iii) expand the Green function in eigenfunctions via the iterated resolvent identity and take finite parts on the diagonal (section 4); (iv) Mellin-transform in $\xi$ along a keyhole contour to get analytic continuation to $\Re s>N/2-n-2$ with explicit poles and values at non-positive integers (section 5); (v) off-diagonal case P != Q uses the variational estimate of $\gamma_n(P,Q)+\gamma_n(Q,P)$ with the symmetric/antisymmetric trick (sections 6); (vi) closed case integrates over V (section 7). Ikehara's Tauberian theorem (Wiener, Ann. Math. 33) converts the simple pole at $s=N/2$ into Weyl-type asymptotics.

Dependency edges: CAND-00279 Theorem sec.5 → Carleman 1934/1936 (generalizes); CAND-00279 Corollary → Ikehara-Wiener Tauberian theorem (imports); CAND-00279 sec.2 → Dirichlet principle (Courant-Hilbert II) (uses variational characterization)

**Imported results.** Carleman 1934, 1936: method for Euclidean domains (generalized); Minakshisundaram, 'A generalization of Epstein zeta functions' (Canad. J. Math., Euclidean domains of any dimension; poles/zeros pattern); Wiener, Tauberian theorems, Ann. of Math. 33 (1932) / Ikehara's theorem; Giraud 1932 and de Rham 1946 (Green function bounds / eigenfunction expansion convergence); Courant-Hilbert vol. I, II (variational principles); Weyl 1911; Watson (Bessel functions); Pleijel 1940, Arkiv Mat. 27A (asymptotics)

**Techniques.** Hadamard parametrix / transport equations (heat kernel coefficients $U_\nu$); Laplace transform from heat kernel to resolvent kernel; Dirichlet principle (variational estimate of regular part of Green's function); Mellin transform in the resolvent parameter, keyhole-contour analytic continuation; Bessel K function finite-part computations; Ikehara/Wiener Tauberian theorem

## Context and interpretation

**Importance and obstacle overcome.** Introduces the zeta function of the Laplacian on a Riemannian manifold (the Minakshisundaram-Pleijel zeta function) with meromorphic continuation, poles from local geometric invariants, and the zeros at negative integers (odd dimension); this is the prototype for spectral zeta functions, heat-kernel asymptotic expansions and later Selberg zeta / zeta regularization. The main obstacle is that Hadamard's convergence proof for the parametrix series fails in the heat setting, so a finite-order parametrix plus variational control of the remainder is used instead.

**Relation to prior work.** Generalizes Carleman and Minakshisundaram (Euclidean domains) to curved manifolds; precursor of the heat kernel asymptotic expansion of Minakshisundaram-Pleijel, used later by Seeley, McKean-Singer, Ray-Singer, and of Selberg trace formula-zeta analogies.

**Limitations and open questions.** Regularity assumed ('sufficiently regular'; analytic stated for convenience); for manifolds with boundary the method gives complete results only for the diagonal and off-diagonal eigenfunction series, not for $\sum\lambda_m^{-s}$ (authors defer to Weyl/Courant methods). No statement about zeros in the critical strip, no functional equation (none exists in general).

**Ideas in remarks/appendices/abandoned paths.** Remark in Introduction (p.244) that the analytic continuation for the sphere was studied earlier by Minakshisundaram (Zeta-functions on the Sphere); remark in section 1 (p.245) that Hadamard's convergence proof fails for the infinite heat parametrix series (hence only an asymptotic expansion, anticipating the asymptotic nature of the heat kernel expansion).

## Research potential

- **Hypotheses that might be weakened.** Regularity of V (analytic -> smooth, even Lipschitz); the use of Ikehara requires only a simple pole with nonnegative coefficients; the closed-manifold conclusion about $\zeta(0)$ values gives the integral of local invariants (relevant to determinants).
- **Generalizations.** Replace Laplacian by other elliptic operators, replace manifold by hyperbolic surface where heat/resolvent trace becomes the Selberg trace formula, yielding Selberg zeta and a functional-equation structure; general zeta regularization.
- **Candidate connections.** For RH-motivated work: the meromorphic structure with trivial zeros at non-positive integers resembles the Gamma-factor analysis of Riemann zeta; for flat tori the series is an Epstein zeta function whose zero location is a genuine RH-type question (Epstein zeta can have zeros off the line), tying this paper to families D/E of the archive.
- **Reusable lemmas.** The estimate $|\gamma_n(P,P;-\xi)|\lesssim\xi^{N/2-n-2}$ and the keyhole-contour computation (31)-(33) as a template for continuation of any resolvent-defined Dirichlet series; the closed-manifold formula giving $\zeta(0)$ and values at negative integers in terms of $\int U_\nu$.
- **Possible experiments.** Check the pole/residue/value table numerically for a flat torus (Epstein zeta, N=2) and the round $S^2$ (eigenvalues $l(l+1)$, mult $2l+1$), verifying $\zeta(0)=\int U_1/(4\pi)-1$ with $U_1(P,P)=R/6$ (scalar curvature term) for sanity.
- **Risks / barriers.** Heat-kernel methods produce only trivial-zero information; no approach to nontrivial zeros without additional (arithmetic) structure.

## Audit notes (Level 1 reader)

Text extracted by pdftotext from Cambridge open PDF; many displayed formulas garbled, so exact printed coefficients in formulas (26),(27),(33) and the section-6 exponent $N/2-2n-3$ could not be verified symbolically. The intro states poles 's=N/2-nu' for N odd, and for N even 's=N/2, N/2-1,...,1', consistent with the theorem. In the intro the Ikehara reference is [14] (Wiener) while the later passage cites '[18]' (OCR artifact). Intro says the case 'p. 243: N even values at non-positive integers' determined from the metric tensor. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00279`; harvest queries: citation_expansion.
- Triage decision: include — Heat kernel zeta on manifolds; basis of spectral zeta.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
