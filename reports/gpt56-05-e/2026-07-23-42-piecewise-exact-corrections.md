# Session report — gpt56-05-e — Issue #42 independent continuation

Date: 2026-07-23  
Agent: `gpt56-05-e`  
Branch: `agent/gpt56-05-e/42-piecewise-exact-corrections`  
Stacked base: draft PR #44  
Status: proposed exact formulas and rigorous correction envelope; no counterexample

## Objective

Determine whether the exact archimedean and pole blocks omitted by the PR #44 high-carrier leading matrix could plausibly erase or reverse its unusually small positive complete-prime margin.

The strongest reported cell was

```text
c = 10^11
K = 1024
T = 4709203636353.65
leading margin = +0.00026896626427230785
```

The prime stream was complete but the matrix arithmetic and phases were not interval certified.

## Main result 1: exact archimedean Toeplitz matrix

For cell width `h=Delta/K`, put

\[
 b=4\pi h=2L/K,
 \qquad
 \omega=T/2,
 \qquad
 k(t)=e^{-t/4}/(1-e^{-t}).
\]

The normalized D-0801 archimedean block is Hermitian Toeplitz. Its diagonal is

\[
 \frac1{2\pi}\left[
 \int_0^b\left\{
 \frac{e^{-t}}t-k(t)(1-t/b)\cos(\omega t)
 \right\}dt+E_1(b)-\log\pi
 \right],
\]

and the upper `d`-th diagonal is half of

\[
 z_d=-\frac1{2\pi}\int_0^{2L}
 k(t)e^{-i\omega t}\tau_d(t/b)\,dt.
\]

The proof uses the same cell-overlap hats as the exact prime Toeplitz reduction in L-0801. This eliminates the missing dense-matrix uncertainty: the nonconstant archimedean term has one compact coefficient per lag.

## Main result 2: explicit uniform O(1/T) bound

The diagonal separates as

\[
 \alpha_0=\frac1{2\pi}\log(T/(2\pi))
 +\frac1{2\pi}\left[
 -Ci(Tb/2)+\int_0^bq_b(t)\cos(Tt/2)dt
 \right].
\]

For `b<=1/20`, a derivative analysis proves that `q_b` is increasing from

\[
 1/b-1/4
\]

to

\[
 1/b,
\]

so its variation is exactly `1/4`.

The off-diagonal hats are compact bounded-variation functions. Retaining the nonzero `d=1` endpoint gives

\[
 |z_1|\le2k(b)/(\pi T),
\]

and

\[
 |z_d|\le2k((d-1)b)/(\pi T),\qquad d>=2.
\]

Summing the Toeplitz row envelope yields

\[
 \left\|A_K-\frac{\log(T/(2\pi))}{2\pi}I\right\|_2
 \le\frac1{\pi T}\left[
 \frac{5+2H_{K-2}}b+2(K-1)+\frac14
 \right].
\]

This bound is vector-independent and therefore controls every eigenvalue.

## Main result 3: pole block is rank at most two

Let `beta(z)` be the vector of cell transforms. The normalized pole matrix is

\[
 R_K=\frac1h\left[
 \beta(T-i/2)\beta(-T+i/2)^T
 +\beta(T+i/2)\beta(-T-i/2)^T
 \right].
\]

The summands are adjoints, so the matrix is Hermitian and rank at most two. Its norm satisfies

\[
 \|R_K\|_2\le
 \frac{2\sinh(\pi\Delta)\cosh^2(\pi h/2)}
 {\pi^2h\sinh(\pi h)(T^2+1/4)}.
\]

A fixed-vector producer needs only two directed complex dot products.

## Exact rational parameter certificate

X-4201 uses no numerical special functions. It proves

\[
 22<11\log10<638/25
\]

from elementary exponential bounds. Hence

\[
 b<319/6400<1/20.
\]

It reconstructs the exact harmonic number and substitutes only `L>22` and `pi>3` into the archimedean theorem. For the pole it uses deliberately coarse rational hyperbolic bounds.

The exact reconstructed upper sizes are

```text
archimedean  1.7781072071831001710e-10
pole          1.6672791396873303641e-16
combined      1.7781088744622398584e-10
```

The committed certificate claims the looser bound

```text
combined < 2.5e-10
```

and verifies it with Python integers and `fractions.Fraction`.

## Interpretation of the PR #44 margin

The reported margin string is greater than `1/4000=2.5e-4`. The rigorous correction threshold `1/(4e9)` is exactly one million times smaller. The exact reconstructed correction bound is approximately 1.5126535 million times smaller than the displayed margin.

This does **not** prove positivity. The reported margin is ordinary floating output and has no directed lower endpoint. The valid conclusion is narrower and strategically important:

> At this parameter cell, omitted archimedean and pole magnitude is no longer the plausible crossing mechanism. Directed prime-phase accumulation and normalization are the decisive blockers.

## Validation

```bash
python verify.py certificates/c11-k1024.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Eight exact tests pass. They cover the small-cell proof, the finite exponential control, threshold mutations, empirical-label preservation, parameter mutation, scale-factor mutation, and harmonic arithmetic.

The analytic formulas were additionally reconstructed independently from the D-0801 overlap identity and checked algebraically against the L-0702 compact archimedean normalization.

## Proof boundary

Rigorous, conditional on named proposed dependencies:

- exact archimedean Toeplitz formula;
- exact rank-two pole formula;
- uniform correction bounds;
- rational parameter and threshold certificate.

Not rigorous in this contribution:

- the PR #44 prime coefficient values;
- huge-phase range reduction;
- accumulation and eigensolve;
- D-0801 admissibility;
- the external Guinand--Weil normalization;
- the displayed leading margin as a mathematical interval.

No counterexample or `Z-####` candidate is allocated.

## Highest-priority review targets

1. Check the archimedean phase `exp(-i*T*t/2)` and upper-diagonal factor `1/2`.
2. Reconstruct the diagonal `E1(b)` tail compression.
3. Audit the cosine-integral identity and all factors of two.
4. Verify the proof that `q_b` has variation `1/4` on `b<=1/20`.
5. Check the nonzero `d=1` endpoint in the bounded-variation estimate.
6. Reconstruct the pole transpose/adjoint relation and normalization by `h`.
7. Independently rerun the exact rational certificate.
8. Preserve the empirical-only status of the PR #44 margin.

## Suggested next attack

Freeze the PR #44 leading vector to dyadic coefficients. Replay the complete prime manifest with directed balls for every logarithm, huge phase, trigonometric reduction, hat deposit, and sum. Compare the resulting one-dimensional Rayleigh interval with the `2.5e-10` correction gate. This avoids a certified eigensolver and directly tests the lowest reported basin.
