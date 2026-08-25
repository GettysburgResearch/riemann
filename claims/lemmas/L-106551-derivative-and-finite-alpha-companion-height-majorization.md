# L-106551 — Derivatives and finite-α companions cannot create unpriced upper height

Claim ID: `L-106551`  
Status: **PROVED EXACT FOR FINITE POLYNOMIALS; COFINAL ENTIRE USE REQUIRES THE DECLARED WINDOW EXHAUSTION**  
Created: 2026-08-25  
Depends on: the differentiator-compression identity and Ky Fan's variational principle  
RH status: **not assumed**

For a polynomial `p` with zeros counted with multiplicity define

\[
\boxed{
\mathfrak h_+(p)
 =\sum_{p(z)=0}(\Im z)_+.
}
\tag{L-106551.1}
\]

## 1. Differentiation decreases upper-height mass

Let `p(z)=prod_(j=1)^n(z-z_j)`, put

\[
A=\operatorname{diag}(z_1,\ldots,z_n),
\qquad
e=n^{-1/2}(1,\ldots,1)^T,
\]

and let `P=I-ee^*`. The characteristic polynomial of the compression

\[
PAP\big|_{e^\perp}
\]

is `p'/n`. Hence the critical points of `p` are the eigenvalues of this
compression.

For any complex matrix `M`, Schur triangularization and Ky Fan's principle
give

\[
\sum_{\Im\lambda_j(M)>0}\Im\lambda_j(M)
 \le\operatorname{tr}(\Im M)_+.
\tag{L-106551.2}
\]

Compression cannot increase the positive trace of a Hermitian matrix, so

\[
\boxed{
\mathfrak h_+(p')\le\mathfrak h_+(p).
}
\tag{L-106551.3}
\]

Iteration gives

\[
\boxed{
\mathfrak h_+(p^{(k)})\le\mathfrak h_+(p)
\qquad(0\le k<n).
}
\tag{L-106551.4}

This strengthens the strip form of Gauss--Lucas: it controls the complete
positive first moment, not only the maximal height.

## 2. Exact finite-α companion bounds

The matrix determinant lemma gives

\[
\boxed{
\begin{aligned}
p(z)+i\lambda p'(z)
 &=\det\left(zI-A+i\lambda n ee^*\right),\\
p(z)-i\lambda p'(z)
 &=\det\left(zI-A-i\lambda n ee^*\right).
\end{aligned}
}
\tag{L-106551.5}

Equivalently, the two zero sets are spectra of

\[
A-i\lambda n ee^*,
\qquad
A+i\lambda n ee^*.
\]

Their imaginary parts differ from `Im A` by a rank-one Hermitian matrix of
trace `minus-or-plus lambda n`. The variational formula

\[
\operatorname{tr}H_+
 =\max_{0\preceq Q\preceq I}\operatorname{tr}(QH)
\]

therefore yields

\[
\boxed{
\begin{aligned}
\mathfrak h_+(p+i\lambda p')
 &\le\mathfrak h_+(p),\\
\mathfrak h_+(p-i\lambda p')
 &\le\mathfrak h_+(p)+\lambda n.
\end{aligned}
}
\tag{L-106551.6}

The orientations reverse after conjugation.

## 3. Odd endpoint denominator

For fixed odd `K<n`, put `q=p^(K)` and

\[
D_{K,\lambda}
 =(p+i\lambda p')
  (q-i\lambda q').
\]

Combining (L-106551.4) and (L-106551.6) gives

\[
\boxed{
\mathfrak h_+(D_{K,\lambda})
 \le
 2\mathfrak h_+(p)+\lambda(n-K).
}
\tag{L-106551.7}

Common-factor reduction can only lower the left-hand side.

Consequently, for any cofinal polynomial endpoint family with

\[
\mathfrak h_+(p_T)=o(n_T),
\qquad
\lambda_T=o(1),
\]

one has

\[
\boxed{
\mathfrak h_+(D_{K,\lambda_T}^{\rm red})=o(n_T).
}
\tag{L-106551.8}

## 4. Xi consumption boundary

`L-106550` proves the required `o(N)` height budget for the **literal Xi zero
divisor** in every dyadic window. Equation (L-106551.8) transfers that budget
to any finite canonical-product endpoint truncation whose declared root
multiset is exactly that divisor plus an `o(N)` boundary collar.

A cofinal entire-function use must still verify that the endpoint truncation,
its fifth derivative, and the companion divisor are the same regular-window
objects consumed by the all-pass index. A remote product tail may not be
silently replaced by a constant. This localization row is named
`ENDLOC106550` in `T-106550`.