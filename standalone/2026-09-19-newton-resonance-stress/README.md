# NSR26 — execute the Newton attack, and test its real arithmetic content

**Status:** proposed component mathematics and exact finite research evidence.
**RH and the native all-scale energy gain remain unproved in this packet.**
Date: 19 September 2026. Continuation of #848, execution brief #902.

This is not another strategic review or a claimed RH completion. The pass
tried to turn the actual signed Newton update into a quantitative gain.
It found a stronger obstruction to a tempting norm-only proof, built an exact
adversarial certificate, and obtained a source-preserving regrouping that
substantially improves the separated finite energy budget.

## Main mathematical output

Read [PROOF.md](PROOF.md), Sections 2–4 first.

**Bounded input energy does not control generic Newton output at all.**
The proposed all-scale theorem constructs ternary prefixes with first
coefficient 1, bounded canonical input energy, both moment balances and ALL
completed coefficients bounded by 1, whose output energy grows at least
linearly in the input cutoff. The earlier BNR26 counterexample had large
balancing coefficients and input energy growing with the cutoff. Those
features are not necessary for the failure.

**This is a non-Mobius counterfamily, not a refutation of the native target.**
It fails the divisor-inverse identities; its initial fixed baseline already
fails at n=6. It demonstrates that those identities cannot be traded for
balance, coefficient bounds and small input energy.

The separately certified rational instance has Y=131072 and

```
1.629167080304 <= input A <= 1.629167080305
output A > 15.732535140697
absolute canonical tail coefficient < 0.001160835923236
```

The output lower bound covers a complete real interval, using 4,096 analytic
cell envelopes and two exact midpoint implementations. It is not a sampled
plot or an enumeration of seventeen billion output coefficients. The actual
prefix is a compactly encoded exact ternary word; no transcendental oracle
enters the acceptance calculation.

## Actual native work, not just the countermodel

Using `e=delta-1*g` for the literal truncated Mobius source, we reconstruct
Newton as `g+g*e`, cancelling the exact low-divisor fibers before squaring.
A causal small-prime regrouping then keeps every original coefficient while
combining its small-prime partners. Its cutoff terms vanish for a proved
support reason, not because they were omitted.

At Y=255, the complete annular energy is 0.179852003503... . With nine fixed
rows, the sum of separate row energies changes as follows:

| Small-prime product | Separate row energy | Valid nine-row Cauchy upper bound |
|---|---:|---:|
| 1 | 2.460478055389... | 22.144302498506... |
| 6 | 0.303702274816... | 2.733320473352... |
| 30 | 0.238532674099... | 2.146794066897... |
| 210 | 0.219222763075... | 1.973004867677... |

Use the outward intervals in [results.json](results.json) for exact receipts;
the displayed decimals above are descriptive truncations. The separate row
energy itself is NOT a universal upper bound. The remaining signed cross term
and the updated signed mean are retained. No uniform-in-Y improvement is proved.

The checker also certifies the existing native gain inequality at all 1,023
integer cutoffs 1 through 1023, covering output prefixes through 1,048,575.
Six source-first Newton reconstructions compare the full stated prefixes.
A finite successful recurrence is not an inductive proof for later scales.

## Replay

Python 3.11+; standard library only. From this directory:

```sh
python -I -S -B verify.py --check results.json
python -I -S -B test_verify.py
python -I -S -B -O verify.py --check results.json
python -I -S -B -O test_verify.py
```

`verify.py` authenticates the exact primitive word, independently compares
ordered product fibers with a hyperbola split at all 4,096 midpoints, pays the
whole interpolation/cross/tail error, regenerates all native data, and refuses
any changed result. Accepting arithmetic uses Python integers and rational
96-bit directed sums; there are no floating point comparisons.

[scout.py](scout.py) is optional ordinary-floating candidate generation. It
writes a new candidate, never overwrites the authoritative source, and makes
no certificate claim. Source selection is not primitive verification.

## Files and reading boundary

- [PROOF.md](PROOF.md): complete proposed counterfamily argument, rational
  certificate proof, native identities, elementary bounds and open step.
- [counterexample.json](counterexample.json): authoritative compressed ternary
  primitive, baseline, output window and fixed grid.
- [verify.py](verify.py) and [test_verify.py](test_verify.py): exact replay and
  bounded negative controls.
- [results.json](results.json): reconstructed finite receipts, with native and
  nonnative statements explicitly distinguished.
- [SOURCES.md](SOURCES.md): exact source commits, attribution and reading scope.
- [VALIDATION.md](VALIDATION.md): executed and unexecuted validation.

This addition changes no predecessor manuscript, canonical status, trusted
formal source, workflow or integration pointer. Keep it proposed on #848.
A publication receipt should name the actual final commit and readback, not
substitute the historical parent for a new head.
