# L-98711 — The fractional heat energy has one exact decorated-history Gaussian Gram

Claim ID: `L-98711`  
Status: **PROVED EXACT FINITE-CUTOFF AND EXHAUSTION THEOREM**  
Created: 2026-08-18  
Depends on: `L-98710`  
RH status: **not assumed**

Let

\[
\mathscr B_{\theta,T}(\tau)
=\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}
\]

and

\[
w_T(t)=\frac{\sqrt T}{\sqrt\pi}e^{-Tt^2}.
\]

Expanding the square and taking the Fourier transform of `w_T` gives the exact
identity

\[
\boxed{
\begin{aligned}
E_{\theta,T}(\tau_0)
&:=\int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
                 w_T(\tau-\tau_0)\,d\tau\\
&=\sum_{m,n\ge1}\frac{b_\theta(m)\overline{b_\theta(n)}}{\sqrt{mn}}
\exp\!\left[-\frac{u_m^2+u_n^2+(u_m-u_n)^2}{4T}\right]
 e^{-i\tau_0(u_m-u_n)},
\end{aligned}}
\tag{L-98711.1}
\]

where `u_n=log n`.

The kernel

\[
\kappa_{T,\tau_0}(u,v)
=e^{-u^2/(4T)}e^{-v^2/(4T)}
 e^{-(u-v)^2/(4T)}e^{-i\tau_0(u-v)}
\tag{L-98711.2}
\]

is positive definite: it is a positive diagonal conjugation and unitary
modulation of the ordinary Gaussian difference kernel.

Using the Sibuya-decorated source from `L-98710`, every finite prime/log cutoff
therefore has one prescribed common Gram. Plus and minus support-parity
histories are two positive subspaces of this same Gram, and all cross-blocks are
simultaneously Schur dominated. No independent local square roots are
required.

This also identifies a statement-to-use error in `L-98703`: its proof invokes

\[
e^{-(u+v)^2/(4T)}e^{-i\tau(u+v)},
\]

which is the total-log Hankel kernel obtained by replacing `v` with `-v`.
That is not the difference kernel in the actual modulus-square energy
(L-98711.1). At `m=n>1`, the two kernels already differ by the nontrivial
factor `e^{-(2\log n)^2/(4T)}`.

For every fixed `T`, the coefficient series with the Gaussian factor is
absolutely summable. Hence the finite-cutoff packets and the full quadratic
form converge by dominated convergence, uniformly for `tau_0` on compact sets.
This is the correct cutoff exhaustion. It does **not** provide the tunable
trace estimate claimed in `L-98703`; the exact phase-blind rate is determined
in `R-98710`.
