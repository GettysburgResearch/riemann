# Scoped review of the mixed completion and spectral means

Reviewer: root AI agent, 2026-10-10. This is an independent mathematical reading of the listed agents' arguments, with exact source and normalization checks. It is neither formal verification nor external peer review. Imported theta and reciprocal theorems remain explicit premises.

## Frozen targets

| Target | SHA-256 |
|---|---|
| `MIXED_LABEL_COMPLETION.md` | `5e77ec88d6a191ec214bcedebc2b42d37f95735ba2bb18955b2f8a16aedfbcad` |
| `ALL_ROW_SPECTRAL_MEAN.md` | `ef597dfc793af976a92b731f01930fc199948e99d5ccf2fc3fe2c91ec5249a8b` |
| `OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md` | `b0d3eee6d32ad7f69bfdd8ac5132c60139f322b1102086897ce0099defab8551` |

The root authored the companion stratified inverse and helped derive the A2 cutoff. This report does **not** count as an independent review of those two arguments; separately assigned agents review them.

## 1. Mixed completion: supported at the stated premises

I compared the literal physical family and inverse with PR #918 at `cfa102748b26f840ccc4b963a660711424db0ec3`, the completed norm and all-row local adapter with PR #923 at `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, and the single-auxiliary reindexing with PR #921 at `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`.

The new conclusion is supported as a source-conditional estimate, with its precise outer-mask coefficient class. It must not be promoted to arbitrary angular coefficient vectors.

The simultaneous relabeling uses `q_* = q/(q,f)`. The fourth-power auxiliary twist already kills every physical factor meeting `f`, including the unrestricted cube factor after cubing. Thus overlap primes of `q` and `f` are redundant; the remaining sixth-power twist supplies the exclusion on all three physical indices. This is an equality of family values and does not permit replacing the physical row ball by a larger ball of height `H F^4 Q^6`.

I reconstructed the new exclusion-prime calculation. At zero physical valuation, effective exponent six has an inactive constant branch and an active branch with squared amplitude `p^-1`, reflected-length dilation `p^2`, and no extracted reflected-prime factor. Its three energy costs are bounded by `1, p, p^(1/3)`. In particular, an exclusion cannot be assigned only a subpower cost. At an auxiliary prime, effective exponent four uses all three source allocations. Keeping their length and amplitude shifts gives `1, p, p^(2/3)`. These are the exact costs needed in the theorem.

At positive physical valuations, the shifts by six and four are kept separately. Combining row-density factors with the three energy monomials gives summable or bounded local series. The finitely many per-prime factors contribute a divisor-type loss, while the powerful-row sums outside the moving labels retain the convergent local tails of the pinned all-row proof. None of this assumes that the row is coprime to either label.

The completed-group pruning uses the whole reunited Ramanujan character sum. It is applied before selecting an individual reflected allocation. The scalar retained after CRT is the canonical infinity type minus three, with the new labels appearing as fixed exclusions. The additional outer mask therefore fits the cited angular reciprocal operator; an arbitrary outer coefficient does not.

I also checked the finite inverse and long-tail grouping. The inverse index avoids `q f S`, but need not avoid the outer mask `r`. On regrouping `d=h b`, neither `d` being squarefree nor `(h,b)=1` may be inserted. The remaining raw inner squarefree variable may meet `d`. The exterior character phase, with its possible zero, is retained as a norm contraction only after fixing `d`. At the fixed physical cube-support cap, the long tail is exactly empty. These distinctions are essential for the subsequent stratified proof.

No blocker was found in the added mixed-label deduction. This review does not independently establish the automorphy theorem or the source-conditional angular reciprocal input, and it does not supply the centered signed two-column comparison.

## 2. Baseline spectral mean: all rows at a > 5/8

I checked the canonical coefficient and cube-Euler definitions against the physical completed sum and read the imported `paper2.tex` Proposition R, including its explicit all-row statement and its row-factor reduction. The result used here is the completed block energy `H + H^2 F/X`. Its row variable is not restricted to squarefree values.

For the classical alternative, the ordinary all-row sieve is applied separately for each fixed cube index. The zero phase on that cube is a norm contraction, and the coefficient `1/Nb` has only a harmonic loss on the base term. The other terms have convergent cube sums. This gives `H + H^(1/6) X + (H X)^(2/3)` without deleting the sixth-power-copy term.

The completed Dirichlet series is normally reconstructed on every strict half-plane `Re(u)>1/2` by summing its smooth physical blocks. Its cube Euler reciprocal is absolutely bounded there because its real exponent is `3 Re(u)-1/2>1`. The `d`-mask and every row-prime zero remain in this product. This transfers the Hilbert-space bound to the stated canonical raw spectral series.

The two block crossover calculations give row-norm exponents `1-11a/12` and `1-4a/5`. Their sufficient thresholds are `6/11` and `5/8`, respectively. The auxiliary exponents are at most `(1-a)/2`. Lower-endpoint sums and logarithms when their geometric exponent vanishes are included. Thus the strict-strip conclusion at `a>5/8` follows at the stated inherited inputs. It does not extend the exact reflected-series identity to all nonsquarefree rows.

## 3. Additional fixed-order sieve: a > 4/7

I read the primary version of Alexandre de Faveri's *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, especially Theorem 1.1 and the fixed-family and reciprocity conventions. The theorem is an external analytic premise. Its sixth-order specialization contains both mixed terms; it is not the bound `U+L` alone. The packet credits this dependence and retains the independent `5/8` baseline.

The all-row adapter preserves literal nonunit zeros. For fixed bad-prime part, unit and sixth-power factor, the latter supplies the column mask `(n,v)=1` before the sieve is applied. No coprimality between the sixth-power factor and the sixth-power-free remainder is assumed. Finite Kummer and ray-class partitions compare the fixed source family with the generator symbols; they do not vary the source's family constants. Summing the sixth-power factors yields the four-term envelope

`H + H^(1/6) X + H^(5/6) X^(1/3) + H^(1/3) X^(5/6)`.

I recalculated the crossovers against `H^2 F/X`. They are `H^(11/12) F^(1/2)`, `H^(7/8) F^(3/4)`, and `H^(10/11) F^(6/11)`. The corresponding row thresholds are `6/11`, `4/7`, and `11/20`. All auxiliary exponents fit the same `F^((1-a)/2)` norm envelope. The strongest restriction is therefore `a>4/7`. The lower-endpoint terms and the transition logarithms are controlled uniformly on the stated strict strips.

The final reflected-series corollary is explicitly restricted to the exact squarefree-row family already constructed in PR #922. Its divisor norm exponent is `(1-5a)/2 + tau`, whose ideal sum converges for `tau < (3a-1)/2`. The complete cusp coefficient mass and finite ray reunion are inherited source assumptions, not newly proved consequences of the scalar mean. A second reviewer was assigned specifically to compare this step against the pinned PR #922 identities.

Finally, I checked the stated non-improvement of the physical envelope. The limiting scalar is `11/14`, approached strictly, and the putative completion energy is `H D^(11/7)`. The elementary and classical comparison ranges `H <= D^(4/7)` and `H >= D^(3/7)` cover all heights. This spectral extension alone therefore supplies no new physical fourth moment or zeta zero-free boundary.

## Disposition

The reviewed deductions are suitable to include as proposed source-conditional research with their exact coefficient classes, strict-strip conventions, zero masks and credited external inputs. No claimed full Möbius moment, `17/24` zero-free result, cofinal hierarchy or proof of RH is supported by this review.
