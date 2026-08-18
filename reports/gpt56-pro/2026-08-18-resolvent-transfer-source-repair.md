# Research digest — raw/contracted resolvent transfer and two-channel source repair

## Chosen task

I adopted PR #576 at exact head
`0f6ea6eae813c1d867ae50744cf5fd57e2720bb7` and attacked the source object it
left open: a literal positive current plus contracted children that preserves
every raw rough coefficient.

This was higher leverage than rechecking the already repaired `1/42` bias. The
surviving proposals repeatedly compose a raw parity edge `r=p^(-1/2)` with a
smaller safe child coefficient while treating the resulting current as if it
were a local finite-P61 scalar packet.

## New results

1. **Exact resolvent conjugacy.** The native scalar is `f=(I+R)^(-1)b`; any
   contracted recursion `T` forces `g=b+(T-R)f`.
2. **Universal local one-channel no-go.** On two nodes, a positive child datum
   gives current `t-r<0` whenever `t<r`. The exact transfer has an alternating
   nonzero coefficient at every history depth.
3. **Literal positive source repair.** In the paired parity cone, place the
   leftover `(r-t)S child` in the current and `tS child` in recursion. This is
   positive, source-disjoint, activation exact, first-owner exact, and retains
   the raw coefficient.
4. **Two-channel minimality.** No nonzero positive scalar map can implement the
   parity sign character.
5. **Exposure conservation.** Current exposure plus recursive exposure is the
   raw exposure. The `<1/8` safe budget cannot replace it. With the repaired
   bounds, interval-only arithmetic needs raw mass at most `4/21`.
6. **Sharp frontier.** The remaining theorem is the nonlocal Bellman current
   inequality `NCBI67: c>=Tc`, equivalent in role to CPSL67/GPHT*/GABPT/TFPE/ACBI.

## Portfolio change

The literal source identity requested by PR #576 is no longer open at the
paired-source level. What remains is narrower and more difficult: the signed
observation of that positive current is nonlocal in the complete child state.
No further local P61 bias improvement can remove this dependence by itself.

The result redirects the factor-67 portfolio toward global parity Hall,
trace-free Julia extraction, or another genuinely nonlocal invariant. It also
provides a precise rejection test for future claimed safe-child compositions.

## Verification

```text
PASS_T97500_RAW_CONTRACTED_RESOLVENT_AND_TWO_CHANNEL_SOURCE_REPAIR
5cd6ea67db8bb335c3d349917ff2b7d739fba83a99231efac27939ae5eb3e9b0
```

Exact rational replay covers 144 random resolvent conjugacies, 16 two-node
separators, 11 nonlocal chain depths, 256 positive paired-source splits, 512
exposure-conservation fixtures, minimality checks, and six hostile mutations.

## RH status

```text
Riemann Hypothesis: UNPROVEN
```
