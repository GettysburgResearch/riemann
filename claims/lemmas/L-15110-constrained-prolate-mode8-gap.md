# L-15110 — Exact constrained prolate mode-8 gap and 0/4 residual

Claim ID: `L-15110`  
Status: **PROVED ABSTRACT PROLATE THEOREM; literature asymptotic imported explicitly**  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-31  
Dependencies: the finite Fourier/prolate spectral theorem; Fuchs fixed-index eigenvalue asymptotic; CCM equations (7.5)--(7.12)  
Scope: the information-theoretic prolate model underlying the positive RH program  
Related counterexample candidates: none

## 1. Setup

Let

\[
 \mathcal H_\lambda=L^2_{\rm even}([-\lambda,\lambda])
\]

and let

\[
 F_\lambda=P_\lambda\mathcal F P_\lambda
\]

be the compressed Fourier transform in the normalization

\[
 (\mathcal Ff)(y)=\int_{\mathbb R}f(x)e^{2\pi ixy}\,dx.
\]

On the real-even sector, choose an orthonormal prolate basis

\[
 e_0,e_2,e_4,e_6,e_8,\ldots,
 \qquad F_\lambda e_n=\chi_n e_n,
\]

with the usual signed ordering: the modes `0,4,8,...` have positive eigenvalues
approaching `+1`, while `2,6,10,...` have negative eigenvalues approaching
`-1`. Put

\[
 D_\lambda=I-F_\lambda,
 \qquad d_n=1-\chi_n.
\]

Thus `D_lambda` is positive. Assume, equivalently use the standard prolate
ordering, that

\[
 D_\lambda\succeq d_8I
 \quad\hbox{on }\{e_0,e_4\}^{\perp}.
 \tag{L-15110.1}
\]

Let

\[
 \ell(f)=\int_{-\lambda}^{\lambda}f(x)\,dx,
 \qquad a_n=\ell(e_n).
\]

The exact finite Fourier identity gives

\[
 a_n=\chi_ne_n(0).
 \tag{L-15110.2}
\]

Assume `a_0a_4!=0` and write

\[
 A^2=a_0^2+a_4^2.
\]

The normalized zero-integral `0/4` target and its orthogonal low companion are

\[
 t=\frac{a_4e_0-a_0e_4}{A},
 \qquad
 u=\frac{a_0e_0+a_4e_4}{A}.
 \tag{L-15110.3}
\]

Then

\[
 \ell(t)=0,
 \qquad \ell(u)=A.
\]

Define the constrained target complement

\[
 S_\lambda=\ker\ell\cap t^\perp.
 \tag{L-15110.4}
\]

Finally put

\[
 \mu_t=\langle D_\lambda t,t\rangle
 =\frac{a_4^2d_0+a_0^2d_4}{A^2}.
 \tag{L-15110.5}
\]

## 2. Exact mode-8 coercivity floor

For every `x in S_lambda`,

\[
 \boxed{
 \langle D_\lambda x,x\rangle
 \ge d_8\frac{A^2}{2\lambda}\|x\|^2.}
 \tag{L-15110.6}
\]

Consequently

\[
 \boxed{
 \langle(D_\lambda-\mu_tI)x,x\rangle
 \ge g_\lambda\|x\|^2,\qquad
 g_\lambda:=d_8\frac{A^2}{2\lambda}-\mu_t.}
 \tag{L-15110.7}
\]

In particular, once `g_lambda>0`, the zero-integral `0/4` target is separated
from its complete constrained complement by a gap whose leading scale is
`d_8/lambda`, not merely by an unquantified mode-8 heuristic.

### Proof

Let `g=1_[-lambda,lambda]`, the Riesz vector of `ell`. Since `ell(t)=0`,
`g` belongs to `t^perp`. Decompose

\[
 t^\perp=\operatorname{span}\{u\}\oplus K,
 \qquad K=\{e_0,e_4\}^\perp.
\]

Because `ell(u)=A`,

\[
 g=Au+g_K,
 \qquad \|g_K\|^2=\|g\|^2-A^2=2\lambda-A^2.
 \tag{L-15110.8}
\]

Write `x=alpha u+y` with `y in K`. The constraint `ell(x)=0` gives

\[
 \alpha A+\langle g_K,y\rangle=0.
\]

Hence

\[
 |\alpha|^2A^2
 \le(2\lambda-A^2)\|y\|^2,
\]

and therefore

\[
 \|y\|^2\ge\frac{A^2}{2\lambda}\|x\|^2.
 \tag{L-15110.9}
\]

The low/high decomposition is `D_lambda`-orthogonal. By positivity and
(L-15110.1),

\[
 \langle D_\lambda x,x\rangle
 \ge\langle D_\lambda y,y\rangle
 \ge d_8\|y\|^2,
\]

which proves (L-15110.6). Subtracting `mu_t||x||^2` proves (L-15110.7). QED.

## 3. Exact target residual

The scalar-free residual of `t` against `S_lambda` is explicit:

\[
 \boxed{
 \|P_{S_\lambda}(D_\lambda-\mu_tI)t\|
 =\frac{|a_0a_4|}{A^2}(d_4-d_0)
   \sqrt{1-\frac{A^2}{2\lambda}}.}
 \tag{L-15110.10}
\]

The same formula holds with `D_lambda` in place of `D_lambda-mu_t I`, since the
subtracted scalar multiple of `t` is orthogonal to `S_lambda`.

### Proof

The low-mode identity is

\[
 D_\lambda t
 =\mu_t t
  +\frac{a_0a_4}{A^2}(d_0-d_4)u.
 \tag{L-15110.11}
\]

Thus only the `u` component survives projection to `S_lambda`. Since
`S_lambda=t^perp cap g^perp` and `u perp t`,

\[
 P_{S_\lambda}u=u-\frac{\langle u,g\rangle}{\|g\|^2}g
 =u-\frac{A}{2\lambda}g,
\]

so

\[
 \|P_{S_\lambda}u\|^2=1-\frac{A^2}{2\lambda}.
\]

Substitution into (L-15110.11) proves (L-15110.10). QED.

## 4. Dimensionless prolate ratio

Whenever `g_lambda>0`, define

\[
 R_{\rm pro}(\lambda)
 =\frac{\|P_{S_\lambda}(D_\lambda-\mu_tI)t\|}{g_\lambda}.
\]

Then

\[
 \boxed{
 R_{\rm pro}(\lambda)
 \le
 \frac{2\lambda|a_0a_4|}{A^4}
 \sqrt{1-\frac{A^2}{2\lambda}}
 \frac{d_4-d_0}
 {d_8-2\lambda\mu_t/A^2}.}
 \tag{L-15110.12}
\]

More transparently, if `mu_t=o(d_8/lambda)`,

\[
 R_{\rm pro}(\lambda)
 \le
 \left(\frac{2\lambda|a_0a_4|}{A^4}+o(\lambda)\right)
 \frac{d_4}{d_8}.
 \tag{L-15110.13}
\]

## 5. Fixed-index asymptotic and the explicit `lambda^-7` law

Fuchs's fixed-index asymptotic, translated to the CCM normalization
`gamma=2*pi*lambda^2`, gives for each fixed nonnegative multiple of four

\[
 \boxed{
 d_n(\lambda)
 \sim
 \frac{2^{4n+1}\sqrt2\,\pi^{n+1}}{n!}
 \lambda^{2n+1}e^{-4\pi\lambda^2}.}
 \tag{L-15110.14}
\]

For `n=4` this is exactly the constant printed in CCM equation (7.12):

\[
 d_4(\lambda)
 \sim\frac{2^{14}}3\sqrt2\,\pi^5
 \lambda^9e^{-4\pi\lambda^2}.
\]

For modes `4` and `8`,

\[
 \boxed{
 \frac{d_4(\lambda)}{d_8(\lambda)}
 \sim\frac{105}{4096\pi^4}\lambda^{-8}.}
 \tag{L-15110.15}
\]

CCM's uniform fixed-mode convergence and exact integral identity imply

\[
 a_0\to h_0(0)=2^{1/4},
 \qquad
 a_4\to h_4(0)=\frac{\sqrt3}{2^{5/4}},
\]

hence

\[
 A^2\to\frac{11}{2^{5/2}},
 \qquad
 \frac{2|a_0a_4|}{A^4}\to\frac{32\sqrt3}{121}.
 \tag{L-15110.16}
\]

Also `mu_t=O(d_4)=o(d_8/lambda)`. Therefore (L-15110.12) yields

\[
 \boxed{
 R_{\rm pro}(\lambda)
 \le
 \left(\frac{105\sqrt3}{15488\pi^4}+o(1)\right)
 \lambda^{-7}
 \longrightarrow0.}
 \tag{L-15110.17}
\]

This proves the proposed `0/4` target versus mode-8 separation model inside the
exact prolate geometry. The unavoidable factor `1/lambda` in the complement
floor is caused by imposing the zero-integral constraint; it still leaves seven
powers of polynomial slack.

## 6. What this does and does not prove

### Proved here

- mode `8` is the first dangerous constrained prolate direction;
- the complete constrained complement has an explicit gap of order
  `d_8/lambda` above the target Rayleigh level;
- the exact scalar-free `0/4` residual is of order `d_4`;
- their dimensionless ratio is `O(lambda^-7)`.

### Not proved here

The localized Weil form is not `D_lambda`. Therefore this lemma does not, by
itself, prove

\[
 B_{\lambda,N,\tau}/h_{\lambda,N,\tau}\to0.
\]

A relative trace-form theorem must transfer both the numerator and the
constrained floor from `D_lambda` to the actual localized Weil geometry. The
transfer must also account for the additional localized global-radical cluster
identified in `L-15106`; a one-dimensional complement that ignores this cluster
cannot have the asserted Weil coercivity.

## 7. Proof boundary and review targets

1. Audit the signed compressed-Fourier eigenvalue convention.
2. Check the standard prolate ordering used in (L-15110.1).
3. Reconstruct Fuchs's fixed-index constant in the CCM parameter
   `gamma=2*pi*lambda^2`.
4. Verify that the production target is exactly the zero-integral `0/4`
   combination (L-15110.3).
5. Keep the source-space prolate parameter `lambda` distinct from the logarithmic
   support length used in the finite CCM Fourier matrices.
