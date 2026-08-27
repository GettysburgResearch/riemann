# L-105446 — The differential microscope is a six-dimensional Newton potential

Claim ID: `L-105446`  
Status: **PROVED EXACT ELLIPTIC STRUCTURE AND FINITE-CONTACT EXCLUSION**  
Created: 2026-08-24  
Depends on: `L-105429`, `L-105442--L-105445`  
RH status: **not assumed**

## 1. Differential field at a moving base

Fix `r>=0`, put

\[
F_r=\Xi^{(r)},
\qquad
m_r={F_r\over F_r'},
\]

and work in a pole-free region of the shifted upper half-plane. For a base
`b>=0`, write

\[
u_b(a,h)=\Im m_r(a+i(b+h)),
\qquad h>0,
\]

and

\[
\boxed{
\mathcal C_b(a,h)
={1\over2}\left[h\,\partial_hu_b(a,h)-u_b(a,h)\right].
}
\tag{L-105446.1}
\]

This is `L-105444.1`. Since `u_b` is harmonic,

\[
\partial_a^2u_b+\partial_h^2u_b=0.
\tag{L-105446.2}
\]

## 2. Exact elliptic equation

Differentiate (L-105446.1). One has

\[
\partial_h\mathcal C_b
={h\over2}\partial_h^2u_b
\tag{L-105446.3}
\]

and

\[
\partial_a^2\mathcal C_b
={1\over2}
\left[h\partial_h\partial_a^2u_b-\partial_a^2u_b\right].
\]

Using (L-105446.2) and its `h` derivative gives

\[
\boxed{
\partial_a^2\mathcal C_b
+
\partial_h^2\mathcal C_b
-
{2\over h}\partial_h\mathcal C_b
=0.
}
\tag{L-105446.4}

This identity is valid before any critical-point reality or sign theorem. It
uses only holomorphy of the sampled ratio.

## 3. Six-dimensional harmonic lift

Define

\[
\boxed{
\mathcal W_b(a,h)={\mathcal C_b(a,h)\over h^3}.
}
\tag{L-105446.5}

Substitution in (L-105446.4) gives

\[
\boxed{
\partial_a^2\mathcal W_b
+
\partial_h^2\mathcal W_b
+
{4\over h}\partial_h\mathcal W_b
=0.
}
\tag{L-105446.6}

Let `y in R^5`, `h=|y|`, and put

\[
\widetilde{\mathcal W}_b(a,y)
=\mathcal W_b(a,|y|).
\]

Then

\[
\boxed{
\Delta_{\mathbb R^6}\widetilde{\mathcal W}_b=0
}
\tag{L-105446.7}

away from the lifted pole set. Thus the conclusion-facing Xi field is not
merely analogous to a potential: after one exact weight it is an ordinary
six-dimensional harmonic function.

## 4. Critical residues are literal Newton charges

On the real-critical stratum, one pole

\[
m_r(z)={\rho_c\over z-c}+\text{holomorphic}
\]

contributes, by `L-105444`,

\[
\mathcal C_0(a,h)
=
\rho_c{h^3\over((a-c)^2+h^2)^2}.
\]

Therefore

\[
\boxed{
\mathcal W_0(a,h)
={\rho_c\over((a-c)^2+h^2)^2}.
}
\tag{L-105446.8}

The right side is the six-dimensional Newton kernel, restricted to axial
coordinates. Negative critical residues are negative point charges; a positive
residue is a positive Newton charge. The former residue-sign and differential
microscope languages are therefore exactly the same potential theory.

At a regular real point `a`, Taylor expansion of the real analytic boundary
value gives

\[
\Im m_r(a+ih)
=h m_r'(a)-{h^3\over6}m_r'''(a)+O(h^5),
\]

\[
\Re m_r'(a+ih)
=m_r'(a)-{h^2\over2}m_r'''(a)+O(h^4).
\]

Hence

\[
\boxed{
\lim_{h\downarrow0}\mathcal W_0(a,h)
=-{1\over6}m_r'''(a).
}
\tag{L-105446.9}

Thus regular zero-height injection is the third derivative of the reciprocal
field, while critical poles are point charges on the same axis.

## 5. The Xi anchor is strict at every base

Let

\[
U_r(y)=\Im m_r(iy)>0.
\]

`L-105445` proves that

\[
{U_r(y)\over y}
\quad\text{is strictly decreasing on }(0,\infty),
\]

so

\[
yU_r'(y)-U_r(y)<0.
\tag{L-105446.10}

For a shifted base, put `y=b+h`. Then

\[
2\mathcal C_b(0,h)=hU_r'(y)-U_r(y).
\]

If `U_r'(y)>=0`, then `h<=y` and (L-105446.10) gives

\[
hU_r'(y)-U_r(y)
\le yU_r'(y)-U_r(y)<0.
\]

If `U_r'(y)<0`, both terms on the left are already strictly negative. Hence

\[
\boxed{
\mathcal C_{r,b}(0,h)<0
\qquad(b>=0,\ h>0).
}
\tag{L-105446.11}

The positive Xi Fourier source therefore pins one strictly negative axial line
through every base-height problem, not only the base-zero problem treated in
`L-105445`.

## 6. No finite interior first contact

Fix a base `b` for which `m_r` is holomorphic throughout `Im z>b`. Suppose

\[
\mathcal C_b(a,h)\le0
\qquad(a\in\mathbb R,\ h>0)
\]

and equality occurs at one finite interior point `(a_*,h_*)`.

On every compact neighbourhood of that point, (L-105446.4) is a uniformly
elliptic equation with smooth first-order coefficient. The strong maximum
principle implies that `mathcal C_b` is identically zero on the connected
pole-free half-plane. This contradicts the strict source anchor
(L-105446.11). Therefore

\[
\boxed{
\mathcal C_b\le0
\quad\Longrightarrow\quad
\mathcal C_b<0
\text{ at every finite interior point.}
}
\tag{L-105446.12}

In particular, as the base descends from the unconditional safe region, the
first loss of the global differential inequality cannot be a finite smooth
zero contact. The contact-curvature target `ACCR105443` is not needed for that
mechanism.

## 7. Coarse scale cannot be the entry point

The completed-zeta estimate of `L-105430` gives, uniformly in real `a` and in
bounded bases `0<=b<=1/2`,

\[
\Im m_r(a+i(b+h))
=
\Re {1\over L(s)}+O_r(|L(s)|^{-3})
\]

with `Re L(s)->infinity` as `h->infinity`. Differentiating the same safe-line
expansion once gives

\[
\boxed{
\mathcal C_{r,b}(a,h)
=-{1\over2}\Re {1\over L(s)}
+O_r(|L(s)|^{-2})<0
}
\tag{L-105446.13}

for all sufficiently large `h`, uniformly in `a` and `b in [0,1/2]`.

Thus failure cannot enter from `h=infinity`.

## 8. Exact first-failure trichotomy

Combine Sections 6--7 with the zero-height variational principle. During
base descent, every genuine first obstruction must enter through at least one
of:

```text
pole:            a zero of Xi^(r+1) reaches the sampled half-plane;
zero-height axis: h tends to zero at a zero/positive boundary charge of Xi^r;
spatial escape:  |a| tends to infinity while h remains bounded.
```

There is no fourth mechanism consisting of a finite smooth contact in
`(a,h)`.

Moreover, `beta_(r+1)<=beta_r`. Hence a denominator pole cannot occur at a
base strictly above the first parent-zero height. It can only be co-terminal
with, or below, the zero-height obstruction. If the supremal zero height is
attained at finite real part, the parent zero is the first obstruction. If it
is not attained, the only remaining form is zero-height injection escaping to
`|a|=infinity`.

## 9. Scope

This theorem does not rule out the zero-height or spatial-escape alternatives.
Those alternatives are the actual RH-bearing content. It removes the finite
contact-curvature programme from the conclusion-facing graph and identifies
the differential microscope as a classical Newton potential with a strictly
negative Xi source anchor.