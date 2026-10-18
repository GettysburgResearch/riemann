# Internal review of the cofinal quartic filter

Reviewed source: intended publication file `quartic/COFINAL_HILBERT_FILTER.md`,
read from workspace `QUARTIC_HILBERT_FILTER_LATE_DRAFT.md`.
Actual raw-file SHA256:
`142fe3cfe5695c270de015f80b798daca17d18a86d651c0018be94b0d84f4f73`.

Outcome: no blocking mathematical error found at the stated imported-source,
normalized commensurator-Hilbert and distinguished local-limit scope.
This is internal team review, not external acceptance. I contributed the
replica-damping proposal and the cusp-trace warning in team discussion;
the checks below are a separate reconstruction of the complete written
argument, rather than a claim of blind or contribution-free review.

I checked the following.

- The normalized common-cover norm makes rational commensurator pullbacks
  unitary. Passing to ker(kappa) is legitimate without claiming that this
  kernel is congruence. The averaging operators are projections on the
  fixed original-unipotent-period subspace, not on an arbitrary function
  without that period.
- The good-prime additive pairing is nondegenerate. Hence `P_d` selects
  exactly `d^4 | nu`, and its constant-mode multiplier is 1. Its lcm law,
  self-adjointness and commuting property hold including shared primes.
- Full classical Suzuki periodicity, the `N(nu)^(1/8)` prefactor and the
  dilated radial height give precisely `P_d theta=(Nd)^(-3/2)T_d theta`.
  The constant term satisfies the same identity. This proves the exact
  norm, the gcd Gram matrix and the convergent Toeplitz synthesis constant
  `zeta_F^S(3/2)^2/zeta_F^S(3)` at their one-vector scope.
- The hard projection's norm product is `1/zeta_F^S(3)`. The geometric
  orthogonal block masses give the positive-damping product
  `zeta_F^S(3+2eta)/zeta_F^S(3)`. The proof uses the exact joint tail
  projections, so it does not assume an unproved pure-tensor factorization.
  Both cofinal strong-convergence arguments are valid.
- The explicit fixed-height Fourier-coefficient bound, K-Bessel decay
  and Gaussian-lattice counting provide a summable majorant for every
  fixed number of derivatives on compact subsets. Thus the particular
  local smooth Fourier limits are proved independently of any false
  general continuity of finite-component evaluation on the Hilbert
  completion. Full fourth-power reduction of a nonzero index proves
  nonvanishing of the hard local limit.
- The zero-frequency double-coset inverse argument justifies the
  Hermitian constant matrix used for the actual nonzero cusp trace.
  Its unchanged constant coefficient and shrinking `q^(-3j/2)` Hilbert
  norm show explicitly why the trace is unbounded. The radial scaling
  `q^(j(1-2s))` and resulting amplification `q^(j(4-2Re(s)))` are correct.
  Finite Fourier truncations must be transported by the same dilation,
  as the final text now specifies.
- In section 7, each field uses damping parameter `eta/2`. On the
  ALREADY SELECTED piece `nu_a m^2`, with `m=d^2 r` and all inputs
  prime to the fixed enlarged deleted set, the two multipliers give
  exactly `(Nd)^(-eta)`. The complete Euler ratio is therefore
  `L_F^(S_a)(2s-1+eta,epsilon^2)/zeta_F^(S_a)(s)`.
  For `eta>=1` its numerator is nonzero at every target zero with
  real part greater than 1/2, by an absolutely convergent Hecke Euler
  product. The fixed base coefficient is preserved. This proves pole
  retention for this arithmetic object, not its holomorphy.

The written limitations are necessary: no fixed finite-index invariance
of the cofinal local function, global squareclass selector, root angular
kernel, fixed bad-prime adapter, or weighted Eisenstein-period estimate
has been supplied. A new zero-free strip does not follow from the
unweighted Hilbert construction or from the initially convergent Euler
identity. These boundaries are stated in the reviewed text.
