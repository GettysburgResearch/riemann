# PAPER-E012 — Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces

Eva A.Gallardo-Gutiérrez and Daniel Seco. *Complex Analysis and Operator Theory*19,Article38(2025),27pages. DOI https://doi.org/10.1007/s11785-025-01661-2 . Received10June2024, accepted11January2025, published29January2025, as stated on the actual journal title page.

Primary versions accessed: complete arXiv2206.02654v6,5June2024 (22pages; manuscript date6June2024), https://arxiv.org/pdf/2206.02654v6 ; actual journal PDF https://link.springer.com/content/pdf/10.1007/s11785-025-01661-2.pdf . These are manifestations of **one work**. Exact version hashes and private paths are in `papers/weighted_dirichlet_round3_records.jsonl` and the scoped audit. Earlier arXiv title/version history has not been reconstructed; no claim thatv6 equals the journal throughout.

**Read/audit scope:** whole-work substantive Level1 reading of the entire22-page preprint, including all five sections and references; journal title/metadata and selected mathematical passages, especially norm definition, Lemma2.3 and Proposition5.1. Not a full27-page journal reading and not whole-paper Level2. Two localized technical passages are independently reconstructed in `audits/gallardo_seco_endpoint_round3.md`, awaiting source/normalization adversarial review. External Selberg, Beurling, Noor, multiplier and Riesz-basis dependencies are not all independently audited.

## Mathematical objects and main source results

D_alpha consists of f(z)=sum_(n>=0)a_nz^n with sum|a_n|²(n+1)^alpha finite. Its coefficient sequence analog is ell^p_alpha with sum_(n>=1)|u(n)|^p n^alpha finite. Put r_k(n)=k{n/k},k>=2. Original coefficient norms are preserved; equivalent area norms do not change bounded-invertibility conclusions but should not be substituted for exact constants.

Theorem2.1 (preprintpp4–6): if1<p<=2, alpha in(−1−p,−1−p/2], and the constant sequence1 lies in the ell^p_alpha closure of span{r_k:k>=2}, thenzeta has no zero in Re(s)>−(alpha+1)/p. Forp1,alpha in[−2,−3/2], the corresponding convergence excludes zeros in the **closed** half-plane Re(s)>=−(alpha+1). This is a sufficient criterion with arbitrary approximating coefficients. Its proof is the constrained fractional-part Mellin transform plus a weighted Hölder estimate; the distinction between open and closed endpoints is exactly the dual-summability condition.

The natural error array is F_m(n)=1+sum_(k2..m)mu(k)r_k(n)/k−r_m(n)sum_(k1..m)mu(k)/k. It vanishes for n<=m and satisfies|F_m(n)|<2m. Proposition2.5 (pp7–8) derives bounded ell^p_(−p−1) norms and convergence when alpha<−p−1. The criticalp1alpha−2 norm question is linked to PNT. These are distinct from fixed logarithmic Möbius windows in the new campaign.

Theorem3.1 (pp9–11): for fixed sigma in[1/2,1), set G(n,m)=sum_(k<=m)mu(k)floor(n/k). Suppose a nondecreasing omega:[0,infinity)->[0,infinity], finite at1/2, bounds, for the stated m,n range m<n<m^(1/sigma),

|G(n,m)| <= [m^sigma+n^sigma/sqrt(logn)+(n/m)^(sigma/(1−sigma))] omega(m|sum_(k<=m)mu(k)/k|).

Then Re(s)>sigma is zero-free. The source's universal m quantifier is to be retained when applying it; its proof selects a sign-change subsequence with m|sum mu/k|<=1/2, uses the weighted norm bound for weak convergence, then Mazur and Theorem2.1. The absolute values around the Möbius sum are visible in the publisher formula despite disappearing from extracted OCR. This is not a discovered missing hypothesis.

Section4 derives the primorial-divisor approximant F'_m and identifies its values for1<=n<m as minus the count of1<k<=n coprime tom (Theorem4.2). Subsequent estimates isolate an early-n obstruction rather than establish critical norm convergence.

Section5 studies T_af=f'−af/(1−z) betweenD_(alpha+2) andD_alpha, and weighted multipliers, to extend Noor's Hardy-space formulation. Two version-specific findings are now independently reviewed and director-adjudicated: Proposition5.1's inclusive bounded-bijection endpoint fails, and Theorem5.5's reverse implication fails at the strictly supercritical pair(alpha,a)=(-3,7/4). The main Theorem2.1 and Section3 do not require the endpoint proposition, and their approximation-to-zero-free implications are not refuted by these witnesses. Exact scope and replacements: audits/adversarial_reviews/gallardo_seco_director_endpoint_round4.md and weighted_criterion_director_round5.md.

## Technical findings and research questions

The initial scoped audit supplied a polynomial approximate-kernel for Proposition5.1 and a separate local constrained-Mellin display issue. The endpoint now has two verified analytic witnesses and a complete strict weighted-Hardy classification. The local omitted-c1 display issue retains its own pending independent classification; it is not automatically promoted with the other findings.

The general weighted-Noor problem has also been resolved at the reconstruction level: for the same original parameters and norm the correct zero-free threshold is b=(1-alpha)/2-a, rather than the printed(-1-alpha)/2. A direct bounded radial functional separates the target at(-3,7/4), while a weighted Mellin/discrete approximation proves the corrected converse using the declared classical Balazard–Saias input. The critical(-3,1) closure has a separate unconditional Bergman proof. Publication priority is unassessed; no whole-paper Level2/3 promotion follows. Next: original-lemma/correction-history comparison, effective fixed-parameter approximation, and the Section3 subsequence mechanism in relation to fixed logarithmic-window multiplicity obstructions.
