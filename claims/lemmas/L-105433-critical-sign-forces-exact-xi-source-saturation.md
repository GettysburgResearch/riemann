# L-105433 — The Xi critical sign forces exact source–critical saturation

Claim ID: `L-105433`  
Status: **PROVED CONDITIONAL SUM-RULE THEOREM — ASSUMES L-105432 HYPOTHESES**  
Created: 2026-08-24  
Depends on: `L-105370`, `L-105417`, `L-105430`, `L-105432`  
RH status: **not assumed**

## 1. Setup

Let

\[
F=\Xi^{(r)}
\]

and assume every zero of `F'` is real, every nonremovable critical pole is
simple, and

\[
\rho_c={F(c)\over F''(c)}\le0.
\]

Use the regularized odd ratio

\[
\widehat m_F(z)=
\begin{cases}
F(z)/F'(z),&F\text{ odd},\\[1mm]
F(z)/F'(z)-\rho_0/z,&F\text{ even}.
\end{cases}
\]

Write

\[
\widehat m_F(z)=z\sum_{n\ge0}a_n(F)z^{2n}
\]

at the origin.

By `L-105432`, `F/F'` is Pick. Therefore `L-105417` gives

\[
\widehat m_F(z)
=az+
\sum_{c>0}W_c{z\over1-s_cz^2},
\qquad
W_c=-{2\rho_c\over c^2}\ge0,
\quad
s_c=c^{-2},
\quad a\ge0.
\tag{L-105433.1}
\]

## 2. The affine coefficient is zero

On the positive imaginary axis, `L-105430` gives, in the coordinate
`s=1/2+y`,

\[
{F(iy)\over F'(iy)}
={i\over L(s)}
\left(1+O_r(|L(s)|^{-2})\right),
\qquad
L(s)={1\over2}\log {s\over2\pi}+o(1).
\tag{L-105433.2}
\]

Hence

\[
\boxed{
\operatorname{Im}{F(iy)\over F'(iy)}
=O_r\!\left({1\over\log(2+y)}\right),
}
\tag{L-105433.3}
\]

and the central even regularization changes this by only `O(1/y)`. For a
Herglotz function, the affine coefficient is

\[
a=\lim_{y\to\infty}{\operatorname{Im}\widehat m_F(iy)\over y}.
\]

Therefore

\[
\boxed{a=0.}
\tag{L-105433.4}
\]

There is no source mass at the reciprocal-square endpoint `s=0`.

## 3. Exact source measure

Equation (L-105433.1) becomes

\[
\boxed{
\widehat m_F(z)
=
\sum_{c>0}
\left(-{2\rho_c\over c^2}\right)
{z\over1-z^2/c^2}.
}
\tag{L-105433.5}
\]

The symmetric series converges locally uniformly away from the critical
poles. Thus the complete source Stieltjes measure is exactly

\[
\boxed{
\nu_{\rm source}
=
\sum_{c>0}
\left(-{2\rho_c\over c^2}\right)
\delta_{1/c^2}.
}
\tag{L-105433.6}
\]

There is no terminal affine remainder and no missing endpoint atom.

## 4. Complete moment sum rules

Comparing Taylor coefficients at the origin gives, for every `n>=0`,

\[
\boxed{
 a_n(F)
=
\sum_{c>0}
{-2\rho_c\over c^{2n+2}}.
}
\tag{L-105433.7}
\]

For odd `F`, `a_0=1`, so the first exact sum rule is

\[
\boxed{
\sum_{c>0}{-2\rho_c\over c^2}=1.
}
\tag{L-105433.8}
\]

For even `F`, the same statement holds with the regularized coefficient
`a_0(F)` of `L-105381`.

At every finite matrix order,

\[
\boxed{
\mathsf A_k^{(a)}(F)
=
\mathsf C_{k,\infty}^{(a)}(F),
\qquad a=0,1.
}
\tag{L-105433.9}
\]

Thus the normalized complete critical-capacity operator is exactly the
identity whenever the source matrix is invertible.

## 5. Finite-window boundary reserve

For a symmetric finite window `Omega`, the exact source split becomes

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}
=
\sum_{\substack{c>0\\c\notin\Omega}}
W_cs_c^a v_k(s_c)v_k(s_c)^T
\succeq0.
}
\tag{L-105433.10}
\]

The boundary reserve is literally the omitted positive critical tail. This is
the Xi analogue of the exact sine/cosine saturation theorem `L-105382`.

In particular, the scalar endpoint gate is saturated:

\[
\boxed{
\widehat a_0-
\sum_{c>0}W_c=0.
}
\tag{L-105433.11}
\]

## 6. Meaning and scope

Once the complete critical sign is known, none of the following is an
independent theorem:

```text
ZCAP105412;
remote-tail moment matching;
terminal affine reserve;
all-order source-critical capacity;
all-packet boundary Loewner positivity.
```

They are exact consequences of the pure atomic Herglotz representation.

The theorem does not prove the critical sign. Without nonpositive residues the
right side of (L-105433.6) is a signed measure and the conclusion-facing
positivity is lost.
