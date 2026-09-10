# Direct closing attempt and its exact remaining burden

Status: proposed component results; no completed RH proof.

The parent supplies three small arithmetic seeds and exact equality of their
joint shift-generated space with the factorial-source space. It also explicitly
leaves full L2 admissibility of arbitrary high-degree raw feedback open. I tried
to remove that obstacle without weakening the growing-horizon test.

## What changes

At polynomial degree D use the SAME gamma shape and rate D. Its Laplace symbol
is M_D(z)=(1+z/D)^(-D), and its physical mean delay is exactly one. The proper
kernels in PROOF.md (6) make every new residual an actual L1/L2 function, for any
finite coefficient array. This is proved from bounded finite floor sources; no
Lindelof or high-zeta-moment theorem is imported for admissibility.

The output is an explicit bounded convolution of the original factorial source,
not a changed zeta function or an auxiliary positive Gram. Its target is the
regularized exponential g_D. This is not hidden: g_D tends in L2 to the FIXED
unit-norm delayed exponential S_1 e. The output agrees with g_D before m log Q.

For every fixed hypothetical off-line zero rho, the observation factor is at
least exp(-|rho-1/2|), uniformly over degree. Hence the full positive exponential
Q^[m(2 Re rho-1)] remains in the mandatory lower energy bound. The smoothing
has NOT made the sufficient estimate insensitive to high but fixed ordinates.
It can suppress heights that move with degree, so the parent's quantitative
near-recurrence/coefficient-cost theorem is not imported unchanged.

The main all-degree construction is a positive result. It is stronger than
asserting that a meromorphic boundary integral converges, because the entire
causal source and a bounded source map are built explicitly.

## The full proposal tested next

Fix the actual bank from #838. Use all homogeneous degree-m monomials, gamma
shape/rate m, and the complete real Gram matrix G_m of their regularized sources.
The explicit ridge choice in PROOF.md (26) defines one controller for EVERY m.
There are (m+1)(m+2)/2 coefficients. The positive ridge is 2^(-m^2); it makes
inversion legitimate even if the feature functions are dependent.

The exact positive scalar b_m is both a minimized complete regularized energy
plus a coefficient penalty and an upper bound for the selected residual energy.
It is defined through the physical functions, not a truncated or data-fit matrix.
All its finite-frequency and future contributions can be enclosed using the
fixed-degree tail theorem. This is not a claim that a large-rank implementation
was executed or that the implicit constants are small.

The decisive proposed statement is:

    liminf_(m->infinity) log(1+b_m)/m = 0.

This would give RH by PROOF.md (17)--(19). I did not prove it. I also do not claim
RH implies this particular homogeneous, ridge-penalized construction succeeds.
The more general regularized-feedback class permits other degrees and controls.

## The upper-bound attack did not close

Young's inequality proves a finite upper bound involving

    sum_alpha |c_alpha| [(2D-1/2) max_j ||f_j||_1]^(|alpha|-1).

For degree comparable to m it allows exp(O(m log m)), not exp(o(m)). The factor
D comes from a differentiated stable filter. It cannot be discarded because its
impulse kernel has signed coefficients. Knowing each initial error is below
0.02 controls one L2 factor but does not make the entire convolution algebra a
contraction. Positivity of the feature Gram or its explicit ridge floor likewise
does not prove the required subtraction in the constrained minimum.

Scalar powering remains rigorously ruled out: the finite seed has recurrent
auxiliary zeros near Re s=1, and the new gamma multiplier stays nonzero at every
fixed one. Their delayed lower bound survives regularization. Thus choosing
P_m(w)=w_j^m, or arbitrary scalar polynomial acceleration of one fixed seed,
is not an unconditional closing construction even assuming RH. A successful
controller must genuinely change or combine the arithmetic information.

The separate all-order diagnostic shows that declaring both raw banks' pure
powers square-integrable for every order would already prove Lindelof. That
hypothesis is avoided by the new construction, but avoiding it does not by
itself give the small-energy estimate.

## Review priority

Check the powers of s versus the centered coordinate z, the proper kernel
(6), the bounded convolution identity (15), the target shift in (16), and
especially the uniform-in-degree fixed-zero bound (18). Check the complete
polynomial tail (21) before using numerical cutoffs. Section 7's LH equivalence
uses Hardy and strip theorems separately from the elementary regularization.
The ridge definition is a concrete unproved candidate, not an accepted edge to RH.

No new zero-free region, actual high-degree optimum, or global entropy/prime-error
bound is claimed. The contribution removes the admissibility gap without deleting
the remaining source-specific estimate or handing it to reviewers as routine work.
