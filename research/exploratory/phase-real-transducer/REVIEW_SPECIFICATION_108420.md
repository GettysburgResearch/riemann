# Hostile review specification — continuation 108420

## Frozen object

Review the continuation based on parent

```text
16d9c586d2f7439187e756066410622fd51c6d56
```

and the files listed in `SHA256SUMS_108420`.

## Review order

### 1. PFR-T10 Hermite source theorem

Check:

- the two-point Hermite remainder sign in (1.10);
- elimination of all Hadamard regularization constants;
- normal convergence of the transformed zero series;
- removability at `z=+/-a`;
- that only safe `xi'/xi` data are used in the source definition.

A sign error or an unremoved polynomial term invalidates the theorem.

### 2. Symmetric spline and prime knots

Check:

- `(a^2-D^2)^m` versus the centered zero modes;
- the highest-derivative coefficient `(-1)^m`;
- the jump sign `(-1)^(m+1)Lambda(n)/sqrt(n)`;
- regularity through order `2m-2`;
- the partial-fraction coefficients in (1.18).

### 3. Positivity equivalence

Check:

- positivity of the weights under RH;
- Bochner and positive-real representations;
- the Pick-kernel algebra;
- the converse pole/sign-change argument;
- the pointwise, weighted-`L2`, and Hardy-space abscissae.

Audit exact overlap with Suzuki/Weil and issue #39 before any novelty statement.

### 4. PFR-T11 orientation and pole correction

Check the counterclockwise rectangle orientation and every sign in
(2.16)--(2.23), especially

```text
Re[2/(-1/2+it)] = -1/(t^2+1/4).
```

Check that `G=(s-1)^2 zeta'` is entire and that its rectangle zeros are exactly
the relevant `zeta'` zeros.

### 5. Screening and firewall

Check:

- `int(L-R)_+=pi*N_L-int min(L,R)`;
- the mirrored-pair exact cancellation;
- that no finite-model conclusion is promoted to actual zeta without the
  background and boundary adapter.

### 6. Combined petal ledger

Verify that the interval hypotheses of PFR-T6 and PFR-T11 are simultaneously
satisfied and that equation (2.28) has the correct inequality direction.

## Computation boundary

The verifier authenticates finite algebra and floating regressions only.
The actual-Xi safe-Hermite comparison uses a finite verified zero prefix and is
`NON_DIRECTED_HIGH_PRECISION`; it is not a proof of the analytic theorem or RH.
