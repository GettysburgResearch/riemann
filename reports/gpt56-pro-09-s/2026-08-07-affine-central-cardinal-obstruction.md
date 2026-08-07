# Final audit of the affine hybrid completion attempt

Agent: `gpt56-pro-09-s`  
Date: 2026-08-07  
PR: #202  
Launch head: `d8511ae3105c4b20524732455e4e55009091520c`  
Classification: **AFFINE ASSEMBLY AUDITED; FINAL GATE IS RH-BEARING; RH NOT PROVED**

## Executive result

The pass attempted to prove the sole remaining theorem in `T-19813`:

```text
A_j-sigma_j I >= c_j D_j,
c_j>0,
A_j(p_j)-sigma_j <= C_j^tar c_j m_j,
C_j^tar m_j -> 0.
```

The high-frequency mechanisms remain useful, but the complete theorem cannot be
obtained from them.  A hypothetical fixed off-line zero produces a Hardy/form-
stable Xi-cardinal direction with a fixed negative Weil value.  That direction
lies in the exact target complement, where the hybrid residual form has floor
one.  Any affine shift low enough to satisfy the complement inequality makes the
Xi target pay a fixed positive excess, whereas its residual energy tends to
zero.  This gives an exact contradiction.

Thus:

```text
complete affine gate => RH directly;
high-ordinate support averaging does not prove the central block;
T-19813 remains a conditional implication, not a completed proof.
```

The proof is `R-19846/T-19814`.

## What survives

The following parts of the final hybrid stack remain mathematically useful.

1. `L-19861`: exact shifted one-sided ground-state theorem.
2. `L-19862`: one exact Xi target plus exterior arithmetic cardinals gives one
   onto reservoir, exponentially small target residual, and a constant second
   residual eigenvalue.
3. `L-19863`: the `k>R` range is handled collectively in the Bessel endpoint
   layer rather than by invalid pointwise stationary phase.
4. `L-19864`: logarithmic periodization folds are distinct from arithmetic
   Poisson aliases and have their own geometric estimate.
5. `L-19865`: the operator algebra converting certified profile LMIs into an
   affine shift is correct.
6. `L-19849/L-16213`: the target is the exact Xi source and admits the required
   moving-Hardy approximation.

None of these items supplies the missing central off-line exclusion.

## Why the central block is decisive

Let `omega` be a hypothetical nonreal centered zero.  The exact cardinal
combination

```text
h_omega=k_omega-k_conjugate(omega)
```

has Weil value `-2m_omega`.  Subtracting any multiple of the Xi radical does not
change that value, so the witness can be made ordinarily orthogonal to the Xi
target.  Cofinal finite approximation produces unit complement vectors with a
fixed negative matrix value.

The hybrid residual metric charges every such complement vector by at least one.
Therefore

```text
A-sigma I >= cD
```

forces the shift below the negative witness by at least `c`.  The target, whose
actual Weil value tends to zero, then has excess at least `c+kappa`.  This is
incompatible with an upper bound of size `c*m`, because `m->0`.

This argument is independent of condition numbers, endpoint asymptotics, and
finite source realization.

## Ground-state escape hatches checked

### Interior eigenstate instead of ground state

The finite CCM real-zero interface used by the branch is ground-state specific.
Replacing the target by an arbitrary isolated interior eigenstate does not give
the imported real-zero conclusion.

### Scalar shift

A scalar shift preserves eigenvectors, but it cannot reorder the Xi target above
a negative cardinal direction.  The contradiction in `R-19846` quantifies this.

### Positive line-zero deflation

Certified critical-line evaluation forms may be deflated positively, but every
off-line cardinal difference vanishes at those real zeros.  The indefinite
cardinal block survives.

### High-frequency support averaging

A fixed off-line cardinal direction has no support-scale oscillatory phase to
average.  It belongs to the bounded/central ordinate block and must be excluded
by genuinely strip-sensitive arithmetic.

### Brownian and terminal-packet imports

The Brownian variance defect (`T-21703`) and the balanced Type-II packet theorem
(`L-23207`) are alternative coordinates for the same obstruction.  Their final
SAT/BTP statements remain open and cannot be imported as proved lemmas.

## Revised status of PR #202's final proposal

```text
T-19813 logical implication                 VERIFIED CONDITIONALLY
R-19846/T-19814 cardinal obstruction        PROVED
source-specific complete affine gate         OPEN / RH-BEARING
completed proof of RH                        NO
```

The proper next research target is not another normalization audit.  It is one
new strip-sensitive theorem that directly kills the off-line cardinal block,
for example:

1. a source-specific signed Type-II/prime-energy contraction;
2. a Brownian martingale/variance saturation theorem;
3. a positive theta/Volterra factorization of the original Xi kernel;
4. a prime-side proof of the full affine gate including the central block.

Each would be a genuine proof of RH, not a technical adapter.

## Publication boundary

This report does not withdraw the exact hybrid algebra.  It withdraws the claim
that the remaining profile theorem is likely to follow by merely binding the
existing high-frequency estimates.  The central cardinal theorem must be part
of any honest future completion.
