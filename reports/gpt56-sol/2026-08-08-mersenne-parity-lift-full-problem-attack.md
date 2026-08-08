# Full-problem attack after the signed-transport and one-crossing refresh

Agent: `gpt56-sol`  
Date: 2026-08-08  
Status: **serious full conditional proposal; RH unproved**

## 1. Refreshed graph

The live graph has changed materially since PR #251.

### Results that close former geometric questions

- PR #265 proves the parabolic seed is already a nonnegative carry-row
  combination and that its continuum defect has ordered zero-cost transport.
- PR #272 gives the complete Pascal-cycle kernel, a canonical balanced tree,
  exact cycle-debt duality, and a dyadic divergence commutator normal form.
- PR #291 now proposes a cofinal proof that the finite dyadic shell has exactly
  one sign crossing.
- PR #286 gives a strict `6/7` contraction for the shifted analytic central
  bulk, leaving only finite cutoff boundary states.
- PR #285 identifies the full central resolvent with `1/eta(s)` and localizes
  negative eta carry charge to Mersenne rows.

### Routes that are no longer viable as stated

- The nonnegative monotone Divisibility Cover costs order `sqrt(X)`.
- Prime-only tail transport has a deterministic positive density drift.
- WSTS has been consolidated as exactly RH-equivalent.
- Fixed third Abel positivity fails at `(Q,n)=(520,15)` with `-91/256`.
- The direct fourth and fifth fixed-order repairs also have exact negative
  coefficients on the separate correction branch.
- Zero extension destroys the claimed all-iterate smooth central monotonicity.

The strongest elementary route must therefore retain the boundary source and
construct a positive finite object, not merely estimate a renamed RH scalar.

## 2. Chosen route

I chose the eta/Mersenne route because its source image has an exceptional
feature absent from the generic balanced packet:

```text
all ordinary binary-window splits have eta charge >=1;
only n=2^r-1 is forced negative;
the extreme Mersenne split has charge exactly -1.
```

The original MCF statement had two obligations:

1. construct the exact support-restricted nonnegative saturation;
2. prove that the Mersenne edge mass is subpower.

`L-29201` removes the second obligation completely. For any nonnegative
sub-saturation, the diagonal column `q=n` bounds the total parent mass by
`w_X(n)`. Summing over Mersenne parents gives

```text
M_X <= (1+sqrt(2)) log X.
```

Thus exact support feasibility alone gives the eta lower envelope and RH.

## 3. New factor-two construction coordinate

`L-29202` introduces three parity siblings of one lower split:

```text
[2n,2j],
[2n+1,2j],
[2n+1,2j+1].
```

All three have exactly the same load on every even column. Their differences on
odd columns are the divisor dipoles

```text
1_(q|2n+1)-1_(q|2(n-j)+1),
1_(q|2n+1)-1_(q|2j+1).
```

Therefore a lower positive flow can be doubled without disturbing a single even
column. The complete odd discrepancy is Möbius-decoded into a charge on odd
nodes, and the lift is possible exactly when that charge can be routed through
a finite network whose arc capacities are the actual lower edge masses.

The shared-capacity constraint is essential:

```text
x_e>=0,
y_e>=0,
x_e+y_e<=2^(-1/2)d_e.
```

The max-flow/min-cut alternative is written explicitly. A failure produces a
finite potential witness; a success emits every upper split coefficient.

## 4. Boundary state

The local sibling lift preserves the MCF menu for every non-Mersenne lower edge.
It deliberately does not pretend that a lower Mersenne extreme edge can be
lifted locally: its even lift is outside the upper binary window. Those edges
form a logarithmic boundary state by `L-29201` and require a complete positive
Pascal/tree reconstruction.

The top lower parent `Y` also lacks the odd parent `2Y+1`; it is a separate
finite endpoint state.

This is the correct boundary rather than an unspecified collar:

```text
ordinary lower edges  -> capacitated odd divisor network;
Mersenne lower edges  -> logarithmic positive reconstruction;
top endpoint          -> finite correction.
```

## 5. Full proposal

The proposed theorem `PPMFL` constructs compatible lower and upper flows through
those three channels at every doubling and unit endpoint. Then

```text
PPMFL
-> support-feasible MCF at all large X
-> automatic O(log X) Mersenne collar
-> eta Riesz lower envelope
-> one-sided Mellin/Landau pole exclusion
-> RH.
```

The proposal does not import WSTS, EPD, a prime-ramp sign, a Mertens bound, a
reflected block norm, or generic carry saturation. Its open theorem is a finite
positive allocation and reconstruction problem.

## 6. What was achieved and what was not

Achieved exactly:

- the collar-rate obligation is eliminated;
- the parity-sibling floor identities are complete;
- the odd discrepancy is decoded exactly;
- the positive lift is reduced to a capacitated network with an exact cut dual;
- support preservation is proved away from the declared boundary;
- a standard-library exact regression covers more than two million sibling
  identities.

Not achieved:

- all-scale feasibility of the source-specific odd network;
- positive reconstruction of the Mersenne boundary state;
- endpoint-compatible recursive PPMFL;
- RH.

The result is a more concrete full attack, not a completed proof. The next
mathematical target is now unambiguous: prove the cut inequalities using the
lower fragmentation conservation law, or emit a cut potential that rejects the
parity lift and forces a pivot.
