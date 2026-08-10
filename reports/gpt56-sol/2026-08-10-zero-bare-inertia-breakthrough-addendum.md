# Addendum — zero-bare Q4 source removes the local polarized-sign bottleneck

Date: 2026-08-10  
Branch: `research/gpt56-sol/90300-claude-inertia-q4`  
Parent report: `2026-08-10-claude-two-thirds-crossfertilization-and-q4-attack.md`  
Status: **new cofinal row theorem; global RH recurrence still open**

## 1. What changed after the first inertia reduction

The first version of this branch reduced the two-state polarized Q4 matrix to one determinant/Wronskian defect but still left that defect open.

A further source choice closes the defect at cofinal balanced-row scope.

Use

```text
b_diamond=(epsilon-delta_4)*(epsilon-4delta_4)*mu.
```

Its divisor prefix is

```text
epsilon-5 delta_4+4 delta_16,
```

so the bare source field is identically zero whenever both children are at least sixteen.

Couple this source leg to the compact-source relative Jordan ratio.  The exact jets are

```text
V(0)  =(1,0),
V'(0) =(E,I),
V''(0)=(E^2-R,T),
```

with

```text
R=Delta_4 R_sharp=Theta_eta(n log n),
E=O_eta(log n),
I=the hard compact RH-sensitive innovation,
T=O(n).
```

The `T=O(n)` theorem follows from

```text
(1-x)(1-4x)C_sharp
 =(1-x)(1-4x)C
 +8 log4 x(1-x)lambda
 +4(log4)^2 x(1-x)(1+4x)/(1-4x)
```

and the classical Selberg symmetry formula.  The first term's `X log X` main coefficient cancels under `1-5 delta_4+4 delta_16`; the other two have linear summatory size.

## 2. Complete bad-eigenvalue estimate

The curvature matrix is

```text
K=[[R,EI-T/2],
   [EI-T/2,I^2]].
```

It has positive trace `R+I^2`.  If it is indefinite, its positive eigenvalue is at least the first diagonal Rayleigh quotient `R`.  Therefore

```text
delta(K)=tr(K_-)
 <=(-det K)/R.
```

Completing the resulting quadratic in the unknown current gives exactly

```text
delta(K)
 <= T^2/[4(R-E^2)].
```

Since `R-E^2 ~ R`,

```text
boxed:
delta(K)=O_eta(n/log n).
```

After critical normalization by the parent size, the bad spectral mass is only `O_eta(1/log n)`.

No estimate for `I` is used.

## 3. What this does close

PR #350 correctly identified scalar trace positivity as insufficient and demanded either the full polarized matrix or an equivalent safe completion.

The new theorem shows that **full PSD is unnecessary and its failure is quantitatively harmless at the row scale** for the zero-bare source carrying the hard compact innovation.

So the live local matrix problem is no longer

```text
prove K>=0.
```

The bad direction is explicit and lower order.

## 4. What this does not yet close

The block-level recurrence still needs a single declared Hilbert metric which simultaneously retains:

1. independent-frequency localization;
2. the zero-bare source difference before individual/product separation;
3. the exact Q2/Q4 finite state and terminal all-pass return;
4. finite causal collars and strictly delayed gauges;
5. the rowwise inertia defect exactly once.

The exact tight-frame identities on PRs #345/#350 strongly constrain this assembly, but the present branch has **not yet proved** that the complete relative-scale output curvature is bounded by the delayed input plus only polynomial forcing.

Thus it is too strong to call the remaining step merely clerical bookkeeping.  The correct statement is:

```text
local polarized-sign/RH-scale matrix estimate    CLOSED at cofinal row scope;
full block/source/delay orientation                OPEN / potentially RH-bearing;
coefficient-one recurrence                         OPEN;
Riemann Hypothesis                                 UNPROVED.
```

## 5. Interaction with the `<2/5` parity synthesis

PR #346 has an exact Bézout coefficient-energy charge `<2/5`.  It is tempting to multiply that by a crude inertia ratio.  This is not justified: coefficient filter energy is not automatically the operator bound `W^*W<=qI` in the curvature Hilbert space.

The same branch does contain an operator-level jet-frame inequality with coefficient `1/2`; that is the correct type of statement, but combining it with the source-relative curvature still requires the full block orientation above.

This firewall is retained explicitly to prevent a fake `9/10` closure.

## 6. Strategic consequence

The Claude cross-fertilization has therefore paid off in a concrete way:

```text
before:
    full 2x2 arithmetic PSD looked like an RH-strength local theorem;

after:
    choose the zero-bare source,
    retain the one bad eigenvalue,
    prove it is O(n/log n) independently of the RH current.
```

The highest-value next calculation is now the exact independent-frequency block composition of this zero-bare state with the Q2/Q4 tight-frame and terminal-state identities.