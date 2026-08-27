# L-105600 — The Herglotz hyperbolic derivative is a unit-phase barycenter

Claim ID: `L-105600`  
Status: **PROVED EXACT PICK-THEORETIC IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105417`, `L-105442`, `L-105451`  
RH status: **not assumed**

## 1. Herglotz setup

Let `f` be a nonconstant Pick function on the upper half-plane, with the
real-symmetric Herglotz representation

\[
f(z)=\alpha z+\beta+
\int_{\mathbb R}
\left({1\over t-z}-{t\over1+t^2}\right)d\mu(t),
\qquad
\alpha\ge0,
\quad \mu\ge0.
\tag{L-105600.1}
\]

Fix

\[
z=a+iy,
\qquad y>0,
\qquad v=\operatorname{Im}f(z)>0.
\]

Define a probability measure `P_z` on the one-point compactification
`R union {infinity}` by

\[
\boxed{
\mathbb P_z(\{\infty\})={\alpha y\over v},
\qquad
 d\mathbb P_z(t)
 ={y\over v((t-a)^2+y^2)}\,d\mu(t).
}
\tag{L-105600.2}
\]

The total mass is one because the numerator is exactly `Im f(z)`.

For finite `t`, put

\[
\boxed{
\omega_z(t)={t-\overline z\over t-z},
\qquad
\omega_z(\infty)=1.
}
\tag{L-105600.3}
\]

Every `omega_z(t)` lies on the unit circle.

## 2. Exact phase-barycenter formula

Define the hyperbolic derivative

\[
\boxed{
\mathfrak d_f(z)
={y f'(z)\over\operatorname{Im}f(z)}.
}
\tag{L-105600.4}
\]

Since

\[
{t-\overline z\over t-z}
{y\over(t-a)^2+y^2}
={y\over(t-z)^2},
\]

the Herglotz formula gives

\[
\boxed{
\mathfrak d_f(z)
=\mathbb E_z\,\omega_z.
}
\tag{L-105600.5}
\]

Thus the Schwarz--Pick contraction is literally the statement that a
barycenter of unit phases lies in the closed unit disk.

The complete defect has the exact variance form

\[
\boxed{
1-|\mathfrak d_f(z)|^2
={1\over2}
\mathbb E_{z,t,s}
|\omega_z(t)-\omega_z(s)|^2.
}
\tag{L-105600.6}
\]

The directional defect toward the affine phase `1` is

\[
\boxed{
1-\operatorname{Re}\mathfrak d_f(z)
={1\over2}\mathbb E_z|\omega_z-1|^2.
}
\tag{L-105600.7}
\]

## 3. The differential microscope is the phase reserve

Use the differential microscope

\[
\mathcal C_f(a,y)
={1\over2}
\left[y\operatorname{Re}f'(a+iy)
      -\operatorname{Im}f(a+iy)\right].
\]

Equations (L-105600.4)--(L-105600.7) give

\[
\boxed{
\mathcal C_f(a,y)
={v\over2}
\left(\operatorname{Re}\mathfrak d_f(z)-1\right)
=-{v\over4}\mathbb E_z|\omega_z-1|^2.
}
\tag{L-105600.8}
\]

Since

\[
|\omega_z(t)-1|^2
={4y^2\over(t-a)^2+y^2},
\]
this is exactly the Newton formula of `L-105451`:

\[
\boxed{
\mathcal C_f(a,y)
=-y^3\int_{\mathbb R}
{d\mu(t)\over((t-a)^2+y^2)^2}.
}
\tag{L-105600.9}
\]

The phase-gap, Schwarz--Pick and six-dimensional Newton descriptions are
therefore the same positive reserve.

## 4. Exact moving-base threshold

Let `beta` be a reference base and suppose

\[
f(w)=m(w+i\beta)
\]

is Pick. Descend to

\[
b=\beta-\delta,
\qquad \delta>0.
\]

At physical scale `h>delta`, put

\[
y=h-\delta,
\qquad z=a+iy.
\]

The lower-base differential field is

\[
\mathcal C_b(a,h)
={1\over2}
\left[h\operatorname{Re}f'(z)-\operatorname{Im}f(z)\right].
\]

Hence

\[
\boxed{
{2\mathcal C_b(a,h)\over v}
=\left(1+{\delta\over y}\right)
 \operatorname{Re}\mathfrak d_f(z)-1.
}
\tag{L-105600.10}
\]

Consequently

\[
\boxed{
\mathcal C_b(a,h)\le0
\iff
\operatorname{Re}\mathfrak d_f(a+iy)
\le {y\over y+\delta}.
}
\tag{L-105600.11}
\]

A nonnegative lower-base contact forces the phase reserve to collapse:

\[
\boxed{
\mathbb E_z|\omega_z-1|^2
\le {2\delta\over y+\delta}.
}
\tag{L-105600.12}
\]

Equality holds at a zero contact.

## 5. Local Herglotz evacuation

For any fixed `R>0`, on `|t-a|<=Ry` one has

\[
|\omega_z(t)-1|^2
\ge {4\over1+R^2}.
\]

Therefore every nonnegative contact obeys

\[
\boxed{
\mathbb P_z\{|t-a|\le Ry\}
\le
{1+R^2\over2}
{\delta\over y+\delta}.
}
\tag{L-105600.13}
\]

Thus a contact with `delta/y -> 0` is possible only if the normalized
Herglotz measure evacuates every fixed local window around the contact centre.
Equivalently, every unit phase in the barycenter aligns with the affine phase
`1`.

## 6. Automorphism blow-up

Normalize the Pick map at `z=a+iy` by

\[
\boxed{
F_z(\zeta)
={f(a+y\zeta)-\operatorname{Re}f(z)
 \over\operatorname{Im}f(z)}.
}
\tag{L-105600.14}
\]

Then `F_z` maps the upper half-plane to itself,

\[
F_z(i)=i,
\qquad
F_z'(i)=\mathfrak d_f(z).
\]

For a sequence of nonnegative contacts with `delta_n/y_n -> 0`,
(L-105600.12) implies

\[
\mathfrak d_f(a_n+iy_n)\longrightarrow1.
\]

The normalized Pick family is normal. Every subsequential limit fixes `i` and
has derivative one there, so equality in Schwarz--Pick forces the identity.
Hence

\[
\boxed{
F_{a_n+iy_n}\longrightarrow\operatorname{id}
}
\tag{L-105600.15}
\]

locally uniformly in the upper half-plane.

This is the exact macroscopic spatial-escape alternative: a shallow base
contact can occur only through an affine/Mobius local limit and complete local
phase collapse.

## 7. Xi specialization

For

\[
m_r={\Xi^{(r)}\over\Xi^{(r+1)}}
\]

and the maximal zero height `beta_r`, `L-105442` makes

\[
f_{r,\beta}(w)=m_r(w+i\beta_r)
\]

Pick in the upper half-plane. The completed-zeta safe asymptotic gives

\[
{f_{r,\beta}(iy)\over iy}\longrightarrow0,
\]
so its affine Herglotz coefficient is zero.

The remaining zero-height/spatial-escape problem is therefore a source-specific
lower bound on the phase variance in (L-105600.7), not an untyped determinant
or arbitrary maximum-principle problem.

## 8. Scope

The lemma does not supply that lower bound. Generic Pick functions can have
arbitrarily small phase variance at remote points. The Xi-specific producer
must come from the reciprocal Dirichlet source, the one-sided Hardy phase gap,
or an equivalent translation-sensitive estimate. RH remains unproved.
