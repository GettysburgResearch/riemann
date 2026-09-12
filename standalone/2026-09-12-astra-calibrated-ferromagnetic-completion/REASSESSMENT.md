# What the new completion changes — and the attempted full ending

Status: proposed research synthesis, not an RH proof or an integration verdict.

## The step back

Recent finite Ising constructions match increasingly long theta moment jets.
The previous connected-chain construction separately matched the full theta
real-field growth through its h log h, h, and log h terms. It was tempting to
read the conjunction of those features as moving especially close to the full
theta law. The new completion theorem shows why that reading needs care.

A harmonic cloud can carry large total observable weight and arbitrarily
small variance. The total weight controls its eventual response to a large
magnetic field; the variance controls its influence on fixed moments and
complex compact sets. These are different limits. By using both quantities,
we can impose the desired three-term growth on ANY finite ferromagnetic core,
not only a core approximating theta.

This gives a useful positive construction: each nonsingular finite moment jet
has a connected infinite completion retaining all those moments. It also
shows that the growth calibration cannot substitute for the missing all-order
moment theorem. The full theta source is selected by its entire moment sequence,
not by three large-field coefficients and a long but finite initial jet.

## How the published strands now fit

- ICR26, #863 at 0640c9c59be0bf20c18258460a7517fb09728e82 supplies the
  272-spin seven-equation native core. Its proposed computer-assisted root and
  positive sixteenth-moment discrepancy are explicitly imported. This pass
  reread the root construction and replayed its original backend; that is not
  a new independent theta-integral implementation or external referee review.
- CTC26, #871 at 43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3 supplies the credited
  harmonic/logarithmic transfer-matrix idea. Its source file matches the earlier
  attached manuscript. The analytic ingredients needed here are reconstructed.
- The fresh #875 head be149104721ae7b65b624c100118edfd7b76b69b already supplies
  a six-moment growth-calibrated small-positive-q family. Its PR description was
  read for orientation; its complete ISING proof and numerical code were not
  independently audited or imported. We do not claim that six-moment advance.
- #842/#867/#869 and the earlier arithmetic/heat programmes appeared in the
  targeted latest-PR search. They remain context, not proof dependencies or
  newly accepted results. This was not a complete post-integration audit.

The present paper supplies a general finite-core completion theorem, rather
than refitting a particular chain. Applied to the existing seven-moment core,
it produces a connected infinite fourteen-moment law with the three theta
real-field coefficients. The explicit analytic choice N=10^1000 is deliberately
conservative. It is not an efficient implementation, a finite model with
10^1000 spins enumerated, or a numerically evaluated completed root.

## Why the attached cloud can do both jobs

Let the finite core have total positive observable weight S. The harmonic
tail starts at N and by itself has a linear-field deficit of approximately
(1/2)log N. Insert N equal small weights whose sum is A_N=(1/2)log N+O(1)-S.
Their squared sum is A_N^2/N -> 0 even though A_N -> infinity.

The added path has fixed positive nearest-neighbor correlation 1/5. Its total
variance is at most (3/2)[A_N^2/N+1/(4(N-1))]. Its complete conditional mean
seen by the core is at most A_N/(4N). Those two estimates keep every cross
term under control and make the perturbation O((log N)^2/N) on fixed disks.
At large h, however, the cloud contributes h A_N+O_N(1), exactly the amount
needed for the calibration.

The root corrector changes only the finite core weights, while the cloud sum
is recomputed from the SAME formula. It cannot accidentally destroy the
calibration. The old nonsingular Jacobian makes this correction possible
for any fixed finite jet. It does not show that one can reach a prescribed
additional moment before a singularity or a positivity boundary is met.

## Actual attempted closure

We tried to use the following implication:

    finite theta jet + real-zero models + connected infinite calibrated source
                  => exact theta source.

CFC3 disproves that implication for the constructed model itself. Its first
fourteen moments and the stated growth agree, yet its sixteenth moment does
not. There is no limiting trick in N that helps: with the core fixed, the
completed laws converge BACK to the finite core, whose sixteenth discrepancy
is positive. The variance carried by the growth-calibrating tail tends to zero.

Thus repeating the completion around this same core cannot prove RH. Making
the tiny core-connecting edges positive likewise cannot fill the missing
higher-moment coordinates.

The correct global theorem would instead supply cores Y_m satisfying, for
an unbounded sequence of m,

    J_ij^(m)>=0, a_i^(m)>=0,
    |E Y_m^(2r)-mu_(2r)|<=2^-m for all 1<=r<=m.             OPEN-CFC

The target mu is the UNCHANGED complete theta law. Every model is zero-field.
The variance bound then pays all complex Taylor tails. For each m choose a
calibrated completion so accurate on the disk |z|<=m that the additional
error is <=2^-m. CFC1 makes this second selection possible. The resulting
entire functions converge to Xi/Xi(0), and Hurwitz would prove RH.

OPEN-CFC is NOT proved here. Calibration and connectivity have been made
available uniformly for each fixed feasible core; they do not establish
arbitrary-order finite feasibility. The new closure equality in Section 8
makes this distinction exact rather than rhetorical.

## What would count as a decisive next theorem

The most important unresolved mathematical question is target-containing
reachability for the finite positive-coupling moment map. One needs a global
argument, using the actual theta moment sequence, that continues through
weight collisions and changing graph size without leaving J>=0 and a>=0.
An invertible Jacobian gives a neighborhood of the current model's moments,
not a proof that theta's next moment is inside that neighborhood.

A universal assertion for all positive even densities would be false: many
such densities have nonreal Fourier zeros. Any proposed reachability induction
must therefore identify and exploit a genuinely source-specific property,
not just positivity of the moment matrix or more available parameters.

The completed global reference model and its complete cutoff bound remain
useful tools. They are not a replacement for that arithmetic selection theorem.
No new zero-free region or full RH proof is obtained in this pass.
