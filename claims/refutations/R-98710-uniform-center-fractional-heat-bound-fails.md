# R-98710 — The uniform-center fractional heat bound is false by Bohr twisting

Claim ID: `R-98710`  
Status: **REFUTATION — EXACT ASYMPTOTIC CONTRADICTION**  
Created: 2026-08-18  
Refutes: `L-98703.1` and the conclusion chain `L-98704/T-98700` as submitted  
RH status: **not assumed**

Let `b_theta(n)` be the coefficients of

\[
B_\diamond(s)^\theta
=\frac{(1-2^{-s})^\theta(1-2^{-s-1})^\theta}{\zeta(s)^\theta}.
\]

The estimate in `L-98703.1` is asserted uniformly in the center `tau_0`. That
uniformity is impossible.

## 1. The extremal Bohr twist

Let `chi_-(p)=-1` for every prime and extend `chi_-` completely
multiplicatively. Twisting the Dirichlet coefficients gives

\[
D_\theta(s)
:=\sum_{n\ge1}b_\theta(n)\chi_-(n)n^{-s}.
\]

A local Euler-factor calculation gives

\[
\boxed{
D_\theta(s)
=\zeta(s)^\theta H_\theta(s),
\qquad
H_\theta(s)
=\left[
\frac{(1+2^{-s})(1+2^{-s-1})}{\zeta(2s)}
\right]^\theta.
}
\tag{R-98710.1}
\]

The factor `H_theta` is holomorphic and strictly positive at `s=1`.

## 2. Gaussian Selberg--Delange asymptotic

If

\[
D(s)=\zeta(s)^\alpha H(s),
\qquad 0<\alpha<1,
\]

with `H` holomorphic and nonzero in a classical zero-free dented neighborhood
of `s=1`, then Gaussian Mellin inversion followed by a Hankel contour at `1`
gives

\[
\sum_{n\ge1}\frac{d(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}
=\frac{2\sqrt\pi H(1)}{\Gamma(\alpha)}
 T^{\alpha-1/2}e^{T/4}(1+o(1)).
\tag{R-98710.2}
\]

Indeed, after writing `s=1/2+z`, the leading contour contribution is

\[
2\sqrt{\pi T}\,H(1)e^{T/4}
\frac1{2\pi i}\int_{\mathcal H}w^{-\alpha}e^{Tw+Tw^2}\,dw,
\]

where `w=z-1/2` and `mathcal H` is a Hankel contour. Scaling `w=u/T`
produces `T^(alpha-1)/Gamma(alpha)`; the Gaussian vertical tails and the dented
zero-free contour are smaller. This uses only the classical zero-free region
near `1`, not RH.

Applying (R-98710.2) to (R-98710.1),

\[
\boxed{
\mathscr B^{\chi_-}_{\theta,T}(0)
=c_\theta T^{\theta-1/2}e^{T/4}(1+o(1)),
\qquad c_\theta>0.
}
\tag{R-98710.3}
\]

The Dirichlet series of the absolute coefficients also has the form
`zeta(s)^theta H_abs(s)` near `1`. The same argument with one logarithmic
weight gives

\[
\sum_n\frac{|b_\theta(n)|}{\sqrt n}
 e^{-(\log n)^2/(4T)}\log n
\ll_\theta e^{T/4}T^{\theta+1/2}.
\tag{R-98710.4}
\]

Therefore the twisted packet remains at least half of its value at zero on an
interval of length `c_theta/T`. Integrating against `w_T` gives

\[
\boxed{
E^{\chi_-}_{\theta,T}(0)
\gg_\theta e^{T/2}T^{2\theta-3/2}.
}
\tag{R-98710.5}
\]

## 3. Vertical translates approximate the twist

For fixed `T`, the heat packet and its windowed energy are absolutely convergent
uniformly almost-periodic Dirichlet series. Rational independence of the
numbers `log p` and Kronecker approximation give centers `tau_j` such that

\[
p^{-i\tau_j}\longrightarrow-1
\]

simultaneously on every prescribed finite prime set. Absolute convergence
then lets the finite set grow, so

\[
\sup_{\tau_0\in\mathbb R}E_{\theta,T}(\tau_0)
\ge E^{\chi_-}_{\theta,T}(0).
\tag{R-98710.6}
\]

## 4. Contradiction with L-98703

Choose the permitted fixed value

\[
\theta_0=\frac1{384}.
\]

The lower exponential rate in (R-98710.5) is `1/2`. The proposed upper rate is

\[
96\theta_0=\frac14,
\]

and its remaining term `C T^(3/4)log^2(2T)` is `o(T)`. Hence, for every finite
choice of the asserted absolute constants, (R-98710.5)--(R-98710.6) contradict
`L-98703.1` for all sufficiently large `T`.

Thus

\[
\boxed{\text{L-98703.1 is false as stated.}}
\]

The refutation uses centers depending on `T`. It does not refute a
**fixed-center, phase-sensitive** estimate with constants allowed to depend on
that fixed center. Such an estimate is the corrected frontier in `T-98710`.
