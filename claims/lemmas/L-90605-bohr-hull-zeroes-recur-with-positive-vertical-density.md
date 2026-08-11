# L-90605 — A Bohr-hull zero forces positive vertical density of actual approximant zeros

Claim ID: `L-90605`  
Status: **PROPOSED COMPLETE GENERAL ALMOST-PERIODIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: Kronecker minimality, Rouché's theorem; the torus-zero constructions `L-90601/L-90603`  
Scope: finite exponential/Dirichlet producers and their functional-equation symmetrisations; no statement about the infinite limiting canonical system or RH

## 1. The hull

Fix \(N\). Let \(\mathcal P_N\) be the primes at most \(N\), and let

\[
\mathbb T_N=\prod_{p\in\mathcal P_N}\{z:|z|=1\}.
\]

For \(\omega\in\mathbb T_N\), extend \(\omega\) completely multiplicatively to the integers supported on these primes. Given coefficients \(a_n\), define the Bohr hull

\[
F_\omega(z)=\sum_{n\le N}a_n\omega(n)n^{-z}.
\tag{L-90605.1}
\]

The vertical translate of the untwisted polynomial corresponds to

\[
\omega_t(p)=p^{-it}.
\tag{L-90605.2}
\]

Because the numbers \(\{\log p:p\le N\}\) are linearly independent over \(\mathbb Q\), the flow \(t\mapsto\omega_t\) is minimal on \(\mathbb T_N\).

## 2. Syndetic recurrence of phase neighbourhoods

### Lemma 2.1

For every nonempty open \(U\subset\mathbb T_N\), the hitting set

\[
\mathcal R(U)=\{t\ge0:\omega_t\in U\}
\]

is relatively dense: there is \(L(U)<\infty\) such that every interval \([T,T+L(U)]\) meets \(\mathcal R(U)\).

### Proof

For every \(x\in\mathbb T_N\), minimality gives \(s_x\ge0\) with \(x\omega_{s_x}\in U\). By continuity there is a neighbourhood \(V_x\) of \(x\) such that \(V_x\omega_{s_x}\subset U\). Compactness gives a finite cover \(V_{x_1},\ldots,V_{x_r}\). Put \(L=\max s_{x_j}\). For any \(T\), \(\omega_T\in V_{x_j}\) for some \(j\), hence \(\omega_{T+s_{x_j}}\in U\). ∎

## 3. Hull zero to positive-density actual zeros

Let

\[
H(z)=\sum_{n\le N}a_n(z+\alpha_n)n^{-z},
\tag{L-90605.3}
\]

where the \(\alpha_n\) are fixed. Suppose some hull member \(F_{\omega_*}\) has a zero at \(z_0\).

Choose a closed disc \(\overline D\) centred at \(z_0\) whose boundary contains no zero of \(F_{\omega_*}\), and put

\[
\delta=\min_{\partial D}|F_{\omega_*}|>0.
\]

Uniform continuity of (L-90605.1) gives a phase neighbourhood \(U\) of \(\omega_*\) such that

\[
\sup_{z\in\partial D}|F_\omega(z)-F_{\omega_*}(z)|<\delta/4
\qquad(\omega\in U).
\tag{L-90605.4}
\]

For \(t\to\infty\),

\[
\frac{H(z+it)}{z+it}
=
F_{\omega_t}(z)
+
\sum_{n\le N}a_n\omega_t(n)n^{-z}\frac{\alpha_n}{z+it},
\tag{L-90605.5}
\]

and the second term tends to zero uniformly on \(\partial D\). Therefore, for every sufficiently large \(t\in\mathcal R(U)\),

\[
\sup_{\partial D}\left|
\frac{H(z+it)}{z+it}-F_{\omega_*}(z)
\right|<\delta/2.
\]

Rouché gives the same positive number of zeros in \(D\). Hence \(H\) has a zero in \(D+it\).

By Lemma 2.1 these translates occur with bounded gaps. Choosing disjoint subfamilies of the discs gives:

### Theorem 3.1

If one Bohr-hull member has a zero at \(z_0\), then for every neighbourhood \(V\) of \(z_0\) there is \(c_{N,V}>0\) such that

\[
\boxed{
\#\{z:H(z)=0,\ \Re z\in\Re V,\ 0<\Im z<T\}
\ge c_{N,V}T-O_{N,V}(1).
}
\tag{L-90605.6}
\]

More precisely, every sufficiently long vertical interval contains a zero of \(H\) whose translation back to the base strip lies in \(V\).

No simplicity of the hull zero is required.

## 4. Application to the raw Brownian numerator

For the raw Brownian producer,

\[
H_N(z)=\sum_{n\le N}C_{N,n}n^{-2z}(z+\alpha_{N,n}).
\]

`L-90601` constructs, for every fixed \(1/4<\sigma<1/2\) and every sufficiently large \(N\), a completely multiplicative \(\chi\) with

\[
F_{N,\chi}(\sigma)=\sum_{n\le N}C_{N,n}\chi(n)n^{-2\sigma}=0.
\]

Apply Theorem 3.1 with the phase flow \(p^{-2it}\). For every \(\varepsilon>0\),

\[
\boxed{
\liminf_{T\to\infty}\frac1T
\#\{z:H_N(z)=0,\ |\Re z-\sigma|<\varepsilon,\ 0<\Im z<T\}>0.
}
\tag{L-90605.7}
\]

Thus the runaway zeros are not a sparse sequence: for each fixed sufficiently large truncation they recur with positive lower vertical density in every prescribed neighbourhood of the torus-zero line.

## 5. Positive mixtures

Let

\[
D_N(s)=sB_N(s)+A_N(s)
\]

be any finite positive Brownian cutoff mixture covered by `L-90603`. That theorem constructs, for each fixed \(1/2<\beta<1\), a twist \(\chi\) with \(B_{N,\chi}(\beta)=0\). Applying the same argument gives

\[
\boxed{
\liminf_{T\to\infty}\frac1T
\#\{s:D_N(s)=0,\ |\Re s-\beta|<\varepsilon,\ 0<\Im s<T\}>0.
}
\tag{L-90605.8}
\]

This applies to both the logarithmic Nörlund and central-binomial Green mixtures.

## 6. Functional-equation symmetrisation

Suppose

\[
\mathcal X_N(s)=A(s)D_N(s)+A(1-s)D_N(1-s),
\qquad
A(s)=\pi^{-s/2}\Gamma(1+s/2).
\tag{L-90605.9}
\]

On every compact \(K\subset\{\Re s>1/2\}\), uniformly as \(t\to\infty\),

\[
\frac{\mathcal X_N(s+it)}{itA(s+it)}
=
B_{\omega_t}(s)+o_K(1),
\tag{L-90605.10}
\]

because the one-sided affine remainder is \(o(1)\), while Stirling gives

\[
\left|\frac{A(1-s-it)}{A(s+it)}\right|
\ll_K t^{1/2-\Re s}=o_K(1).
\]

The \(o_K(1)\) is uniform for every large return time, not merely along one chosen sequence. The phase-neighbourhood/Rouché argument therefore applies unchanged:

\[
\boxed{
\liminf_{T\to\infty}\frac1T
\#\{s:\mathcal X_N(s)=0,\ |\Re s-\beta|<\varepsilon,\ 0<\Im s<T\}>0.
}
\tag{L-90605.11}
\]

Thus finite functional-equation symmetry inherits a positive-density family of off-line zeros.

## 7. Producer-design criterion

A viable globally stable finite Dirichlet producer must satisfy the **complete Bohr-hull condition**

\[
\boxed{
F_\omega(z)\ne0
\quad\text{for every }\omega\in\mathbb T_N
\text{ and every }z\text{ in the target half-plane}.
}
\tag{L-90605.12}
\]

Checking the untwisted member \(\omega=1\), any finite collection of vertical scans, local convergence to \(\xi\), or exact functional-equation symmetry is insufficient. A single hull zero forces linearly many actual violations.

The selected-prime polygon argument of `L-90601/L-90603` is a general mechanism for disproving (L-90605.12) whenever independent prime fibers have divergent total mass and negligible largest fiber.

## 8. Proof boundary

```text
Bohr phase returns are syndetic                      proved
one hull zero gives positive-density actual zeros    proved
raw Brownian positive-density violations             conditional only on L-90601
positive-mixture/symmetrized violations              conditional only on L-90603/L-90604
complete-hull producer-design firewall                proved
height-dependent or infinite producer                 still open
RH                                                     unproved
```
