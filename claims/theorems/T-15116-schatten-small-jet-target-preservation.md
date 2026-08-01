# T-15116 — Schatten-small finite jets preserve the Guinand--Weil target

Claim ID: `T-15116`  
Status: **PROVED QUANTITATIVE COMPOSITION THEOREM; RIEMANN SCHATTEN ESTIMATES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15136`--`L-15138`; Schatten Hölder; coherent Hilbert--Schmidt determinant limit  
Scope: a concrete sufficient theorem ensuring that the nonlinear Ward amendment has the same classical limit  
Related counterexample candidates: none

## 1. Setup

At level `(M,N)`, let

\[
 \widetilde R_{M,N},\qquad C_{M,N},\qquad
 R_{M,N}=\widetilde R_{M,N}-C_{M,N}
 \tag{T-15116.1}
\]

be the actual raw, finite-jet, and renormalized comparison maps of `L-15136`, and
let `S_R` be the self-adjoint seam involution. Put

\[
 A_{M,N}=\widetilde R_{M,N}^*S_R\widetilde R_{M,N},
 \qquad
 K_{M,N}=R_{M,N}^*S_RR_{M,N}.
 \tag{T-15116.2}
\]

Let `g_M^lin` be the original one-contour Guinand--Weil transform and put

\[
 g_{A,M,N}(w)=\frac d{dw}\log\det{}_2(I+iwA_{M,N}),
 \tag{T-15116.3}
\]

\[
 g_{K,M,N}(w)=\frac d{dw}\log\det{}_2(I+iwK_{M,N}).
 \tag{T-15116.4}
\]

For a disk `|w|<=r`, define the raw comparison error

\[
 \rho_{M,N}(r)
 :=\sup_{|w|\le r}|g_M^{\rm lin}(w)-g_{A,M,N}(w)|.
 \tag{T-15116.5}
\]

## 2. Power-trace stability

Suppose

\[
 \|A_{M,N}\|_2\le C,
 \qquad
 \|K_{M,N}\|_2\le C
 \tag{T-15116.6}
\]

and put

\[
 \varepsilon_{M,N}=\|A_{M,N}-K_{M,N}\|_2.
 \tag{T-15116.7}
\]

For every integer `ell>=2`,

\[
 \boxed{
 \left|
  \operatorname{Tr}(A_{M,N}^{\ell})
  -\operatorname{Tr}(K_{M,N}^{\ell})
 \right|
 \le \ell C^{\ell-1}\varepsilon_{M,N}.}
 \tag{T-15116.8}
\]

### Proof

Telescope

\[
 A^\ell-K^\ell
 =\sum_{j=0}^{\ell-1}
   A^{\ell-1-j}(A-K)K^j.
\]

In each trace term place `A-K` and one factor from `A` or `K` in
`S_2`, and bound all remaining factors in operator norm by their `S_2` norms.
Every term is at most `C^(ell-1) epsilon`; summing the `ell` terms gives the
claim. QED.

## 3. Uniform logarithmic-derivative bound

If `Cr<1`, then

\[
 \boxed{
 \sup_{|w|\le r}
 |g_{A,M,N}(w)-g_{K,M,N}(w)|
 \le
 \varepsilon_{M,N}
 \left[
  \frac1{(1-Cr)^2}-1
 \right].}
 \tag{T-15116.9}
\]

### Proof

Use the determinant power series and (T-15116.8):

\[
\begin{aligned}
 |g_A-g_K|
 &\le\sum_{\ell\ge2}
 \ell C^{\ell-1}\varepsilon |w|^{\ell-1}\\
 &\le\varepsilon
 \sum_{\ell\ge2}\ell(Cr)^{\ell-1}\\
 &=\varepsilon\left[(1-Cr)^{-2}-1\right].
\end{aligned}
\]

QED.

Combining this with `L-15138.22` gives

\[
 \boxed{
 \sup_{|w|\le r}
 |g_M^{\rm lin}(w)-g_{K,M,N}(w)|
 \le
 \rho_{M,N}(r)
 +\varepsilon_{M,N}
  \left[(1-Cr)^{-2}-1\right].}
 \tag{T-15116.10}
\]

## 4. Finite-jet Schatten-four bound

The actual map identity factors as

\[
 \boxed{
 A_{M,N}-K_{M,N}
 =\widetilde R_{M,N}^*S_RC_{M,N}
  +C_{M,N}^*S_RR_{M,N}.}
 \tag{T-15116.11}
\]

Therefore Schatten Hölder gives

\[
 \boxed{
 \varepsilon_{M,N}
 \le
 \left(
  \|\widetilde R_{M,N}\|_4
  +\|R_{M,N}\|_4
 \right)
 \|C_{M,N}\|_4.}
 \tag{T-15116.12}
\]

Thus a concrete sufficient jet-decoupling condition is

\[
 \sup_{M,N}
 \left(
  \|\widetilde R_{M,N}\|_4
  +\|R_{M,N}\|_4
 \right)<\infty,
 \tag{T-15116.13}
\]

\[
 \boxed{
 \|C_{M,N}\|_4\longrightarrow0.}
 \tag{T-15116.14}
\]

This is precisely the operator estimate missing from a mere test-function
convergence statement.

## 5. Target-preservation theorem

Let `(M_j,N_j)` be an unbounded diagonal sequence. Assume:

1. the original classical ledger converges locally uniformly,
   
   \[
   g_{M_j}^{\rm lin}(w)
   \longrightarrow
   \frac d{dw}\log
   \frac{\xi(1/2+w)}{\xi(1/2)};
   \tag{T-15116.15}
   \]

2. for every `r<1/C`,
   
   \[
   \boxed{\rho_{M_j,N_j}(r)\longrightarrow0;}
   \tag{T-15116.16}
   \]

3. the uniform Schatten bounds (T-15116.6) hold and
   
   \[
   \boxed{\varepsilon_{M_j,N_j}\longrightarrow0.}
   \tag{T-15116.17}
   \]

Then

\[
 \boxed{
 g_{K,M_j,N_j}(w)
 \longrightarrow
 \frac d{dw}\log
 \frac{\xi(1/2+w)}{\xi(1/2)}}
 \tag{T-15116.18}
\]

locally uniformly on `|w|<1/C`.

If additionally

\[
 K_{M_j,N_j}\longrightarrow K=K^*
 \quad\text{in }\mathfrak S_2,
 \tag{T-15116.19}
\]

then

\[
 \boxed{
 \frac{\xi(1/2+w)}{\xi(1/2)}
 =\det{}_2(I+iwK)}
 \tag{T-15116.20}
\]

first near zero and hence everywhere. Therefore RH follows.

### Proof

Equation (T-15116.10) and assumptions (T-15116.16)--(T-15116.17) show that
`g_K-g_lin` tends locally uniformly to zero. Combine with (T-15116.15). The
`S_2` convergence gives local uniform determinant convergence; normalization at
zero and the identity theorem give (T-15116.20). Self-adjointness puts every
nonzero determinant zero on the centered imaginary axis. QED.

## 6. Quartic specialization

Under the same hypotheses,

\[
 \boxed{
 |e_{4,M,N}|
 \le
 |a_{4,M}^{\rm lin}-\operatorname{Tr}(A_{M,N}^4)|
 +4C^3\varepsilon_{M,N}.}
 \tag{T-15116.21}
\]

Thus the genuine quartic target is preserved whenever the raw quartic pullback
converges and the finite-jet contact map is Schatten-small. This gives a direct
finite production test rather than an all-orders symbolic assertion.

## 7. Audit against the displayed manuscript estimates

The manuscript states convergence of the regularized finite-window test source
inside its closed Cauchy--Laplace comparison space and pre-determinant
continuity of the finite-part scalar functional. Those assertions concern the
**linear regularized scalar ledger**. They do not state:

\[
 \rho_{M,N}(r)\to0,
 \tag{T-15116.22}
\]

or

\[
 \|C_{M,N}\|_4\to0
 \tag{T-15116.23}
\]

for the singular-seam comparison map. In fact the manuscript explicitly
retains the singular boundary trace after regular area-trace cancellation.
Therefore the displayed convergence cannot be substituted for
(T-15116.16)--(T-15116.17) without a new mapping theorem.

## 8. Proof boundary

The theorem proves exactly how the nonlinear relative-`det_2` Ward amendment can
preserve the Riemann target. It does not establish the two Riemann-specific
limits (T-15116.16) and (T-15116.17). A production proof must estimate the raw
pullback error and the finite-jet comparison map in the declared Schatten
norms, beginning with the quartic gate (T-15116.21).
