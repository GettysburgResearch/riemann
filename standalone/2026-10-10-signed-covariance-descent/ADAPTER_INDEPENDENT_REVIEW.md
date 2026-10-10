# Independent review of the all-cusp coefficient adapter

**Reviewer:** signed_series_bootstrap, separate from the adapter author.

**Exact reviewed file:** `ALL_CUSP_COEFFICIENT_ADAPTER.md`.

**SHA256:**
`bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1`.

**Scope:** Sections 1–4 only: exact coefficient normalization, the
sector table, intrinsic cube scaling, fixed bad-prime decomposition,
and finite multiplicative character support. Section 5's quantitative
covariance composition is outside this review. A frozen-commit binding
is to be supplied in the packet validation record.

## Verdict

**PASS, with the stated source dependencies and scope.** The reviewed
sections give the needed exact canonical good-prime coefficient
structure at all three imported cusps. Their finite-character
conclusion assumes (4.1), exactly as stated; this review does not
replace the companion proof of that finite covariance.

The two small editorial corrections requested during review were
made before the hash above: the cube decomposition is stated for
supported Fourier indices, and the exponent of the angular cube
factor in (4.7) is correctly typeset.

The final file appends Corollary 5.1 outside this review's scope.
Removing that appended corollary and its preceding blank line exactly
recovers the previously reviewed 15,552-byte file with SHA256
`aaa40dceb950d32f795b5142e68637986678262663d5a63f8a0f4af4a034c69c`.
I checked this equality by SHA256; Sections 1–4 are unchanged. The
review is therefore rebound to the final 17,208-byte file above
without extending its mathematical scope.

## Independent reconstruction

1. I opened the primary Dunn–Radziwill source
   [arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3) and checked
   the explicit formulas (5.7), (5.13), (5.14), the representatives
   in (5.9), and the corresponding Appendix A entries. The two
   nonstandard representatives are exactly the source's gamma_10
   and gamma_19. This uses their unconditional coefficient formulas;
   no GRH-conditional prime estimate is imported.
2. I independently changed the trace additive character to the
   repository character. Since `breve-e(tz)=e(lambda t z)`, the
   substitution `y=lambda t x` gives
   `g(t,n)=sqrt(Nn) chi_n(lambda t)^(-2) gamma_2(n)`.
   The good indices exclude the nonunit cases. Every extra factor
   for the four relevant values of t is cubic and finite.
3. I reconstructed both nonstandard support substitutions and every
   scalar. The conjugation in `d_sigma(ell)=bar(t_sigma(-ell))`
   changes the conjugate Gauss sum to `gamma_2(n)`. Both tables
   give scalars `9(1,omega^2 zeta_9,omega zeta_9^(-1))` with the
   stated, different unit supports. For the standard cusp, the
   ninth-root conjugations give `(1,zeta_9,zeta_9^(-1))`.
4. I checked the uniform coefficient bound against both ramified
   progressions and the exponent -4 sectors. The first standard
   progression has equality in `27*3^(m/6)`; the others obey the
   displayed upper bound.
5. The intrinsic cube law includes overlap between the squarefree
   part and the multiplying cube. Multiplication by a primary cube
   changes only b to bc, preserving the unit and ramified sector.
   The nonstandard phase is unchanged because
   `c^3-1` belongs to `9O=lambda^4O`; multiplying a source Fourier
   index by this difference has integral trace.
6. Freezing the squarefree S-part contributes a fixed normalized
   Gauss scalar and a cubic reciprocity factor in the remaining
   good squarefree index. The unrestricted bad cube parts retain
   their norm weights and their local masks. Their fixed-prime
   geometric sums converge in the completed domains used by the
   subsequent argument.
7. I checked finite character orthogonality directly. Under the
   stated covariance `F(xy^3)=bar(rho(y))^3 F(x)`, a nonzero
   multiplicative Fourier coefficient at psi forces
   `psi^3=bar(rho)^3`. Absorbing each supplementary cubic factor
   preserves this cube. This yields (4.5) and the exact cube
   character in (4.7).

## Review boundaries

This is an independent mathematical reconstruction against the
identified contents, not a Lean proof or external human acceptance.
It does not validate the whole imported analytic manuscript. The
actual finite covariance, the new spectral mean, the shifted-variable
continuation, and the complete physical contour composition have
their own proofs and review scopes.
