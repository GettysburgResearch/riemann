# Parabolic carry continuation: monotone cover refuted, signed constraint dipole isolated

Date: 2026-08-07  
Agent: `gpt56-pro-22`  
Issue: #253  
Base reviewed: PR #248 at `c2a34e282f65ca0d890dc55e5e2fba08bed140c9`

## Executive result

The parabolic seed remains one of the strongest elementary coordinates in the
repository: it carries the full `4 sqrt(X)-O(log X)` objective before
arithmetic repair.

However, the proposed monotone Divisibility Cover cannot preserve that
constant. Exact von-Mangoldt duality charges every nonnegative covering atom,
and the seed has a uniformly positive constraint-excess band on

```text
X/40 <= q <= X/37.
```

The resulting cover cost is at least

```text
sqrt(X)/4000
```

for all sufficiently large `X`.

Thus route A of PR #248 is refuted.

## New structure

The seed simultaneously has square-root positive defect and square-root
negative slack, while their signed difference is only `o(sqrt(X))`. The
correct picture is a macroscopic constraint dipole.

A successful proof must transport defect into slack through the exact signed
adjacent-flow or primitive-neighbor matrix. It cannot delete positive defect
with a nonnegative tail cover.

The exact surviving theorem is:

```text
construct a signed flow
-> keep every repaired b_m nonnegative
-> make every prime-power constraint feasible
-> pay only X^epsilon objective cost
-> prime ramp >= 4 sqrt(X)-X^o(1)
-> square-screw/Landau
-> RH.
```

No such transport is proved in this continuation.

## Exact replay

`X-25301` uses only integers and `fractions.Fraction`. It proves:

```text
E(theta)>2/5 on [1/40,1/37]
formal von-Mangoldt/divisibility dual rows through 128
eventual monotone-cover cost >= sqrt(X)/4000
5/5 fail-closed tests
```

Proof-object SHA-256:

```text
9eb7d95d872332d5830eb027e786319084aab2ea4a7e22909a0791ef35a5c690
```

## Corrected status

```text
parabolic seed                           retained
reciprocal-cell calculus                 strengthened / exact band certified
monotone Divisibility Cover              refuted
primitive-neighbor and adjacent flow     retained
signed constraint-dipole transport       open
RH                                       unproved
```
