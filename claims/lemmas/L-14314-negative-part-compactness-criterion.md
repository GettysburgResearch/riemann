# L-14314 — One-sided collective compactness closes only the negative low spectrum

Claim ID: `L-14314`  
Title: Strong convergence to a nonnegative limit plus collective compactness of the negative parts forces a vanishing lower-floor defect  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14312`; continuous functional calculus for uniformly bounded self-adjoint operators; `T-14302`  
Scope: the corrected growing low matrices when positive critical-line modes need not vanish  
Related counterexample candidates: none

## Motivation

`L-14312` proves `||K_j||->0` from full collective compactness. That is
stronger than the RH lower-floor program needs: harmless positive directions in
the generalized-prolate packet may retain nonzero energy. Only the negative
part must disappear.

For a bounded self-adjoint operator `K`, write

\[
 K_-:=(-K)_+=\max\{-K,0\}.
 \tag{L-14314.1}
\]

Then

\[
 \lambda_{\min}(K)\ge-\|K_-\|.
\]

## Main theorem

Let `K_j` be bounded self-adjoint operators on one Hilbert space `H`. Assume

\[
 \sup_j\|K_j\|<\infty,
 \tag{L-14314.2}
\]

\[
 K_j\longrightarrow K
 \quad\hbox{strongly},
 \tag{L-14314.3}
\]

and

\[
 K\succeq0.
 \tag{L-14314.4}
\]

Suppose the negative parts

\[
 N_j=(K_j)_-
\]

are collectively compact; equivalently, for fixed finite-rank projections
`P_m -> I` strongly,

\[
 \boxed{
 \lim_{m\to\infty}\sup_j\|(I-P_m)N_j\|=0.}
 \tag{L-14314.5}
\]

Then

\[
 \boxed{\|N_j\|\longrightarrow0,}
 \tag{L-14314.6}
\]

and hence

\[
 \boxed{\liminf_j\lambda_{\min}(K_j)\ge0.}
 \tag{L-14314.7}
\]

### Proof

All spectra lie in one compact interval `[-C,C]`. The continuous function

\[
 f(x)=\max\{-x,0\}
\]

can be uniformly approximated there by real polynomials. Strong convergence
of the uniformly bounded self-adjoint operators implies strong convergence of
every polynomial, and therefore

\[
 N_j=f(K_j)\longrightarrow f(K)=0
\]

strongly. Apply `L-14312` to the positive self-adjoint family `N_j`, using
(L-14314.5). This gives (L-14314.6), and (L-14314.7) follows. QED.

## Dense-core adapter

It is enough to verify `K_jx->Kx` on a dense common core, provided
(L-14314.2) holds. Thus an exact fixed-mode computation may establish the
strong-limit part of the theorem. What it cannot establish is the separate
negative-part tightness (L-14314.5).

## Quantitative form

If a packet proves

\[
 \|(I-P_m)N_j\|\le\delta_{j,m}
\]

and

\[
 \|P_mN_jP_m\|\le\rho_{j,m},
\]

then

\[
 \boxed{
 \max\{0,-\lambda_{\min}(K_j)\}=\|N_j\|
 \le\rho_{j,m}+2\delta_{j,m}.}
 \tag{L-14314.8}
\]

A proof checker need not trust a floating spectral decomposition. It may use a
rational polynomial majorant `p(x)>=max(-x,0)` on a directed spectral interval,
and certify the corresponding finite matrix inequalities exactly.

## Application to the corrected low matrix

Embed

\[
 K_j=B_j-h_j^{-1}R_j^*M_j^{-1}R_j
 \tag{L-14314.9}
\]

in a common scaled-coordinate Hilbert space. Suppose:

1. the exact fixed radical/critical-line core converges strongly to a
   nonnegative limiting operator;
2. the family is uniformly bounded;
3. the negative parts satisfy (L-14314.5).

Then the low-block lower defect tends to zero. Combined with the complete
complement and assembly gates in `T-14302`, RH follows.

Unlike `L-14312`, this permits positive packet eigenvalues to remain bounded
away from zero.

## Escaping-mode dichotomy under false RH

Assume the complete complement block is nonnegative and the block
decomposition is exact. If RH is false, Suzuki's localized criterion and
support monotonicity give a support `a_0` and `c>0` such that

\[
 \inf\sigma(A_a)\le-c
 \qquad(a\ge a_0).
 \tag{L-14314.10}
\]

For a decomposition

\[
 A_a=\begin{pmatrix}B&R^*\\R&C\end{pmatrix},
 \qquad C\succ0,
\]

a negative Rayleigh vector cannot lie entirely in the complement. Minimizing
in the complement coordinate shows that the exact Schur complement

\[
 S=B-R^*C^{-1}R
\]

has

\[
 \lambda_{\min}(S)\le-c.
 \tag{L-14314.11}
\]

If `C>=hM`, then

\[
 C^{-1}\preceq h^{-1}M^{-1},
\]

so the conservative corrected matrix satisfies

\[
 K=B-h^{-1}R^*M^{-1}R\preceq S
\]

and therefore

\[
 \lambda_{\min}(K)\le-c.
 \tag{L-14314.12}
\]

Consequently, if all fixed modes have a nonnegative strong limit, a false-RH
negative direction must violate (L-14314.5): it escapes every fixed compact
packet. This identifies the exact spectral location of a hypothetical
off-critical zero in the positive-path architecture.

## Gap audit

- The abstract theorem is exact.
- Constructing `N_j` numerically is not a proof of collective compactness.
- Strong convergence of `K_j` alone is insufficient; `R-14301` supplies the
  counterexample.
- A trace or rank bound on `N_j` is insufficient if its eigenvectors wander.
- The zeta application still needs a common-frame tightness theorem for the
  negative spectral subspaces, or the stronger whole-packet radical-frame bound
  of `L-14313`.
- The escaping-mode dichotomy explains the blocker; it does not exclude the
  escaping mode and therefore does not by itself prove RH.
