# Internal review of the height-adapted mixed-norm comparison

Reviewed `../eisenstein/GROWING_PROFILE_COMPARISON.md`, actual SHA256
`7218a83fe0ea4d657e425af1a465ac8864ea5a1cc16cb42de4e9456f643c8097`.
This is an internal reconstruction of the root agent's proposal. I
developed a parallel two-profile construction in
`NORM_MELLIN_PROBE_ADAPTER.md`; the idea is therefore not an externally
independent discovery. No full complementary norm is claimed.

I found no blocker in Sections 1--2 or the squarefree-label conclusion
of Section 3. In compact logarithmic coordinates `(a,an,u)` the common
profile has rapid Fourier decay and a single row-independent density.
For every outer height the annular response and all its fixed height
derivatives are `O(1/Ng)`. The same positive matrix thus gives a uniform
weighted coefficient norm of subpower size, and its complete inverse
square-root label resource is at most `sqrt(G)` times a subpower.

The tail in these product-profile coordinates is untwisted; leaving
the outer height outside instead inserts its opposite phase in the
tail. These are the same construction. To estimate the error one may
insert a fixed plain-input cutoff covering the tail/product supports,
then Fourier-expand the product profile again. This gives two actual
plain factors at a common extra height. The complete squarefree-tail
Euler expansion retains every original zero and the moving g-mask.
Source TWO-PLAIN, followed by Minkowski over all labels and the original
Fourier density, gives exactly the claimed complete UG error.

The original zero detector is retained through the explicit norm
comparison; its modified modal vector need not itself preserve zeros.
I also reconstructed the later complete arithmetic-energy and
specific-head infinity-norm additions. The exact inverse of the main
gcd matrix has entries bounded by the gcd times a subpower. Its product
with the UNNORMALIZED squarefree-sieve error has row-sum norm
`O(D^(-1/2)G^(1+epsilon))`. Two downward divisor inversions give the
Mobius head's main solution a subpower infinity norm, so the finite
Neumann series preserves that bound throughout the full stated Gram
range. The same argument with the zero-height prefix weight gives
`(G/D)^(1-beta)` times a subpower at that special height. The complete
tail arithmetic square mass follows directly from its exact B-energy;
it does not improve the separately proved UG row comparison.
The final bounded-head extension also reconstructs: `|Z_h|<=C/Nh`
and the exact inverse entry bound imply a subpower main solution since
`sum_h N(g,h)/Nh` is a divisor bound times a harmonic logarithm.
The same infinity-norm Neumann estimate preserves it. Thus pointwise
subpower control applies to every bounded annular head in that stated
range, not only the Mobius head; the extra zero-height power gain
still uses its specific reciprocal cancellation.
The squarefree-label polar cancellation follows from the separately
reviewed growing-residue functional. The extension to sixth-free R
invokes `RESIDUE_VALUATIONS.md` and is not independently reconstructed
by this receipt. Neither the full continuous family nor canonical
recursion stability is proved by this comparison. The generic response
inverse argument alone permits a square-root-G pointwise price; the
new bounded-head inversion removes it for every bounded annular
arithmetic head in the displayed Gram range. An arbitrary unrelated
response vector without the `1/Nh` divisor-response bound is outside
this stronger conclusion.

## Subsequent annular-head scope correction

`ANNULAR_PROFILE_DEBIAS.md` supplies an additional reciprocal-based
improvement discovered after the above first read. A compact ANNULAR
Mobius head has an entire Mellin transform, so its
`D^(beta-1)g^(-beta)` response bound holds at EVERY real norm height,
with a fixed polynomial height cost. That cost is integrated against
the ORIGINAL common Fourier density. The zero-height-only caveat is
valid for a modulated PREFIX whose shifted Mellin pole can survive;
it must not be extended to the annular head explicitly used in this
comparison. The general UG theorem reviewed above remains valid, but
under the working reciprocal input its annular price improves to
`U D^(2beta-2) G^(3-2beta)`. This paragraph corrects any exclusivity
inference from this receipt's earlier zero-height discussion. It does
not claim an estimate for the remaining modified norm.
