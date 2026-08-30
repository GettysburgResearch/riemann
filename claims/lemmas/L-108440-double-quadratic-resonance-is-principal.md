# L-108440 — The double quadratic resonance is exactly the principal physical member

Claim ID: `L-108440`  
Status: **PROVED EXACT SOURCE-LEVEL ALIAS THEOREM**  
Created: 2026-08-31  
Depends on: the physical map of PR #765 and the resonance classification of `L-107301--L-107302`  
RH/GRH status: **not assumed**

Fix one shared-conductor fibre

\[
\iota=(g,\ell,\rho,\sigma,\tau),
\]

with physical squareclass map

\[
(Q,d;P,c)\longmapsto(Qd^2,Pc^2)
\tag{L-108440.1}
\]

and owner classes

\[
\kappa_\ell(Q)=\sigma,
\qquad
\kappa_\rho(P)=\tau.
\tag{L-108440.2}
\]

Assume both quadratic characters are even, equivalently

\[
\ell\equiv\rho\equiv1\pmod4.
\]

For arbitrary literal coefficients `z_omega`, define the physical character
transform

\[
\widehat Z(\eta,\theta)
=
\sum_\omega z_\omega
\eta(Q_\omega d_\omega^2)
\theta(P_\omega c_\omega^2).
\tag{L-108440.3}
\]

Then

\[
\kappa_\ell(Qd^2)=\kappa_\ell(Q)=\sigma,
\qquad
\kappa_\rho(Pc^2)=\kappa_\rho(P)=\tau.
\]

Therefore

\[
\boxed{
\widehat Z(\kappa_\ell,\kappa_\rho)
=
\sigma\tau\,\widehat Z(\mathbf1,\mathbf1),
}
\tag{L-108440.4}
\]

and in particular

\[
\boxed{
|\widehat Z(\kappa_\ell,\kappa_\rho)|^2
=
|\widehat Z(\mathbf1,\mathbf1)|^2.
}
\tag{L-108440.5}
\]

The identity is coefficientwise and survives every source mask, endpoint
colour, Mellin parameter, Boolean history and physical shell retained inside
the fixed fibre.

## 1. Exact Gauss-weight ratio

In the bilateral tensor normalization of `L-106120`, a nonprincipal even
character has weight

\[
w_q={2q\over q-1},
\]

while the principal member has weight

\[
c_q={q+1\over q-1}.
\]

Consequently, after applying the exact source-to-squareclass adapter, the
double quadratic row has the fixed positive weight ratio

\[
\boxed{
{w_\ell w_\rho\over c_\ell c_\rho}
=
{4\ell\rho\over(\ell+1)(\rho+1)}.
}
\tag{L-108440.6}
\]

Thus a positive or absolute-value bound for the double quadratic row is,
fibre by fibre, the same bound as for the principal physical member up to the
explicit factor (L-108440.6).

## 2. Geometric meaning

The pullback of each quadratic Kummer sheaf by the square map is constant.
For the double row both core variables disappear, leaving only the fixed
owner-class scalar `sigma tau`. Deligne cancellation and nonconstant trace
estimates have no leverage on this row.

The row must instead be recombined with the principal/root ledger before any
absolute value is taken. Calling it one of “at most three finite resonance
errors” hides the conclusion channel.

## 3. Scope

The theorem does not prove the principal estimate. It proves that the double
quadratic part of `QRESBIND107300` is not an independently disposable local
error. When one or both quadratic characters are absent, the corresponding
row is absent. The one-coordinate quadratic rows remain separate one-sided
arithmetic problems.
