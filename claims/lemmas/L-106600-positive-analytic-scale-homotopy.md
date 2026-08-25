# L-106600 — Positive analytic companion scales preserve the endpoint index

Claim ID: `L-106600`  
Status: **PROVED EXACT AT FINITE REGULAR MEROMORPHIC SCOPE**  
Created: 2026-08-26  
Depends on: `L-105280`, `L-106501`  
RH status: **not assumed**

Let \(K\ge1\) be odd. Let \(F\) be meromorphic in a neighbourhood of a
regular compactified real contour and real-valued on its real boundary.
Assume that \(F,F'\) and \(F^{(K)},F^{(K+1)}\) have no common boundary zero.

Let \(a\) be holomorphic near the contour, real and strictly positive on the
real boundary, with no boundary pole. Define

\[
E_{0,\pm}^{a}=F\pm iaF',
\qquad
E_{K,\pm}^{a}=F^{(K)}\pm iaF^{(K+1)}
\]

and the reduced endpoint quotient

\[
\boxed{
U_{K,a}
=
\frac{E_{0,-}^{a}E_{K,+}^{a}}
     {E_{0,+}^{a}E_{K,-}^{a}} .
}
\tag{L-106600.1}
\]

Common analytic factors are reduced before inner degrees or Hankel charges
are formed.

## 1. Boundary unitarity

On the real boundary,

\[
E_{j,-}^{a}=\overline{E_{j,+}^{a}},
\]

and hence

\[
\boxed{|U_{K,a}(t)|=1.}
\tag{L-106600.2}
\]

A boundary zero of \(E_{0,+}^{a}\) would force simultaneously
\(F=F'=0\), because \(a>0\). The regularity hypothesis excludes this.
The same argument applies at the \(K\)-endpoint.

## 2. Positive-scale homotopy

Let \(a_0,a_1\) be two admissible scales and put

\[
a_s=(1-s)a_0+sa_1,\qquad 0\le s\le1.
\]

Every \(a_s\) remains real and strictly positive on the boundary. Therefore
no companion zero or pole crosses the boundary during the homotopy.
The boundary winding is integer-valued and continuous in \(s\), so

\[
\boxed{
\operatorname{wind}U_{K,a_0}
=
\operatorname{wind}U_{K,a_1}.
}
\tag{L-106600.3}
\]

Taking \(a_0\) to be a positive constant and invoking the ordinary companion
index gives

\[
\boxed{
\operatorname{wind}U_{K,a}=R_0-R_K
}
\tag{L-106600.4}
\]

with the literal finite-window endpoint and confluent ledger retained.

Thus the companion scale may be selected adaptively without changing the
reverse--Rolle zero-count index.

## 3. Weighted endpoint Wronskian

Writing \(U_{K,a}=N_a/D_a\), direct multiplication gives

\[
\boxed{
N_a-D_a
=
2ia\left(FF^{(K+1)}-F'F^{(K)}\right).
}
\tag{L-106600.5}
\]

If

\[
\mathcal L_K=(-1)^{(K-1)/2}
\left(F'F^{(K)}-FF^{(K+1)}\right),
\]

then

\[
|1-U_{K,a}|^2
=
\boxed{
\frac{4a^2\mathcal L_K^2}
{(F^2+a^2F'^2)
 ((F^{(K)})^2+a^2(F^{(K+1)})^2)} .
}
\tag{L-106600.6}
\]

No derivative of \(a\) appears in the algebraic endpoint difference because
the same scale multiplies both endpoint companions.

## 4. Scope

The theorem changes the companion coefficient, not the derivative chain.
In particular the pinned lower bound for the real zeros of \(F^{(5)}\)
continues to apply at \(K=5\).

The theorem does not estimate the inner phase density created by an adaptive
scale. Pointwise smallness of (L-106600.6) is not sufficient; the phase
measure can concentrate, as recorded in `R-106600`.
