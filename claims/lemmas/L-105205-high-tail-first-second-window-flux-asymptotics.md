# L-105205 — Both critical-residue window fluxes are asymptotically Gaussian in the Xi high tail

Claim ID: `L-105205`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200--L-105204`; PR #723 `L-105101`  
RH status: **not assumed**

## 1. Regular buffered rectangles

Fix

\[
0<C_0<C_1,
\qquad 0<\eta<H.
\]

For `m>=M`, let

\[
F_m=\Xi^{(m)}
\]

and use the larger natural box

\[
|\Re z|\le C_1\sqrt{M/\log M},
\qquad |\Im z|\le H.
\]

By `L-105201`, every zero of `F_m'` and `F_m''` there is real and simple for
large `M`. Choose a regular vertical edge `T_(m,M)` satisfying

\[
C_0\sqrt{M/\log M}
\le T_{m,M}
\le C_0\sqrt{M/\log M}+{\pi\over w_m},
\tag{L-105205.1}
\]

and separated by `c/w_m` from the model zeros of both the first and second
derivatives. The Gaussian approximation and Rouché localization then give the
same separation from the actual zeros after reducing `c` once. The horizontal
edges at `Im z=+-eta` contain no derivative zero because every zero in the
larger box is real.

Let

\[
R_m=\#\{c\in(-T_{m,M},T_{m,M}):F_m'(c)=0\}.
\]

Then

\[
R_m={2w_mT_{m,M}\over\pi}+O(1).
\tag{L-105205.2}
\]

## 2. First flux

Let

\[
B_{1,m}
={1\over2\pi i}
\int_{\partial\Omega_{T_{m,M},\eta}}
{F_m(z)\over F_m'(z)}\,dz.
\]

There is no nonreal `F_m'` zero in the rectangle. Hence `L-105204.6` and the
residue asymptotic `L-105202` give

\[
\boxed{
B_{1,m}
=-{R_m\over w_m^2}(1+o(1)).
}
\tag{L-105205.3}
\]

The error is uniform for every `m>=M`.

## 3. Adjacent-derivative debt is lower order

The second flux of `L-105101` contains the debt

\[
D_m
=
\sum_{F_m''(d)=0}
{F_m(d)^2\over F_m'(d)F_m'''(d)},
\tag{L-105205.4}
\]

with the sum over zeros in the same rectangle.

Consider the Gaussian trigonometric model

\[
f(x)=e^{-v x^2/2}\chi(wx),
\qquad v=s_m^2,
]

where `chi` is sine or cosine. Write

\[
r={\chi'(wx)\over\chi(wx)}.
\]

At a real zero of `f''`, the exact equation is

\[
-v-w^2+v^2x^2-2vwxr=0.
\tag{L-105205.5}
\]

On the natural box, `vx^2=O(1)` and `v/w^2=o(1)`. Equation (L-105205.5)
therefore implies

\[
|\chi(wx)|\ll {\sqrt v\over w},
\qquad
|f'(x)|\asymp w e^{-vx^2/2},
\qquad
|f'''(x)|\asymp w^3e^{-vx^2/2}.
\tag{L-105205.6}
\]

The order-three approximation `L-105200.10` transfers these estimates to
`F_m` at every actual zero of `F_m''`, with an additional relative error
`delta_M=o(1)`. Consequently each debt residue satisfies

\[
\left|
{F_m(d)^2\over F_m'(d)F_m'''(d)}
\right|
\ll
{(\delta_M+\sqrt v/w)^2\over w^4}.
\tag{L-105205.7}
\]

There are `O(R_m)` such zeros. Hence

\[
\boxed{
D_m=o\!left({R_m\over w_m^4}\right)
}
\tag{L-105205.8}
\]

uniformly for `m>=M`.

The estimate uses the exact debt rather than assuming a sign. In the pure
monochromatic limit the debt singularities are removable, and (L-105205.8)
quantifies that degeneration.

## 4. Second flux

Put

\[
B_{2,m}
={1\over2\pi i}
\int_{\partial\Omega_{T_{m,M},\eta}}
{F_m(z)^2\over F_m'(z)F_m''(z)}\,dz.
\]

There are no nonreal `F_m'` zeros in the rectangle, so the correction
`C_(2,F)` of `L-105101` vanishes. The exact identity is

\[
M_{2,m}=B_{2,m}-D_m.
\]

By `L-105202` and (L-105205.8),

\[
\boxed{
B_{2,m}
={R_m\over w_m^4}(1+o(1)).
}
\tag{L-105205.9}

uniformly for `m>=M`.

## 5. Direct contour coherence

Combining (L-105205.3) and (L-105205.9),

\[
\boxed{
{B_{1,m}^2\over R_m B_{2,m}}
=1-o(1).
}
\tag{L-105205.10}

Thus the asymptotically optimal residue coherence can be read directly from
the two oriented rectangle fluxes. The nonreal squared-residue correction is
zero in the high tail, and the adjacent-derivative debt is lower order.

## 6. Scope

The vertical edge is selected separately for each derivative order inside one
model cell. This theorem does not yet provide a single common vertical edge
for a long low-order derivative ladder. It evaluates the exact PR #723 window
fluxes in the high tail; it does not bound the fixed-order fluxes occurring in
`CRDB105200` and does not prove RH.
