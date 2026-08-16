# L-94200 — Exact average-binomial inversion and the scale-four annular telescope

Claim ID: `L-94200`  
Status: **PROVED EXACT FINITE ALGEBRA**  
Created: 2026-08-16  
Primary inputs: `L-24501`, `L-24502`, `L-91377`, `L-91378`  
RH status: **unproved**

For real \(X\ge2\), put

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

For a finitely supported ordinary target \(C(q)\), define its unique row
\(\mathscr I C=(d_C(n))\) by backward substitution:

\[
 d_C(n)=\frac{n+1}{n-1}
 \left[
 C(n)-\sum_{m>n}d_C(m)\beta_{mn}
 \right].
\tag{L-94200.1}
\]

Triangularity gives, exactly,

\[
 C(q)=\sum_{n\ge q}d_C(n)\beta_{nq}.
\tag{L-94200.2}
\]

Linearity and the native normalization theorem give

\[
 c_X=\mathscr I w_X.
\tag{L-94200.3}
\]

Define the scale-four annular target

\[
 \Omega_X^{\rm ann}(q)
 =w_X(q)-w_{X/4}(q)
 =
 \frac1{\sqrt q}
 \min\!\left(\log4,\log\frac Xq\right)_+.
\tag{L-94200.4}
\]

Its inverse row is

\[
 a_X^{(4)}
 :=\mathscr I\Omega_X^{\rm ann}
 =c_X-c_{X/4}.
\tag{L-94200.5}
\]

No floor convention is hidden: \(c_Y\) is defined for every real endpoint \(Y\)
by zero extension, and the finite row support is \(n\le\lfloor Y\rfloor\).

Iterating (L-94200.5) terminates after finitely many scales:

\[
 \boxed{
 c_X=\sum_{j\ge0}a_{X/4^j}^{(4)}.
 }
\tag{L-94200.6}
\]

Consequently, coefficientwise positivity of every annular row implies
coefficientwise positivity of the full native row.
