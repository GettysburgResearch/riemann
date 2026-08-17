# T-97200 — Source-complete single-scalar frontier after the parity correction

Claim ID: `T-97200`  
Status: **PROVED EXACT CONDITIONAL REDUCTION; GLOBAL PRODUCER OPEN**  
Created: 2026-08-17  
Inputs: `L-97000`, PR #561 `L-96503`, `L-97200`, PR #564

Put

\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]

After the entire finite rough-prime tree is expanded and every history parity is
incorporated as in `L-97200`, let `E_X` and `O_X` be the actual positive even and
odd source atoms. Each atom has its native target coordinate and scalar row
coordinate `R_*=5R_2+3R_3`.

Define `GPHT*` to be the following all-endpoint assertion. For every `X`, there
are coefficients `0\le u_e\le a_e` on the even atoms such that the same
coefficients simultaneously satisfy

\[
\sum_e u_e t_e=\sum_o b_o t_o,
\qquad
\sum_e u_e R_*(e)\ge\sum_o b_o R_*(o).
\tag{T-97200.1}
\]

This is source-complete: no history is collapsed before the single common
coefficient vector is chosen, every source coefficient is spent at most once,
and odd histories enter with their swapped orientation.

If `GPHT*` holds, write `U_X=\sum_eu_e e`. Then

\[
\begin{aligned}
R_*(E_X)-R_*(O_X)
&=R_*(E_X-U_X)+R_*(U_X)-R_*(O_X)\\
&\ge0.
\end{aligned}
\]

Hence `\mathcal R_X\ge0` for every `X`. The exact Mellin identity from
`L-97000` is

\[
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)},
\qquad z=s+\frac12.
\]

Its finite numerator has no zero in `\Re z>0`. The fixed-sign Mellin–Landau
consumer therefore gives

\[
\boxed{\mathrm{GPHT*}\Longrightarrow\mathcal R_X\ge0\ (\forall X)
\Longrightarrow \mathrm{RH}.}
\tag{T-97200.2}
\]

At each fixed endpoint, feasibility versus a finite separating functional is an
exact compact-convex primal-dual alternative by PR #561 `L-96503`. Uniform
feasibility for all endpoints remains open and RH-bearing.

PR #564 supplies an equivalent all-depth scalar frontier in the finite-prime
state variables:

\[
\mathrm{TFPE}:\quad D_{P,X}\le6B_{P,X},
\]

or recursively

\[
\mathrm{ACBI}:\quad U_P(X)\ge p^{-1}U_P(X/p).
\]

Thus the strongest correct successor is the exact source-complete reduction
`GPHT*` / `TFPE` / `ACBI`; the parity-blind leafwise theorem is withdrawn.

```text
parity-covariant atomwise ledger        PROVED EXACT INTERFACE
leafwise parity-blind promotion          REFUTED
finite primal-dual alternative           PROVED EXACT
GPHT* / TFPE / ACBI                      OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
