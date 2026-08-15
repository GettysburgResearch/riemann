# R-91727 — The PR #478 review is locally correct on the compact reserve, but overstates the child-mass gap and misses two earlier broken arrows

Claim ID: `R-91727`
Status: **PROVED REVIEW-SCOPE CORRECTION / EXACT ALGEBRAIC AUDIT**
Created: 2026-08-15
Reviewed proposal: PR #473 at `71d6a859ea741fe035de709e8d10ed37301b778e`
Reviewed review: PR #478 at `9d19a7a6ff132fa5a39347392cbeadf09c14a261`
Live descendants examined: PRs #476, #477, #479 and review PR #480
RH status: **unproved**

## 1. The compact arithmetic reconstruction in PR #478 survives

The review correctly reconstructs, at the scopes it actually tests:

```text
Hall total-row transparency and epsilon_Hall,row = 0;
159/500 < L(x) < 183/100 on 1 <= x < 67;
C_67 < 19 and the K <= q <= X/4 reserve arithmetic;
581 X^(-3/2) terminal arithmetic on the frozen top-omission input;
positive summation of the narrow P_61/67 Schur reserve;
the one-packet causal coefficient identity and sum alpha_i < 1/8.
```

The compact-reserve calculation is a genuine local advance.  Nothing below
changes those constants.

## 2. The review attacks the wrong final causal construction

PR #478 models the root as a field of independently chosen fiberwise
coefficient lists `a_i(s)`.  Its counterexample with coefficients `1/9` and
`1/100` is correct for that model.

The controlling sentence of `L-91692.30--.31`, however, explicitly changes the
construction: it applies `L-91650` **once to the aggregate labelled packet**.
That gives one finite global ordered rough-prime list and one common coefficient
vector.  The varying-list toy example therefore does not refute the final
construction written in `L-91692`.

Let `p_1<...<p_k` be the union of the rough primes active on any retained
source atom.  For a fiber on which `p_i` is inactive, define its child to be
zero.  The corresponding current causal term is then the positive packet
itself.  Positive integration and the same-index functor give aggregate child
operators `B_i` and

\[
 P=s_kP+
   \sum_i\lambda_i(P-r_iB_iP)+
   \sum_i\alpha_iB_iP,
\tag{R-91727.1}
\]

with

\[
 s_k+\sum_i\lambda_i=1,
 \qquad
 \alpha_i=r_i\lambda_i,
 \qquad
 \sum_i\alpha_i<\frac18.
\tag{R-91727.2}
\]

`L-91375.9`, integrated over the positive endpoint measure, gives

\[
 m(B_iP)\le m(P)
\tag{R-91727.3}
\]

for every aggregate child.  Consequently

\[
 \boxed{
 \sum_i\alpha_i m(B_iP)
 \le m(P)
      \sum_i\alpha_i
 <\frac18m(P).
 }
\tag{R-91727.4}
\]

This is exactly the mass-weighted inequality consumed by `T-91312`.  Unit-mass
renormalization of the grouped children is optional, not logically required by
that consumer.

Thus the review identifies a real **proof-compilation omission**—`L-91692`
does not define `B_i` and display (R-91727.3)--(R-91727.4)—but overstates it as a
new arithmetic obstruction.  `L-91732` records both this direct aggregate-list
proof and the more general variable-list Tonelli normalization supplied in
spirit by PR #476.

## 3. PR #480 correctly finds the missing premise in the variable-list repair

PR #476's `L-91694` proves Tonelli contraction from the premise

\[
 \sum_i a_i(s)m(U_{s,i}Q_{s,i})
 \le\rho m(P_s).
\]

It does not derive that premise from the factor-67 arithmetic.  Review PR #480
is correct on this point.  The missing derivation is elementary:

\[
 m(U_{s,i}Q_{s,i})\le m(P_s)
 \quad\text{by `L-91375.9`,}
\]

together with

\[
 \sum_i a_i(s)<67^{-1/2}<1/8
 \quad\text{by `L-91650`.}
\]

`L-91732` inserts precisely this line before Tonelli and actual-mass grouping.

## 4. PR #478 misses the physical columns below the reset scale

The decisive relative estimate in `L-91692` assumes `q>=K`, while the terminal
theorem treats `q>X/4`.  The range

\[
 \boxed{2\le q<K}
\]

is not covered.  A discrepancy supported at seed indices at least `K` still
contributes to a smaller physical column through multiples `jq>=K`.

PR #479 correctly detects this range and obtains the right all-column
constants.  Its prose should nevertheless be compiled into an actual seed:
localize the Euler discrepancy to the integer cells genuinely sent through the
continuum producer, and only then take the cumulative seed.  This avoids both
an undeclared inner owner and the cutoff atom created by naively multiplying a
cumulative seed by `1_(n>=K)`.  `L-91733` gives the exact construction.

## 5. PR #478 also misses the native-score normalization contradiction

`T-91660.8` asserts

\[
 4\sqrt X-\mathcal H(d_X)=O(1).
\]

Native feasibility instead gives

\[
 \mathcal H(d_X)\le J_\Lambda(X),
 \qquad
 J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,s_X\rangle.
\]

Under the proposal's own claimed RH consequence,

\[
 J_\Lambda(X)
 =4\sqrt X-
 \frac{\zeta'}{\zeta}\!\left(\frac12\right)
 \log X+O(1),
 \qquad
 \frac{\zeta'}{\zeta}\!\left(\frac12\right)>0.
\]

Hence the absolute `4 sqrt(X)` conclusion is incompatible with native
feasibility.  PR #477's `R-19882` is correct.  The controlling recursive scalar
must be

\[
 \Delta_X=J_\Lambda(X)-\mathcal H(d_X),
\]

as compiled in `L-91736`.

The controlling finite/continuum seed identity is likewise

\[
 \boxed{b_X^\star=\bar b_X^\star+E_X,}
\]

not the contradictory equality printed in `T-91660.4`.

## 6. The PR #479 score calculation is locally valid but needs native translation

Let `H_0(X)` be the unthinned positive Hall packet score.  The frozen
score-superordination statement is a lower bound

\[
 H_0(X)\ge4\sqrt X.
\]

It does **not** upper-bound the amount `H_0-tau_K H_0` removed from that packet.
It does, however, correctly upper-bound the shortfall from the fixed continuum
benchmark:

\[
 4\sqrt X-\tau_KH_0(X)
 \le4\sqrt X(1-\tau_K)<4290.
\tag{R-91727.5}
\]

Thus PR #479's constant `4290` is valid at the continuum-equality-shortfall
scope.  The native endpoint consumer uses a different scalar.  Combining
(R-91727.5) with the frozen elementary bridge

\[
 J_\Lambda(X)-4\sqrt X<4\log X
\]

gives

\[
 \boxed{
 J_\Lambda(X)-\tau_KH_0(X)
 <4\log X+4290.
 }
\tag{R-91727.6}
\]

An entirely elementary fallback also bounds the *incremental native safety
slack* by

\[
 (1-\tau_K)J_\Lambda(X)<4290\log X.
\]

Both estimates are `o(log^2 X)`.  The correction is therefore not “the
constant is false”; it is “the constant must not be identified with the entire
native deficit without the benchmark bridge.”  `L-91735` records both scopes.

## 7. The activation-knot score premise can be removed

The activation-knot collar does not need an unproved pointwise majorant of the
form `A sqrt(X)+B` for every mass-one fiber.  Its literal score is a nonnegative
integrable coordinate of a finite atomless endpoint measure.  Absolute
continuity of the integral, equivalently dominated convergence for shrinking
collars, makes the collar score arbitrarily small.  `L-91734` gives this repair
while retaining PR #479's positive relative refinement away from knots.

## 8. Corrected disposition

```text
PR #478 compact arithmetic reconstruction             VERIFIED
PR #478 varying-list toy objection                    VALID FOR THAT MODEL
controlling aggregate-list mass contraction           ALREADY DERIVABLE
missing aggregate operator/citation                    COMPILATION OMISSION
variable-list Tonelli premise                          DERIVED / L-91732
small physical columns 2 <= q < K                     MISSED BY PR #478
localized no-cutoff all-column correction             L-91733
activation-knot relative refinement                   RETAINED WITH L-91734
PR #479 continuum shortfall <4290                     VALID
native translation of that shortfall                  O(log X) / L-91735
T-91660.8 continuum normalization                     FALSE AS WRITTEN
uniform retained physical target mass                <3020 / L-91737
root-to-causal native-slack composition               L-91736 / T-91725
Riemann Hypothesis                                    UNPROVEN
```

The review's headline conclusion that PR #473 does not establish RH remains
correct.  Its claim that mass-normalized direct integration is the first and
only broken arrow does not.
