# M-15106 — Source-bound singular-seam quartic producer protocol

Methodology ID: `M-15106`  
Status: **EXECUTABLE FAIL-CLOSED PROTOCOL**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15141`, `X-15120`, the directed `tau_4` target of `X-15119`

## 1. Purpose

Emit the first honest quartic row for the complete singular-seam comparison
chain, without substituting a surrogate operator for an unspecified source map.

## 2. Required source package

Fill a manifest with schema

```text
riemann.singular-seam-source-row.v1
```

and bind:

- manuscript version and normalization/source-map SHA-256 fingerprints;
- a concrete window identifier and cutoff;
- the exact parameter values `alpha,s_R,a_tr`;
- one finite readout Gram and quartic jet coordinate;
- matrices for raw and finite-jet contour coordinates;
- seam transpose, comparison trace, `LCI`, projection, and seam involution;
- a directed `a_(4,M)^lin` interval;
- the independent directed `tau_4` interval.

Every matrix must be generated from the named source definitions and use one
common finite basis.  If transcendental entries are not exact, the source
producer must emit directed rational enclosures and a compatible interval
consumer; point midpoints are insufficient.

## 3. Command

```bash
python experiments/X-15120-singular-seam-source-producer/produce.py \
  source-bound-M1.json > results/source-bound-M1-row.json
```

An incomplete package returns

```text
SOURCE_SPECIFICATION_INCOMPLETE
```

with the missing paths.  A complete exact package returns

```text
CERTIFIED_SOURCE_BOUND_QUARTIC_ROW
```

and emits `c4`, `A`, `K`, `Tr A^4`, `Tr K^4`, the jet Schatten-four value,
and the directed target relations.

## 4. Growing-window ladder

For windows `M_1<M_2<...`, retain separately:

```text
c4_normalized_lower_bound_squared
jet_schatten4_fourth_power
trace_A4
trace_K4
a4_linear_interval
tau4_interval
normalization_sha256
source_map_sha256
```

A persistent positive lower bound on the normalized `c4` value proves a body
obstruction.  A decreasing `c4` value is not a proof of full Schatten-four
decay; the complete `jet_schatten4_fourth_power` must also tend to zero.

All source-package fingerprints must remain compatible across refinement.

## 5. Immediate handoff

The public-source audit manifest already binds every datum that is explicitly
available and reports the remaining 17 fields.  The next source-level
contribution should supply those fields for one actual first window, not another
abstract convergence statement.
