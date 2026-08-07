# L-23002 — Critical correlation / transport gate

Claim ID: `L-23002`  
Title: One signed near-resonance estimate simultaneously closes the dyadic transport, prime-energy, and totient-energy routes  
Status: **OPEN PROPOSED LEMMA — THIS IS THE LOAD-BEARING GAP IN T-23001**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: PR #218 dyadic transport; PRs #216/#222/#224 prime-only Hardy energy; PR #226 analytic-totient energy  
Scope: cofinal, not finite; all normalizations must be source-bound before promotion

## 1. Dyadic transport formulation

Let

\[
 J_r=[r\log2,(r+1)\log2]
\]

and let `T_j=log q_j` run over its prime-power knots. In the notation of
`L-20208/L-20209`, define

\[
 \mathfrak M_{r,j}
 =H_r^*(A_j)-B_j-D_{H_r}(T_j,\tau_{r,j}),
 \qquad
 \tau_{r,j}=(H_r')^{-1}(A_j).
 \tag{L-23002.1}
\]

The exact identity on PR #218 is

\[
 \mathfrak M_{r,j}
 =\widetilde{\mathcal D}_r(T_j/r).
 \tag{L-23002.2}
\]

The required cofinal estimate is

\[
 \boxed{
 \max_j(-\mathfrak M_{r,j})_+
 +\sum_{\text{two endpoints}}(-\mathfrak M_{r,\partial})_+
 \le C_\varepsilon e^{\varepsilon r}}
 \tag{L-23002.3}
\]

for every `epsilon>0` and all sufficiently large `r`.

By the exact concavity/knot reduction and the `O(r)` endpoint stitching, this
implies the complete dyadic-cell lower envelope and hence RH through the Landau
and pole-exposure theorems.

## 2. Curvature-normalized sufficient form

Let

\[
 m_r=\inf_{T\in J_r}H_r''(T)>0.
\]

It is enough to prove

\[
 \boxed{
 H_r^*(A_j)-B_j
 \ge {\left[A_j-H_r'(T_j)\right]^2\over2m_r}
      -C_\varepsilon e^{\varepsilon r}.}
 \tag{L-23002.4}
\]

The left side is the one-sided prime-quantile transport reserve. The square on
the right is the centered cumulative prime-mass discrepancy. The theorem must
retain both; an absolute PNT estimate or an un-oriented `L2` estimate is
insufficient.

## 3. Prime-only Hardy formulation

Let `Q_H^P` be the ordinary-prime, boundary-safe signal of PR #216. The
corresponding sufficient estimate is

\[
 \boxed{
 \int_X^{X+1}|Q_H^P(x)|^2dx
 \le C_\varepsilon e^{\varepsilon X}}
 \tag{L-23002.5}
\]

uniformly on the right, or the locally uniform vertical-line form of PR #224.
After exact diagonal removal, PRs #216/#222 identify the remaining term as a
finite signed system of balanced squarefree-semiprime Type-II cells.

The load-bearing estimate is not an entrywise bound. It is cancellation in the
**common signed cell sum**.

## 4. Analytic-totient formulation

Let

\[
 E^{\rm AN}(x)
 ={1\over2}\left[1+\sum_{d\le x}\mu(d)\{x/d\}^2\right]
\]

in the normalization of PR #226. The corresponding critical estimate is

\[
 \boxed{
 \int_X^{2X}|E^{\rm AN}(t)|^2dt
 \ll_\varepsilon X^{2+\varepsilon}.}
 \tag{L-23002.6}
\]

The complete-period resonances already admit the positive Jordan-totient square
factorization of PR #226. A standard large sieve controls separated Farey
frequencies. The only unresolved portion is the Möbius-weighted critical
near-resonance cluster, where denominators of size `D` have frequency spacing
`D^-2` but the physical interval has length only `D`.

## 5. Proposed common-cell estimate

A proof-facing version of the remaining arithmetic statement is the following.
For every smooth coefficient sequence `c_k` arising from the fixed safe window,
and every dyadic denominator block `d,e asymp D`, prove

\[
 \boxed{
 \begin{aligned}
 &\sum_{d,e\asymp D}\mu(d)\mu(e)
  \sum_{k,\ell\ne0}c_k\overline{c_\ell}\,
  \mathcal J_D\!\left({k\over d}-{\ell\over e}\right)\\
 &\hspace{35mm}\ll_\varepsilon D^{2+\varepsilon},
 \end{aligned}}
 \tag{L-23002.7}
\]

where

\[
 \mathcal J_D(\alpha)=\int_D^{2D}e^{2\pi i\alpha x}\,dx,
\]

**after** the exact-resonance Jordan square is extracted and before absolute
values are taken.

The analogous prime formulation is the signed common-cell Type-II bound of PR
#222. Under the exact Mellin/finite-difference dictionaries, (L-23002.7) is the
same critical local-to-Bohr phenomenon measured in denominator rather than
prime coordinates.

## 6. Partial proof already available

The repository collectively supplies:

1. exact diagonal and exact-resonance factorizations;
2. polynomial bounds for the diagonal;
3. far-frequency large-sieve control;
4. finite signed cubic cell decompositions;
5. explicit pole-free multipliers and vertical pole tomography;
6. exact Selberg analytic squares for real exponential tests (`L-23001`);
7. proof that phase-blind absolute values lose a full exponential factor;
8. proof that frequency resolution fine enough to diagonalize the cells creates
   the same forbidden loss.

Thus (L-23002.7) concerns only the genuinely critical near-resonant signed
cluster.

## 7. Attempted closing mechanism

The most plausible route is a three-part decomposition:

1. parameterize near-resonances by
   \[
   ke-\ell d=h,
   \qquad |h|\ll1;
   \]
2. use the Möbius factors to apply a two-dimensional Vaughan/Heath-Brown or
   Selberg dispersion identity *before* summing over `h`;
3. identify the `h=0` term with the existing positive Jordan/semiprime square
   and show the total `h!=0` leakage is `D^{2+o(1)}`.

No repository branch currently proves Step 3 at the critical length. Standard
large sieve gives one extra power, while entrywise absolute values are
exponentially too large in the prime coordinate.

## 8. Status boundary

This file is deliberately not labeled proved. It is the smallest common
arithmetic statement left after the repository-wide synthesis.

A proof of any one of (L-23002.3), (L-23002.5), (L-23002.6), or the appropriately
normalized common-cell estimate (L-23002.7) completes the corresponding global
chain to RH. No such proof is currently present in the repository or claimed
here.
