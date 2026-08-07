# Integration handoff — adversarial review of reflected Selberg–Möbius proposal

Frozen source:

```text
repository  gfreund123/riemann
PR          #226
head        63a4d7c0f482a57893db420e64b22f6a605c72e6
```

Review branch:

```text
agent/gpt56-pro-review-226-reflected-selberg
```

## Frozen classification

```text
L-9516 reflected coefficient algebra       VERIFIED WITH SIGN/SCOPE FIXES
L-9517 terminal contraction derivation     REJECTED
T-9509 proof of RH                         REJECTED
conditional recurrence-to-RH deduction     VERIFIED
RH                                          UNPROVED
```

## Exact content retained

1. For an invertible Dirichlet series,
   ```text
   Lambda_A=b*(a log),
   b*(a log^2)=Lambda_A log+Lambda_A*Lambda_A.
   ```
2. The conjugate-product subtraction is exact.
3. The diagonal specialization gives the global weighted Hermitian Hardy
   energy.
4. The finite Möbius resolvent is exact through its endpoint at its scalar
   scope.
5. A valid vanishing-rate lower-scale recurrence would imply RH.

## New exact repair

`L-9518` replaces the false local-block identification by the independent
frequency identity

```text
C_(t,-s)-C_t-C_(-s)=2 Lambda_t*Lambda_(-s).
```

Together with

```text
Phi_(J,alpha)(omega)
 = integral_J^(J+1) exp(2 alpha x) exp(i omega x) dx,
```

this gives the exact unit-block normal Gram through a double `(t,s)` integral.
It restores the physical orientation

```text
P_Lambda^* chi_J P_Lambda.
```

It does not prove an estimate.

## Independent blockers in the frozen proof

```text
single-frequency global energy substituted for unit block
balanced BTP(K) treated as finite induction
finite arithmetic packet interiors treated as null densities
aggregate scalar Selberg positivity applied to packet energies
no packet source map or coupled matrix equation
no strict coercivity coefficient
terminal geometry allows Omega(K) short divisor coordinates
endpoint coordinate count does not bound Mertens partial sums
no packet-level q_0=2 -> Delta_(2/3)^K M decoder
```

## Terminal/balanced correction

True complete-lattice terminal rows are already Euler-small after the corrected
source reduction on PRs #233/#235.

The exact fixed-logarithm Möbius slice cannot disappear into this easy terminal
family. Hilbert-space geometry forces at least one balanced destination to
retain the full Möbius/rightmost-zero exponent.

The remaining theorem is therefore a source-specific, signed, coupled balanced
normal-Gram contraction, not an endpoint-count theorem.

## New artifacts

```text
claims/refutations/R-9507-reflected-terminal-proof-boundary.md
claims/lemmas/L-9518-bireflected-selberg-local-block-identity.md
claims/observations/O-9513-terminal-face-dimension-and-mobius-firewall.md
experiments/X-9515-bireflected-selberg/
reports/gpt56-pro/2026-08-07-review-pr226-reflected-selberg-terminal.md
```

## Retained regression

```text
PASS_EXACT_BIREFLECTED_IDENTITY_AND_TERMINAL_GEOMETRY_MUTATION
proof-object SHA-256
c194c7cdcc5a13cf69baaed6cdf798666656b925ddfd07f614106c7a1a591165
```

## Recommended next target

Trace the exact fixed-`q_0=2` Möbius slice through `L-9518` and the corrected
terminal/balanced partition. Emit:

```text
complete tuple manifest
balanced destination of every tuple
packet source vector
all packet cross terms
two-frequency localized normal Gram
exact Selberg matrix identity
strict coercive reserve
lower-scale residual destinations
```

Only then attempt a vanishing-rate recurrence.
