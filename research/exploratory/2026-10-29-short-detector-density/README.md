# A conditional density gain from short saturated witnesses

**Status:** Proposed fixed-field density argument; source-conditional, with independent review requested. It uses the general-order conjugate-exponent sieve in [the companion note](../2026-10-29-conjugate-conductor-sieve/README.md) and a nontrivial extension of the buffered saturated detector below its printed t-range. No individual zero-free region or priority claim is made. The imported preprint lemmas, the fixed-field detector transfer and the uniform Sobolev step are not independently established here.

Fix n≥3, a number field K containing μ_n, its De Faveri good ideal set S and family, and one fixed unitary Hecke character ψ. Let `g=a b^(n−1)` with a,b good, squarefree and coprime, and use primitive inducing functions of `ψχ_g`. Subject to the two inputs just named, for every fixed `1/2<σ<1` and ε>0 there exists τ>0 such that

    Σ_{N(ab)≤X} N(σ,X^τ; ψχ_g)
       ≪_{K,S,n,ψ,σ,ε} X^{(7−6σ)/(6−4σ)+ε}.      (1)

Here the sum is over the stated squarefree-coprime pairs and N counts zeros with multiplicity. Equivalently the cutoff may be placed on the conductor of ψχ_g, with a fixed change of X: outside S and the fixed conductor of ψ, every p|ab appears in the primitive conductor. The exponent in (1) is below one whenever σ>1/2; good prime labels provide ≫X/log X distinct inducing characters. Thus all but O of the bound in (1) of those characters are zero-free in the rectangle `Re s≥σ`, `|Im s|≤X^τ`, and their proportion tends to one. This is a density-one family rectangle only, not an individual or unbounded-height zero-free region. For n≥4 the family contains only the two local exponents 1,n−1, not all n-th-power-free labels.

## A plain second moment

For a centrally normalized ordinary block of length D=X^m,

    S_m(g)=D^(−1/2) Σ_{j good} ψ(j)χ_g(j) W(Nj/D),

with a fixed smooth annular profile W, use the imprimitive presentation with all S Euler factors removed. Those deleted factors have no zeros in Re s>0. The rectangular sieve implies

    Σ_{N(ab)≤X} |S_m(g)|² ≪ X^{1+ε},  0≤m≤1/2.        (2)

The same holds with finitely many fixed ray twists, fixed finite unitary types, and differentiated common profiles, with the source's fixed polynomial height and seminorm cost. To prove (2), uniquely decompose each good index as `j=q r²` with q squarefree. For fixed r, the row-dependent factor `ψ(r²)χ_g(r²)` has modulus at most one and is **outside** the inner q-sum, even when q and r share primes; drop its modulus only after forming that sum. Partition the fixed finite reciprocity ray classes of g and q. Then the inner character is the source's `χ_q(a b^(n−1))` times a fixed column phase.

For a q-dyad of scale Q≤C D/(Nr)², its coefficient squared mass is `≪Q/D≪1/(Nr)²`. All q are squarefree and retain their zero masks. Partition a,b dyadically, remove their coprimality and product cutoff only when enlarging a nonnegative row sum, and apply the source rectangular sieve. Since Q≤C X^(1/2), its operator bound is `≪X^(1+ε)` by the calculation in the companion note. The L² norm of the fixed-r q-sum is therefore `≪X^(1/2+ε)(Nr)^(−1)` up to logarithmic dyadic factors. Minkowski over r costs at most `Σ_{Nr≪sqrt D}(Nr)^(−1)≪log(2D)`. Squaring and absorbing log factors proves (2). No row-dependent coefficient is placed inside the q-vector.

Uniformity in the witness's rowwise real exponent and common height is a separate source input: use fixed profiles with sufficiently many derivatives, insert the bounded logarithmic derivatives into the common q coefficients, and apply the finite-dimensional Sobolev reduction from [the detector Sobolev note](../2026-10-29-cubic-detector-sobolev/README.md). A single fixed-point moment does not suffice. Fixed S and original Euler zero masks are retained throughout, and all small powers, profile orders and τ must be chosen in that order.

## Short detector and scalar minimax

The source [OpenAI Proposition 8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) prints `1≤t≤3/2`. The required additional analytic input is its fixed-field/fixed-type extension to any **fixed** t∈[1/2,1], and, for σ≤51/100, the lowering of the source's printed bin floor to any fixed value strictly above 1/2. All constants may depend on that fixed gap from 1/2. Specifically, on a buffered bin of endpoint a with δ=2a−1>0 it must supply simultaneous witnesses

    0≤r, 0≤m, r≤t+O(κ), m≤1/2+O(κ), r+m≥t−O(κ),
    |M_r|²≥X^{δr−O(κ)},  |S_m|²≥X^{δm−O(κ)}.          (3)

All detector/bin losses κ>0 are fixed before X grows. The zero, finite presentation and separating frequency are common to both witnesses; the real-part and height variation must meet the Sobolev hypothesis above. No individual t depending on X is required.

The proposed extension follows the [fixed-field detector replay](../2026-10-29-fixed-field-saturated-detector/README.md): its truncated inverse can have length `D*=X^t` for t>0, the Möbius convolution still cancels every nonunit ideal of norm ≤D*, and the contour-shift upper bound on that finite polynomial is no larger than in the printed t≤3/2 range. The terminal cutoff, logarithmic Fourier separation, individual pointwise bounds and conclusion m≤1/2 are unchanged. These simultaneous short witnesses are a substantive source replay, not a consequence of the previously stated t=1 detector and not a theorem quoted verbatim; every profile, mask, rowwise-height and fixed-field functional-equation requirement must be verified before (1) is treated as proved.

Combine (2) with the companion inverse estimate

    Σ |M_r|² ≪ X^{max(1,1/2+r)+ε}.                      (4)

For a witness with r,m, Chebyshev gives the better exponent

    min{ max(1,1/2+r)−δr, 1−δm }.

Ignoring arbitrarily small fixed losses, take m=t−r; the worst case has `max(0,t−1/2)≤r≤t`. For r≤1/2 the worst exponent is `1−δt/2`, attained at r=m=t/2. For r≥1/2 both candidate exponents increase with r, so the worst occurs at r=t,m=0 and equals `min(1/2+(1−δ)t,1)`. Choosing the fixed

    t = 1/(2−δ) = 1/(3−2a) ∈ [1/2,1]

balances the two branches, with worst exponent

    1−δ/[2(2−δ)] = (4−3δ)/(4−2δ) = (7−6a)/(6−4a).  (5)

This expression decreases with a. A zero with real part ≥σ puts its row in a bin with `a≥σ−O(κ)`; finite binning and dyadic grouping absorb into small powers. Select κ first, then the source's polynomial height/profile orders, and finally τ so small that both the height cost and the standard individual zero-count factor are absorbed in ε. This gives (1) **if** the detector extension and source moment uniformity hold. At σ=4/5, (1) gives exponent 11/14≈0.785714, versus 9/10 from the inverse-only t=1 argument. □

This analysis does not use the false broad selected-norm bound at slopes below one sixth. It applies only to the explicit conjugate-exponent family and does not establish the short detector or the source preprints independently.

**Independent internal review:** Two researchers checked the good-index squarefree decomposition, coefficient mass and Minkowski sum, zero-mask placement, scalar minimax, and the fixed-loss/height order. They identified the printed source floor and `t≥1` as genuine extension hypotheses. A related [independent review of the cubic short-detector replay](../2026-10-29-short-cubic-conductor-detector/INDEPENDENT-REVIEW.md) is relevant but does not independently prove the general-order sieve or the fixed-field detector.

For ψ=1 and nontrivial labels, class field theory realizes χ_g as a finite-order Hecke character of exact order n, hence as a one-dimensional Artin character of a cyclic extension. On a rectangle symmetric in height, `L(s,χ_g)L(s,overline{χ_g})` is zero-free exactly when χ_g is zero-free there. Thus the same conditional exceptional bound applies to the corresponding two-dimensional Artin representations `χ_g⊕overline{χ_g}`; identifying a pair with its conjugate changes multiplicities by at most two. For n=3 this product is the relative quotient `ζ_L/ζ_K`. For n≥4 it need not equal the full relative quotient, because other powers of χ_g also occur in that quotient. This is the same density-one conclusion, not an individual Artin zero-free region.

For orientation against one general-family source, in the fixed Galois-field and finite-order-twist setting, [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3) gives at fixed or polylogarithmic height a conductor exponent `2 min(3/(2−σ),2/σ)(1−σ)` for all primitive ray characters. The locally ±1 labels above induce distinct characters: at every good ramified prime, the local character distinguishes exponent 1 from n−1 since n≥3; twisting by one fixed character preserves distinctness. Subject to both cited results, the short-detector exponent `(7−6σ)/(6−4σ)` is strictly smaller than that comparator for `1/2<σ<(47−sqrt(97))/44≈0.84434414`. At sufficiently small fixed power heights the strict comparison persists after including both height factors. This is only a comparison to the named general-family estimate, under its Galois and finite-order assumptions; it is not an exhaustive literature search or priority claim.

For n=3 over the Eisenstein field with the standard cubic-residue normalization and principal fixed twist, [rStation paper 52 v5, Theorem 5.7](https://rstation.ai/problems/riemann_hypothesis/papers/52) states the natural-index exponent `D(σ)=(8−7σ)/(3(2−σ))` for all `1/2<σ<1` and sufficiently small power heights. Conjugate-label reordering and its cumulative cutoff give conductor exponent `(3/2)D(σ)` by taking P=X^{3/2}; small indices are included in that single cumulative bound. At σ=4/5 this exponent is 1, versus 11/14 in (1). Indeed `(3/2)D(σ)−(7−6σ)/(6−4σ)=(1−σ)(5−4σ)/[(2−σ)(3−2σ)]>0` throughout the open range. The paper's separate dyadic Theorem 1 needs a small-index split to transfer a single conductor height, as described in [the review](../2026-10-29-cubic-conductor-density-review.md), and can be stronger in the higher strip. Theorem 5.7's analytic proof and inputs are not independently verified here.
