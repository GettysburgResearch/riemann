# L-91325 — A bounded renormalized Fisher feature isolates the reciprocal-xi Toeplitz leg

Claim ID: `L-91325`  
Status: **PROVED EXACT RENORMALIZED FACTORIZATION AND UNBOUNDED-LEG ISOLATION**  
Created: 2026-08-13  
Depends on: `L-91312`, `L-91316.7`, `R-91324`  
Corrects: the normalized Bochner feature map of `L-91316`  
RH status: **unproved**

## 1. Remove the reciprocal amplitude from the random feature

Fix `a>1/2` and abbreviate

\[
 \varphi(t)=\varphi_a(t),
 \qquad
 \Theta(t)=\Theta_a(t)=\frac{\varphi(-t)}{\varphi(t)}.
 \tag{L-91325.1}
\]

Retain the normalized phase feature

\[
 h_t(Y)
 =\frac{e^{-itY}}{\varphi(-t)}
  -\frac{e^{itY}}{\varphi(t)}.
\]

Define instead

\[
 \boxed{
 k_t(Y)=\varphi(t)h_t(Y)
 =\Theta(t)^{-1}e^{-itY}-e^{itY}.
 }
 \tag{L-91325.2}
\]

Because `|Theta(t)|=1` on the real boundary,

\[
 \boxed{|k_t(Y)|\le2.}
 \tag{L-91325.3}
\]

Moreover

\[
 \mathbb E_a k_t
 =\Theta(t)^{-1}\varphi(-t)-\varphi(t)=0.
 \tag{L-91325.4}
\]

Thus `k_t` is a uniformly bounded centered phase feature on the same fixed
completed source space.

## 2. The renormalized covariance is bounded and asymptotically flat

Put

\[
 \mathcal K_a(s,t)
 =\mathbb E_a[k_s\overline{k_t}].
 \tag{L-91325.5}
\]

Since `k_t=varphi(t)h_(a,t)`,

\[
 \boxed{
 \mathcal K_a(s,t)
 =\varphi(s)\overline{\varphi(t)}\,
  \mathcal H_a(s,t).
 }
 \tag{L-91325.6}
\]

It is positive semidefinite on every finite carrier packet. On the diagonal,

\[
 \boxed{
 \mathcal K_a(t,t)
 =|\varphi(t)|^2\mathcal H_a(t,t)
 =2\left[
  1-\operatorname{Re}
  \frac{\varphi(-t)\varphi(2t)}{\varphi(t)}
 \right].
 }
 \tag{L-91325.7}
\]

The pointwise bound (L-91325.3) gives

\[
 0\le\mathcal K_a(t,t)\le4.
 \tag{L-91325.8}
\]

Since `varphi(2t)->0`, the second form in (L-91325.7) gives

\[
 \boxed{
 \mathcal K_a(t,t)\longrightarrow2
 \qquad(|t|\to\infty).
 }
 \tag{L-91325.9}
\]

The exponential explosion in `H_a(t,t)` has been removed exactly.

## 3. A bounded source map on the whole model space

For `g in K_Theta`, retain

\[
 (\mathcal U_\Theta g)(t)=\overline{\Theta(t)}g(t).
\]

Define the ambient-boundary feature map

\[
 \boxed{
 (\mathcal B_ag)(Y,t)
 =k_t(Y)(\mathcal U_\Theta g)(t).
 }
 \tag{L-91325.10}
\]

Then

\[
 \mathcal B_a:
 K_\Theta\longrightarrow L^2(P_a;L^2(\mathbb R))
\]

is bounded on the entire model space, and

\[
 \boxed{
 \|\mathcal B_ag\|^2
 =\int_{\mathbb R}\mathcal K_a(t,t)|g(t)|^2dt
 \le4\|g\|^2.
 }
 \tag{L-91325.11}
\]

No dense-core assertion and no distributional boundary product is needed.

## 4. The score observation remains a coisometry

Let

\[
 V_a=\operatorname{Var}_a(Y)>0,
 \qquad
 s_a(Y)=\frac{\sigma_a(Y)}{\sqrt{V_a}}.
\]

On `L2(P_a;L2(R))`, define

\[
 (\mathcal C_aF)(t)
 =\mathbb E_a[s_a(Y)F(Y,t)].
 \tag{L-91325.12}
\]

Its adjoint is `(C_a^*v)(Y,t)=s_a(Y)v(t)`, so

\[
 \boxed{
 \mathcal C_a\mathcal C_a^*=I_{L^2(\mathbb R)}.
 }
 \tag{L-91325.13}
\]

Thus `Pi_a=C_a^*C_a` is the orthogonal score-channel projection and

\[
 \boxed{
 \|\mathcal B_ag\|^2
 =\|\mathcal C_a\mathcal B_ag\|^2
 +\|(I-\Pi_a)\mathcal B_ag\|^2.
 }
 \tag{L-91325.14}
\]

The random-source part of the corrected factorization is therefore a fixed
bounded map followed by one fixed coisometry, with an exact positive
score-orthogonal reserve.

## 5. The missing amplification is an explicit reciprocal-amplitude leg

Define the Toeplitz-type operator

\[
 \boxed{
 \mathfrak T_{\varphi,a}f
 =P_+\left(\frac{f}{\varphi}\right),
 \qquad
 \operatorname{Dom}(\mathfrak T_{\varphi,a})
 =\left\{f\in L^2:
  \frac f\varphi\in L^2
 \right\}.
 }
 \tag{L-91325.15}
\]

This domain is dense because it contains every bounded compactly supported
function: `varphi` is continuous and nonzero on each compact real interval.

Let

\[
 \mathcal D_a
 =\left\{g\in K_\Theta:
  \ell\,\mathcal U_\Theta g\in L^2(\mathbb R)
 \right\},
 \qquad
 \ell=a\partial_a\log\Theta_a.
 \tag{L-91325.16}
\]

From `L-91312.10` and `k_t=varphi(t)h_t`,

\[
 \mathbb E_a[\sigma_a(Y)k_t(Y)]
 =-\frac{\varphi(t)}a\ell(t).
 \tag{L-91325.17}
\]

Consequently, for `g in D_a`,

\[
 \mathcal C_a\mathcal B_ag
 =-\frac{\varphi\ell}{a\sqrt{V_a}}
  \mathcal U_\Theta g
 \in\operatorname{Dom}(\mathfrak T_{\varphi,a}).
 \tag{L-91325.18}
\]

Using the exact model-space identity `L-91316.7`, one obtains

\[
\boxed{
\begin{aligned}
 \mathcal J_ag
 &=-\sqrt2P_+(\ell\mathcal U_\Theta g)\\
 &=a\sqrt{2V_a}\,
   \mathfrak T_{\varphi,a}
   \mathcal C_a\mathcal B_ag.
\end{aligned}}
 \tag{L-91325.19}
\]

This is an exact corrected factorization. The reciprocal `1/varphi` has not
been hidden inside an infinite-norm random feature; it appears as its own
explicit analytic leg.

## 6. The reciprocal-amplitude leg is unbounded

The boundary characteristic function satisfies

\[
 |\varphi(t)|\le1,
 \qquad
 \varphi(t)\to0
 \quad(|t|\to\infty).
 \tag{L-91325.20}
\]

Choose real `t_n->infinity` and normalized upper-Hardy reproducing kernels
`e_n` whose squared boundary moduli are Poisson kernels concentrating at
`t_n`. By continuity of `varphi`, the approximate-identity property and
`|varphi|<=1`, the concentration widths may be chosen so that

\[
 \|\varphi e_n\|_2\longrightarrow0,
 \qquad
 \|e_n\|_2=1.
 \tag{L-91325.21}
\]

Set `f_n=varphi e_n`. Then `f_n` belongs to the domain in (L-91325.15), and

\[
 \mathfrak T_{\varphi,a}f_n
 =P_+e_n=e_n.
\]

Therefore

\[
 \boxed{
 \mathfrak T_{\varphi,a}
 \text{ has no bounded extension on }L^2(\mathbb R).
 }
 \tag{L-91325.22}
\]

In particular, the corrected factorization does not imply the contraction
inequality claimed in `L-91316.15`. The score channel is contractive; the
reciprocal completed-amplitude leg is not.

## 7. Exact corrected endpoint

For any `g in D_a`, define the structured source vector

\[
 F_g=\mathcal C_a\mathcal B_ag
 =-\frac{\varphi\ell}{a\sqrt{V_a}}
  \mathcal U_\Theta g.
 \tag{L-91325.23}
\]

The remaining analytic problem is no longer a vague Fisher-Hankel domain
question. It is the structured observability estimate

\[
 \boxed{
 \|\mathfrak T_{\varphi,a}F_g\|_{H^2}^2
 \le \text{completed arithmetic source form on }g,
 }
 \tag{L-91325.24}
\]

with all delays, orientations and the bridge retained. Any proof must control
the exponentially amplifying reciprocal-xi leg on the special range generated
by the score covariance. Ordinary data processing cannot do this.

For the undelayed rational Cauchy model vectors of `L-91323`, the kernel
formulas show `g(t)=O((1+|t|)^{-1})`; the logarithmic derivative formula for
`xi` on `Re(s)>1` gives `ell(t)=O(log(2+|t|))`. Hence those base vectors lie in
`D_a`. Stability of `D_a` under the full forced delay colligation remains a
separate question.

## 8. Exact boundary

```text
normalized random feature h_t                       EXPONENTIALLY LARGE
natural normalized boundary-L2 core                 {0} BY R-91324
renormalized feature k_t=varphi(t)h_t               UNIFORMLY BOUNDED
renormalized covariance kernel                      POSITIVE, DIAGONAL <=4
bounded source map B_a                              EXACT ON ALL K_Theta
score observation C_a                               COISOMETRY
reciprocal-amplitude Toeplitz leg T_(varphi,a)       EXPLICIT AND UNBOUNDED
corrected factorization J=a sqrt(2V) T C B           EXACT ON D_a
base rational Cauchy model vectors in D_a            PROVED
forced-delay stability of D_a                       OPEN
structured arithmetic observability estimate        OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
