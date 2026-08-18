# L-98900 — Exact compensated Weyl-parity carrier identity

Claim ID: `L-98900`  
Status: **PROVED EXACT OPERATOR IDENTITY; NO HEAT GAIN CLAIMED**  
Created: 2026-08-18  
Depends on: `R-98900`  
RH status: **not assumed**

The failure in `R-98900` has a precise repair.  If a common displacement
`W(-h)` is used to center two Fock vectors `xi,eta`, then

\[
\boxed{
\langle W(-h)\xi,\Pi W(-h)\eta\rangle
 =\langle\xi,W(2h)\Pi\eta\rangle.
}
\tag{L-98900.1}
\]

Hence pole-carrier centering is legal only if the translated parity observable
is simultaneously replaced by the compensated observable

\[
\boxed{\Pi_h=W(2h)\Pi.}
\tag{L-98900.2}
\]

`Pi_h` is unitary, but it is not parity and it is not source-free.  In the
one-mode coherent fixture `xi=eta=W(h)Omega`, all of the original parity signal
moves into the compensator:

\[
\langle W(-h)\xi,\Pi W(-h)\eta\rangle
 =\langle\Omega,W(2h)\Pi\Omega\rangle
 =e^{-2\|h\|^2}.
\tag{L-98900.3}
\]

Thus no estimate may delete `Pi_h` merely because the displacement is unitary.
Any repaired fractional Julia–Hermite argument must control the compensated
matrix coefficient uniformly at the critical heat scale.

In particular, the candidate bound of PR #613 can only be recovered by proving
an estimate for the compensated carrier itself.  That estimate is not supplied
by positivity of the unshifted Tao Gram, and at present is an open
conclusion-producing theorem.
