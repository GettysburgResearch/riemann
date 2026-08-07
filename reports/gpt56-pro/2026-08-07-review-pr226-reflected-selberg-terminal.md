# Adversarial review of PR #226: reflected Selberg–Möbius terminal proposal

Reviewer: `gpt56-pro`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Frozen PR: `#226`  
Frozen head: `63a4d7c0f482a57893db420e64b22f6a605c72e6`

## Executive verdict

The proposal contains one genuine exact advance: the conjugate-product Selberg
identity converts the analytic square into a Hermitian product. Its diagonal
specialization is correct, and the finite Laurent-polynomial regression checks
the coefficient algebra within its declared scope.

The proposal is nevertheless rejected as a proof of RH. The advertised
absolute endpoint-count assertion is not the only missing theorem and, even if
proved as a geometric statement, would not imply the terminal estimate claimed
in `L-9517`.

The independent blockers are:

1. the single-frequency vertical integral is a global exponentially weighted
   all-line energy, not the unit logarithmic block used by the packet recurrence;
2. the proof treats the open balanced Type-II theorem as though finite
   complexity induction had already proved it;
3. the high-order null quotient kills continuous polynomial-exponential
   densities, not arbitrary finite Möbius/residual packet interiors;
4. scalar aggregate Selberg positivity does not control packet self-energies
   without an exact packet source map or a coupled matrix equation;
5. terminal scale geometry permits `Omega(K)` short divisor coordinates;
6. endpoint-coordinate counting does not estimate the Mertens partial sum that
   appears when the long coefficient retains the Möbius source;
7. no coercive coefficient is computed when the “Hermitian diagonal” is moved
   to the energy side;
8. the claimed packet-level `q_0=2 -> Delta_(2/3)^K M` decoder is not supplied.

The target estimates may still be true. The frozen derivation does not prove
them.

## Classification

```text
L-9516 generalized Selberg identity         VERIFIED WITH SIGN FIX
L-9516 reflected conjugate subtraction      VERIFIED
L-9516 global vertical Plancherel identity  VERIFIED WITH SCOPE FIX
L-9516 unit-block identification            REJECTED
X-9514 finite algebra regression            VERIFIED WITH DECLARED SCOPE
finite Möbius resolvent                     VERIFIED AT SCALAR SCOPE
balanced packet elimination                 REJECTED
terminal null-quotient reduction            GAP/BLOCKED
packet Selberg absorption                   GAP/BLOCKED
absolute endpoint count C_*                 GAP/BLOCKED
C_* count -> terminal recurrence            REJECTED
q_0=2 packet-to-Mertens decoder             GAP/BLOCKED
conditional recurrence -> RH               VERIFIED
T-9509 as a proof of RH                     REJECTED
RH                                           UNPROVED
```

## Exact algebra retained

For an invertible Dirichlet series

```text
A=sum a(n)n^-s,
B=A^-1=sum b(n)n^-s,
```

and

```text
-A'/A=sum Lambda_A(n)n^-s,
```

the correct first identity is

```text
Lambda_A=b*(a log),
```

not the negative version stated in the prose of `L-9516`. The second identity is
correct:

```text
b*(a log^2)=Lambda_A log+Lambda_A*Lambda_A.
```

For independent real frequencies `t,s`, applying it to

```text
zeta(w+it),
zeta(w-is),
zeta(w+it)zeta(w-is)
```

gives exactly

```text
C_(t,-s)-C_t-C_(-s)=2 Lambda_t*Lambda_(-s).
```

The diagonal `s=t` produces the Hermitian square.

## Localization audit

Write

```text
Q_H(x)=sum Lambda(n)/sqrt(n) H(x-log n),
F_alpha(t)=Hhat(alpha+it)[-zeta'/zeta](1/2+alpha+it).
```

Plancherel gives

```text
integral |F_alpha(t)|^2 dt
 =2 pi integral exp(-2 alpha x)|Q_H(x)|^2 dx.
```

This is an all-line weighted energy. It contains no output-block parameter
`J`. Compact support of the autocorrelation restricts factor ratios but not the
common arithmetic scale.

A unit block requires

```text
B_J=(2 pi)^-2 double_integral
    F_alpha(t) conjugate(F_alpha(s))
    Phi_(J,alpha)(t-s) dt ds,
```

where

```text
Phi_(J,alpha)(omega)
 =integral_J^(J+1) exp(2 alpha x) exp(i omega x) dx.
```

This observation led to the exact repair `L-9518`. Its two-frequency reflected
identity recovers the physical factor-ratio normal Gram exactly. It supplies no
upper bound by itself.

## Dependency audit

The corrected version of PR #233 explicitly states that finite complexity
induction only composes already-proved inequalities. A balanced row must first
satisfy a source-specific estimate `BTP(K)`, which remains open and RH-bearing.

The corrected scalar Selberg adapter on the same PR explicitly records the
packet-source firewall: aggregate scalar positivity cannot be applied to
packet-specific self-energies without either an exact packet source map with all
cross terms or a coupled vector/matrix Selberg equation.

PR #158's exact fixed-log decoder proves that the `q_0=2` slice is an exact
Möbius safe signal. Any fixed finite packetization leaves at least one packet
with the full Möbius energy exponent. Thus balanced packet control cannot be
removed by naming a destination or by finite bookkeeping.

## Terminal-face mutation

At reserve `delta=1/5`, set

```text
V=X^(1/K),
j_K=floor(K/5)-1.
```

One expanded resolvent row may contain `j_K` short residual/divisor coordinates
of scale approximately `V`, whose total product remains below `X^(1/5)`, and
one terminal-large coordinate filling the remaining scale.

After the long-variable endpoint is taken, the short face remains parametrized
by `j_K=Omega(K)` divisor coordinates. `X-9515` checks this scale family at
orders `20,30,50,100,200`.

This is not a no-cancellation theorem. It proves that an absolute `C_*`
independent of `K` does not follow from terminality, spline degree, high-order
moments, or finite complexity alone.

## Mertens firewall

There is a sharper obstruction than dimension.

If the final long variable is a true complete-lattice coordinate with
polynomial logarithmic coefficient, the terminal Euler theorem closes it
unconditionally with exponential decay.

If its coefficient still contains the Möbius source, Abel summation leaves a
Mertens partial sum. In the claimed scalar mutation this is

```text
G_K(D)=Delta_(2/3)^K M(D).
```

For every fixed `K`, the square-root bound for `G_K` is RH-equivalent. Counting
short endpoint coordinates does not estimate it. Even a zero-dimensional
endpoint would still require arithmetic cancellation in the remaining scalar
coefficient.

The corrected scalar theorem `L-23202` explicitly says that no packet-level map
to `G_K` has been supplied. `L-9517` asserts such a map without a tuple ledger,
cutoff equality, or equality of physical block kernels.

## Missing coercivity

The reflected identity has the form

```text
2 E = forcing.
```

To derive an estimate after a diagonal is recognized inside the forcing, one
needs an exact relation such as

```text
2 E = kappa E + R,
kappa<2,
```

or a matrix inequality with a strict positive reserve. `L-9517` computes no
`kappa`, no sign, and no packet matrix. Moving an exact copy of `2E` to the
left would simply cancel the identity.

This is a distinct gap from endpoint enumeration.

## Positive continuation

The corrected durable spine is

```text
exact reflected Selberg algebra
-> two-frequency local-block identity L-9518
-> exact finite signed packetization
-> complete-lattice terminal Euler closure
-> coupled signed balanced Type-II normal-Gram theorem
-> strict lower-scale recurrence
-> RH.
```

The next proof attempt should not enumerate all endpoint faces first. It should
trace the exact fixed-`q_0=2` Möbius slice into the localized two-frequency
normal Gram, emit the complete coupled packet matrix, and seek a strict coercive
inequality for that one RH-bearing balanced destination.

## New artifacts

```text
claims/refutations/
  R-9507-reflected-terminal-proof-boundary.md

claims/lemmas/
  L-9518-bireflected-selberg-local-block-identity.md

claims/observations/
  O-9513-terminal-face-dimension-and-mobius-firewall.md

experiments/X-9515-bireflected-selberg/
  verify.py
  README.md
  results/verification.json
```

Retained regression verdict:

```text
PASS_EXACT_BIREFLECTED_IDENTITY_AND_TERMINAL_GEOMETRY_MUTATION
proof-object SHA-256
c194c7cdcc5a13cf69baaed6cdf798666656b925ddfd07f614106c7a1a591165
```

## Frozen conclusion

```text
PR #226 at 63a4d7c0...       REJECTED AS A PROOF OF RH
exact reflected algebra      RETAINED
local two-frequency adapter  SUPPLIED
terminal Euler subclass      RETAINED FROM CORRECTED DEPENDENCIES
balanced packet theorem      OPEN / RH-BEARING
RH                            UNPROVED
```
