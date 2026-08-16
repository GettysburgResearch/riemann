# L-94123 — The frozen one-sided endpoint consumer applies to the projective row

Claim ID: `L-94123`  
Status: **PROVED COMPOSITION FROM THE DECLARED FROZEN CONSUMER THEOREMS**  
Created: 2026-08-16  
Frozen inputs: PR #352 `906b5a477a1ed7c88a40db7569924f15f3d54b72`; PR #353 `ed566f3198e236c54ba18049181016536f56d456`; PR #508 `4ae97dffd1f76ed3244b8f3028560ffa80663caf`  
RH status: **candidate conclusion pending independent reconstruction**

The finite dual has the one-sided orientation

\[
F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X).
\tag{L-94123.1}
\]

By `L-94122`, the right side is bounded by `3457`, hence is
`o(log^2 X)`.  The frozen prime-square moat removes every higher-prime-power
contribution with the correct sign.  Therefore the prime endpoint transform has
the eventual one-sided sign required by the Mellin–Landau theorem.

The frozen Mellin computation identifies all possible poles of the transform.
Landau's one-sign theorem excludes a rightmost off-critical pole.  Functional
equation symmetry excludes its reflected partner.  Consequently every
nontrivial zero has real part `1/2`.

No estimate for `J_Lambda(X)-4sqrt(X)` enters (L-94123.1).  The only new
antecedent supplied by this packet is the actual nonnegative native-feasible row
of `L-94122`.
