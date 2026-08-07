# T-20206 — Transcendental pinning makes the optimal Fejer filter RH-complete

Claim ID: `T-20206`  
Title: An arbitrarily small transcendental first-tap pin prevents every off-line pole cancellation while preserving the sharp `O(N^-2)` prime debt  
Status: **PROPOSED — COMPLETE POLE-EXPOSURE AND SAMPLING ARGUMENT PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the screw/Laplace normalization of `T-20201`; `L-20211`; Landau's one-sign theorem; Lindemann--Weierstrass  
Scope: one fixed finite positive filter for each degree `N>=2`

## 1. Algebraic endpoint filter

Fix an integer `N>=2`. Let

\[
 \alpha_N={\pi\over N+1},
 \qquad
 q_j^{(N)}=(-1)^j\sin((j+1)\alpha_N)
 \quad(0\le j<N),
\]

and put

\[
 Q_N(z)=\sum_{j=0}^{N-1}q_j^{(N)}z^j,
 \qquad
 A_N(z)=(1-z)Q_N(z),
\]

\[
 P_N(x)=|A_N(e^{ix})|^2
       =\sum_{k=1}^{N}\lambda_{N,k}^{(0)}(1-\cos kx).
\]

Every `q_j^(N)` and every `lambda_(N,k)^(0)` is algebraic, because roots of
unity are algebraic. The polynomial `P_N` is nonnegative and is the sharp
half-knot extremizer of `L-20208/L-20211`.

Choose

\[
\boxed{
 \eta_N=e^{-N}>0.}
\]

By Lindemann--Weierstrass, `eta_N` is transcendental. Define the pinned filter

\[
\boxed{
 \widetilde P_N(x)=P_N(x)+\eta_N(1-\cos x).}
\]

Thus

\[
 \widetilde\lambda_{N,1}
 =\lambda_{N,1}^{(0)}+\eta_N,
 \qquad
 \widetilde\lambda_{N,k}
 =\lambda_{N,k}^{(0)}\quad(k\ge2).
\]

Clearly

\[
 \widetilde P_N(x)\ge0
 \qquad(x\in\mathbb R).
\]

## 2. Pinned screw statistic

Define

\[
\boxed{
 \mathcal E_N(t)
 =\sum_{k=1}^{N}\widetilde\lambda_{N,k}\Psi(kt).}
\]

Under RH, the paired zero expansion gives

\[
\boxed{
 \mathcal E_N(t)
 =2\sum_{\gamma>0}{m_\gamma\over\gamma^2}
   \widetilde P_N(\gamma t)
 \ge0.}
\]

The Laplace transform is

\[
\boxed{
 \int_0^\infty\mathcal E_N(t)e^{izt}\,dt
 =-{1\over z^2}
  \sum_{k=1}^{N}k\widetilde\lambda_{N,k}
  {\xi'\over\xi}\left({1\over2}-{iz\over k}\right),}
\]

initially in the common half-plane of absolute convergence.

## 3. Transcendental pole pin

Suppose

\[
 \rho={1\over2}+w
\]

is an off-line zero with `Re(w)>0` and multiplicity `m>=1`. At

\[
 z_0=iw
\]

the `k=1` logarithmic derivative has a pole. For `k>=2`, the `k`-th term has a
pole at the same `z_0` only when

\[
 \rho_k={1\over2}+{w\over k}
\]

is also a zero; let its multiplicity be `m_k`, with `m_k=0` when it is not a
zero.

Since

\[
 {\xi'\over\xi}(s)
 ={m_k\over s-\rho_k}+O(1),
\]

the residue of the bracket at `z_0` is, up to the common nonzero factor `i`,

\[
\begin{aligned}
 \mathcal R
 &=(\lambda_{N,1}^{(0)}+\eta_N)m
   +\sum_{k=2}^{N}k^2\lambda_{N,k}^{(0)}m_k\\
 &=m\eta_N+\mathcal A,
\end{aligned}
\]

where `mathcal A` is algebraic: all base coefficients are algebraic and all
multiplicities are integers.

Because `m eta_N` is nonzero and transcendental, it cannot equal the algebraic
number `-mathcal A`. Hence

\[
\boxed{
 \mathcal R\ne0.}
\]

Every off-line zero therefore produces an uncancelled pole in the pinned
transform. No descendant maximum principle, multiplicity monotonicity, or
iteration is required.

Consequently, holomorphy of the displayed transform throughout `Im z>0` implies
RH directly.

## 4. Critical logarithmic sampling

For fixed `N`, the unconditional screw derivative budget gives

\[
 |\mathcal E_N'(t)|
 \le C_N(1+t)e^{Nt/2}.
\]

Use the critical mesh

\[
\boxed{
 t_n={2\log n\over N}.}
\]

Then

\[
 t_{n+1}-t_n=O(n^{-1})=O(e^{-Nt_n/2}),
\]

so interpolation between consecutive samples loses only a polynomial in
`log n`.

If, for every `epsilon>0`,

\[
 \mathcal E_N(t_n)
 \ge-C_\epsilon n^{2\epsilon/N}
\]

eventually, equivalently

\[
\boxed{
 (-\mathcal E_N(t_n))_+=n^{o(1)},}
\]

then the complete half-line has the lower envelope

\[
 \mathcal E_N(t)\ge-C'_\epsilon(1+t)^{B_\epsilon}e^{\epsilon t}.
\]

Adding the usual positive exponential-polynomial correction and applying
Landau's one-sign theorem makes the transform holomorphic in every half-plane
`Im z>epsilon`. Letting `epsilon` decrease to zero and invoking Section 3 gives
RH.

Thus, for every fixed `N>=2`,

\[
\boxed{
 RH
 \iff
 \mathcal E_N\left({2\log n\over N}\right)\ge0
 \text{ eventually},}
\]

and more weakly

\[
\boxed{
 RH
 \iff
 \left(-\mathcal E_N\left({2\log n\over N}\right)\right)_+
 =n^{o(1)}.}
\]

## 5. Near-optimal prime debt

Let `L_N` be the ramp of `P_N`. The pinned ramp is

\[
 \widetilde L_N(s)=L_N(s)+\eta_N(1-s)_+.
\]

The exact endpoint formulas of `L-20211` give

\[
 L_N(0)=N+1,
 \qquad
 L_N(1/2)=(N+1)\sin^2\!\left({\pi\over2(N+1)}\right).
\]

Therefore

\[
\boxed{
 {\widetilde L_N(1/2)\over\widetilde L_N(0)}
 ={
  (N+1)\sin^2(\pi/[2(N+1)])+e^{-N}/2
  \over
  N+1+e^{-N}}.}
\]

In particular,

\[
\boxed{
 {\widetilde L_N(1/2)\over\widetilde L_N(0)}
 ={\pi^2\over4N^2}+O(N^{-3})+O(e^{-N}/N).}
\]

The transcendental pin restores a rigorous off-line-zero exposure mechanism
without sacrificing the optimal quadratic decay of the unavoidable first-prime
debt.

## 6. Why this bridges the two cones

`L-20212` showed that:

- the simple positive multiplicity-descent cone is RH-complete but has half-knot
  debt at least `1/4`;
- the optimal endpoint Fejer cone has `O(N^-2)` debt but lacks that maximum
  principle.

The transcendental pin supplies a different exposure theorem. It makes residue
cancellation arithmetically impossible rather than forcing a positive descendant
average. Hence the pinned endpoint family has both:

1. exact RH completeness for every fixed degree;
2. asymptotically optimal `O(N^-2)` half-knot debt.

## 7. Proof-producing implications

For one chosen fixed large `N`, a production proof needs:

1. exact algebraic base coefficients and autocorrelations;
2. a typed symbolic coefficient `eta_N=e^{-N}`;
3. complete prime powers through the degree-`N` support cutoff;
4. directed pole, gamma, Lerch, and prime accumulation;
5. a cofinal symbolic sign or subpower negative-part estimate.

The transcendence argument belongs to the analytic theorem and is not replaced
by a floating decimal approximation to `e^{-N}`.

## 8. Proof boundary

- Spectral nonnegativity under RH is exact.
- Pole noncancellation uses only algebraicity of the endpoint coefficients,
  integrality of multiplicities, and transcendence of `e^{-N}`.
- The sampling/Landau step is inherited from `T-20201/T-20203` and remains
  proposed pending independent review.
- No cofinal sign estimate for the pinned filter is proved here.
- The theorem bridges false-RH exposure and optimal filter conditioning; it does
  not itself prove RH.
