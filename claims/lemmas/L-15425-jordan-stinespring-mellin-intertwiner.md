# L-15425 — Exact Jordan Stinespring–Mellin intertwiner

Claim ID: `L-15425`  
Title: Generalized Jordan divisor conditioning is an exact isometric dilation of the arithmetic zeta ratio  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: Suzuki's coefficients `c_omega(n)`; elementary Dirichlet convolution  
Scope: arithmetic half of the requested Jordan/Volterra intertwiner  
Related counterexample candidates: none

## Generalized Jordan weights

For `omega>0`, put

\[
 J_{2\omega}(n)
 =n^{2\omega}\prod_{p\mid n}(1-p^{-2\omega})
 =n^\omega c_\omega(n).
 \tag{L-15425.1}
\]

Then

\[
 J_{2\omega}=\mu*\operatorname{id}^{2\omega},
 \qquad
 \sum_{d\mid n}J_{2\omega}(d)=n^{2\omega}.
 \tag{L-15425.2}
\]

## Stinespring isometry

Define

\[
 V_\omega:\ell^2(\mathbb N)\longrightarrow
 \ell^2(\mathbb N\times\mathbb N)
 \tag{L-15425.3}
\]

by

\[
 \boxed{
 (V_\omega a)(d,m)
 =\frac{\sqrt{J_{2\omega}(d)}}{(dm)^\omega}
  a(dm).}
 \tag{L-15425.4}
\]

Then `V_omega` is an isometry. Indeed,

\[
\begin{aligned}
 \|V_\omega a\|_2^2
 &=\sum_{d,m\ge1}
   \frac{J_{2\omega}(d)}{(dm)^{2\omega}}
   |a(dm)|^2\\
 &=\sum_{n\ge1}|a(n)|^2n^{-2\omega}
   \sum_{d\mid n}J_{2\omega}(d)\\
 &=\sum_{n\ge1}|a(n)|^2.
\end{aligned}
 \tag{L-15425.5}
\]

For a bounded function `F` on the divisor coordinate, let `M_F` denote
multiplication by `F(d)` on the dilation space. Then

\[
 \boxed{
 (V_\omega^*M_FV_\omega a)(n)
 =\left[
   \sum_{d\mid n}
   \frac{J_{2\omega}(d)}{n^{2\omega}}F(d)
  \right]a(n).}
 \tag{L-15425.6}
\]

Thus the Jordan divisor Markov operator of `L-15424` is the compression of an
ordinary multiplication operator through one explicit isometry. Its carré du
champ is the Stinespring defect.

## Exact coherent-vector factorization

For complex `s` with `Re s>1+omega`, define

\[
 e^-_s(n)=n^{-(s-\omega)/2},
 \qquad
 e^+_s(m)=m^{-(s+\omega)/2},
 \tag{L-15425.7}
\]

and

\[
 j_{s,\omega}(d)
 =\sqrt{J_{2\omega}(d)}d^{-(s+\omega)/2}.
 \tag{L-15425.8}
\]

The dilation factorizes exactly:

\[
 \boxed{
 V_\omega e^-_s
 =j_{s,\omega}\otimes e^+_s.}
 \tag{L-15425.9}
\]

If

\[
 u={s+\bar t\over2},
 \tag{L-15425.10}
\]

then

\[
 \boxed{
 \langle j_{t,\omega},j_{s,\omega}\rangle
 =\sum_{d\ge1}{J_{2\omega}(d)\over d^{u+\omega}}
 ={\zeta(u-\omega)\over\zeta(u+\omega)}.}
 \tag{L-15425.11}
\]

This is the exact positive Kolmogorov decomposition of the arithmetic ratio in
its half-plane of absolute convergence.

## Zeta-law independence

Let `alpha>1` and choose an integer `N` from

\[
 \Pr(N=n)={n^{-\alpha}\over\zeta(\alpha)}.
 \tag{L-15425.12}
\]

Conditionally on `N=n`, choose a divisor `D` with

\[
 \Pr(D=d\mid N=n)
 ={J_{2\omega}(d)\over n^{2\omega}}\mathbf1_{d\mid n},
 \tag{L-15425.13}
\]

and put `M=N/D`. Then `D` and `M` are independent, with

\[
 \Pr(M=m)={m^{-(\alpha+2\omega)}\over\zeta(\alpha+2\omega)}
 \tag{L-15425.14}
\]

and

\[
 \Pr(D=d)
 ={\zeta(\alpha+2\omega)\over\zeta(\alpha)}
 J_{2\omega}(d)d^{-(\alpha+2\omega)}.
 \tag{L-15425.15}
\]

Indeed, their product is exactly

\[
 {J_{2\omega}(d)d^{-(\alpha+2\omega)}
   m^{-(\alpha+2\omega)}\over\zeta(\alpha)},
 \tag{L-15425.16}
\]

which is the joint law obtained from (L-15425.12)--(L-15425.13).

## Interpretation

The arithmetic local-place map is therefore completely explicit:

```text
parent integer
  -> Jordan-distributed divisor + independent residual factor.
```

It is genuinely isometric and its positivity is unconditional. No zeta zero,
analytic continuation, or RH-conditional identity enters the construction.

## Gap audit

- The coherent vectors belong to `ell^2` only for `Re s>1+omega`.
- Formula (L-15425.11) is a positive-kernel identity only in that half-plane.
- Analytic continuation of the scalar zeta ratio does not continue the
  Hilbert-valued feature across its abscissa of convergence.
- This lemma supplies the exact arithmetic isometry; it does not yet identify
  the critical physical Volterra metric.
