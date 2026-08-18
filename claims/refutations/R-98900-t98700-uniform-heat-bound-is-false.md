# R-98900 — The uniform fractional heat estimate `L-98703.1` is false

Claim ID: `R-98900`  
Status: **PROVED ANALYTIC REFUTATION OF THE LOAD-BEARING CANDIDATE THEOREM**  
Created: 2026-08-18  
Depends on: `L-98900`  
Reviewed head: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`

`L-98703` claims, for every `0<theta<=1/8`, every `T>=1`, and every real center
`tau_0`,

\[
\mathcal E_{\theta,T}(\tau_0)
\le C(1+T)^{24}
 \exp\!\left(96\theta T+CT^{3/4}(\log(2T))^2\right),
\tag{R-98900.1}
\]

with an absolute constant `C`.

Choose any fixed

\[
0<\theta<\frac1{192};
\]

for example `theta=1/384`. At `tau_0=0`, `L-98900` gives

\[
\log\mathcal E_{\theta,T}(0)
=\frac12T+O_\theta(\log T).
\tag{R-98900.2}
\]

The claimed upper bound has

\[
\log\mathrm{RHS}
=96\theta T+o(T),
\tag{R-98900.3}
\]

and `96 theta<1/2`. Equations (R-98900.2)--(R-98900.3) contradict one another
for all sufficiently large `T`.

Therefore

\[
\boxed{\text{`L-98703.1` is false as quantified.}}
\]

The contradiction is present even if RH is true. It comes from the real pole
carrier at `s=1`, not from an off-line zero.

## Uniform-center firewall

For every fixed `T`, the series in `L-98900.1` converges absolutely and uniformly
on the real `tau` axis. It is therefore uniformly Bohr almost periodic.
Consequently, for every `epsilon>0`, there are arbitrarily large shifts `h`
such that

\[
\sup_\tau
|\mathscr B_{\theta,T}(\tau+h)-\mathscr B_{\theta,T}(\tau)|<\epsilon.
\]

Thus the large center-zero energy recurs at arbitrarily large centers. Merely
adding a lower bound on `|tau_0|` does not repair any estimate that remains
uniform over all centers.

## Consequence for `T-98700`

`L-98704` and `T-98700` use `L-98703` as their sole unconditional upper bound.
Since that theorem is false, the submitted chain does not prove RH.

A repaired argument must define a genuinely different pole-subtracted packet,
prove its exact source-side realization, and redo both the off-line-pole lower
bound and the upper energy estimate for that new observable.
