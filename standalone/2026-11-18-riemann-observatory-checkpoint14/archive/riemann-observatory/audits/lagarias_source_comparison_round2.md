# Prior-source comparison for the Lagarias concavity campaign

Search/read cutoff:2026-11-17. No novelty or priority conclusion is asserted. The comparison uses actual mathematical sources, not their abstracts alone.

## MacArevey, arXiv:2602.15905v2

Andrew MacArevey, *On the Lagarias Inequality and Superabundant Numbers*. First submitted16February2026, v2 dated19February2026. The actual seven-page v2 was read in full. Local files: `sources/lagarias_compact/2602.15905.pdf` and `.txt`; identity/history saved from the arXiv abstract page.

Its continuous function is exactly L(x)=[H(x)+e^(H(x))logH(x)]/x, with H(x)=ψ(x+1)+γ. Thus it is the same profile whose logarithmic concavity is studied in our campaign, not merely a thematic analogy.

Precise claims:

* Lemma2.1 p2 gives L′(x)=N₁(x)/x², with N₁ the **first-derivative numerator**. This is not the negative second-derivative numerator N₂(h) used in the compact concavity certificate.
* Lemmas2.2–2.3 pp2–3 prove H′(x)≥1/(x+1) and log(x+1)≤H(x)≤1+logx.
* Lemmas2.4–2.7 pp3–5 reduce positivity ofN₁ to an elementary logarithmic inequality and e^t≥2t²+3t+1 fort≥4.
* Proposition2.1 pp5–6 proves L′(x)>0 for realx≥e^4.
* Corollary2.1 p6 proves L(n+1)>L(n) for all integersn≥1, invoking direct finite checks forn≤54. Those author checks were not independently replayed here.
* Theorem3.1 p6 shows the least Lagarias counterexample, if any, is superabundant: an earlier abundancy record has at least as largeσ(n)/n, while its smaller index has a strictly smallerL(n), forcing an earlier counterexample.

The elementary continuous proof was reconstructed without finding a problem in its stated large-x range. It contains no logarithmic-concavity theorem, no second-derivative analysis of logL(e^t), and no common-parameter global-maximizer endpoint interpolation argument.

The independent global concavity proof would imply continuous L′>0 even on1≤x<e^4: g″<0 and g′→0 at infinity giveg′>0 everywhere. This is a stronger calculus statement than the particular monotonicity proof in the inspected source. It does not establish historical priority, since other sources may already contain it.

## Hu et al., arXiv:2606.15096v1

Zhixin Hu, Tao Xu, Xiaodian Sun, Li Jin and Momiao Xiong, *VGPT-RSI for RH-Adjacent Formal Progress: Boundary Certificates, Verified Finite Lagarias Inequalities, and Explicit Failure Localization*, v1 submitted13June2026. The actual31-page PDF was accessed. This track read pp1–3,12–18 and20–28, including the Lagarias methods, finite-result descriptions, limitation statements and references. The boundary-curve derivation and all figures were not fully audited, so no whole-paper reading is claimed.

The relevant source claims are finite and formal-computational:

* §§2.5–2.6, pp12–17, describe finite Lagarias objects, harmonic lower bounds, interval inequalities, divisor-sum factorization certificates, chunk compilation and assumption checking.
* §3.6, pp21–23, reports the range1≤n≤10000 verified by ten1000-integer chunks, with Coq theorem names for the assembled certificate. The source reports a successful nonrecursive checker and a full recursive-check timeout while traversing dependencies.
* §3.7 p24 explicitly leaves the global tail beyond a finite cutoff unresolved and identifies possible reduction to colossally abundant or related extremal integers as a further mathematical task.

No associated formal artifact bundle was obtained or replayed in this track. Therefore “Coq-checked” remains a source-reported status in this record, not an independent certification of those files. Their finite inequality can be checked separately, but that would not validate their particular implementation or dependency audit.

No smooth-profile log-concavity theorem or common-ε endpoint interpolation theorem was identified in the inspected Lagarias sections. The symbolB(x,T) in the separate boundary-curve branch denotes a different function from the Lagarias envelopeB(x); the common letter supplies no mathematical connection by itself.

## Exact distinction from the independent campaign

Our calculus statement is g″(t)<0 for g(t)=logL(e^t), t≥0, proved by an analytic tail plus170 rigorous compact cells. Its arithmetic consequence requires **two endpoints maximizingσ(n)/n^(1+ε) for the sameε** and both satisfying Lagarias. Those hypotheses supply an affine support line that concavity puts belowg between the endpoints. Neither an arbitrary superabundant pair nor a pair supported by unrelated parameters supplies this line.

Thus the mathematical objects match MacArevey's profile exactly, but the logical conclusion differs from mere monotonicity and the least-superabundant-counterexample statement. The finite-certificate methodology overlaps Hu et al., but our compact certificate concerns a continuous derivative inequality and has an explicit portable integer-arithmetic replay. It is not a substitute for the unproved infinite arithmetic tail.

## Search limits and next provenance steps

Focused searches used combinations of Lagarias, harmonic/digamma, concavity, log-concavity, superabundant and colossally abundant. The above two exact primary papers were then obtained. No matching global concavity theorem was located in this limited search. Absence from these two papers and search results does not prove novelty.

The next backward source to inspect is MacArevey's reference1, Assani–Chester–Paschal, arXiv:2503.03159, concerning Robin and Kaneko–Lagarias inequalities. A broader priority review should also inspect smooth harmonic-function inequalities and classical colossally abundant interpolation arguments. No further constant optimization should be presented as research novelty before that comparison is complete.

## Backward check: Assani–Chester–Paschal2503.03159v2

The actual10-page v2 dated16August2025 was obtained. This track read the introduction, complete§3(pp7–9) and references, but not all Robin-family arguments in§2; PAPER-C110 is therefore a partial-reading record.

Proposition3.6 pp8–9 concerns K(x)=e^(H(x))logH(x)/x, **without the additive H(x) term** in the original Lagarias envelope. It states K increases forrealx≥4; Corollary3.7 supplies integer monotonicity; Theorem3.9 reduces least Kaneko–Lagarias counterexamples to superabundant integers. The introduction explicitly leaves an analogous original Lagarias result for future work. No logarithmic-concavity theorem was identified in§3.

A real-variable identity in the printed proof requires care. Equation(57) uses the standard integer identity H_n=logn+γ+∫_n^∞{t}/t²dt. The subsequent g_k(x)=e^γ logH(x)exp(∫_x^k{t}/t²dt) is asserted to tend to K(x) for realx. In fact

logx+γ+∫_x^∞{t}/t²dt=H_(floorx)+1−floorx/x,

which agrees with smooth digammaH only at integers in general. For example, atx=9/2 the left side is79/36, whereas H(9/2)=1126/315−2log2. Their difference is2log2−1739/1260>0, since log2>56/81 gives2log2>112/81>1739/1260. Thus that specific real-limit identification is invalid under the paper's smooth definition ofH. Equality at integer endpoints nevertheless suffices for the integer monotonicity argument described there.

Moreover, a direct argument repairs and strengthens the actual continuous conclusion. Forx≥1, H≤1+logx and

e^t>(1+t)log(1+t), t≥0,

because the difference has positive second derivative, zero first derivative at0 and value1 at0. Sinceh↦hlogh increases forh≥1, H(x)logH(x)<x. Also xH′(x)≥x/(x+1). Thus forx>1,

d/dlogx logK(x)=xH′(x)[1+1/(HlogH)]−1
> [x/(x+1)](1+1/x)−1=0.

Atx=1, K(1)=0 and the direct derivative is positive. Hence K is strictly increasing on the full real range x≥1 by this alternate proof. This is an independently reconstructed consequence of elementary harmonic bounds; no novelty claim is made. The paper's main discrete consequence is not refuted by the real-interpolation observation. The archive should preserve the corrected route rather than present a failed theorem.
