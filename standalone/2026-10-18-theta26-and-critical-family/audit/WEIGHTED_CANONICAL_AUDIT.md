# Independent review of the positive weighted half-plane criterion

**Pass for the conditional theorem.** The reviewer read the complete note
independently of its author and rederived its analytic estimates. This is
a component review, not an assertion that the all-order feasibility
hypothesis holds for the theta cumulants.

Reviewed file: `theta/WEIGHTED_CANONICAL.md`.

SHA-256: `787105a0dbab8dcc045a31b92b4b08bc1fc4ba999c03320814f92fb6c7f61f0b`.

## Branch and domain

For a positive real node b and a point in the open upper half-plane,
`1-b*z^2` cannot lie on the nonpositive real axis. Its imaginary part is
`-2*b*Re(z)*Im(z)`; if that vanishes, `Re(z)=0` and the value is positive.
The principal logarithm is therefore holomorphic on the entire open upper
half-plane and is real on its positive imaginary axis. The fractional
canonical products used in the note are nonvanishing there. They are not
claimed to extend across their real branch points as entire functions.

## Uniformity without a common support bound

The inequality `abs((1-w)*exp(w))<=exp(abs(w)^2/2)` follows immediately
from `log(t)<=t-1` applied to `t=abs(1-w)^2`, with the zero case handled
directly. Taking positive real powers preserves this modulus inequality.
Matching the second node power, which is the fourth theta coefficient,
therefore gives the stated common quartic envelope independently of node
count, support, total weight, and the signed Gaussian coefficient.

The proof does not use a common disk of analyticity at zero for the
approximants. Its exact logarithm remainder after degree M-1 has sign
`(-1)^(M-1)` and magnitude at most `x^M/M` for **every** x>=0. This was
checked by integrating the finite geometric expansion of `1/(1+x)`.
Positive node weights permit summation of that bound using exactly the
matched highest power Q_M.

The target's logarithm is analytic on some disk about zero because H(0)=1.
Cauchy's coefficient estimate gives `abs(Q_M)/M<=C*d^(-2*M)`. Thus the
global remainder and the target Taylor tail tend to zero on each fixed
point `z=it` with `0<t<d`, even if auxiliary branch points approach zero
along the real boundary. All logarithms at those points are the real ones.

## Limit and mathematical scope

The quartic envelope supplies normality on the open upper half-plane.
The positive imaginary interval has accumulation points in that domain;
pointwise identification there forces every locally uniform subsequential
limit to be the actual H by the identity theorem. Hence the entire cofinal
sequence converges on the open half-plane. Hurwitz excludes its zeros
there, and conjugation handles the lower half-plane. The target is not
identically zero, as shown by the same imaginary-axis identification.

The reformulation as positive measures with masses `lambda*b^2` has the
correct power indices. Both displayed Hankel positivity conditions are
necessary. The note does not assert that a particular finite collection
of principal determinant tests is sufficient for a truncated Stieltjes
problem, or that all-order positivity has been proved. This distinction
avoids replacing the missing construction by a finite semidefinite check.

The theorem genuinely removes the integer-multiplicity and Gaussian-reserve
restrictions from this sufficient consumer. It does not remove the
unbounded-order positive moment hypothesis. The finite certificates in
the packet provide its hypotheses only through M=13; no new global zeta
zero-free bound or RH proof follows from the reviewed files.

No numerical checker is needed for this elementary analytic implication.
The finite theta inputs and their directed arithmetic have a separate
source-bound review. The present review is by another research agent in
the same session, not an external human referee or formal proof assistant.
