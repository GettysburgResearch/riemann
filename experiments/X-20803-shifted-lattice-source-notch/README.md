# X-20803 — Exact shifted-lattice source-notch replay

This standard-library-only checker replays the finite algebra in `L-20803` for

```text
theta = 3/4,
N = 1,...,8.
```

At each level it constructs

```text
P_N(x)=product_(j<=N) [x-(j-theta)^2],
D_N(x)=product_(j<=N) [x-j^2],
```

extracts every partial-fraction residue exactly, and verifies

```text
P_N(x)/D_N(x)
 =u_0+2 sum_(n=1)^N u_n x/(x-n^2),

u_0+2 sum_(n=1)^N u_n=1,

u_n>0.
```

The emitted coefficient metric is

```text
u_0^2+2 sum u_n^2.
```

Run:

```bash
python verify.py --max-n 8 --output results/verification.json
python -m unittest discover -s tests -v
```

The checker certifies the rational finite identities only. The gamma-ratio
asymptotic and the metric-adjusted exponent wedge are proved analytically in the
claim file. No Schur sign or RH conclusion is inferred from this replay.
