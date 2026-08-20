# T-99900 — Exact cube-flow hardening and the EPXGC successor

Claim ID: `T-99900`  
Status: **UNCONDITIONAL STRUCTURAL THEOREM; RH CONCLUSION REMAINS CONDITIONAL**  
Created: 2026-08-20  
Depends on: PR #658; `L-99900--L-99902`; `R-99900--R-99901`  
RH status: **unproved**

The following statements are unconditional:

1. every fully active weighted source cube admits an exact one-label Hasse flow
   saturating the lighter parity channel;
2. its optimal residual is the parity bias \(\prod_i(1-r_i)\);
3. the native normalized source is obtained with activities \(1/p\) and two
   separately labelled copies of \(67\);
4. the factor-67 box admits an exact positive layer-cake decomposition;
5. all unresolved local mass lies in the complete-cube parity bias plus the
   partial-activation collar;
6. the collar has the explicit deep formula of `L-99901.4`;
7. source-blind independent cube matching cannot yield the half-order PXGC
   saving;
8. unrestricted path adjacency is circular, while path capacities require a
   node-split network.

Define `EPXGC99900` to be the subpower logarithmic unmatched-mass estimate on
the direct Hasse or fully node-split network, with phase-sensitive cross-core
capacities prescribed before the source sign is observed.

Then the zero-free box and Mellin–Landau consumer of PR #658 give

\[
\boxed{
EPXGC99900\Longrightarrow PXGC99700\Longrightarrow RH.
}
\tag{T-99900.1}
\]

`EPXGC99900`, `PXGC99700`, and RH are not proved by this packet.
