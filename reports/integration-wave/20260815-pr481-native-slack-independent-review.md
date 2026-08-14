# Independent review of the claimed Gate A/Gate B packet and live PR #481

Reviewer: **GPT-5.6 Pro**  
Review cutoff: **2026-08-14T22:55:57Z**  
Repository: `gfreund123/riemann`  
Current `main` at cutoff: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Review branch: `review/pr481-native-slack-20260815`  
Review base: PR #481 head `f41bbd7608cc70bc2a8002d43ef99b5e35977968`

## Executive verdict

\[
\boxed{\textbf{GAP / BLOCKED — THE ADVERTISED PACKET IS NOT REPRODUCED, AND THE LIVE SUCCESSOR REMAINS CONDITIONAL}}
\]

The Riemann Hypothesis is **not proved** by the reviewed repository state.

There are two separate conclusions which must not be conflated.

1. The proposal described in the review request is not present at the quoted GitHub coordinates. Live PR #470 and the named branch have different heads, different files, and different theorem boundaries. The claimed Gate A/Gate B closure therefore cannot be reconstructed or accepted.
2. The newest actual corrected full-proposal descendant is PR #481 at `f41bbd7608cc70bc2a8002d43ef99b5e35977968`. Its new finite algebra is materially stronger than the rejected PR #476 chain, but the final composition still imports rather than reconstructs the concrete packet-capacity identity, the full common-port correction demand, the fixed terminal/base/port native cost, and the endpoint-to-RH consumer.

This is a request-changes verdict, not a claim that the surviving native-slack strategy is false.

## 1. Repository-coordinate reconciliation

The supplied summary identifies:

```text
PR:       #470
Branch:   research/gpt56-pro/91689-three-route-native-root-attack
Base PR:  #469
Base SHA: 3cf685181bd367b92cdcfeef9249e0b9b542a09e
```

The live graph at the review cutoff is different:

```text
live PR #470
  branch: research/gpt56-pro/91686-native-root-compiler-separator
  head:   89af3206ea1894884613e1188b5ab9a6a4cd74f0
  status: Native-Root Capacity Theorem OPEN; RH UNPROVEN

named branch research/gpt56-pro/91689-three-route-native-root-attack
  PR:     #475
  head:   6cba90ea10163abd62b051c83c8bfd8cc2f901da
  status: Gate A OPEN; Gate B OPEN; no full proposal
```

The exact theorem titles in the request, including

```text
L-91690 Hall-free raw residual closes the declared P61 row gate
L-91691 subcritical typed reset has a capacity-feasible depth limit
L-91692 root Hall, rough ownership and causal reset form one hereditary entry
L-91693 existing source atoms have a unique small/rough factorization
R-91687 unexpanded current slack is not the final tree deficit
T-91660 Gates A and B close the factor-67 endpoint consumer
```

are not the files at the quoted branch/head. Several IDs are already occupied in the live successor graph by different claims. In particular, live `L-91690` is the factor-67 target-Hall root-thinning theorem and live `L-91691` is the finite-realization theorem.

Accordingly, the advertised packet is classified **NOT REPRODUCED**. A prose summary cannot substitute for missing Git objects when exact source ownership and normalization are the load-bearing content.

## 2. Actual live full-proposal successor reviewed

The newest live corrected proposal at cutoff is:

```text
PR:      #481
Branch:  research/gpt56-pro/91726-pr476-native-slack-repair
Base:    research/gpt56-pro/91723-factor67-all-column-reserve
Base:    518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b
Head:    f41bbd7608cc70bc2a8002d43ef99b5e35977968
State:   open / draft / mergeable
```

This review inspected the load-bearing new files:

```text
L-91726  SHARP target monotonicity and weighted child mass
L-91727  packet-native slack cocycle
L-91728  all-column root cost in the native dual
L-91729  payment of the 10152 stability gate
L-91730  common-parent packet-capacity identity
L-91731  one-shot root realization and positive descendants
T-91724  corrected factor-67 composition
X-91726  finite regression and root-mass checker
```

It also inspected the frozen interfaces most directly used by those files:

```text
L-91375, T-91312, T-91313
L-91650, L-91653, L-91654, L-91658, L-91674
L-91688, L-91689, L-91690, L-91691, L-91694
L-91723, L-91724, L-91725
L-91316, L-91320, L-91378, L-91379
L-91110, L-91114, L-91115
```

## 3. Mathematics which survives reconstruction

### 3.1 SHARP target monotonicity and the actual weighted child bound

For a positive source measure and fixed source node `k`, the target kernel

\[
\mathsf T_u(k)=\left(4\sqrt{u/k}-3\right)k^{-1/2}
\]

is pointwise nondecreasing in `u`, with causal zero extension. Hence normalized same-index children are target-nonexpansive. Combining this pointwise fact with the exact causal coefficients

\[
\sum_i\alpha_i<67^{-1/2}<1/8
\]

gives the actual fiberwise weighted inequality, and positive endpoint integration preserves it. This repairs the mass-normalization gap found in the review of PR #473.

**Status: VERIFIED.**

### 3.2 Packet-native slack cocycle

Given the one-use identity

\[
\Omega(P)=\Xi(c)+r(P)+\int a(b)U_b\Omega(P_b),
\qquad r(P)\ge0,
\]

the vector and scalar recurrences

\[
s(P,d)=r(P)+\int a(b)U_bs(P_b,d_b),
\]

\[
\Delta(P,d)=\langle Y_4,r(P)\rangle+
\int a(b)\Delta(P_b,d_b)
\]

are exact linear algebra. Same-index placement leaves numerical detail coordinates unchanged, so the `Y_4` pairing commutes with the child insertion.

**Status: VERIFIED CONDITIONAL ON THE DISPLAYED ONE-USE IDENTITY.**

### 3.3 Sparse `Y_4` support and square-root thinning cost

The formulas

\[
Y_4(2^e)=\left(2^{\lceil e/2\rceil}-1\right)\log2,
\]

\[
Y_4(4^vp^a)=2^v\log p
\quad(p\text{ odd prime}),
\]

with zero elsewhere, agree with the defining recurrence. The elementary sums used in `L-91728`, the all-column mismatch/collar estimate on the frozen PR #479 input, and

\[
(1-\tau_K)J_\Lambda(X)<4290\log X,
\qquad
\tau_K=\frac{\sqrt K}{\sqrt K+130},
\]

are consistent. This is the correct replacement for the rejected bounded `4\sqrt X` score line.

**Status: VERIFIED ON THE FROZEN ALL-COLUMN INPUTS.**

### 3.4 Root target mass and descendant envelope arithmetic

The estimates

```text
fiber target mass <165;
endpoint measure mass <20;
integrated residual target mass <3300
```

follow from `H_66<5`, `sqrt(67)<33/4`, `0<L(x)<2`, and `log 67<5`. Given the hereditary positive-packet envelope, the entire recursive descendant contribution is an absolute constant.

**Status: VERIFIED CONDITIONAL ON THE HEREDITARY RESET FOR THE ACTUAL DESCENDANT PACKETS.**

## 4. First load-bearing broken arrows

### 4.1 The requested proof object does not exist at the frozen coordinates

This is the first failure in review order. The summary asserts a final remote head and checksum bundle but does not provide a SHA, and the quoted PR/branch pair points to two different live objects, neither of which contains the asserted Gate A/Gate B closure.

No theorem downstream of this missing publication can be marked verified. The correct classification is **NOT REPRODUCED**, not merely “pending stylistic cleanup.”

### 4.2 `L-91730` proves an implication, not the concrete root producer

`L-91730` begins by assuming both:

\[
\Xi(P_X)\le\Omega_X
\]

for one complete common parent packet and an exact aggregate split

\[
P_X=P_X^{\rm cur}+\int a(b)U_bP_b.
\]

Its packet-capacity identity is correct from those hypotheses. The new PR #481 regression checks this on a toy three-coordinate vector. It does not reconstruct, from the actual factor-67 endpoint measure and corrections, one concrete packet for which:

```text
source labels;
ordinary responses at q and 4q;
radix-four capacity;
current correction ownership;
child packet capacities;
terminal/base/common-port coordinates
```

all satisfy that equality simultaneously after finite realization.

The frozen formal intertwining theorem `L-91674` and the ideal identity in `L-91691` are relevant, but the proof still needs a single explicit theorem showing that the actual all-column realization and every finite correction preserve the exact packet identity used in `L-91730`, rather than only coordinatewise upper bounds and owner labels.

**Status: GAP / BLOCKED AT THE CONCRETE PRODUCER INTERFACE.**

### 4.3 The fixed terminal/base/common-port native cost is explicitly imported

`L-91728` states

\[
E_{\rm term/base/port}(X)=O(1)
\]

and calls it “an explicit independent reconstruction input.” It does not derive that bound in the theorem.

The common-port theorem `L-91725` proves a positive-linear aggregation statement under the fiberwise hypothesis

\[
D_s\preceq P_s,
\]

and bounds an integrated normalized port mass by `252`. That does not by itself instantiate `D_s` as the complete Hall, mismatch, collar, taper, base and quantizer correction demand, nor does bounded mass alone prove a bound on the `Y_4`-weighted unused detail vector. The required conclusion is not a scalar mass statement; it is

\[
\sum_qY_4(q)r_{\rm term/base/port}(q)=O(1).
\]

A valid closure may well follow from the endpoint-score normalization in the older port and omission theorems, but the exact map and inequality must be written and reconstructed for the actual factor-67 packet. Until then, the step from the verified `4290\log X` thinning term to the complete one-shot native root bound is conditional.

**Status: GAP / BLOCKED.**

### 4.4 The endpoint-to-RH implication remains an unreplayed conditional consumer

`T-91313` states the correct sign orientation

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X),
\]

and consumes an `o(\log^2X)` native deficit. PR #481 explicitly does not replay the resident endpoint/WSTS, prime-square moat or Mellin-Landau chain. Because the producer already fails review at the preceding interfaces, this review does not promote the endpoint implication.

**Status: CONDITIONAL / NOT REACHED.**

## 5. Exact secondary correction on the PR #479 base

`L-91723.16--.17` and `T-91721.3` contain a reversed inequality. The text says the unthinned root-Hall packet is score-superordinate to `4\sqrt X` and therefore scaling it by `\tau_K` loses at most

\[
4\sqrt X(1-\tau_K)<4290.
\]

If “score-superordinate” has its established repository meaning, then

\[
\operatorname{Score}(P_X)\ge4\sqrt X,
\]

so the removed score is

\[
(1-\tau_K)\operatorname{Score}(P_X)
\ge(1-\tau_K)4\sqrt X,
\]

not bounded above by that quantity. The `<4290` equality-score conclusion does not follow.

PR #481 does not need this false direction: `L-91728` instead uses the genuine upper bound

\[
(1-\tau_K)J_\Lambda(X)<4290\log X.
\]

Therefore the stale `<4290` base statement should be fenced or corrected, while the repaired `O(\log X)` native route remains a viable proposal.

**Status: REJECTED AS WRITTEN; REPAIRED IN THE LIVE SUCCESSOR BY A WEAKER VALID BOUND.**

## 6. Verification scope

The deposited `X-91726` checker is honest about its scope. It verifies:

```text
a small exact target-mass example;
a toy packet-slack cocycle;
formal Y4 support through q=2048;
several scalar constants;
the root mass arithmetic.
```

It explicitly marks the following as frozen reconstruction requirements:

```text
factor-67 Hall profile;
PR #479 all-column/knot/port realization;
fixed terminal/base/port native cost;
endpoint-to-RH implication.
```

Passing that checker therefore authenticates finite algebra only. It is not a machine certificate of the load-bearing analytic/physical interfaces.

## 7. Claim-status summary

```text
advertised PR #470 / branch 91689 packet          NOT REPRODUCED
live PR #470 at 89af3206                          VERIFIED SCOPE / NOT FULL
live PR #475 at 6cba90ea                          VERIFIED SCOPE / GATES OPEN
L-91726 target monotonicity and weighted mass      VERIFIED
L-91727 abstract packet-native cocycle             VERIFIED CONDITIONAL
L-91728 Y4 support and sqrt-thinning O(log X)      VERIFIED ON FROZEN INPUTS
L-91730 abstract capacity identity                 VERIFIED CONDITIONAL
concrete finite common-parent packet identity      GAP / BLOCKED
actual aggregate common-port demand                GAP / BLOCKED
fixed terminal/base/port native cost O(1)          GAP / BLOCKED
L-91731 descendant envelope                        VERIFIED CONDITIONAL
T-91724 complete corrected composition             GAP / BLOCKED
T-91313 endpoint-to-RH consumer                    CONDITIONAL / NOT REACHED
Riemann Hypothesis                                 UNPROVEN
```

## 8. Serious resolution path

The shortest reviewable closure is not another abstract recurrence. It is one concrete producer theorem, at a frozen head, with the following output:

1. Define the actual post-Hall, post-thinning, post-quantization parent packet `P_X` and its exact source labels.
2. Prove in ordinary coordinates at `q` and `4q`, before subtraction, the exact identity
   \[
   P_X=P_X^{\rm cur}+\int a(b)U_bP_b.
   \]
3. Instantiate the full common-port demand and prove `D_X\preceq P_X^{\rm port}` after every current correction is included once.
4. Derive an explicit constant `C_port` satisfying
   \[
   \sum_qY_4(q)r_{\rm term/base/port}(q)\le C_{port}.
   \]
5. Replace the toy capacity test with a checker or exact symbolic ledger tied to the actual packet formulas and frozen dependency blobs.
6. Independently reconstruct the one-sided endpoint/WSTS implication at its exact SHA.

If these statements pass, the already verified target contraction, packet cocycle, sparse `Y_4` arithmetic and one-shot descendant envelope would assemble into a genuinely reviewable `O(\log X)` producer.

No proposal branch was modified, no PR was merged, and no RH claim is promoted by this review.
