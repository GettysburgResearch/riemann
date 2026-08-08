# X-27901 — Dyadic shell one-crossing replay

This standard-library package supports `L-27901`--`L-27904` and the full proposal `T-27901`.

## Run

```bash
python3 verify.py
```

The retained result is in

```text
results/verification.json
```

with digest

```text
cf3007f56fb5a85f008bcd99723b4c24c1323e8252601eaaa9e821d4649c402d
```

## What the replay checks

The script reconstructs the reciprocal-cell shell formula and reports:

- the unique continuum zero bracket;
- the signs at `1/7`, `1/8`, and `1/9`;
- the maxima of the six negative upper cells;
- derivative-left margins through cell 200,000;
- all-coordinate finite shell scans through `X=20,000`;
- prime-coordinate scans through `X=200,000`;
- the maximum weighted prime tail and its start.

Every retained finite shell has one sign change and no positive weighted prime tail.

## Separate discovery

An optimized floating reconnaissance, not replayed here, scanned prime shells through

```text
X=10,000,000
```

and found

```text
one-crossing violations             0
positive weighted-tail violations   0
crossing ratio                       0.1408523
```

This evidence is discovery only.

## Proof boundary

The package does not prove the analytic claims. In particular, it does not certify:

- the all-cell inequalities in `L-27901`;
- the Euler/Hurwitz asymptotics and transition derivative in `L-27904`;
- endpoint prime domination `EPD`;
- squarefree collector existence `ESC`;
- WSTS;
- RH.

`FSCR` is claimed by the written analytic theorem `L-27904`, not by this finite replay. A reviewer must verify that proof independently. The scans are mutation and discovery evidence only.
