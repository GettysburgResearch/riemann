# L-106700 — Every primal Cauchy transport retains the endpoint topological floor

Claim ID: `L-106700`  
Status: **PROVED EXACT FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-27  
Depends on: `L-106512`, `L-106630--L-106631`  
RH status: **not assumed**

Let

\[
U=\omega B_+\overline{B_-}
\]

be a reduced finite inner quotient on the upper half-plane, with model-space projections

\[
P_\pm=P_{K_{B_\pm}},\qquad m_\pm=\operatorname{rank}P_\pm.
\]

Define

\[
\mathfrak C_-(U)=\operatorname{tr}\bigl(P_-(I-P_+)\bigr),
\]

\[
\mathfrak C_+(U)=\operatorname{tr}\bigl(P_+(I-P_-)\bigr).
\]

## 1. Exact index decomposition

Since

\[
\operatorname{tr}(P_-P_+)=\operatorname{tr}(P_+P_-),
\]

one has

\[
\boxed{\mathfrak C_-(U)-\mathfrak C_+(U)=m_- -m_+=-\operatorname{wind}U.}
\tag{L-106700.1}
\]

Consequently,

\[
\boxed{\mathfrak C_-(U)=-\operatorname{wind}U+\mathfrak C_+(U).}
\tag{L-106700.2}
\]

The adverse Hankel charge is the signed topological loss plus one nonnegative favorable-space escape. It can never lie below the adverse index.

## 2. Every explicit transport has three nonnegative debts

Let

\[
E_-:\mathbb C^{m_-}\to\mathcal H,\qquad E_+:\mathbb C^{m_+}\to\mathcal H
\]

synthesize full-rank frames for the two model spaces, with Grams `G_±` and cross Gram `C`. For a matrix `X`, let `R(X)` be the generalized residual of `L-106630`.

The completion of the square gives

\[
\mathcal R(X)=\mathfrak C_-(U)+\mathfrak E_X,
\]

where

\[
\mathfrak E_X=\operatorname{tr}\!\left[G_-^{-1}(X-X_*)^*G_+(X-X_*)\right]\ge0,
\qquad X_*=G_+^{-1}C^*.
\]

Combining with (L-106700.2),

\[
\boxed{\mathcal R(X)=-\operatorname{wind}U+\mathfrak C_+(U)+\mathfrak E_X.}
\tag{L-106700.3}
\]

If a selected numerator subfactor `A_+ | B_+` is used, there is one further nonnegative omission debt

\[
\mathfrak E_{\rm sub}=\operatorname{tr}\bigl(P_-(P_+-P_{A_+})\bigr)\ge0,
\]

and

\[
\boxed{\mathcal R_{A_+}(X)=-\operatorname{wind}U+\mathfrak C_+(U)+\mathfrak E_{\rm sub}+\mathfrak E_X.}
\tag{L-106700.4}
\]

Thus no transport ansatz, whitening, numerator selection, or exact solution of the normal equations can remove the topological reverse--Rolle loss.

## 3. Shallow/deep endpoint split

Let

\[
B_-=B_-^{\rm sh}B_-^{\rm deep}.
\]

The model-space decomposition

\[
K_{B_-}=K_{B_-^{\rm sh}}\oplus B_-^{\rm sh}K_{B_-^{\rm deep}}
\]

is orthogonal, hence the full adverse charge splits exactly. For every shallow transport certificate `X`,

\[
\boxed{\mathcal R_{\rm sh}(X)+\mathfrak C_{\rm deep}(U)\ge-\operatorname{wind}U.}
\tag{L-106700.5}
\]

For the fifth endpoint,

\[
-\operatorname{wind}U_5=R_5-R_0
\]

up to the declared finite-window, common-zero and confluent ledger. Therefore

\[
\boxed{\mathcal R_{\rm sh}(X)+\mathfrak C_{\rm deep}(U_5)\ge R_5-R_0-\mathcal E_{\rm reg}.}
\tag{L-106700.6}
\]

Equation (L-106700.6) is the exact no-free-lunch boundary of `MESOTRANS106630`.
