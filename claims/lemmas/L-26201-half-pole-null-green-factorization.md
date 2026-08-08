# L-26201 — Half-pole-null Green factorization

Claim ID: `L-26201`  
Title: Completed dyadic pairs make every Green derivative kernel a rank-one Gram, and all failure of positivity is concentrated in two explicit boundary moments  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `R-26201`; exact carry Green generator from PR #243  
Scope: finite measures and finite source packets

## 1. Kernel factorization

For

\[
\phi(t)=8e^t-7e^{t/2}-\frac32te^{t/2},
\]

define the derivative Hankel form

\[
Q_r(\nu)=\iint\phi^{(r)}(x+y)d\nu(x)d\overline{\nu(y)}.
\]

With the weighted moments

\[
A=\int e^{x/2}d\nu,
\qquad
B=\int xe^{x/2}d\nu,
\qquad
C=\int e^xd\nu,
\]

one has

\[
\boxed{
Q_r(\nu)=8|C|^2-
\begin{pmatrix}\overline A&\overline B\end{pmatrix}
N_r
\begin{pmatrix}A\\B\end{pmatrix},}
\tag{L-26201.1}
\]

where

\[
\boxed{
N_r=2^{-r}
\begin{pmatrix}
7+3r&3/2\\
3/2&0
\end{pmatrix}.}
\tag{L-26201.2}
\]

The matrix `N_r` is indefinite. No positivity is claimed before the source
constraint is imposed.

## 2. Exact source constraint

If `A=0`, then

\[
\boxed{Q_r(\nu)=8|C|^2.}
\tag{L-26201.3}
\]

For a family of source columns `nu_j` with `A(nu_j)=0`, polarization gives

\[
\boxed{
[Q_r(\nu_j,\nu_k)]_{j,k}
=8cc^*,
\qquad
c_j=C(\nu_j),}
\tag{L-26201.4}
\]

so the whole packet Gram is positive semidefinite and has rank at most one.

## 3. Complete-pair operator

For `a>0`, let

\[
D_a=I-e^{-a/2}\tau_a.
\]

Every column of `D_a V` is half-pole-null. Hence

\[
\boxed{
Q_r(D_aV,D_aV)=8C(D_aV)C(D_aV)^*\succeq0.}
\tag{L-26201.5}
\]

This statement is exact for arbitrary finite source packets and does not use
Möbius cancellation, a zero-free region, or an asymptotic limit.

## 4. Boundary-jet Schur form

For an incompletely paired packet write

\[
\nu=\nu_{\rm pair}+\nu_{\rm bd},
\qquad A(\nu_{\rm pair})=0.
\]

All negative dependence of the Green derivative form is carried by

\[
J_{\rm bd}(\nu)=
\begin{pmatrix}A(\nu_{\rm bd})\\B(\nu_{\rm bd})\end{pmatrix}.
\]

After retaining all positive complete-pair and cross terms, a sufficient and
source-sharp finite condition is the Schur inequality

\[
\boxed{
R_{\rm bd}+D_{\rm bd}
\succeq
J_{\rm bd}^*N_rJ_{\rm bd},}
\tag{L-26201.6}
\]

where `R_bd` is a source-specific reflected block and `D_bd` is an exact digital
or boundary-spline reserve. This is the replacement interface developed in
`L-26204`.

## 5. Why this avoids the old refutation

The determinant `-233/64` tests arbitrary point masses and therefore violates
no statement above. Equation (L-26201.3) is restricted by the exact weighted
moment `A=0`; all directions with `A!=0` are exported to (L-26201.6).

The proposal does not claim that the number of boundary sources is bounded.
Each source contributes only two explicit jets, but the complete source manifest
may grow. This avoids the bounded-face-rank mistake refuted by the Möbius
hypercubes.

## 6. Proof boundary

Closed exactly:

- the moment factorization;
- packet polarization;
- positivity of completed weighted pairs;
- reduction of every negative term to boundary jets.

Open:

- the arithmetic boundary domination (L-26201.6);
- its cofinal summation;
- RH.
