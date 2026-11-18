# PAPER-S001 — Riemann, 1859

**Identity.** Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, Monatsberichte der Berliner Akademie, November1859. Source read: David R. Wilkins, *On the Number of Prime Numbers less than a Given Quantity*, preliminary translation December1998, ten PDF pages including title; text numbered1–9. Canonical historical collection: https://www.claymath.org/collections/riemanns-1859-manuscript/ . Translation: https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf . DOI not established here. Read in English, not a claimed German-language audit. Access:2026-11-17. The source manifest records the exact downloaded file hash.

**Audit scope.** Level0 verified from full document and historical collection. Entire translation read substantively (Level1). No complete Level2 proof reconstruction: historical zero counting, canonical product, contour passages and ordered zero sums require later rigorous dependencies. No Level3 paper-wide audit. Reading Riemann is not certification of all historical proof details.

## Mathematical extraction

Riemann starts with ζ(s)=∑n≥1 n^(−s)=∏p(1−p^(−s))^(−1) in Re(s)>1 (p1). The gamma integral and a Hankel-type contour extend the function; the complex power uses the logarithm real on the negative x axis (p2). The gamma-completed expression is invariant under s↦1−s (p2–3). An alternative route uses ψ(x)=∑n≥1exp(−πn²x), the Jacobi transformation 2ψ(x)+1=x^(−1/2)(2ψ(1/x)+1), and splitting the Mellin integral at1 (p3). In modern notation ξ_mod(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2; Riemann's ξ(t) is ξ_mod(1/2+it), an even entire function.

On p4 Riemann states the reality of all zeros of ξ(t) as a conjectural belief and explicitly leaves proof aside. The approximate zero count Tlog(T/(2π))/(2π)−T/(2π) also appears there. It must not be silently upgraded to the modern fully quantified Riemann–von Mangoldt remainder based only on this paper.

For x>1 he uses the jump-averaged prime count F(x) and J(x)=∑m≥1F(x^(1/m))/m. With a>1 the inverse-Mellin expression is J(x)=(2πi)^(−1)∫_(a−i∞)^(a+i∞)(logζ(s)/s)x^s ds (p5–6), interpreted with the boundary half-values. He notes that termwise integrals after splitting logζ do not separately converge, and integrates by parts before proceeding (p6). Thus a proof attempt that interchanges the unsmoothed infinite zero sum and contour integral needs a separate convergence argument.

The explicit formula on p8 has main term Li(x), paired nontrivial-zero terms, a trivial-zero integral and constant logξ(0). The zeros are ordered; Riemann emphasizes the relevance of the summation order. Complex Li branches matter (p7). Möbius inversion recovers F from J (p8). The final numerical interpretation separates prime-power corrections from zero oscillations (p8–9); historical statements about Li(x) exceeding π(x) are not universal theorems supplied by this memoir.

## Proof dependency graph

Euler product (Re s>1) → gamma Mellin transform → contour continuation / theta functional equation → entire even ξ → zero information and canonical product (historically sketched) → inverse Mellin for logζ/s → controlled contour evaluation and paired zero sum → J(x) explicit formula → Möbius inversion → π(x).

## Reusable ideas and limitations

The Mellin–Fourier conversion y=logx is the precise reusable operation behind later spectral analogies, not merely shared terminology. The theta transform supplies both functional-equation symmetry and a rapidly decreasing real kernel. The conjectural reality assertion is unnecessary for writing a properly interpreted explicit formula with complex zeros; imposing it during derivation would be circular.

## Research question

Construct a single documented Schwartz/Paley–Wiener test-function convention that carries Riemann's inverse Mellin formula, a Weil explicit formula and a candidate graph trace formula into the same normalization. State exactly which test functions permit absolute prime-side convergence and which require a distributional limit. Then compare equality of distributions rather than finite plots of oscillations.
