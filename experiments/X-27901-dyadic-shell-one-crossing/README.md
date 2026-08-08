# X-27901 — Dyadic shell one-crossing replay

This standard-library package supports the proposed claims `L-27901`--`L-27903` and the full proposal `T-27901`.

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
- the derivative-left margins through cell 200,000;
- all-coordinate finite shell scans through `X=20,000`;
- prime-coordinate scans through `X=200,000`;
- the maximum weighted prime tail and its start.

The retained finite scans have one sign change and no positive weighted prime tail.

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

The package does not prove:

- the analytic all-cell inequalities in `L-27901`;
- cofinal finite shell-crossing rigidity `FSCR`;
- endpoint prime domination `EPD`;
- squarefree collector existence `ESC`;
- WSTS;
- RH.

A reviewer must check the written analytic proof and the cofinal production gates independently. Finite scans are not substitutes for those theorems.
