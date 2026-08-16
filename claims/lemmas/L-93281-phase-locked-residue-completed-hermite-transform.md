# L-93281 - Phase locking removes the complete critical-boundary lattice from the cubic-to-Hermite inverse

Claim ID: `L-93281`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93272`; the phase-locked multiplier of PR #520; `L-93280`  
RH status: **not assumed**

## 1. The critical-adjoint multiplier

Put

\[
L=\log4,
\qquad
P(z)=5-4\cos(Lz),
\tag{L-93281.1}
\]

and let

\[
(\mathcal D_Lf)(v)=5f(v)-2f(v-L)-2f(v+L).
\tag{L-93281.2}
\]

Its Fourier multiplier is `P(xi)`. If

\[
z=\frac{s-1/2}{i},
\]
then exactly

\[
\boxed{
P(z)=4(1-4^{s-1})(1-4^{-s}).
}
\tag{L-93281.3}
\]

Thus `P` vanishes simply at

\[
z=\frac{2\pi k}{L}\pm\frac i2,
\qquad k\in\mathbb Z.
\tag{L-93281.4}
\]

For `0<y<1/2`,

\[
P(iy)=5-4\cosh(Ly)>0,
\tag{L-93281.5}
\]

so the multiplier retains every terminal off-line depth.

## 2. Filtered First-Hermite kernels

For `q>0`, let

\[
h_q(v)=\left(1-\frac{v^2}{2q}\right)e^{-v^2/(4q)},
\qquad
\widehat h_q(\xi)=4\sqrt\pi q^{3/2}\xi^2e^{-q\xi^2}.
\tag{L-93281.6}
\]

For an integer `m>=1`, define

\[
h_{q,m}=\mathcal D_L^{2m}h_q,
\qquad
\widehat h_{q,m}(\xi)=P(\xi)^{2m}\widehat h_q(\xi).
\tag{L-93281.7}
\]

Let

\[
k_C(v)=e^{-v/2}W_C(e^{-v})\mathbf1_{v\ge0},
\qquad
\widehat k_C(\xi)=\widehat W_C(1/2+i\xi).
\tag{L-93281.8}
\]

Define `A_(q,m)` by

\[
\boxed{
\widehat A_{q,m}(\xi)
=\frac{P(\xi)^{2m}\widehat h_q(\xi)}
{\widehat k_C(-\xi)}.
}
\tag{L-93281.9}
\]

There is no real-axis singularity. More strongly, put

\[
B_{q,m}(r)=e^{r/2}A_{q,m}(r).
\tag{L-93281.10}
\]

Then

\[
\widehat B_{q,m}(\xi)
=\frac{P(\xi+i/2)^{2m}\widehat h_q(\xi+i/2)}
{\widehat W_C(1-i\xi)}.
\tag{L-93281.11}
\]

The denominator has a double zero at `xi=0` and simple zeros at
`xi=2 pi k/L`, `k!=0`. The numerator `P(xi+i/2)^(2m)` has order `2m` at every
one of those points. Hence every critical-boundary pole is cancelled for
`m>=1`. Gaussian decay then gives

\[
\boxed{B_{q,m}\in\mathcal S(\mathbb R).}
\tag{L-93281.12}
\]

This is the residue completion missing from raw `SID_H`.

## 3. Exact prime-field identity

Define

\[
\mathcal F_C(r,t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}n^{it}
 k_C(r-\log n).
\tag{L-93281.13}
\]

At each fixed `r` the sum is finite. The filtered prime polynomial is

\[
S_{q,m}(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}n^{it}h_{q,m}(\log n).
\tag{L-93281.14}
\]

Fourier inversion and finite summation give

\[
\boxed{
S_{q,m}(t)=\int_{\mathbb R}A_{q,m}(r)\mathcal F_C(r,t)\,dr.
}
\tag{L-93281.15}
\]

Let `F_C^cont` be (R-93280.3) and define the explicit continuous model

\[
S_{q,m}^{\rm cont}(t)
=\int_0^\infty e^{(1/2+it)u}h_{q,m}(u)\,du.
\tag{L-93281.16}
\]

Since

\[
\mathcal G_C(r,t)=e^{-r/2}
\left(\mathcal F_C(r,t)-\mathcal F_C^{\rm cont}(r,t)\right),
\]

we obtain the legal centered identity

\[
\boxed{
S_{q,m}(t)-S_{q,m}^{\rm cont}(t)
=\int_0^\infty B_{q,m}(r)\mathcal G_C(r,t)\,dr.
}
\tag{L-93281.17}
\]

Both factors on the right are in `L2`. No divergent raw-field norm and no
formal contour shift remains.

## 4. Boundary

The theorem closes the carrier normalization and transform interface. It does
not prove the signed covariance in (L-93281.17) is smaller than the filtered
archimedean reserve.
