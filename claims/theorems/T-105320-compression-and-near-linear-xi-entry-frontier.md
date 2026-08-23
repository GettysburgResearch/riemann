# T-105320 — Compression geometry and the near-linear Xi entry frontier

Claim ID: `T-105320`  
Status: **EXACT FINITE ADVANCE + PROPOSED ANALYTIC ADVANCE; LOW-ORDER BUDGET OPEN**  
Created: 2026-08-23  
Depends on: `L-105320--L-105322`; parent `T-105200`; PRs #720, #723  
RH status: **unproved**

## 1. Exact residue-compression dictionary

For a real-rooted monic polynomial with root matrix

\[
D=\operatorname{diag}(x_1,\ldots,x_n),
\]

let `C` be its compression to the zero-sum subspace and let

\[
b=PDe.
\]

`L-105320` proves the exact chain

\[
\boxed{
\begin{array}{c}
D\text{ and the uniform root vector }e\\
\Downarrow\\
C=PDP|_{e^\perp},\quad \det(zI-C)=p'(z)/n\\
\Downarrow\\
-U_p=n^{-1}\operatorname{Pin}_C(bb^*)\\
\Downarrow\\
\text{residue coherence}
=\text{inverse participation of }b\text{ in the }C\text{-eigenbasis}.
\end{array}
}
\tag{T-105320.1}
\]

The true second derivative is the compression of `C` in the uniform
critical-eigenbasis direction `h`; the physical two-step Krylov compression is
the compression in the normalized coupling direction `beta=b/||b||`.
Consequently

\[
\boxed{
\max_j|d_j-k_j|
\le
2\operatorname{diam}(C)
\sqrt{\min\left(1,{1-\mathfrak C(p)\over\mathfrak C(p)}\right)}.
}
\tag{T-105320.2}
\]

This is a new exact interpretation of the residue-coherence loss: it is the
angular defect between the derivative's uniform compression and the physical
Krylov compression of the root cloud.

The exact rational replay returns

```text
PASS_X_105320_ROOT_COMPRESSION_SCHUR
e3a54b6fa894ecaf87e860510ff9aa0f7c2858220327892328dd89b2d45b2d13
RH_UNPROVEN
```

with 97 checks.

## 2. Exact moving-saddle proposal

The finite Gaussian and cubic expansions on this branch are reorganized into
one exact moving saddle. For the positive Xi tilted measure, let
`u_(m,z)` solve

\[
S_m'(u_{m,z})+iz=0.
\]

`L-105321` proposes, for one fixed small `c_0>0`, the relative formula

\[
\boxed{
A_m(z)
=
\exp\!\left(
S_m(u_{m,z})-S_m(w_m)+izu_{m,z}
\right)
\left({\kappa_m\over-S_m''(u_{m,z})}\right)^{1/2}
(1+o(1))
}
\tag{T-105320.3}
\]

uniformly over every `m>=M` and

\[
|\Re z|\le c_0M/\log M,
\qquad |\Im z|\le H.
\]

This statement is stronger than the cubic truncation and is marked for
independent hostile review. Its load-bearing point is global dominance of the
shifted contour relative to the moving saddle, not merely local saddle
existence.

## 3. Proposed near-linear high-derivative entry

The odd part of the exact saddle logarithm defines an analytic phase
`Theta_m`. On every smaller box,

\[
\Re\Theta_m'(z)\ge w_m/2.
\]

`L-105322` uses exact phase cells and Rouché to derive

\[
\boxed{
\Xi^{(m)}\text{ has only real simple zeros in }
|\Re z|\le c_1M/\log M,\ |\Im z|\le H
}
\tag{T-105320.4}
\]

simultaneously for every `m>=M`, conditional only on the proposed contour
theorem `L-105321`.

The normative count is

\[
\boxed{
N_m(T)
={\Theta_m(T)-\Theta_m(-T)\over\pi}+O(1),
}
\tag{T-105320.5}
\]

with the coarser expansion

\[
N_m(T)={2w_mT\over\pi}+O(T).
\]

At every buffered critical point,

\[
\boxed{
{\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
=-w_m^{-2}(1+o(1)),
\qquad
\mathfrak C_{m,M}=1-o(1).
}
\tag{T-105320.6}
\]

Thus a height-`T` rectangle has the proposed unconditional terminal entry
order

\[
\boxed{r(T)=O(T\log T),}
\tag{T-105320.7}
\]

subject to independent verification of the exact-saddle contour proof.

## 4. Updated reverse-Rolle ledger

The parent exact transport remains

\[
O_{\Omega_T}(\Xi)
\le
O_{\Omega_T}(\Xi^{(r)})
+2\sum_{j<r}R_j(T)(1-\mathfrak C_j(T))
+\sum_{j<r}(B_j(T)+W_j(T)-1).
\tag{T-105320.8}
\]

Taking the proposed entry order (T-105320.7) removes the terminal term with
only `O(T log T)` intervening levels. The complete conclusion-facing statement
is still

\[
\boxed{
2\sum_{j<r(T)}R_j(T)(1-\mathfrak C_j(T))
+
\sum_{j<r(T)}(B_j(T)+W_j(T)-1)
<2.
}
\tag{CRDB105200}
\]

If this holds at every sufficiently large regular height, the even nonnegative
off-real count vanishes and RH follows. It is not proved here.

## 5. New geometric reading of the open budget

Whenever the derivative parent at level `j` is real-rooted, let `theta_j` be
the angle between its uniform derivative direction and physical Krylov
direction. Then

\[
\sin^2\theta_j
\le
\min\left(1,{1-\mathfrak C_j\over\mathfrak C_j}\right).
\tag{T-105320.9}
\]

Thus the residue part of `CRDB105200` is a weighted accumulated failure of the
derivative ladder to follow a Hermitian Krylov-compression flow. This
interpretation supplies a concrete spectral object for the next passes, but it
does not remove the first non-real-rooted level or the boundary winding.

## 6. Exact status

```text
root matrix -> derivative compression          PROPOSED EXACT / REPLAYED
residue operator = spectral pinching            PROPOSED EXACT
coherence = inverse participation               PROPOSED EXACT
coherence -> adjacent spectral-flow bound       PROPOSED EXACT
moving exact Xi saddle                          PROPOSED ANALYTIC / REVIEW REQUIRED
near-linear O(T log T) derivative entry         PROPOSED ANALYTIC / REVIEW REQUIRED
high-tail residue coherence                     PROPOSED ANALYTIC / REVIEW REQUIRED
low-order coherence and winding budget          OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
