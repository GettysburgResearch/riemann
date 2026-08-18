# L-97700 — Source-faithful Lorenz dual slack and the exact rough-prime recurrence

Claim ID: `L-97700`  
Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

## 1. Paired source state

A finite paired source is an ordered pair

\[
\mathcal P=(E,O)
\]

of positive atom families. An atom is a quadruple

\[
(a,t,r,\omega),\qquad a\ge0,\quad t>0,\quad r\ge0,
\quad \omega\in\{+,-\},
\]

where `a` is available source capacity, `t` is the target coordinate, `r` is the `5:3` scalar coordinate, and `omega` is cumulative rough-history parity. The swap is \(\mathsf S(E,O)=(O,E)\).

Write \(T_E=\sum_{i\in E}a_it_i\), \(R_E=\sum_{i\in E}a_ir_i\), and similarly for `O`. For real `lambda`, put

\[
H_E(\lambda)=\sum_{i\in E}a_i(r_i-\lambda t_i)_+,
\qquad
H_O(\lambda)=\sum_{i\in O}a_i(r_i-\lambda t_i)_+.
\]

Define the two oriented Lorenz dual slacks

\[
\boxed{D_{\mathcal P}^+(\lambda)=\lambda T_O+H_E(\lambda)-R_O,}
\tag{L-97700.1}
\]

\[
\boxed{D_{\mathcal P}^-(\lambda)=\lambda T_E+H_O(\lambda)-R_E.}
\tag{L-97700.2}
\]

The `+` orientation asks even source to pay odd demand; the `-` orientation is the reversed problem. The definitions retain target, scalar, capacity and cumulative parity in one state.

## 2. Exact completed-parity Lorenz dual

The forward source problem is

\[
0\le u_i\le a_i,
\qquad
\sum_{i\in E}t_i u_i=T_O,
\qquad
\sum_{i\in E}r_i u_i\ge R_O.
\tag{L-97700.3}
\]

Its fractional-knapsack dual is

\[
\Phi(T_O)-R_O=\min_{\lambda\in\mathbb R}D_{\mathcal P}^+(\lambda).
\tag{L-97700.4}
\]

Consequently (L-97700.3) is feasible if and only if

\[
\boxed{D_{\mathcal P}^+(\lambda)\ge0\quad\text{for every real }\lambda.}
\tag{L-97700.5}
\]

Target insufficiency is included: if \(T_E<T_O\), then \(D^+(\lambda)\to-\infty\) as \(\lambda\to-\infty\). If target capacity holds, negative `lambda` gives

\[
D^+(\lambda)=R_E-R_O+\lambda(T_O-T_E),\qquad \lambda<0,
\tag{L-97700.6}
\]

and is no smaller than its value at zero. For nonnegative `lambda`, every finite minimum occurs at zero or at an even atom ratio \(r_i/t_i\).

## 3. Universal cushion

For every paired source,

\[
\boxed{D_{\mathcal P}^+(\lambda)+D_{\mathcal P}^-(\lambda)=\sum_{i\in E\cup O}a_i(\lambda t_i-r_i)_+\ge0.}
\tag{L-97700.7}
\]

Thus \(D^-\ge-D^+\). At `lambda=0`, the cushion vanishes and

\[
D^+(0)=R_E-R_O,\qquad D^-(0)=-(R_E-R_O).
\tag{L-97700.8}
\]

## 4. Covariance

For positive direct sums and `c>=0`,

\[
D_{\mathcal P\oplus\mathcal Q}^{\pm}=D_{\mathcal P}^{\pm}+D_{\mathcal Q}^{\pm},
\qquad D_{c\mathcal P}^{\pm}=cD_{\mathcal P}^{\pm},
\]

and

\[
D_{\mathsf S\mathcal P}^+=D_{\mathcal P}^-,
\qquad D_{\mathsf S\mathcal P}^-=D_{\mathcal P}^+.
\tag{L-97700.9}
\]

## 5. Exact rough-prime recurrence

Let \((U_p\mathcal P)_X=\mathcal P_{X/p}\) and \(\rho_p=p^{-1/2}\). Source covariance gives the literal identity

\[
\mathcal P_{Q\cup\{p\},X}=\mathcal P_{Q,X}\oplus\rho_p\mathsf S\mathcal P_{Q,X/p}.
\tag{L-97700.10}
\]

Every atom retains its actual first owner and coefficient; no child capacity is promoted and no signed observation is inserted into a positive source ledger. Therefore

\[
\boxed{D_{Q\cup\{p\}}^+(X,\lambda)=D_Q^+(X,\lambda)+\rho_pD_Q^-(X/p,\lambda),}
\tag{L-97700.11}
\]

\[
\boxed{D_{Q\cup\{p\}}^-(X,\lambda)=D_Q^-(X,\lambda)+\rho_pD_Q^+(X/p,\lambda).}
\tag{L-97700.12}
\]

## 6. Source-faithful current form

For the contracted identity

\[
\mathcal P_v=\mathcal C_v\oplus\bigoplus_w t_{vw}\mathsf S\mathcal P_w,
\qquad t_{vw}\ge0,
\tag{L-97700.13}
\]

let `G_v^+` be the forward Lorenz slack of the positive current packet. Then

\[
D_v^+=G_v^++\sum_wt_{vw}D_w^-.
\tag{L-97700.14}
\]

Define

\[
\boxed{\mathfrak B_v(\lambda)=G_v^+(\lambda)-\sum_wt_{vw}D_w^+(\lambda).}
\tag{L-97700.15}
\]

Using (L-97700.7),

\[
\boxed{D_v^+(\lambda)=\mathfrak B_v(\lambda)+\sum_wt_{vw}(D_w^+(\lambda)+D_w^-(\lambda)).}
\tag{L-97700.16}
\]

Therefore \(\mathfrak B_v\ge0\) is a source-faithful sufficient Bellman theorem for completed-parity Lorenz feasibility. At zero the cushion vanishes and \(\mathfrak B_v(0)=D_v^+(0)\).