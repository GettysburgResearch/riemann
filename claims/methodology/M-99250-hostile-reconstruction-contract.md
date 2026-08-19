# M-99250 — Hostile reconstruction contract for the scalar SHARP route

Claim ID: `M-99250`  
Status: **METHODOLOGY / FAIL-CLOSED REVIEW ORDER**  
Created: 2026-08-19

Review `T-99250` in the following order.

1. Re-derive the PR #642 kernel integral and the proof `kappa_j(t)>0`.
2. Differentiate `T(Y/t)/T(Y)` and verify the normalized-profile derivative in
   `L-99250`.
3. Check the Radon–Nikodym identity `M_Z=R_(Z|Y)M_Y`; reject any replacement by
   a raw support cutoff.
4. Replay the compact Hall base and the wrong-target state `t=13`, `x=67`.
5. Reindex the factor-67 dilation and recover the local coefficients
   `(1,-2,1)`.
6. Check the all-real cell semantics: both the post-activation left endpoint
   and the pre-activation right limit are tested.
7. Recompute the exact interval at `x=201^-` independently.
8. Run `replay.sh --full` and require byte-identical `10^8` producer output.
9. Re-derive the Mellin transform, including the removable point at `s=1/2`.
10. Apply Landau only to the exact nonnegative scalar `mathfrak H_67`.
11. Verify `1-67^(-rho)` cannot cancel a zero with `Re(rho)>1/2`.
12. Confirm all global and RH status flags remain false.

Immediate falsifiers are:

```text
a negative compact SHARP Hall prefix;
a negative kappa_j value;
a child density not dominated by its parent;
a duplicated random-key child owner;
a mismatch in the local (1,-2,1) coefficient;
a missing right-limit cell evaluation;
a nonpositive retained directed lower bound;
a positive-real singularity omitted from the Mellin audit;
a global-tail or RH flag set true without a proof.
```

The only conclusion-producing unproved statement is

```text
mathfrak H_67(x) >= 0 for every x >= 100000001.
```
