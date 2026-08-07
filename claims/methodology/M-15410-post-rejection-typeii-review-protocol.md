# M-15410 — Fail-closed review protocol for the post-Farey Type-II proposal

Methodology ID: `M-15410`  
Title: Freeze, replay, and either verify or reject the terminal-closed high-order Type-II architecture without importing the failed Farey ledger  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `R-15407`, `L-15449`, `L-15450`, `T-15415`

## 1. Required frozen dependencies

A review must record exact heads for:

```text
PR #165  replacement proposal branch
PR #158  high-order safe window and Heath--Brown packet
PR #216  prime/full-Lambda Hardy energy source
PR #219  difference-squared Selberg identities
PR #229  first-cell Mertens decoder and generic-operator no-go
PR #233  finite Möbius resolvent and terminal packet schema
```

No later branch head inherits a frozen verdict automatically.

## 2. Review the refutation first

Before reviewing the replacement, reproduce:

1. the true solution step `(q/g,v/g)` for `av-bq=r`;
2. the `q=v=5,r=5` missing-chain example;
3. the cotangent residue for `v=q+1,r=1`;
4. the first-cell Mertens decoder.

This prevents accidental reuse of the rejected local-to-Bohr argument under a
new notation.

## 3. Terminal Euler theorem

For `L-15449`, verify independently:

1. the change of variables in the continuous lattice integral;
2. the exact use of the half-pole moments;
3. the first periodic-Bernoulli/Euler formula for a compact BV function;
4. the derivative calculation and cancellation of `A`;
5. the exponent ledger `-1/2+delta` for amplitude and `-1+2delta` for energy;
6. the initial-endpoint condition and finite-row separation.

A reviewer should test piecewise-linear windows with derivative jumps. The
proof uses bounded variation and must not silently assume global `C^1`.

## 4. Terminal normal form

For `L-15450`, emit the complete finite type graph at several orders. The
checker must reject:

```text
same-scale Type-I cycle
unchanged complexity rank
truncated variable declared terminal-large
missing unrestricted-variable range
undeclared first-crossing boundary
coefficient mass larger than the divisor ledger
```

Mandatory stress cases should include:

- all small variables equal to one;
- the crossing occurring at the final unrestricted variable;
- a large suffix with two unrestricted variables, which must reduce rather than
  be called terminal;
- a residual Möbius coefficient expanded in both direct and divisor forms.

## 5. Balanced Type-II theorem

`T-15415` is not complete until BTP(K) is supplied. Every proposed BTP(K)
certificate must contain:

```text
complete signed source packet
normal/factor-ratio orientation
null companion and proof of null membership, if used
all cutoff and transition residuals
linear or tensor auxiliary-energy destination
strict logarithmic scale bound
coefficient exponent epsilon_K
fixed reserve delta or tensor kappa_K
first-cell Mertens mutation output
source and window digests
```

Reject any proof that applies total variation before recombining all signed
Heath--Brown indices assigned to the same destination.

## 6. Cross-route mutation tests

A passing balanced theorem must imply all of the following through explicit
maps, not prose analogy:

1. the fixed-ratio square-root Mertens increment of PR #229;
2. subexponential prime-only safe-window energy of PR #216;
3. the rightmost-zero exponent zero through the Hardy transfer;
4. the analytic-totient critical second moment through `L-15447`, if that route
   is claimed as an output.

Failure of the first mutation is decisive: it means the coherent critical cell
has been discarded.

## 7. Allowed classifications

```text
VERIFIED
    every source identity, terminal theorem, BTP(K), rate, and Hardy transfer
    passes at the frozen commits;

VERIFIED WITH FIXES
    the proof survives but named non-load-bearing repairs are mandatory;

GAP/BLOCKED
    terminal theorem passes, but BTP(K) or its vanishing rate is absent;

REJECTED
    a load-bearing identity, scale destination, source orientation, or
    first-cell mutation fails.
```

A repaired theorem is a new proposal and does not retroactively verify the
frozen object.

## 8. Current expected classification

At publication of this protocol:

```text
R-15407                         PROPOSED REFUTATION
L-15449/L-15450                 PROPOSED COMPLETE SUBTHEOREMS
T-15415 architecture            PROPOSED
BTP(K)                          OPEN
RH                              UNPROVED
```

The correct current classification of the replacement is therefore
`GAP/BLOCKED AS A PROOF`, while remaining a serious full proposal with a
strictly smaller hinge than the rejected Farey route.
