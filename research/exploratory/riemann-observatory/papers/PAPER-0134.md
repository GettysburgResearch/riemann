# PAPER-0134 — Neue Anwendungen der Theorie der diophantischen Approximationen auf die Riemannsche Zetafunktion.

| Field | Value |
|---|---|
| Authors | Bohr, Harald; Courant, Richard |
| Year / stratum | 1914 / S2 |
| Venue | J. Reine Angew. Math. 144, 249-274 (1914). |
| Identifiers | zbMATH [45.0718.02](https://zbmath.org/?q=an:45.0718.02) · DOI [10.1515/crll.1914.144.249](https://doi.org/10.1515/crll.1914.144.249) |
| MSC | 11M06, 11J99 |
| Families | A, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/id/PPN243919689_0144 (page-level OCR via https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0144/00000253 to 00000279; Crelle vol. 144, pp. 249-274) |
| Selection | score 3.5429, in-pool citations 38, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Describe the set of values taken by zeta(sigma+it) on a vertical line with sigma in (1/2,1]: is the set {zeta(sigma_0+it): t in R} dense in C? The method deepens Bohr's Kronecker-theorem argument for sigma>1 to the region where the Euler product does not converge.

**Historical motivation.** Bohr had described the value distribution of zeta for sigma>1 using Kronecker's theorem. The obstruction for 1/2<sigma<=1 is the lack of uniform convergence of the Euler product in t. Bohr-Courant replace pointwise convergence by convergence in measure (via Schnee), combined with equidistribution to show the exceptional set cannot hide the target values.

### Main results

- **THM-PAPER-0134-1** (Hauptsatz (stated in the introduction p. 255 and proved in Sec. 4, pp. 271-274), theorem, scope: global; Introduction p.255; Sec. 4). For every fixed $\sigma_0$ with $\tfrac12<\sigma_0\le1$ (the table of contents gives the range as 1/2<sigma_0<=1; the sentence stating the theorem in the OCR reads 1/2<sigma_0<1 with equality allowed per the introduction, which treats $\sigma=1$ explicitly), the set $\{\zeta(\sigma_0+it):t\in\mathbb R\}$ is dense in $\mathbb C$: for every $a\in\mathbb C$ and $\varepsilon>0$ there is $t_0$ with $|\zeta(\sigma_0+it_0)-a|<\varepsilon$.
- **THM-PAPER-0134-2** (Introduction pp. 249-251 (recalled earlier result of Bohr), prior result (not new, quoted), scope: global; Introduction). For fixed $\sigma_0>1$ the set $U(\sigma_0)=\{\prod_n(1-p_n^{-\sigma_0}e^{2\pi i\eta_n})^{-1}\}$ is dense in $V(\sigma_0)=\{\zeta(\sigma_0+it)\}$ closure; and there is $\sigma_0(R)>1$ such that for $1<\sigma_0<\sigma_0(R)$ the circle-multiplication set $F(\sigma_0)$ contains the disc $|z|\le R$, hence the values of $\zeta$ on the line are dense in any bounded region of the plane for $\sigma_0$ close to 1.

### Key definitions

- F_N(s)=prod_{n<=N}(1-p_n^{-s})^{-1}; R_N(s)=zeta(s)/F_N(s)
- U(sigma_0), V(sigma_0): set of values of the infinite product in free variables eta_n, and values of zeta on the line
- W_N(R_0): Jordan volume of eta-set with S_N in rectangle R_0
- mu(M(T)): Lebesgue measure of time set

### Principal lemmas

- **THM-PAPER-0134-L1** (Hilfssatz I (Sec. 1); Sec. 1, pp. 255-258). Let $\tfrac12<\sigma_0<1$, $\varepsilon,\delta>0$ and $R_N(s)=\zeta(s)\prod_{n\le N}(1-p_n^{-s})$. Then there is $N_0(\sigma_0,\varepsilon,\delta)$ such that for every $N\ge N_0$ the total length $\mu_N(T)$ of the set of $t\in[-T,T]$ with $|R_N(\sigma_0+it)-1|\ge\varepsilon$ is $<\delta T$ for $T\ge T_0(N)$. (The tail product need not converge pointwise but converges 'almost everywhere in measure'.) — *Role:* Controls the remainder: shows the truncated Euler product approximates zeta for most t; proof via Schnee's mean-value theorem for Dirichlet series (imported)
- **THM-PAPER-0134-L2** (Hilfssatz II (Sec. 2); Sec. 2, pp. 258-263). (Kronecker equidistribution in Jordan measure) If $\lambda_1,\dots,\lambda_N$ are linearly independent over $\mathbb Q$ and $\Omega$ is a Jordan-measurable region in the unit cube $Q$ of volume $W$, then the set $M(T)$ of $t\in[0,T]$ with $(t\lambda_1,\dots,t\lambda_N)\bmod 1\in\Omega$ has $\mu(M(T))/T\to W$. The authors note it fails for Lebesgue measure on non-Jordan measurable sets. — *Role:* Quantifies how often the finite Euler product reaches a region; Weyl's proof (July 1913) is acknowledged
- **THM-PAPER-0134-L3** (Hilfssatz III (Sec. 3, p. 268); Sec. 3, pp. 263-270). Let $r_n\in(0,1)$ with $\sum r_n$ divergent and $\sum r_n^2$ convergent, and $R_0$ a fixed axis-parallel rectangle with centre $z_0$ in the $z$-plane. Then there is $k=k(R_0,z_0)>0$ and $N_0$ such that for $N\ge N_0$ the probability $W_N(R_0)$ (volume in $\eta\in[0,1]^N$) that the point $S_N(\eta)=\sum_{n\le N}\log(1-r_ne^{2\pi i\eta_n})^{-1}$ lies in $R_0$ is $>k$, with $k$ independent of $N$. — *Role:* Key probabilistic lemma: the sum of logs of the Euler factors (sums of convex closed curves) spreads over the whole plane without the hitting probability for a fixed rectangle tending to 0

### Proof architecture

Fix a target a. Write zeta = F_N * R_N with F_N the initial Euler product over n<=N and R_N=zeta*prod(1-p^-s) the remainder. (i) Hilfssatz I: for large N, |R_N-1|<eps except on a set of t of relative measure <delta. (ii) Take logs: log F_N(sigma_0+it) = sum_n log(1-p_n^{-sigma_0}e^{-it log p_n})^{-1}, which depends on the point (t log p_n/2 pi) mod 1; since log p_n are Q-linearly independent (unique factorization), Kronecker/Weyl (Hilfssatz II) says the relative time t spends in any Jordan-measurable region Omega of the cube equals vol(Omega). (iii) Hilfssatz III with r_n=p_n^{-sigma_0} (sum diverges iff sigma_0<=1, sum of squares converges iff sigma_0>1/2) gives a lower bound k>0, independent of N, on the volume of eta with S_N(eta) in a small rectangle around log a. (iv) Choose N>=N_0 and then T large so that the measure of {t: S_N in rectangle} exceeds k T/2 while the exceptional set from step (i) has measure <k T/4 (delta chosen < k/ something): hence some t_0 lies in the first set but not the second, giving |F_N(sigma_0+it_0)-a|<eps and |R_N-1|<eps, so |zeta(sigma_0+it_0)-a|<epsilon'. Uniformity in N of the lower bound k is the crux. The restriction to sigma_0>1/2 enters through convergence of sum r_n^2 and the Schnee mean-value estimate.

Dependency edges: CAND-00087 → Bohr 1912-1913 papers on zeta in sigma>=1 (extends method to critical strip); CAND-00087 → Voronin universality theorem (1975) (later strengthening: not only density of values but approximation of functions); CAND-00087 → Kronecker-Weyl equidistribution (uses)

**Imported results.** Kronecker's approximation theorem; Weyl's uniform distribution proof (communicated July 1913 in Goettingen); Schnee: mean value theorem for Dirichlet series (used for Hilfssatz I); Bohr: earlier papers on zeta on sigma>1 (C.R. Paris 154, 1912; Danish Academy 1913 on the line sigma=1)

**Techniques.** Kronecker's approximation theorem with uniform distribution (Weyl) in Jordan measure; truncated Euler product with mean-value control of the remainder (Schnee); sum of random convex curves / probabilistic geometry of Minkowski sums of circles; Linear independence of log p_n over Q; measure-theoretic selection of a good t_0 by comparing two measures

## Context and interpretation

**Importance and obstacle overcome.** Shows the zeta function takes values arbitrarily close to any complex number on every vertical line in 1/2<sigma<=1, a first step toward universality (Voronin 1975) and a classical result in value distribution (and used in discussions of the Lindelof/zero-free-region interplay). The obstacle is non-convergence of the Euler product to the left of sigma=1; overcome by the mean-value remainder estimate plus a quantitative (N-independent) hitting probability.

**Relation to prior work.** Direct continuation of Bohr's work on sigma>1 and the Bohr 1913 note for the line sigma=1; predecessor of Bohr-Jessen distribution theorem and Voronin universality.

**Limitations and open questions.** Density only; no quantitative rate and no statement that the closure is controlled on sigma=1/2 (the critical line) - Bohr-Courant's range excludes sigma_0=1/2 because sum r_n^2 diverges. Whether zeta(1/2+it) is dense in C remains unproven unconditionally (known only under heavier hypotheses; I did not verify the literature status).

## Research potential

- **Hypotheses that might be weakened.** The condition sum p^{-2 sigma_0}<infinity (sigma_0>1/2) in Hilfssatz III and the mean-value remainder (Hilfssatz I) are the only places 1/2 is needed; relaxing them is exactly the open critical-line question. Approach: replace pure Euler products by a Selberg-type or mollified-product approximation on sigma=1/2 and test whether Hilfssatz III survives with r_n=p_n^{-1/2} at the cost of a growing hitting-probability bound.
- **Generalizations.** The same architecture (truncated product + mean-value remainder + Kronecker/Weyl + N-uniform hitting probability) applies to Dirichlet L-functions, L-functions with Euler products of bounded degree and gives density, and was the template for Voronin's joint universality. For an RH-oriented use: density of zeta values near 0 is not zero-existence information, so no implication to RH.
- **Candidate connections.** Connect with the Bagchi/Voronin universality picture: zero-free vs zero-containing strips for universality is the observatory-relevant distinction (universality holds in 1/2<sigma<1 for functions without zeros, and the zeros of zeta in 1/2<sigma<1 are approximable by Voronin: RH is equivalent to a non-universality statement of a different kind, see Bagchi).
- **Reusable lemmas.** Hilfssatz III (N-uniform positive hitting probability for sums of logs of Euler factors with sum r_n=infinity, sum r_n^2<infinity) is reusable for any Dirichlet-series with Euler products of the same shape.
- **Possible experiments.** Numerical: for sigma_0=0.75, simulate S_N(eta) for random eta and compare the empirical hitting probability for a rectangle to the claimed k>0 as N grows (testing the N-independence); compare with the actual time density from zeta(0.75+it), t up to 10^6.
- **Risks / barriers.** The method is inherently qualitative (limits of relative measure) and loses at sigma=1/2; any RH-adjacent use would require quantitative control in T.

## Audit notes (Level 1 reader)

The OCR text has errors; the exact formulation of the sigma_0 range in the Hauptsatz is ambiguous between 'sigma_0<1' (sentence in Introduction, p.255: 'bei festem sigma_0 im Intervall 1/2 < sigma_0 < 1' appears to be read with an extra strict inequality) and 'sigma_0<=1' (table of contents, and the discussion of the line sigma=1 in the introduction); the archive record of the triage (1/2<sigma<=1) agrees with the TOC. A fully careful read of Hilfssatz III's proof (convex-curve geometry) was not done. The small mismatch (the main claim states density for 'jede Gerade' including sigma=1) should be checked in the facsimile.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00087`; harvest queries: msc_11M06.
- Triage decision: include — Bohr-Courant: zeta on vertical lines dense.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
