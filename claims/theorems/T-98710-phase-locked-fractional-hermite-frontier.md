# T-98710 — Corrected phase-locked fractional Hermite frontier

Claim ID: `T-98710`  
Status: **EXACT CONDITIONAL REDUCTION; PRODUCER OPEN**  
Created: 2026-08-18  
Supersedes: the uniform-center theorem `L-98703` and complete claim `T-98700`  
RH status: **unproved**

For a fixed real center `tau_0`, define

\[
E_{\theta,T}(\tau_0)
=\int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \frac{\sqrt T}{\sqrt\pi}e^{-T(\tau-\tau_0)^2}\,d\tau.
\]

Define **PLFHE** (phase-locked fractional Hermite energy) to mean that there is
an absolute `c<infinity` such that, for every fixed `tau_0` and every
`0<theta<=1/8`,

\[
E_{\theta,T}(\tau_0)
\le C_{\theta,\tau_0}(1+T)^{A_{\theta,\tau_0}}
 \exp\{c\theta T+o_{\theta,\tau_0}(T)\}.
\tag{T-98710.1}
\]

The constants may depend on the fixed center; no uniformity over centers which
move with `T` is required or possible by `R-98710`.

If PLFHE holds, then RH follows. Indeed, if
`rho=beta+i gamma`, `delta=beta-1/2>0`, the pole-growth theorem `L-98702`
gives at the fixed center `gamma`

\[
E_{\theta,T}(\gamma)
\gg_{\rho,\theta}T^{2m\theta-1}e^{2\delta^2T}.
\]

Choose `theta<2delta^2/c`. This contradicts (T-98710.1).

The exact source formulation of PLFHE is the Sibuya-decorated Gaussian Gram in
`L-98710`--`L-98711`. `L-98713` proves that the corresponding phase-blind
uniform-center norm has exact exponential type `1/2`, so any successful proof
must use the fixed center before taking norms. The remaining estimate must
exploit the fixed arithmetic phases `p^(-i tau_0)` and may not be obtained from
a phase-independent trace or an unconstrained common contraction. Its first
variation at `theta=0` is the phase-locked prime carrier of the independent
First-Hermite lane, so a proof must visibly control that carrier and all higher
support cumulants.

```text
fractional decorated source              proved exact
one common finite heat Gram               proved exact
cutoff exhaustion                         proved exact
uniform-center exponential type           exactly 1/2
first-chaos trace                          (theta/2)log T+O(theta)
Weyl parity invariance                     false
fixed-center PLFHE                         open / RH-bearing
PLFHE -> RH                                proved conditional
Riemann Hypothesis                         unproved
```
