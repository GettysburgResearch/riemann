# Scoped internal review of growing residue debiasing

**Independent internal reconstruction; not external review.** Reviewed
`../eisenstein/GROWING_RESIDUE_DEBIAS.md`, actual file-byte SHA256
`1f3cecc2064ea1429b06dd94f1328c7e56de981219c9eebe927822da21a51f66`.
The imported fixed-field zero-free/vertical input and the source zero-slot
TWO-PLAIN theorem remain explicitly assumed source interfaces.

I found no blocking error at the stated component scope.

1. The smoothed prefix response follows by factoring out the squarefree
   label, using the absolutely convergent correction to the reciprocal
   zeta Euler product, and shifting the smooth Mellin integral. Its zero
   at one cancels the cutoff transform's possible pole at zero. The
   growing-label factor costs only a prescribed subpower.
2. The response matrix has the claimed uniform squarefree-sieve error
   for all least common multiples in the matrix. I reconstructed its
   exact gcd factorization and weighted divisor inversion. The normalized
   main inverse costs a subpower; the normalized error has Schur norm
   `O(D^(-1/2)G^(1+epsilon))`, so the entire growing matrix is invertible
   when `G<=D^(1/2-eta)`. The two coefficient resources and the pointwise
   divisor bound then follow by weighted Cauchy. No empirical singular
   value lower bound is being substituted for this argument.
3. For the analytic tail, extracting a fixed label costs its inverse
   square root. The squarefree positive series and its added coprimality
   Euler factors can be expanded with absolute central-line mass a
   subpower. The square index costs a harmonic logarithm. Applying the
   source TWO-PLAIN estimate after these expansions keeps the original
   common character and its zero values. Summing the complete label
   family before taking the final norm gives (7). In particular
   `beta=7/8,G=D^(1/5-eta)` has the claimed nonpositive power cost, even
   for the full polynomial cutoff `D=U^(3/2)`.
4. I checked the polar extension against the finite cusp calculation in
   `rstation-8-v1.md`, Section 5.1. The unit-cusp matrices, their
   multipliers, fixed-level periodicity and the finite cusp family remain
   valid when the good denominator has prime valuations one or two.
   Every nonunit primitive denominator then carries a nonprincipal unit
   character, so its constant term sums to zero. The unit denominator
   alone contributes density `1/N(aR)`. This conclusion does **not** use
   the squarefree primitive Gauss-factorization formula for nonconstant
   Fourier terms; that formula cannot be imported at exponent two.
5. The primitive-density transfer has local factors
   `(1+h(p))/q^e` at primes in `aR`, and `1+h(p)/q` elsewhere. These give
   exactly `Z_S v(rad(aR))/(Na NR)`. Splitting the gcd factor by its
   divisor expansion gives the stated linear combination of the exact
   `F_g`. Thus all squarefree labels through G have their indicated
   product-profile polar functional annihilated simultaneously.

The conclusion is an affordable finite, zero-preserving correction that
kills a specified growing polar space. It does not estimate the growing
nonconstant progression transforms, the continuous primitive remainder,
or the complete mixed mean. In particular, it supplies no new zero-free
boundary and does not cancel a further independent character or height
functional without a separate argument.
