# L-15631 — Smooth differential Mellin cardinals give an exact sub-square-root source inverse

Claim ID: `L-15631`  
Title: Exact finite Fourier interpolation, both source constraints, and a two-end support-phase ledger from one smooth cardinal construction  
Status: `PROPOSED — COMPLETE SOURCE/INTERPOLATION PROOF; LOCAL ZETA LOWER BOUND AND PRODUCTION NORM TRANSPORT AUDIT DECLARED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: the Mellin normalization of `L-16205/L-16211`; Riemann--von Mangoldt; the standard local zeta-product estimate in a fixed strip  
Scope: production input for `L-15630`  
Related counterexample candidates: none

## 1. Purpose

`L-15628` used sharp logarithmic box cardinals and one guard mode to impose the
ordinary source integral. The exact interpolation idea is sound, but a
proof-grade radial/endpoint producer benefits from smooth sources and should not
rely on a high-frequency guard denominator.

This lemma gives a smoother construction.

1. Convolve the exact Fourier box cardinal with one fixed smooth bump. The
   grid zeros remain exact.
2. Apply the differential operator
   \[
   \partial_t+\frac12.
   \]
   Its Fourier multiplier vanishes exactly at the Mellin point representing the
   ordinary source integral.
3. Divide by the nonzero real-grid multiplier.

Every column is smooth and compactly supported, both Connes--Consani source
constraints hold exactly, and the Fourier/Mellin interpolation remains the
Kronecker delta. The high-frequency transform has exactly two endpoint phases,
so it fits the support-average architecture directly.

## 2. Smooth cardinal window

Fix once and for all

\[
 \eta\in C_c^\infty((-a,a)),
 \qquad
 \int_{\mathbb R}\eta(t)\,dt=1.
 \tag{L-15631.1}
\]

For `L>1`, put

\[
 b_L(t)=\frac1L\mathbf1_{[-L/2,L/2]}(t),
 \qquad
 \chi_L=b_L*\eta.
 \tag{L-15631.2}
\]

Then

\[
 \chi_L\in C_c^\infty((-L/2-a,L/2+a)),
 \qquad
 \int\chi_L=1.
 \tag{L-15631.3}
\]

Use the Fourier convention

\[
 \widehat q(z)=\int_{\mathbb R}q(t)e^{-izt}\,dt.
 \tag{L-15631.4}
\]

A direct calculation gives

\[
 \boxed{
 \widehat\chi_L(z)
 =
 \frac{2\sin(Lz/2)}{Lz}\widehat\eta(z),
 }
 \tag{L-15631.5}
\]

with the removable value one at `z=0`.

Let

\[
 \omega_k={2\pi k\over L}.
 \tag{L-15631.6}
\]

Then

\[
 \boxed{
 \widehat\chi_L(\omega_j-\omega_k)=\delta_{jk}
 }
 \tag{L-15631.7}
\]

for all integers `j,k`. The smoothing factor does not change any grid zero.

## 3. Differential source correction

Define

\[
 g_{k,L}(t)=\chi_L(t)e^{i\omega_kt}
 \tag{L-15631.8}
\]

and

\[
 \boxed{
 q_{k,L}(t)
 =
 { (\partial_t+1/2)g_{k,L}(t)
  \over i\omega_k+1/2}.
 }
 \tag{L-15631.9}
\]

The denominator never vanishes for real `omega_k`. Integration by parts gives

\[
 \widehat q_{k,L}(z)
 =
 {iz+1/2\over i\omega_k+1/2}
 \widehat\chi_L(z-\omega_k).
 \tag{L-15631.10}
\]

At the real Fourier grid,

\[
 \boxed{
 \widehat q_{k,L}(\omega_j)=\delta_{jk}.
 }
 \tag{L-15631.11}
\]

At the source-integral Mellin point,

\[
 iz+\frac12=0
 \quad\text{when}\quad z=\frac i2.
\]

Therefore

\[
 \boxed{
 \widehat q_{k,L}(i/2)=0.
 }
 \tag{L-15631.12}
\]

No guard mode or finite correction solve is needed.

## 4. Multiplicative source

On the positive half-line define

\[
 f_{k,L}(e^t)=e^{-t/2}q_{k,L}(t)
 \tag{L-15631.13}
\]

and extend evenly to the real additive source variable.

Because `q_(k,L)` has compact support bounded away from `t=-infinity`, the even
source is smooth and vanishes in a neighborhood of zero:

\[
 f_{k,L}(0)=0.
 \tag{L-15631.14}
\]

Moreover,

\[
 \int_0^\infty f_{k,L}(x)\,dx
 =
 \int_{\mathbb R}q_{k,L}(t)e^{t/2}\,dt
 =
 \widehat q_{k,L}(i/2)
 =0.
 \tag{L-15631.15}
\]

Thus the even extension satisfies exactly

\[
 \boxed{
 f_{k,L}(0)=0,
 \qquad
 \int_{\mathbb R}f_{k,L}(x)\,dx=0.
 }
 \tag{L-15631.16}
\]

The positive-half Mellin transform is exactly `widehat(q_(k,L))`, in the
normalization of `L-16205`.

## 5. Exact projected right inverse

Let

\[
 E_N(L)=\operatorname{span}
 \{e^{i\omega_k t}:|k|\le N\},
 \qquad
 N\le C_0L^2.
 \tag{L-15631.17}
\]

Assume the selected length obeys

\[
 \zeta(1/2+i\omega_k)\ne0
 \qquad(|k|\le N).
 \tag{L-15631.18}
\]

For

\[
 y(t)=\sum_{|k|\le N}y_ke^{i\omega_kt},
\]

define

\[
 \boxed{
 {\cal C}_Ly
 =
 \sum_{|k|\le N}
 {y_k\over\zeta(1/2+i\omega_k)}f_{k,L}.
 }
 \tag{L-15631.19}
\]

The arithmetic Mellin multiplier and (L-15631.11) give

\[
 \boxed{
 P_N\Sigma E({\cal C}_Ly)=y.
 }
 \tag{L-15631.20}
\]

Every column already belongs to the exact source space. Hence `C_L` is an exact
smooth source right inverse on the complete finite Fourier target.

## 6. Polynomial smooth graph bound before zeta inversion

For every integer `p>=0`, convolution gives

\[
 \|\chi_L^{(p)}\|_1\le\|\eta^{(p)}\|_1.
 \tag{L-15631.21}
\]

Leibniz and

\[
 |i\omega_k+1/2|\asymp1+|\omega_k|
\]

give

\[
 \boxed{
 \|q_{k,L}\|_{W^{p,1}}
 \le C_{p,\eta}(1+|\omega_k|)^p.
 }
 \tag{L-15631.22}
\]

Since `N=O(L^2)`,

\[
 \max_{|k|\le N}|\omega_k|=O(L)
 \tag{L-15631.23}
\]

and the number of columns is `O(L^2)`. Cauchy--Schwarz therefore gives the
synthesis estimate

\[
 \boxed{
 \left\|\sum_{|k|\le N}c_kq_{k,L}\right\|_{W^{p,1}}
 \le C_{p,\eta}L^{p+1}\|c\|_{\ell^2}.
 }
 \tag{L-15631.24}
\]

The same argument after differentiating with respect to `L` is polynomial in
`L`: the moving box endpoints are convolved with `eta`, and
`partial_L omega_k=O(|k|/L^2)=O(1)` on the declared window. Thus

\[
 \boxed{
 \|Q_L\|_{\ell^2\to W^{p,1}}
 +\|\partial_LQ_L\|_{\ell^2\to W^{p,1}}
 \le L^{C_p}.
 }
 \tag{L-15631.25}
\]

No distributional endpoint derivative remains.

## 7. Cofinal zero avoidance and zeta multiplier

Choose lengths `ell_A in [A,A+1]` by deleting the resonant sets

\[
 \left|{2\pi k\over\ell}-\gamma\right|<A^{-4}
 \tag{L-15631.26}
\]

for every required integer `k` and every nontrivial zero ordinate in the
required height range. The Riemann--von Mangoldt count gives total deleted
measure

\[
 O(A^{-2}\log A)<1.
 \tag{L-15631.27}
\]

The standard local zeta product and partial-fraction estimates then give

\[
 \boxed{
 \max_{|k|\le C A^2}
 |\zeta(1/2+2\pi ik/\ell_A)|^{-1}
 +
 \max_k\left|\partial_\ell
 \zeta(1/2+2\pi ik/\ell)^{-1}\right|_{\ell=\ell_A}
 \le
 \exp(C(\log A)^2).
 }
 \tag{L-15631.28}
\]

The bounded low-height range is handled by finite avoidance and compactness.

If

\[
 R=e^{L},
\]

then the right side is

\[
 R^{o(1)}.
 \tag{L-15631.29}
\]

Combining (L-15631.25) and (L-15631.28), the exact logarithmic source inverse has
fixed-order graph norm and support derivative

\[
 \boxed{R^{o(1)}.}
 \tag{L-15631.30}
\]

## 8. Exact two-end support-phase decomposition

Equation (L-15631.5) gives

\[
 \widehat\chi_L(z-\omega_k)
 =
 {e^{iL(z-\omega_k)/2}-e^{-iL(z-\omega_k)/2}
  \over iL(z-\omega_k)}
 \widehat\eta(z-\omega_k).
 \tag{L-15631.31}
\]

Since

\[
 e^{\mp iL\omega_k/2}=e^{\mp i\pi k}=(-1)^k,
\]

we obtain the exact two-branch formula

\[
 \boxed{
 \widehat q_{k,L}(z)
 =
 e^{iLz/2}a_{k,+}(z,L)
 +e^{-iLz/2}a_{k,-}(z,L),
 }
 \tag{L-15631.32}
\]

where

\[
 a_{k,\pm}(z,L)
 =
 \pm(-1)^k
 {iz+1/2\over i\omega_k+1/2}
 {\widehat\eta(z-\omega_k)
  \over iL(z-\omega_k)}.
 \tag{L-15631.33}
\]

The apparent singularity at `z=omega_k` is removable in the sum. For a
proof-producing phase partition one may retain a compact neighborhood of that
point exactly and use (L-15631.10) there.

Because `eta` is smooth and compactly supported, integration by parts gives,
uniformly on every fixed horizontal strip,

\[
 |\partial_z^r\widehat\eta(x+iy)|
 \le C_{r,p}(1+|x|)^{-p}.
 \tag{L-15631.34}
\]

Consequently the branch-amplitude synthesis and its logarithmic support
derivative have only the graph cost already recorded in (L-15631.30). The
common phases are exactly

\[
 e^{\pm iLz/2}.
 \tag{L-15631.35}
\]

Thus the exact completion has a finite two-end support-phase ledger; it is not
an arbitrary Möbius tail with unknown oscillatory geometry.

## 9. Multiplicative profile envelope

In the reciprocal Hardy/endpoint normalization used by the current radial
ledger, transporting a logarithmic source supported in

\[
 [-L/2-a,L/2+a]
\]

to the symmetric multiplicative source costs at most a fixed constant times

\[
 e^{L/4}=R^{1/4}.
 \tag{L-15631.36}
\]

Together with (L-15631.30), this gives the complete unwhitened graph target

\[
 \boxed{
 M_R
 \le
 R^{1/4}\exp(O((\log\log R)^2))
 =R^{1/4+o(1)}.
 }
 \tag{L-15631.37}
\]

In particular,

\[
 \boxed{
 {M_R\log R\over\sqrt R}\longrightarrow0.
 }
 \tag{L-15631.38}
\]

This is exactly the production rate required by `L-15630`.

## 10. Advantages over the guard-mode construction

The differential cardinal construction has four useful features.

1. Every source is `C_c^infinity`; the endpoint/Poisson derivative ledger is
   legitimate at arbitrary fixed order.
2. The ordinary source integral vanishes identically through one fixed
   multiplier, not through a high-mode quotient.
3. Exact interpolation survives smoothing because the sinc zero lattice is
   retained.
4. The two support phases and all branch amplitudes are explicit.

## 11. Proof boundary

- The smoothing, differential correction, exact source constraints, cardinal
  interpolation, polynomial graph estimates, and two-end decomposition are
  complete.
- Equation (L-15631.28) imports the standard local zeta-product/partial-fraction
  normalization and requires independent source review.
- Equation (L-15631.36) must be replayed in the exact production metric,
  including the even-extension convention.
- The theorem supplies the unwhitened graph LMI/rate for `L-15630`; it does not
  determine the finite soft-sector Weil sign and does not prove RH.
