# Independent review: unrestricted numerator-label principal energy

Reviewed `../rational/UNRESTRICTED_POLAR_ENERGY.md`, actual-byte SHA256
`5c88ae67d837a78c2d6c655d1fd0ce463ccbfee944baf3eb060bd7421c2f3531`.
This is an internal component review, not external referee acceptance.

I independently reconstructed the all-valuation extension, using the
declared base fixed section's cusp-density and full-series periodicity
inputs, rather than assuming primitive periodicity.

At `e=6k+r`, the cusp sum telescopes to
`Delta(p^e)=q^(-e+k)`. Converting the progression variable from n to nR
then leaves the actual outer factor `R_red^(-1/6)`. The primitive local
factor retains every prime of `rad R`, including positive sixth-power
exponents absent from R_red. For residue r=0 such a prime has the small
coefficient `1/q-1/q^2`; residue5 retains `q-1/q`. This agrees with the
direct fact that a new primitive exclusion cannot be erased by a full
residue's sixth-power periodicity.

The decomposition `R=t^6 R_red` is unique and needs no coprimality
condition. Its complete remaining-label count costs `Z^(2/3)` because
`sum_t (Nt)^(-4)` converges. For each prime constrained to divide g,
the complete positive-exponent sum is `O(q^(-3))`: residue5 first costs
`q^2*q^(-5)`, residue0 starts at exponent6 with `q^(-6)`, and every
additional sixth power contributes `q^(-4)`. This proves the asserted
weighted g-sum and the same omitted-response energy exponent.

I also reconstructed the scalar bound and the actual adjoint factors
`U^(1/6)L^(1/3)`. At the adaptive cutoff, (11) gives exactly
`U^(-4/15)K^(2/3)` under the stated D,N range, including the displayed
`K=U^(2+eta)` exponent. No blocking error was found at this scope.

This does not establish a row-frame inverse or identify other numerator
sections with the base section. The cited smooth adjoint row profile is
annular; an original profile nonzero near0 needs its own complete
treatment. Both the nonconstant Type-I error and the adjoint contour
remainder remain unpaid. A complete operator or improved zero-free
region is outside this review.
