# L-19823 — The complete signed prolate constraint has first scales `d_4` and `d_6`

Claim ID: `L-19823`  
Status: **PROPOSED PURE-PROLATE THEOREM — ARITHMETIC-TAIL TRANSFER OPEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: exact prolate Fourier signs and leakage normalization; fixed-mode Fuchs ratios; uniform point-value window `L-16219`; exact low-kernel lemma `L-19824`  
Scope: repairs the complete-space hierarchy rejected in `T-19807`; no localized-Weil or RH conclusion

## 1. Setup

Let

\[
 \mathcal H_\lambda
 =\operatorname{span}\{e_n:n=0,2,4,\ldots,2M_\lambda\},
 \qquad
 M_\lambda=O((\log\lambda)^2),
 \tag{L-19823.1}
\]

where the even prolate eigenfunctions are ordinary-`L2` orthonormal and satisfy

\[
 \widehat e_n=\varepsilon_n\chi_ne_n,
 \qquad
 \varepsilon_n=(-1)^{n/2},
 \qquad
 0<\chi_n<1.
 \tag{L-19823.2}
\]

Put

\[
 q_n=e_n(0),
 \qquad
 d_n=1-\chi_n,
 \qquad
 \delta_n={1-\chi_n^2\over2}.
 \tag{L-19823.3}
\]

The exact positive-ray leakage form is diagonal:

\[
 \mathcal D_\lambda e_n=\delta_ne_n.
 \tag{L-19823.4}
\]

Since

\[
 \int e_n=\widehat e_n(0)=\varepsilon_n\chi_nq_n,
 \tag{L-19823.5}
\]

the exact two-constraint source space is

\[
 \mathcal S_\lambda
 =\left\{
 f=\sum c_ne_n:
 \sum q_nc_n=0,
 \quad
 \sum\varepsilon_n\chi_nq_nc_n=0
 \right\}.
 \tag{L-19823.6}
\]

Let

\[
 0<\theta_1(\lambda)\le\theta_2(\lambda)\le\cdots
 \tag{L-19823.7}
\]

be the eigenvalues of the compression of `mathcal D_lambda` to
`mathcal S_lambda` in the ordinary metric.

## 2. Hypotheses

Assume the fixed-mode hierarchy

\[
 {d_0\over d_4}\to0,
 \qquad
 {d_2\over d_6}\to0,
 \qquad
 {d_4\over d_6}\to0,
 \qquad
 {d_6\over d_8}\to0.
 \tag{L-19823.8}
\]

The same ratios hold for `delta_n` because
`delta_n=d_n(1+chi_n)/2`.

Assume the point-value window

\[
 c(n+1)^{-1/4}
 \le {|q_n|\over|q_0|}
 \le C(n+1)^{-1/4}
 \qquad(0\le n\le2M_\lambda),
 \tag{L-19823.9}
\]

and monotonicity

\[
 \delta_n\ge\delta_8
 \qquad(n\ge8).
 \tag{L-19823.10}
\]

Then

\[
 \boxed{
 \kappa_\lambda
 :=\delta_6
 \sum_{\substack{8\le n\le2M_\lambda\\n\ {m even}}}
 {|q_n|^2\over\delta_n}
 \longrightarrow0,}
 \tag{L-19823.11}
\]

because

\[
 \kappa_\lambda
 \ll {\delta_6\over\delta_8}\sqrt{M_\lambda}\to0.
 \tag{L-19823.12}
\]

## 3. Theorem

Under the preceding hypotheses,

\[
 \boxed{
 \theta_1(\lambda)=O(d_4(\lambda)),
 \qquad
 \theta_2(\lambda)=\Theta(d_6(\lambda)).}
 \tag{L-19823.13}
\]

Thus the complete signed constrained packet has first scales

```text
d_4, d_6,
```

not `d_4,d_8`. The `d_8` scale is the next `+1`-sector scale after the lower
`-1` sector has been treated.

## 4. Two-dimensional upper packet

Define

\[
 p_+={e_0\over q_0}-{e_4\over q_4},
 \qquad
 p_-={e_2\over q_2}-{e_6\over q_6},
 \tag{L-19823.14}
\]

with integral residuals

\[
 r_+=d_4-d_0,
 \qquad
 r_-=-(d_6-d_2).
 \tag{L-19823.15}
\]

Then

\[
 u_1=r_-p_+-r_+p_-
 \tag{L-19823.16}
\]

belongs to `mathcal S_lambda`, and orthogonality of the two Fourier-sign sectors
gives

\[
 {\mathcal D(u_1/r_-,u_1/r_-)
  \over\|u_1/r_-\|^2}
 =O(d_4)+O(d_4^2/d_6)
 =O(d_4).
 \tag{L-19823.17}
\]

Hence `theta_1<=C d_4`.

Next put

\[
 p_{+,2}={e_4\over q_4}-{e_8\over q_8},
 \qquad
 r_{+,2}=d_8-d_4,
 \tag{L-19823.18}
\]

and

\[
 u_2=r_{+,2}p_- - r_-p_{+,2}.
 \tag{L-19823.19}
\]

Again `u_2 in mathcal S_lambda`, and

\[
 {\mathcal D(u_2/r_{+,2},u_2/r_{+,2})
  \over\|u_2/r_{+,2}\|^2}
 =O(d_6)+O(d_6^2/d_8)
 =O(d_6).
 \tag{L-19823.20}
\]

The normalized overlap of `u_1/r_-` and `u_2/r_(+,2)` is

\[
 O(d_4/d_6+d_6/d_8)=o(1).
 \tag{L-19823.21}
\]

Their metric Gram is therefore uniformly positive, while the defect Gram has
trace `O(d_6)`. The maximum Rayleigh quotient on their two-dimensional span is
`O(d_6)`, and min--max gives

\[
 \theta_2\le C d_6.
 \tag{L-19823.22}
\]

## 5. Exact low kernel

Let

\[
 L_0=\operatorname{span}\{e_0,e_2,e_4,e_6\},
 \qquad
 H_0=L_0^\perp\cap\mathcal H_\lambda.
 \tag{L-19823.23}
\]

Let `C_L` and `C_H` be the restrictions of the two source constraints. The
normalized matrix of `C_L` tends to two independent sign rows. Hence `C_L` has
a uniformly bounded right inverse

\[
 B_\lambda:\mathbb C^2\to L_0.
 \tag{L-19823.24}
\]

By `L-19824`, the exact two-dimensional low kernel

\[
 K_0=\ker C_L
 \tag{L-19823.25}
\]

has generalized defect eigenvalues

\[
 \lambda_1(\mathcal D|_{K_0})=\Theta(d_4),
 \qquad
 \lambda_2(\mathcal D|_{K_0})=\Theta(d_6).
 \tag{L-19823.26}
\]

## 6. Graph representation of the full constraints

Every `f in mathcal S_lambda` has a unique representation

\[
 f=k+R_\lambda z+z,
 \qquad
 k\in K_0,
 \quad z\in H_0,
 \tag{L-19823.27}
\]

where

\[
 R_\lambda=-B_\lambda C_H.
 \tag{L-19823.28}
\]

Let `D_H` be the tail restriction of `mathcal D`. The rows of `C_H` have
coefficients `q_n` and `epsilon_n chi_nq_n`. Weighted Cauchy--Schwarz yields

\[
 \boxed{
 \|R_\lambda D_H^{-1/2}\|^2
 \le C\sum_{n\ge8}{|q_n|^2\over\delta_n}.}
 \tag{L-19823.29}
\]

Consequently

\[
 \delta_6\|R_\lambda D_H^{-1/2}\|^2=o(1).
 \tag{L-19823.30}
\]

## 7. Lower bound for the second eigenvalue

Choose `c_1>0` small. Suppose

\[
 \mathcal D(f,f)<c_1d_6\|f\|^2.
 \tag{L-19823.31}
\]

Since `D_H>=delta_8I`,

\[
 \|z\|^2
 \le {c_1d_6\over\delta_8}\|f\|^2
 =o(\|f\|^2).
 \tag{L-19823.32}
\]

Equation (L-19823.29) then gives

\[
 \|R_\lambda z\|=o(\|f\|).
 \tag{L-19823.33}
\]

Thus `||k||=(1+o(1))||f||`. Moreover,

\[
 \mathcal D(k,k)
 \le2\mathcal D(k+R_\lambda z,k+R_\lambda z)
    +2\delta_6\|R_\lambda z\|^2
 \le(2c_1+o(1))d_6\|f\|^2.
 \tag{L-19823.34}
\]

For `c_1` smaller than one quarter of the lower constant in
(L-19823.26), the image of the complete spectral subspace below `c_1d_6` under
`f mapsto k` lies in the one-dimensional first spectral subspace of
`mathcal D|K_0`. The map is injective there: if `k=0`, (L-19823.32)--
(L-19823.33) contradict `||f||>0`.

Therefore the complete constrained space has at most one eigenvalue below
`c_1d_6`. Min--max gives

\[
 \theta_2\ge c_1d_6.
 \tag{L-19823.35}
\]

Together with (L-19823.22), this proves the theorem.

## 8. Boundary

This closes the **diagonal pure-prolate** signed hierarchy:

\[
 \boxed{
 \text{target scale }d_4,
 \qquad
 \text{complete next scale }d_6.}
 \tag{L-19823.36}
\]

Since `d_4/d_6->0`, the Rayleigh-floor route survives the reviewer's sector
correction.

The following transfers remain open:

1. a quantitative exact source frame containing both Fourier-sign sectors;
2. the same `d_4,d_6` hierarchy for the complete arithmetic omitted-tail Gram;
3. collective alias and endpoint bounds;
4. the full relative localized-Weil scalarization.

No RH conclusion is claimed.
