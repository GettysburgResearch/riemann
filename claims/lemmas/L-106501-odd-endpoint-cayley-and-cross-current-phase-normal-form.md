# L-106501 — Odd endpoint Cayley and cross-current phase normal form

Claim ID: `L-106501`  
Status: **PROVED EXACT FINITE ALGEBRA + FAIL-CLOSED OPERATOR INTERFACE**  
Created: 2026-08-25  
Depends on: `L-105623`, `L-106500`; the companion winding theorem  
RH status: **not assumed**

Let `K=2m+1` be odd and let `F` be real on the real axis.  For `lambda>0`
define

\[
U_{K,\lambda}(t)=
{(F-i\lambda F')(F^{(K)}+i\lambda F^{(K+1)})
 \over
 (F+i\lambda F')(F^{(K)}-i\lambda F^{(K+1)})}.
\tag{L-106501.1}

At finite regular rational scope, reduce common factors before taking the
Hankel symbol.

## 1. Exact endpoint telescope

The boundary symbol is unimodular.  Companion-index additivity gives

\[
\boxed{
\operatorname{wind}U_{K,\lambda}=R_0-R_K,
}
\tag{L-106501.2}

where `R_j` is the real-zero count of `F^(j)` on the declared regular window,
with the literal endpoint and confluent ledger retained.

Writing `U=N/D`, direct multiplication gives

\[
\boxed{
N-D=2i\lambda
\left(FF^{(K+1)}-F'F^{(K)}\right)
=-2i\lambda(-1)^m\mathcal L_K.
}
\tag{L-106501.3}

Thus every intermediate derivative companion cancels: an odd block from
`F` to `F^(K)` has one endpoint Wronskian source.

## 2. Scalar Cayley form

On the real axis put

\[
A_{K,\lambda}
=FF^{(K)}+\lambda^2F'F^{(K+1)}.
\]

Then

\[
\boxed{
D=A_{K,\lambda}+i\lambda(-1)^m\mathcal L_K,
\qquad
N=A_{K,\lambda}-i\lambda(-1)^m\mathcal L_K.
}
\tag{L-106501.4}

Away from the zero set of `A_(K,lambda)`, the endpoint symbol is the literal
Cayley transform

\[
\boxed{
U_{K,\lambda}
={1-iX_{K,\lambda}\over1+iX_{K,\lambda}},
\qquad
X_{K,\lambda}
={\lambda(-1)^m\mathcal L_K\over A_{K,\lambda}}.
}
\tag{L-106501.5}

No approximation is involved.  In particular

\[
\boxed{
|1-U_{K,\lambda}|^2
={4\lambda^2\mathcal L_K^2
 \over
 (F^2+\lambda^2F'^2)
 ((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}
\le4.
}
\tag{L-106501.6}

The numerator of the physical phase angle is exactly the positive-source
Wronskian of `L-106500`; the denominator is the actual endpoint companion
metric.

## 3. Canonical current contraction

For `h>0`, let `J_(K,h)` be the positive cross current of `L-106500` and define
on its positive-frequency support

\[
\boxed{
r_{K,h}(\xi)
={h e^{-h\xi}\widehat{\mathcal L_K}(\xi)
 \over \widehat J_{K,h}(\xi)},
\qquad 0\le r_{K,h}\le1,
}
\tag{L-106501.7}

with `r=0` where the denominator vanishes.  Let `R_(K,h)` be multiplication by
`r_(K,h)` in the source Fourier space and let `V_(K,lambda)` denote the
unitary physical phase action induced by `U_(K,lambda)` on the same declared
finite bank.

The exact algebraic identity

\[
\boxed{
I-\operatorname{Re}(V R)
=(I-R)
 +R^{1/2}(I-\operatorname{Re}V)R^{1/2}
 -\operatorname{Re}\left([V,R^{1/2}]R^{1/2}\right)
}
\tag{L-106501.8}

specializes `L-105623` to every odd endpoint block.

Therefore the diagonal source contraction is not the missing theorem.  The
only sign-indefinite promotion term is the explicitly typed phase collision

\[
\boxed{
\mathcal K_{K,h,\lambda}
=[V_{K,\lambda},R_{K,h}^{1/2}]R_{K,h}^{1/2}.
}
\tag{L-106501.9}

## 4. Binding firewall

Equations (L-106501.7)--(L-106501.9) do **not** identify a source-density ratio
with the compressed Hankel norm of `U_(K,lambda)`.  Denominator multiplication
would put an analytic Hardy source in the Hankel kernel, as recorded in
`R-106417/R-106432`.  A conclusion-facing proof must instead control the
actual phase collision, the model-space coverage and every endpoint/tail
charge on one common source bank.
