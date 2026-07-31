# L-20303 — Affine Möbius extensions and the invariant zero signature

Claim ID: `L-20303`  
Title: All Dirichlet-polynomial tails beyond the exact inversion cutoff preserve local reconstruction, but none can alter the zeta-zero residual  
Status: `PROPOSED — COMPLETE ALGEBRAIC PROOF; FORM NORMALIZATION INHERITED`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: `L-20301`; the Mellin factorization of `L-16205`; the centered zero-side Weil formula  
Scope: optimization and impossibility theorem for the explicit complete-kernel tail  
Related counterexample candidates: none

## 1. Affine extension family

Let \(h\), \([a,b]\), \(g(u)=u^{-1/2}h(u)\), and \(\psi\) be as in
`L-20301`. Fix one exact inversion cutoff \(N_0\) satisfying

\[
N_0a>b.
\tag{L-20303.1}
\]

Choose any \(M\ge N_0\) and arbitrary coefficients

\[
c_{N_0+1},\ldots,c_M\in\mathbb C,
\tag{L-20303.2}
\]

while fixing

\[
\boxed{c_n=\mu(n)\qquad(1\le n\le N_0).}
\tag{L-20303.3}
\]

Put

\[
P_c(s)=\sum_{n\le M}\frac{c_n}{n^s},
\qquad
q_c=P_c(1)=\sum_{n\le M}\frac{c_n}{n},
\tag{L-20303.4}
\]

and define

\[
\boxed{
f_{c,h}^+(x)
=
\sum_{n\le M}c_ng(nx)
-
q_c\!\left(\int g\right)\psi(x).
}
\tag{L-20303.5}
\]

Even extension gives \(f_{c,h}\).

Exactly as before,

\[
f_{c,h}(0)=0,
\qquad
\int f_{c,h}=0,
\tag{L-20303.6}
\]

so \(E(f_{c,h})\) is a global weak Weil-radical vector.

## 2. Local reconstruction is independent of the free coefficients

Define

\[
A_c(k)=\sum_{\substack{d\mid k\\d\le M}}c_d.
\tag{L-20303.7}
\]

For \(k\le N_0\), every divisor \(d\mid k\) satisfies \(d\le N_0\), so
(L-20303.3) gives

\[
A_c(1)=1,
\qquad
A_c(k)=0\quad(2\le k\le N_0).
\tag{L-20303.8}
\]

For \(u\in[a,b]\), every term with \(k>N_0\) has

\[
ku>(N_0a)>b
\]

and therefore vanishes. The source correction is also zero on the target
interval. Consequently

\[
\boxed{
E(f_{c,h})(u)=h(u)
\qquad(a\le u\le b)
}
\tag{L-20303.9}
\]

for **every** choice of the coefficients above \(N_0\).

Thus exact local inverses form an affine space of arbitrarily large finite
dimension. The Möbius prefix is forced; the higher Dirichlet-polynomial tail is
free.

## 3. Exact residual producers

Let

\[
t_{c,h}=E(f_{c,h})-h.
\tag{L-20303.10}
\]

Its physical formula is

\[
\boxed{
\begin{aligned}
t_{c,h}(u)
={}&u^{1/2}\sum_{k>N_0}A_c(k)g(ku)\\
&-u^{1/2}q_c\left(\int g\right)
\sum_{m\ge1}\psi(mu).
\end{aligned}
}
\tag{L-20303.11}
\]

The Mellin formula is

\[
\boxed{
\widehat t_{c,h}(z)
=
\bigl[\zeta(s)P_c(s)-1\bigr]\widehat h(z)
-
q_c\widehat h(i/2)\zeta(s)M_\psi(z),
\quad s=\frac12-iz.
}
\tag{L-20303.12}
\]

The entire coefficient freedom is now explicit.

## 4. Zeta-zero residual is invariant

At every nontrivial zero parameter \(z_\rho\),

\[
\zeta\!\left(\frac12-iz_\rho\right)=0.
\]

Equation (L-20303.12) therefore gives

\[
\boxed{
\widehat t_{c,h}(z_\rho)
=-\widehat h(z_\rho)
}
\tag{L-20303.13}
\]

for every \(M\) and every free coefficient vector.

For two localized targets \(h,k\) and arbitrary affine extensions,
polarization of global radicality gives

\[
\boxed{
Q_W(t_{c,h},t_{d,k})=Q_W(h,k).
}
\tag{L-20303.14}
\]

Hence the complete tail Weil matrix is independent of every optimization
coefficient above the exact inversion prefix.

This is an important impossibility theorem:

\[
\boxed{
\text{mollifier optimization can improve analytic norms and Schur cross maps,
but cannot repair a hidden zeta-zero signature.}
}
\tag{L-20303.15}
\]

## 5. Exact norm lower bounds from one zero

Suppose a Hilbert norm \(X\) has bounded evaluation at \(z_\rho\):

\[
|\widehat q(z_\rho)|
\le C_{\rho,X}\|q\|_X.
\tag{L-20303.16}
\]

Then every affine local extension satisfies

\[
\boxed{
\|t_{c,h}\|_X
\ge
\frac{|\widehat h(z_\rho)|}{C_{\rho,X}}.
}
\tag{L-20303.17}
\]

For the reciprocal Hardy norm of strip width \(\tau\) and a critical-line
ordinate \(\gamma\in\mathbb R\), the evaluation constant used in the repository
is

\[
C_{\gamma,\tau}^2=\frac\pi{4\tau}.
\]

Therefore

\[
\boxed{
\|t_{c,h}\|_\tau^2
\ge
\frac{4\tau}{\pi}|\widehat h(\gamma)|^2.
}
\tag{L-20303.18}
\]

A finite evaluation Gram gives the corresponding packet lower bound.

## 6. What the free coefficients can optimize

Let \(X\) be any positive Hilbert norm for which all dilation columns are in the
domain. After the forced Möbius prefix is fixed, the map

\[
(c_{N_0+1},\ldots,c_M)
\longmapsto t_{c,h}
\]

is affine. Consequently

\[
\|t_{c,h}\|_X^2
\tag{L-20303.19}
\]

is a finite positive-semidefinite quadratic function of the free coefficients.
The best extension in that norm is obtained from exact or directed normal
equations; kernel directions are handled by the Moore–Penrose/range
formulation or by exact rational constraints.

For a packet \(J\), one may likewise minimize:

- the Hardy tail operator norm;
- the Hilbert–Schmidt tail norm;
- the Schur cross norm \(\|C^{-1/2}ZJ\|\);
- a weighted combination of positive analytic error channels.

The invariant term

\[
Q_W(T,T)=Q_W(J,J)
\]

must not be placed in that optimization objective as if it depended on the free
coefficients.

## 7. Production implication

The proof-producing scheduler should separate:

```text
immutable zero signature:
    complete localized Weil matrix on the target kernel;

optimizable extension cost:
    Hardy/form-domain realization and positive-complement Schur cross.
```

A numerical improvement in the latter cannot be advertised as evidence for the
sign of the former.

## 8. Proof boundary

- The affine local reconstruction and zero invariance are exact.
- The norm-minimization statement is finite positive quadratic algebra.
- No uniform optimizer bound is proved as support and packet dimension grow.
- The invariant zero signature remains the final RH-bearing form.
- No proof of RH is claimed.
