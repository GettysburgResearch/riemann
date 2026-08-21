# Fixed-ratio cluster-elimination addendum — 2026-08-07

Status: `PROPOSED COMPLETE LOCAL-TO-BAND THEOREM / RH UNPROVED`  
PR: #248  
Issue: #245

`L-24513` globalizes the exact cluster algebra of `L-24511`.

For every fixed integer `R>=2`, there are constants `X_R,C_R` such that, for all `X>=X_R`, a constructive nonnegative adjacent flow supported only at prime powers

```text
X/R <= q <= X
```

makes every prime-power constraint in that band feasible and costs at most

```text
C_R X^(-3/2)
```

in the exact objective metric.

The proof uses:

1. the explicit parabolic seed derivative to bound every initial band residual by `K_R/sqrt(X)`;
2. the uniformly bounded inverse-positive consecutive-prime-power cluster matrices;
3. the fact that every positive child outside one cluster is below `2q/3` once the band lies above `5`;
4. a fixed depth `O(log R)` descendant tree;
5. the `q^-2` adjacent-flow objective weight throughout the fixed-ratio band.

No PNT, zero estimate, numerical solver, or RH hypothesis enters.

The theorem proves that the unresolved correction cannot reside in any fixed-ratio carry band. It must persist in a moving core

```text
q/X -> 0.
```

This does not contradict the exact fixed-ratio Mertens/Farey firewall. That firewall is a scalar projection of a complete signed arithmetic packet; `L-24513` concerns the local carry correction geometry and may transfer defect to lower ratios. A uniform theorem permitting `R=R(X)` at the full logarithmic scale remains open.
