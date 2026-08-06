# L-19823 — The complete signed prolate constraint has first scales `d_4` and `d_6`

Claim ID: `L-19823`  
Status: **PROPOSED PURE-PROLATE THEOREM — ARITHMETIC-TAIL TRANSFER OPEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: exact prolate Fourier signs and leakage normalization; fixed-mode Fuchs ratios; the uniform point-value window of `L-16219`  
Scope: repairs the complete-space hierarchy rejected in `T-19807`; no localized-Weil or RH conclusion

## 1. Setup

Let

\[
 \mathcal H_\lambda
 =\operatorname{span}\{e_n: n=0,2,4,\ldots,2M_\lambda\},
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

Since evaluation of the Fourier transform at zero gives

\[
 \int e_n=\varepsilon_n\chi_nq_n,
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

be the generalized eigenvalues of the compression of `mathcal D_lambda` to
`mathcal S_lambda` in the ordinary `L2` metric.

## 2. Hypotheses used

Assume the standard fixed-mode hierarchy

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

Because `delta_n=d_n(1+chi_n)/2`, the same ratios hold with `delta` in place of
`d`.

Assume also the uniform point-value comparison

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

These imply the tail susceptibility estimate

\[
 \boxed{
 \kappa_\lambda
 :=\delta_6
 \sum_{\substack{8\le n\le2M_\lambda\\n\ {m even}}}
 {|q_n|^2\over\delta_n}
 \longrightarrow0.}
 \tag{L-19823.11}
\]

Indeed, (L-19823.9)--(L-19823.10) give

\[
 \kappa_\lambda
 \ll {\delta_6\over\delta_8}\sqrt{M_\lambda}
 \longrightarrow0.
 \tag{L-19823.12}
\]

## 3. Main theorem

Under the preceding hypotheses,

\[
 \boxed{
 \theta_1(\lambda)=O(d_4(\lambda)),
 \qquad
 \theta_2(\lambda)=\Theta(d_6(\lambda)).}
 \tag{L-19823.13}
\]

In particular, the full signed constrained packet has:

```text
first exact-radical scale    d_4,
second complete scale        d_6.
```

The `+1`-sector `d_8` scale remains the next scale only after the `-1` Fourier
sector has been removed or separately paid.

## 4. Two exact low vectors

Define

\[
 p_+={e_0\over q_0}-{e_4\over q_4},
 \qquad
 p_-={e_2\over q_2}-{e_6\over q_6},
 \tag{L-19823.14}
\]

and

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

belongs to `mathcal S_lambda`. After division by `r_-`, the two Fourier-sign
sectors are orthogonal and give

\[
 {\mathcal D( u_1/r_-,u_1/r_-)
  \over
  \|u_1/r_-\|^2}
 =O(d_4)+O(d_4^2/d_6)
 =O(d_4).
 \tag{L-19823.17}
\]

Thus

\[
 \theta_1\le C d_4.
 \tag{L-19823.18}
\]

Next put

\[
 p_{+,2}={e_4\over q_4}-{e_8\over q_8},
 \qquad
 r_{+,2}=d_8-d_4,
 \tag{L-19823.19}
\]

and

\[
 u_2=r_{+,2}p_- - r_-p_{+,2}.
 \tag{L-19823.20}
\]

Again `u_2` satisfies both source constraints, and

\[
 {\mathcal D(u_2/r_{+,2},u_2/r_{+,2})
  \over
  \|u_2/r_{+,2}\|^2}
 =O(d_6)+O(d_6^2/d_8)
 =O(d_6).
 \tag{L-19823.21}
\]

The normalized overlap of the two displayed vectors is

\[
 O(d_4/d_6+d_6/d_8)=o(1).
 \tag{L-19823.22}
\]

Therefore their span has maximum Rayleigh quotient `O(d_6)`, and min--max gives

\[
 \theta_2\le C d_6.
 \tag{L-19823.23}
\]

## 5. Low four-mode kernel

Let

\[
 L_0=\operatorname{span}\{e_0,e_2,e_4,e_6\},
 \qquad
 H_0=L_0^\perp\cap\mathcal H_\lambda.
 \tag{L-19823.24}
\]

Let `C_L:L_0->C^2` and `C_H:H_0->C^2` be the two source-constraint maps. The
normalized matrix of `C_L` tends to two independent sign rows, so its smallest
singular value is bounded below. Choose a right inverse

\[
 B_\lambda:\mathbb C^2\to L_0,
 \qquad
 C_LB_\lambda=I,
 \qquad
 \|B_\lambda\|\le C.
 \tag{L-19823.25}
\]

The exact low kernel

\[
 K_0=\ker C_L
 \tag{L-19823.26}
\]

is two-dimensional and is spanned by the low vectors `u_1` and the version of
`u_2` with its `e_8` term omitted and the corresponding low right-inverse
correction inserted. Equivalently, direct `2x2` generalized eigenvalue
calculation in any fixed basis of `K_0` gives

\[
 \lambda_1(\mathcal D|_{K_0})=O(d_4),
 \qquad
 \lambda_2(\mathcal D|_{K_0})\ge c_0d_6.
 \tag{L-19823.27}
\]

One may see the second estimate directly from the limit: the first low kernel
vector tends to the positive-sector difference `p_+`, while the second tends to
the negative-sector difference `p_-`; their Gram stays nonsingular and their
defect energies have scales `d_4` and `d_6`.

## 6. Graph representation of the complete constraint space

Every `f in mathcal S_lambda` has the unique representation

\[
 f=k+R_\lambda z+z,
 \qquad
 k\in K_0,
 \quad z\in H_0,
 \tag{L-19823.28}
\]

where

\[
 R_\lambda=-B_\lambda C_H.
 \tag{L-19823.29}
\]

Let `D_H` be the tail restriction of `mathcal D`. Since the two rows of `C_H`
have coefficients `q_n` and `epsilon_n chi_n q_n`, weighted Cauchy--Schwarz
and (L-19823.25) give

\[
 \boxed{
 \|R_\lambda D_H^{-1/2}\|^2
 \le C
 \sum_{n\ge8}{|q_n|^2\over\delta_n}.}
 \tag{L-19823.30}
\]

After multiplication by `delta_6`, the right side tends to zero by
(L-19823.11).

## 7. Lower bound for the second eigenvalue

Fix a sufficiently small constant `c_1>0`. Suppose

\[
 \mathcal D(f,f)<c_1d_6\|f\|^2
 \tag{L-19823.31}
\]

for a nonzero vector represented as in (L-19823.28). Since
`D_H>=delta_8 I`,

\[
 \|z\|^2
 \le {c_1d_6\over\delta_8}\|f\|^2
 =o(\|f\|^2).
 \tag{L-19823.32}
\]

Furthermore, (L-19823.30) gives

\[
 \|R_\lambda z\|
 \le \|R_\lambda D_H^{-1/2}\|
      \mathcal D(z,z)^{1/2}
 =o(\|f\|).
 \tag{L-19823.33}
\]

Thus the low projection `k` has norm `(1+o(1))||f||`. Its defect energy differs
from the low part of `f` by `o(d_6)||f||^2`. Hence (L-19823.31) maps the complete
low-energy spectral subspace injectively into the spectral subspace of
`mathcal D|K_0` below `(c_1+o(1))d_6`.

By (L-19823.27), that latter subspace is one-dimensional when `c_1<c_0/2`.
Therefore the complete constrained space has at most one eigenvalue below
`c_1d_6`. Min--max gives

\[
 \theta_2\ge c_1d_6.
 \tag{L-19823.34}
\]

Together with (L-19823.23), this proves (L-19823.13).

## 8. Consequences for the positive route

The pure-prolate signed hierarchy is therefore not an open guess:

\[
 \boxed{
 \text{target scale }d_4,
 \qquad
 \text{complete next scale }d_6.}
 \tag{L-19823.35}
\]

Since

\[
 d_4/d_6\to0,
 \tag{L-19823.36}
\]

the Rayleigh-floor/Hurwitz route remains viable after replacing every
complete-space `d_8` claim by `d_6`.

What remains open is transport from this diagonal prolate defect model to the
complete **arithmetic omitted-tail Gram** and then to the exact localized Weil
matrix. That transport must include:

1. both Fourier-sign sectors in one controlled exact source frame;
2. a signed arithmetic-tail lower hierarchy at scales `d_4,d_6`;
3. the complete alias and endpoint ledger;
4. the corrected local-Weyl/support-average theorem.

This lemma proves none of those arithmetic interfaces and does not prove RH.
