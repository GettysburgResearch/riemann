# Agent report — recovered target vector and rigorous phase-grid kernel

Agent: `gpt56-01-f`  
Date: 2026-07-25  
Cross-route target: Issues #28/#42; PR #65  
Branch: `agent/gpt56-01-f/65-rigorous-phase-grid`

## Starting point

The previous proof-production pass had closed the exact alpha, nonprime
correction, shard-composition, and fixed-vector interfaces, but the historical
`c=10^11`, `K=1024` discovery coefficients and vector were not preserved.

During this continuation, PR #65 regenerated and committed:

- all 5,000 discovery segments arranged as 50 complete shards;
- exact global counts `4,118,054,813 + 28,156 = 4,118,082,969`;
- a complete merged Toeplitz midpoint result;
- a 96-bit Gaussian-dyadic vector;
- exact autocorrelations and normalization fingerprints.

The preserved vector SHA-256 is

```text
3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
```

and the canonical coordinate-object digest is

```text
e0e861b4b619e17f74d83c41905ef46587ef027289716e30453c2b0aa8b4c96d
```

The regenerated ordinary midpoint leading margin is positive,
`+0.0002691184519925116`, with residual about `2.622e-15`.  These are discovery
diagnostics only.

## New proof units

### L-2813 — phase-grid compression

For a frozen exact vector, grid every phase by `M` roots of unity, accumulate
complex residual moments through order `R`, and contract only after the complete
stream.  The total Taylor error is bounded by

```text
W_x exp(pi/M) (pi/M)^(R+1)/(R+1)!.
```

At the active target, `M=32768`, `R=3`, and elementary rational estimates prove

```text
error < 1/21,816,000,000 < 1/20,000,000,000.
```

This is below one tenth of the exact nonprime correction gate.  The lemma gives
an independent proof-producing alternative to one high-precision trigonometric
evaluation per prime power.

### L-2814 — one directed precision suffices

A single collection of outward shard intervals is already an inclusion proof.
Duplicate 256-bit evaluation is valuable reproduction, but it need not block
the first exact verdict.  If a complete 192-bit interval meets zero, only shards
whose radii need reduction must be rerun; nonempty interval intersections retain
rigor under heterogeneous precision.

## Verification

The standard-library exact checker for the L-2813 target specialization was run
locally.  Five tests pass:

- committed target clears the rational gate;
- halving the grid is rejected;
- lowering the Taylor order is rejected;
- vector-fingerprint mutation is rejected;
- Boolean-as-integer schema mutation is rejected.

The checker output contains only integer and `Fraction` arithmetic.  It proves:

```text
derived W upper       32,887,712 / 3
eta upper             11 / 114,688
coarse remainder      1 / 21,816,000,000
required gate         1 / 20,000,000,000
```

## Pilot implementation finding

A straightforward interval-moment prototype enclosed all `78,734` prime-power
terms through `c=10^6` and contained an independent 80-decimal direct value.  A
`c=10^7` timing comparison showed that the naive MPFR moment implementation was
not yet faster than direct MPFR sine/cosine because four interval moments add
several multiplications per term.  No speedup claim is therefore made for that
prototype.  The durable contribution is the exact compression theorem and
remainder moat; an optimized producer must benchmark before replacing X-2805.

## Coordination

A handoff comment on PR #65 records:

1. the recovered vector and fingerprints;
2. the sufficiency of one first-pass directed precision;
3. a quota-safe one-host/multiworker scheduling suggestion;
4. the new phase-grid route as independent acceleration/reproduction work.

## Counterexample status

No strict negative interval was produced.  No `Z-####` identifier is allocated.
The regenerated midpoint is positive and suggests that this particular basin
may close positively, but no sign is asserted until the complete directed
fixed-vector interval is composed.

## Next actions

1. Finish one complete 192-bit X-2805 scalar pass over the 50 target ranges.
2. Assemble it immediately with the exact alpha and correction artifacts.
3. If strict, retain the exact verdict and rerun independently at 256 bits.
4. If unresolved, use L-2814 to escalate only the widest shards.
5. Implement a performance-optimized L-2813 producer only if benchmarked faster
   than the reviewed direct backend.
6. In parallel, continue searching distinct carrier/cutoff basins rather than
   assuming this positive-midpoint vector will become a counterexample.
