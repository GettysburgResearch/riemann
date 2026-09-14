# L-106674 — Source-Pick free energy factors into topology and balanced phase

Claim ID: `L-106674`  
Status: **PROVED EXACT FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-27  
Depends on: `L-106512`, `L-106670`; principal-angle decomposition  
RH status: **not assumed**

Let

\[
U=\omega B_+\overline{B_-},
\qquad
m_\pm=\deg B_\pm,
\]

be reduced, and let

\[
Q=P_-(I-P_+)P_-\big|_{K_{B_-}}
\]

be the adverse canonical contraction.  Put

\[
d=(m_--m_+)_+.
\]

## 1. Forced unit spectrum

The compression `P_-P_+P_-` has rank at most `m_+`.  Hence, when
`m_->m_+`, it has at least `d` zero eigenvalues and `Q` has at least `d`
eigenvalues equal to one.  The remaining eigenvalues are the squared sines

\[
\mu_1,\ldots,\mu_r\in[0,1]
\]

of the matched principal angles, with `r<=min(m_+,m_-)`.  Consequently

\[
\boxed{
\det(I-\tau Q)
=(1-\tau)^d
\prod_{\nu=1}^r(1-\tau\mu_\nu),
\qquad 0<\tau<1.
}
\tag{L-106674.1}
\]

Define

\[
\mathfrak F_\tau(U)
=-{1\over\tau}\log\det(I-\tau Q),
\qquad
c(\tau)={-\log(1-\tau)\over\tau}.
\]

Then

\[
\boxed{
\mathfrak F_\tau(U)
=c(\tau)d
+
\sum_{\nu=1}^r{-\log(1-\tau\mu_\nu)\over\tau}.
}
\tag{L-106674.2}
\]

The first term is topological and cannot be reduced by frame conditioning,
source smoothing, or phase alignment.

## 2. Small-regularization limit

Let

\[
\mathfrak P_0(U)
=m_+-\operatorname{tr}(P_-P_+)
=\|H_{U^{-1}}\|_{\mathcal S_2}^2.
\]

If `m_->=m_+`, the matched-angle sum is exactly `mathfrak P_0(U)`, and

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=(m_--m_+)+\mathfrak P_0(U).
}
\tag{L-106674.3}
\]

Moreover

\[
\boxed{
\lim_{\tau\downarrow0}\mathfrak F_\tau(U)
=(m_--m_+)+\mathfrak P_0(U).
}
\tag{L-106674.4}
\]

Thus the lossless source-Pick scalar contains two logically distinct debts:

```text
signed endpoint index / unmatched dimension;
degree-zero reverse-oriented phase overlap.
```

## 3. Fifth-endpoint consequence

For the fifth endpoint, the signed global dimension difference is the exact
reverse-Rolle deficit

\[
\sum_j(m_{-,j}-m_{+,j})=R_5(T,2T)-R_0(T,2T)
\]

up to the declared common-zero, endpoint and confluent ledger.  Therefore any
proof of the full `97/1000` free-energy bound necessarily proves the same
`97/1000` bound for the positive unmatched endpoint index, before the
balanced phase term is even considered.

This is not circular bookkeeping: it identifies the rigid factor
`(1-tau)^d` inside the literal determinant.  It also explains why the
unregularized determinant vanishes whenever one unmatched adverse direction
is present.

## Scope

The lemma does not estimate either the endpoint index or the balanced phase
for Xi.  It rules out a proof that attempts to obtain the full determinant
bound solely by conditioning the matched Cauchy frame while leaving the
unmatched dimension untreated.
