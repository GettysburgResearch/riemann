# L-21502 — Prime-quantile transport recurrence for the polygon margin

Claim ID: `L-21502`  
Title: The RH polygon margin is the cumulative barycentric transport surplus from the archimedean reference quantile to prime-power atoms  
Status: `PROPOSED — COMPLETE CONVEX-ANALYTIC IDENTITY`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21501`; elementary convex conjugacy  
Scope: exact positive attack on the cofinal polygon inequality

## 1. Two mass quantiles

Retain the prime-power masses and cumulative moments

\[
a_j={\Lambda(q_j)\over\sqrt{q_j}},
\qquad
\nu_j=\log q_j,
\qquad
A_j=\sum_{i\le j}a_i,
\qquad
B_j=\sum_{i\le j}a_i\nu_i.
\tag{L-21502.1}
\]

Define the prime quantile step function

\[
\boxed{
\nu_{\rm pp}(A)=\nu_j
\quad(A_{j-1}<A\le A_j).
}
\tag{L-21502.2}
\]

Let `F` be the strictly convex archimedean function of `L-21501`. Its conjugate is differentiable away from the initial boundary transition. Define the monotone reference quantile by the generalized inverse of `F'` on `[log 2,infinity)`:

\[
\boxed{
\tau_F(A)=
\begin{cases}
\log2,&A\le F'(\log2),\\
(F')^{-1}(A),&A>F'(\log2),
\end{cases}}
\tag{L-21502.3}
\]

where the first case is empty on `A>=0` if `F'(log 2)<0`. Then `tau_F` is the right derivative of `F*`, and

\[
F^*(A)-F^*(C)=\int_C^A\tau_F(s)\,ds
\qquad(0\le C\le A).
\tag{L-21502.4}
\]

## 2. Exact one-atom recurrence

Define the polygon margin

\[
\boxed{M_j=B_j-F^*(A_j).}
\tag{L-21502.5}
\]

Then

\[
\boxed{
M_j-M_{j-1}
=
\int_{A_{j-1}}^{A_j}
\bigl(\nu_j-\tau_F(A)\bigr)dA.
}
\tag{L-21502.6}
\]

### Proof

Since `B_j-B_(j-1)=a_j nu_j` and `A_j-A_(j-1)=a_j`,

\[
\begin{aligned}
M_j-M_{j-1}
&=a_j\nu_j-
  \bigl(F^*(A_j)-F^*(A_{j-1})\bigr)\\
&=\int_{A_{j-1}}^{A_j}
  \bigl(\nu_j-\tau_F(A)\bigr)dA.
\end{aligned}
\]

QED.

Thus the new prime-power atom transports an archimedean mass interval of exactly the same mass `a_j` to the single location `nu_j`. The margin increment is its barycentric transport surplus.

## 3. Global integrated-quantile identity

Put

\[
\boxed{M_0=-F^*(0).}
\tag{L-21502.7}
\]

This is one explicit archimedean constant; no sign or endpoint-location assertion is needed. Summing (L-21502.6) gives

\[
\boxed{
M_j
=M_0+
\int_0^{A_j}
\bigl(\nu_{\rm pp}(A)-\tau_F(A)\bigr)dA.
}
\tag{L-21502.8}
\]

Consequently the full RH criterion becomes

\[
\boxed{
\mathrm{RH}
\iff
M_0+\int_0^{A_j}
(\nu_{\rm pp}-\tau_F)dA\ge0
\quad\text{for every sufficiently large }j.
}
\tag{L-21502.9}
\]

This is an integrated-quantile, Lorenz-order, or stop-loss comparison between one explicit continuous reference measure `F''(t)dt` and the discrete prime-power measure

\[
\sum_ja_j\delta_{\nu_j}.
\]

## 4. Exact block certificate

For any block of consecutive prime powers `r<i<=s`,

\[
\boxed{
M_s-M_r
=
\sum_{i=r+1}^{s}a_i\nu_i
-
\int_{A_r}^{A_s}\tau_F(A)dA.
}
\tag{L-21502.10}
\]

Therefore a partition

\[
0=j_0<j_1<j_2<\cdots
\]

with

\[
\boxed{
\sum_{j_{r-1}<i\le j_r}a_i\nu_i
\ge
\int_{A_{j_{r-1}}}^{A_{j_r}}\tau_F(A)dA
}
\tag{L-21502.11}
\]

for every sufficiently late block proves that the margin is nondecreasing at the block endpoints. Combined with one finite initial moat and an intra-block lower bound, this proves the cofinal polygon inequality and hence RH.

This is the exact mass-transport theorem targeted by `M-21501`. It allows negative individual atom increments and asks only for cumulative barycentric domination.

## 5. Local slope gates

Because `tau_F` is increasing, the one-atom increment has immediate sufficient signs:

\[
\boxed{
A_j\le F'(\nu_j)
\quad\Longrightarrow\quad
M_j-M_{j-1}\ge0,
}
\tag{L-21502.12}
\]

and

\[
\boxed{
A_{j-1}\ge F'(\nu_j)
\quad\Longrightarrow\quad
M_j-M_{j-1}\le0.
}
\tag{L-21502.13}
\]

The discrepancy

\[
\Delta_j=A_j-F'(\nu_j)
\tag{L-21502.14}
\]

is exactly the negative right derivative of the screw function at the prime-power knot:

\[
\boxed{
\Delta_j=-\Psi'(\nu_j+).
}
\tag{L-21502.15}
\]

Hence the polygon margin is the integrated history of the same centered weighted-prime discrepancy that drives the square-screw route. Pointwise derivative control is sufficient but not necessary; the transport formulation preserves all favorable cancellation across prime-power blocks.

## 6. A Hall-type matching formulation

Let the reference mass interval `(A_(j-1),A_j]` be denoted `I_j`. A stronger sufficient theorem is the existence, after finitely many initial atoms, of a partition or fractional allocation of the reference mass to prime-power locations satisfying:

1. prime atom `j` receives total mass exactly `a_j`;
2. the average reference quantile assigned to atom `j` is at most `nu_j`;
3. every initial allocation deficit is covered by the finite margin `M_0`.

The total surplus of such an allocation is exactly the right side of (L-21502.8). Thus a constructive monotone or blockwise transport supplies a proof of RH without estimating an oscillatory zero sum.

The difficulty is sharp: PNT-level weak convergence of the two mass measures does not control every cumulative barycentric deficit. A successful matching theorem must use multiplicative prime structure at the order-one margin scale.

## 7. Relation to the other global routes

- The phase-complete prime-energy criterion measures the exponential type of the same signed discrepancy but squares after filtering.
- The centered infinite-notch route annihilates the line spectrum of the discrepancy but uses the complete line-zero set in its kernel.
- The Hausdorff route probes inverse moments of the same spectral charge and has an unconditional fixed-row saddle sector.
- The present transport identity is the only one of these formulations whose negative witnesses require no zero input and whose positive theorem is a direct finite-prefix arithmetic majorization.

These are complementary coordinates, not independent escapes from the same RH-strength sign.

## 8. Proof boundary

- Equations (L-21502.6), (L-21502.8), and (L-21502.10) are exact.
- No block partition satisfying (L-21502.11) is proved cofinally.
- The Hall-type allocation is a sufficient construction, not an existence theorem established here.
- A finite favorable transport does not prove RH.
- No RH resolution is claimed.
