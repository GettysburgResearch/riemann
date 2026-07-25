# Integration patch — `gpt56-03-h` whole-matrix closure program

This file is an integrator-ready summary. It does not edit concurrent global
registries directly.

## Proposed claim registrations

| ID | Kind | Title | Status | Primary dependency |
|---|---|---|---|---|
| `O-8501` | observation | Complete `c=10^11` recovered fixed-vector replay is strictly positive | `PROPOSED certified computation` | X-2805 / X-2801 |
| `L-8501` | lemma | Circulant completion converts a Toeplitz upper bound to finite DFT inequalities | `PROPOSED` | finite interlacing and Fourier diagonalization |
| `L-8502` | lemma | One exact direction plus coarse complement/residual/operator gates closes a Hermitian matrix | `PROPOSED` | finite Schur complement |
| `L-8503` | lemma | Termwise coefficient errors give a dimension-free Toeplitz operator moat | `PROPOSED` | L-0801 coefficient convention |
| `L-8504` | lemma | Rational congruence certificate proves the orthogonal-complement gap | `PROPOSED` | finite Hermitian congruence |
| `L-8505` | lemma | Late fast coefficient source has static operator budget below `1/17,000,000` | `PROPOSED` | L-2813--L-2818; L-8503 |
| `O-8502` | observation | Recovered vector is first-cell threshold-insusceptible above `10^11` | `PROPOSED` | L-4204; O-8501 |

## Proposed experiment registrations

| ID | Path | Classification |
|---|---|---|
| `X-8201` | `experiments/X-8201-circulant-completion/` | empirical completion reconnaissance; no retained result yet |
| `X-8502` | `experiments/X-8502-one-direction-schur/` | exact conditional target-gate checker |
| `X-8503` | `experiments/X-8503-fast-toeplitz-operator/` | static exact budget, prototype producer, binder, and hybrid source merger |
| `X-8504` | `experiments/X-8504-threshold-insusceptibility/` | exact replay of endpoint susceptibility and fixed-vector moat |

## Dependency edges

```text
X-2805 final positive verdict
        -> O-8501
        -> L-8502 directional gate
        -> O-8502

L-0801 coefficient convention
        -> L-8503
        -> L-8505
        -> X-8503 operator source
        -> L-8502 operator gate

X-8503 exact reference matrix
        -> L-8504 complement + residual gates
        -> L-8502 whole-matrix conclusion

X-8503 exact reference matrix
        -> L-7501 arbitrary vectors / Gram portfolios
        -> L-8501 circulant completion
```

## Exact target gates

The complete recovered direction proves

```text
normalized exact lower > 1/4000.
```

L-8502 reduces whole-matrix positivity to:

```text
reference complement lower  > 7/1000
normalized residual         < 1/5000
exact/reference distance    < 1/1000.
```

The exact coarse Schur surplus is

```text
3 / 50,000,000.
```

The source plan reserves:

```text
prime coefficient operator radius < 999/1,000,000
```

so alpha and nonprime radii may still fit under the `1/1000` total gate.

L-8505 supplies the late-source static component

```text
B_fast,op < 1/17,000,000.
```

## Machine-readable fingerprints

```text
vector SHA-256
3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297

parameter SHA-256
ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34

normalization SHA-256
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be

X-8502 Schur target verification SHA-256
4e217fd02072600f99c1c5d002b95a0e475b18a0d5a684116b2f3d00e9ecd319

X-8503 static operator-budget verification SHA-256
9a2c928b5a56440a212402d78cd95510b13b17116fdcf26b9a82a4a501ea9780

X-8504 threshold-insusceptibility verification SHA-256
df56a0ee9dedab633bc6ad9537aa2d1c0c69fe4554980713cbce6b6361955aa5
```

## Review order

1. `claims/lemmas/L-8502-one-direction-schur-repair.md`
2. `claims/lemmas/L-8503-termwise-toeplitz-operator-moat.md`
3. `claims/lemmas/L-8505-fast-coefficient-operator-budget.md`
4. `experiments/X-8503-fast-toeplitz-operator/verify_operator_budget.py`
5. `experiments/X-8503-fast-toeplitz-operator/fast_toeplitz_shard.cpp`
6. `experiments/X-8503-fast-toeplitz-operator/bind_fast_shard.py`
7. `experiments/X-8503-fast-toeplitz-operator/merge_hybrid_source_strict.py`
8. `claims/lemmas/L-8504-rational-congruence-complement-certificate.md`
9. `experiments/X-8502-one-direction-schur/verify_target_gate.py`
10. `claims/observations/O-8501-complete-c1e11-fixed-vector-positive.md`
11. `claims/observations/O-8502-historical-vector-threshold-insusceptibility.md`
12. `claims/lemmas/L-8501-circulant-completion-toeplitz-bound.md`
13. append-only session report.

## Promotion boundary

- No counterexample or `Z-####` identifier is created.
- O-8501 excludes one vector only.
- The whole-matrix theorem remains conditional until all three new gates are
  supplied from one exact reference matrix.
- The static fast budget is not a completed source run.
- D-0801 admissibility and Guinand--Weil normalization retain their existing
  statuses.
- A future strict negative matrix or portfolio still requires independent
  coefficient reproduction before RH-disproof promotion.
