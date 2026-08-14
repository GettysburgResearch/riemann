# T-91658 — Hall-free stopped-leaf positivity reduces NRCT to native-reservoir/root intertwining

Claim ID: `T-91658`
Status: **CONDITIONAL REDUCTION THEOREM ON FROZEN INPUTS — NOT A COMPLETE RH PROOF**
Created: 2026-08-14
Primary new input: `L-91685`
RH status: **unproved**

## 1. Purpose

The stopped-leaf Hall theorem used by the former single-SHARP proposal is false. PR `#467` replaces it with a target-Lorenz source producer and leaves one explicit row family. PR `#468` independently corrects the native-root normalization and isolates the Native-Root Capacity Theorem (`NRCT`) as the single remaining producer interface.

`L-91685` gives a different local result: at every canonical `P_61` stopped leaf, the exact Boolean one-prime residual is already positive in every component row and in both physical response signs, has strict target/score/entropy surplus, and leaves one exact terminal native child. This theorem records exactly what that closes and what the PR `#468` rough-reservoir firewall still forbids.

## 2. Local stopped-leaf replacement

For every rough prime `p>=67` and terminal endpoint `1<=y<67`, put

\[
G_{p,y}=D_{P_{61},py}-p^{-1/2}D_{P_{61},y},
\qquad
C_{p,y}=p^{-1/2}D_{P_{61},y}.
\tag{T-91658.1}
\]

`L-91685` proves, on its frozen inputs, that

```text
G_(p,y) is coefficientwise nonnegative in every row;
G_(p,y) has nonnegative ordinary and radix-four responses;
G_(p,y) has positive target and score, with score above target;
literal entropy of G_(p,y) exceeds its declared score;
C_(p,y) is the exact native terminal row p^(-1/2)c_y;
G_(p,y)+C_(p,y)=D_(P61,py) in every linear coordinate.
```

No stopped-leaf Hall graph, source fraction, target-normalized determinant, or fixed-67 proxy child occurs.

## 3. What this closes

Assume a labeled source-disjoint stopping-line expansion whose canonical leaf fibers are

\[
a_vD_{P_{61},p_vy_v},
\qquad a_v\ge0,
\qquad 1\le y_v<67.
\tag{T-91658.2}
\]

Substitute

\[
a_vD_{P_{61},p_vy_v}
=
a_vG_{p_v,y_v}+a_vC_{p_v,y_v}.
\tag{T-91658.3}
\]

The substitution is exact in every linear coordinate and preserves the leaf coefficient and label. It closes, on the frozen terminal-leaf inputs, the following local sign questions:

```text
coefficientwise current-row positivity;
ordinary/detail response positivity;
positive target and declared score;
literal-entropy domination;
exact terminal child realization.
```

Consequently the stopped-leaf Hall obstruction, the finite target-Lorenz row-family campaign of PR `#467`, and aggregate leaf score-debt bookkeeping are bypassed **as mechanisms for proving the aggregate leaf row and score signs**.

This is a bypass, not a proof of the target-Lorenz determinant inequalities themselves.

## 4. The PR #468 normalization firewall

By exact linearity,

\[
\Gamma(G_{p,y})+\Gamma(C_{p,y})
=
\Gamma(D_{P_{61},py}),
\]

and similarly for `Xi`. `L-91379` on PR `#468` proves that the right side equals the native capacity plus an exact positive rough reservoir. Therefore (T-91658.3) is not yet an `NRCT` certificate:

```text
positive canonical row       does not imply native capacity feasibility;
positive current + child     may still include the rough reservoir;
rough reservoir + child      may not be spent twice.
```

This corrects the stronger interpretation of the first draft of this packet.

## 5. Exact surviving interface: NRSLI

To combine the local theorem with `T-91314`, prove the following typed statement.

> **Native-Reservoir/Stopping-Line Intertwining (`NRSLI`).** Expand the native root datum and its exact rough reservoir into source-disjoint least-prime fibers. Preserve every coefficient and provenance label. On each terminal stopped leaf, use the decomposition (T-91658.3), but assign every positive reservoir coordinate to exactly one recursive child or current owner so that, after summing all leaves,
> \[
> C_{d_X^{\rm cur}}(q)+\sum_b\alpha_b C_{P_b}(q)\le w_X(q),
> \]
> \[
> \Xi_{d_X^{\rm cur}}(q)+\sum_b\alpha_b\Xi_{P_b}(q)\le\Omega_X(q),
> \]
> with the analogous one-use inequalities for all boundary/common-port coordinates, total child coefficient below `1/8`, and `Y_4`-weighted current slack bounded as required by `T-91314`.

All endpoint-frame, mismatch, collar, safety, omission, taper, and common-port corrections must retain one owner and be charged once after the common parent sum.

`L-91674` supplies a formal positive-linear commutation theorem for root integration and one global quantizer. `L-91379` supplies the exact rough-reservoir identity. `L-91685` supplies the terminal stopped-leaf row/response signs. `NRSLI` is the remaining arithmetic allocation and ownership theorem joining them.

## 6. Conditional consequence

If `NRSLI` supplies the hypotheses of the Native-Root Capacity Theorem `T-91314`, then the resident subcritical consumer gives

\[
\Lambda(X)\le 2+\frac18\Lambda(X/67+C_0),
\]

hence

\[
\Lambda(X)=O(1)=o(\log^2X).
\]

The resident endpoint consumer `T-91313` then yields the proposed RH implication. This paragraph is conditional: the companion replay does not certify `NRSLI`, `NRCT`, the endpoint correction packet, or the endpoint-to-RH chain.

## 7. Comparison with the live branches

```text
PR #463  verifies single-SHARP normalization and refutes stopped-leaf Hall.
PR #464  supplies a root-window Hall and one-global-quantizer formalism.
PR #466  independently closes the literal-entropy/score-debt interface.
PR #467  closes causal profiles/debt and leaves one target-Lorenz row family.
PR #468  fixes native normalization and isolates NRCT / rough-reservoir ownership.
L-91685 proves the PR #468 one-prime current candidate on all terminal leaves.
```

The routes help each other as follows:

```text
#466 corroborates strict physical-entropy surplus;
#467 supplies complete causal-profile and finite-cutoff diagnostics;
#468 supplies the controlling native-capacity firewall and exact reservoir;
L-91685 closes the terminal one-prime generator sign without Hall;
T-91658 reduces the next step to the explicit NRSLI allocation theorem.
```

## 8. Immediate falsifiers

Reject this reduction upon the first occurrence of:

```text
L-91347 and L-91364 use different P61/Q normalizations;
the full global L-91364 theorem fails reconstruction;
a stopped leaf is not exactly a_v D_(P61,p_v y_v);
a leaf coefficient or source label changes under the raw split;
the child D_(P61,y) differs from c_y for y<67;
ordinary or detail responses do not telescope current+child;
the rough reservoir is counted in both current and recursive children;
total recursive coefficient is not below 1/8;
Y4-weighted current slack is not uniformly controlled;
a root correction is charged once per leaf rather than once globally;
the final finite-dual or endpoint sign is reversed.
```

## 9. Exact status

```text
stopped-leaf Hall                              FALSE / REMOVED
terminal one-prime current-row sign            PROPOSED CLOSED / FROZEN INPUTS
terminal ordinary/detail response signs        CLOSED
terminal target/score/entropy signs            CLOSED ON FROZEN INPUTS
finite leaf determinant corridor               BYPASSED FOR AGGREGATE SIGN
native rough-reservoir allocation NRSLI        OPEN / LOAD BEARING
Native-Root Capacity Theorem                   OPEN / RH-BEARING
conditional subcritical endpoint deficit       DERIVED FROM NRCT
Riemann Hypothesis                             UNPROVEN
```
