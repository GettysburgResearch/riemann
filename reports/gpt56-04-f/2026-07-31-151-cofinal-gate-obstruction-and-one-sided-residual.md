# Cofinal arithmetic completion: exact obstruction and one-sided residual correction

Agent: `gpt56-04-f`  
Date: 2026-07-31  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Status: **no RH proof; exact scope theorem and sharper finite/cofinal interface**

## Requested statement

The requested assertion was

\[
 \exists\text{ an unbounded smooth-window sequence with }
 \mu_j^*=\sup_c\min_k w_{j,k}(c)>0
\]

at every retained level, equivalently cofinal strict relative LMIs for the
complete arithmetic Weil source.

## Audit result

That assertion has not been proved.  More importantly, it is not a routine
estimate left after the finite algebra.

For any actual smooth finite transforms `F_j -> Xi` locally uniformly in the
open centered critical strip, a single off-line zero of `Xi` forces a nonreal
zero of every sufficiently large `F_j` by Rouché.  A positive arithmetic
special completion would force all zeros of `F_j` real.  Therefore false RH
forces every sufficiently large arithmetic scalar line to fail.

This is recorded as `R-15105`.

The residue quantity `mu_j^*` is root-explicit and presupposes a simple real
finite target polynomial.  Cofinal positivity of those finite targets already
feeds Hurwitz directly.  The genuinely noncircular route must prove the fixed
arithmetic matrix positive without first certifying all finite target roots.

## New finite correction

`L-15126` replaces the absolute complete-residual estimate

```text
|x^T R x| <= omega_abs x^T M x
```

by the exact one-sided floor

```text
x^T R x >= -omega_minus x^T M x.
```

Only the negative part matters.  Positive unselected critical-line mass should
not be charged.  If

```text
Q_Z >= g M                 on p^perp,
|(Q_Z p)_i| <= rho |p_i| M_ii,
R_p(c) >= -omega_minus M   on p^perp,
rho+omega_minus < g,
```

then the full arithmetic target-pinned matrix is PSD with kernel `Rp`.

The optimal residual radius is

\[
 \omega_-^*(c)
 =\max\{0,-\lambda_{\min}(M^{-1/2}R_p(c)M^{-1/2}|_{p^\perp})\}.
\]

This can be certified by one directed complement LMI.  No upper bound on the
positive residual spectrum is needed.

## Exact off-line mechanism

PR #179 identifies an off-line cardinal pair with exact Weil block

\[
 m\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

and negative difference value `-2m`.  That difference vanishes at every real
zeta zero, so every selected critical-line frame is blind to it.  The complete
prime-side residual must carry the negative direction.

Thus any successful cofinal one-sided residual estimate already excludes every
off-line cardinal block.  This is the same RH-bearing arithmetic content that
PR #177 isolates as the centered terminal-prime matrix.

## Correct production target

The next proof-grade computation should not report an absolute residual norm.
For each actual smooth level it should emit:

1. directed smooth target coefficients;
2. a selected critical-line Cauchy frame and its target-pinned floor `s_Z`;
3. the complete residual source after selected-zero subtraction;
4. a rational scalar `c`;
5. the directed smallest generalized eigenvalue of the residual on `p^perp`;
6. the strict comparison
   
   ```text
   omega_minus < s_Z.
   ```

If this succeeds on a finite level, the finite arithmetic completion is proved.
A finite ladder is still evidence only.  Cofinal success is the RH-bearing
statement itself.

## Literature boundary

The newest coefficient-total-positivity result proves a uniform cubic tail
wedge but explicitly leaves the RH-critical central region open.  The newest
truncated-Weil computations likewise report striking finite convergence while
stating that rigorous convergence/positivity remains open.  Neither supplies
the signed cofinal residual floor required here.

## Conclusion

The exact current frontier is

\[
 \boxed{
 \text{prove a cofinal lower bound for the complete signed residual}
 }
\]

rather than a two-sided norm bound or a canonical root census.  No unconditional
proof of that lower bound, and hence no proof of the requested sequence or RH,
was obtained in this pass.
