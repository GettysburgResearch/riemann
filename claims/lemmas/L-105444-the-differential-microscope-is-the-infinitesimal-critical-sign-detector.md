# L-105444 — The differential microscope is the infinitesimal Xi critical-sign detector

Claim ID: `L-105444`  
Status: **PROVED EXACT DIFFERENTIAL LOCALIZER THEOREM**  
Created: 2026-08-24  
Depends on: `L-105429`, `L-105438--L-105442`  
RH status: **not assumed**

## 1. One-height differential field

Fix one derivative order and write

\[
F_r=\Xi^{(r)},
\qquad
m_r={F_r\over F_r'}.
\]

For a base height `b>=0`, put

\[
z=a+i(b+h)
\]

and define

\[
\boxed{
\mathcal C_{r,b}(a,h)
={1\over2}
\left[
 h\operatorname{Re}m_r'(z)
-
\operatorname{Im}m_r(z)
\right].
}
\tag{L-105444.1}

At base zero write `mathcal C_r=mathcal C_(r,0)`.

The field uses one physical height and one adjacent-rung derivative. Every
affine Herglotz carrier `Az+B` cancels exactly.

## 2. Infinitesimal limit of the normalized two-height family

For `lambda>1`, the unique two-height affine-free residue-normalized field is

\[
\mathcal Q_r^{(\lambda)}(a,h)
=-{\lambda^2\over\lambda^2-1}
 \Im m_r(a+ih)
+{\lambda\over\lambda^2-1}
 \Im m_r(a+i\lambda h).
\tag{L-105444.2}

The two constraints are

\[
-\lambda^2+\lambda\cdot\lambda=0
\]

for affine cancellation and

\[
{\lambda^2\over\lambda^2-1}
-{1\over\lambda^2-1}=1
\]

for residue recovery. Taylor expansion in `lambda` gives

\[
\boxed{
\lim_{\lambda\downarrow1}
\mathcal Q_r^{(\lambda)}(a,h)
=
\mathcal C_r(a,h).
}
\tag{L-105444.3}

Thus `mathcal C_r` is the unique infinitesimal member of the minimal
source-independent microscope family.

## 3. Residue recovery and positive kernel

At a simple real critical point,

\[
m_r(c+ih)=-i{\rho_c\over h}+O(1),
\qquad
m_r'(c+ih)={\rho_c\over h^2}+O(1).
\]

Therefore

\[
\boxed{
\lim_{h\downarrow0}h\mathcal C_r(c,h)=\rho_c.}
\tag{L-105444.4}

If the critical poles are real, the contribution of one residue at `c` is

\[
\boxed{
\rho_c
{h^3\over((a-c)^2+h^2)^2}.
}
\tag{L-105444.5}

Hence, under the complete critical sign,

\[
\boxed{
\mathcal C_r(a,h)
=
\sum_{F_r'(c)=0}
\rho_c{h^3\over((a-c)^2+h^2)^2}
\le0.
}
\tag{L-105444.6}

The kernel is strictly positive. Its Fourier transform is

\[
\boxed{
{\pi\over2}(1+h|\xi|)e^{-h|\xi|}>0.
}
\tag{L-105444.7}

## 4. Exact monotonicity coordinate

Put

\[
u_{r,b}(a,h)=\Im m_r(a+i(b+h)).
\]

Then

\[
\boxed{
\mathcal C_{r,b}(a,h)
={h^2\over2}
\partial_h\left({u_{r,b}(a,h)\over h}\right).
}
\tag{L-105444.8}

Therefore

\[
\mathcal C_{r,b}\le0
\]

is exactly the continuous monotonicity statement

\[
{u_{r,b}(a,h)\over h}
\quad\text{is nonincreasing in }h.
\]

If the sampled ratio is holomorphic in `Im z>b`, the safe half-plane gives

\[
\lim_{h\to\infty}{u_{r,b}(a,h)\over h}=0.
\]

Consequently

\[
\boxed{
\mathcal C_{r,b}(a,h)\le0\ \forall a,h
\Longrightarrow
u_{r,b}(a,h)\ge0\ \forall a,h.
}
\tag{L-105444.9}

The strong minimum principle gives strict positivity unless the ratio is
constant. Conversely, a Pick ratio has the Herglotz representation, and each
measure atom contributes the negative kernel in (L-105444.5). Thus

\[
\boxed{
\mathcal C_{r,b}\le0\text{ everywhere}
\Longleftrightarrow
m_r\text{ is Pick in }\Im z>b,
}
\tag{L-105444.10}

with holomorphy/finiteness retained.

## 5. Zero-height variational formula

Let `beta_r` be the upper zero height of `F_r`. By `L-105442` and the
continuous characterization above,

\[
\boxed{
\beta_r
=
\inf\left\{
 b\ge0:
 \begin{array}{l}
 m_r\text{ is holomorphic in }\Im z>b,\\
 \mathcal C_{r,b}(a,h)\le0\quad\forall a,h>0
 \end{array}
\right\}.
}
\tag{L-105444.11}

At `r=0`, the right side vanishes exactly under RH.

## 6. Local off-line-zero calibration

Let `z_0=a_0+i\beta` be a simple zero of `F_r`, and choose

\[
b=\beta-\delta.
\]

Since

\[
m_r(z)=z-z_0+O((z-z_0)^2),
\qquad
m_r'(z)=1+O(z-z_0),
\]

one obtains

\[
\boxed{
\mathcal C_{r,b}(a_0,h)
={\delta\over2}+O(h^2+\delta^2).
}
\tag{L-105444.12}

Thus a simple off-line zero creates positive differential-microscope mass with
universal transverse slope `1/2` immediately below its height.

## 7. Adjacent-rung expression

The exact identity

\[
m_r'=1-
{F_rF_{r+2}\over F_{r+1}^2}
\]

gives

\[
\boxed{
\mathcal C_{r,b}(a,h)
={1\over2}
\left[
 h\left(1-\Re{F_rF_{r+2}\over F_{r+1}^2}(z)\right)
-\Im m_r(z)
\right].
}
\tag{L-105444.13}

This is the one-point conclusion-facing consumer for adjacent-derivative
ratio estimates.

## 8. Scale flow

For a signed real critical measure, the multiplier in (L-105444.7) gives

\[
\boxed{
\partial_h\mathcal C_r
=-|D|{h|D|\over I+h|D|}\mathcal C_r,
}
\tag{L-105444.14}

and

\[
\boxed{
(\partial_h+|D|)^2\mathcal C_r=0.
}
\tag{L-105444.15}

Increasing `h` is dissipative. The RH-bearing base-height descent remains the
opposite, unstable direction.

## 9. Scope

The theorem does not prove `mathcal C_(0,0)<=0`. It replaces the minimal
two-height field by its exact one-height differential limit and exposes one
adjacent-rung ratio at one point.
