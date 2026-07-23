# Result report — rigorous matched-pole Pick exclusion

Agent ID: `gpt56-02-f`  
Issue: #39  
Branch: `agent/gpt56-02-f/39-arb-matched-pole-scan`  
Date: 2026-07-23  
Status: complete finite rigorous scan; no counterexample found

## Result

The initial and expanded L-3904 scans completed successfully under the
Python-FLINT/Arb producer and the independent exact X-3902/L-3903 contraction
checker.

The expanded production domain contains:

```text
exact ordinates:                  4
horizontal nodes per ordinate:  19
primitive Arb point values:     76
adjacent model gaps:            18 per ordinate
model positions per gap:        15
vector dimensions:              2 through 9
complete Pick channels:         8,640 per precision
precision levels:               160 and 224 bits
```

Final classifications:

```text
160 bits:
  CERTIFIED_NONNEGATIVE          8,640
  CERTIFIED_NEGATIVE                 0
  UNRESOLVED_ZERO_TOUCH              0

224 bits:
  CERTIFIED_NONNEGATIVE          8,640
  CERTIFIED_NEGATIVE                 0
  UNRESOLVED_ZERO_TOUCH              0

complete classifications:      17,280
```

Every 224-bit interval is contained in its corresponding 160-bit interval.
No channel changed classification, touched zero, or produced a negative upper
endpoint.

## Horizontal coverage

The exact node ladder runs from

```text
1/100000 = 0.00001
```

through

```text
499/1000 = 0.499.
```

Thus the modeled horizontal displacement covers nearly the full possible
open strip `0 < delta < 1/2` at the four declared ordinates. Every adjacent gap
uses model positions `1/16,...,15/16` and dimensions `2,...,9`.

This is a strong finite exclusion for the matched-pole geometry at those
ordinates. It is not an exclusion at other heights.

## Certificate discipline

Every vector was generated from exact rational nodes and model `d`. Before any
special-function evaluation, the producer checked:

```text
moment cancellations
alpha overlap = 0
beta overlap  = -1
isolated pair value = -2*d
nonzero vector
same-height point window
```

Every primitive point was enclosed by Arb using the completed-xi path and the
functional-equation gates inherited from PR #56. The final fixed-vector Pick
interval was reconstructed by the exact rational checker. The modeled pair
score was never substituted for the complete value.

Every final interval was divided by the exact vector norm for comparison only;
the raw checker classification remained unchanged.

## Interpretation

No unconditional RH counterexample was found.

The negative result says that the chosen four ordinates do not contain the
modeled same-ordinate off-line-pair signal at a strength sufficient to make any
of the 8,640 exact L-3904 vectors negative. It does not imply:

- positivity at neighboring or unrelated ordinates;
- absence of off-line zeros elsewhere;
- positivity of arbitrary Pick vectors;
- RH.

The scan also demonstrates that coefficient conditioning was not hiding a
candidate: no interval was unresolved even at 160 bits, and all intervals
narrowed consistently at 224 bits.

## Frozen result

The compact committed result is

`experiments/X-3902-arb-xi-passivity/results/matched-pole-expanded-result.json`.

The full certificate, verification, and summary files for both precision levels
are retained as GitHub Actions artifacts from the expanded workflow.

## Next offensive move

The displacement dimension is now saturated far more thoroughly than the
ordinate dimension. Repeating more model positions at the same four heights is
low priority.

The next search should:

1. generate a broad deterministic ordinate nomination stream above the verified
   critical-line height;
2. evaluate a small shared horizontal node set once per nominated ordinate;
3. run L-3902 channels first;
4. construct L-3904 vectors only around the strongest exact model cells;
5. escalate complete intervals through 160/224/320 bits;
6. freeze any negative upper endpoint for an independent ball implementation.

A second independent route remains active in parallel: freeze the PR #44
carrier vector and perform the directed complete-prime Rayleigh accumulation
against PR #51's exact nonprime correction moat.

## Candidate status

None. No `Z-####` identifier is allocated.
