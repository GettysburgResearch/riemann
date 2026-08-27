# L-105442 — The minimal microscope is an exact zero-height variational principle

Claim ID: `L-105442`  
Status: **PROVED EXACT XI-DERIVATIVE ZERO-HEIGHT CHARACTERIZATION**  
Created: 2026-08-24  
Depends on: `L-105429`, `L-105438`  
RH status: **not assumed**

## 1. Shifted-base microscope

Fix `r>=0` and put

\[
F_r=\Xi^{(r)},
\qquad
m_r={F_r\over F_r'}.
\]

For a base height `b>=0`, define

\[
\boxed{
\mathcal Q_{r,b}(a,h)
=-{4\over3}\Im m_r(a+i(b+h))
+{2\over3}\Im m_r(a+i(b+2h)),
}
\tag{L-105442.1}

whenever both sampled values are finite.

Define the upper zero height

\[
\boxed{
\beta_r
=\sup\{\Im z:F_r(z)=0\}
\in[0,1/2].
}
\tag{L-105442.2}

The interval bound is `L-105429`; conjugation symmetry makes the supremum
nonnegative.

## 2. Pick above a zero-free horizontal line

If `b>=beta_r`, every zero `tau` of `F_r` satisfies `Im tau<=b`. The paired
logarithmic derivative gives, for `Im z>b`,

\[
\Im {F_r'(z)\over F_r(z)}<0.
\]

Hence

\[
\boxed{
\Im m_r(z)>0
\qquad(\Im z>b).
}
\tag{L-105442.3}

Thus the translated function

\[
f_b(w)=m_r(w+ib)
\]

is a Herglotz--Pick function on the upper half-plane.

Its representation is

\[
f_b(w)=A_bw+B_b+
\int_{\mathbb R}
\left({1\over t-w}-{t\over1+t^2}\right)d\mu_b(t),
\]

where `A_b>=0`, `B_b` is real and `mu_b>=0`. Therefore

\[
\Im f_b(a+ih)
=A_bh+
\int {h\over(t-a)^2+h^2}\,d\mu_b(t).
\]

The affine term cancels from (L-105442.1), while each measure atom contributes
minus the positive kernel of `L-105438`. Hence

\[
\boxed{
\mathcal Q_{r,b}(a,h)\le0
\qquad(a\in\mathbb R,\ h>0).
}
\tag{L-105442.4}

Both sampled denominators are automatically nonzero.

## 3. Dyadic converse

Conversely, assume that for one base `b` the two sampled ratios are finite and

\[
\mathcal Q_{r,b}(a,h)\le0
\]

for every `a,h`. Put

\[
u_a(h)=\Im m_r(a+i(b+h)).
\]

The inequality is exactly

\[
\boxed{u_a(h)\ge{1\over2}u_a(2h).}
\tag{L-105442.5}

Choose `n` so large that `b+2^nh>1/2`. By `L-105429`,

\[
u_a(2^nh)>0.
\]

Iterating (L-105442.5) gives

\[
\boxed{u_a(h)\ge2^{-n}u_a(2^nh)>0.}
\tag{L-105442.6}

Thus `m_r` is Pick throughout `Im z>b`. In particular it cannot vanish there.
Every zero of `F_r` in that half-plane would be a zero of `m_r`, because the
finiteness hypothesis already excludes a simultaneous denominator pole.
Therefore

\[
\beta_r\le b.
\]

## 4. Exact variational formula

Sections 2--3 prove

\[
\boxed{
\beta_r
=
\inf\left\{
 b\ge0:
 \begin{array}{l}
 m_r(a+i(b+h)),m_r(a+i(b+2h))\text{ are finite},\\
 \mathcal Q_{r,b}(a,h)\le0
 \quad\forall a\in\mathbb R,\ h>0
 \end{array}
\right\}.
}
\tag{L-105442.7}

The infimum may be read with `b>beta_r` and then closed by monotone limiting;
zeros on the boundary do not affect the open half-plane assertion.

At the base rung,

\[
\boxed{
\beta_0=0
\Longleftrightarrow
\mathrm{RH}.}
\tag{L-105442.8}

Since `beta_0<=1/2` unconditionally, RH is exactly the descent of the shifted
minimal field from base `1/2` to base `0`.

## 5. Local detection of a zero above the base

Let `z_0=a_0+i\beta` be a simple zero of `F_r`, and choose a base

\[
b=\beta-\delta,
\qquad\delta>0.
\]

Locally,

\[
m_r(z)=z-z_0+O((z-z_0)^2).
\]

Therefore, whenever `h,delta` are small enough for both sample points to stay
in the local disk,

\[
\boxed{
\mathcal Q_{r,b}(a_0,h)
={2\over3}\delta+O(h^2+\delta^2)>0.
}
\tag{L-105442.9}

This holds on a suitable subcone such as `h` comparable to `delta`. Thus a
nonreal zero is not merely excluded abstractly by the Pick property: it
creates a positive minimal-microscope contact immediately below its height.

A nonreal zero of `F_r'` instead appears as a pole in one sampled ratio. These
are the two first-obstruction types of `T-105441`.

## 6. Derivative ladder

Gauss--Lucas/Hurwitz gives

\[
\boxed{\beta_{r+1}\le\beta_r.}
\tag{L-105442.10}

Thus the Xi derivative ladder has an exact nonincreasing sequence of microscope
base heights. High-derivative local real-rootedness controls this height only
in the corresponding finite real window; it does not prove the global height
vanishes.

## 7. Scope

The variational formula is equivalent to the zero-height problem and does not
prove `beta_0=0`. Its advance is to replace every global outer-boundary and
critical-capacity matrix by one scalar dyadic inequality with a geometric base
parameter in the compact interval `[0,1/2]`.
