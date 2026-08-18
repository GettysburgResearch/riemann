# M-98900 — Correct proof obligations for a pole-subtracted fractional heat route

Status: **METHODOLOGY / REPAIR SPECIFICATION — NO RH CLAIM**  
Created: 2026-08-18

The fractional route can only be reconsidered after replacing the observable.
A valid repair must satisfy all of the following.

## 1. Define the new observable

The packet in `L-98702` contains the branch contribution of `s=1`. Define an
explicit renormalized packet

\[
\mathscr B^{\circ}_{\theta,T}(\tau)
=\mathscr B_{\theta,T}(\tau)-\mathscr P_{\theta,T}(\tau),
\]

where `mathscr P` is the complete Hankel-cut contribution of the real pole
carrier, not merely its leading asymptotic term.

## 2. Reprove the lower interface

Show that every off-line zero still contributes

\[
\exp((\beta-1/2)^2T+o(T))
\]

to the renormalized packet in its ordinate window. This cannot be inherited
by name from `L-98702`, because the scalar observable has changed.

## 3. Build a phase-covariant positive source

Supply an exact Gram whose off-diagonal is the renormalized logarithmic phase
packet. The unphased Tao diagonal is insufficient by `L-98901`. Every prime
update and every Stieltjes lift must be written explicitly before taking a
limit.

## 4. Prove the actual upper estimate

The required conclusion-producing estimate is a high-center or pole-subtracted
bound

\[
\log\mathcal E^\circ_{\theta,T}(\tau_0)
\le c\theta T+o(T),
\]

with `c` absolute and with constants uniform in the centers to which the zero
lower bound is applied. This statement remains open and RH-bearing.

## 5. Exhaustion contract

A cutoff proof must provide:

```text
exact coefficient convergence;
phase-ready Gram covariance;
uniform heat-regularized diagonal trace;
no post hoc use of the target zero location;
strong enough convergence to pass the window energy.
```

Without these five gates, “Weyl removal” is only a change of intended model and
not a proof about the packet written in `L-98702`.
