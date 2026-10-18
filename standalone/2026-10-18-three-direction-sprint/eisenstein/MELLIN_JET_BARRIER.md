# Finite Mellin jets do not suppress the complete separated family

**PROPOSED elementary obstruction within the stated tail architecture.**
This does not bound the actual signed mixed character covariance. It
explains why adding more scalar Mellin-derivative cancellation conditions
to `TAIL_DEBIASED_MOLLIFIER.md` is insufficient by itself.

Let the good ideals and the positive weight `v(a)<=1`, `v(1)=1`, be as
in that file. Only the elementary ideal count `#{Na<=x}<<x` is used.
For `D>=2`, let `b_D` be any finite coefficient sequence satisfying

    b_D(a)=mu(a)                         (Na<=D),
    supp(b_D-mu*1_[Na<=D]) subset {Na>D},
    L_D=sum_(Na>D) |b_D(a)|v(a)/Na <= exp(o(log(D)^2)).       (1)

In particular, a tail in `[2D,3D]` with any fixed polynomial or polylogarithmic
harmonic coefficient mass satisfies (1). No constraint on the number of
Mellin derivatives cancelled at zero is imposed. Put

    F_D(t)=sum_a b_D(a)v(a)Na^(-1-it).

There is a fixed `tau>0` and a fixed `D_0` such that, for all `D>=D_0`,

    integral_R exp(-t^2/tau^2)|F_D(t)|^2 dt/(tau sqrt(pi))
          >= 9/16.                                         (2)

The same assertion holds after replacing every coefficient by
`b_D(a)Na^(-iT)`, uniformly in the real shift `T`.

## Proof

Gaussian Fourier inversion gives, exactly,

    integral_R exp(-t^2/tau^2)F_D(t)dt/(tau sqrt(pi))
       = sum_a b_D(a)v(a)/Na exp[-tau^2 log(Na)^2/4].         (3)

The unit contributes one. The elementary ideal count implies convergence
of

    sum_(a!=1) Na^(-1) exp[-tau^2 log(Na)^2/4]

for every positive `tau`. It tends to zero as `tau` tends to infinity:
apply dominated convergence, for example dominating by the convergent
series at `tau=1`. Choose a fixed `tau` making this series at most `1/8`.
Then every nonunit prefix contributes in absolute value at most `1/8`,
uniformly in `D` and in the phases `Na^(-iT)`. The tail in (3) is at most

    L_D exp[-tau^2 log(D)^2/4]=o(1).

Thus the absolute value of (3) is at least `3/4` for large `D`.
Cauchy--Schwarz in the Gaussian probability measure proves (2).
The identical argument proves the uniform shifted version. This proof
uses every nonunit coefficient; it does not discard a tail after imposing
the cancellation conditions.

For the weaker hypothesis `L_D<=exp(c log(D)^2)` with a fixed `c`, the
same proof works after making the fixed `tau` also satisfy `tau^2/4>c`.

## Consequences and scope

One may choose `b_D` so that `F_D^(j)(0)=0` for finitely many `j` while
retaining `b_D(1)=1`. Equation (2) still applies, including when the
number of imposed jets grows with `D`, as long as their harmonic
coefficient resource has the displayed size. Local high-order vanishing
cannot be substituted for a power saving on the complete Mellin family.

If the total harmonic coefficient mass is `O((log D)^A)`, truncate the
Gaussian integral at

    |t| <= tau sqrt((2A+3)loglog D).

The discarded squared-norm integral is `o(1)`, by the elementary bound
`|F_D(t)|<=sum |b_D(a)|v(a)/Na`. Hence a fixed positive amount of (2)
already lies in this slowly growing height window.

More generally (2) remains a lower bound, with a changed positive
constant, for every fixed positive weight `w(t)` satisfying
`w(t)>=c exp(-t^2/tau^2)`. For example the squared modulus of any fixed
product of Gamma factors on positive fixed real lines has such a lower
bound, by Stirling's formula and positivity on compact intervals.
An arbitrary Mellin transform with zeros is not asserted to satisfy it.

This is an obstruction to cancelling **all separated outer Mellin
functionals** with a cheap finite tail. The global product-profile
identity `sum b_D(a)v(a)/Na=0` in the companion file is exact and remains
valid; it cancels its one specified residue functional. Neither result
controls the arithmetic covariance that remains after that cancellation.

The proof is analytic and elementary. No numerical fitting or finite
zero census is used.
