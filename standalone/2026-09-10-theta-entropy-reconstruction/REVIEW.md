# Independent-review handoff

Status: new author research, not an acceptance report. No complete RH proof.
Parent: PR #842 at 8f1f457b0b92e76a0a75bd3d8a8921c205fa75b0.
New directory only; preceding manuscripts and their statuses are preserved.

## Statements to reconstruct

ER1 / PROOF Sections 2.1--2.2: for each FIXED confining even P, the displayed
finite spin laws converge to normalized exp(-P) with all moments and on every
complex MGF compact. Check N=L^(2d+1), the scale L^(-2d), the entropy coefficient
1/[2r(2r-1)], the exact Stirling prefactor, and both all-aligned configurations.
The edge region must be paid by the fixed positive entropy gap, not a central
Gaussian approximation. Verify that the lattice offset for odd N is harmless.

ER2 / Section 3: construct even rational Q_j from the actual positive density,
not from its roots; P_j=t^2+Q_j^2 must dominate t^2 globally. Check the 256 Gaussian
envelope, the positive log/sqrt arguments, the Bernstein error and the weighted
L1 bound (21). This is a paper construction; no such large polynomial or complete
large spin table was evaluated in the author session.

ER3 / Section 4: the polynomial degree is frozen BEFORE L grows for each stage.
No uniform-in-degree Stirling error is presumed. The diagonal covers every fixed
moment and complex compact. The limit is xi(1/2+h)/xi(1/2), in the unstandardized
coordinate. Standardization inserts h/sigma, not sigma*h in that formula.

ER4 / Section 5: OPEN-PAIR is an UNPROVED sufficient theorem. Full restricted
partition sums include every hidden configuration. Check the extra factor two
in normalized density ratios, the use of M_mu(R), and the two separate Hurwitz
applications for zero-weight hidden spins and the whole-source limit. No claim
that this strong comparison is necessary, feasible, or implied by RH is made.

ER5 / Section 6: check both exact four-spin polynomials, including conditional
attraction and the positive pair part of (27a), and the full-integral
sixth-cumulant enclosure for exp(-x^2/2-10^-6*x^6). These refute a GENERIC
positive-many-spin or convex-score Lee--Yang inference, not the actual theta
law. Applying ER1 to that sextic proves the same mechanism can produce non-LY
limits. The counterlaw's negative cumulant is not a native theta calculation.

## The central distinction

Nonnegative even MANY-BODY coefficients and conditional pair attraction are
not the class of zero-field PAIR Ising models with nonnegative couplings.
The construction proves membership only in the former. Treating it as the
latter would turn the manuscript into a false proof. The classical pair-only
zero theorem, by itself, does not settle this realization problem.

## Source and evidence boundaries

The exact full parent proof was read and its supplied bytes authenticated.
Its finite seed and code were not rerun. The parallel Brownian fixed-point
proposal #850 received substantive orientation on contraction and its open
zero-preservation premise; no theorem or executable from it is used here.
Ellis--Newman and Newman's 1991 paper were read at publisher abstract scope,
not subscription full-text scope. Needed entropy estimates are rederived.
Classical pair Lee--Yang, Hadamard, Hurwitz and Stirling remain named analytic
inputs. No novelty/priority investigation or full-repository audit is claimed.

The exact code compares two finite representations of spin-subset coefficients,
checks Gaussian moment remainder arithmetic, and exercises the delivery contract.
It does not machine-prove the analytic lemmas or the all-order limit. Even two
same-author implementations are not independent mathematical peer review.

## Required verdict granularity

Give separate verdicts on the positive many-spin reconstruction, its native
theta approximation, the conditional pair consumer, and the two counterexamples.
The submitted pair-realization status must remain OPEN unless a new proof of
(24), or another sufficient actual-source construction, is supplied. Do not
merge the branch as a claimed RH completion or promote the seed by inheritance.
