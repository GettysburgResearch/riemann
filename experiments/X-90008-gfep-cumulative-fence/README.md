# X-90008 — Exact GFEP cumulative fence

Run:

```bash
python experiments/X-90008-gfep-cumulative-fence/verify.py
```

Expected first line:

```text
PASS_EXACT_GFEP_FOURFOLD_CUMULATIVE_REFUTATION
```

The checker uses only integer arithmetic and `fractions.Fraction`.  It builds the
exact first-entrance weight for

```text
X=1000, n=21, p=21,
```

forms the Möbius-transformed kernel `K=(Delta F)*mu`, and evaluates its first six
successive prefix sums.  In particular it authenticates

```text
C4(841) = -21060753/8 < 0.
```

This refutes the fixed fourfold cumulative-positivity shortcut in `R-90004`.
It does not test or refute GFEP itself.
