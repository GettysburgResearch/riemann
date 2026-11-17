# PAPER-0005 — Sharpenings of Li's criterion for the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Voros, André |
| Year / stratum | 2006 / S5 |
| Venue | Math. Phys. Anal. Geom. 9, No. 1, 53-63 (2006). |
| Identifiers | zbMATH [1181.11055](https://zbmath.org/?q=an:1181.11055) · DOI [10.1007/s11040-005-9002-8](https://doi.org/10.1007/s11040-005-9002-8) · arXiv [math/0506326](https://arxiv.org/abs/math/0506326) |
| MSC | 11M26 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/math/0506326 (v2, 25 Jan 2006) |
| Selection | score 4.8363, in-pool citations 24, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can the Li coefficients lambda_n be described by a sharp large-n dichotomy, with polynomial-order tempered growth if RH holds and exponentially growing oscillation if RH fails? What are the exact asymptotics of lambda_n under RH, and does the same dichotomy hold for general zeta and L-functions?

**Historical motivation.** Li (1997) showed RH iff lambda_n>=0 for all n. Keiper (1992) had already noted the n log n trend, with no proof. Maslanka observed numerically a smooth growth plus small oscillations. Voros announced the dichotomy in 2004 and published the full text here.

### Main results

- **THM-PAPER-0005-1** (Eq. (9), exact formula (unconditional), scope: finite; Sect. 2, Eq. (9); inverse in Eq. (11)). With Z(\sigma)=\sum_k x_k^{-\sigma}, x_k=\rho_k(1-\rho_k)=\tfrac14+\tau_k^2, \mathrm{Re}\,\sigma>1/2: \lambda_n=-n\sum_{j=1}^{n}(-1)^j\frac{1}{j}\binom{n+j-1}{2j-1}Z(j), where the sum is over the pairs of zeros \rho=\tfrac12\pm i\tau_k grouped as in Eq. (2).
- **THM-PAPER-0005-2** (Eq. (12), integral representation (unconditional), scope: finite; Sect. 2, Eq. (12)). \lambda_n=\frac{(-1)^n n i}{\pi}\oint_C I(\sigma)\,d\sigma with I(\sigma)=\frac{\Gamma(\sigma+n)\Gamma(\sigma-n)}{\Gamma(2\sigma+1)}Z(\sigma), and C a contour encircling only the poles \sigma=1,\dots,n.
- **THM-PAPER-0005-3** (Eq. (14), asymptotic (RH false), rigorous via Darboux, scope: asymptotic; Sect. 3 [RH false], Eq. (14)). The generating function f(z)=\sum\lambda_n z^{n-1} has simple poles of residue 1 at z_k=(\tau_k-i/2)/(\tau_k+i/2) and \bar z_k inside the unit disc. Hence \lambda_n\sim\sum_{|z_k|<1} z_k^{-n}+\mathrm{c.c.} \pmod{o(e^{\varepsilon n})\ \forall\varepsilon>0}, with multiplicities. This gives exponentially growing oscillations of both signs.
- **THM-PAPER-0005-4** (Eq. (15), asymptotic (RH true, general L), scope: asymptotic; Sect. 3, Eqs. (5),(15),(16)). If all zeros are on the critical line and Z has a double pole at \sigma=1/2 with polar part R_{-2}\varepsilon^{-2}+R_{-1}\varepsilon^{-1}, then \lambda_n=2\pi n[2R_{-2}(\log n-1+\gamma)+R_{-1}]+o(n). Hypothesis (16): N(T)=2T[2R_{-2}(\log T-1)+R_{-1}]+\delta N(T), \delta N(T)=O(T^\alpha), \alpha<1.
- **THM-PAPER-0005-5** (Theorem (asymptotic criterion), Eqs. (17)-(18), theorem (equivalence), scope: asymptotic; Sect. 3 Recapitulation, Eqs. (17)-(18)). RH holds iff \lambda_n\sim \tfrac12 n(\log n-1+\gamma-\log 2\pi) \pmod{o(n)} (tempered growth to +\infty). RH fails iff \lambda_n\sim\sum_{\arg\tau_k>0}\big(\tfrac{\tau_k+i/2}{\tau_k-i/2}\big)^n+\mathrm{c.c.} \pmod{o(e^{\varepsilon n})}. The values R_{-2}=(8\pi)^{-1}, R_{-1}=-(4\pi)^{-1}\log 2\pi are used for \zeta.
- **THM-PAPER-0005-6** (Eqs. (20)-(26), decomposition (partly unconditional), scope: asymptotic; Sect. 4, Eqs. (20)-(26)). \lambda_n=S_n+\bar S_n with S_n=-\sum_{j=1}^n\binom nj\eta_{j-1} (from (s-1)\zeta(s)) and \bar S_n=1-\tfrac{\log 4\pi+\gamma}{2}n+\sum_{j=2}^n(-1)^j\binom nj(1-2^{-j})\zeta(j). Unconditionally, \bar S_n\sim\tfrac12 n(\log n-1+\gamma-\log 2\pi)+\tfrac34-\sum_{k\ge1}\frac{B_{2k}}{4k}n^{1-2k}. Then S_n=o(n) iff RH, while S_n\sim\sum z_k^{-n}+\mathrm{c.c.} if RH fails.

### Key definitions

- \lambda_n=\sum_\rho[1-(1-1/\rho)^n] (Li's normalization, n times Keiper's)
- \Xi(s)=s(s-1)\Gamma(s/2)\pi^{-s/2}\zeta(s)
- Z(\sigma)=\sum_k x_k^{-\sigma}, x_k=\rho_k(1-\rho_k)
- \eta_n via \log[s\zeta(1+s)]=-\sum \eta_{n-1}s^n/n
- f(z)=\frac{d}{dz}\log\Xi(1/(1-z))=\sum\lambda_n z^{n-1}

### Principal lemmas

- **THM-PAPER-0005-L1** (Oesterle argument (unnumbered); Sect. 3 end of [RH true]). If all zeros lie on the critical line, \lambda_n=2\int_0^\infty[1-\cos n\theta(T)]\,dN(T) with \theta(T)=2\arctan(1/2T). After integration by parts and Riemann-Lebesgue (using (16)), \lambda_n=n\int_0^\infty\frac{\sin t}{t}[8R_{-2}(\log\frac nt-1)+4R_{-1}]\,dt+o(n). — *Role:* A rigorous real-analytic proof of RH => (17), attributed to J. Oesterle (private communication, unpublished).
- **THM-PAPER-0005-L2** (Conformal map remark; Sect. 3 [RH false]). Under s\mapsto z=s/(s-1) type change of variable ([2]), the zeros \rho map to z_\rho; RH is equivalent to all z_\rho lying on |z|=1, and zeros off the line give poles with |z_k|<1. — *Role:* Input to the Darboux step for the RH-false branch.
- **THM-PAPER-0005-L3** (Residue (19); Sect. 3 after the Theorem). \delta\lambda_n=(-1)^n 2n\,\mathrm{Res}_{\sigma=0}I(\sigma)=2Z(0)=7/4, matching numerics at the sub-leading level. — *Role:* Numerical consistency check of the saddle-point/residue picture.

### Proof architecture

Hadamard product -> log Xi expanded in Z(j) -> exact finite sum (9) -> contour integral (12) with Gamma-ratio kernel and secondary zeta function Z(sigma). RH-true branch: saddle point at sigma_r(n) near 1/2 merges with the double pole of Z at 1/2, so the contour is shrunk to the residue (15); the saddle-point step is explicitly heuristic, and Oesterle's Stieltjes-integral argument makes it rigorous. RH-false branch: Darboux's theorem on the poles of the generating function in the unit disc (rigorous) gives (14), which the saddle-point analysis confirms (saddle points sigma_k=ni/(2 tau_k) lie in Re sigma>1/2 only for off-line zeros). The two forms are mutually exclusive, which gives the equivalence. Section 4 splits off the explicit archimedean piece to isolate S_n=o(n) vs exponential oscillation.

Dependency edges: CAND-01183 → CAND-01219 (generalized to GL(N) with rigorous remainder by Lagarias); CAND-01183 → Bombieri-Lagarias 1999 Li criterion paper (builds on)

**Imported results.** Darboux theorem on Taylor coefficients (Dingle, [6] ch. VII sec. 2); Bombieri-Lagarias [2]: Li criterion and affine expression of lambda_n in eta_j, Cor. 1(c); Li's criterion [17]; Stirling formula and Bessel/Fourier-integral evaluation [9]; Pole structure of Z(sigma) at negative half-integers and sigma=1/2 [13,26]

**Techniques.** Hadamard product and secondary zeta function Z(sigma); contour integral and residue calculus; saddle-point method (heuristic); Darboux's theorem on singularities of generating functions; Stirling and digamma asymptotics; Stieltjes integration by parts and Riemann-Lebesgue (Oesterle); Stieltjes cumulants eta_j

## Context and interpretation

**Importance and obstacle overcome.** It upgrades Li's positivity criterion to a sharp asymptotic dichotomy. Under RH, lambda_n grows like (1/2) n log n with explicit B; otherwise it oscillates with exponentially growing amplitude. In particular borderline behavior such as lambda_n -> 0 is ruled out. The obstacle overcome is the lack of control of the oscillatory sum (9), handled by passing to the contour integral (12) and the double pole of Z at 1/2.

**Relation to prior work.** Extends Li, Keiper and Bombieri-Lagarias: the RH-true asymptotic (17) was displayed by Keiper (Eq. 37) as a stronger-than-RH property, and Voros shows it is equivalent to RH. It proves Maslanka's conjectured expansion (24).

**Limitations and open questions.** The author states the saddle-point step is a heuristic, and the rigorous RH-true proof is only the unpublished Oesterle argument, sketched in the text. Detecting a zero off the line at height Im rho needs n of order 2|Im rho|, hence n >~ 10^18 given the known zero-free verification up to about 10^9 in height at the time, so the criterion has no practical sensitivity. A real-analytic proof of the RH-false branch is not available. Sect. 5 for general L is a summary only.

## Research potential

- **Hypotheses that might be weakened.** The RH-true branch needs only the zero counting asymptotic (16) with delta N=O(T^alpha), alpha<1, and meromorphy of Z with double pole at 1/2. It may be possible to state a Li-type dichotomy with weaker error terms, or for zeta-like Dirichlet series lacking Euler products but having a functional equation.
- **Generalizations.** Axiomatize (5)+(16) for the Selberg class, for Hecke L-functions on Gamma_0(N), and for GL(N) automorphic L-functions (this was done by Lagarias, see CAND-01219). The same dichotomy applies to any multiset satisfying Bombieri-Lagarias hypothesis (1.6).
- **Candidate connections.** Lagarias CAND-01219 (rigorous O(sqrt n log n) remainder under RH); Maslanka's expansion of lambda_n; Keiper's 1992 computation; Bombieri-Lagarias positivity as Weil positivity; Oesterle's argument as a template for a rigorous real-variable treatment.
- **Reusable lemmas.** The Darboux step (14) is directly reusable and rigorous: poles of the generating function f(z) inside |z|<1 correspond bijectively to zeros off the line. The exact finite sum (9) gives an integer-binomial formula for lambda_n in Z(j), and the inversion (11) recovers Z(j) from lambda_n.
- **Possible experiments.** Compute lambda_n via (9) from tabulated Z(j) to n about 10^4 with high precision, then fit S_n=lambda_n-bar S_n and test S_n=o(n). Insert a synthetic off-line zero pair and verify that S_n tracks (14) once n exceeds about |Im 1/tau|^{-1}; this gives an empirical n-detection threshold versus height.
- **Risks / barriers.** The criterion is equivalent to RH and numerically insensitive. It does not obviously yield a route to RH, since S_n=o(n) needs the same information as RH. The RH-true proof depends on an unpublished argument.

## Audit notes (Level 1 reader)

Heuristic status of the saddle-point step is acknowledged by the author (Sect. 3 intro). The rigorous RH-true proof is attributed to private communication (Oesterle, ref. [23]), unpublished; the sketch in the text is compressed, e.g. 'neglecting delta N(T) and other O(theta^{-alpha}) terms: error o(1)'. In the RH-false branch, Darboux gives asymptotics only mod o(e^{eps n}), and the 'simple zero for argument's sake' assumption is later removed via (14). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01183`; harvest queries: kw_RH_any, msc_11M26, arxiv_li_criterion, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Exact and asymptotic formulae for Li coefficients.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
