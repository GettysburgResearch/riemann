# X-91686 — Native-root compiler, exact separator, and score-free repair replay

This experiment replays the exact/directed claims deposited with `T-91659`.

## Verdict

```text
EXACT_NATIVE_ROOT_COMPILATION_DISCREPANCY_AND_SEPARATOR
PASS_NATIVE_ROOT_CAPACITY_THEOREM = false
Riemann Hypothesis = unproved
```

## Commands

```bash
cd experiments/X-91686-native-root-compiler-separator
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

A successful run prints

```text
EXACT_NATIVE_ROOT_COMPILATION_DISCREPANCY_AND_SEPARATOR
PASS_EXACT_RAW_LEAF_NATIVE_CAPACITY_SEPARATOR
PASS_FINITE_CONTINUUM_REALIZATION_DEFECT
PASS_LORENZ_CUTOFF_IS_EXACT_SIMULTANEOUS_LP_BASIS
PASS_HOSTILE_LEAF_TARGET_LORENZ_OPTIMAL_ROW
PASS_Y4_ZERO_SCORE_FREE_TRIANGULAR_REPAIR
```

## What is checked

### 1. Exact raw-leaf native-capacity separator

At `(X,p,q)=(136,67,2)` the replay verifies the rough sets

```text
R_67 intersect [1,68] = {1,67};
R_67 intersect [1,17] = {1}.
```

It then certifies

```text
raw current ordinary response = w_136(2);
raw current detail response   = Omega_136(2);
terminal child adds           delta=log(68/67)/sqrt(134)>1/810;
Y4(2)*delta                   >1/1215.
```

It also checks the asymptotic family at `p=71`. The analytic proof in `R-91686` extends this to every prime `p>=71` with

```text
X=2(p+1), y=2(p+1)/p, q=2,
raw-current overdraw > 5/834.
```

### 2. Exact finite/continuum realization discrepancy

The checker encloses

\[
4\sqrt2-4\sqrt3+
\frac{5\sqrt2}{2}\log(3/2)
\]

strictly above `1/10`.

### 3. Exact LP-basis theorem control

A rational box-LP fixture verifies the threshold duals for:

```text
leftmost target fill = score minimum;
leftmost target fill = row maximum;
a deliberate row demand above the dual optimum is rejected by gap 1/7.
```

The general theorem is proved symbolically in `L-91686`; the fixture is a regression control.

### 4. Directed hostile-leaf reconstruction

Using exact `Fraction` arithmetic and outward rational intervals for square roots and logarithms, the checker reconstructs

```text
p=67, y=13, row=66;
target cutoff=123;
cutoff fraction=0.283843792756777528...;
optimal row margin>0.0083815482754633380.
```

This checks one historically hostile activation cell, not the full remaining cell family.

### 5. `Y_4`-zero triangular repair

For `q<=5000`, the checker verifies the radix-four recurrence, the exact zero-weight characterization, and the first 200 triangular repair columns. It confirms

\[
h_q^{(q)}=\frac{q+1}{q-1},
\qquad
h_{q-1}^{(q)}=-\frac{q(q-3)}{(q-1)(q-2)}.
\]

## Arithmetic model

All sign decisions use exact rational arithmetic plus outward rational enclosures. Decimal values in `results/verification.json` are display-only. The script has no third-party dependencies.

## Scope boundary

The replay does **not** certify:

```text
the full PR #464 endpoint producer;
all stopped-leaf activation cells;
a source-owned thinning row;
ports or finite correction ownership;
SONTR;
NRCT;
CFFP;
Riemann Hypothesis.
```
