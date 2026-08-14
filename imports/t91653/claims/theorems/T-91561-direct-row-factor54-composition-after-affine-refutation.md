# T-91561 — The corrected factor-54 composition lives entirely in the native finite-row space

Claim ID: `T-91561`  
Status: **CANDIDATE COMPLETE ON FROZEN ONE-STEP INPUTS — LIVE REPLAY AND INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Frozen inputs: PR `#399` at `22d7f2f3f3668f664c09708838f6a738e4398eef`; imported PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Corrects: `T-91546`, `T-91551`, `T-91555` after `R-91552/R-91558`  
Depends on: retained `L-91112.25--26`; `L-90029`; `L-91545`, `L-91547`, `L-91550`, `L-91553/L-91554`, `L-91556`, `L-91557`, `L-91559/L-91560`  
RH status: **unproved pending Section 8**

## 1. Two refuted shortcuts are not used

The corrected composition contains neither of the false implications

```text
declared affine source score
 = literal component-row entropy;                 false by R-91552

child detail feasible
 -> fixed-67 affine image detail feasible;        false by R-91558
```

Instead it uses:

1. the exact component entropy and fixed-67 difference inequality of
   `L-91553`;
2. the finite-Euler terminal source bound of `L-91554`;
3. the exact row-budgeted binary normalization of `L-91556`;
4. the direct nested physical target of `L-91559`;
5. the residual-plus-child controlled cocycle of `L-91560`.

No continuum endpoint-measure identity and no affine finite child lift occurs in
the recursive physical construction.

## 2. Native one-step row cocycle

At one active rough prime, the raw arithmetic residual and its exact raw child
satisfy, pointwise in each source node,

\[
 (T_a,S_a,R_a)+(T_c,S_c,R_c)
 =(T_0,S_0,Q_Y).
 \tag{T-91561.1}
\]

`L-91560` constructs controlled survival and hazard packets with

\[
 \boxed{
 (T_s,\widetilde S_s,R_s)
 +(T_h,\widetilde S_h,R_h)
 =(T_0,S_0,Q_Y).
 }
 \tag{T-91561.2}
\]

The row coefficients are

\[
 \kappa_s=1-r^2,
 \qquad
 \kappa_h=r^2,
 \qquad
 \kappa_s+\kappa_h=1.
 \tag{T-91561.3}
\]

The full binary state score exceeds the native row-budgeted score by the
positive target-null amount

\[
 r(1-r)(\sqrt Y-1).
 \tag{T-91561.4}
\]

Thus (T-91561.2) is a one-use identity in all three ledgers, not a scalar target
analogy.

## 3. Target Hall is an exact row identity

Apply the merged target-Hall projections to the two controlled branch labels.
`L-91545/L-91556`, with the directed margins replayed in `L-91550`, give
positive residual source measures `c_s,c_h` and positive row bonuses `B_s,B_h`
such that

\[
 \boxed{
 T(c_s)+T(c_h)=T_{\rm parent},
 }
 \tag{T-91561.5}
\]

\[
 \boxed{
 \widetilde S(c_s)+
 \widetilde S(c_h)
 \ge S_{\rm parent},
 }
 \tag{T-91561.6}
\]

and, coefficientwise in every exact finite row,

\[
 \boxed{
 R_{\rm native,parent}
 =R_s(c_s)+R_h(c_h)+B_s+B_h.
 }
 \tag{T-91561.7}
\]

The Hall bonuses carry no recursive source target.  Equation (T-91561.7) is an
equality of the literal row vector, so every ordinary and radix-four response
of the native row is unchanged.

## 4. Exact physical target of a component packet

For the positive component row `Q_Y`, `L-91559` proves

\[
 C_Y(q)=q^{-1/2}H(Y/q)
 \tag{T-91561.8}
\]

and

\[
 \boxed{
 \Theta_Y(q)
 =q^{-1/2}[H(Y/q)-H(Y/(4q))]
 \ge0.
 }
 \tag{T-91561.9}
\]

Moreover `Theta_Y(q)` and `Q_Y(n)` are nondecreasing in the endpoint `Y`.
Therefore the deterministic fixed-67 split has the exact common-row-space
replacement

\[
 \boxed{
 d_X=a(Q_X-Q_{X/67})+d_{X/67},
 }
 \tag{T-91561.10}
\]

where any child row feasible for `aTheta_(X/67)` yields a nonnegative parent row
feasible for `aTheta_X`.

Apply (T-91561.10) to every positive source atom in `c_s,c_h` and retain
`B_s+B_h` in the current row.  Positive summation gives a capacity-faithful
replacement of arbitrary survival and hazard child packings at endpoint
`X/67`.

The child is embedded by the identity map.  There are no colored columns,
unmatched affine fibers, noninteger child columns, or branchwise
quantizations.

## 5. Native score of the literal row

Let

\[
 \mathcal E(Y)=\sum_nQ_Y(n)G_n.
 \tag{T-91561.11}
\]

`L-91553/L-91556` prove, for every nonterminal quotient `Y>=67`,

\[
 \mathcal E_\tau(Y)-
 \mathcal E_\tau(Y/67)
 \ge
 \widetilde S_\tau(Y)-
 \widetilde S_\tau(Y/67).
 \tag{T-91561.12}
\]

At the unique terminal quotient `1<=Y<67`, `L-91554` uses the fixed Euler
support and the exact sourcewise telescope to prove the unnormalized bounds

\[
 E_{\rm source}(P_{61})<3600,
 \qquad
 E_{\rm source}(P_{79})<5600.
 \tag{T-91561.13}
\]

Hence the complete literal row produced by Sections 2--4 realizes the native
row-budgeted source score up to one absolute constant.  The exact continuum
equality state has physical score

\[
 4\sqrt X
 \tag{T-91561.14}
\]

by `L-26204/L-91557`.  On the frozen one-step source identity, the final
nonnegative row therefore satisfies

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-C,
 }
 \tag{T-91561.15}
\]

for an absolute constant `C` (the larger explicit Euler term is `5600`; the
remaining finite base/port term is retained separately).

Unlike the withdrawn affine composition, no score change occurs when a child is
placed in the parent row space.

## 6. Final detail feasibility and native loss

The exact finite equality row has ordinary target `w_X` and radix-four target
`Omega_X`.  Section 3 preserves that literal row; Section 4 replaces each
canonical child by a row consuming no more than the exact canonical child
capacity.  Consequently

\[
 \boxed{
 \mathcal D_4C_{d_X}(q)
 \le\Omega_X(q)
 \qquad(q\ge2).
 }
 \tag{T-91561.16}
\]

and `d_X>=0`.  `L-90029` then reconstructs ordinary feasibility by positive
radix-four telescoping.

`L-91557` gives the elementary native upper bound

\[
 J_\Lambda(X)<4\sqrt X+4\log X.
 \tag{T-91561.17}
\]

Combining (T-91561.15)--(T-91561.17),

\[
 \boxed{
 \mathfrak L_X(d_X)
 =J_\Lambda(X)-\mathcal S_X(d_X)
 \le4\log X+C
 =O(\log X).
 }
 \tag{T-91561.18}
\]

Thus the corrected finite-row composition gives

\[
 \mathfrak L_X=o(\log^2X)
 \tag{T-91561.19}
\]

on the frozen one-step input.

## 7. Candidate RH implication

The exact consumer in `L-90029` states that a nonnegative detail-feasible row
with (T-91561.19) implies RH.  Therefore Sections 1--6 are a complete
**candidate** factor-54 composition on the frozen Hall and native-entry inputs.

This theorem does not promote the Riemann Hypothesis to established status.
The decisive remaining work is independent reconstruction and live replay of
the imported one-step arithmetic/Hall entry.

## 8. Mandatory hostile review

A reviewer must rebuild the following without relying on this theorem's
summary:

1. **Native parent source.** Starting from the exact finite equality row, derive
   the `P_61` or `P_79` parent packet and its one-prime residual-plus-child
   partition with every source coefficient used once.
2. **Controlled cocycle.** Verify (T-91561.2) in target, native score and every
   row coordinate, including the coefficient `r` of the raw child.
3. **Hall normalization.** Re-run the target-Hall margins and normalized row
   monotonicity with the row coefficients `1-r^2` and `r^2`, not the older full
   branch-score coefficients.
4. **Row identity.** Verify that the Hall residual-source formula and row bonus
   sum to the exact native row before any capacity inequality is applied.
5. **Sourcewise terminal bound.** Verify the parent-index support and
   coefficient domination used in `L-91554`, including any countable
   least-prime disintegration present on the live branch.
6. **Finite base and port.** Reconstruct the finite terminal block and prove
   that any remaining common-port row is included once in the literal row
   identity.
7. **Live movement.** Replay the complete packet on the current PR `#399` head,
   which has moved beyond the frozen SHA and now contains additional one-prime
   row work.

Any failure retracts the candidate conclusion while leaving the exact
counterexample, component-capacity theorem and local cocycle intact.

## 9. Boundary

```text
false source-score identity                           NOT USED
false affine child capacity lift                      NOT USED
one-prime native three-ledger cocycle                 EXACT
row-budgeted target-Hall residualization              EXACT ON FROZEN INPUT
component packet detail target Theta_Y                EXACT / POSITIVE
fixed-67 identity physical replacement                EXACT
finite-Euler terminal entropy debt                    ABSOLUTELY BOUNDED
J_Lambda <4sqrt(X)+4log(X)                            EXACT
native O(log X) loss                                  CANDIDATE ON FROZEN ENTRY
live independent reconstruction                      REQUIRED
Riemann Hypothesis                                    UNPROVEN
```
