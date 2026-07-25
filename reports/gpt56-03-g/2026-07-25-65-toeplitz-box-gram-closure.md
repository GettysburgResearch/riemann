# Agent report — one-pass Toeplitz-box dual closure

Agent: `gpt56-03-g`  
Carrier handoff: Issues #55/#65 and draft PRs #61/#65/#73  
Branch: `agent/gpt56-03-g/65-whole-toeplitz-box`  
Date: 2026-07-25  
Status: theorem and exact checker complete; production lag boxes pending

## Objective

Make the complete directed carrier pass useful for discovering a counterexample,
not merely certifying the already recovered positive-looking vector.

The active producer is designed to traverse exactly `4,118,082,969`
prime-power terms and emit 1,024 simultaneous complex lag boxes. Earlier
postselection work showed that one midpoint vector may be chosen after the pass.
The missing dual layer was a proof object that could:

1. test many exact vectors without rerunning primes;
2. combine vectors before widening shared coefficient uncertainty;
3. certify a negative matrix even when every individual interval is unresolved;
4. optionally close a whole finite matrix positive.

## Main result — L-7501

For a directed Hermitian Toeplitz box, let

\[
 H=\alpha I-S+C,
 \qquad \|C\|_2\le\varepsilon.
\]

For an exact vector `z`, define

\[
 A_d(z)=\sum_jz_{j+d}\overline{z_j}.
\]

The prime contraction is

\[
 z^*Sz=c_0A_0(z)+\sum_{d\ge1}\operatorname{Re}(c_dA_d(z)).
\]

Every term is a rational interval contraction against one lag rectangle.

The new step is to permit a positive Gram portfolio

\[
 W=\sum_\ell\theta_\ell z_\ell z_\ell^*,
 \qquad\theta_\ell>0.
\]

Its exact aggregate autocorrelations are

\[
 A_d(W)=\sum_\ell\theta_\ell A_d(z_\ell).
\]

The checker contracts each shared lag box only once, after aggregation. If the
upper endpoint for

\[
 \operatorname{tr}(WH)
\]

is negative, then `H` is not positive semidefinite. Under the parent D-0801
interface, this is a finite counterexample matrix certificate.

## Why a portfolio can beat every member

The exact synthetic control has

```text
K=2
alpha=0
c0=1/10
c1 in [-1,1]
```

and vectors `v+=(1,1)`, `v-=(1,-1)`.

Separately, each interval is

```text
[-6/5, 4/5]
```

and touches zero. For

\[
 W=v_+v_+^*+v_-v_-^*=2I,
\]

the aggregate uncertain lag coefficient is exactly zero. The exact checker
proves

\[
 \operatorname{tr}(WH)=-\frac25.
\]

Thus shared-feature cancellation can make a finite negative certificate visible
although every separately widened vector is inconclusive.

This is especially relevant to the carrier route, where all candidate vectors
reuse the same huge-phase coefficient boxes.

## Postselection theorem

The expensive producer proves one universal inclusion statement for the lag
vector. Any exact vector, subspace, or positive Gram portfolio chosen later from
the box midpoints remains covered. Therefore the workflow is:

```text
one complete directed source pass
-> retain 1,024 lag boxes
-> arbitrary midpoint/subspace optimization
-> rational freeze
-> exact contraction
```

There is no selection bias because the primitive boxes are independent of the
later dual object.

## Optional whole-matrix closure

Let `S0` be the rational midpoint Toeplitz matrix. Coefficient rectangle radii
`rho_d` give

\[
 \|S-S_0\|_2
 \le\rho_0+\sum_{d=1}^{K-1}\rho_d.
\]

Adding scalar and correction uncertainty gives total radius `R`. If an exact
certificate proves

\[
 \alpha_0I-S_0-\delta I\succ0
\]

and `R<delta`, then every admitted full matrix is positive definite.

The committed checker implements exact Gaussian-rational `LDL^*` for small and
moderate controls. The theorem deliberately allows a future structured
large-`K` midpoint lower-bound certificate instead of insisting on dense exact
`1024 x 1024` elimination.

## Experiment X-7501

The standard-library checker supports:

- `fixed-vector`;
- `gram-portfolio`;
- `whole-matrix-positive`.

It rejects:

- negative or zero Gram weights;
- zero or wrong-dimensional vectors;
- missing, duplicated, or reordered lags;
- a nonreal lag-zero box;
- duplicate check IDs;
- reversed intervals;
- zero-touching conclusions.

An adapter reads the existing target schemas:

```text
riemann.toeplitz-coefficient-box.v1
riemann.piecewise-carrier-final-interval.v1
riemann.piecewise-carrier-vector.v1
```

and emits one X-7501 certificate containing all supplied vectors plus their
positive portfolio.

## Verification

Local commands:

```bash
python -m unittest -v \
  experiments/X-7501-toeplitz-box-spectral-closure/tests/\
test_verify_toeplitz_box.py

python -m compileall -q \
  experiments/X-7501-toeplitz-box-spectral-closure/verify_toeplitz_box.py \
  experiments/X-7501-toeplitz-box-spectral-closure/from_target_artifacts.py \
  experiments/X-7501-toeplitz-box-spectral-closure/tests
```

Five exact tests pass:

1. complex autocorrelation contraction agrees with a direct dense form;
2. the strict Gram-cancellation regression succeeds;
3. a small whole-matrix positive certificate succeeds;
4. a negative Gram weight is rejected;
5. duplicate check IDs are rejected.

The committed synthetic certificate and verification output contain exact
fractions only.

## Relationship to the full objective

A negative X-7501 portfolio is more than an optimization score. It proves the
finite carrier matrix is non-PSD for every realization admitted by all complete
lag boxes and the correction radius. Since the portfolio is a positive sum of
exact rank-one directions, at least one listed finite test function is negative
for the actual matrix.

The remaining route gates are explicit:

1. produce the complete directed lag boxes;
2. find a negative vector or portfolio with strict moat;
3. independently reproduce the coefficient boxes;
4. close D-0801 admissibility;
5. close the Guinand--Weil normalization and implication.

No counterexample is claimed by this PR because the production coefficient
artifact does not yet exist.

## Strategic consequence

The `c=10^11` recovered vector has an ordinary positive leading margin near
`2.69e-4`; certifying only that vector is likely a positive exclusion. X-7501
preserves the expensive computation for a broader offense:

- postselect the true midpoint eigenspace;
- import vectors from first-deposition threshold cells;
- optimize rational low-rank PSD portfolios for shared uncertainty cancellation;
- test all of them without another prime pass.

If the target matrix remains positive, the same lag boxes become a reusable
calibration artifact for searching nearby carriers and threshold cells with a
trusted directed backend.

## Files added

- `claims/lemmas/L-7501-toeplitz-box-gram-spectral-closure.md`;
- `experiments/X-7501-toeplitz-box-spectral-closure/verify_toeplitz_box.py`;
- `from_target_artifacts.py`;
- exact tests, synthetic certificate, verification result, README, and this
  report.

## Proof boundary

- Matrix algebra and checker: exact rational arithmetic.
- Synthetic result: exact.
- No production prime coefficient is evaluated here.
- Source completeness and interval arithmetic remain producer responsibilities.
- D-0801 and Guinand--Weil dependencies retain current statuses.
