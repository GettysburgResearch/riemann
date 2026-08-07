# L-19841 — The complete Poisson tail preserves the signed `d_4,d_6` hierarchy

Claim ID: `L-19841`  
Status: **PROPOSED EXACT TRANSFER THEOREM — ANALYTIC CROSS/UPPER BOUNDS SUPPLIED BY `L-19842`**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: pure signed prolate hierarchy `L-19823/L-19824`; exact first-alias orthogonality; complete branch/endpoint/alias theorem `L-19842`  
Scope: theorem 2 in the repaired prolate programme

## 1. Setup

Let `S_R` be the exact two-constraint signed prolate coefficient space and let

\[
 D_R^{(1)}\succ0
 \tag{L-19841.1}
\]

be the first-arithmetic-alias Gram in the ordinary coefficient metric `G_R`.
The exact leakage normalization identifies `D_R^(1)` with the diagonal
pure-prolate defect form. Write its generalized eigenvalues on `S_R` as

\[
 0<\theta_{1,R}^{(1)}\le\theta_{2,R}^{(1)}\le\cdots.
 \tag{L-19841.2}
\]

The signed theorem `L-19823` gives

\[
 \theta_{1,R}^{(1)}\le C_4d_4(R),
 \qquad
 \theta_{2,R}^{(1)}\ge c_6d_6(R),
 \qquad
 \frac{d_4(R)}{d_6(R)}=R^{-2+o(1)}.
 \tag{L-19841.3}
\]

Let `F_R:S_R->mathscr H_R` be the normalized first-alias synthesis, so

\[
 F_R^*F_R=I_{S_R}.
 \tag{L-19841.4}
\]

Let `H_R` synthesize every remaining Poisson alias, including all stationary,
fold, endpoint, and post-cutoff channels, in the same normalized coordinates.
The complete ordinary tail Gram is

\[
 \begin{aligned}
 D_R
 &=D_R^{(1)1/2}
   (F_R+H_R)^*(F_R+H_R)
   D_R^{(1)1/2}\\
 &=D_R^{(1)1/2}
   (I+C_R+P_R)
   D_R^{(1)1/2},
 \tag{L-19841.5}
 \end{aligned}
\]

where

\[
 C_R=F_R^*H_R+H_R^*F_R,
 \qquad
 P_R=H_R^*H_R\succeq0.
 \tag{L-19841.6}
\]

The positive self-energy `P_R` is retained exactly. It is never discarded or
required to be small.

## 2. Analytic input

Assume the complete theorem `L-19842`, which produces one support in every
sufficiently large dyadic block for which

\[
 \|C_R\|\le\epsilon_R,
 \qquad
 \epsilon_R\to0,
 \tag{L-19841.7}
\]

and

\[
 \|F_R+H_R\|^2\le K_R,
 \qquad
 K_R=\exp(o(\log R))=R^{o(1)}.
 \tag{L-19841.8}
\]

The second estimate is deliberately subpolynomial rather than uniformly
bounded. Endpoint logarithms, shrinking excluded resonance neighborhoods, and
the growing `O(log^2 R)` packet are all permitted.

## 3. Complete lower bound

From `P_R>=0` and (L-19841.7),

\[
 I+C_R+P_R\succeq(1-\epsilon_R)I.
 \tag{L-19841.9}
\]

Therefore

\[
 \boxed{
 D_R\succeq(1-\epsilon_R)D_R^{(1)}.}
 \tag{L-19841.10}
\]

The min--max principle gives, for every `j`,

\[
 \theta_{j,R}(D_R,G_R)
 \ge(1-\epsilon_R)\theta_{j,R}^{(1)}.
 \tag{L-19841.11}
\]

In particular,

\[
 \boxed{
 \theta_{2,R}(D_R,G_R)
 \ge(1-o(1))c_6d_6(R).}
 \tag{L-19841.12}
\]

This is the complete signed lower hierarchy. The `-1` sector is included; no
`d_8` complete-space claim remains.

## 4. Target upper bound

Let `u_R` be the exact normalized signed target vector from `L-19823`, so

\[
 \langle u_R,D_R^{(1)}u_R\rangle
 \le C_4d_4(R)\|u_R\|_{G_R}^2.
 \tag{L-19841.13}
\]

Using (L-19841.5) and (L-19841.8),

\[
 \begin{aligned}
 \langle u_R,D_Ru_R\rangle
 &\le K_R
 \langle u_R,D_R^{(1)}u_R\rangle\\
 &\le K_RC_4d_4(R)\|u_R\|_{G_R}^2.
 \end{aligned}
 \tag{L-19841.14}
\]

Hence

\[
 \boxed{
 \theta_{1,R}(D_R,G_R)
 \le K_RC_4d_4(R).}
 \tag{L-19841.15}
\]

Because `K_R=R^{o(1)}` and `d_4/d_6=R^{-2+o(1)}`,

\[
 \frac{K_Rd_4(R)}{d_6(R)}\longrightarrow0.
 \tag{L-19841.16}
\]

Combining (L-19841.12) and (L-19841.15),

\[
 \boxed{
 \theta_{1,R}=R^{o(1)}O(d_4(R)),
 \qquad
 \theta_{2,R}=\Omega(d_6(R)),
 \qquad
 \frac{\theta_{1,R}}{\theta_{2,R}}\to0.}
 \tag{L-19841.17}
\]

## 5. Fixed-target complement formulation

The spectral statement is the invariant form needed by the Rayleigh-floor
argument. If a fixed target-line Loewner estimate is desired, let `Pi_R` be the
`G_R`-orthogonal projection onto `span(u_R)` and put

\[
 \alpha_R=K_RC_4d_4(R).
 \tag{L-19841.18}
\]

For `v` in the target complement, min--max and the two-dimensional subspace
`span(u_R,v)` imply

\[
 \langle v,D_Rv\rangle
 \ge
 \bigl[(1-o(1))c_6d_6(R)-\alpha_R\bigr]
 \|v\|_{G_R}^2
 \tag{L-19841.19}
\]

up to the standard rank-one target-angle correction. Equivalently, after the
Rayleigh-floor lemma is applied,

\[
 D_R-\theta_{1,R}G_R
 \succeq
 (1-o(1))c_6d_6(R)G_R
 \quad\text{on the exact ground complement}.
 \tag{L-19841.20}
\]

The ground line converges projectively to `u_R` because its target Rayleigh
excess divided by the second-eigenvalue gap is bounded by

\[
 O\!\left(K_R\frac{d_4}{d_6}\right)=o(1).
 \tag{L-19841.21}
\]

## 6. Why positive alias energy is harmless

The earlier upper-bound ledger tried to prove absolute summability of every
alias norm and thereby make `H_R^*H_R` small. That is unnecessary and, for the
leading endpoint channel, generally false. Equation (L-19841.9) shows the exact
correct principle:

```text
positive rest/rest self-energy may be arbitrarily large;
only the first/rest Hermitian cross must be small from below.
```

For the target upper bound one needs only the subpolynomial complete synthesis
bound (L-19841.8), not smallness. This is why collective polylogarithm/sawtooth
summation is sufficient.

## 7. Exact proof boundary

- The transfer from the pure signed `d_4,d_6` hierarchy to the complete Poisson
  tail is proved exactly in Sections 1--5.
- The theorem uses one common coefficient metric and includes both Fourier-sign
  sectors.
- The analytic estimates (L-19841.7)--(L-19841.8) are not imported as anonymous
  constants; their branch, fold, endpoint, and infinite-alias proof is the
  content of `L-19842`.
- This theorem concerns the ordinary arithmetic tail Gram. Identifying the exact
  localized Weil matrix with `(log R)D_R` to relative `o(1)` is theorem 4,
  `L-19843`.
- No RH conclusion is claimed by this lemma alone.
