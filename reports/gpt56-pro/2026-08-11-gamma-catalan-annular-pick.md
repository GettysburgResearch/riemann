# Gamma–Catalan safe-disc law and annular Pick continuation — 2026-08-11

## Freeze

```text
repository:   gfreund123/riemann
base PR:      #394
base branch:  research/gpt56-pro/91004-radial-curvature-depth-projector
base SHA:     82ee32348b05512514462966bfeb4e2de4ae5ecf
branch:       research/gpt56-pro/394-gamma-pick-annular-asymptotic
RH status:    UNPROVED
```

This continuation starts from PR #394's exact radial-curvature/Peano/Pick reduction. It attacks the high-carrier prime side rather than adding another equivalent criterion.

## I. Universal high-carrier law

Let

\[
 s_x=\frac12+ix,
 \qquad
 \ell_x=\log(2+|x|),
\]

and let `A_x(w)` be the single-safe-line unit-disc generator. On every fixed disc

\[
 |w|<R<\frac34,
\]

the new theorem gives

\[
 \frac{A_x(w)}{\ell_x}
 \longrightarrow
 \Phi(w)
 :=\frac1{2(1+\sqrt{1-w})^2}
\]

locally uniformly as `|x|->infinity`.

For `1/2<=R<3/4`, the quantitative form is

\[
 \max_{|w|=R}|A_x(w)-\ell_x\Phi(w)|
 \ll1+\left(\sqrt{1-R}-\frac12\right)^{-1}.
\]

The leading function is completely explicit:

\[
 \Phi(w)
 =\sum_{k\ge0}\frac{C_{k+1}}{8\,4^k}w^k
 =\int_0^1\frac{1}{1-w\lambda}
 \frac1\pi\sqrt{\lambda(1-\lambda)}\,d\lambda.
\]

Thus the high-carrier background is the Stieltjes transform of the beta-`(3/2,3/2)` density. Every fixed Pick, Loewner, Hausdorff, Hankel, and Bernstein packet wholly inside the safe disc is eventually strictly positive independently of RH.

## II. Unconditional safe-ray sign

The Cauchy boundary estimate yields an effective `C_0` such that

\[
 A_x(w)>0
 \qquad
 \left(
 0\le w\le\frac34-\frac{C_0}{\ell_x}
 \right)
\]

for all sufficiently large `|x|`.

In the radial variable `t=1-w`, this proves positivity of the tangent defect

\[
 J_x(1)+J_x'(1)(t-1)-J_x(t)>0
\]

for

\[
 t\ge\frac14+\frac{C_0}{\ell_x}.
\]

## III. Sharp growing-order positive jet

Writing

\[
 A_x(w)=\sum_{k\ge0}a_k(x)w^k,
 \qquad
 c_k=\frac{C_{k+1}}{8\,4^k},
\]

one obtains

\[
 |a_k(x)-\ell_xc_k|
 \ll(k+4)\left(\frac43\right)^k.
\]

Since `c_k asymp k^(-3/2)`, every fixed `epsilon>0` gives

\[
 a_k(x)>0
\]

uniformly through

\[
 k\le
 \left(
 \frac1{\log(4/3)}-\varepsilon
 \right)
 \log\ell_x,
\]

where

\[
 \frac1{\log(4/3)}
 =3.4760594967822069\ldots.
\]

Every fixed-order Hausdorff finite difference has the same leading range. Its positive main term is the exact beta cell

\[
 \frac1\pi B\left(k+\frac32,m+\frac32\right).
\]

## IV. Exact sharpness against one off-line pair

A matching off-line zero of depth `y` has pole

\[
 w_y=1-y^2
\]

and coefficient contribution

\[
 -4my^2w_y^{-k-3}.
\]

It competes with the Catalan background at order

\[
 k_{\rm det}(x,y)
 \sim
 \frac{\log\ell_x}
 {\log(1/(1-y^2))}.
\]

The earliest possible universal detection occurs as `y->1/2`, giving exactly

\[
 k_{\rm edge}(x)
 \sim
 \frac{\log\ell_x}{\log(4/3)}.
\]

This matches the proved positive range. Hence fixed safe-disc packets and strictly subcritical growing order are high-carrier blind by an exact asymptotic mechanism, not merely because no proof was found.

## V. Vinogradov–Korobov penetration of the sign annulus

A general transfer lemma shows that any logarithmic-derivative estimate

\[
 \left|\frac{\zeta'}{\zeta}(\sigma+it)\right|
 \le B(T)=o(\log T)
\]

in a zero-free strip

\[
 \sigma\ge1-c_0\eta(T)
\]

implies the expanding-disc asymptotic

\[
 A_x(w)=\ell_x\Phi(w)+O(1+B(T))
\]

through

\[
 |w|\le\frac34+c_1\eta(|x|+3).
\]

Inserting the standard Vinogradov–Korobov logarithmic-derivative estimate gives unconditional real-ray positivity through

\[
 0\le w\le\frac34+
 \frac{c_1}
 {\{\log(|x|+3)\}^{2/3}
  \{\log\log(|x|+3)\}^{1/3}}.
\]

Equivalently, the radial tangent defect is positive slightly inside `0<t<1/4` at the same scale. This does not improve the classical zero-free region; it transports its analytic content into a Pick-sign statement.

## VI. Verification

Retained finite verdicts:

```text
PASS_GAMMA_CATALAN_SAFE_DISC
PASS_VK_ANNULAR_PICK_RAY
```

The first replay checks Catalan coefficients, the beta Stieltjes integral, Hausdorff cells, a strict finite Pick matrix, the Cauchy boundary scale, and planted-pair crossover. The second checks only the elementary Vinogradov–Korobov scale transfer. Neither evaluates zeta or certifies the analytic theorems.

## Exact boundary

```text
high-carrier safe-disc Catalan law                    PROPOSED COMPLETE
beta(3/2,3/2) Stieltjes/Pick background              EXACT
real safe-ray positivity to 3/4-C/log|x|              PROPOSED COMPLETE
growing coefficient/Hausdorff positivity             PROPOSED COMPLETE
sharp edge constant 1/log(4/3)                       PROPOSED COMPLETE
subcritical safe-disc tests high-carrier blind        PROPOSED COMPLETE FIREWALL
VK-scale annular real-ray positivity                  PROPOSED COMPLETE / EXTERNAL INPUT
fixed annular radius beyond 3/4                       OPEN / RH-BEARING
full Pick/Stieltjes positivity to radius one          OPEN / RH-EQUIVALENT
radial curvature positivity on 0<t<1/4                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
