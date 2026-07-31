# T-15301 — Energy-gap finite-diagonal criterion implying RH

Claim ID: `T-15301`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10-b`  
Created: 2026-07-31  
Dependencies: `T-14301`, audited `L-14302`, `L-15301`, and the imported CCM finite real-zero theorem  
Scope: positive finite-dimensional sufficient criterion for the Riemann hypothesis

## Statement

Use the notation and exact CCM normalization of `T-14301`. Let

\[
\lambda_j\to\infty,
\qquad
N_j\to\infty,
\qquad
0<\tau_j<\frac12,
\qquad
\tau_j\nearrow\frac12.
\]

At level `j`, let

\[
A_j=QW_{\lambda_j}^{N_j}
\]

be the exact finite localized-Weil matrix, let `k_j` be the explicit CCM
prolate target, and put

\[
p_j=P_{N_j}k_j,
\qquad
q_j=\|p_j\|_2,
\qquad
v_j=p_j/q_j.
\]

Assume `p_j` is nonzero. Let `M_j` be the Hardy-strip Gram on the even
complement of `v_j`, and suppose finite proof objects certify:

1. the global finite ground state of `A_j` is simple and even;
2. the odd-sector separation gate of `L-14302`;
3. an upper target Rayleigh endpoint `mu_j`;
4. a lower global ground endpoint `L_j`;
5. an even-complement Hardy coercivity constant `h_j>0`:

   \[
   C_{j,+}-U_jI\succeq h_jM_j,
   \qquad U_j\ge\mu_j;
   \]

6. a weighted projection-tail bound

   \[
   t_j\ge
   \|k_j-p_j\|_{\lambda_j,\tau_j}.
   \]

If

\[
\boxed{
 t_j+q_j
 \sqrt{\frac{\mu_j-L_j}{h_j}}
 \longrightarrow0,}
\tag{T-15301.1}
\]

then the Riemann hypothesis is true.

### Positive-semidefinite specialization

If every finite matrix `A_j` is certified positive semidefinite, one may take
`L_j=0`. It is then sufficient that

\[
\boxed{
 t_j+q_j\sqrt{\frac{\mu_j}{h_j}}
 \longrightarrow0.}
\tag{T-15301.2}
\]

## Proof

Let `xi_j` be the normalized simple-even ground eigenvector. Applying
`L-15301` at level `j` gives an explicit scalar `c_j` such that

\[
\|c_j\xi_j-k_j\|_{\lambda_j,\tau_j}
\le
 t_j+q_j\sqrt{\frac{\mu_j-L_j}{h_j}}.
\]

The right side tends to zero by hypothesis. Therefore the moving-strip
approximation hypothesis of `T-14301` holds. The support-independent
Hardy-strip transform bound gives local-uniform convergence of
`\widehat{c_j\xi_j}` to `Xi` on every compact subset of
`|Im z|<1/2`. The imported CCM finite theorem puts every zero of each
`\widehat{\xi_j}` on the real axis. Hurwitz then excludes every nonreal zero of
`Xi`, which is equivalent to RH. QED.

## Comparison with the residual criterion

The old sufficient condition was

\[
 t_j+q_j\frac{B_j}{h_j}\to0,
\qquad
B_j=\|P_{v_j^\perp}A_jv_j\|_{M_j^{-1}}.
\]

By `L-15301.13`, whenever the exact ground value is used,

\[
\sqrt{\frac{\mu_j-\lambda_{0,j}}{h_j}}
\le
\frac{B_j}{h_j}.
\]

Thus `T-15301` is a genuine weakening of the asymptotic numerical target. It
also aligns both numerator and denominator with the same energy hierarchy.

## Proof boundary

This theorem does **not** establish (T-15301.1). In the current repository, the
remaining analytic work is to compare:

- the target Rayleigh energy with the constrained `0/4` prolate defect;
- the even-complement Weil coercivity with the first constrained higher prolate
  defect;
- both comparisons in one exact CCM/Hardy normalization.

The theorem is conditional only in this explicit sense; it does not conceal a
numerical limit inside a qualitative convergence statement.
