# Independent review of the quartic Hilbert filter

Reviewed source raw SHA256:
`142fe3cfe5695c270de015f80b798daca17d18a86d651c0018be94b0d84f4f73`.

**No blocking issue found at the stated common-cover Hilbert and local Fourier scope.** The norm/damping construction and the period-cost observation were jointly developed in discussion; this receipt records a fresh reconstruction, not complete authorship independence.

I checked the following against the full displayed proof.

- Normalizing a finite-cover integral by its index makes rational pullbacks unitary: after changing variables, the numerator and denominator indices have the same ratio by equality of conjugate covolumes. This does not assume that the multiplier kernel is a congruence subgroup.
- On the subspace periodic under translations by lambda^4 O, the stated averages are orthogonal finite-group projections, and their products give the least-common-multiple projection.
- Suzuki's original full periodicity, visually inspected on printed page 114, gives the exact POINTWISE identity P_d theta=(Nd)^(-3/2)theta(d^4 z,(Nd)^2 y). The nonzero-mode normalization and the constant y^(3/4) both give precisely the same scalar. It follows that the norm square is (Nd)^(-3).
- The projection product and Gram formulas follow without a pure-tensor hypothesis. The local Toeplitz majorant gives the displayed finite synthesis constant. Inclusion-exclusion gives the exact hard-filter product 1/zeta_F^S(3).
- Nested valuation projections give block masses (1-q^(-3))q^(-3j). The positive damping spectrum therefore has the stated norm ratio and the cofinal Euler product zeta_F^S(3+2eta)/zeta_F^S(3). Monotone commuting positive contractions give strong convergence.
- The special local Fourier limit is established independently of a trace theorem. A fixed smaller positive height bounds the original Fourier amplitudes; the larger-height K-Bessel exponential then supplies a summable majorant for every fixed derivative. Bounded multipliers permit dominated convergence. A nonzero coefficient can be reduced to a fourth-power-free index by full periodicity, so this particular local hard limit is nonzero.
- Inverting the constant-term double cosets at zero Fourier index transposes the cusp indices and conjugates the unitary multiplier. Equal cusp widths and the real scalar K(0,s,0) give the Hermitian residue matrix used for the nonzero base constant. Its preservation under P_(p^j), together with norm decay q^(-3j/2), demonstrates the stated unbounded trace.
- The scalar radial change of variables gives q^(j(1-2s)); comparison with the product of Hilbert norms gives q^(j(4-2Re(s))). It is a continuity warning, not a claim that a complete signed global period diverges.

The proof correctly keeps the cofinal vector separate from a fixed finite-level automorphic function, and separately constructs only the distinguished local Fourier limit of this explicit sequence. It does not supply a squareclass selector, a root angular character, a normalized genuine quadratic Eisenstein period, or a new reciprocal-zeta estimate. Those remaining gates are essential.

Final-source refresh: publication target is `quartic/COFINAL_HILBERT_FILTER.md`.
I additionally reconstructed final Section7. On nu=nu_a*m^2, m=d^2*r with
r squarefree and all shared primes retained, floor(v_p(nu)/4)=v_p(d)
outside the fixed deleted set. Damping eta/2 in each field therefore
shifts only the replica numerator to L(2s-1+eta,epsilon^2). At eta>=1
it is Euler-nonzero for Re(s)>1/2. This proves the stated meromorphic
arithmetic pole retention; it does not prove continuation/holomorphy of
a global weighted period or exclude any zeta zero.
