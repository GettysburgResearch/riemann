# PR #497 comparison and directed Target-Lorenz hardening

Date: 2026-08-15  
Repository: `gfreund123/riemann`  
Frozen proposal: PR #497 at `bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74`  
Frozen base: PR #468 at `9e2ae6d26a7920055e1f11327dc0ddeb7b855c61`  
Intended successor: `research/gpt56-pro/93780-target-lorenz-directed-hardening`  
RH status: **unproved pending independent reconstruction**

## Executive conclusion

The unpublished `93420-target-lorenz-complete-successor` packet must not be
republished. PR #497 is a newer durable realization of the same programme and
is mathematically stronger on the tail:

```text
93420:
  uniform remainder asserted as 2/25;
  17,508,451-event extremal-row description;
  floating tail values;
  explicit leaf label and current-only bonus notation.

PR #497:
  proved 5Y^(-3/2) Euler-ramp remainder;
  explicit first-activation boundary strip;
  all 65 rows;
  51,118,080 exact uint128 event records;
  explicit common-parent integral;
  all-column one-shot native and 60989 Y4 ledger.
```

The only genuine `93420` carryover is the more explicit source/physical typing:
the Target-Lorenz residual is positive source, while the AVLT row bonus is a
current-only physical row with one leaf owner. That distinction is installed in
`L-93783` without reviving any `93420` claim.

PR #497 is therefore adopted as the controlling frozen proposal. The present
successor adds only nonduplicative hardening.

## I. Claim-by-claim disposition

The exact table is deposited under

```text
audits/gpt56-pro/2026-08-15-93420-vs-pr497-claim-comparison.tsv.
```

Summary:

| Preserved local object | PR #497 object | Verdict |
|---|---|---|
| `L-93420` tail | `L-93600/L-93601` | PR #497 strictly controls |
| `L-93421` AVLT | `L-93602` | duplicate, PR #497 controls |
| `L-93422` common parent | `L-93603` | same theorem; carry only explicit typing and labels |
| `L-93423` two-ledger feasibility | `R-93600/L-93604` | duplicate, PR #497 controls |
| `L-93424` native cost | `L-93605` | duplicate, PR #497 controls |
| `R-93420` firewall | `R-93600` | duplicate |
| `T-93420/T-93421` | `T-93600/T-93601` | duplicate |
| `X-93420` | `X-93600/X-93601` | PR #497 stronger artifact |

The local SHA-256 values and PR #497 content-manifest SHA-256 values are in the
TSV, making this disposition reproducible without relying on titles.

## II. Directed tail replacement

PR #497 correctly sorts every event exactly, but its decisive transcendental
values are computed in unprotected extended `long double` and guarded by a
one-unit reserve. The successor replaces that contract completely.

### Directed constants

`L-93780/X-93780` prove by Hurwitz Euler--Maclaurin with an exact periodic-`B_2`
remainder that

```text
zeta(1/2)  in [-1.460355,-1.460354];
zeta'(1/2) in [-3.922647,-3.922646].
```

The narrower computed intervals and exact remainder radii are retained in
`results/zeta_intervals.json`.

### Every event interval

The PR #497 analytic envelope is reevaluated with:

```text
exact uint128 event ordering;
integer-to-long-double adjacent-value bracketing;
Boost.Numeric.Interval;
saved hardware fenv directed rounding;
directed sqrt and log;
-frounding-math -fno-fast-math;
all sums, products, derivatives and final-tail polynomials interval-valued.
```

All 65 rows and all `51,118,080` event records certify:

```text
full causal determinant lower     26.785819887137002938...
parent determinant lower          79.236873638887636066...
parent derivative lower            0.239715873017393344...
minimum row                        66
minimum x                          166000
```

The final unbounded interval has positive directed persistence polynomials.
This closes the stated floating-evaluation vulnerability rather than merely
widening its heuristic reserve.

## III. Row-66 extremality and exact join

A directed upper enclosure of the row-66 lower envelope at the boundary is

```text
26.786653212345143966...
```

while the nearest competing global row certificate, row 65, has lower bound

```text
28.241619047675702022...
```

so row 66 is the unique extremal certificate row with separation

```text
>1.454965835330558.
```

The theorem is deliberately finite and precise: it concerns the global minima
of the deposited lower-envelope certificate, not an unproved pointwise ordering
between exact row determinants.

The compact theorem owns the real half-open domain `x<166000`; the directed
tail owns `x>=166000`. The two are disjoint and exhaustive, and the boundary is
directedly positive. The frozen compact claim and result blobs are recorded in
the control file.

## IV. Concrete typed leaf and common parent

The successor rewrites the leaf construction as a direct-sum typed object

\[
G_\omega=(\nu_\omega;B_\omega;\sigma_\omega),
\]

with

```text
nu=E-U                     positive residual arithmetic source;
B=R(U)-R(O)>=0             current-only physical row bonus;
sigma=S(O)-S(U)>=0         declared-score surplus.
```

The exact identities are

\[
T(\nu)=T(E)-T(O),
\]

\[
S(\nu)=S(E)-S(O)+\sigma,
\]

\[
R(\nu)+B=R(E)-R(O).
\]

This derives the physical leaf marginal directly. It does not require an
abstract joint coupling and does not claim that `B` is positive source. Every
leaf has the complete owner label

```text
(endpoint cell, rough history, first owner, P61 divisor, parity, causal path).
```

The common parent is the explicit positive integral of these typed leaves.
All actual child rows remain internal colours. The exported recursive family is
empty. The declared operation list has no auxiliary state completion, so the
root matrix port is exactly absent rather than assumed affordable.

## V. Native all-column and `Y_4` composition

The positive source operations are performed once:

```text
literal omissions;
one common thinning;
one parent pushforward;
one positive global quantizer.
```

Finite/continuum, collar and terminal data remain one separate signed
observation ledger. The frozen all-column estimate gives

\[
\tau_K(1+129/\sqrt K)
=(\sqrt K+129)/(\sqrt K+130)<1
\]

for every nonterminal `q>=2`, including `q<K`; the terminal omission leaves
`581X^(-3/2)`. Positive radix-four inversion gives ordinary feasibility.

Only then is

\[
r_X=\Omega_X-\Xi(d_X)\ge0
\]

defined. Direct `Y_4` pricing gives

```text
12012 + 4 + 48972 + 1 = 60989 < 61000.
```

No signed error is called positive source, no full child capacity is promoted,
no recursive slack is exported, and no estimate of
`J_Lambda(X)-4sqrt(X)` appears.

## VI. Endpoint dependency reconstruction

The successor lock is transitive enough for hostile review. In addition to the
PR #497 producer blobs, it freezes the endpoint chain at:

```text
PR #352 head 906b5a477a1ed7c88a40db7569924f15f3d54b72
  L-90004 blob 17036c42170750956743555458104bdbada954e4
  L-90006 blob 201de91c1f38334da7dc54cab04f78a8720c4bd6
  T-90008 blob 21eae10025b03b724233d49ea09fbc90f4aa66fd

PR #353 head ed566f3198e236c54ba18049181016536f56d456
  L-90020 blob bfe7b71eb2db0a2ad4d987e75b43d5872fc84d37
  T-90011 blob 9c93dc10bb12d85785d16f4643dd81d3070c0043
```

The exact implication remains proposal-level: native deficit `<61000` gives the
one-sided bound on `F_Lambda`; the prime-square moat forces the prime endpoint
negative; the Mellin pole audit and Landau theorem exclude an off-line zero.
Those analytic files remain independent reconstruction targets.

## VII. Provenance correction

PR #497's lock contains incorrect strings for the heads of review PRs #490,
#491 and sibling PRs #493, #494. `R-93780` and the new lock record the live exact
heads. This is a metadata repair, not a change in the mathematical dependency
DAG.

## Verification

```bash
cd experiments/X-93780-target-lorenz-directed-tail
python3 verify.py --output /tmp/x93780.json
python3 verify.py --full --workers 4 --output /tmp/x93780-full.json

cd ../X-93781-target-lorenz-typed-ledger
python3 verify.py --output /tmp/x93781.json
```

Retained verdicts:

```text
PASS_TARGET_LORENZ_DIRECTED_TAIL_HARDENING
PASS_TARGET_LORENZ_TYPED_LEAF_COMMON_PARENT_NATIVE_LEDGER
```

The complete 65-row directed campaign was executed in 65 independent row
runs and aggregated before publication. Quick mode reruns the extremal row and
audits the retained all-row object; full mode reproduces every row.

## Exact boundary

```text
93420 packet                                     superseded / not republished
PR #497                                         controlling frozen proposal
directed zeta primitives                       proved
51,118,080 directed tail events                 proved on PR497 formula
row-66 certificate extremality                  proved directed
compact/tail real-domain join                   exact
complete AVLT                                   hardened candidate on frozen compact input
typed leaf marginal and ownership               exact algebra
concrete common-parent/native compiler          proposed complete on frozen frame bounds
native Y4 deficit                               <60989 on frozen estimates
endpoint chain                                  explicitly frozen / reconstruct
Riemann Hypothesis                              unproved pending hostile review
```
