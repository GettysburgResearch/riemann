# X-105659 — Rank-two Cauchy translation trace replay

Run:

```bash
python -B experiments/X-105659-rank-two-cauchy-trace/verify.py
```

Expected verdict:

```text
PASS_X_105659_RANK_TWO_CAUCHY_TRACE
```

The script works symbolically over exact rational functions.  It uses the
normalization

```text
lambda_1=A,
lambda_2=B+iD,
H>0,
U=D^2,
P=A+B,
R=AB.
```

It constructs the exact two-by-two Cauchy Grams, clears the positive rational
denominator of

```text
tr(G0^-1 G_(2H) G_(4H)^-1 G_(2H))
 - tr(G0^-1 G_H),
```

symmetrizes in the two positive depths, and verifies coefficientwise
nonnegativity in `P,R,U,H`.  Four strict rational fixtures are also replayed.

The replay proves only packet rank two.  It does not extrapolate to arbitrary
rank, execute a cofinal Xi passage, establish the pointwise microscope, or
prove RH.
