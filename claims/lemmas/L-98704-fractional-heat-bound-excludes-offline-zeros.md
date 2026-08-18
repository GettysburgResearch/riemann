# L-98704 — A tunable fractional heat bound excludes every off-line zeta zero

Claim ID: `L-98704`  
Status: **PROVED CONDITIONAL COMPOSITION FROM L-98702 AND L-98703**  
Created: 2026-08-18  
Depends on: `L-98702`, `L-98703`  
RH status: **conclusion-producing**

Assume an off-line zero `rho=beta+i gamma`, `delta=beta-1/2>0`. Choose

\[
0<\theta<\min\left(\frac18,\frac{\delta^2}{192}\right).
\]

By `L-98702`, a Gaussian window centered at `gamma` has lower energy

\[
\gg T^{2m\theta-1}e^{2\delta^2T}.
\]

By `L-98703`, the same energy is at most

\[
C(1+T)^{24}e^{96\theta T+C T^{3/4}(\log(2T))^2}.
\]

Since `96 theta<delta^2/2`, the lower exponential rate is strictly larger. Letting `T` tend to infinity gives a contradiction. Therefore zeta has no zero with real part greater than `1/2`. The functional equation gives the symmetric half, and all nontrivial zeros lie on the critical line.
