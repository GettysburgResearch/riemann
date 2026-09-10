# End-to-end attempt and the exact remaining assertion

## Why this route

The cumulative project separates genuine graph and approximation theorems from
their unpaid arithmetic source/metric adapters. The newer PR #834 offers a
more direct object: an explicit operator T with ordinary Fredholm determinant
Xi(z)/Xi(0)=det(I-z^2 T). Its singular-value base is positive but does not
control the arguments of its eigenvalues. This packet attacks the resulting
spectral sign through exact whole-source traces, rather than composing
incompatible graph and approximation estimates.

The source is frozen at f0e34780f4fe91bd5d07e791e8855189838c3df5. The operator
interpretation inherits that proposed result; our power-sum theorems can be
read directly from the classical entire xi product without it.

## The complete desired chain

Let s_m=sum_j z_j^(-2m), all positive-real-part xi zeros with multiplicity.
For real polynomial P, the desired inequality is

    Tr[(T P(T))^2] = sum_j z_j^(-4) P(z_j^(-2))^2 >= 0.

It is the ordinary square INSIDE the trace. It is not (Tr A)^2 and not
Tr(A* A), either of which would lose the question.

For every polynomial degree, that inequality gives all Hankel matrices
(s_(i+j+2)) positive semidefinite. Hamburger moment existence plus compact
support and analytic Cauchy-transform uniqueness then force every nonzero
spectral value z_j^(-2) to be positive real. The proof in PROOF.md Section 7
retains every multiplicity and excludes complex poles by their nonzero
residues. This completes the implication to RH, but the starting all-degree
inequality is not established.

## What did work

A single real low-zero mode pays the entire possible negative Gaussian tail,
not merely a sample of it. This gives theta(u)>0 for all u>0 and the exact
positive Laplace representation of p(t)=d/dt log[Xi(i sqrt(t))/Xi(0)]. Thus p
is completely monotone, every scalar trace is positive, and every
FACTORIAL-WEIGHTED trace Hankel form is positive definite.

A separate interpolation argument proves unweighted positive definiteness
through rank 25 at every integer shift n>=2 (and rank nine at n>=1), with
an explicit relative lower bound and the whole infinite tail retained.

The shift-uniform conclusion follows analytically because each error term
shrinks by a factor r/l_j<1. It is not inferred from checking several shifts.

## Three tempting finishing steps do not follow

1. **Scalar to mixed positivity.** Tr(T^m)>0 for all m does not imply
   Tr[(T P(T))^2]>=0 for every real polynomial. The compact-density example
   in Section 6 has all scalar traces positive and an exact negative
   four-by-four mixed-moment determinant.
2. **Weighted to unweighted positivity.** The inverse-factorial multiplier
   already has determinant -1/12 at size two. It is not a general PSD
   preserving operation and is not a diagonal change of basis.
3. **One Laplace level to two.** Positivity of theta(u) makes its Laplace
   transform p completely monotone. RH requires theta itself to be
   completely monotone, equivalently the relevant Stieltjes spectral
   structure. Positivity of a Laplace density does not imply complete
   monotonicity of that density.

These are not just warnings about a hypothetical general matrix. The
symmetric-translation perturbation in Section 5 starts from the actual theta
density and retains all the proved positive properties while adding nonreal
zeros. It preserves the entire real-zero set, not just the first 25 modes.
It deliberately does NOT preserve the infinite theta/arithmetic formula or
modular identity. Hence it invalidates finishing arguments that use only
those positive properties, without disproving any assertion about the
unmodified xi source.

## The remaining direct operator inequality

For A=T P(T), the identity

    Re Tr(A^2) = ||A||_HS^2 - (1/2)||A-A*||_HS^2

isolates the missing comparison. Neither the positive singular-value operator
nor the present weighted Hankel form bounds the second term by twice the
first. A source-specific argument must do so for every real polynomial P,
or prove an alternative genuinely sufficient condition.

During closing, #834 acquired a separate crowding argument at
62bd9bbed134e20c1ee9cd92d008562079af9ceb. It obstructs bounded equivalent
metrics even on the infinite spectral core using already known real zeros.
That new manuscript is source-pinned as read context; it is not independently
accepted or a premise of the positive results here. Our attempt does not
assume the existence of such a bounded symmetrizer.

## Verdict

This is a proposed completed component packet, not a completed RH proof.
The numerical controls support the particular finite inequalities and exact
counterexamples; the infinite theorems rest on their written proofs and
named imports. There is no automatic change to accepted mathematics.
