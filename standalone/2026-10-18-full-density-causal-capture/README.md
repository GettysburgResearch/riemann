# Full-density capture of a fixed native member

Status: PROPOSED complete component proofs; independent review required.
No RH proof or new cancellation exponent is claimed.

## What changes

For the literal Gaussian Mobius source A and its Euler-deleted replicas A_b,
put N_B=#{b:Nb<=B}. At every fixed weight sigma>0, all sufficiently large B,
EVERY finite horizon T, and simultaneously for 1<=p<=infinity,

    ||N_B^(-1) sum_b A_b||_(sigma,p,T) asymp ||A||_(sigma,p,T).

The constants in these ROOT norms do not depend on p, T, B, or the permitted
character phases. This is a bounded inverse of the SIGNED average, not a
triangle-inequality bound on independently treated rows. It includes sigma=1/2.

The exact average kernel is chi(d) I_S(B/Nrad(d))/I_S(B). Its limit is
chi(d)/Nrad(d), with weighted coefficient-norm error O(B^(-eta)) for every
fixed eta<min(sigma,1/2) over the Eisenstein field. The limit and its inverse
have absolutely summable explicit Euler kernels. Finite-B inversion follows
by a paid Neumann estimate. No limiting inverse-zeta bound is assumed.

Any vanishing fraction of WHOLE replica trajectories may be deleted before
averaging, even adaptively. A sufficiently small fixed fraction is also
allowed. The survivor set must be fixed across the observation interval;
a scale-dependent deletion inside the integral is a different problem.

The complete averaged second energy has an explicit quadratic-form limit,
with O(B^(-1/2+epsilon)) RELATIVE operator error at the critical weight. All
shared-prime and off-diagonal terms, and the upper horizon, remain. The form
is bounded above AND below by fixed multiples of the original native energy.

## What does not change

No subpower upper bound for that native energy is proved. The limiting signed
source has coefficients mu(d)chi(d) product_(p|d)(1-1/Np), not positive ones.
The theorem preserves the fixed-member difficulty instead of solving it.
The large-sieve residual and capped reciprocal laws are different observables.

Relative to #983, this supplies a signed-mean inverse and full-density capture
for finite-horizon norms, rather than relying on B/log B prime replicas or a
pointwise source-envelope bootstrap. It is not a claim about arbitrary
pointwise deletion of moving rows. The earlier Euler identities and mean-mask
bounds are explicitly credited; no worldwide novelty claim is made.

## Recovery and reproduction

The ten-file joint-mollifier packet is ALREADY recovered unchanged on #989,
commit 30151b285f3334484758c8305b58da380ff73488. Its full original replay was
freshly rerun and its complete tree matches the published tree. Nothing from
that archive is duplicated here; see RECOVERY_AUDIT.json.

Read PROOF.md, then SOURCES_AND_VALIDATION.md. Run:

    python -B replay.py

The finite checker uses complete stated ideal prefixes, exact Q(omega)
arithmetic, and a finite critical-weight coefficient-space model. It does
not compute the infinite Gaussian, certify the analytic theorem, or prove RH.
