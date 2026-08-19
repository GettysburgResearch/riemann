# L-99100 — A high-order phase-locked Hermite notch preserves an off-line zero and annihilates the safe-line saddle

Claim ID: `L-99100`  
Status: **PROVED EXACT TRANSFORM THEOREM**  
Created: 2026-08-19  
Depends on: `L-98702`, `L-98710`  
RH status: **not assumed**

Fix `0<theta<1`. Let

\[
B_\theta(s)=B_\diamond(s)^\theta
=\sum_{n\ge1}b_\theta(n)n^{-s}
\]

be the branch positive on the real line `s>1`, and let

\[
\mathscr B_{\theta,T}(\tau)
=\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\]

Assume, for contradiction, that

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<\delta<\frac12,
\]

is a nontrivial zero of zeta. Put

\[
q=\frac12-\delta>0.
\]

For an integer `M>=0`, define the phase-locked Hermite notch

\[
\boxed{
\mathscr N_{\theta,T,M}^{\rho}(\tau)
=\left(\frac{1-(i/T)\partial_\tau}{2q}\right)^M
 \mathscr B_{\theta,T}(\tau).
}
\tag{L-99100.1}
\]

Termwise differentiation is legal at every fixed `T`, and gives the exact coefficient formula

\[
\boxed{
\mathscr N_{\theta,T,M}^{\rho}(\tau)
=\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
 \left(\frac{1-\log n/T}{2q}\right)^M
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
}
\tag{L-99100.2}
\]

On the Mellin contour of `L-98702`, the same operator contributes the multiplier

\[
\boxed{
\left(-\frac{s-(1+i\tau)}q\right)^M.
}
\tag{L-99100.3}
\]

At the phase-locked center `tau=gamma` and the hypothetical zero `s=rho`,

\[
-\frac{\rho-(1+i\gamma)}q
=-\frac{\delta-1/2}q=1.
\]

Thus the notch leaves the off-line branch contribution unchanged. On the coefficient side it vanishes exactly at the classical safe-line saddle `log n=T`.

If the zero has multiplicity `m`, the Hankel contribution from `rho` therefore retains the lower exponential rate

\[
\mathscr N_{\theta,T,M}^{\rho}(\gamma)
=c_{\rho,\theta,M}
 T^{m\theta-1/2}e^{\delta^2T}(1+o(1))
 +\text{other contours},
\]

where the leading multiplier at `rho` is exactly one. No uniform-center or phase-blind estimate is used.
