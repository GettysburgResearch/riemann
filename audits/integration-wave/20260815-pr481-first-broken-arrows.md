# PR #481 first broken arrows

Frozen proposal: `research/gpt56-pro/91726-pr476-native-slack-repair` at `f41bbd7608cc70bc2a8002d43ef99b5e35977968`  
Review cutoff: `2026-08-14T22:55:57Z`  
Verdict: **GAP / BLOCKED**  
RH: **unproved**

## Arrow 0 — publication/provenance

The review request describes a Gate A/Gate B closure on:

```text
PR #470
research/gpt56-pro/91689-three-route-native-root-attack
```

These coordinates do not identify one live object.

```text
PR #470 -> research/gpt56-pro/91686-native-root-compiler-separator
           89af3206ea1894884613e1188b5ab9a6a4cd74f0

research/gpt56-pro/91689-three-route-native-root-attack -> PR #475
           6cba90ea10163abd62b051c83c8bfd8cc2f901da
```

Neither contains the stated depth-limit and Gate A/Gate B theorem files. The first fail-closed verdict is therefore:

\[
\boxed{\text{ADVERTISED PACKET: NOT REPRODUCED}}
\]

A corrected PR number, branch, exact head SHA and content ledger are required before that proposal can be reviewed.

## Arrow 1 — abstract packet cocycle to actual finite root packet

The live corrected route uses

\[
\Omega_X=\Xi(c_X)+r_X+
\int a(b)U_b\Omega(P_b),
\qquad r_X\ge0.
\tag{1}
\]

`L-91730` proves (1) from two assumptions:

1. one complete common parent packet is all-column feasible;
2. that packet has an exact aggregate current/child split in the complete typed space.

The derivation is valid. The missing arrow is the concrete producer:

\[
\boxed{
\text{factor-67 endpoint frame + Hall + finite realization + corrections}
\Longrightarrow \text{one actual packet satisfying (1)}.
}
\]

The current patch does not write this as a single instantiated theorem. The all-column work supplies numerical reserve inequalities and an adjacent-cell owner split; the formal endpoint theorem supplies linear commutation on stated hypotheses; `L-91730` then assumes the exact packet split. A hostile reconstruction still has to prove that the actual mismatch, collar, activation refinement, terminal omission, base correction and common port remain current-owned coordinates of the same packet while the reserved child coordinate is exactly the actual child packet capacity.

The finite regression does not close this arrow. It checks a toy three-coordinate identity with hand-entered vectors.

### Required repair

Deposit a concrete equality with all objects defined from the actual endpoint measure:

\[
P_X^{\rm phys}=P_{X,\rm cur}^{\rm phys}
+\int a(b)U_bP_b^{\rm phys},
\]

and prove it in source, ordinary `q`, ordinary `4q`, detail, target, score, boundary and port coordinates after every one-use correction.

## Arrow 2 — common port and native scalar cost

`L-91725` proves the abstract implication

\[
D_s\preceq P_s\quad\text{for each fiber}
\Longrightarrow
\int b_sD_s\,d\mu(s)
\preceq
\int b_sP_s\,d\mu(s).
\tag{2}
\]

It also bounds normalized integrated port mass. The reviewed composition needs more:

1. identify the actual complete correction demand `D_s` after Hall, mismatch, collar, taper, base and quantizer corrections;
2. prove that this actual `D_s` satisfies the fiberwise or aggregate domination required in (2);
3. prove the native dual bound
   \[
   \sum_qY_4(q)r_{\rm port}(q)=O(1).
   \tag{3}
   \]

`L-91728` explicitly labels the terminal/base/port `O(1)` bound as an independent reconstruction input. A bounded port mass is not, without an exact response identity, the same statement as (3).

### Required repair

Give the exact ordinary response of the common port, form its radix-four response from `q` and `4q`, and evaluate or dominate its `Y_4` pairing. The same ledger must include the fixed terminal and base packets. The final theorem should display a numerical or symbolic constant `C_port`.

## Arrow 3 — producer to endpoint criterion

`T-91313` consumes

\[
J_\Lambda(X)-\mathcal H(d_X)=o(\log^2X)
\]

with the one-sided orientation `F_\Lambda(X)<=Delta_X`. PR #481 does not reconstruct the resident WSTS, prime-square moat and Mellin-Landau implication. This arrow is not reached until Arrows 1 and 2 close.

### Required repair

Freeze and replay the exact endpoint-consumer dependency chain, including the normalization of `F_Lambda`, the prime-square positive moat and the Landau converse used to exclude a zero with real part greater than one half.

## Exact stale inequality on the PR #479 base

The following implication in `L-91723.16--.17` and `T-91721.3` is invalid as written:

```text
Score(P_X) is superordinate to 4 sqrt(X)
therefore scaling loss <= (1-tau_K) 4 sqrt(X).
```

Under the repository's established use of “superordinate,”

\[
\operatorname{Score}(P_X)\ge4\sqrt X.
\]

Therefore

\[
(1-\tau_K)\operatorname{Score}(P_X)
\ge(1-\tau_K)4\sqrt X,
\]

which has the opposite direction from the claimed upper bound.

This does not kill PR #481. `L-91728` replaces the stale step by the valid native upper bound

\[
(1-\tau_K)J_\Lambda(X)<4290\log X.
\]

The exact status is:

```text
PR #479 bounded equality-score loss <4290     REJECTED AS WRITTEN
PR #481 native thinning cost <4290 log X       SURVIVES
```

## Fail-closed frontier

```text
advertised Gate A/Gate B packet               NOT REPRODUCED
actual weighted child target <1/8             VERIFIED
abstract packet-native cocycle                 VERIFIED
actual finite common-parent packet identity   GAP
actual common-port demand                     GAP
terminal/base/port Y4 cost O(1)               GAP
one-shot native root O(log X)                 BLOCKED
endpoint-to-RH implication                    NOT REACHED
Riemann Hypothesis                            UNPROVEN
```
