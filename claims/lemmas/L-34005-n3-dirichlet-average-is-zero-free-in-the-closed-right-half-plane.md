# L-34005 — The N=3 Dirichlet-average Mellin factor is zero-free in the closed right half-plane

Claim ID: `L-34005`

Status: **PROPOSED COMPLETE EXACT HALF-PLANE THEOREM — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34003`

Scope: exact `N=3` Brownian raw stability; no cofinal theorem and no RH claim

## 1. Explicit numerator

For `N=3`, `L-34003` gives, up to a positive constant and a zero-free gamma factor, the numerator

\[
\boxed{
H_3(z)
=\frac94\left(z+\frac1{12}\right)
 +\frac9{25}\,4^{-z}\left(z+\frac{31}{15}\right)
 +\frac1{100}\,9^{-z}\left(z+\frac{137}{20}\right).
}
\tag{L-34005.1}
\]

We prove

\[
\boxed{H_3(z)\ne0\qquad(\Re z\ge0).}
\tag{L-34005.2}
\]

Hence `M_3(z)=E[Q_3^z]` is zero-free throughout the closed right half-plane.

## 2. Exterior disk: first-term Rouché domination

Let

\[
T_1=\frac94\left(z+\frac1{12}\right),
\quad
T_2=\frac9{25}4^{-z}\left(z+\frac{31}{15}\right),
\quad
T_3=\frac1{100}9^{-z}\left(z+\frac{137}{20}\right).
\]

When `Re z>=0`,

\[
|4^{-z}|\le1,
\qquad |9^{-z}|\le1.
\]

Therefore

\[
|T_1|
\ge \frac94\left(|z|-\frac1{12}\right),
\]

while

\[
|T_2|+|T_3|
\le
\left(\frac9{25}+\frac1{100}\right)|z|
+\frac9{25}\frac{31}{15}
+\frac1{100}\frac{137}{20}.
\]

The constant terms simplify exactly to

\[
\frac94\frac1{12}
+\frac9{25}\frac{31}{15}
+\frac1{100}\frac{137}{20}=1,
\tag{L-34005.3}
\]

and

\[
\frac94-\frac9{25}-\frac1{100}=\frac{47}{25}.
\tag{L-34005.4}
\]

Consequently

\[
|T_1|>|T_2|+|T_3|
\quad\text{whenever}\quad
|z|>\frac{25}{47}.
\tag{L-34005.5}
\]

Thus `H_3(z)` cannot vanish in the portion of `Re z>=0` outside the closed disk

\[
|z|\le25/47.
\]

This is a direct triangle/Rouché domination; no zero computation is used.

## 3. Interior disk: positive real part

It remains to consider

\[
\Re z=x\ge0,
\qquad
|z|\le\frac{25}{47}.
\]

Write `z=x+iy`. Then `|y|<=25/47`.

The first term has

\[
\Re T_1=\frac94\left(x+\frac1{12}\right)>0.
\tag{L-34005.6}
\]

For a general term

\[
e^{-\lambda z}(z+b),
\qquad b>0,
\]

its real part is

\[
e^{-\lambda x}
\left[(x+b)\cos(\lambda y)+y\sin(\lambda y)\right].
\tag{L-34005.7}
\]

If `|lambda y|<pi/2`, then the cosine is positive, and

\[
y\sin(\lambda y)\ge0.
\]

For `T_2`, `lambda=log4`; for `T_3`, `lambda=log9`.  It is therefore enough to note

\[
\frac{25}{47}\log9<\frac\pi2.
\tag{L-34005.8}
\]

For a completely elementary verification, use

\[
\log9<\frac{11}{5},
\qquad
\pi>3,
\]

which give

\[
\frac{25}{47}\log9
<\frac{55}{47}
<\frac32
<\frac\pi2.
\]

Hence both `T_2` and `T_3` have strictly positive real part throughout the remaining half-disk. Together with (L-34005.6),

\[
\boxed{\Re H_3(z)>0}
\tag{L-34005.9}
\]

there.

Combining Sections 2 and 3 proves (L-34005.2).

## 4. Brownian consequence

By `L-34001/L-34003`, the omitted prefactor relating `H_3` to

\[
M_3(z)=\mathbb E[Q_3^z]
\]

has no zeros. Therefore

\[
\boxed{
M_3(z)\ne0\qquad(\Re z\ge0).
}
\tag{L-34005.10]

(The closing bracket in the equation tag is typographical only.)

Equivalently, the raw Brownian `N=3` factor `D_3(s)` is zero-free for

\[
\Re s\ge0.
\]

This is stronger than the RH-facing requirement `Re z>1/4` at this finite level.

## 5. Strategic consequence

The proof has a two-region form:

```text
large |z|:
  first exponential term dominates globally;

small |z|:
  all exponential phases lie in a common open half-plane,
  so the real part is positive.
```

This mechanism is now exact for `N=2` and `N=3`.  It suggests an all-`N` attack based on finding a positive low-frequency block which dominates the tail outside a compact disk while the full phase span remains below `pi/2` inside that disk.

The coefficient identity

\[
C_{N,i+1}/C_{N,i}
=\left(\frac{N-i}{N+i+1}\right)^2
\]

from `L-34003` is the natural tool for estimating such tails.  No all-`N` domination theorem is asserted here.

## 6. Proof boundary

Closed exactly:

1. explicit `N=3` numerator;
2. exterior Rouché domination;
3. interior positive-real-part sector;
4. zero-freeness in the complete closed right half-plane.

Open:

1. extension of the two-region argument to unbounded `N`;
2. cofinal raw Brownian stability;
3. RH.
