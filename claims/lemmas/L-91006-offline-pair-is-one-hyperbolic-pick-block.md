# L-91006 — The unit-disc Pick defect of one off-line pair is one hyperbolic block

Claim ID: `L-91006`  
Status: **PROPOSED COMPLETE EXACT SIGNATURE FACTORIZATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-91001`  
RH status: **unproved**

## 1. Rational block of a reflected pair

Fix a centre `x` and one right-side zero coordinate

\[
 z=\rho-\left(\frac12+ix\right),
 \qquad
 a=1-z^2,
 \qquad
 R=\frac{2m z^2}{a^2}.
\]

The complete reflected-pair contribution to the unit-disc function is

\[
 \boxed{
 F_z(w)=\frac{R}{w-a}+\frac{\bar R}{w-\bar a}.
 }
\tag{L-91006.1}
\]

This is the same expression as the second line of (T-91001.2), written in residue orientation.

## 2. Exact Pick-kernel signature

For a scalar meromorphic function `F`, use the Pick kernel

\[
 K_F(w,v)=\frac{F(w)-\overline{F(v)}}{w-\bar v}.
\]

Put

\[
 \Phi_z(w)=
 \begin{pmatrix}
 (w-a)^{-1}\\
 (w-\bar a)^{-1}
 \end{pmatrix}.
\]

A direct subtraction gives

\[
 \boxed{
 K_{F_z}(w,v)
 =\Phi_z(w)^T
 \begin{pmatrix}
 0&-R\\
 -\bar R&0
 \end{pmatrix}
 \overline{\Phi_z(v)}.
 }
\tag{L-91006.2}
\]

The coefficient matrix has eigenvalues

\[
 \boxed{\pm|R|.}
\tag{L-91006.3}
\]

Thus one complex reflected pair is exactly one positive and one negative Pick direction: the same signature `(1,1)` block that appears in the Zeta23 and Q4 Hermitian programmes. No generic matrix estimate or limiting argument is involved.

## 3. Matched ordinate: negative rank one

If the centre is the ordinate of the zero, then `z=y` is real,

\[
 a=1-y^2\in(3/4,1),
 \qquad
 R_{\rm tot}=\frac{4my^2}{(1-y^2)^2}>0,
\]

and the two conjugate terms coalesce:

\[
 F_y(w)=\frac{R_{\rm tot}}{w-a}.
\tag{L-91006.4}
\]

Its Pick kernel is the negative rank-one square

\[
 \boxed{
 K_{F_y}(w,v)
 =-R_{\rm tot}
 \frac1{w-a}\frac1{\bar v-a}.
 }
\tag{L-91006.5}
\]

At `w=a+i epsilon`,

\[
 \boxed{
 \frac{\Im F_y(w)}{\Im w}
 =-\frac{R_{\rm tot}}{\epsilon^2}<0.
 }
\tag{L-91006.6}
\]

This is the one-point Pick witness recorded qualitatively in `T-91001`, now with its exact rank-one factorization.

## 4. Positive cut and hyperbolic defect

The critical-line part of `A_x` is

\[
 S_x(w)=\sum_\gamma
 \frac{2m_\gamma u^2}
 {(1+u^2)^2(1+u^2-w)},
 \qquad u=\gamma-x,
\]

and has the positive Stieltjes jump

\[
 \boxed{
 \frac1{2\pi i}
 \left[S_x(v+i0)-S_x(v-i0)\right]
 =\sum_\gamma
 \frac{2m_\gamma u^2}{(1+u^2)^2}
 \delta\bigl(v-1-u^2\bigr)
 \ge0.
 }
\tag{L-91006.7}
\]

Every off-line pair contributes only a rational hyperbolic block (L-91006.2), with no negative continuous cut density. Therefore the exact analytic decomposition is

```text
positive Stieltjes cut carried by critical-line zeros
+
finite/local signature-(1,1) rational blocks carried by off-line pairs.
```

This is the unit-disc scalar analogue of the signature decomposition in the imported Zeta23 operator.

## 5. Boundary

Established here:

```text
exact residue form of one off-line pair;
exact Pick-kernel factorization;
one negative and one positive direction per complex pair block;
negative rank-one matched-ordinate block;
positive critical-line Stieltjes jump;
all indefiniteness localized in rational hyperbolic blocks.
```

Not established here:

```text
absence of the hyperbolic blocks;
prime-side unit-disc Pick positivity;
Riemann Hypothesis.
```
