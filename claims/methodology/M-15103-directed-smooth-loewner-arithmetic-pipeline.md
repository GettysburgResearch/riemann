# M-15103 — Directed smooth-target, Loewner-inertia, and arithmetic-line pipeline

Claim ID: `M-15103`  
Status: **PROOF-PRODUCING METHODOLOGY; COFINAL THEOREM OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Depends on: `L-15117`--`L-15121`, `T-15105`, `X-15106`

## 1. Objective

At a sequence of supports and bands, prove the fixed arithmetic scalar
completion—not merely free special completion—using only source-bound directed
objects.

The proof-facing flow is

```text
actual smooth target coefficients
  -> canonical Loewner inertia and moat
  -> actual arithmetic Weil source
  -> scale-optimized source-line LP
  -> exact residue thresholds when necessary
  -> cofinal pass and Hurwitz.
```

## 2. Stage A — actual smooth coefficients

For `ell=log(lambda)` and `|n|<=N`, compute completed-`Xi` balls at

```text
omega_n = pi n/ell
```

and add the analytic cutoff-tail radius of `L-15117`.  Preserve both:

```text
p_n_interval
full_sample_interval
smooth_tail_radius
```

rather than replacing the first by the second.

Fail closed if any target interval contains zero after boundary normalization;
a different basis or smaller band is then required before using the formulas
with `1/p_i`.

## 3. Stage B — canonical inertia

Construct the canonical source directly:

```text
g_i = -sum_(j!=i) (1+p_j/p_i)/(lambda_i-lambda_j).
```

Use an ordinary midpoint only to nominate a rational center.  Certify the exact
matrix by:

1. exact symbolic target kernel;
2. entrywise directed radii;
3. exact center inertia;
4. a directed nonzero moat;
5. `L-15113` kernel-pinned inertia transfer.

Retain one of:

```text
CERTIFIED_CANONICAL_PSD_CORANK_ONE
CERTIFIED_CANONICAL_NONREAL_PAIR_COUNT
UNRESOLVED_CANONICAL_INERTIA.
```

Do not infer the arithmetic verdict from this output.

## 4. Stage C — arithmetic source

Evaluate `L-15119` in the exact same node convention:

```text
beta = polar source + archimedean source + complete prime-power source.
```

The producer must bind every prime-power segment and term count, independently
of the matrix diagonal.  Check odd parity and reconstruct selected off-diagonal
Weil entries from source differences.

## 5. Stage D — scale-optimized finite decision

First solve the exact rational LP of `L-15120`:

```text
minimize M over t>0,q,z_ij
z_ij >= +(t A_ij-Qcan_ij-q)
z_ij >= -(t A_ij-Qcan_ij-q)
M >= sum_(j!=i)(1+|p_j/p_i|) z_ij.
```

A rational feasible solution with

```text
M < m_can
```

proves the arithmetic scalar completion with

```text
a=1/t,
c=q/t.
```

Replay the resulting matrix independently with exact/directed complement
`LDL^T`.

If this sufficient moat test fails, do **not** retire the level.  Proceed to the
exact residue line:

```text
w_k(c)=-R_c(r_k)/P'(r_k)
```

or the equivalent root/source threshold interval of `L-15109`.  The line may
intersect the positive orthant far from the canonical ray.

## 6. Stage E — polynomial differential residual

Use `L-15121` to retain the analytic object

```text
R_(t,q,e)(s)
 = t R_0(s)-q(sP(s)+Omega(s))+P'(s)-eP(s).
```

This is the normalized source defect before division by small node values.  It
supports three proof strategies:

1. coefficient-space interval bounds;
2. nodewise canonical-ray LP bounds;
3. rootwise residue bounds
   ```text
   |R(r_k)| < |P'(r_k)|.
   ```

The third is often sharper than the row-sum relaxation.

## 7. Cofinal ledger

At every level retain:

```text
ell, N, cutoff profile
coefficient intervals and tail radius
canonical inertia, moat, and kernel hash
arithmetic source intervals and term manifest
LP optimum upper/lower bounds
chosen t,q and exact matrix replay
exact threshold interval if LP inconclusive
transform approximation bound
```

A proof needs either:

```text
limsup Theta_j < 1
```

for the canonical-ray statistic, or direct positive residue/threshold
certificates at every level of an unbounded diagonal.

## 8. Scheduling

Use a nested diagonal rather than fixing `N` first:

1. choose `ell`;
2. increase `N` until the smooth finite-projection tail clears its target;
3. stop before coefficient intervals or canonical node denominators become
   unresolved;
4. certify both canonical and arithmetic gates;
5. enlarge `ell` and repeat.

The super-Gaussian localization radius leaves a broad polynomial-band range;
the practical limiter is canonical conditioning, not the radical tail.

## 9. Fail-closed rules

- Never substitute full `Xi` samples for actual smooth coefficients.
- Never use a canonical real-root census as the arithmetic scalar verdict.
- Never use the unscaled `a=1` proximity ratio.
- Never omit higher prime powers.
- Never promote midpoint roots, eigenvalues, or LP objectives.
- Never infer a cofinal theorem from a finite trend.
- Keep the arbitrary-completion and fixed-arithmetic readings in separate
  fields and reports.

## 10. Current boundary

The finite consumer side is complete.  The unproved statement is the cofinal
arithmetic comparison between the explicit source `beta^Weil` and the canonical
Herglotz source—or, more generally, direct positivity of all arithmetic residue
weights.  This is the point at which genuine zeta arithmetic, rather than
approximation theory, must enter.