# L-97202 — TFPE/ACBI is the exact factor-four average of the boundary defect

Claim ID: `L-97202`  
Status: **PROVED EXACT RECONSTRUCTION OF THE 97120 MATHEMATICS**  
Created: 2026-08-18  
PR #564 status: only `O-97120` was published; the formulas below are independently reconstructed  
RH status: **unproved**

For a finite odd-prime set `P`, let

\[
a_P=6(\delta_1-b_P),
\qquad
M_P(Y)=\sum_{n\le Y}\frac{a_P(n)}{\sqrt n}
      =6[1-\mathcal B_P(Y)].
\]

Define the scale-four hinge

\[
h_X(n)=\frac1{\sqrt n}\min\!\left(\log4,\log\frac Xn\right)_+.
\]

The elementary identity

\[
\min\!\left(\log4,\log\frac Xn\right)_+
=\int_{X/4}^{X}\mathbf1_{n\le y}\frac{dy}{y}
\]

gives the exact factorization

\[
\boxed{
A_{P,X}:=\sum_na_P(n)h_X(n)
       =\int_{X/4}^{X}M_P(y)\frac{dy}{y}.
}
\tag{L-97202.1}
\]

Thus TFPE is not pointwise RJTE. It is the factor-four moving-average inequality

\[
\boxed{A_{P,X}\ge0.}
\]

The finite overshoot in `R-97200` can coexist with a positive annular average.

## Bulk/defect split

Let

\[
B_{P,X}=\sum_{(n,P)=1}h_X(n),
\]

\[
\psi_X(d)=6h_X(d)-9h_X(2d)+3h_X(4d)\ge0,
\]

\[
D_{P,X}=\sum_{d\mid P}\mu(d)\psi_X(d).
\]

Finite coefficient comparison gives

\[
\boxed{A_{P,X}=6B_{P,X}-D_{P,X}.}
\tag{L-97202.2}
\]

The matrix

\[
\sum_{d\mid P}\psi_X(d)
\begin{pmatrix}1&\mu(d)\\\mu(d)&1\end{pmatrix}
\]

is PSD and has off-diagonal `D_(P,X)`. This reconstructs the parity Julia Gram.

## Bellman recurrence

For a new prime `p` not dividing `P`,

\[
\boxed{
A_{Pp,X}=A_{P,X}-p^{-1/2}A_{P,X/p}.
}
\tag{L-97202.3}
\]

With `U_P(X)=A_(P,X)/sqrt X`,

\[
U_{Pp}(X)=U_P(X)-p^{-1}U_P(X/p).
\]

Therefore the exact prime-adjoining sufficient inequality is

\[
\boxed{
\mathrm{ACBI}:\qquad U_P(X)\ge p^{-1}U_P(X/p).
}
\]

Equivalently,

\[
\boxed{
\mathrm{TFPE}:\qquad D_{P,X}\le6B_{P,X}.
}
\]

If TFPE/ACBI holds through the complete finite Euler system, the resulting annular scalar is nonnegative. Its Mellin transform has the zero-safe multiplier `1-4^{-s}`, so the real-`X` Mellin--Landau consumer yields RH.

TFPE/ACBI remains unproved. It is a legitimate smoothed replacement for RJTE, not metadata and not a consequence of Julia trace positivity alone.
