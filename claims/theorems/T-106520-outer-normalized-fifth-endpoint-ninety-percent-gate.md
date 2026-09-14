# T-106520 — Outer-normalized fifth-endpoint gate for more than ninety percent

Claim ID: `T-106520`  
Status: **UNCONDITIONAL TOPOLOGY-SAFE REDUCTION; ONE OUTER DIRICHLET ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: `L-106500`, `L-106501`, `L-106507`, `L-106509`; the pinned `R_5/N>997/1000-o(1)` input  
RH status: **unproved**

## 1. Canonical endpoint pair

For `F=Xi`, let

\[
N_T=(F-i\lambda_TF')(F^{(5)}+i\lambda_TF^{(6)}),
\]

\[
D_T=(F+i\lambda_TF')(F^{(5)}-i\lambda_TF^{(6)})
\]

on a cofinal regular window.  Reduce common factors and form

\[
U_T={N_T\over D_T}.
\]

The exact odd-endpoint telescope gives

\[
\operatorname{wind}U_T=R_0(T,2T)-R_5(T,2T)
\]

and

\[
N_T-D_T=-2i\lambda_T\mathcal L_5,
\qquad
\mathcal L_5=F'F^{(5)}-FF^{(6)}.
\]

## 2. Cancel only the common outer factor

Let

\[
N_T=O_TB_{+,T},
\qquad
D_T=O_TB_{-,T}
\]

be the canonical common-outer factorization of `L-106507`.  Then

\[
S_T={N_T-D_T\over O_T}=B_{+,T}-B_{-,T}
\]

retains every inner unit charge.  `L-106507` proves

\[
\boxed{
\|H_{U_T}\|_{\mathcal S_2}^2
\le\|S_T\|_{\mathcal D}^2
=4\lambda_T^2
\left\|{\mathcal L_5\over O_T}\right\|_{\mathcal D}^2.
}
\tag{T-106520.1}

This replaces the forbidden normalization by the complete denominator, which
would put an analytic source in `ker H_(U_T)`.

## 3. Exact sufficient estimate

Define `OUTERDIR106520` by

\[
\boxed{
\limsup_{T\to\infty}
{4\lambda_T^2
 \|\mathcal L_5/O_T\|_{\mathcal D}^2
 \over N(T,2T)}
< {97\over1000},
}
\tag{T-106520.2)

with common-zero, confluent, endpoint and cofinal-factorization errors included
in the displayed left side.

The endpoint Hankel inequality and the pinned unconditional input

\[
\liminf {R_5(T,2T)\over N(T,2T)}>{997\over1000}
\]

then give

\[
\boxed{
\mathrm{OUTERDIR}_{106520}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106520.3)

No source dimension, model-space coverage, denominator-multiplied Hardy bank,
or operator-norm approximation is assumed.

## 4. Two exact representations of the open quantity

The numerator is already an actual positive Xi current chaos:

\[
\widehat{\mathcal L_5}
={1\over16}
\left(5\xi^4\Lambda_2+10\xi^2\Lambda_4+\Lambda_6\right)\ge0.
\tag{T-106520.4)

At finite rational scope, `L-106509` also gives

\[
\left\|{N_T-D_T\over O_T}\right\|_{\mathcal D}^2
=m_{+,T}-m_{-,T}
-2\operatorname{Re}
\sum_{D_T(c)=0,\ \operatorname{Im}c>0}
{\nabla_{O_T}(N_T-D_T)(c)\over D_T'(c)}.
\tag{T-106520.5)

Thus `OUTERDIR106520` may be attacked either as an outer-weighted Dirichlet
mean value or as one covariant companion-residue sum.

## 5. Boundary

```text
fifth-endpoint telescope                       PROVED EXACT
actual Xi fifth Wronskian source               PROVED POSITIVE
common outer factor cancellation               PROVED TOPOLOGY SAFE
all-pass charge <= outer Dirichlet defect       PROVED EXACT
covariant residue representation               PROVED EXACT
OUTERDIR106520                                  OPEN / RECORD-BEARING
ninety percent for zeta                        UNPROVED
density one                                    UNPROVED
Riemann Hypothesis                             UNPROVED
```
