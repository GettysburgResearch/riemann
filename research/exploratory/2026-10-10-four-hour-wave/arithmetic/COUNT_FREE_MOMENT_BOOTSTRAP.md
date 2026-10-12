# Bootstrap a source-bound real census with a higher complete moment

Status: **Proposed analytic component B-C1--B-C3, pending independent
review.** This generalizes the new count-free moment exclusion mechanism;
it supplies no additional native height by itself. A new height requires
its own directed actual-source coefficient and finite-root interval guard.
No global real-zero or RH statement is made.

Exact sources: `xi/outer-ray/COUNT_FREE_CENSUS_RECOVERY.md` CF1--CF9,
the complete paired Xi product in `xi/outer-ray/THEOREM.md`, and the
source-qualified finite sign facts. The initial count-free packet recovers
H_0=2240 without a historical zero-count input. This note retains the
same distinction between primitive signs, complete moments and analytic
product hypotheses.

What was actually run: analytic derivation. The approximate proposed
degree-eight planning values mentioned below are ordinary reconnaissance,
not a certificate. No new native jet or root bracket is produced here.

## B-C1. Previous completeness moves the entire residual sector

Let F(z)=Xi(z), and retain its complete multiplicity-preserving zero
strip |Im rho|<=A, its even real paired product and F(0)>0. Suppose an
authenticated finite set of disjoint positive real sign-change intervals
provides a selected root gamma_j in each interval, **one occurrence** per
interval. Evenness removes its opposite occurrence as well.

Assume independently proved completeness and simplicity at a positive
height H_0: every actual zero with |Re rho|<=H_0 is one of these selected
real roots or its reflection, and each selected root there is simple.
This is the conclusion already recovered by CF9; no initial uniqueness
outside H_0 is assumed. Thus every zero occurrence remaining after the
whole finite selected list is removed has |Re rho|>H_0. Extra roots and
extra multiplicities in intervals above H_0 remain in the source.

For any integer k>=1 the exact complete residual moment is

    T_k=-k[z^(2k)]log(F(z)/F(0))-sum_j gamma_j^(-2k)
       =sum_(remaining Re rho>H_0) m_rho rho^(-2k).        (B-C1)

Nonreal conjugates are both retained; all sums converge absolutely by the
complete paired product. The equality uses the chosen actual root in each
sign interval, not its midpoint or a putative complete census above H_0.

## B-C2. An exact rational phase and exclusion guard

Choose k satisfying the simple sufficient guard2kA<H_0. Then
2k arctan(A/H_0)<1<pi/2. Define

    c_k(H_0,A)=cos(2k arctan(A/H_0))
      =sum_(j=0)^k (-1)^j binomial(2k,2j)
          H_0^(2k-2j) A^(2j)/(H_0^2+A^2)^k >0.           (B-C2)

For rational H_0,A this is an exact rational number. Every remaining
positive-half-plane root satisfies

    Re(rho^(-2k)) >=c_k(H_0,A)|rho|^(-2k),

because its argument has absolute value at most arctan(A/H_0) and cosine
decreases in the stated acute interval. Conjugation makes T_k real.
Therefore

    T_k>=c_k sum_(remaining Re rho>H_0)m_rho|rho|^(-2k)>=0. (B-C3)

Suppose an actual directed coefficient/root-interval computation encloses
T_k for every allowed selected gamma_j, with upper endpoint U_k. Let
H_1>=H_0 satisfy the strict guard

    U_k (H_1^2+A^2)^k <c_k(H_0,A).                       (B-C4)

Then the selected list is complete and simple in |Re rho|<=H_1.
Indeed a remaining occurrence with0<Re rho<=H_1 has
|rho|^2<=H_1^2+A^2 and contributes at least
c_k/(H_1^2+A^2)^k to(B-C3). All other contributions remain nonnegative,
contradicting(B-C4). Additional multiplicity at any selected point in that
height is also a remaining occurrence and is excluded by the same argument.
The exclusion includes the boundary; requiring no selected interval to meet
H_1 makes the interval inventory identify the retained roots unambiguously.

This proof may be iterated: once a new height has passed, it supplies the
H_0 premise for a later complete moment. Larger k can become admissible
because the entire residual sector has moved, rather than because a finite
sample suggests the unknown roots are real.

## B-C3. A bounded native degree-eight route

The reviewed count-free height2240 supplies H_0=2240 and A=1/2.
For k=4 the simple guard is4<2240; the exact phase is

    c_4=[H_0^8-28H_0^6 A^2+70H_0^4 A^4
                     -28H_0^2 A^6+A^8]/(H_0^2+A^2)^4.   (B-C5)

A new degree-eight native logarithmic jet and a complete selected-root
inverse-eighth interval sum could then test(B-C4). The first111 brackets
at width2^-80 alone may not resolve that subtraction; refining a larger
low prefix while replaying every new actual Hardy-Z endpoint would lower
that finite interval uncertainty. The unchanged high brackets remain
full intervals and their strict sign facts remain explicit imports.

Ordinary scale estimates suggest a prefix through512 and a candidate
height near3300 could be affordable. These are planning values only.
They authenticate neither U_4 nor(B-C4), and no new finite census or
derivative column is claimed by this note. A separate checker must bind
the full selected inventory, native jet, previous count-free premise,
all new bracket signs, exact positive phase and strict complete-height
exclusion. It need not call a historical zero-count routine.
