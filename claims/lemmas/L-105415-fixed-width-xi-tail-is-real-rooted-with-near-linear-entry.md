# L-105415 — The fixed-width high Xi derivative tail is real-rooted with near-linear entry order

Claim ID: `L-105415`  
Status: **PROPOSED COMPLETE ANALYTIC CONSEQUENCE — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-24  
Depends on: `L-105414`; the phase-cell argument of `L-105322`  
RH status: **not assumed**

## 1. Fixed-width real-rooted tail

Fix `H>0` and `0<c_2<c_1<c_0`, where `c_0` is from `L-105414`. Put

\[
T_M=c_1{M\over\log M}.
\]

For all sufficiently large `M`, simultaneously for every `m>=M`, every zero of

\[
\Xi^{(m)}(z)
\]

in

\[
\boxed{
|\Re z|\le T_M,
\qquad
|\Im z|\le H
}
\tag{L-105415.1}
\]

is real and simple.

## 2. Proof by the exact phase

The reflected derivative is

\[
\Xi^{(m)}(z)
=i^mM_m[A_m(z)+(-1)^mA_m(-z)].
\]

Replacing both factors by `L-105414` gives the nonvanishing model

\[
\mathcal X_m(z)
=
\begin{cases}
2e^{E_m(z)}\cos\Theta_m(z),&m\text{ even},\\
2ie^{E_m(z)}\sin\Theta_m(z),&m\text{ odd}.
\end{cases}
\tag{L-105415.2}
\]

Because `Re Theta_m'>0` on the convex box, `Theta_m` is univalent there. It is real and strictly increasing on the real axis, and

\[
\operatorname{sgn}\Im\Theta_m(x+iy)
=
\operatorname{sgn}y.
\tag{L-105415.3}
\]

Thus all model zeros are real and simple.

Choose phase disks of radius `delta_M` with

\[
\kappa_M^{-1/3}=o(\delta_M),
\qquad
\delta_M\to0.
\]

Work inside the `c_1` box while constructing all intersecting phase cells in the larger `c_0` box. On every phase-cell boundary the sine/cosine factor is `gg delta_M`; on the complement either the phase is vertically separated or its real part is away from the lattice. The relative error in `L-105414` is `o(delta_M)`. Rouché gives exactly one Xi zero in each conjugation-symmetric cell and none outside. Each such zero is real and simple.

## 3. Exact count and residue sign

For every regular `T<=T_M`,

\[
\boxed{
N_m(T)
={\Theta_m(T)-\Theta_m(-T)\over\pi}+O(1).
}
\tag{L-105415.4}
\]

Moreover,

\[
\Theta_m'(x)=w_m+O(c_1)+o(1),
\]

so

\[
N_m(T)={2w_mT\over\pi}+O(c_1T)+O(1).
\tag{L-105415.5}
\]

At every real zero `c` of `Xi^(m+1)` in the buffered `c_2` box,

\[
\boxed{
{\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
=-w_m^{-2}(1+o(1))<0.
}
\tag{L-105415.6}
\]

This follows from the exact identity for `g=e^E chi(Theta)`:

\[
{g''\over g}
=
E''-(\Theta')^2-(E')^2-{E'\Theta''\over\Theta'},
\tag{L-105415.7}
\]

together with the fixed-derivative transfer in `L-105414`.

## 4. Height/order inversion

The condition `T<=c_1 M/log M` is paid by

\[
\boxed{
M\ge K_H T\log(2+T)
}
\tag{L-105415.8}
\]

for one sufficiently large constant. Hence a fixed physical Xi rectangle is cleared by all derivative orders

\[
\boxed{m\ge K_HT\log(2+T).}
\tag{L-105415.9}
\]

This supplies the proposed `O(T log T)` high-derivative entry of `L-105322`, subject to hostile review of `L-105413--L-105414`.

## 5. Scope

The theorem supplies the fixed-width terminal derivative and negative high-tail residues. It does not estimate the derivative-ladder Levinson quotient, prove the low-order pointwise residue signs, establish the low-order boundary Loewner kernel, or prove RH.
