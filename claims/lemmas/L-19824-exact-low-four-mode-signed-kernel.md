# L-19824 — Exact basis and `d_4,d_6` inertia of the low signed prolate kernel

Claim ID: `L-19824`  
Status: **PROPOSED FINITE PROLATE LEMMA**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: notation and fixed-mode hypotheses of `L-19823`  
Scope: supplies the explicit low-kernel calculation used in `L-19823.27`

## 1. Low space and constraints

On

\[
 L_0=\operatorname{span}\{e_0,e_2,e_4,e_6\},
\]

use

\[
 \widehat e_n=\varepsilon_n\chi_ne_n,
 \qquad
 \varepsilon_n=(-1)^{n/2},
 \qquad
 q_n=e_n(0),
\]

and the two source constraints

\[
 f(0)=0,
 \qquad
 \int f=0.
\]

Put

\[
 p_+={e_0\over q_0}-{e_4\over q_4},
 \qquad
 p_-={e_2\over q_2}-{e_6\over q_6},
\]

\[
 c_{02}={e_0\over q_0}-{e_2\over q_2},
\]

and

\[
 r_+=\chi_0-\chi_4=d_4-d_0,
\]

\[
 r_-=-\chi_2+\chi_6=-(d_6-d_2),
\]

\[
 h=\chi_0+\chi_2.
\]

Then all three displayed vectors vanish at zero, while

\[
 \int p_+=r_+,
 \qquad
 \int p_-=r_-,
 \qquad
 \int c_{02}=h.
\]

## 2. Exact kernel basis

Define

\[
 \boxed{
 w_+=p_+-{r_+\over h}c_{02},
 \qquad
 w_-=p_--{r_-\over h}c_{02}.}
 \tag{L-19824.1}
\]

Both vectors satisfy both source constraints exactly. As `lambda->infinity`,

\[
 {r_+\over h}=O(d_4),
 \qquad
 {r_-\over h}=O(d_6),
\]

so

\[
 w_+=p_++o(1),
 \qquad
 w_-=p_-+o(1)
\]

in ordinary norm. The limiting vectors lie in opposite Fourier-sign sectors and
are nonzero. Hence `w_+,w_-` are linearly independent for all sufficiently large
`lambda`.

The low constraint matrix has rank two, so its kernel has dimension two.
Therefore

\[
 \boxed{
 \ker(C_L)=\operatorname{span}\{w_+,w_-\}.}
 \tag{L-19824.2}
\]

## 3. Defect form

Let

\[
 \mathcal De_n=\delta_ne_n,
 \qquad
 \delta_n={1-\chi_n^2\over2}\asymp d_n.
\]

The point-value ratios for the fixed modes are bounded above and below. Using

\[
 d_0=o(d_4),
 \qquad
 d_2=o(d_6),
 \qquad
 d_4=o(d_6),
\]

one obtains

\[
 \mathcal D(p_+,p_+)=\Theta(d_4),
 \qquad
 \mathcal D(p_-,p_-)=\Theta(d_6),
\]

and

\[
 \mathcal D(c_{02},c_{02})=O(d_2).
\]

The correction coefficients in (L-19824.1) then give

\[
 \boxed{
 \mathcal D(w_+,w_+)=\Theta(d_4),
 \qquad
 \mathcal D(w_-,w_-)=\Theta(d_6).}
 \tag{L-19824.3}
\]

The cross term has no leading contribution because `p_+` and `p_-` lie in
opposite Fourier-sign sectors. Every remaining term contains at least one small
correction coefficient or one of the smaller defects `d_0,d_2`. Consequently

\[
 \boxed{
 |\mathcal D(w_+,w_-)|
 =o(\sqrt{d_4d_6}).}
 \tag{L-19824.4}
\]

The ordinary Gram matrix of `w_+,w_-` converges to the positive diagonal Gram of
`p_+,p_-`. Thus it remains uniformly positive definite.

## 4. Low generalized eigenvalues

Relative to the basis `w_+,w_-`, the metric Gram is uniformly positive and the
defect Gram has diagonal scales `d_4,d_6` with an asymptotically negligible
normalized off-diagonal. Exact `2x2` determinant and trace comparison therefore
gives

\[
 \boxed{
 \lambda_1(\mathcal D|_{\ker C_L})=\Theta(d_4),
 \qquad
 \lambda_2(\mathcal D|_{\ker C_L})=\Theta(d_6).}
 \tag{L-19824.5}
\]

This is the explicit calculation invoked in `L-19823.27`. It is a pure prolate
statement. It does not transfer these scales to the arithmetic omitted-tail Gram
or the localized Weil operator.
