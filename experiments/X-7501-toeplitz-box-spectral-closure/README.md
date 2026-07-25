# X-7501 — Toeplitz-box spectral closure

X-7501 turns one complete directed coefficient pass into a reusable exact
matrix certificate rather than a one-vector result.

The input is:

- a rational interval for the scalar `alpha`;
- one ordered complex rectangle for every Hermitian Toeplitz lag;
- a nonnegative operator-norm bound for all remaining corrections;
- exact Gaussian-rational vectors or positive Gram weights.

The standard-library checker reconstructs all autocorrelations and contracts
shared coefficient uncertainty only after exact aggregation.

## Why this is offensive

A complete `c=10^11`, `K=1024` coefficient run costs one pass over
`4,118,082,969` prime powers. Once the 1,024 lag boxes exist, X-7501 permits
arbitrarily many cheap exact postselections:

- the midpoint leading vector;
- vectors from adjacent threshold cells;
- rationalized low-rank subspaces;
- positive Gram portfolios designed to cancel shared lag uncertainty.

No additional prime enumeration or phase reduction is required.

## Certificate kinds

### `fixed-vector`

For one exact Gaussian-rational vector, the checker reconstructs the complete
prime Rayleigh interval and adds scalar and correction uncertainty.

### `gram-portfolio`

For

```text
W = sum_l weight_l * v_l v_l^*
```

with positive rational weights, the checker aggregates the autocorrelations
before interval widening. A strict negative interval for `trace(W H)` proves the
matrix is non-PSD. It also proves at least one listed exact vector is negative
for the actual matrix, although the certificate need not identify which one.

### `whole-matrix-positive`

For small or moderate dimensions, exact Gaussian-rational `LDL^*` of a shifted
midpoint matrix plus the Toeplitz row-sum uncertainty radius can certify every
complex direction positive. Large dimensions may use a future structured
midpoint lower-bound certificate with the same perturbation transfer.

## Strict synthetic regression

The committed example has

```text
K=2
alpha=0
correction=0
c0=1/10
c1 in [-1,1]
```

and vectors

```text
v+ = (1, 1)
v- = (1,-1).
```

Each vector separately has interval

```text
[-6/5, 4/5]
```

and is unresolved. Their positive Gram portfolio has aggregate lag-one
autocorrelation zero, so the shared uncertainty cancels before widening and the
checker proves

```text
trace(W H) = -2/5.
```

This is a strict negative matrix certificate.

## Commands

```bash
python -m unittest discover \
  -s experiments/X-7501-toeplitz-box-spectral-closure/tests -v

python experiments/X-7501-toeplitz-box-spectral-closure/verify_toeplitz_box.py \
  experiments/X-7501-toeplitz-box-spectral-closure/certificates/\
synthetic-gram-cancellation.json
```

When target artifacts exist:

```bash
python experiments/X-7501-toeplitz-box-spectral-closure/from_target_artifacts.py \
  --boxes target-merged-lag-boxes.json \
  --final target-final-interval.json \
  --vector vector-a.json --weight 1 \
  --vector vector-b.json --weight 3/2 \
  --output target-gram-certificate.json

python experiments/X-7501-toeplitz-box-spectral-closure/verify_toeplitz_box.py \
  target-gram-certificate.json \
  --output target-gram-verification.json
```

## Trust boundary

Exact in the checker:

- rational parsing;
- Gaussian-rational autocorrelations;
- fixed-vector and Gram aggregation;
- rectangular interval contraction;
- correction operator-radius composition;
- small-matrix `LDL^*` and row-sum transfer;
- final strict sign.

Not proved by X-7501:

- complete prime-power coverage;
- huge-phase and hat-placement enclosures;
- correctness of the producing interval library;
- D-0801 admissibility;
- the Guinand--Weil normalization and RH implication;
- independent numerical reproduction.

The adapter preserves source metadata but does not treat a hash as arithmetic
verification.
