# Independent review of the all-order overlap and local-adapter proofs

**Verdict:** PASS for the explicitly conditional reductions and finite identities below. No mathematical correction identified. This review does not prove the short-row moment, independently validate the imported quasi-Riemann manuscript, or certify a zero-free region.

## Frozen files reviewed in full

1. `standalone/2026-10-10-generalized-inverse-moments/HYPERGRAPH_REDUCTION.md`
   SHA256: `e22637f2378adf35768d62b1270eb63615cc1c3058faae976e3d28d2f0bf9dac`.
2. Working companion `analysis_theta_closure.md`
   SHA256: `c718a99f031ba4ac1d636eb3f13f3592ab9ff30c35cd38c40bd94663a6ff6c5b`.

The hashes bind the contents read for this review. Renaming an unchanged file does not change its content scope; substantive edits require another review.

## 1. Hypergraph decomposition

The assignment of each occurring prime to its exact nonempty incidence subset is bijective. Prime ideals appearing in one factor form singleton columns; all other prime ideals form pairwise-coprime squarefree overlap ideals. The decomposition preserves the Möbius signs, multiplicative character factors, and the exact scale of every original smooth test.

The support conditions are sufficient and correct. A nonzero singleton term requires `X_i >= 1/b`, including the allowed range `1/b <= X_i < 1`. No appeal to fractional ideal norms is made. Every overlap ideal satisfies `Nq_I <= bD`, and

\[
NQ\le\prod_I(Nq_I)^{|I|/2}
=\left(\prod_iNc_i\right)^{1/2}\le(bD)^{k/2}.
\]

Unit ideals and the empty overlap family for `k=1` are included correctly. When an overlap has cardinality divisible by six, its row factor remains a coprimality mask; it is not replaced by the constant one. All external factors are contractions only after passage to the row norm.

Minkowski gives the claimed normalization. The pair-overlap factors have weight `(Nq)^{-1}` and contribute one harmonic logarithm each. There are exactly `binom(k,2)` such factors. Every larger overlap has exponent at least `3/2`, so extending its sum to all ideals is legitimate and gives a convergent Dedekind zeta value. Squaring gives the stated `log^{k(k-1)}` loss; for each fixed `k` this is absorbed by an arbitrarily small power of `D`.

The required singleton hypothesis is explicitly stronger than independent smaller-scale moments: it uses the same ambient row set and the same ambient `D` for every rectangle and moving exclusion. The proof does not silently enlarge a proven smaller row range. No uniformity as `k` varies is asserted.

## 2. Moving exclusions and fixed small primes

The multivariable formal reciprocal of `1-z_1-...-z_r` gives exactly the displayed multinomial coefficients. After smoothing, its operator identity is finite because nonzero shifted terms satisfy `Nd_i <= b_iX_i`. All norm phases factor through complete multiplicativity and remain contractions, including at row primes where the phase is zero.

After excluding the finitely many primes with `Np <= 4r^2`, the local weighted norm series converges and has exact sum `(1-r/sqrt(Np))^{-1}`. The product over an arbitrary moving squarefree ideal is bounded by `(Nc)^delta` times a fixed constant: sufficiently large prime factors are bounded individually, and the finitely many remaining factors are absorbed into that constant. This is genuinely uniform in the moving ideal.

The small-prime restoration is finite. In singleton columns each such prime is assigned either to no factor or to exactly one factor; a prime in the moving exclusion must be absent. There are at most `(r+1)^{|P|}` assignments. The resulting smooth tests are evaluated at smaller rectangular scales already covered by the hypothesis. Terms below the support floor vanish. Thus no divergent small-prime geometric series is needed.

An optional wording improvement in the main hypergraph note is to call the original set `S_0` and the enlarged set `S_k` explicitly. The unmasked analytic hypothesis must be assumed for the fixed enlarged set; it is not deduced by discarding a small-prime mask from a signed sum. The companion already states this distinction accurately.

## 3. Euler correction and conditional equivalence

The local coefficient of the correction

\[
\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
\]

is `1-|supp e|` for a nonzero multi-index. Hence all one-coordinate terms vanish, and the absolute local coefficient sum is `1+O(q^{-1-2delta})` on `Re(s_i)>=1/2+delta`. Absolute and locally uniform convergence, including coefficient summability, follows.

For the reciprocal correction, removing the fixed small primes makes `sum_i|z_i|<1/2`. The given geometric expansion is valid, starts in total degree two, and gives the same summability. The nonnegative-integer interpretation of the reciprocal coefficients is sound: inclusion–exclusion over distinct designated positions gives exactly the displayed factorial formula. It is not needed for the norm equivalence.

Both finite smoothed convolution identities preserve the row and the test functions. The common ambient polynomial bound on all scales permits the loss from replacing exponent `1/2` by `1/2+delta` to be absorbed into `D^epsilon`. The same argument works in both directions. Thus the conditional equivalence is proved, but neither side is supplied by the local Euler algebra.

## 4. Source-interface check

The imported October 5 source was checked directly at `eq:initial-scales`, `prop:canonical`, and `eq:initial-positive-gap`. Its initial column-auxiliary product is `Sigma=XF`, and its canonical proposition requires `H_dual <= Sigma D^{-kappa}` with a fixed positive gap. In the unsplit leading range, collapsing `r` factor scales of size `D` gives `Sigma=D^r` and dual row length of order `D^{2r}/H`. Their ratio is `D^r/H`. At the proposed `H=D^{1+theta}`, this fails the positive-gap condition for `r>=2`.

That source obstruction is correctly limited to reusing the existing descent after this collapse. It is not a theorem that every possible factor-preserving strategy must fail.

## Remaining analytic issue

The proof packet reduces the original moment to a correctly normalized unmasked rectangular singleton estimate, and relates that estimate to the actual correlated product moment. These are structural reductions. The required bound for the correlated nonprincipal arithmetic terms at `H=D^{1+theta}` remains unproved.
