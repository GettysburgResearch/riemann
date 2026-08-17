# M-97300 — Hostile reconstruction protocol for the completed-parity scalar route

Claim ID: `M-97300`  
Status: **METHODOLOGY / FAIL-CLOSED REVIEW CONTRACT**

A reviewer should reject any claimed completion that violates one of these
interfaces:

1. **Parity owner:** every history contributes `S^|h|`, not a canonical packet.
2. **Target direction:** row-ratio information is not a target-capacity proof.
3. **Normalization:** distinguish row-2 exactness from `5:3` scalar exactness.
4. **Typed scope:** target-plus-scalar feasibility does not silently imply score
   or all-row feasibility.
5. **Depth:** no bounded-depth parity reset may be promoted after PR #561/#568.
6. **Global ownership:** one even source coefficient cannot be spent by two odd
   histories.
7. **LP gate:** at fixed `X`, compare the odd scalar demand to the exact Lorenz
   optimum `Phi_X(T_O)`; do not substitute a larger unrestricted reservoir.
8. **Analytic consumer:** the replay does not prove Landau's theorem or RH.

A positive successor must provide either a proof of `CPSL67` for every endpoint,
an equivalent all-scale Bellman/Julia extraction, or a source-complete dual
argument excluding every separating threshold.
