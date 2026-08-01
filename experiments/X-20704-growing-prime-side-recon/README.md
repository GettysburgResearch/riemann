# X-20704 — Growing complete prime-side packet reconnaissance

This ordinary 60-digit experiment evaluates the complete released D-0001
finite matrix at

```text
(c,N)=(5,1),(10,2),(20,3),(50,4),(100,5),(200,6),(500,7).
```

Every level contains:

- the complete polar matrix;
- the cutoff-free archimedean matrix;
- every prime power `q<=c` with its von Mangoldt weight;
- rational-Leja first-frame rows from the first 100 critical-line zeros;
- the exact product-form kernel vector;
- one conditional second frame;
- the joint prime-side Schur pivot after eliminating the whole complement.

All seven midpoint Schur pivots are positive. The smallest retained value is

```text
4.81980622711245885233946415093e-33
```

at `(c,N)=(500,7)`.

The raw kernel coefficient norm becomes large, but the rational-Leja pivots
remain on ordinary scales (roughly `1e-3` to `1e-1`). This confirms the theorem
that generic raw Cauchy inversion is the wrong numerical object.

Run:

```text
python -m pip install mpmath
python recon.py --digits 60 --zero-count 100 --output /tmp/recon.json
cmp /tmp/recon.json results/recon.json
```

Classification: `NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE`.

The formulas are complete, but neither the special functions nor the zero
ordinates are directed in this experiment. It nominates the first growing
levels for an Arb replay; it is not a proof of their signs.
