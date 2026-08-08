# M-27501 — Final Weighted Shell-Tail review protocol

Methodology ID: `M-27501`  
Title: Clean-room review of the canonical elementary RH equivalence  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08

## 1. Frozen review object

Freeze the consolidation branch at one exact commit before beginning the review.
Record separately the frozen heads of every imported PR.  Do not review mutable
branch tips under one combined verdict.

The principal new claims are:

```text
L-27501  RH gives O(log^4 X) weighted shell sampling;
T-27501  WSTS is equivalent to RH;
O-27501  all live carry routes consolidate to the same final scalar.
```

The inherited load-bearing files are:

```text
L-23823  normalized continuum shell-tail order;
L-23824  zero-cost weighted prime-tail transport;
L-23825  finite shell and exact sampling remainder;
L-23826  in-support weighted shell charge and dyadic assembly;
T-23811  WSTS -> prime ramp -> RH.
```

## 2. Required verdict vocabulary

Classify each item as one of:

```text
VERIFIED
VERIFIED WITH FIXES
UNPROVEN
FALSE
```

Use `FALSE` only when an exact witness satisfies the frozen hypotheses and
contradicts the frozen conclusion.  A missing proof, insufficient estimate, or
failed composition is `UNPROVEN`.

## 3. Clean-room reconstruction order

### Phase A — continuum profile

1. Recompute the reciprocal-cell formula for `F`, `E`, `H`, and `J`.
2. Differentiate `J=H/sqrt(theta)` independently and verify
   \[
   J_N'(\theta)
   ={2\over\theta^{3/2}}
   [N\theta+1-(S_N+1)\sqrt\theta].
   \]
3. Check continuity at every reciprocal knot using `g(1)=0`.
4. Reconstruct normalized-tail monotonicity and the derivative moat.
5. Reconstruct the fixed-ratio shell identity
   \[
   H_c(\theta)=H(\theta)-\sqrt c H(\theta/c).
   \]

### Phase B — finite shell

1. Derive the finite response from the parabolic seed by the fundamental theorem
   of calculus.
2. Prove the uniform floor error
   \[
   r_X(q)=X^{-1/2}E(q/X)+O(q^{-3/2}[1+\log(X/q)]).
   \]
3. Repeat at both endpoints and verify the shell normalization.
4. Check logarithmically weighted absolute summability of the floor error.
5. Reconstruct the Stieltjes identity, including endpoint atoms and the exact
   convention at prime lower endpoints.

### Phase C — transport and dyadic assembly

1. Independently derive the weighted upper-tail min-cost transport.
2. Check that every internal prime-incidence block has zero weighted objective
   cost after complete endpoint pairing.
3. Verify the in-support boundary charge and its sign.
4. Verify exact telescoping of seed, target, and correction shells across
   `X, floor(X/2), floor(X/4), ...`.
5. Check that the total subpower loss remains subpower after summing the dyadic
   levels.

### Phase D — reverse implication under RH

1. Use only
   \[
   \vartheta(t)-t=O(\sqrt t\log^2(2t))
   \]
   as the RH input.
2. Reprove the sum–integral estimates for `S_N` and `A_N`.
3. Verify the size and derivative bounds for `E` and `E_c`.
4. Perform Stieltjes integration by parts with all knots and boundary values
   retained.
5. Check explicitly that
   \[
   \int_z^X{\log^2(2t)[1+\log(X/t)]\over t}dt
   =O(\log^4(2X))
   \]
   uniformly in `z`.
6. Confirm that the floor error does not exceed the declared polylogarithmic
   budget.

### Phase E — RH consumer

1. Freeze and reconstruct the exact prime-ramp/square-screw normalization.
2. Check the sign orientation: a prime-ramp lower bound gives an upper envelope
   for the screw.
3. Audit interpolation between square samples.
4. State precisely the one-sign Landau theorem being used and verify its
   hypotheses.
5. Check that functional-equation symmetry supplies the opposite half-strip.

## 4. Mandatory mutations

A valid checker or human replay must reject all of the following.

1. Replace `theta(t)-t` by an unsigned PNT error before retaining the negative
   shell moat.
2. Delete the lower-endpoint atom in Stieltjes summation.
3. Use a fixed-ratio convergence theorem at a ratio tending to zero.
4. Reverse the shell dilation factor `c^(-1/2)`.
5. Replace the weighted tail by an unweighted tail without proving a sign-safe
   comparison.
6. Drop the final in-support boundary charge.
7. Sum finite shell errors without preserving their exact dyadic signs.
8. Replace the `2/3` or dyadic shell by an unrelated generic coefficient vector.
9. Invoke the old one-frequency physical-block identity.
10. Promote a finite numerical ladder to `WSTS`.

## 5. Dependency firewall

The canonical WSTS proof does not depend on:

```text
ESBT/ESGS;
PTQ/PTC;
DGB(5);
F5TC;
FAGD;
ADF;
PGC;
BJD;
full Carry Saturation;
generic balanced Type II;
a reflected positive reserve.
```

A reviewer may use these mechanisms to attack `WSTS`, but must not treat their
open conclusion as an imported theorem.

## 6. Proof-object requirements for a future unconditional WSTS proof

A claimed completion must emit:

```text
all dyadic endpoint shells;
all weighted prime residuals;
all upper-tail maxima;
all continuum shell cells;
all floor-error intervals;
the exact Chebyshev sampling remainder;
the complete weighted transport plan;
all in-support boundary charges;
the dyadic objective telescope;
the final prime-ramp interval;
the square-screw/Landau normalization.
```

The proof must fail closed if one tail exceeds its declared budget.

## 7. Correct review conclusion

Acceptance of `L-27501/T-27501` establishes the equivalence

\[
\mathrm{WSTS}\Longleftrightarrow\mathrm{RH}.
\]

It does not establish `WSTS` unconditionally.  The final review report must keep
those two statements separate.