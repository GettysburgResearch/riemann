# M-98710 — Proof program after the uniform fractional heat no-go

Claim ID: `M-98710`  
Status: **RESEARCH PROGRAM**  
Created: 2026-08-18

The exact source is the Sibuya-decorated squarefree-support measure of
`L-98710`, and the exact finite energy is the Gaussian Gram of `L-98711`.
Future work must preserve those objects.

## Mandatory firewalls

1. No estimate uniform in a center which may move with `T`; `R-98710` refutes
   every tunable phase-blind rate of the proposed form.
2. No use of the integer Tao trace-free atom at `p^2`; it vanishes while the
   fractional coefficient is nonzero.
3. No independent local square roots or post-hoc Douglas contraction.
4. No replacement of the difference kernel in the energy by a total-log Hankel
   kernel.
5. No claim that a trace `<12` is the diagonal mass of the fractional Fock
   histories.
6. No Weyl removal without retaining the displaced-parity operator from
   `R-98712`.

## Correct finite-cutoff target

For a fixed center `tau_0`, a proof must estimate directly

\[
\left\|
 \sum_\omega \epsilon(\omega)w_\theta(\omega)
 e^{-u_\omega^2/(4T)}e^{-i\tau_0u_\omega}
 \Phi_{T,u_\omega}
\right\|^2,
\]

where `omega` ranges over decorated squarefree supports,
`epsilon(omega)=mu(support omega)`, and `Phi` is the Gaussian feature map.

The first variation at `theta=0` is the explicit prime-power carrier. The
second and higher variations are source-owned cumulants, not an unsigned Fock
remainder. A viable route should therefore prove a fixed-center cumulant or
martingale estimate covariant under support-prime adjoining.

## Three concrete attacks

1. **Phase-locked cumulant expansion.** Split the continuous pole carrier at
   the fixed center, compute it exactly, and prove a convergent cluster bound
   for the Sibuya residual. The bound must be nonuniform in `tau_0` and must
   reproduce the Bohr no-go when `tau_0` moves.
2. **First-Hermite carrier covariance.** Couple the first variation to the
   phase-locked covariance kernel of the independent First-Hermite lane, then
   control higher cumulants by decorated-support hypercontractivity.
3. **Arithmetic cross-state Gram.** Prescribe cross blocks directly from the
   support-owner transition, not from local Tao marginals. Test every proposed
   Gram on the exact `p^2` fixture and on the Bohr-twist lower bound.

A successful theorem is PLFHE from `T-98710`. It would imply RH immediately,
but it is not proved here.
