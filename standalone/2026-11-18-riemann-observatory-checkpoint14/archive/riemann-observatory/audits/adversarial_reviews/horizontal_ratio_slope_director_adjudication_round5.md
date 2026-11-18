# Adjudication of the exact horizontal-ratio slope

2026-11-17. Accepted as a **scoped RH-conditional mathematical reconstruction**, with historical priority unassessed. The director derived the Schur/Poisson proof, then read the complete independent skeptic proof and a different product-defect/residue proof from the equivalences researcher. The arguments preserve zero multiplicities, the full real-line integral and the exact source normalization. No RH or simplicity proof, new unconditional zero bound, publication novelty or whole-paper audit is claimed.

## Accepted statement

For J_epsilon defined in PAPER-C103 Proposition2, under RH,

lim_(epsilon down to0) J_epsilon/epsilon
= Sum_(distinct gamma) m_gamma[1-binomial(2m_gamma,m_gamma)/4^(m_gamma)]/(1/4+gamma²).

The sum includes positive and negative ordinates separately, with m_gamma the multiplicity of the corresponding zero. It is absolutely convergent. Its value is at least C0=xi'(1)/xi(1)=1+EulerGamma/2-log(4pi)/2, with equality precisely when every nontrivial zero is simple, still assuming RH. It is strictly below2C0. An arbitrarily high multiple zero can make an arbitrarily small positive excess; finite numerical agreement at a few epsilon values supplies no simplicity certificate.

## Why the noncompact integral is justified

The crucial check is not the elementary local beta integral. For F(w)=xi(1/2+w), the quotient H_epsilon=F(w)/F(w+epsilon) is contractive on the right half-plane. The positive real-defect measure has total mass

integral [1-Re H_epsilon(it)]dnu(t)/epsilon
=[1-F(1/2)/F(1/2+epsilon)]/epsilon -> C0,

where dnu=dt/[2pi(1/4+t²)]. Its local profile at a multiplicity-m zero is (iu/(1+iu))^m. The local real-defect integral is m pi, and the local squared-defect integral is 2m pi[1-binomial(2m,m)/4^m]. The paired order-one product gives C0=(1/2)Sum m_gamma/(1/4+gamma²), exactly the sum of all limiting local real-defect masses. Finite sets of rescaled windows therefore exhaust the total mass. Contractivity bounds the squared defect by twice the real defect on every omitted set. This proves the global limit without zero-gap, simplicity or inverse-derivative assumptions.

The skeptic's proof uses only fixed bounded scaled windows before the exhaustion limit; it avoids any uniform local Taylor estimate over the whole zero set. The director's alternative fixed-neighborhood argument explicitly bounds cross-errors by O(epsilon² log(1/epsilon)). Both lead to the same limit. The independently derived second proof instead bounds infinite product tails by a sum of Poisson kernels. Their convolutions with the completion-weighted measure are O((1+|gamma|)^(-2+epsilon0)), uniformly for0<epsilon<=epsilon0<1; Riemann–von Mangoldt makes the multiplicity-weighted tail summable. This is a mathematically different global check.

The completion ratio has L2 distance O(epsilon) from1, whereas the completed squared-defect norm is O(epsilon). Thus replacing xi by zeta changes squared norms by O(epsilon^(3/2))=o(epsilon). Pointwise convergence of completion factors would not suffice.

## Negative control retained

For F(w)=exp(w²), evenness and Schur contractivity still hold for F(w)/F(w+epsilon), but there are no zeros and the corresponding squared-defect slope at Poisson center1/2 equals2. Mass escapes to infinity. This refutes an overgeneralization based only on contractivity and evenness. The xi order-one paired-product identity is indispensable to the exhaustion proof; it is not a disposable technicality.

## Source, independence and next step

The O(epsilon) result belongs to Balazard–de Roton, PAPER-C103. Its inspected manuscript remarks that a precise asymptotic would be interesting; that historical remark does not establish that the present formula is new at the execution date. A later-literature search is active. Burnol's Hilbert-space work and later horizontal regularization/negative-moment papers are priority targets. If the formula is already known, preserve the exact source and these independent reconstructions rather than claiming rediscovery as novelty.

Full proofs: proposals/independent_campaigns/horizontal_ratio_slope_director_round5.md; audits/adversarial_reviews/horizontal_ratio_slope_skeptic_round4.md; proposals/independent_campaigns/horizontal_ratio_slope_equivalences_round4.md. The independent proof attempts were derived before reading one another's completed drafts. Their common underlying source definitions and the director's proposed formula are explicitly acknowledged.

A precise further problem is an effective remainder for J_epsilon=C epsilon+o(epsilon) under explicit quantitative spacing/multiplicity hypotheses, with all large-height tails retained. No such rate, computable uniform threshold or publication-readiness determination is supplied here.
