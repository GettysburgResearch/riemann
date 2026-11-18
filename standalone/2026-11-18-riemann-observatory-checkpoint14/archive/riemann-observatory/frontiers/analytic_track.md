# Analytic frontiers inspected in this checkpoint

Literature search date: 17 November 2026. These are verified source statements and scoped reconstructions, **not** a claim to exhaust all latest literature.

| Program | Source result inspected | Exact obstacle | Useful next step |
|---|---|---|---|
| Large values/zero density | Guth–Maynard Thm1.1,1.2, arXiv v2; Annals203(2026) | S3 loss at the σ=7/10 envelope bottleneck; worst-case rational concentration | Reconstruct Prop9.1 sharpness examples at T1 scales before proposing a transplanted incidence estimate |
| Pair correlation without RH | BGSTB Lemma5 and Lamzouri Prop2.1/Lemma3.2 | Complex zero differences destroy termwise positivity, while global tensor positivity survives; bandwidth is limited | Make fixed-test error terms effective; track Q and Q'' separately |
| Critical-line proportions | Lamzouri2026 claims ≥0.6725007 simple critical, later Knausgård2026 claims ≥0.67353 | Single-window Montgomery–Taylor optimum; improvements need additional pair interactions or data beyond available statistics | Independently replay finite local-interaction certificates and audit exact theorem/axiom dependencies |
| Rigorous finite RH | Platt–Trudgian2020/2021: exact height3,000,175,332,800 | Certifying zero counts and numerical error bounds, then bounding an uninspected infinite tail | Reproduce a small certified segment and its Turing accounting; separately audit a tail-dependent arithmetic corollary |

## Historical transitions relevant here

Prime-counting via explicit formulas made the horizontal position of zeros an arithmetic problem; large-value/mollifier machinery then gave quantitative partial results rather than an all-or-nothing RH attack. Montgomery's correlations and later extremal windows reorganized multiplicity information statistically. The inspected 2023–2026 path removes RH from an analytic correlation identity, then replaces pointwise positivity by inertia or a tensor norm. This distinction is precise: an unconditional scalar correlation theorem does not make individual complex-zero summands positive. Computational verification also moved from floating-point detection to interval enclosures plus a completeness count. Formal proofs introduce another separate question: what was assumed about analytic inputs or a compiled finite search?

## A concrete failed theorem chain

Trying to feed Guth–Maynard Thm1.2 directly into BGSTB Thm3 fails at σ=3/4. The known density upper exponent is5/9, while BGSTB asks for little-o of exponent1/2. Better-than-old bounds are not automatically strong enough for a different paper's quantifiers. A moving endpoint σ=1/2+1/(2logT) adds uniformity requirements. No contradiction between the papers follows.

## Structural positivity obstruction

A nonconstant entire K cannot satisfy ReK(z)≥0 on all C: exp(−K) would be bounded entire, hence constant by Liouville; differentiating gives K'≡0. Therefore a proof that requires a nonconstant entire bandlimited kernel to be termwise positive for arbitrary complex differences cannot work under that premise. This does **not** prohibit positivity on a restricted strip, nor global positivity of a conjugation-symmetric sum. Lamzouri explicitly explains this obstruction on p5 and bypasses it through Prop2.1. Do not present this standard observation as a new result.

## Concrete research questions

1. For a fixed smooth positive even η supported strictly inside(−1/2,1/2), can the BGSTB remainder be bounded explicitly in a finite collection of norms of Q=η²*η² and Q''? This would turn Lamzouri's limiting statement into a computable finite-T certificate.
2. Can a kernel-checked finite certificate for local pair-interaction bounds be generated from a compiled branch-and-bound search without trusting the success axiom? The mathematical task is a compact exact witness and independent checker, not merely rerunning the same program.
3. At the GM bottleneck, what inverse theorem does near-saturation of the S3 estimate force on W and R(v)? State all scales, then test whether available incidence bounds rule out that structure. Random-set gains do not suffice.
4. Can effective constants in the independently repaired AF frame-operator boundary estimate be made explicit? The repaired bound justifies the displayed remainder asymptotically; see scoped review. Quantitative optimization is a research task, not an unresolved main-theorem objection.
