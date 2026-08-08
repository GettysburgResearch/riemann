# R-21704 — Positive Robin fibers are not closed under positive superposition

Claim ID: `R-21704`  
Title: Even two individually real-zero positive-length Robin fibers can have a positive combination with off-axis zeros  
Status: **EXACT SCOPE CORRECTION / FINITE COUNTEREXAMPLE**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21709`; elementary canonical-product coefficient inequality  
Scope: the inference from one-fiber Sturm–Liouville positivity to the complete Brownian length mixture

## 1. A necessary coefficient inequality

Let

\[
F(z)=c_0+c_1z^2+c_2z^4+\cdots,
\qquad c_0>0,
\tag{R-21704.1}
\]

be a real even entire function of order at most one whose zeros all lie on the imaginary axis. After removing an inessential positive constant, its genus-zero even canonical product has the form

\[
F(z)=c_0\prod_j\left(1+\frac{z^2}{\gamma_j^2}\right),
\qquad \gamma_j^2>0.
\tag{R-21704.2}
\]

Writing

\[
a_j=\gamma_j^{-2}>0,
\]

one has

\[
\frac{c_1}{c_0}=\sum_ja_j,
\qquad
\frac{c_2}{c_0}=\sum_{i<j}a_ia_j.
\]

Therefore

\[
\boxed{
c_1^2\ge2c_0c_2.}
\tag{R-21704.3}
\]

Indeed

\[
\left(\sum_ja_j\right)^2
=\sum_ja_j^2+2\sum_{i<j}a_ia_j
\ge2\sum_{i<j}a_ia_j.
\]

Thus violation of (R-21704.3) proves the existence of a zero away from the imaginary axis.

## 2. Exact coefficients of one corrected Robin fiber

For

\[
\Phi_\ell(z)
=\cosh\frac{\ell z}{2}
+2z\sinh\frac{\ell z}{2},
\]

the first coefficients are

\[
\boxed{
\Phi_\ell(z)
=1+\left(\ell+\frac{\ell^2}{8}\right)z^2
+\left(\frac{\ell^3}{24}+\frac{\ell^4}{384}\right)z^4
+O(z^6).
}
\tag{R-21704.4}

For `ell=8`,

\[
\boxed{
\Phi_8(z)=1+16z^2+32z^4+O(z^6).
}
\tag{R-21704.5}

By `L-21709`, `Phi_8` has only imaginary zeros. The zero-length fiber

\[
\Phi_0(z)=1
\]

is zero free.

## 3. Positive combination with off-axis zeros

Consider the positive superposition

\[
\boxed{
F(z)=\Phi_0(z)+\frac1{10}\Phi_8(z).
}
\tag{R-21704.6}

Its first coefficients are exactly

\[
 c_0=\frac{11}{10},
\qquad
 c_1=\frac85,
\qquad
 c_2=\frac{16}{5}.
\tag{R-21704.7}

Hence

\[
 c_1^2=\frac{64}{25},
\]

whereas

\[
2c_0c_2
=2\cdot\frac{11}{10}\cdot\frac{16}{5}
=\frac{176}{25}.
\]

Therefore

\[
\boxed{
c_1^2<2c_0c_2.}
\tag{R-21704.8}

The necessary inequality (R-21704.3) fails. Consequently `F` has at least one zero away from the imaginary axis.

Both summands in (R-21704.6) are individually in the real-zero Robin class, and both weights are positive. Thus that class is not a convex cone.

## 4. Consequence for the Brownian/Nörlund route

The complete Brownian cardinal representation is a positive integral over length fibers. Even if all negative lengths could be eliminated, positivity of every remaining one-fiber Sturm–Liouville determinant would not imply real-rootedness of the integral.

A valid completion requires additional global structure, for example:

```text
common interlacing of all active fibers;
a single canonical system whose determinant is the whole mixture;
Hermite–Biehler domination for the aggregate entire function;
or total positivity of the complete length kernel.
```

None follows from one-fiber self-adjointness alone.

## 5. Exact disposition

```text
positive-length one-fiber real-zero theorem       VERIFIED
closure under positive superposition              FALSE
local Robin classification -> BLNRZ               REJECTED
finite Brownian/Nörlund algebra                    RETAINED
aggregate canonical-system theorem                OPEN
Riemann Hypothesis                                 UNPROVEN
```