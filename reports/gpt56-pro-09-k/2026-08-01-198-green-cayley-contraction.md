# Green-lift contraction: exact Cayley reduction and the compression no-go

Agent: `gpt56-pro-09-k`  
Date: 2026-08-01  
PR: #202  
Verdict: **the completed-domain contraction has not been proved**

## Objective

The requested theorem was

\[
\|CKE\|\le1
\]

on the actual Green-minimizer plus-feature range, using the lifted multiplier

\[
\kappa(s,u)=\frac{1-s-u}{1+s+u},\qquad |\kappa|\le1.
\]

The source argument combined pointwise multiplier contraction with the
trace-fibre Euler equation. This pass reconstructed the exact operator algebra
and tested that inference independently.

## 1. Exact Cayley reduction

With stacked Green moments

\[
\mathcal Mx=(\sqrt{w_\sigma}M_{\sigma,x})_\sigma,
\qquad
\mathcal Nx=(\sqrt{w_\sigma}N_{\sigma,x})_\sigma,
\]

the features are

\[
G_+x=\frac12(\mathcal Mx+\mathcal Nx),
\qquad
G_-x=\frac12(\mathcal Mx-\mathcal Nx).
\]

Whenever `ker M subset ker N`, define the Green moment operator by

\[
\mathcal A(\mathcal Mx)=\mathcal Nx.
\]

Then exactly

\[
CKE=(I-\mathcal A)(I+\mathcal A)^{-1}
\]

and

\[
I-(CKE)^*(CKE)
=2(I+\mathcal A)^{-*}
 (\mathcal A+\mathcal A^*)
 (I+\mathcal A)^{-1}.
\]

Thus contractivity is equivalent to accretivity of the Green moment operator.
If `A` is self-adjoint positive, the defect factor is

\[
W=2\mathcal A^{1/2}(I+\mathcal A)^{-1},
\qquad
I-(CKE)^*(CKE)=W^*W.
\]

## 2. Theta-Hankel form of the missing estimate

For

\[
g=f/\Psi,
\qquad
\varphi_{\sigma,\omega}(r)=e^{\sigma\omega r/2}\Psi(r),
\]

let `H_(sigma,omega)` be the Hankel operator with kernel
`varphi_(sigma,omega)(s+u)`. Then

\[
M_\sigma=H_\sigma g,
\qquad
N_\sigma=(XH_\sigma+H_\sigma X)g.
\]

The accretive form is exactly

\[
\operatorname{Re}\langle H g,(XH+HX)g\rangle
=2\langle g,\mathcal K_Hg\rangle,
\]

where

\[
\mathcal K_H
=HXH+\frac14[H,[H,X]].
\]

This is the theta-Hankel Gram/anticommutator of `L-19814`. A concrete sufficient
estimate on the coupled Green source range is

\[
\|X^{-1/2}[H,X]g\|
\le2\|X^{1/2}Hg\|.
\]

No proof of this range estimate was found.

## 3. Exact refutation of the shortcut

The implication

```text
Euler orthogonality
+ positivity on ker R
+ fibre minimality
+ CE=I
+ ||K||<1
=> ||CKE||<=1
```

is false.

The retained exact rational example has

\[
G_+(x,n)=x+\frac32n,
\qquad
G_-(x,n)=\frac32x+n,
\]

so

\[
Q=G_+^2-G_-^2=\frac54(n^2-x^2).
\]

For `R(x,n)=x`, the Green minimizer is `(x,0)`, the kernel direction has floor
`5/4`, and the Euler cross term is zero. Yet the observed Green transfer is
multiplication by `3/2`.

It also has a strict diagonal lifted realization

\[
C(a,b)=a+b,
\qquad
Ey=(4y/3,-y/3),
\qquad
K=\operatorname{diag}(9/10,-9/10),
\]

with

\[
CE=I,
\qquad
\|K\|=9/10,
\qquad
\|CKE\|=3/2.
\]

Therefore pointwise multiplier contraction does not survive a noncommuting
Volterra compression automatically.

## 4. Correct completion target

The load-bearing theorem is now exactly one of the following equivalent
statements on the actual Green moment range:

\[
\operatorname{Re}\mathcal A\succeq0,
\]

\[
\sum_\sigma w_\sigma
\operatorname{Re}\langle
 H_{\sigma,\omega}g,
 (XH_{\sigma,\omega}+H_{\sigma,\omega}X)g
\rangle\ge0,
\]

or the stronger range-Hardy bound

\[
\|X^{-1/2}[H_{\sigma,\omega},X]g\|
\le2\|X^{1/2}H_{\sigma,\omega}g\|.
\]

An alternative valid closure would be a genuine coisometric Green lift with
`E` isometric and `C=E*`; then the defect has the automatic two-square
factorization

\[
I-(E^*KE)^*(E^*KE)
=E^*(I-K^*K)E+((I-EE^*)KE)^*((I-EE^*)KE).
\]

The actual Green lift has not been proved to satisfy that compatibility.

## 5. Reproducibility

`X-19802` is standard-library only and uses exact `fractions.Fraction`.
The retained result is

```text
kernel floor   5/4
green value   -5/4
||K||          9/10
||CKE||        3/2
```

with proof-object SHA-256

```text
2357472909fe1507c7982f53bd1c7c6a6789b0087612db5418bef33469c83b8b
```

Eight adversarial tests pass.

## Final status

The Cayley factorization is a useful breakthrough: it gives the exact positive
defect that a successful proof must construct. But the desired theta
accretivity has not been established. The existing finite generalized
eigenvalues below one remain evidence, not a continuum proof. No proof of RH is
claimed.
