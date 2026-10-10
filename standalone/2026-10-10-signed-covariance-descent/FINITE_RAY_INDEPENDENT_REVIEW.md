# Independent review of the actual finite-ray covariance

**Reviewer:** signed_series_bootstrap, separate from the two proof
files' author.

**Exact reviewed contents:**

| File | SHA256 |
|---|---|
| `FINITE_RAY_REUNION.md` | `8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0` |
| `FINITE_CUBE_HOMOGENEITY.md` | `e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1` |

**Scope:** all numbered claims in both files, subject to their exact
imported theta and PR #920 dependencies. The intrinsic three-cusp
coefficient input is Sections 1–3 of the independently reviewed
`ALL_CUSP_COEFFICIENT_ADAPTER.md`; its review hash and derivation are
recorded in `ADAPTER_INDEPENDENT_REVIEW.md`. A frozen-commit binding is
to be supplied in the packet validation record.

## Verdict

**PASS, with the stated source dependencies and scope.** The actual
finite coefficients force the divisor character `kappa=eta rho^3`,
remove the old artificial finite-character poles on the stated
overlap, and have the contragredient cube law. These are identities of
the complete source finite sum. They do not hold for arbitrary
independently assigned old ray coefficients.

No mathematical correction was required during this review. I checked
the less immediate ramified matrix case directly against the primitive
appendix rather than assuming that its multiplier obeyed an
unramified formula.

## Independent reconstruction of reunion

1. In the exact finite Fourier sum, substitution `x=d^2 y` proves
   `phi_hat(d^(-2)h)=rho(d)^2 phi_hat(h)`. Primary support and every
   nonunit zero are preserved because d is primary and prime to S.
   No squarefreeness assumption is needed for this elementary
   identity; the application retains its original squarefree d.
2. I reconstructed the fixed bad congruences using the source
   numerator `a=lambda^2 c(h/L+sum h_p/p)` and its CRT construction.
   When `r=k` becomes `kd`, relabeling h by `d^(-2)h` gives
   `a_d=d^(-1)a`, `c_d=dc`, `delta_d=d delta`, and
   `b_d=d^(-1)b` at all required fixed bad precision. Division by c0
   is legitimate after increasing the chosen numerator precision.
   These are local congruences, not a claim of a global integral
   diagonal matrix transformation.
3. Primary d preserves the source normalization and the residues
   selecting each of the three cusps. The bad additive factor only
   involves `delta_0 r^(-1)` and is therefore unchanged. The
   argument includes zero and nonprimitive Fourier labels and all
   ramified frequency indices.
4. I checked the three bad Kubota factors separately. The first
   denominator character contributes `(c0/d)_3^(-1)`. In the
   middle case both denominator characters scale together and give
   `(-c0/d)_3^(-1)=(c0/d)_3^(-1)`. In the final case primary cubic
   reciprocity converts `(d/c0)_3^(-1)` to the same expression.
   The supplementary conductors are fixed and included in the
   chosen bad modulus. Thus all cases give `chi_d(c0)^(-2)`.
5. Combining the conjugated Kubota ratio with the outside scalar
   cancels the residual c0 character. The Fourier factor supplies
   the additional `rho(d)^2`, leaving exactly `eta(d)rho(d)^3`.
   Since the relabeling is a bijection of the entire finite sum for
   each d, grouping by the baseline cusp does not lose a term.
6. The local Euler factor of P is exactly `D=1-x+z`. On multiplying
   by the signed Ramanujan factor, its two cases are `D-z=1-x`
   and `D+(q-1)z=1-x+qz`. This leaves the complete reciprocal
   `1/L(w,chi^-)` and the finite product over primes dividing the
   actual frequency. Primes at kS remain omitted, and the row
   character's literal zero mask is unchanged.
7. On `sigma<min(0,tau-1)`, the proof gives `Re(w)>5/2`. The
   reciprocal Euler product is consequently absolute, while the
   frequency weight is bounded by
   `Nm^(max(0,1-tau)+epsilon)`. The full three-cusp coefficient
   series is absolutely summable at any exponent greater than one.
   The strict domain inequalities give the required summability
   margin, hence local normal convergence in both complex variables.
   The gamma numerator has no pole for `Re(s)<0`; Stirling yields
   precisely the displayed polynomial vertical growth.
8. The pole-removability statement follows on the common domain by
   equality of holomorphic continuations. Its residue corollary is
   stated for the complete finite source sum, and the argument at
   possible zeros of outside factors uses an open set followed by
   analytic continuation. The residual exponent comparison remains
   strictly greater than one throughout this raw domain.

## Independent reconstruction of cube homogeneity

1. Substituting `y=b^3x` gives
   `phi_hat(b^3h)=bar(rho(b))^3 phi_hat(h)`. At fixed active
   product k the same bad CRT calculation gives
   `a_b=b^3a`, `delta_b=b^(-3)delta`, and `beta_b=beta`.
   The denominator, its normalizing unit, and the cusp remain fixed.
   All these calculations use invertibility at S alone; b may
   therefore meet k or the frequency without invalidating them.
2. For the two direct Kubota cases the ratio is a cubic character
   evaluated at a cube and is one. In the middle lambda-adic case
   the source explicitly gives `beta=0` modulo its fixed large
   power at every prime of c0. I checked that statement in
   `paper2.tex`, Appendix `app:fixed-ray`, in the CRT display
   immediately preceding the definition of H. Increasing the fixed
   precision to contain the supplementary conductor makes
   `a_b-u0 beta_b=b^3(a-u0 beta)` at that conductor. Its ratio is
   therefore one as claimed. This is the load-bearing ramified
   check.
3. In the bad additive phase, multiplying the argument by b cubed
   cancels the inverse cube in delta. Thus the complete finite
   function obeys its stated covariance for every integral argument,
   including bad nonunits, before any character expansion.
4. The independently reconstructed theta coefficient formula proves
   `d_sigma(b^3 ell)=sqrt(Nb)d_sigma(ell)` for all three cusps,
   including overlap with the squarefree coefficient part. Unsupported
   indices stay unsupported. The intrinsic nonstandard additive
   phase is unchanged because `b^3-1` is in `9O=lambda^4O` for
   primary b. This intrinsic phase and the external source additive
   phase are handled separately.
5. On the fixed primary unit residue group, coefficientwise
   comparison of a multiplicative Fourier expansion under cube
   scaling forces `rho_prime^3=bar(rho)^3`. The finite cubic
   supplementary factors preserve this equation. Extending the
   characters by zero at S restores precisely the arithmetic masks
   used in the subsequent canonical series.

## Review boundaries

This is an independent mathematical reconstruction of the identified
contents. It is not a Lean proof, an external human acceptance, or an
independent proof of every imported theorem in the primitive analytic
manuscript. No finite diagnostic is used to infer an infinite identity.

The shifted-variable analytic continuation, its spectral row estimate,
and the composition summing all cusp and bad labels have separate
review scopes. These two finite-ray results do not establish the
generalized moment hypothesis or RH.
