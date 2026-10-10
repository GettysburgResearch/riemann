# Independent review of complete cusp descent

**Reviewer:** signed_series_bootstrap, separate from the author of
`FULL_CUSP_DESCENT.md`.

**Exact reviewed file:** `FULL_CUSP_DESCENT.md`, 11,988 bytes.

**SHA256:**
`b025af8af1ac13d07a04fbc7de71401d2a47ef2c8df5a1e89a4edc4973482504`.

**Scope:** the new composition, including its exact function,
all-cusp/bad-part decomposition, quantitative summation, holomorphic
gluing, and conductor mean. This reviewer authored the companion
bootstrap input; the bootstrap itself therefore has a separate
independent review by scale_covariance_attack in
`INDEPENDENT_SPECTRAL_BOOTSTRAP_REVIEW.md`. A frozen-commit binding
is to be supplied in the packet validation record.

## Verdict

**PASS, with the declared source dependencies and scope.** The full
actual three-cusp output of the specified reunited standard-face
Dirichlet object has the stated larger domain and squarefree-row
mean. The theorem does not identify that object with the entire
original physical moment and does not assert an estimate for every
row valuation or for growing auxiliary twists.

A literal carriage-return byte in the squarefree annotation of (4.2)
was removed during review. The final additional comparison in Section
5 was also checked; its hypothetical spectral threshold was clarified
to `1/2<=a0<1`, matching the strip used by this mechanism. Both changes
precede the reviewed hash above. The full-cusp factorization and its
analytic estimates required no correction in this composition audit.

## Input identities used in this review

I independently reconstructed both finite-ray proofs at the hashes
in `FINITE_RAY_INDEPENDENT_REVIEW.md` and Sections 1–4 of the
all-cusp adapter at the final hash in
`ADAPTER_INDEPENDENT_REVIEW.md`. The quantitative adapter Section 5
is not an input to this composition. The independently reviewed
spectral and bootstrap inputs are:

| Input | SHA256 |
|---|---|
| `SECOND_REFLECTION_BOOTSTRAP.md` | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` |
| `SPECTRAL_ROW_MEAN.md` | `5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1` |

The spectral theorem applies to a fixed finite ray family and to any
subset of squarefree rows. I separately checked its dyadic block
norm summation and its threshold `Re(u)>5/8`; this does not replace
the independent input review recorded by its assigned reviewer.

## Independent reconstruction

1. **Exact initial object.** Equation (1.3) is the finite-ray theorem's
   complete actual series after grouping labels with the same cusp
   and bad denominator. Y is defined by that series, so no division
   by the possibly zero gamma factor is used. Its original domain
   becomes `a>1, tau<a` under `a=Re(v-s)`, `tau=Re(v)`.
2. **Complete support.** Every supported frequency has the unique
   sector decomposition in (2.1), with the prescribed unit and
   lambda-adic support. Splitting the squarefree S-part from the
   arbitrary S-supported cube part retains all bad frequencies.
   The good squarefree part n may divide the good cube part b;
   no additional coprimality condition is introduced.
3. **Cube compatibility with bad nonunits.** The finite-cube theorem
   holds for every integral argument. It therefore applies after
   freezing a possibly nonunit factor
   `epsilon lambda^(j+4)n0 b0^3`. The intrinsic additive phase is
   invariant under primary cubes, while each supplementary Gauss
   factor is cubic. Ordinary finite character orthogonality then
   forces the exact contragredient cube in (2.3) in every sector.
4. **Uniform finite family.** All the multipliers are evaluated on
   one fixed bad residue group. Varying j, n0, b0 only changes the
   finite residue function on that group; multiplication by a fixed
   possibly nonunit bad factor does not increase its period. The
   Gauss CRT split at n0 adds only fixed cubic characters. The
   number of possible output characters is consequently independent
   of the infinite bad indices and of k.
5. **Canonical good part and masks.** The good coefficient is
   precisely (2.4), including the cube angular character, cube row
   character, and square-root cube coefficient. Only good primes
   dividing nb enter the deformation. Primes at k vanish in the
   original row character and stay omitted in every product.
   Changing the row twist to the reciprocal primary orientation
   for the spectral input uses a fixed finite residue partition
   and supplementary character. The local cube identities are
   established first in the inherited convention; the spectral
   estimate permits these additional fixed characters. No claimed
   orthogonality across the row partition is needed.
6. **Exact coefficient series.** Freezing the bad labels and taking
   the stated finite Fourier coefficients yields (2.5) on the
   common absolute domain `tau<1, a>1`. No bounding operation
   replaces the actual coefficients in this identity. The factor
   `3^(j/6)` in the coefficient table, the full norm power, and
   `sqrt(Nb0)` give exactly the exponents in (2.6). Fixed bad norm
   factors are harmless on bounded real strips. The finite Fourier
   transform has bounded operator norm on this fixed group, and
   every remaining k-dependent phase is bounded uniformly in k.
7. **All infinite tails.** The j sum converges geometrically for
   `Re(t)>1/6`. The b0 sum is a finite product of geometric series
   at exponent `3Re(t)-1/2>0`; no summation over an unbounded set
   of bad primes is hidden here. The proposed continuation domain
   has `Re(t)>1`, hence these tails remain uniformly summable on
   compact subregions with more than the needed margin.
8. **Holomorphic gluing.** In the new bootstrap domain
   `a>1/2, tau<1, 3a-2tau>1`, (2.5) converges locally normally
   after the preceding bad-label summation. It agrees with the raw
   function on the open overlap. Its union with the raw domain is
   exactly `a>1/2, tau<min(a,(3a-1)/2)`: for a>1 the first
   bound is controlling, and for a<=1 the second is controlling.
   The case a=1 is covered by the new domain. The resulting domain
   is convex, and `Re(s)<0` there ensures that H has no pole.
9. **Pointwise and mean estimates.** Summing the normal divisor
   bound over the absolute B-mass gives (3.2). For the mean, first
   apply the squarefree-row spectral estimate inside each canonical
   Z; then use Hilbert-space Minkowski and the sum of the k-uniform
   suprema of B. This includes all cross terms between cusp and
   bad labels rather than deleting them. Restoring
   `H(s)(Nk)^(1-2s)` changes the row energy exponent from one to
   `3-4Re(s)`, as in (4.3). All imaginary variables have only the
   stated fixed-strip polynomial growth.
10. **Quantitative meaning.** The balanced scalar has exponent
    `2a-tau`, whose infimum is `(a+1)/2` on the strict new
    domain. Letting a approach 5/8 from above gives 13/16 as an
    infimum, not an attained contour. I checked the companion exact
    comparison: the resulting candidate `Q D^(13/8+epsilon)`
    never improves the minimum of the two stated existing physical
    bounds. The new general comparison is valid as well: for
    `1/2<=a0<1`, a candidate `Q D^(1+a0)` is dominated, up to a
    fixed constant, by the factorwise bound when `Q<=D^a0` and
    by the classical bound when `Q>=D^(1-a0)`. Its mixed-term
    condition `Q>=D^(1-3a0)` is automatic for `Q>=1`.
    Because `1-a0<=a0`, these two ranges cover all rows. Merely
    lowering the spectral threshold toward 1/2 through this same
    summation therefore does not improve the old physical envelope.
    The scope paragraph correctly leaves a different joint covariance
    argument, the complete physical contour passage, and the long
    signed moment core open.

## Review boundaries

This is an independent review of a composition against the identified
file contents, retaining the imported source conditions and all
input review boundaries. It is not a Lean proof or an external human
acceptance. It does not claim that a finite diagnostic proves any
analytic continuation, nor that the stated spectral mean is a full
generalized moment theorem.
