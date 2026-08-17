# L-97302 — Completed-parity scalar Hall is an exact finite Lorenz linear program

Claim ID: `L-97302`  
Status: **PROVED EXACT FINITE-DIMENSIONAL REDUCTION**  
Created: 2026-08-17  
Depends on: `L-97300`; PR #561 `L-96503`; PR #567 `T-97200`  
RH status: **unproved**

Fix one endpoint `X` and fully expand its finite rough source with cumulative
parity retained.  Let the actual even atoms be indexed by `i=1,...,M`.  Atom
`i` has available coefficient `a_i>=0`, strictly positive target `t_i`, and
scalar row coordinate

\[
r_i=5R_2(i)+3R_3(i).
\]

Let the full odd source have target demand and scalar demand

\[
T_O=\sum_o b_ot_o,
\qquad
R_O=\sum_o b_or_o.
\]

The scalar common-source problem is to find

\[
0\le u_i\le a_i
\]

such that

\[
\sum_i t_i u_i=T_O,
\qquad
\sum_i r_i u_i\ge R_O.
\tag{L-97302.1}
\]

Put `T_E=sum_i a_i t_i`.  For `0<=T<=T_E`, define

\[
\Phi_X(T)=
\max\left\{
\sum_i r_i u_i:
0\le u_i\le a_i,
\ \sum_i t_i u_i=T
\right\}.
\tag{L-97302.2}
\]

Then (L-97302.1) is feasible if and only if

\[
\boxed{T_O\le T_E\quad\text{and}\quad R_O\le\Phi_X(T_O).}
\tag{L-97302.3}
\]

## Explicit Lorenz formula

Order the even atoms so that

\[
\theta_1\ge\theta_2\ge\cdots\ge\theta_M,
\qquad
\theta_i=\frac{r_i}{t_i}.
\]

Let

\[
A_k=\sum_{i\le k}a_it_i,
\qquad A_0=0.
\]

For the unique `k` with `A_{k-1}<=T<=A_k`,

\[
\boxed{
\Phi_X(T)=
\sum_{i<k}a_ir_i+
\theta_k(T-A_{k-1}).
}
\tag{L-97302.4}
\]

Thus the optimal scalar source spends target capacity in decreasing order of
scalar-per-target ratio and uses at most one fractional terminal atom.

## One-parameter dual

The same value has the exact dual representation

\[
\boxed{
\Phi_X(T)=
\min_{\lambda\in\mathbb R}
\left[
\lambda T+
\sum_i a_i(r_i-\lambda t_i)_+
\right].
}
\tag{L-97302.5}
\]

Consequently, if `R_O>Phi_X(T_O)`, an optimizing threshold `lambda` is an
explicit separating functional for the entire completed-parity scalar cone.

## Proof

This is the continuous fractional-knapsack theorem.  If two non-boundary
coefficients satisfy `theta_i>theta_j`, transfer a small target amount from `j`
to `i`; the target equality is unchanged and the scalar objective increases.
Hence all larger ratios are saturated before any smaller ratio is used, proving
(L-97302.4).  Equation (L-97302.5) is weak duality followed by equality at a
threshold `lambda=theta_k`.

## Scope firewall

The theorem is source-complete at the target-plus-scalar-row scope used in PR
#567 `GPHT*`.  A stronger physical packet may also demand a score inequality or
additional typed coordinates; those create a multi-resource LP and are **not**
erased by (L-97302.4).

Uniform validity of (L-97302.3) for every endpoint is the completed-parity
scalar Lorenz producer `CPSL67`.  It is not proved here.
