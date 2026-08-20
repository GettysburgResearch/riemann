# T-100610 — First-owner and largest-owner collar energies form an exact AND-gate to RH

Claim ID: `T-100610`  
Status: **PROVED CONDITIONAL COMPOSITION; TWO COLLAR ENERGIES OPEN; RENEWAL REFERENCES REMOVED**  
Created: 2026-08-20  
Depends on: `L-100610--L-100615`; PR #676 detector  
RH status: **unproved**

Let

\[
F_k(X)=\prod_{i=1}^k(I-r_iU_i)\Psi(X),
\qquad
L_i=\prod_{h<i}(1-r_h),
\qquad
R_i=\prod_{h>i}(1-r_h),
\]

where the two copies of `67` remain distinct labels and `Psi` is the critical cubic kernel.

For `i<j`, put

\[
H_{ij}^{(k)}(X)
=(I-U_i)(I-U_j)E_{i+1:j-1}\Psi(X).
\]

`L-100614` gives the explicit nonnegative carrier

\[
M_{ij}^{(k)}(X)
=192\sqrt X(1-p_i^{-1/2})(1-p_j^{-1/2})
\prod_{i<h<j}(1-p_h^{-1})
\]

and the centered collar entry

\[
\widetilde H_{ij}^{(k)}=H_{ij}^{(k)}-M_{ij}^{(k)}.
\]

The two-ended hazard identity and cubic endpoint positivity imply

\[
\boxed{
(F_k(X))_-
\le
\sum_{i<j}r_ir_jL_iR_j
|\widetilde H_{ij}^{(k)}(X)|.
}
\tag{T-100610.1}
\]

Define

\[
\mathfrak R_k(X)
=
\sum_{i<j}r_ir_jL_i^2
|\widetilde H_{ij}^{(k)}(X)|,
\]

\[
\mathfrak C_k(X)
=
\sum_{i<j}r_ir_jR_j^2
|\widetilde H_{ij}^{(k)}(X)|.
\]

Cauchy--Schwarz on the pair index gives exactly

\[
\boxed{
(F_k(X))_-
\le
\sqrt{\mathfrak R_k(X)\mathfrak C_k(X)}.
}
\tag{T-100610.2}
\]

Thus the two conditions

\[
\sup_k\int_1^Y\mathfrak R_k(X){dX\over X}=Y^{o(1)},
\qquad
\sup_k\int_1^Y\mathfrak C_k(X){dX\over X}=Y^{o(1)}
\tag{T-100610.3}
\]

imply subpower logarithmic negative mass for the complete cubic source after finite-source exhaustion.  The centered-cubic Mellin--Landau theorem then yields

\[
\boxed{
\mathrm{FOCR100610}\wedge\mathrm{LOCR100610}
\Longrightarrow RH.
}
\tag{T-100610.4}
\]

`L-100612--L-100615` remove the root, singleton, fully active, ratio-eight, and every asymptotic interval `q<=p^A` with `A<e^(3/4)` from the unknown collar matrix.

## Audit correction

The proof of (T-100610.1)--(T-100610.4) uses only the exact hazard tensor, carrier subtraction, and two-sided Schur inequality.  It does **not** use the withdrawn `HDRB100603` or `ODSB100604` reductions.  Finite squaring remains an internal forward coordinate, but PR #671's divisor renewal is unavailable unless a literal divisor restriction is separately produced.

```text
two-ended hazard identity                 proved exact
two-sided Schur AND-gate                   proved exact
short/power-width positive regions         proved
positive-renewal long-region shortcut      withdrawn
FOCR100610                                 open
LOCR100610                                 open
Riemann Hypothesis                         unproved
```
