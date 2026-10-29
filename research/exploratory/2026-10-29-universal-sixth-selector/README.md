# A universal low-slope selector and the joint-detector consequence

**Status:** The selector lemma and its scalar implications are proved below, conditional only on the prime ideal theorem and the ordinary zero-extended sextic symbol identities. The detector consequence is an implication: it assumes a proposed uniform joint-count extension and the source's detector-to-zero bridge. It is **not** a counterexample to that joint count, a zero-free-region theorem, or a statement about physical prime-only slots. No priority claim is made.

## Universal selector

Fix the Eisenstein field, a finite bad-prime set S containing the primes above 6, A>0, and a slope `0≤s<1/6`. Given any positive early mesh, choose once a fixed slot width `0<w<mesh`; choose a fixed positive width floor at most w. For each large Z set X=Z^w. There is an ordinary-ideal slot polynomial

    Q_Z(u) = Σ_{I∈𝒮_Z} a_I χ_I(u)

whose source ideals are nonzero, S-good and have norms at most X; its coefficient squared mass is exactly one; and for **every** nonzero row u with `Nu≤Z^A`,

    |Q_Z(u)|² ≥ X^s.                                    (1)

This includes arbitrary sixth-power-free rows, every fixed ray class, and all source coprimality zero masks. It is uniform over the row set, which may be selected later. The construction's sources are sixth powers of prime ideals, not physical prime ideals.

**Proof.** Set `R=(X/64)^(1/6)` and take all S-good prime ideals p with `R≤Np≤2R`. Their number n satisfies `n≫R/log R` by the prime ideal theorem. Put source `I=p^6` with coefficient `1/√n`. These ideals are distinct, `NI≤X`, and the squared coefficient mass is one. The sextic character and its zero extension give the exact identity

    χ_{p^6}(u) = 1 if p∤u, and 0 if p|u.

At most `A log Z/log R` primes of this annulus divide u; with w fixed this is O(A/w) uniformly in u. As n→∞, for all sufficiently large Z it is at most n/2. Thus

    Q_Z(u) ≥ √n/2,  |Q_Z(u)|² ≥ n/4 ≫ X^(1/6)/log X.

The last expression exceeds `X^s` because `s<1/6`. The slot, its width and coefficient mass meet the source interface for every fixed finite bad set and every sufficiently large Z. The width may be chosen after the supplied mesh, while the width floor and the slot count N=1 are fixed before Z grows, as in PR93's quantifier order. □

Taking all good primary sixth-power-free rows with `Nu≤Y=Z` gives `≫Y` rows by their positive ideal density; even just prime rows give `≫Y/log Y`. Therefore the unit-source component of any putative all-source selected-norm estimate

    selectedNorm(F,Sources) ≪ Z^ε(L+Y^(1−s)L^s)

already fails for this selector and `Sources={1}`, `L=1`, whenever `0<s<1/6` and `ε<s`. This strengthens the earlier prime-row obstruction by making the selector work uniformly on *every* row. At s=0 the same construction supplies the subsequent joint-count implication, but it does not contradict the trivial unit-source exponent one. Nothing here contradicts the actual PR93 norm theorem, which assumes slope above one half.

## What an unrestricted joint extension would imply

Set `ν=2a−1`, and let `s` denote the squared selected-slot slope. The three-word joint-count exponent in PR93's `WordCount.lean` is

    R_J(ν,s) = 3(1−s)(1−ν)/(3−ν−2s).                   (2)

Suppose a proposed extension applies this bound uniformly to *every* row satisfying the detector conditions and the broad ordinary-ideal aggregate selection condition, at some fixed `0<s<1/6`, with the same source masks, norm range and fixed-width order above. The universal selector makes that additional condition true for the **entire** detector family. Consequently such a joint-count theorem, together with the usual source bridge from zeros at `Re ρ≥a` to detected rows and with its stated height and small-power losses, immediately gives an **unmarked** row zero-density bound with exponent `R_J(ν,s)`. This conclusion is not an impossibility: a sufficiently strong new zero-density theorem could supply it. It shows the proposed broad-source joint count cannot obtain a low-slope gain merely from the slot selection hypothesis.

For comparison, the unmarked separate inverse/plain moment balance used by [Xu–Sang §6](https://arxiv.org/html/2610.17675v2) gives

    R₀(ν) = (15−16ν)/(15−6ν),    a=(1+ν)/2,             (3)

within its stated range. The hypothetical joint exponent improves this particular unmarked bound exactly when

    s > 2ν²/(18ν²−31ν+15),                               (4)

provided `0<ν<3/4` and `0≤s≤ν`; the denominator in (4) is positive on this range. This is an algebraic comparison with (3), not a claim that (3) is the strongest known density theorem in every family.

At the rational proxy for the new PR94 numerical bottleneck,

    ν=297617/1000000,       p=61939/1000000,
    s=2νp=18434099363/500000000000≈0.036868198726,
    a=1297617/2000000=0.6488085,

we have `s<1/6` and the threshold in (4) is approximately `0.02404261884`. Consequently

    R_J ≈ 0.7720559355,
    R₀  ≈ 0.7747765337,
    R₀−R_J ≈ 0.0027205982.

Thus an unrestricted ordinary-source joint count at this single bin would already require a zero-row density improvement of about 0.00272 in the exponent over the unmarked source balance, before obtaining any leverage from the selected slot. These rational values are a proxy for the floating-point bottleneck in [the exploratory return scan](../2026-10-29-arvi-return/hypothetical-joint-landscape.md), not a certified location of a global maximum.

## Where the original proof needs more

In PR93, `supported_witness_fiber_count` in `FineDetectorCount.lean` uses `SelectedAllSourceNormBound` to bound three detector words of lengths r, 2m and r+m; `wordEnvelope` and `count_word_min_le` then yield (2). The `SelectedAllSourceNormBound` is the substantive operator input: the universal selector shows that its desired all-source form cannot hold below one sixth, already at the unit source. The numerical word geometry is a separate issue: the compiled lemmas assume `1/2≤s≤ν`, and extending those algebraic and buffered losses to this range also requires proof. Even after that algebra, a detector-specific substitute for the false broad operator bound, stronger unmarked moments/density, or a genuinely physical prime-slot joint estimate is necessary. The lemma here does not address any of those narrower possibilities.

## A fixed scalar point just below one sixth

The old PR94 branch alone also gives an exact obstruction to the illustrative `0.001` target when the hypothetical new joint branch is allowed only for `s≥1/6`. This is a conditional scalar comparison inside the candidate geometry, not a statement about actual zeta zeros or alternative physical faces.

Use `theta=43643617/50000000=0.87287234`, `h=4/5`, the formulas in [the hypothetical landscape](../2026-10-29-arvi-return/hypothetical-joint-landscape.md), and the rational point

    ν=313264/1000000,  p=266015/1000000,
    s=2νp=1041661537/6250000000=0.16666584592 < 1/6.

Every one of the 31 imported non-old PR94 source windows has lower p bound at least 3/8, so at this point their guards do not make a branch available. With `d=h+10^(−10)`, the old count and the unchanged physical conductor edge have exact row excess

    6126846623895440724696345220996823334100321 /
    43091984449575605704331250000000000000000000000
      ≈ 0.000142180656 > 0.

The calculation uses the exact rational old-count normalization, the physical constants and cap in the landscape note, and sets the row reserve to zero, which is favorable to the proposal. Thus the target cannot pass this point by adding (2) only at slopes `s≥1/6`, if the other branches and this geometry are retained. A different count, a different physical face, or changed geometry could remove this particular obstruction.

**Independent scalar review:** A second researcher independently recomputed the sub-one-sixth point, physical conductor capacity, source-window exclusions and exact positive excess.

## The exact three-word replacement at low slope

The scalar part of PR93's joint detector does extend to low slope; it is the operator premise, not this algebra, that fails for the universal slot. Let `0≤s≤ν≤3/4`, and set

    D=3−ν−2s,  ℓ=2(1−s)/D,  h=3(1−s)/D,
    E(w)=max{(1−ν)w, (1−s)−(ν−s)w}.

Then D>0, ℓ≤1≤h, and `E(w)≤R_J(ν,s)` for every `ℓ≤w≤h`: the two endpoints are exactly where the corresponding affine terms equal R_J. If `0≤r≤1`, `0≤m≤1/2`, and `r+m≥1`, at least one of `r,2m,r+m` belongs to `[ℓ,h]`. Indeed, if r≥ℓ use r; otherwise if 2m≥ℓ use 2m; otherwise `1≤r+m<3ℓ/2=h`. This is the proof of PR93 `count_word_min_le`; its argument named `_hδ : 1/2≤δ` is not used. The scalar bound is sharp for these relaxed witness constraints: take r=ℓ and m=ℓ/2, so the three lengths are ℓ, ℓ and h, and all three envelopes equal R_J. With buffered lengths, `E` is 1-Lipschitz throughout this enlarged parameter range, so the source's small O(ε) losses remain O(ε), with adjusted constants.

For a fixed detector witness fiber, write its three **actual normalized** source words as `M_r`, `S_m²` and `M_r S_m`, at lengths `w=r,2m,r+m`. The detector lower bounds give respectively squared magnitudes at least `U^{νw−o(1)}`. Thus it is sufficient for the joint count to prove, on selected rows, at the row-dependent witness points and with the source's uniform profile/height losses, the three restricted moment estimates

    Σ_selected |D_w(u)|² ≪ U^{max(w,1−s+s w)+o(1)}.       (5)

Equivalently, one must establish uniform fixed-frequency/zero-real-part estimates and the required profile derivatives, then apply the source's Sobolev bridge to the row-dependent witness points; a single fixed-point estimate is insufficient. Constants and the early-mesh/height quantifier order must be retained. Chebyshev gives exponent E(w), and the scalar argument picks one word. One may weaken (5) further to an appropriate disjunction: it suffices that at least one word whose length lies in `[ℓ,h]` obeys the stated estimate. This is a *detector-specific* moment target, not a claim that the moments hold. It avoids asking for an operator bound on every coefficient vector, so the unit-column counterexample does not itself refute it.

The universal selector nevertheless makes any version of (5) uniform over all broad ordinary-ideal slot polynomials an estimate with the slot condition removed. If (5) is asserted only for detected witness fibers, the zero/detector restrictions remain; if it is asserted on arbitrary selected row sets, it becomes a genuinely all-row unmarked moment estimate. At the rational bottleneck above, `ℓ≈0.73279672`, `h≈1.09919508`, and `R_J≈0.77205594`. For w<1, the power required on the right of (5) is strictly below U; for w≥1 it is U^w. Existing unmarked inverse and plain-moment upper bounds do not directly provide this three-word statement. Establishing the appropriate moment or disjunction, exploiting actual coefficient signs and correlations, would be a genuine new analytic input; the physical prime-slot problem may have additional structure unavailable to the universal selector.

The standard sixth-order large sieve alone does not supply (5) for these lengths. Even with sixth-power-free rows and columns, for an unrestricted coefficient vector of length `B=U^w` its bound contains

    U + U^w + U^(5/6+w/3) + U^(1/3+5w/6).

When `w<1`, the first term is U but (5) asks for `U^{1−s(1−w)}`. When `1≤w≤h<2`, the last term exceeds the required U^w by the positive exponent `(2−w)/6`. Even with sixth-power-free source indices, the latter off-diagonal term remains in the sharp squarefree large sieve. This is a limitation of applying that general upper bound to the detector word, not a lower bound for the actual Möbius or plain coefficients and not a refutation of (5).

**Independent three-word review:** A second researcher checked the covering, envelope identities, 1-Lipschitz bound, detector word forms and sieve exponents. The row-dependent witness/Sobolev requirement above remains an essential hypothesis.

The exact rational comparisons can be reproduced with `python research/exploratory/2026-10-29-universal-sixth-selector/check.py`.

**Independent selector review:** A second researcher checked the uniform annular-prime argument, source masks and quantifiers, joint-to-unmarked implication and its limitations, and the rational calculations.

The all-row form of the plain-square estimate in (5) is in fact false at the bottleneck length: the independently reviewed [plain fourth-moment lower bound](../2026-10-29-plain-fourth-lower/README.md) proves `Σ|S_m|⁴≫U/log²U` for `m<5/12`, contradicting the proposed power below U. It uses trivial twist and a nonnegative smooth profile, both allowed in a uniform all-row formulation. This does not settle an estimate restricted to detector-zero witness fibers, or a disjunctive bound supplied by one of the other words.
