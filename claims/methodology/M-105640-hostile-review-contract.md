# M-105640 — Hostile review contract for strong log-concavity and the critical-depth collar

Claim ID: `M-105640`  
Created: 2026-08-25  
Applies to: `L-105640--L-105646`, `R-105640`, `T-105640`  
RH status: **unproved**

An independent reviewer should try to break the packet in the following order.

## A. Strong-log-concavity audit

1. Re-derive the theta summand formula and the exact score/curvature formulas
   in `L-105640`.
2. Check that every summand is positive for `u>=0`.
3. Verify

   ```text
   sum_(n>=2) phi_n/phi_1 < 1/200,
   p_1 > 200/201.
   ```

4. Reconstruct the retained score-variance bound

   ```text
   sum_(n>=2) (phi_n/phi_1)(a_n-a_1)^2
   < 4x * 1881/7000.
   ```

5. Check the exact rational ledger

   ```text
   (200/201)*12*(5119/7000)
   = 20476/2345
   = 8 + 1716/2345.
   ```

6. Confirm that even extension and smoothness justify the negative half-line
   and the origin.

Any failure in these rows invalidates the claimed uniform constant. The older
strict-log-concavity theorem may still survive independently.

## B. Current-profile envelope audit

1. Verify the conditional exterior-square law and the identity

   ```text
   j_H/(H Lambda_2)
   = E[sinh(2H X)/(2H X)].
   ```

2. Check the separate meanings of:

   ```text
   H = total analytic height;
   h = physical microscope coefficient;
   b = H-h = base height.
   ```

3. Confirm that the upper exponential cap uses only `sinh(z)/z>=1`.
4. Confirm that log-concavity is used for monotonicity in frequency.
5. Confirm that the profile decreases in total height because the numerator
   decreases and the hyperbolic moment denominator increases.

## C. Maxwell-sandwich audit

1. From `psi''>=kappa_0`, verify

   ```text
   d/dx log(q_s/g_kappa0) <= 0,
   g_kappa0 proportional to x^2 exp(-kappa_0 x^2).
   ```

2. Check the monotone-likelihood-ratio implication
   `q_s <=_st g_kappa0`.
3. Evaluate exactly

   ```text
   E_g[sinh(2H X)/(2H X)] = exp(H^2/kappa_0).
   ```

4. Re-derive the operator sandwich

   ```text
   exp(-H xi-H^2/kappa_0) <= R_H(xi) <= exp(-H xi).
   ```

5. Check the critical-height rational ledger

   ```text
   1-1/(4 kappa_0)=79559/81904>97/100.
   ```

The reviewer should pay special attention to the orientation of stochastic
domination; reversing it reverses the lower profile bound.

## D. Model-space trace normalization

1. Re-derive the Paley--Wiener reproducing kernel with the stated
   `1/sqrt(2 pi)` convention.
2. Verify the continuous resolution

   ```text
   integral |k_(x+iH/2)><k_(x+iH/2)| dx = M_(exp(-H xi)).
   ```

3. Check the factor `1/(2 pi H)` in the midline trace formula.
4. For one Blaschke factor, integrate the Poisson defect and recover exactly

   ```text
   2y/(H+2y).
   ```

5. Ensure every trace is taken only after finite/model-space compression. The
   continuum multiplication operator is not declared trace class.
6. Check that the Maxwell sandwich passes to finite model-space traces by
   positive operator order.

## E. Xi-prime collar orientation

1. Verify that a zero `rho=alpha+i gamma` of `Xi'` above height `H` becomes an
   upper zero `alpha+i(gamma-H)` of `Xi'(z+iH)`.
2. Check that this is the anti-inner denominator packet, with multiplicity and
   common-factor reduction retained.
3. Recompute the soft-depth and layer-cake inequalities.
4. Check the collar constant `4 delta/beta_1` under
   `H=beta_1-delta`, `delta<=beta_1/2`, `h<=H`.
5. Treat the cofinal `O(N(T))` comparison as a separately normalized
   zero-count input, not part of the finite identity.

## F. Height-owner audit

1. For one zero at height `gamma`, verify

   ```text
   Q_rho(H)=E_(Exp(2(gamma-H)))[R_H]
   ```

   and its endpoint values `Q_rho(0)=1`, `Q_rho(gamma-)=0`.
2. Check both ingredients of monotonicity:

   ```text
   R_H decreases with H;
   the exponential model vector shifts stochastically to higher frequencies.
   ```

3. Confirm that `-dQ_rho` is a probability measure.
4. Check the explicit reference survival

   ```text
   S_gamma(H)=2(gamma-H)/(2gamma-H)
   ```

   and density `2gamma/(2gamma-H)^2`.
5. Verify the uniform survival comparison

   ```text
   0 <= S_gamma-Q_rho < 3/100
   ```

   for `gamma<=1/2`.
6. Do not identify the sum of one-zero owner measures with the trace of a
   nonorthogonal multi-zero model space at each fixed height.

## G. Topology firewall

The reviewer must verify that the packet never uses

```text
weighted model-space charge -> unweighted degree.
```

The one-factor separator has degree one but charge `2y/(H+2y)->0`.
Consequently the packet may localize the unresolved geometry to a vanishing
collar and resolve each zero into a positive height-owner law, but it may not
remove the collar without a signed index, pointwise phase theorem, or
confluent endpoint argument.

## H. Status audit

The following must remain false in every result object and summary:

```text
HOWNXFER105644 proved;
BCOLLAR105643 proved;
POINTID105630 proved;
SAFEDESC105628 proved;
Riemann Hypothesis established.
```

The strong-log-concavity, Maxwell-domination and shifted-inner theorems should
receive independent analytic review before integration.