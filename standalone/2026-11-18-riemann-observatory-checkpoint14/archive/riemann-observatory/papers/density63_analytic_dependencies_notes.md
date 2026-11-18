# Analytic dependencies for zero counts, values and universality

The ledger records the consulted edition and a located mathematical statement for each work. The arXiv records cite a pinned PDF and its submission history. Publisher-side information, where verified, identifies a separate manifestation. The classical records identify the scanned journal edition. The results are scoped to the statements and hypotheses of those sources.

## Complete edition readings

### Johan Andersson, Lavrent′ev approximation and universality

Read all five pages of arXiv:1010.0386v1. Theorem 1 takes a continuous target on a compact set of empty interior and connected complement. Lavrent′ev first gives a uniform polynomial approximation. The proof moves each of its finitely many roots into the complement by an arbitrarily small perturbation. The perturbed coefficients converge, hence the perturbed polynomials converge uniformly on the compact set. For a zero approximant the same conclusion follows by choosing a small nonzero constant.

Theorem 2 applies classical universality to the resulting nonvanishing polynomial with half the error budget and uses the other half for uniform approximation to the original target. Corollary 1 takes a vertical segment. Corollary 2 takes ζ itself as the continuous target on the prescribed compact set. The paper explains that Bagchi's implication to RH needs contours enclosing interior zeros for a Rouché argument. The theorem here imposes empty interior, even for examples of positive planar measure, so it does not supply that implication. The final remark identifies the same polynomial-approximation step in joint and Selberg-class universality.

### Christoph Aistleitner, Kamalakshya Mahatab and Marc Munsch, extreme values at σ=1

Read all seven pages of arXiv:1703.08315v2. Theorem 1 gives a lower bound on the maximum on [√T,T] for each sufficiently large T. The comparison conjecture concerns the shorter interval [T,2T] and an asymptotic equality. Lemma 1 imports a finite Euler-product approximation, uniform for T^(1/10)≤|t|≤T. The proof sets X=(log T)(log log T)/6, takes q_p=1−p/X for p≤X, and extends the coefficients completely multiplicatively.

Equations (3)–(8) give a pointwise resonator bound and estimate the Gaussian-weighted tails. The denominator has a lower bound from the diagonal. Fourier positivity in (9) permits dropping the ζ Euler-product primes above X. For each k in the truncated Euler product, retain m divisible by k in the double resonator sum. Writing m=kr and using q_kr=q_kq_r gives exactly q_k times the same Gaussian denominator. The quotient is then bounded below by the product in (10). Mertens’ theorem and the estimate for the second factor give e^γ(log₂T+log₃T) up to bounded error. The symmetry under t↦−t and the tail bounds permit restriction to positive t on [√T,T], where Lemma 1 transfers the estimate back to ζ. The concluding remarks explain why the multiplicativity and coefficient positivity matter for the argument.

### K. Soundararajan, conditional moments

Read all eleven pages of arXiv:math/0612106v2. The theorem bounds the measure of log |ζ(1/2+it)|≥V in three V ranges on [T,2T], assuming RH. Corollary A integrates the tail against 2k exp(2kV), giving the upper bound T(log T)^(k²+ε) for fixed k>0 alongside a previously known lower bound. Corollary B derives a logarithmic measure asymptotic for exceeding (log T)^k. Corollary C applies the proposition directly with a short cutoff.

In §2 the integrated Hadamard logarithmic derivative gives a negative term involving the nonnegative zero sum F(s) under RH. Lemma 1 obtains a smoothed explicit formula by shifting a contour and collecting the pole, zero and derivative terms. With σ₀=1/2+λ/log x, the remaining F coefficient in (7) is nonpositive for λ≥λ₀, where exp(−λ₀)=λ₀+λ₀²/2. Section 3 bounds the prime-power contribution and splits the prime sum into two ranges. The k-th power of a Dirichlet polynomial has support bounded by x^k, diagonal coefficients are estimated by a multinomial sum, and the off-diagonal logarithmic denominators are controlled when x^k≤T/log T. Markov bounds at separately chosen k for the two prime ranges give the tail theorem. Section 4 sketches related GRH bounds for primitive Dirichlet characters, quadratic characters and quadratic elliptic-curve twists. The quadratic-family prime-square terms shift the centers in opposite directions.

## Access decisions

The six candidate IDs with unrelated PDF titles were excluded. The author-hosted Lemke Oliver–Thorner PDF was treated as another manifestation of the arXiv work. The Göttingen PDF resolved to the entire journal volume, so it was excluded as an unconfirmed article match. The classical fetch log preserves unsuccessful attempts at Math-Net.Ru and journal delivery endpoints. These outcomes describe the attempted endpoints. 

The source directory retains the accepted primary PDFs, primary bibliographic receipts where available, discovery logs, and hashes. The initial arXiv receipt files include excluded candidates and describe the earlier fetch. The final ledger controls inclusion and level.

## Corpus reconciliation

The ledger contains 45 distinct works, with three whole-edition Level 1 readings and 42 targeted Level 0 readings. Checks used DOI, the base arXiv identifier and normalized title against the bibliography and every sibling paper-record shard. Six near-title matches were examined. Ford's zero-free region paper and the modern Mossinghoff–Trudgian–Yang paper are separate works. Soundararajan's moments paper and Conrey–Gonek's high moments paper are separate works, as are the Montgomery–Vaughan and Bombieri large-sieve articles. Andersson's Lavrent′ev and Mergelyan papers concern different compact-set hypotheses. The two Matomäki–Radziwiłł papers and the two Matomäki short-interval almost-primes papers are separate installments.

The [selection receipt](../sources/density63_analytic_dependencies/final_selection_receipt.json) identifies the screening outcomes. The [hash manifest](../sources/density63_analytic_dependencies/SHA256SUMS) covers the retained PDFs and bibliographic receipts. Crossref rate-limited some publication-counterpart requests. Those rows describe the verified primary-source manifestation and, where available, the DOI linkage reported by arXiv.

## Short-interval universality dependency

Andersson's Theorem 1 in arXiv:2312.04255 states the lower endpoint T^(1273/4053). Its equation (3) invokes the mean-square estimate for U=T^(1273/4053+ε) from reference [4], the Bourgain–Watt perturbed-cones paper published as DOI 10.1093/imrn/rnx009. The result is stated explicitly in §13 Theorem 3 of its pinned preprint arXiv:1505.04161v1. A separate work, arXiv:1709.04340, announces an improved exponent and was withdrawn in v2 on 2023-07-16. That withdrawal applies to the sequel. [Andersson source](../sources/density63_analytic_dependencies/anders_notes.pdf) · [Bourgain–Watt cited text](../sources/analytic64_statistics/bw_perturbed.pdf) · [Withdrawal receipt for the sequel](../sources/analytic64_statistics/bourgain_watt_withdrawal.html)
