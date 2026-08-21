# X-91312 — Causal `P_79` low-prefix Hall certificate

This replay repairs the exact support error identified in review PR #431.

The historical checker replaced the parent kernel by a full formal prefix through `t+8`, even when the parent endpoint `py` lay between `t` and `t+8`.  This script retains both causal cutoffs:

```text
parent: d <= py;
child:  d <= y.
```

## Real-cell proof

For fixed prime `p` and threshold `t`, the parent prefix changes only when

```text
py = e,  mu(e)=1, t<e<=t+8,
```

and the child prefix changes only at a divisor activation `y=d`.  On every open cell the Hall margin is affine in `sqrt(y)`, so both endpoint limits suffice.  The script evaluates:

```text
the causal right state at every activation;
the left limit at every activation;
the active lower boundary y=max(1,t/p);
the terminal limit y=83 from the left.
```

## Infinite prime tail

Once `p>=max(83,t+8)`, every selected parent source is active.  Exact reciprocal-prefix positivity and exact child-margin positivity make the Hall margin monotone increasing in `p`.  The infinite tail is reduced to one real boundary value per threshold.

Thus the finite census consists of all actual primes before that boundary plus the boundary itself.

## Retained census

```text
P_79 mu=-1 thresholds below 4096:      385
finite prime plus tail cases:       91,090
real breakpoint sets:            4,616,606
child-margin checks:                 78,540
causal Hall checks:              18,102,064
all directed inequalities:       18,180,604
```

The exact fixed-denominator interval proof certifies

```text
target Hall margin > 7/4;
declared-score Hall margin > 3/2.
```

The global minima occur at

```text
target: t=73, p=83, y=2 from the left;
score:  t=79, p=83, y=85/83 from the left.
```

The score minimum is immediately before the missing parent source at `py=85` activates, which is precisely the cell omitted by the old formula.

Run:

```bash
python3 verify.py
```

Expected output:

```text
PASS_P79_CAUSAL_LOW_PREFIX_HALL
```

The script uses only the Python standard library.  It certifies Hall inequalities, not a source-labelled Hall flow, the `LRPT` packet, the full factor-54 recurrence, or RH.
