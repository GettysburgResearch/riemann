# Integration handoff — L-14316 / L-14317 / T-14305

Target stack: PR #152, Issue #143.

## What to import

- `L-14316`: ambient multiplier floor from the uniform Fourier-density cap;
- `L-14317`: packet/radical complement floor from the exact leverage deficit;
- `T-14305`: cofinal lowest-symbol-volume criterion implying RH;
- `X-14309`: exact ambient cell-deficit checker;
- `X-14310`: exact packet-leverage checker.

## Recommended order

For every exact Suzuki symbol level:

1. run `X-14309` on the complete directed cell table;
2. if it fails, remove the exact constant radical and run `X-14310`;
3. if needed, enlarge the packet to the weighted/multiband low space of
   `L-14311` and recompute its leverage-deficit cap;
4. apply `L-14308` only to the unresolved finite packet itself;
5. feed the resulting whole-space floor into `T-14302`.

## Required producer artifacts

```text
support a
exact normalization digest
disjoint rational frequency cells
outward lower complete-symbol bound per cell
analytic tail floor and digest
complete breakpoint levels
X-14309 verification output
```

For `X-14310`, additionally retain:

```text
exact packet/radical basis or Gram certificate
packet digest
directed upper leverage-deficit bound per frequency cell
subspace-error moat for any approximate packet
```

## Search metrics

Ambient rank:

```text
sup_G [G-(1/pi) integral (G-s_a)_+].
```

Packet-complement rank:

```text
sup_G [G-integral c_K(xi)(G-s_a(xi))_+ dxi].
```

Do not rank by the sampled symbol minimum.

## Nonclaim

No production symbol floor, leverage floor, or cofinal estimate is supplied. RH
remains open.
