# Two quintic pair-Grams can align at the one-pair bound

**Status:** An exact finite character-matrix obstruction to proving a stronger quintic bound from the individual pair-Gram norms, positivity, diagonals, ranks, or Schatten data alone. It is not a counterexample to the arithmetic quintic sieve or to a stronger estimate using actual prime-ideal structure, coprimality and reciprocity.

For a full fifth-free label `g=a₁ a₂² a₃³ a₄⁴`, after removing pairwise-coprime row restrictions by positivity the q-column vector splits as the tensor product of the `(a₁,a₄)` and `(a₂,a₃)` group vectors. Its column Gram is the Hadamard product

    G=G₁∘G₂,
    G₁(q,q')=Σ_{a₁,a₄} χ_q(a₁)χ̄_q(a₄)
                       overline[χ_q'(a₁)χ̄_q'(a₄)],
    G₂(q,q')=Σ_{a₂,a₃} χ_q(a₂)²χ̄_q(a₃)²
                       overline[χ_q'(a₂)²χ̄_q'(a₃)²].

Both matrices are positive semidefinite. The Schur-product inequality gives `||G||≤min{||G₁|| max_q G₂(q,q), ||G₂|| max_q G₁(q,q)}`, recovering the method that freezes one pair. The following model attains that bound and also respects the formal `χ²` relation between the two factors.

Fix v≥1 and set `k=5^v`, `U=k²`, `Q=U`, `X=U²`. Let V=F₅^v, with fixed nondegenerate bilinear pairing, and index the Q columns by pairs `(t,j)∈V×V`. For a∈V put

    χ_(t,j)(a)=exp(2πi⟨t,a⟩/5).

The j index intentionally duplicates each t exactly k times. Let each pair-row set be V×V, so it has U rows. Define

    B₁[(a,d),(t,j)] = χ_(t,j)(a) overline(χ_(t,j)(d)),
    B₂[(b,c),(t,j)] = χ_(t,j)(b)² overline(χ_(t,j)(c)²).

Every entry is a fifth root of unity, and the second factor is exactly the square of the same underlying character family. Character orthogonality gives

    G₁=B₁*B₁=U · (direct sum of k copies of J_k),
    G₂=B₂*B₂=G₁,
    G₁∘G₂=U² · (direct sum of k copies of J_k).

Here J_k is the k×k all-ones matrix. Thus each G_i has diagonal U and norm Uk=U^(3/2)=X^(3/4), while

    ||G₁∘G₂||=U²k=X^(5/4).                                  (1)

At Q=U=X^(1/2), the source-conditional effective-order-five pair sieve allows exactly this size: its balanced pair bound is `U+U^(1/2)Q+U^(4/5)Q^(2/5)≍U^(3/2)`. The full-family one-pair estimate `X+X^(3/4)Q` is likewise ≍X^(5/4), matching (1). Consequently the source pair norm, positive semidefiniteness, exact constant diagonals, and even the complete spectra of the two pair Grams are compatible with no gain from their Hadamard product. The example already incorporates fifth-root phases, the (a,d)/(b,c) product pattern and powering by 2; it does not model the arithmetic indexing of distinct prime ideals, the physical zero constraints, or forced coprimality masks.

At σ=4/5, the source-conditional full fifth-free density proof has exceptional exponent 19/20. The point Q=X^(1/2) is exactly where its normalized inverse and ordinary witness moment bound reaches X^(5/4); the abstract model above shows that merely combining the two existing pair-sieve operator norms cannot reduce that input. An improvement would require a result sensitive to arithmetic correlations between the two powered character systems, their index multiplicities, or the detector's specific rows/coefficients. No assertion is made that the constructed degenerate q-columns occur in the number-field family.
