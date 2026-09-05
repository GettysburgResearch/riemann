# L-106437 — Companion zero-height mass is trace-norm contracting

Claim ID: `L-106437`  
Status: **PROVED EXACT FOR FINITE POLYNOMIALS**  
Created: 2026-08-25  
Depends on: elementary determinant identities, Schur triangularization and Schatten trace norm  
RH status: **not assumed**

For a polynomial `p`, write

\[
\mathfrak h(p)=\sum_{p(\rho)=0}|\operatorname{Im}\rho|
\]

with multiplicity.  This lemma gives a source-free control of the complete
vertical mass of every linear derivative companion.

## 1. Eigenvalue height majorization

Let `A` be an arbitrary complex `n x n` matrix with eigenvalues
`lambda_1,...,lambda_n`.  Schur triangularization gives `A=QTQ^*`, with the
`lambda_j` on the diagonal of `T`.  The diagonal of

\[
Q^*\operatorname{Im}(A)Q
\]

is `(Im lambda_j)`.  Schur--Horn majorization and convexity of the absolute
value therefore give

\[
\boxed{
\sum_{j=1}^n|\operatorname{Im}\lambda_j|
\le\operatorname{tr}|\operatorname{Im}A|.
}
\tag{L-106437.1}
\]

## 2. Linear companion as a dissipative rank-one perturbation

Let

\[
p(z)=\prod_{j=1}^n(z-z_j),
\qquad
Z=\operatorname{diag}(z_1,\ldots,z_n),
\qquad
e=(1,\ldots,1)^T.
\]

The matrix determinant lemma gives

\[
\det\bigl(zI-(Z-i\lambda ee^*)\bigr)
 =p(z)+i\lambda p'(z),
\tag{L-106437.2}
\]

and

\[
\det\bigl(zI-(Z+i\lambda ee^*)\bigr)
 =p(z)-i\lambda p'(z).
\tag{L-106437.3}
\]

Since

\[
\operatorname{Im}(Z\mp i\lambda ee^*)
 =\operatorname{diag}(\operatorname{Im}z_j)
  \mp\lambda ee^*,
\]

(L-106437.1) and the triangle inequality for the trace norm imply

\[
\boxed{
\mathfrak h(p\pm i\lambda p')
\le\mathfrak h(p)+\lambda n.
}
\tag{L-106437.4}
\]

The one-sided refinements are

\[
\sum_{p+i\lambda p'(\rho)=0}(\operatorname{Im}\rho)_+
\le
\sum_{p(z_j)=0}(\operatorname{Im}z_j)_+,
\tag{L-106437.5}
\]

\[
\sum_{p-i\lambda p'(\rho)=0}(-\operatorname{Im}\rho)_+
\le
\sum_{p(z_j)=0}(-\operatorname{Im}z_j)_+,
\tag{L-106437.6}
\]

because subtracting, respectively adding, the positive semidefinite rank-one
matrix can only decrease the corresponding positive trace.

## 3. Derivatives contract total height mass

Let `Q` be an isometry from `C^(n-1)` onto `e^perp`.  The characteristic
polynomial of the compression `Q^*ZQ` is `p'(z)/n`.  Applying
(L-106437.1) and trace-norm contractivity under compression gives

\[
\boxed{
\mathfrak h(p')\le\mathfrak h(p).
}
\tag{L-106437.7}
\]

Iteration yields

\[
\boxed{
\mathfrak h(p^{(k)})\le\mathfrak h(p)
\qquad(0\le k<n).
}
\tag{L-106437.8}
\]

## 4. Endpoint denominator

For

\[
D=(p+i\lambda p')(p''-i\lambda p'''),
\]

common-factor reduction can only decrease zero-height mass.  Equations
(L-106437.4) and (L-106437.8) therefore give

\[
\boxed{
\mathfrak h(D_{\rm red})
\le2\mathfrak h(p)+2\lambda n.
}
\tag{L-106437.9}
\]

The upper zeros of the reduced denominator are the adverse all-pass poles; the
reflections of its lower zeros are the favorable upper all-pass zeros.  Thus
(L-106437.9) controls the complete absolute vertical mass of both endpoint
divisors without any separation assumption.

## 5. Scope

The theorem is finite and exact.  Applying it to Xi requires a declared
canonical-product truncation and a cofinal passage.  It controls vertical mass,
not the number of arbitrarily shallow poles, so it does not prove the signed
index estimate or ninety percent by itself.
