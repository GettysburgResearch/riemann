# L-106415 — Endpoint companion coverage is one model-space sampling matrix

Claim ID: `L-106415`  
Status: **PROVED EXACT FOR FINITE RATIONAL ALL-PASS SYMBOLS; CONFLUENT FORM INCLUDED**  
Created: 2026-08-24  
Depends on: finite Blaschke/model-space theory; `L-105551`  
RH status: **not assumed**

Let

\[
U=\omega\frac{B_+}{B_-}
\]

be a reduced rational unimodular function on the circle, with
\(m=\deg B_-\).  By `L-105551`,

\[
\ker H_U=B_-H^2,
\qquad
\mathcal I_U:=(\ker H_U)^\perp=K_{B_-},
\qquad
\dim\mathcal I_U=m.
\tag{L-106415.1}

Let \(\mathcal S=\operatorname{span}\{s_1,\ldots,s_d\}\subset H^2\), where the
\(s_\ell\) are orthonormal and are fixed before the divisor of \(U\) is
observed.

## 1. Simple-zero sampling matrix

Assume first that the zeros \(b_1,\ldots,b_m\) of \(B_-\) are simple.  Let

\[
e_j=\frac{k_{b_j}}{\|k_{b_j}\|}
\]

be the normalized Hardy reproducing kernels, and define

\[
G_{jk}=\langle e_k,e_j\rangle,
\qquad
A_{j\ell}=\langle s_\ell,e_j\rangle.
\tag{L-106415.2}

The kernels form a basis of \(K_{B_-}\), so \(G>0\).  For
\(v=\sum_jc_je_j\),

\[
\|v\|^2=c^*Gc,
\qquad
\|P_{\mathcal S}v\|^2=c^*AA^*c.
\]

Therefore the compression of the source projection to the complete bad
model space is represented by

\[
\boxed{
\mathcal C_{U,\mathcal S}
=G^{-1/2}AA^*G^{-1/2},
\qquad 0\preceq\mathcal C_{U,\mathcal S}\preceq I_m.
}
\tag{L-106415.3}

The exact missed dimension is

\[
\boxed{
\dim\bigl(K_{B_-}\cap\mathcal S^\perp\bigr)
=\dim\ker\mathcal C_{U,\mathcal S}.
}
\tag{L-106415.4}

More generally, for \(0<a<1\), the number of model-space directions whose
source energy is below \(a\) is the number of eigenvalues of
\(\mathcal C_{U,\mathcal S}\) below \(a\).  If

\[
\operatorname{tr}(I-\mathcal C_{U,\mathcal S})_+\le\varepsilon m,
\]

then `L-106412` discards at most

\[
\frac{\varepsilon}{1-a}m
\]

such directions and the retained inverse-frame cost is at most \(a^{-1}\).

## 2. Evaluation form

Reproducing gives

\[
\boxed{
A_{j\ell}
=\frac{s_\ell(b_j)}{\|k_{b_j}\|}.
}
\tag{L-106415.5}

Thus the endpoint-bank coverage problem is an explicit sampling theorem at the
bad companion zeros.  No contour norm or unspecified partial-index remainder
appears in (L-106415.3).

In the upper-half-plane Paley--Wiener model with Fourier support \([0,B]\), the
reproducing kernel is

\[
\boxed{
K_B(z,w)
=\int_0^B e^{iuz}e^{-iu\overline w}\,du
=\frac{1-e^{iB(z-\overline w)}}{-i(z-\overline w)}.
}
\tag{L-106415.6}

Hence both \(G\) and \(A\) are explicit finite exponential/Cauchy matrices once
the source frame and companion divisor are declared.

## 3. Confluent divisor

If \(b\) is a zero of \(B_-\) of multiplicity \(r\), replace the single kernel
by the derivative kernels

\[
\partial_{\overline b}^{q}k_b,
\qquad 0\le q<r.
\]

Their Gram matrix is the corresponding confluent derivative of
\(K_B(z,w)\), and the evaluation matrix uses the jets

\[
s_\ell^{(q)}(b).
\]

Equations (L-106415.3)--(L-106415.5) remain exact.  Near collisions are
therefore represented by a stable confluent block rather than silently treated
as distinct well-separated points.

## 4. Exact endpoint frontier

For the endpoint all-pass symbol of `L-106400`, define

\[
\mathcal C_T
=\mathcal C_{U_T,\mathcal S_T}
\]

using the predeclared two-boundary Paley--Wiener source frame of `L-106413`.
The source-coverage row in `ENDPOINTBANK106410` is precisely a one-sided lower
spectral estimate for \(\mathcal C_T\).  This theorem proves the normal form, not
its favorable asymptotic estimate.
