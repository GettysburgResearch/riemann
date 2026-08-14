# T-91653 — Direct native-row replacement closes the PR #450 capacity gate with logarithmic reset debt

Status: **proposed complete RH proof packet; independent reconstruction required; RH not accepted**  
Created: 2026-08-14  
Supersedes as review target: `L-91659` and `T-91652` Sections 5--6  
Normative lock: `integration/2026-08-14/t91653-direct-root-lock.json`

## 1. Review disposition

PR #450 correctly rejected the unproved implication that a heterogeneous sum of
Hall, outer, and port rows is feasible against a coordinatewise residual
complement. The replacement does not repair that inference; it supersedes it
and returns to the coefficient-one factor-54 consumer `T-91101`.

The review overreaches in two architecture-specific claims. A corrected
`P_61/67` port already exists in `L-91320`, with mass `<14/3` and strict `1/9`
Schur reserve. The negative-center and boundary-atom gates of `L-91321` bind the
old butterfly realization, not the direct Hall row

\[
 R(E)-R(O)=R(c)+B,\qquad c\ge0,\quad B\ge0.
\]

## 2. Exact physical replacement

Let `R_ch` be the canonical child row at the common contracted endpoint and let
`d_ch` be any row feasible for its complete child capacities. The direct current
row is the canonical parent-minus-child row together with positive Hall bonuses.
For every physical integer column,

\[
 \boxed{
 \Gamma(d_X;q)=\Gamma(R_{parent};q)-\Gamma(R_{ch};q)
 +\Gamma(d_{ch};q)\le\Gamma(R_{parent};q),
 }
\]

\[
 \boxed{
 \Xi(d_X;q)=\Xi(R_{parent};q)-\Xi(R_{ch};q)
 +\Xi(d_{ch};q)\le\Xi(R_{parent};q).
 }
\]

These are proved in `L-91663` after the complete current row is summed. They
supply the antecedent of `L-90029`; ordinary feasibility is not inferred before
the detail inequality is known. The child is inserted at the same row indices,
with no affine lift, fractional column, duplicated finite block, or scalar-native
identification.

## 3. Complete reset

The retained current packet of `T-91101` pays once for the positive outer
equality producer, B-spline quantization, width-three collar,
finite/continuum mismatch, interior safety factor, fixed top omission,
terminal annulus, and corrected `P_61/67` port.

The imported one-prime cocycle is exact in target, row-budgeted native score,
and literal row. Leafwise Hall gives positive residual sources and positive
row bonuses. The deterministic child endpoint is at most `X/67+C_0`.

The corrected component-score inequality is

\[
 \boxed{
 E(Y)-E(Y/67)\ge5(\sqrt Y-\sqrt{Y/67})\qquad(Y\ge67),
 }
\]

with the split base `3.2764007195...>3`; the historical parent display was high
by two. Thus inherited score loss is carried with coefficient one.

All finite current charges are absorbed in one effective absolute constant and
`L-91665` proves

\[
 \boxed{Loss_X\le Loss_{X/67+C_0}+C_{reset}.}
\]

## 4. Logarithmic conclusion

Exact capacity does not by itself transfer the continuum equality score to the
finite row with absolute all-depth loss. That over-strong historical wording is
not used. Iterating the bounded one-generation recurrence gives

\[
 \boxed{Loss_X=O(\log X)=o(\log^2X).}
\]

The finite von-Mangoldt dual bridge gives

\[
 F_\Lambda(X)\le Loss_X.
\]

The frozen endpoint theorem `T-90011`, followed by the resident prime endpoint
Landau theorem `T-90008`, yields the **candidate** conclusion

\[
 \boxed{\mathrm{RH}.}
\]

This conclusion is not promoted before every frozen arithmetic, Hall,
current-packet, and endpoint input is independently reconstructed.

## 5. Falsifiers

Reject the packet on the first occurrence of any of:

```text
failed frozen Hall prefix or row cell;
duplicated source monomial;
failed same-index response identity;
current mismatch/collar/omission term charged twice;
port using the obsolete P53 constant;
failed fixed67 score inequality;
scale-dependent C_reset;
endpoint bridge or threshold sign failure.
```

```text
PR450 L91659 objection                       ACCEPTED
P61/67 port absence                          REFUTED
old butterfly gates                          BYPASSED
simultaneous residual capacity               DISPLAYED
constant finite-row score transfer           NOT USED
one-generation debt                          O(1)
all-generation debt                          O(log X)
full theorem                                 PROPOSED / REVIEW REQUIRED
Riemann Hypothesis                            NOT ACCEPTED
```
