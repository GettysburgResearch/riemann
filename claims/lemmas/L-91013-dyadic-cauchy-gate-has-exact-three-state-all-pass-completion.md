# L-91013 — The dyadic Cauchy gate has an exact three-state all-pass completion

Claim ID: `L-91013`  
Status: **EXACT FINITE SCATTERING THEOREM**  
Created: 2026-08-11  
Depends on: `L-91012`  
RH status: **unproved**

## 1. Scalar input and two defect channels

Put

\[
 h_a(u)=\frac{a^2}{a^2+u^2}.
\]

The two channels of `L-91012` are

\[
 g_{1,a}(u)
 =\frac{2\sqrt6\,a^3u}
 {(a^2+u^2)(4a^2+u^2)},
\]

\[
 g_{2,a}(u)
 =\frac{\sqrt{15}\,a^2u^2}
 {(a^2+u^2)(4a^2+u^2)}.
\]

Then

\[
 h_{2a}(u)^2=h_a(u)^2+g_{1,a}(u)^2+g_{2,a}(u)^2.
\tag{L-91013.1}
\]

## 2. Exact orthogonal transfer matrix

Define

\[
\boxed{
 U_a(u)=\frac1{4(a^2+u^2)}
 \begin{pmatrix}
 4a^2+u^2&2\sqrt6\,au&\sqrt{15}\,u^2\\
 -2\sqrt6\,au&4a^2-4u^2&2\sqrt{10}\,au\\
 \sqrt{15}\,u^2&-2\sqrt{10}\,au&4a^2-u^2
 \end{pmatrix}.
}
\tag{L-91013.2}
\]

A direct polynomial multiplication gives, for every real `u`,

\[
\boxed{
 U_a(u)U_a(u)^T=I_3,
 \qquad
 \det U_a(u)=1.
}
\tag{L-91013.3}
\]

Moreover its first row is exactly the normalized dyadic decomposition:

\[
\boxed{
 h_{2a}(u)\,e_1^TU_a(u)
 =
 \bigl(h_a(u),g_{1,a}(u),g_{2,a}(u)\bigr).
}
\tag{L-91013.4}
\]

Thus the one old channel at resolution `2a` scatters without loss into the old
channel at resolution `a` plus exactly two innovation channels.

## 3. Fixed Cayley generator

Let

\[
\boxed{
 A=\frac12
 \begin{pmatrix}
 0&\sqrt6&0\\
 -\sqrt6&0&\sqrt{10}\\
 0&-\sqrt{10}&0
 \end{pmatrix}.
}
\tag{L-91013.5}
\]

Then

\[
 A^T=-A,
 \qquad
 A^3=-4A,
\]

and

\[
\boxed{
 U_a(u)
 =
 \left(I-\frac{u}{2a}A\right)^{-1}
 \left(I+\frac{u}{2a}A\right).
}
\tag{L-91013.6}
\]

Therefore the entire dyadic resolution transfer is the Cayley transform of
one fixed three-state skew generator. No row-dependent or prime-dependent
matrix is introduced.

The unit axis is

\[
 n=\left(-\frac{\sqrt{10}}4,0,-\frac{\sqrt6}4\right)^T,
 \qquad An=0.
\]

On the orthogonal two-plane, `U_a(u)` is rotation through angle

\[
 2\arctan(u/a).
\]

Equivalently its eigenvalues on the real line are

\[
\boxed{
 1,
 \quad
 \frac{a-iu}{a+iu},
 \quad
 \frac{a+iu}{a-iu}.
}
\tag{L-91013.7}
\]

This is a rational all-pass scattering system with one neutral state and one
reflected conjugate phase pair.

## 4. Source interpretation

The scalar all-pass factor

\[
 b_a(u)=\frac{a-iu}{a+iu}
\]

has one exponential causal state. Equation (L-91013.7) shows that the complete
three-state transfer is a fixed real representation of

\[
 1\oplus b_a\oplus b_a^{-1}.
\]

Hence its physical kernels consist only of the identity contact and the two
reflected exponential states at scale `a`. This is exactly the finite state
content needed by an independent-frequency Hermitian assembly.

Combined with the positive sieve cocycle of `L-91012`, the remaining theorem
may be stated without any unspecified channel:

```text
push the completed positive sieve source through U_a;
retain the reflected pair of exponential states;
prove that the two innovation outputs have nonnegative complete Weil energy;
return the neutral output with coefficient one at resolution a.
```

## 5. Firewall

Boundary unitarity of `U_a` proves the algebraic no-loss identity but does not
prove positivity of the complete arithmetic Weil form. The latter is precisely
the RH-equivalent critical-boundary theorem. No operator norm is inferred from
coefficientwise positivity of the sieve cocycle.
