# L-105351 — The symmetric Xi boundary gate is one origin Stieltjes moment problem

Claim ID: `L-105351`  
Status: **PROVED EXACT COORDINATE REDUCTION — XI SIGN HIERARCHY OPEN**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`, `L-105329`, `L-105350`  
RH status: **not assumed**

## 1. Symmetric boundary Cauchy function

Let `F` be entire, real on the real axis, and of definite parity. Let `\Omega`
be a bounded conjugation- and parity-symmetric Jordan domain, regular for
`F'`, and containing the origin. Put

\[
m_F(z)={F(z)\over F'(z)}
\]

and define the boundary Cauchy function

\[
\boxed{
H_{F,\Omega}(z)
={1\over2\pi i}
\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta.
}
\tag{L-105351.1}
\]

Since `F/F'` is odd and the contour is invariant under `\zeta\mapsto-\zeta`,

\[
\boxed{H_{F,\Omega}(-z)=-H_{F,\Omega}(z).}
\tag{L-105351.2}
\]

Thus

\[
H_{F,\Omega}(z)=
\sum_{n\ge0}\beta_n(F;\Omega)z^{2n+1}
\tag{L-105351.3}
\]

near the origin, where

\[
\boxed{
\beta_n(F;\Omega)
={H_{F,\Omega}^{(2n+1)}(0)\over(2n+1)!}
={1\over2\pi i}
\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta.
}
\tag{L-105351.4}
\]

These are literal source-owned contour moments. No packet nodes or adaptive
interpolation points occur.

## 2. Parity splitting of the one-anchor hierarchy

For `H=H_{F,\Omega}` and anchor zero, the Hamburger sequence of `L-105350` is

\[
m_{2n}=\beta_n,
\qquad
m_{2n+1}=0.
\tag{L-105351.5}
\]

After separating even and odd polynomial powers, every confluent Hankel matrix
is permutation-congruent to the two blocks

\[
\boxed{
\mathsf S_k^{(0)}
=\bigl[\beta_{r+s}\bigr]_{r,s=0}^{k-1},
\qquad
\mathsf S_k^{(1)}
=\bigl[\beta_{r+s+1}\bigr]_{r,s=0}^{k-1}.
}
\tag{L-105351.6}
\]

Consequently,

\[
\boxed{
\mathscr L_{H_{F,\Omega}}\succeq0
\text{ on every finite real packet}
\iff
\mathsf S_k^{(0)}\succeq0
\text{ and }
\mathsf S_k^{(1)}\succeq0
\quad(k\ge1).
}
\tag{L-105351.7}
\]

The two families are exactly the Stieltjes moment criterion.

## 3. Positive Stieltjes representation

The equivalent conditions in (L-105351.7) hold if and only if there is a
finite positive compactly supported measure `\nu` on `[0,\infty)` such that

\[
\boxed{
\beta_n(F;\Omega)=
\int_{[0,\infty)}s^n\,d\nu(s),
\qquad n\ge0.
}
\tag{L-105351.8}
\]

In that case

\[
\boxed{
{H_{F,\Omega}(z)\over z}
=
\int_{[0,\infty)}
{d\nu(s)\over1-sz^2}
}
\tag{L-105351.9}
\]

near zero and, by analytic continuation, throughout the common domain.

One proof is to apply `L-105350` and use uniqueness of the compact Hamburger
measure. Oddness of `H` forces that measure to be symmetric under
`t\mapsto-t`; pushing it forward by `s=t^2` gives `\nu`. Conversely, the two
positive Hankel families give a Stieltjes measure, whose symmetric square-root
lift gives the Hamburger representation of `L-105350`.

## 4. Safe-axis Stieltjes transform

For real `y` in the safe imaginary-axis segment,

\[
\boxed{
{H_{F,\Omega}(iy)\over iy}
={1\over2\pi i}
\int_{\partial\Omega}
{F(\zeta)/F'(\zeta)\over\zeta^2+y^2}\,d\zeta.
}
\tag{L-105351.10}
\]

This follows by subtracting the Cauchy formulas at `iy` and `-iy` and using
oddness. Under (L-105351.8),

\[
\boxed{
{H_{F,\Omega}(iy)\over iy}
=
\int_{[0,\infty)}
{d\nu(s)\over1+s y^2}.
}
\tag{L-105351.11}
\]

Hence it is a Stieltjes function of `y^2`; in particular,

\[
(-1)^j{d^j\over d(y^2)^j}
\left[{H_{F,\Omega}(iy)\over iy}ight]\ge0
\qquad(j\ge0).
\tag{L-105351.12}
\]

The derivative inequalities are equivalent to the positive measure only when
the complete analytic/moment conditions are retained; finitely many signs are
not enough.

## 5. Xi boundary gate

For `F=\Xi^{(k)}` in the parity-symmetric canonical exhaustion, define

```text
OASH105350:
  for every regular window and every order j>=1, both origin matrices
  S_j^(0)=[beta_(r+s)] and S_j^(1)=[beta_(r+s+1)] are PSD.
```

Then `L-105350` and (L-105351.7) give

\[
\boxed{
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}
}
\tag{L-105351.13}
\]

with the same separate requirement that the nonreal critical correction be
absent in the last-defect exhaustion.

The boundary gate has therefore been reduced from arbitrary packet geometry
to one explicit Stieltjes moment sequence at the functional-equation anchor
zero.

## 6. Polynomial calibration

If `F=p` is a polynomial of degree `n` and the symmetric outer contour contains
all zeros of `p'`, then the boundary part of `p/p'` is its polynomial part

\[
H_{p,\Omega}(z)={z\over n}+b.
\]

For a definite-parity polynomial, oddness forces `b=0`. Hence

\[
\beta_0={1\over n},
\qquad
\beta_j=0\quad(j\ge1),
\]

so the representing Stieltjes measure is `(1/n)\delta_0`. This is the exact
finite outer-window model; the entire Xi difficulty is the persistence of a
positive Stieltjes measure under the infinite-window boundary current.

## 7. Scope

This theorem identifies the exact coordinate but proves none of the Xi Hankel
inequalities. The complete hierarchy is load bearing. The order-three safe
Pick theorem and any bounded list of origin derivatives remain insufficient by
`R-105203` and `R-105350`. RH remains unproved.
