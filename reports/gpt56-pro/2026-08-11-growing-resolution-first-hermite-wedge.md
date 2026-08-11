# Growing-resolution first-Hermite wedge — 2026-08-11

**Branch:** `research/gpt56-pro/384-diagonal-heat-wedge`  
**Base:** PR #384 at `95ed673529fd4ed8ac9308f6ef43e11bda1954c1`  
**RH:** unproved

## Main theorem

For every `epsilon>0`, the first-Hermite scalar is unconditionally positive for all sufficiently large `|x|` throughout

```text
0<q<=(4-epsilon) log log(2+|x|).
```

The proof combines:

```text
gamma reserve      >= c q^-3/2 log |x|;
all-prime envelope <= C q exp(q/4);
pole term          exponentially negligible.
```

The ratio after normalisation is

```text
q^(5/2) exp(q/4)/log |x|,
```

which tends to zero below the constant four.

## Exact frontier

Any negative witness at height `x->infinity` must satisfy

```text
q/log log |x| >= 4-o(1).
```

The first-Hermite prime weight is concentrated near `log n~q`, so the first unresolved arithmetic scale is

```text
n~exp(q)~(log |x|)^4.
```

Crossing the boundary requires signed use of `cos(x log n)`; absolute prime estimates grow above constant four.

## Boundary

```text
subcritical growing-resolution wedge      proposed complete unconditional
constant-four necessary resolution law   proposed complete
prime scale (log height)^4               proposed complete saddle identification
boundary/supercritical signed sign        open / RH-equivalent
Riemann Hypothesis                        unproved
```
