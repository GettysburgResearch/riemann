# L-105226 — Direct Clark sampling bypasses canonical-product exhaustion of the residue moment Gram

Claim ID: `L-105226`  
Status: **PROPOSED EXACT ENTIRE-DE-BRANGES THEOREM UNDER EXPLICIT HYPOTHESES; independent review pending**  
Created: 2026-08-23  
Depends on: `L-105224`  
RH status: **not assumed**

## 1. Entire derivative-real-rooted setting

Let \(G\) be a real entire function with simple real zeros \(\mathcal C\), and
assume

\[
E=G+iG'
\]

is Hermite--Biehler. Let \(\mathcal H(E)\) be its de Branges space and let
\(\mathcal H_{\mathcal C}\) be the closed span of the mutually orthogonal
reproducing kernels \(K_c\), \(c\in\mathcal C\). At every such zero,

\[
K_c(c)=\frac{G'(c)^2}{\pi}.
\tag{L-105226.1}
\]

Let \(p\) be a real entire antiderivative of \(G\), and define

\[
\rho_c=\frac{p(c)}{G'(c)}.
\tag{L-105226.2}
\]

Fix a real centre \(a\) and retain

\[
g_a(z)=\frac{6}{(z-a+i)(z-a+2i)(z-a+3i)},
\qquad
w_c=|g_a(c)|^2.
\tag{L-105226.3}
\]

Assume only the two moment-finiteness conditions

\[
N_a=\sum_{c\in\mathcal C}w_c<\infty,
\qquad
B_a=\sum_{c\in\mathcal C}w_c\rho_c^2<\infty.
\tag{L-105226.4}
\]

## 2. Direct Hilbert-space construction

The orthogonal kernel series

\[
\boxed{
u_a=\pi\sum_{c\in\mathcal C}\frac{g_a(c)}{G'(c)}K_c,}
\tag{L-105226.5}
\]

\[
\boxed{
v_a=\pi\sum_{c\in\mathcal C}\frac{g_a(c)\rho_c}{G'(c)}K_c
}
\tag{L-105226.6}
\]

converge in \(\mathcal H_{\mathcal C}\). They satisfy

\[
u_a(c)=g_a(c)G'(c),
\qquad
v_a(c)=g_a(c)p(c)
\tag{L-105226.7}
\]

at every spectral point and

\[
\boxed{
\|u_a\|^2=\pi N_a,
\qquad
\langle v_a,u_a\rangle=-\pi A_a,
\qquad
\|v_a\|^2=\pi B_a,
}
\tag{L-105226.8}
\]

where

\[
A_a=-\sum_cw_c\rho_c.
\]

Hence

\[
\boxed{\|u_a\wedge v_a\|^2=\pi^2(N_aB_a-A_a^2).}
\tag{L-105226.9}
\]

No polynomial truncation, root-by-root limiting argument, Bézout interpolant,
or nonreal-critical subtraction occurs.

## 3. Safe-point representation of the count vector

Put

\[
\lambda_h=a-ih,
\qquad
(\gamma_1,\gamma_2,\gamma_3)=(-3,6,-3),
\qquad
w_h=\overline{\lambda_h}.
\]

The finite safe-point vector

\[
\widetilde u_a
=-\pi\sum_{h=1}^3\frac{\gamma_h}{G(\lambda_h)}K_{w_h}
\tag{L-105226.10}
\]

has the same samples as \(u_a\) at every zero of \(G\). Therefore

\[
\boxed{P_{\mathcal H_{\mathcal C}}\widetilde u_a=u_a.}
\tag{L-105226.11}
\]

If the Clark family is complete in \(\mathcal H(E)\), then the projection is
unnecessary and \(\widetilde u_a=u_a\).

## 4. Application to a reverse--Rolle step

At a downward Xi step take

\[
p=\Xi^{(k-1)},
\qquad
G=\Xi^{(k)}.
\]

Once \(G\) is known to have only simple real zeros, the usual real-zero
canonical product gives the Hermite--Biehler sign for \(G+iG'\). Under the
moment finiteness in (L-105226.4), the actual residue Gram is therefore
defined directly in the entire de Branges space.

Thus the former gate `DBEX105230`, formulated as convergence of
canonical-product truncations, is not intrinsically necessary. It can be
replaced by the explicit and narrower conditions

```text
derivative-real-rooted Hermite--Biehler structure;
finite weighted second residue moment.
```

The conclusion-bearing difficulty is the quantitative angle or centered Gram
estimate, not an interpolation/exhaustion theorem.

## 5. Scope

The theorem does not prove \(B_a<\infty\) for an unknown low Xi derivative,
does not estimate the angle between \(u_a\) and \(v_a\), and does not handle
multiple derivative zeros without a confluent Clark ledger. It removes only
the artificial canonical-product-exhaustion layer from the simple
derivative-real-rooted stratum.
