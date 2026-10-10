# Independent cross-review of the derivative and eventual-tail obstructions

Status: ACCEPT_AT_STATED_PROPOSED_SCOPE, pending the repository review process.
Reviewer: operator-mechanisms track, distinct from the xi author.
Scope: exact synthetic/source-class obstructions; no assertion about an actual
off-line xi zero or failure of any correctly specified exact-theta descent.
Files read: `../xi/DERIVATIVE_COUNTEREXAMPLE.md`,
`../xi/THETA_TAIL_OBSTRUCTION.md`, and the complete inherited high-order entry
proof in `reviews/A/supplement/REPORT.md#S06`.

## Discrete model

The factorization D1 expands exactly: its linear coefficient is
epsilon*(2c^2-1)/c=1 and its constant is -epsilon.  The two cosine values are
-cosh(delta) and 1/(2cosh(delta)); their entire preimages are precisely the
nonreal and real classes listed in D2.  Their sine derivatives are nonzero
when delta>0, so all original zeros are simple.

For every positive even derivative the effective coefficient w>1.  The
quadratic 2w v^2+v-w is positive at both v=-1 and v=1 and negative at v=0,
so both roots belong to (-1,1).  Every complex solution of cos(z)=v in this
range is real.  Odd derivatives factor as sin(z)*(1+2w cos(z)); their extra
cosine value also belongs to (-1,1) and does not coincide with a sine zero.
This verifies the complete, all-order root classification without sampling.

On the lower ray, F'=i g and F''=-h, giving precisely D3.  Since
g>=0, h>0, and h'=sinh(y)*(16epsilon*cosh(y)-1)>0 for y>0, f+lambda*g
increases from epsilon-1<0 to a positive value at y=delta.  Its unique ray
zero and all signs in D5 follow.  Implicit differentiation verifies the
strict negative lambda derivative.  Integrating h twice gives D7 with the
stated lower and upper curvature constants.  Direct expansion of the
hyperbolic functions gives the quartic D8.  The fixture rho=7/23,
lambda_0=27/37 and endpoint -259/621 are arithmetically consistent.

## Smooth eventual-theta-tail model

Because h is even, normalized, and supported within eta<1/4, the two positive
u bumps have cosine transform B(z)*cos(z) and epsilon*B(z)*cos(2z), with exactly
the factors 1/2 shown in the source density.  Near u=0 they vanish, so the
even extension inherits smoothness from the positive theta source.

The T1 exponential estimate is valid for complex z.  The Taylor remainder in
the first factor of C is at most a²*cosh(delta+a)/2 <= s*a/8.  The second
factor has modulus at least 3c/4.  Including |B|>1/2 gives the stronger
boundary lower bound |BC|>21epsilon*c*s*a/32; the paper's epsilon*c*s*a/2
therefore has slack.  The prescribed tau*Xi bound is at most half the paper's
BC lower bound.  The disk excludes the reflected nonreal zero, all real zeros,
and other periods.  Rouché proves exactly one nonreal zero in that disk.

For u>2+eta, the density is exactly tau times the theta density.  The log-tail
derivatives and their asymptotic errors are consequently unchanged.  Positivity
and smoothness on each bounded interval bound the compact second log derivative.
The inherited S06 proof needs only those conditions to obtain eventual global
log concavity after multiplication by u^r, the theta tail saddle, central
curvature, and exterior exponential tails.  All survive, with constants and
starting order depending on the perturbation.  The frozen companion parameter
must remain the source's own M_r/M_(r+1); no varying-parameter derivative
identity is inherited.  Thus the claimed complete lower-ray entry in
T²*log(r)/r ->0 follows conditionally on the named S06 theorem and its classical
theta source inputs.

The mass bound T4 uses only u<=U for the compact source and u>=V on the positive
theta reserve interval.  Its y>=0 uniformity and T5 total variation convention
are correct.  For each desired fixed exponential rate, one may fix V>U
accordingly before r tends to infinity; the possibly tiny C_V changes only
the fixed constant.  The manuscript correctly avoids promoting TV control to
unbounded moments without extra normalization.

No load-bearing gap was found.  The smooth example establishes high-order
entry and a low-order nonreal zero together; it does not inherit global
real-rootedness of every derivative or the thin global zero strip of the
separate discrete model.
