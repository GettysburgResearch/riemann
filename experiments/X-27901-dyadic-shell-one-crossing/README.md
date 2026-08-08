# X-27901 — Dyadic shell and complete-endpoint replay

This standard-library package supports `L-27901`--`L-27906`, `T-27901`, and the preferred full proposal `T-27902`.

## Run

```bash
python3 verify.py
python3 verify_endpoint.py
```

## Dyadic shell replay

The retained result is

```text
results/verification.json
```

with digest

```text
cf3007f56fb5a85f008bcd99723b4c24c1323e8252601eaaa9e821d4649c402d
```

It reports:

- the unique continuum zero bracket;
- signs at `1/7`, `1/8`, and `1/9`;
- maxima of the six negative upper cells;
- derivative-left margins through cell 200,000;
- all-coordinate finite shell scans through `X=20,000`;
- prime-coordinate scans through `X=200,000`;
- the maximum weighted prime tail and its start.

Every retained finite shell has one sign change and no positive weighted prime tail.

## Endpoint reserve replay

The retained endpoint result is

```text
results/endpoint-verification.json
```

with digest

```text
075a26346e614ff9255c7e56ff6b0365513a972e2d4a7d046f9524b0b686f8fc
```

It checks:

- 44,847 direct-versus-closed endpoint-residual cells;
- exclusion of the zero terminal multiple through `floor((X-1)/q)`;
- the positive endpoint-cell recurrence through `N=100,000`;
- four exact rational Mellin kernel identities;
- the identity
  ```text
  ordinary endpoint scalar
   =complete endpoint scalar-proper-power reserve;
  ```
- positive proper-power reserves at selected endpoints;
- a deliberate positive complete scalar at `X=1398`, rejecting the false one-sign mutation.

The maximum floating mismatch in the finite residual identity is approximately `4.2e-14`.

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
- the cofinal logarithmic proper-power reserve in `L-27905`;
- the Mellin continuation and residue theorem in `L-27906`;
- Complete Endpoint Stability `CEP`;
- Endpoint Prime Domination `EPD`;
- WSTS;
- RH.

`FSCR` and the prime-power reserve are claims of the written analytic lemmas, not consequences of finite replay. The scripts are exact/formal checks and discovery mutations only.
