# Independent review of the frozen spectral packet

Reviewer: `family_escape`. Date: 24 October 2026.

Disposition: no material mathematical gap found in the independently
reviewed results at their stated scope. The two amendments requested during
review—the explicit lower bound for the theta density and the legal range
of the variance selector—are present in the frozen files below.

## Frozen source files

| File under `spectral/` | SHA-256 |
| --- | --- |
| `THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md` | `783c98402482a109d3ebf5743792f3c6cb15cc1d17efe519014e65aa5c98196b` |
| `POSITIVE_NULLSOURCE_PERTURBATIONS.md` | `5dde659415115313e99373f69e5c8b7f4fb96f426e441c9eddc040292d428817` |
| `check_polynomial_identities.py` | `4c2a0387fa998155ba0c98eb9c59a8f51a01600e3c1948e87848cf2183ce7b03` |
| `polynomial_checks.json` | `1cb937b06dcbf1a1db45475d7b1645943e83ab5fac736539c614cf3fb4928103` |

The hashes were independently recomputed locally. This is an internal
mathematical review, not external peer review or formal verification. The
inherited de Branges theorem and the complete analytic source chain of
PR #1017 were not independently reproved here.

### Authorship boundary

The reviewer developed the elementary variance bound now used in Section
4.2 of the main note and the prescribed-width quartet now stated as
Theorem 2 of the positive-nullsource note. These are **not** independently
reviewed by this reviewer. The spectral author separately checked their
proofs. The original derivations and the initial independent review of the
other spectral arguments are recorded in
`SPECTRAL_AUDIT_AND_TWO_LEMMAS.md`.

The review below independently covers the main jump identity, broadened
approximate nullvectors, safely shifted delocalization, the new deep-shift
theorem, the finite-prefix downward perturbation, and the explicit global
positivity certificate. It also checks the author's use of the two
reviewer-supplied lemmas, without treating that use as an independent
verification of the lemmas themselves.

## 1. Jump form and broadened approximate nullvectors

The ground-state expansion has the displayed archimedean and prime
coefficients. Expanding the pole kernel gives the stated hyperbolic form,
including its two rank-one terms and their signs. The quotient formulas
require the displayed decay estimates rather than only the formal
annihilator identity.

The explicit lower bound

`phi(x) >= c exp(9|x|/2 - pi exp(2|x|))`

from the first positive theta term is now included. Together with the
fixed-order derivative estimates, it supplies the needed integrability of
the derivative-to-density ratios. This closes the presentation gap found
in the initial draft.

For the broadened source, convolution with a compact probability bump
preserves exact full-source annihilation before cutoff. The mass remains
one after normalization, the squared norm is `O(1/a)`, and the cutoff
error is super-exponentially small. I checked the small-translation
archimedean cancellation and the treatment of all prime powers, including
those beyond `exp(2a)`. The summable majorant is proportional to

`exp(2a) sum_(n>=2) (log n) n^(-5/2)`.

Thus the tail argument does not silently drop the large prime powers.

## 2. Safely shifted selection and the variance selector

Coercive constrained minimization gives the claimed norm bound with
denominator `lambda_0(a)-kappa_a`; no unproved spectral margin is being
replaced by `|kappa_a|`. Plancherel, local uniform convergence, and the
normalization at zero give the nonnormality conclusion whenever that
norm bound tends to zero. The explicit shift `2b_a-1` has the required
relative margin from the stated elementary lower bound.

The note correctly does not extend this Plancherel argument to an
unbounded Gaussian compensation factor. Its stronger compensation
obstruction comes from the separate deep-shift theorem reviewed below.

The original conditional variance bracket approached the bottom
eigenvalue while restricting shifts to be negative. That would be
insufficient when the bottom is positive. The frozen text explicitly
allows the full legal range `kappa<lambda_0(a)` for the proposed selector,
while labeling the earlier norm-based window as a negative-shift result.
For a nonnegative legal shift, the variational inequality indeed gives

`d_a ||f_a||_2^2 <= epsilon_a`,

and the Rayleigh quotient of the broadened test vector gives

`lambda_0(a) <= 2a epsilon_a`.

Consequently any positive legal shift is itself on the residual scale.
The conditional endpoint bracket is now consistent with its permitted
shift range. Its bottom-projection and endpoint inequalities remain
explicit assumptions, not established facts about the full operator.
The caution against inferring monotonicity from self-adjointness is
correct: the numerator has mixed spectral coefficients.

## 3. Deep-shift theorem and zero-free compensation

For `kappa_a=-exp(4a)`, the constant function on the finite interval is in
the actual operator domain. Its zero extension has Fourier transform
`2 sin(at)/t`; multiplication by the logarithmically growing
archimedean symbol remains square integrable. After rescaling, the
archimedean contribution is `O(sqrt(a))`. The finite prime and pole
operators give the asserted combined estimate

`||A_a 1||_2 <= C a^(3/2) exp(a)`.

The elementary prime bound and the lower spectral bound suffice; no
prime number theorem or zero-free estimate is used at this step.

The resolvent identity is legitimate on this operator-domain vector.
Writing `K=exp(4a)` yields

`||K(A_a+K)^(-1)1 - 1||_2 <= C a^(3/2) exp(-3a)`.

The integral differs from `2a` by `O(a^2 exp(-3a))`. Normalization then
gives exactly the claimed `O(sqrt(a) exp(-3a))` error from the flat
density on the interval. Evaluation at `w/a` costs only
`sqrt(2a) exp(|Im w|)`, establishing locally uniform convergence to
`sin(w)/w` in the rescaled variable.

Rouche's theorem near its simple zero at `pi` gives a unique nearby zero.
The real-entire symmetry makes it real, so this part does not need the
inherited general real-zero theorem. Its original-scale location tends
to zero. Every zero-free entire multiplier normalized to one at zero
retains that zero. Local uniform convergence of any subsequence would
then force a limiting value both zero and one at the origin. The stated
compensation obstruction is valid in this deep-shift regime; the note
correctly leaves the narrow source-sensitive regime open.

## 4. Finite-prefix positive perturbations

Theorem 1 of the positive-nullsource note is independently verified. The
ratio of the highest even derivative to the theta density dominates the
lower derivative and tends to positive infinity at both ends. A compact
minimum argument therefore supplies a global positive perturbation for
small positive epsilon. Integration by parts preserves the prescribed
moment prefix and lowers the next even moment by precisely

`c epsilon (2m+2)!`.

The Fourier multiplier has the displayed sign. For even `m` it has no
real roots, and for odd `m` it has exactly two real roots; in either case
it inserts nonreal roots. The leading double-exponential tail rate is
unchanged, and differentiation preserves annihilation of the full
convolution source. The theorem concerns an auxiliary density and does
not assert anything new about the zeros of Xi.

## 5. The explicit positivity certificate

I ran the author's exact checker and also recomputed the finite
identities independently with standard-library rational arithmetic. The
independent computation expanded the differentiated theta term using
the Euler differential operator, then converted the resulting polynomial
directly to the Bernstein basis on `[3,10]`. This reproduced all seven
positive Bernstein coefficients. A separate translation to `10+y`
reproduced all seven positive tail coefficients for `P_4-P_2`.

Because every theta summand has `u>=pi>3`, these two exact certificates
prove global positivity of the explicit perturbation; no numerical
sampling of the theta function is being promoted to a proof. The
variance decrement `1/5000` and the quartet
`+/-sqrt(199)/2 +/- i sqrt(201)/2` also check exactly.

The prescribed-width quartet of Theorem 2 is separately attributed as
described above. The frozen text correctly distinguishes its approximate
variance matching from Theorem 1's exact moment-prefix preservation.
Those properties are not combined into an unproved stronger example.

## 6. Accepted scope

The packet gives source-specific obstructions and a quantitatively
narrower selection target. It does not establish existence of the
variance-matched selector, identify any normal limit with Xi, prove the
inherited de Branges theorem afresh, or improve a zero-free boundary.
The finite polynomial checks certify their exact algebraic identities,
not the analytic conclusion of a zero-free theorem.
