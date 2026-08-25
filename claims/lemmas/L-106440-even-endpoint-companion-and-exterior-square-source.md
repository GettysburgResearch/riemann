# L-106440 — Every even Xi endpoint has one companion and one positive exterior-square source

Claim ID: `L-106440`  
Status: **PROVED EXACT AT FINITE REGULAR SCOPE; ACTUAL-XI FOURIER SOURCE PROVED UNCONDITIONALLY**  
Created: 2026-08-25  
Depends on: `L-105280`, `L-105290`, `L-106400--L-106401`  
RH status: **not assumed**

Let `F` be a real entire function, or first a regular real polynomial, and let

\[
K=2m\ge 2.
\]

For `lambda>0` put

\[
E_{j,\pm}=F^{(j)}\pm i\lambda F^{(j+1)}
\]

and define the endpoint all-pass symbol

\[
\boxed{
U_{0,K}
 =\frac{E_{0,-}E_{K,+}}{E_{0,+}E_{K,-}}.
}
\tag{L-106440.1}
\]

On the real line the numerator is the complex conjugate of the denominator,
so `|U_(0,K)|=1`.

## 1. Complete derivative telescope

Let `R_j` be the real-zero count of `F^(j)` on one regular window.  The
companion winding theorem gives

\[
\boxed{
\operatorname{wind}U_{0,K}=R_0-R_K.
}
\tag{L-106440.2}

All intermediate companions cancel.  Equivalently, if `E_j` is the wrong
extremum count at the `j`th downward step,

\[
R_0-R_K=K-2\sum_{j=1}^{K}E_j.
\]

The negative-half Fourier/Hankel identity therefore gives

\[
\boxed{
R_0\ge R_K-\|H_{U_{0,K}}\|_{\mathcal S_2}^2
}
\tag{L-106440.3}

up to the declared endpoint and confluent ledger in the entire-window passage.
No rung-by-rung norm estimate is required.

## 2. Exact denominator cancellation

Write

\[
N_K=E_{0,-}E_{K,+},
\qquad
D_K=E_{0,+}E_{K,-}.
\]

Direct multiplication gives the universal Wronskian identity

\[
\boxed{
N_K-D_K
 =2i\lambda\left(FF^{(K+1)}-F'F^{(K)}\right).
}
\tag{L-106440.4}

Both the identity term `F F^(K)` and the quadratic companion term
`lambda^2 F' F^(K+1)` cancel before estimation.

## 3. Actual Xi exterior-square density

Use the classical positive even Fourier representation

\[
\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad \Phi(u)=\Phi(-u)\ge0.
\]

Put

\[
\mathcal T_{2m}
 =\Xi\,\Xi^{(2m+1)}-\Xi'\,\Xi^{(2m)}.
\]

For `v=xi-u`, symmetrization under `u<->v` gives

\[
\widehat{\mathcal T_{2m}}(\xi)
 =(-1)^m i\xi\,\Lambda_m(\xi),
\tag{L-106440.5}
\]

where

\[
\boxed{
\Lambda_m(\xi)
 ={1\over2}\int_{\mathbb R}
 (u-v)^2
 \left(\sum_{j=0}^{m-1}u^{2j}v^{2(m-1-j)}\right)
 \Phi(u)\Phi(v)\,du
 \ge0.
}
\tag{L-106440.6
}

The density is even, rapidly decreasing and nonnegative.  The algebra is the
factorization

\[
(v-u)(v^{2m}-u^{2m})
 =(u+v)(u-v)^2
  \sum_{j=0}^{m-1}u^{2j}v^{2(m-1-j)}.
\]

Thus every even endpoint numerator is, up to the fixed phase
`(-1)^m i`, one derivative of an actual-Xi positive exterior-square density.
For `m=1` this is exactly `L-106401`; for `m=2`,

\[
\Lambda_2(\xi)
 ={1\over2}\int (u-v)^2(u^2+v^2)\Phi(u)\Phi(v)\,du.
\]

After Hardy compression, the endpoint numerator is one explicit actual-Xi
Hankel source.  No frozen Euler-product approximation is used in this
identification.

## 4. Scope

The theorem proves the endpoint telescope, the denominator cancellation and
the sign of the actual numerator source.  It does not bound the complete
all-pass index or the signed unobserved companion tail.  That remaining
quantity is retained explicitly in `T-106440`.