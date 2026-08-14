# Factor-67 target Hall and the SONTR closure proposal

Date: 2026-08-14  
Status: **candidate complete SONTR composition; RH unproved pending review**

## Executive result

The source-owned native-thinning problem admits a substantially cleaner
composition once the reset boundary is moved from the historical one-crossing
constant to the exact rough threshold `67`.

Use

\[
 K=\lfloor X/67\rfloor+1.
\]

Then every outer normalized quotient satisfies `x=X/s<67`. Root Hall therefore
sees only the finite `P_61` arithmetic source, while every prime at least `67`
remains in the exact first-owner rough partition. This removes the source
collision which made raw stopped-leaf current infeasible.

The pass proves or assembles the following:

```text
root equality and reserve states positive through 67;
all 22 root target Hall prefixes >7/20;
one target-exact positive residual source;
score superordination and nonnegative bonus in every row;
unique first-owner rough provenance;
recursive coefficient mass <1/8;
finite mismatch constant C67<19;
interior detail correction <177/K;
terminal overfill <4452 X^-3/2;
fixed omission reserve >5033 X^-3/2;
one global quantizer, correction packet and shared port.
```

The resulting packet is the proposed Source-Owned Native Thinning and
Realization theorem (`SONTR`).

## I. Why the strict window matters

At a stopped leaf, the parent argument `py` is unbounded and the no-upward Hall
prefix at `y=13` is negative. At the root, the same arithmetic threshold is
evaluated only for `x<67`.

For target atoms

\[
 T_x(k)=4\sqrt x/k-3/\sqrt k,
\]

the threshold margin is

\[
 H_t(x)=4\sqrt x\sum_{n\le t}\mu(n)/n
       -3\sum_{n\le t}\mu(n)/\sqrt n.
\]

Every threshold is positive. The minimum is at `(t,x)=(13,67)` and is greater
than `7/20`. The root Hall graph is therefore valid even though the stopped-leaf
Hall graph is false.

Because `x<67`, the root operation never consumes the prime `67`. The rough
monoid begins precisely where the finite root source ends.

## II. One common target flow

The target Hall flow is source-owned and exact. Its residual coefficient vector
uses every positive even source at most once. The same flow is favorable in the
other coordinates:

- score per target decreases with `sqrt(x/k)`, so matched even score is no
  larger than matched odd score;
- each component row per target increases with `x/k`, so matched even row is no
  smaller than matched odd row.

Thus

```text
signed target = positive residual target;
positive residual score >= signed score;
signed row = positive residual row + nonnegative target-null bonus.
```

No coordinatewise complement or stopped-leaf Hall theorem is used.

## III. Rough first-owner causal reset

Attach the exact first-owner label of `L-91688` to every residual source. Apply
the causal identity only after positive root entry. Every monomial is then
owned once by:

```text
current survival;
current causal difference;
one recursive child;
terminal stop;
or unused thinning.
```

The total recursive coefficient is below `1/sqrt(67)<1/8`.

## IV. Finite realization without false equality

The finite equality seed is not equal to its continuum Volterra model. The
exact discrepancy at `X=3,m=2` remains positive. The construction does not
remove that firewall.

Instead, all positive endpoint fibers are summed and quantized once. Two
literal thinning operations create enough native reserve:

1. multiply retained endpoint weights by `(1+178/K)^(-1)`;
2. omit a fixed top interval of width `10000`.

The factor-67 mismatch computation gives

\[
 C_{67}<19,
\]

which propagates to the relative interior error `<177/K`. In the terminal
annulus the possible overfill is below `4452X^-3/2`, while the fixed omission
removes more than `5033X^-3/2`.

Every outer physical detail column is therefore feasible. Ordinary feasibility
follows from the positive radix-four inverse. The exact inner residual remains
in the contracted first-owner child packet and is never approximated twice.

## V. Score and weighted slack

Root target Hall creates no declared-score debt. Positive causal generators have
debt at most twice their exact target mass. The safety factor, fixed omission,
mismatch, taper, finite base and common port cost only one absolute amount per
generation.

Hence the normalized equality deficit satisfies

\[
 \Lambda_{eq}(X)
 \le C_{67}+\rho\Lambda_{eq}(X/67+1),
 \qquad \rho<1/8,
\]

and is uniformly bounded.

After restoring the exact native benchmark,

\[
 J_\Lambda(X)-\mathcal H(d_X)
 \le4\log X+O(1).
\]

The radix-four dual turns this into

\[
 \sum_qY_4(q)s_X(q)
 =O(\log X)=o(\log^2X).
\]

This is the conclusion-producing SONTR slack bound.

## Verification

```bash
cd experiments/X-91690-factor67-sontr
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_TARGET_HALL_SONTR_ROOT_PACKET
```

Proof-object digest:

```text
37774aeb5a1843c75ce14b8a0a6c167f743faa60e9582d2939acf6d7addce53a
```

The replay certifies the compact arithmetic and analytic constants. It does not
by itself replay every imported endpoint-frame, causal, common-port or
endpoint-consumer theorem.

## Exact boundary

```text
factor-67 root Hall and source ownership        PROVED EXACT/DIRECTED
factor-67 finite correction constants           PROVED EXACT/DIRECTED
full endpoint-frame SONTR composition            CANDIDATE COMPLETE
Native-Root Capacity Theorem                     CANDIDATE COMPLETE
endpoint-to-RH implication                       FROZEN CONDITIONAL CONSUMER
Riemann Hypothesis                               UNPROVED PENDING REVIEW
```
