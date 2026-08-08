# Central carry cascade: post-review full proposal

Date: 2026-08-08  
Branch: `research/gpt56-sol/277-central-carry-cascade`  
Base: PR #247 at `fb69b22bb3a29e5709f9927d129ef968c2d04fb9`  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL; ONE EXPLICIT LATTICE-STABILITY THEOREM OPEN**  
RH: **UNPROVED**

## 1. Why this route was selected after refreshing the graph

The newest post-PR-251 work sharpens several former endgames but also identifies
which ones have become canonical restatements of the RH-bearing scalar.

In particular:

- PR #276 proves its WSTS scalar is equivalent to RH.  It is an excellent final
  reduction, but not a promising place to hide a missing easy lemma.
- PRs #263/#269/#271 consolidate the parity/factor-five reflected route, but the
  final physical boundary/source-image recurrence remains open.
- PRs #270/#274 identify finite Green and squarefree-collector transports, but
  their logarithmic dual mode remains the actual prime-ramp deficit.
- PR #272 gives a major structural simplification: every balanced exact carry
  flow is an explicit canonical tree plus Pascal cycles, and only optimized
  negative capacity debt matters.
- PRs #247/#277 expose a fully explicit fragmentation producer and the first
  unconditional positive packing with constant `4 log 2`.

The last pair provides a route where the missing theorem can be attacked without
introducing a new zeta-equivalent scalar: reuse the already-positive carry atoms
and understand their exact residual.

## 2. New exact finite result

For the central split, the carry indicator is periodic in the parent:

```text
chi_n(q)=1 iff n mod 2q lies in [q,2q-2].
```

Therefore the first-difference packing for any decreasing target `r` leaves the
exact residual

```text
(T_X r)(q)
 = sum_(k>=1) [r(2kq-1)-r((2k+1)q)].
```

For the critical target

```text
w_X(q)=q^(-1/2) log(X/q),
```

the function

```text
h_X(t)=-t w_X'(t)
      =t^(-1/2)[1+(1/2)log(X/t)]
```

is decreasing.  This proves each residual summand is decreasing in `q` and
hence the complete first residual is again decreasing.

So the one-pass packing of PR #247 can be applied **a second time
unconditionally**.

The resulting prime-power ramp lower bound is

```text
prime_ramp(X)
 >= 4 log(2) (2-log(2)) sqrt(X) - O(log^2 X).
```

This improves the prior unconditional constant

```text
4 log 2
```

to approximately

```text
3.624.
```

This is a genuine new theorem, not a conditional RH reformulation.

## 3. The continuum mechanism closes completely

The continuum residual is

```text
(T f)(x)=sum_(k>=1)[f(2kx)-f((2k+1)x)].
```

It has exact mass factor

```text
integral T f = (1-log 2) integral f.
```

For

```text
W(x)=x^(-1/2)log(1/x)
```

all logarithmic derivatives satisfy

```text
D^m W(x)
=x^(-1/2)[2^-m log(1/x)+m 2^(1-m)]>0,
D=-x d/dx.
```

Since `D` commutes with `T`, every continuum residual remains in the positive
monotonicity cone.  Iterating central extraction therefore recovers

```text
4[1-(1-log 2)^J]
```

after `J` stages and the full constant `4` in the limit.

Thus there is **no continuum positivity obstruction**.

## 4. The exact finite cascade also closes algebraically

The discrete operator differs from the continuum one only by

```text
(E f)(q)=sum_(k>=1)[f(2kq-1)-f(2kq)].
```

This is the lattice endpoint commutator created by the forced noncarry site
`2q-1`.

Iterating the exact discrete residual, and at each stage placing its signed
first differences on central splits, gives an exact signed carry saturation.
The support halves at every stage, so after `ceil(log_2 X)+1` stages the residual
is identically zero.

The full finite problem has therefore been reduced to one issue:

```text
how much negative first-difference mass is created by repeated lattice
commutators?
```

PR #272's cycle-debt theorem makes this quantity directly meaningful: it is a
primal upper bound for the optimized negative capacity debt, and Pascal cycles
may repair it without altering the carry target.

## 5. New preferred theorem: DCCS

Define the explicit cascade residuals `r_j` and the capacity-weighted negative
debt

```text
D_cas(X)
 =sum_j sum_n omega_n [r_j(n+1)-r_j(n)]_+.
```

The proposed theorem is

```text
DCCS:
D_cas(X)=X^o(1).
```

The strongest desired form is `O(log^A X)`.

This is narrower than general BCT/CDT and more concrete than a new RH-equivalent
sampling statement.  Every quantity is generated from floors, square roots,
logs, and the explicit central carry pattern.

The initial commutator already satisfies

```text
sum_q sqrt(q) E w_X(q) << log^2 X.
```

The missing estimate is uniform stability under the remaining `O(log X)`
support halvings.

A sufficient recurrence is a weighted variation norm `V_j` with

```text
V_(j+1)
 <= rho_* V_j + polylog(X,j),
rho_*<1.
```

An alternative proof may repair each negative central edge by the explicit
balanced Pascal cycles of PR #272 and show the total cycle capacity is
subpower.

## 6. Full conditional spine

```text
central first-difference carry atoms
-> exact alternating-block residual T_X
-> unconditional second positive stage
-> continuum contraction rho=1-log2
-> exact finite support-halving signed cascade
-> DCCS lattice-debt estimate
-> PR #272 capacity/entropy adapter
-> prime ramp = 4 sqrt(X)+X^o(1)
-> square-screw/Landau
-> RH.
```

Only DCCS is open in the new part of this chain.

## 7. Why this is preferable to the canonical equivalent scalars

This proposal deliberately does not attack WSTS directly.  PR #276 shows WSTS
is equivalent to RH, so an estimate of WSTS by another name would add no
mechanism.

DCCS instead separates an exactly solved continuum contraction from a finite
lattice error.  If DCCS turns out false, its failure produces explicit bad
stages and edge locations and can be fed directly into the Pascal-cycle repair
space.  This makes the proposal falsifiable and generative even before closure.

## 8. Correct boundary

```text
post-review proof graph refresh                 COMPLETE FOR RELEVANT LIVE FRONTS
central residual identity                       PROPOSED COMPLETE
critical first-residual monotonicity             PROPOSED COMPLETE
unconditional two-pass carry packing             PROPOSED COMPLETE
improved constant 4 log2(2-log2)                PROPOSED COMPLETE
continuum infinite cascade                       PROPOSED COMPLETE
exact finite signed support-halving cascade      PROPOSED COMPLETE
initial lattice commutator polylog bound         PROPOSED COMPLETE
DCCS all-stage lattice stability                 OPEN / LOAD BEARING
DCCS -> sharp prime ramp -> RH                   COMPLETE CONDITIONAL COMPOSITION
Riemann Hypothesis                               UNPROVED
```

## 9. Review order

1. `claims/lemmas/L-27701-central-carry-residual-and-unconditional-two-pass-packing.md`
2. `claims/lemmas/L-27702-continuum-central-cascade-and-lattice-commutator.md`
3. `claims/theorems/T-27701-discrete-central-cascade-stability-rh-proposal.md`
4. `claims/methodology/M-27701-central-cascade-production-and-review-protocol.md`
5. PR #272 `L-27204/L-27205`
6. PR #247 `L-23808/L-23810/L-23814` and square-screw/Landau consumer
