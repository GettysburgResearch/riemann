# X-8301 — Exact endpoint Green threshold certificates

Status: exact finite synthetic regression; production Toeplitz adapter pending  
Agent: `gpt56-05-i`  
Issue: #83  
Claims: L-8301, L-8302, T-8301

## Purpose

The prior threshold-directed carrier work ranks a newly admitted prime power by
its overlap with one frozen vector.  That score can be zero even when the
rank-two corner event rotates the matrix into a different negative direction.

X-8301 verifies the stronger whole-matrix reduction.  For a positive Hermitian
background `H`, endpoint phase `zeta`, and corner event

```text
C = zeta e_0 e_{K-1}^* + conj(zeta) e_{K-1} e_0^*,
```

only the endpoint Green matrix

```text
G = [e_0,e_{K-1}]^* H^-1 [e_0,e_{K-1}]
```

is required.  The exact secular polynomial is

```text
1 - 2*r*tau - D*tau^2,
r = Re(conj(zeta)*G_01),
D = G_00*G_11 - |G_01|^2.
```

The positive generalized pressure is

```text
lambda_plus = r + sqrt(r^2 + D).
```

A smooth background of operator radius `beta` is absorbed through the spectral
floor `mu`:

```text
mu*(1 - tau*lambda_plus) > beta  => robust positive;
mu*(tau*lambda_plus - 1) > beta  => robust crossing.
```

## Breakthrough regression

The committed `3 x 3` example uses

```text
H = diag(1/10, 1/100, 1/10).
```

Its smallest-eigenvalue vector is the middle coordinate, so its endpoint
susceptibility is exactly zero.  Nevertheless the endpoint Green matrix is
`diag(10,10)`, giving `lambda_plus=10`.

With

```text
tau  = 3/25
mu   = 1/100
beta = 1/1000
```

T-8301 proves a robust crossing with exact moat `1/1000`.  The determinant ratio
is `-11/25`.  Thus frozen-vector ranking can provably miss a whole-matrix first-cell
crossing.

At `tau=2/25`, the same data instead give a robust positive moat `1/1000`.
The equality case `tau=1/10` is rejected as unresolved.

A second control uses an exact complex phase `(3+4i)/5` and a correlated
endpoint Green matrix.  It reconstructs

```text
r           = 1/2
D           = 15/4
lambda_plus = 5/2
determinant ratio at tau=1/2 = -7/16.
```

## Files

- `verify.py` — integer/Fraction Gaussian-rational checker;
- `certificates/synthetic-green-cases.json` — crossing, exclusion, complex, and equality controls;
- `tests/test_verify.py` — adversarial tests;
- `results/synthetic-verification.json` — exact replay output;
- `results/tests.txt` — executed test log.

## Reproduction

```bash
python verify.py certificates/synthetic-green-cases.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Nine tests pass.

## Exact checker responsibilities

The checker:

1. parses exact Gaussian-rational Hermitian matrices;
2. proves positive definiteness by exact `LDL*`;
3. proves the claimed spectral floor by exact semidefinite `LDL*`;
4. reconstructs the exact inverse and endpoint Green matrix for the small controls;
5. checks the determinant ratio independently;
6. encloses irrational square roots by dyadic rationals;
7. applies the robust positive/crossing moat;
8. rejects nonunit phases, duplicate IDs, invalid floors, altered verdicts, and zero-touching boundaries.

The production path will not invert a `1024 x 1024` interval matrix.  L-8302
uses two approximate endpoint solves plus residual norms and a positive floor.

## Production adapter

Given PR #79-style complete lag boxes:

1. choose a rational Hermitian midpoint `H_0`;
2. prove an operator radius `delta` for the exact box;
3. certify `H_0 >= m I` with `m>delta`, hence `mu=m-delta`;
4. solve `H_0 y_0=e_0` and `H_0 y_1=e_{K-1}` at high precision;
5. use exact residuals plus `delta ||y_j||` to enclose `G`;
6. rank each threshold by an interval for
   `tau_max*(r+sqrt(r^2+D))`;
7. combine it with the first-cell smooth-background radius;
8. run a full directed cell calculation only if the robust pressure interval meets zero.

## Proof boundary

All committed outputs concern finite synthetic Hermitian matrices.  No
production D-0801 matrix, prime-power threshold, or RH counterexample is
certified.  Any eventual negative matrix still depends on independent
admissibility and Guinand--Weil normalization review.
