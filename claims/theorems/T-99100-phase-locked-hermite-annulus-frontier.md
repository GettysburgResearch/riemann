# T-99100 — Optimal phase-locked Hermite annular cancellation implies RH

Claim ID: `T-99100`  
Status: **PROPOSED CONDITIONAL COMPOSITION — NEW SHARP FRONTIER**  
Created: 2026-08-19  
Depends on: `L-98702`, `L-99100`--`L-99103`  
RH status: **unproved because PLHAC99100 is open**

Define **PLHAC99100** as follows. If

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<\delta<\frac12,
\]

is a hypothetical zeta zero, set

\[
q=\frac12-\delta,
\qquad
M=\lfloor2q^2T\rfloor,
\]

and form the one-sided optimally notched packet of `L-99102`. Prove, from the Sibuya source and the phase-twisted owner martingale of `L-99103`, that for some `eta=eta(rho,theta)>0`,

\[
\boxed{
\left|\mathscr N_{\theta,T,M}^{\rho}(\gamma)\right|
\le
\exp\bigl((\delta^2-\eta)T+o_{\rho,\theta}(T)\bigr).
}
\tag{T-99100.1}
\]

Equivalently, relative to the optimal absolute envelope, the arithmetic phases must save more than

\[
\delta(1-2\delta)T.
\]

`L-99100` shows that the multiplier at `rho` is exactly one. The local Hankel term of `L-98702` therefore gives

\[
\left|\mathscr N_{\theta,T,M}^{\rho}(\gamma)\right|
\gg_{\rho,\theta}
T^{m\theta-1/2}e^{\delta^2T}
\]

after fixed-center isolation of the selected branch. This contradicts (T-99100.1).

Hence

\[
\boxed{
\mathrm{PLHAC99100}\Longrightarrow\mathrm{RH}.
}
\]

This theorem is not presented as a proof of PLHAC99100. Its contribution is to replace the false uniform-center heat estimate and the vague fixed-center frontier by:

1. the unique optimal scalar notch;
2. the exact annular scale `log n=2delta T+O(sqrt T)`;
3. the exact missing phase-saving exponent `delta(1-2delta)`;
4. a prescribed fractional owner martingale on which a source-faithful Carleson/dispersion proof must operate.

No RH-strength estimate is assumed elsewhere in the chain.
