# Exact-head comparative review of PR #505 and PR #507

**Review type:** independent, review-only  
**Date:** 2026-08-16  
**Repository:** `gfreund123/riemann`  
**RH status:** **unproved**

## Frozen objects

```text
shared two-ledger comparison input / PR #496:
commit 96f8a6b3cc3d474217633e16d4caa490a0aae518
tree   aa9933522d3e4dd0ee8287c6dcfcce2f03c015bc

shared physical-coupling base / PR #500:
commit d73c1e7a1a482cac31581211a84db43cc34c824e
tree   72421c74d9d5f92aa4c36e5ad571b29442aad42b

PR #505:
commit 1113fe6d55e955a8d9de7b43ceb24f5792870550
tree   8f6ffe32961062e1c53e2bcba1415fa51d7ead6f

PR #507:
commit dfaa70cd2eefcabbf6717e3da060792904c7f357
tree   f8fdef949b85ebe0be5a1e745da33241b426731d
```

PR #505 is a one-commit child of the exact PR #500 head. PR #507 contains one mathematical commit on the same exact PR #500 head followed by one checksum/line-ending repair. Their common #496/#500 spine is reconstructed once below. No shared theorem, constant, checker fixture, or imported analytic estimate is counted as independent confirmation.

## Executive verdict

```text
common #496/#500 spine:
PARTIAL PASS / SHARED CONDITIONAL INFRASTRUCTURE

PR #505 local normalization algebra:
PARTIAL PASS
- native versus rough-lift orientation identity: exact
- qualified q=2 rough-lift separator: exact in stated scope
- branchwise positive realization of actual oriented children: false

PR #505 end to end:
REQUEST CHANGES / BLOCKED AT L-92921.2--L-92921.4

PR #507 local type firewall:
PARTIAL PASS
- source-tree versus rough-lift distinction: exact
- signed-observation separation: exact
- actual children as positive capacities/terminal packets: false

PR #507 one-shot end to end:
REQUEST CHANGES / BLOCKED AT L-92931 AND L-92934

PR #507 terminal-child end to end:
REQUEST CHANGES / BLOCKED AT L-92932
```

The decisive point is not the already-qualified `109/1200` statement. It is a new exact sign obstruction:

> the aggregate signed ordinary response of the actual oriented stopping-line children is strictly negative at `q=2`, while every separately realized nonnegative physical row has nonnegative ordinary response.

Thus the orientation bit correctly reconstructs the native marginal **as signed algebra**, but it cannot be implemented by the branchwise positive child placements asserted by either sibling.

---

# 1. Common #496/#500 spine, reconstructed once

## 1.1 What survives from PR #496

The abstract two-ledger distinction is valid:

```text
positive arithmetic source:
  source restriction, Hall ownership, first-owner labels, literal omissions,
  thinning and genuinely positive child source;

signed observation data:
  finite/continuum mismatch, collar and terminal response corrections.
```

A signed finite comparison must not be called unused positive source. If a genuine positive unused-capacity vector `u_X` and signed excess-use vector `e_X` are separately derived, then `r_X=u_X-e_X>=0` is legitimate once the all-column domination is proved.

PR #496 did not derive the native child marginal required by its specialization. That is the exact gap the siblings attempt to repair.

## 1.2 What survives from PR #500

The abstract Hall--causal--physical coupling theorem is valid for inputs already lying in its positive product cone. It preserves source ownership, positive same-index placement, ordinary response before detail, one common positive quantizer, and a separate signed comparison ledger.

The factor-67 Hall theorem it imports is oriented in one direction: positive/even target capacity exhausts negative/odd demand on the finite `P_61` root fibre, with one source owner and one nonnegative residual-plus-bonus row. It does not prove that the parity-swapped actual rough-child block admits the same positive realization.

The formal integration theorem is likewise conditional: it commutes positive sums, positive placements and positive quantization only after every input is in the declared positive cone.

## 1.3 Shared downstream inputs

Both siblings reuse the same frozen estimates:

```text
all physical columns, including 2 <= q < K_X;
strict nonterminal ratio (sqrt(K)+129)/(sqrt(K)+130) < 1;
terminal omission margin 5033-4452 = 581;
direct native Y_4 ledger <60989;
zero-port specialization;
one-sided native-deficit endpoint consumer;
prime-square and Mellin--Landau endpoint chain.
```

These are shared assumptions, not two confirmations. This review uses only lightweight algebra and the exact `q=2` sign test; it does not rerun the large Hall/profile, endpoint-frame, all-column, prime-square, or Mellin--Landau analyses.

---

# 2. Native source tree versus rough lift

Let `N_X` denote the native datum and let the finite-Euler `P_61` rough lift be

\[
 \mathfrak D_X
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}N_{X/m}
 =N_X+\mathcal R_X,
\]

where `m=1` is the native term and `\mathcal R_X` is the positive rough response reservoir.

The paired stopping-line identity carries one extra channel swap at the least rough prime. Applying the signed channel observation therefore gives

\[
 \Sigma(F_{61,X})=N_X+\mathcal R_X,
 \qquad
 \Sigma(P_X^{\rm actual\ children})=-\mathcal R_X,
\]

and hence

\[
 \Sigma(F_{61,X})+
 \Sigma(P_X^{\rm actual\ children})=N_X.
\]

This is the genuine local advance shared by the siblings:

```text
orientation forgotten              rough lift, not native;
orientation retained algebraically native signed marginal;
actual child response               minus rough reservoir;
full native child capacity          not the actual child response.
```

It removes the old `A_X(P_b^src)=Omega(P_b)` assumption at the level of signed source observation. It does not yet place the signed child cancellation in the nonnegative physical-row cone.

---

# 3. Exact negative-coordinate obstruction

The finite-Euler ordinary response is

\[
 C_{P,X}(q)
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}w_{X/m}(q)
 =w_X(q)+C_{\mathcal R_X}(q).
\]

Therefore the aggregate actual oriented child response is

\[
 C_{\rm child}(q)
 =w_X(q)-C_{P,X}(q)
 =-C_{\mathcal R_X}(q).
\]

At `q=2`, the single `m=67` term gives, for every `X>134`,

\[
 C_{\mathcal R_X}(2)
 \ge
 \frac1{\sqrt{67}}w_{X/67}(2)
 =\frac1{\sqrt{134}}\log\frac X{134}>0.
\]

Hence

\[
\boxed{
 C_{\rm child}(2)
 \le-\frac1{\sqrt{134}}\log\frac X{134}<0.
}
\]

For `X>=536`, the detail coordinate also satisfies

\[
 \Xi_{\rm child}(2)
 \le-\frac1{\sqrt{67}}\Omega_{X/67}(2)
 =-\frac{\log4}{\sqrt{134}}<0.
\]

Every nonnegative physical row produced from positive endpoint atoms, positive Hall residuals/bonuses, positive same-index placements, positive integration and a Markov quantizer has nonnegative ordinary response, because the ordinary response kernel is nonnegative. Positive linearity preserves that property under sums.

Consequently there cannot exist a family of separately nonnegative child rows `R_b` satisfying

\[
 \sum_b C(R_b;2)=C_{\rm child}(2)<0.
\]

This directly contradicts the branchwise acceptance contracts

```text
PR #505: L-92920.9, L-92921.2 and L-92921.3;
PR #507: L-92931.2/L-92931.6 as positive child capacities,
         L-92932.1 as positive packet terminalization,
         L-92934.2 as positive internal child placements.
```

The checker fixtures do not test this point. PR #505 uses synthetic vectors in which a swapped child cancels a reservoir algebraically. PR #507 uses synthetic **positive** current and child vectors whose sum is native. Neither fixture instantiates the actual negative ordinary response of the oriented stopping-line child block.

---

# 4. PR #505 claim-level verdicts

| Claim or interface | Local verdict | Finding |
|---|---|---|
| `R-92920` | **PASS, QUALIFIED** | Exact rough-lift separator and formal withdrawal of unconditional PR application are correct. |
| `L-92920.1--L-92920.8` | **PASS** | The orientation bit and actual stopping-line children derive the native signed marginal rather than the rough lift. |
| `L-92920.9` | **FAIL** | It asks a positive physical child realization to reproduce an aggregate negative ordinary response. |
| `L-92921.1` | **PASS AS LABEL DATA** | The bit is a necessary provenance label. |
| `L-92921.2--L-92921.4` | **FAIL / FIRST BROKEN ARROW** | The Hall and child-placement maps are asserted to be positive and observation preserving, but the oriented child block has a negative `q=2` ordinary coordinate. |
| `L-92922` | **CONDITIONAL ONLY** | The inherited bounds cover all columns if a nonnegative native ideal row exists; that premise is not established. |
| `L-92923` | **ARITHMETIC PASS / PRODUCER BLOCKED** | The named `<60989` ledger is arithmetically consistent but cannot price a row not constructed. |
| `T-92920` | **BLOCKED** | Endpoint composition is downstream of the failed producer. |

## Requested criteria for PR #505

```text
orientation derives native rather than rough lift       YES, AS SIGNED ALGEBRA
Hall realizes every oriented observation positively     NO
hidden negative coordinate                               YES, ordinary q=2
one-shot uses actual responses rather than Omega(Y)      YES SYNTACTICALLY
actual responses positively placeable                    NO
q=2 normalization test                                   ROUGH-LIFT FIREWALL PASS;
                                                        CHILD SIGN TEST FAIL
all physical columns                                     CONDITIONAL SHARED BOUNDS
one-use source ownership                                 PASS AT SOURCE-LABEL LEVEL
one-use physical realization                             NOT ESTABLISHED
zero port                                                LEGITIMATE BY ABSENCE
signed finite comparison separated                       PASS
native deficit                                           NOT ESTABLISHED
endpoint chain                                           BLOCKED AT PRODUCER
```

**PR #505 end-to-end verdict:** **REQUEST CHANGES.** The orientation repair is a valid source-observation identity but not a positive physical compiler.

---

# 5. PR #507 claim-level verdicts

| Claim or interface | Local verdict | Finding |
|---|---|---|
| `R-92930` | **PASS, QUALIFIED** | Keeps the rough-lift separator in its correct scope and withdraws the unproved PR-specific use. |
| `L-92930.1--L-92930.5` | **PASS** | Correctly separates the native source tree from the row-first rough lift. |
| `L-92930` compiler contract | **NECESSARY, NOT SUFFICIENT** | Linking a compiler to the paired identity fixes normalization but does not prove positive physical realization. |
| `L-92931.1` | **PASS AS SOURCE-DISJOINT PAIRED IDENTITY** | Actual children have real source owners. |
| `L-92931.2/L-92931.6` | **FAIL AS POSITIVE CAPACITY IDENTITY** | The actual oriented child observation is negative in ordinary `q=2`; it is not an admissible positive capacity packet. |
| `L-92932` | **FAIL / FIRST TERMINAL-CHILD ARROW** | `L-91375/L-91751` apply only after entry into the positive typed packet cone. The oriented child block is outside that cone. |
| `L-92933` | **BLOCKED** | `493951/8<61744` is exact arithmetic conditional on invalid child terminalization. |
| `L-92934` | **FAIL / FIRST ONE-SHOT ARROW** | A label-blind quantizer is positive linear; it cannot turn separately placed negative-response child observations into positive rows. |
| `T-92930` | **BLOCKED** | Both advertised implementations fail before the native deficit. |

## Requested criteria for PR #507

```text
actual stopping-line source derives native marginal      YES, AS SIGNED ALGEBRA
source-tree child distinct from rough reservoir           YES
Hall/current placement realizes every observation         NO
hidden negative coordinate                                YES, ordinary q=2
one-shot uses actual response rather than Omega(Y)         YES SYNTACTICALLY
one-shot positive realization                             NO
terminal child uses actual response rather than Omega(Y)  YES SYNTACTICALLY
actual response promoted to positive capacity             YES / INVALID TYPE STEP
q=2 rough-lift firewall                                   PASS, QUALIFIED
all columns                                               CONDITIONAL SHARED BOUNDS
one-use source ownership                                  PASS
one-use physical ownership                                NOT ESTABLISHED
zero port                                                 LEGITIMATE BY ABSENCE
signed finite comparison separation                       PASS
native deficit                                             NOT ESTABLISHED
endpoint chain                                             BLOCKED AT PRODUCER
```

**PR #507 one-shot verdict:** **REQUEST CHANGES.**  
**PR #507 terminal-child verdict:** **REQUEST CHANGES.**

The terminal-child variant is not rescued by avoiding `Omega(Y)`: it instead promotes a signed actual response to a positive packet capacity, then invokes a theorem whose explicit premise is positive typed source entry.

---

# 6. Qualified `109/1200` statement

The exact retained statement is:

```text
at X=10^16;
if the ideal precomparison marginal is the complete thinned P61 rough lift;
and if the complete frozen downward allowances are bounded as stated;
then the final relative q=2 overfill is >109/1200.
```

It is not an unconditional refutation of PR #496, #500, #505, or #507 because those proposals claim a native paired source marginal rather than the full rough lift.

The negative-child-coordinate obstruction in this review is distinct and stronger for the new siblings: it accepts their source identity and shows that the claimed **branchwise positive physical realization** of its cancelling child term is impossible.

---

# 7. All columns, port, ownership and endpoint

## All columns

The inherited nonterminal and terminal estimates do cover the declared physical ranges, including `q=2` and every `2<=q<K_X`, conditional on a correctly normalized nonnegative ideal row. Neither sibling constructs that row. The all-column theorem cannot repair a negative-coordinate type error in its input.

## One-use ownership

Least-rough-prime and stopping-line labels give one source owner. This is a valid local repair. Ownership does not imply that the owner's signed observation is an admissible positive capacity. The missing theorem is physical realization, not source partition.

## Zero port

Both routes omit projective rough-state completion and any Schur-complement mechanism. Their zero auxiliary matrix port is therefore legitimate by absence. Reintroducing such machinery would require a fresh audit, but no port is needed to diagnose the present failure.

## Signed observations

Finite/continuum mismatch, collar and terminal corrections are correctly kept outside the positive-source ledger. The new leak occurs earlier: oriented child cancellation data are placed into the positive physical packet ledger even though their ordinary observation is negative.

## Endpoint chain

The native dual and one-sided endpoint consumer are not the first broken arrows. If a nonnegative row with the stated ordinary/detail capacities and bounded native deficit were supplied, the formal downstream composition would proceed on the frozen endpoint inputs. Neither sibling reaches that interface.

---

# 8. Genuine repair pursued separately

The exact repair is not another branchwise child packet. It is a **joint paired native compiler**:

```text
finite forcing and actual oriented rough children remain in one paired source;
source owners and orientation labels remain auditable;
no child is required to have a separate nonnegative physical realization;
one joint Hall/cancellation operation acts before channel subtraction;
only the total native marginal enters the nonnegative physical-row cone;
ordinary q and 4q are evaluated on that same total before detail;
one common quantizer, one thinning and one signed comparison are then applied.
```

A separate proposed packet `92940` records the exact no-go theorem and this open producer interface. It does **not** claim that the joint compiler has been constructed or that RH follows unconditionally.

---

# 9. Final boundary

```text
native versus rough-lift algebra                       VERIFIED
orientation bit as provenance                         VERIFIED
actual stopping-line source ownership                 VERIFIED
qualified 109/1200 rough-lift statement               VERIFIED IN SCOPE
branchwise positive oriented-child realization        FALSE
PR #505 one-shot producer                              BLOCKED
PR #507 one-shot producer                              BLOCKED
PR #507 terminal-child producer                        BLOCKED
all-column and <60989/<61744 arithmetic               CONDITIONAL ONLY
zero-port specialization                              VALID
finite signed-observation separation                  VALID
endpoint algebra                                      DOWNSTREAM CONDITIONAL
joint paired native compiler                          PROPOSED / OPEN
Riemann Hypothesis                                    UNPROVED
```

Lightweight exact replay:

```text
PASS_EXACT_ORIENTED_CHILD_Q2_NEGATIVE_COORDINATE_OBSTRUCTION
ddd7c681300e6b4400c509811148998a18488e4511ba181a847e97c095296694
```
