# L-106507 — Outer-only cancellation controls the all-pass charge

Claim ID: `L-106507`  
Status: **PROVED EXACT FOR FINITE RATIONAL ALL-PASS PAIRS**  
Created: 2026-08-25  
Depends on: canonical inner–outer factorization and the Dirichlet–Hankel identity  
RH status: **not assumed**

Let `N,D` be analytic rational functions with no boundary zero on the declared
regular contour and

\[
|N|=|D|
\]

on the boundary.  Reduce common analytic factors first and write

\[
U={N\over D}.
\]

## 1. Canonical outer-only cancellation

The inner–outer factorizations have the same boundary outer modulus.  After a
harmless constant phase there is one common outer factor `O` and finite inner
functions `B_+,B_-` such that

\[
\boxed{
N=OB_+,
\qquad
D=OB_-,
\qquad
U=B_+\overline{B_-}.
}
\tag{L-106507.1}

The topology-safe normalized endpoint difference is

\[
\boxed{
S={N-D\over O}=B_+-B_-.
}
\tag{L-106507.2}

Cancelling `O` is legitimate because it has no inner divisor.  Cancelling the
complete denominator `D=OB_-` would additionally erase `B_-` and place an
analytic source in `ker H_U`; that forbidden step is exactly the firewall of
`R-106417/R-106432`.

## 2. Dirichlet–Hankel domination

For an analytic function `f(z)=sum_(n>=0) f_n z^n`, use the boundary Dirichlet
seminorm

\[
\|f\|_{\mathcal D}^2
=\sum_{n\ge1}n|f_n|^2.
\]

The Hankel coefficient identity gives

\[
\boxed{
\|H_{\overline f}\|_{\mathcal S_2}^2
=\|f\|_{\mathcal D}^2.
}
\tag{L-106507.3}

Since `B_+` is analytic,

\[
H_U=H_{\overline{B_-}}T_{B_+}.
\]

Moreover

\[
H_{\overline{B_+}}T_{B_+}=H_1=0.
\]

Therefore

\[
\boxed{
H_U
=\left(H_{\overline{B_-}}-H_{\overline{B_+}}\right)T_{B_+}.
}
\tag{L-106507.4}

Because `T_(B_+)` is an isometry,

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
\le
\|H_{\overline{B_-}}-H_{\overline{B_+}}\|_{\mathcal S_2}^2
=
\|B_--B_+\|_{\mathcal D}^2
=
\left\|{N-D\over O}\right\|_{\mathcal D}^2.
}
\tag{L-106507.5}

This is a direct topology-sensitive bound.  It neither multiplies by the inner
denominator nor assumes a source subspace covers the bad model space.

## 3. Exact positive remainder

Let

\[
A=H_{\overline{B_-}}-H_{\overline{B_+}}.
\]

Since `T_(B_+)T_(B_+)^*=I-P_(K_(B_+))`, cyclicity gives

\[
\boxed{
\|B_--B_+\|_{\mathcal D}^2
-\|H_U\|_{\mathcal S_2}^2
=
\|A P_{K_{B_+}}\|_{\mathcal S_2}^2
\ge0.
}
\tag{L-106507.6)

Thus (L-106507.5) loses only an explicit positive numerator-model remainder.

## 4. Odd endpoint specialization

For `U_(K,lambda)` of `L-106501`,

\[
N-D=-2i\lambda(-1)^m\mathcal L_K.
\]

If `O_(K,lambda)` is the common outer spectral factor of the two endpoint
products, then

\[
\boxed{
\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2
\le
4\lambda^2
\left\|{\mathcal L_K\over O_{K,\lambda}}\right\|_{\mathcal D}^2.
}
\tag{L-106507.7)

The remaining analytic problem is now an outer-normalized Dirichlet estimate
for the positive current chaos of `L-106500`.  No inner partial index is hidden
inside the normalization.

## 5. Entire-window scope

For Xi, apply the finite theorem to regular canonical-product truncations and
retain common-zero, confluent, endpoint and cofinal errors.  Passage to the
entire function requires a uniform outer-factor construction and the declared
Dirichlet bound; neither is silently supplied here.
