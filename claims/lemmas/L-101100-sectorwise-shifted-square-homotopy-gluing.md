# L-101100 — Source-owned sectorwise shifted-square homotopy gluing

Claim ID: `L-101100`  
Status: **PROVED EXACT LINEAR GLUING THEOREM**  
Created: 2026-08-20  
Inputs: PR #688 `L-100400`; source-cover principle `L-101003`  
RH status: **not assumed**

Let \(a=\sum_{\nu\in\mathcal N}a_\nu\) be a finite disjoint decomposition of
one signed arithmetic source before physical observation.  All transforms
below are linear in the source.

For \(-1\le c\le0\), put
\[
 \lambda_c={(3-c)^2\over 9}.
\]
The exact shifted-square identity of `L-100400`, applied to the sector
\(a_\nu\), has the form
\[
 \mathcal E[a_\nu](X)
 =\mathcal A_c[a_\nu](X)
 +\mathcal I_c[a_\nu](X)
 +\mathcal P_c[a_\nu](X),                         \tag{L-101100.1}
\]
where
\[
 \mathcal A_c[a](X)
 =X(1+c)^2\sum_{n>\lambda_cX}{a(n)\over n^{3/2}}, \tag{L-101100.2}
\]
\[
 \mathcal I_c[a](X)
 =(3-c)X\int_{\lambda_cX}^{\infty}
 L_c[a](t){dt\over t^2},                          \tag{L-101100.3}
\]
and
\[
 \mathcal P_c[a](X)
 =\sum_{X<n\le\lambda_cX}{a(n)\over\sqrt n}
       \left(4\sqrt{X/n}-3\right)^2.              \tag{L-101100.4}
\]

Choose an arbitrary homotopy parameter \(c_\nu\in[-1,0]\) separately for
each source sector.  Summing (L-101100.1) gives the exact identity
\[
 \boxed{
 \mathcal E[a](X)
 =\sum_{\nu\in\mathcal N}
 \bigl(
  \mathcal A_{c_\nu}[a_\nu](X)
 +\mathcal I_{c_\nu}[a_\nu](X)
 +\mathcal P_{c_\nu}[a_\nu](X)
 \bigr).
 }                                                   \tag{L-101100.5}
\]

The two endpoint choices are complementary:
\[
 c=0:\quad \mathcal P_0=0,                         \tag{L-101100.6}
\]
\[
 c=-1:\quad \mathcal A_{-1}=0.                     \tag{L-101100.7}
\]
Thus one source sector may be represented with no activation collar, while
another disjoint sector is represented with no activation atoms.

This does **not** contradict `R-100400`.  That refutation concerns a positive
scalar mixture of the two representations after observation.  Equation
(L-101100.5) chooses the representation on disjoint source-owned atoms before
observation.  No coefficient is duplicated or discarded.

Finally, for every finite partition,
\[
 [ -\mathcal E[a](X)]_+
 \le
 \sum_\nu
 \left[
 -\bigl(
  \mathcal A_{c_\nu}[a_\nu]
 +\mathcal I_{c_\nu}[a_\nu]
 +\mathcal P_{c_\nu}[a_\nu]
 \bigr)(X)
 \right]_+.                                        \tag{L-101100.8}
\]
Consequently sectorwise one-sided estimates compose without requiring either
global homotopy to be sign-definite.
