# Exact divisor resummation of the Ramanujan-weighted theta dual

Date: 2026-10-20. Status: native algebraic lemma with proof; the analytic
finite-profile closure and self-absorption are a separate proposed result.

Source: Dunn--Radziwill,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
(1.4)--(1.5), (2.3), (5.7), (5.13)--(5.14), (5.68), (5.73)--(5.79).
All sums use primary generators in \(E=\mathbb Q(\omega)\).
The level \(r\) is squarefree and prime to 3, \(R=Nr\), and
\(\lambda=\sqrt{-3}\).

## 1. The identity in an exact normalization

Let \(\kappa\) be any fixed unitary multiplicative character on primary
elements prime to 3, of conductor a power of 3. The algebra below does not
require \(\kappa^3=1\). Fix an integer \(a\), which is the angular order
of the series in this lemma. Define

\[
 \mathcal G_{k,\kappa}(w;a)=
 \sum_c\widetilde g(c)\kappa(c)\alpha(c)^a
                 \overline{(c/k)_3}(Nc)^{-w},
 \tag{D1}
\]

\[
 Z_{k,\kappa}(w;a)=
 \sum_{(d,k)=1}\kappa(d)^3\alpha(d)^{3a}(Nd)^{1/2-3w},
 \qquad
 Q_{k,\kappa}(w;a)=Z_{k,\kappa}(w;a)\mathcal G_{k,\kappa}(w;a).
 \tag{D2}
\]

Thus the index \(w\) of \(Z_{k,\kappa}\) in this note already includes
the substitution \(3w-1/2\). Write

\[
 z_{\mathfrak p}=\kappa(\mathfrak p)^3
            \alpha(\mathfrak p)^{3a}q^{1/2-3w},
 \qquad q=N\mathfrak p.
 \tag{D3}
\]

The raw, fully cube-completed Ramanujan-weighted series is

\[
 \mathscr D_{r,\kappa}(w;a)=
 \sum_{c,d}\widetilde g(c)\kappa(cd^3)\alpha(cd^3)^a
 (Nd)^{1/2}c_r(cd^3)(Nc(Nd)^3)^{-w}.
 \tag{D4}
\]

Here
\(c_r(n)=\mu_E(r/(r,n))\varphi_E((r,n))\), including its sign.
The \(c\)-sum is squarefree automatically because
\(|\widetilde g(c)|=\mu_E^2(c)\).

**Exact lemma.** In the absolutely convergent half-plane \(\Re w>1\),

\[
 \boxed{
 \mathscr D_{r,\kappa}(w;a)=
 \sum_{k\mid r}
 \widetilde g(k)\kappa(k)\alpha(k)^a (Nk)^{1-w}
 Q_{k,\kappa}(w;a)
 \prod_{\mathfrak p\mid r/k}(qz_{\mathfrak p}-1).
 }
 \tag{D5}
\]

Both sides subsequently agree wherever their meromorphic continuations
exist. This is an identity of actual cubic Gauss coefficients, not an
Euler product for those coefficients.

## 2. Proof retaining the excluded primes

Split \(c=hc_0\), with \(h\mid r\) and \((c_0,r)=1\). Split
\(d=d_0d_r\), where \((d_0,r)=1\) and \(d_r\mid r^\infty\).
For a prime \(\mathfrak p\mid h\), the local \(d_r\)-sum is
\((q-1)/(1-z_{\mathfrak p})\). For a prime
\(\mathfrak p\mid r/h\), it is

\[
 -1+(q-1)\sum_{j\ge1}z_{\mathfrak p}^j
       =\frac{-1+qz_{\mathfrak p}}{1-z_{\mathfrak p}}.
 \tag{D6}
\]

The full cube product is
\(Z_{1,\kappa}(w;a)=\prod_{\mathfrak p}(1-z_{\mathfrak p})^{-1}\).
Twisted multiplicativity (2.3) and cubic reciprocity give

\[
 \begin{split}
 \mathscr D_{r,\kappa}(w;a)
 ={}& Z_{1,\kappa}(w;a)
 \sum_{h\mid r}
  \widetilde g(h)\kappa(h)\alpha(h)^a(Nh)^{-w}
  \varphi_E(h)
  \prod_{\mathfrak p\mid r/h}(-1+qz_{\mathfrak p})\\
 &\hspace{12mm}\times
 \sum_{(c_0,r)=1}
 \widetilde g(c_0)\kappa(c_0)\alpha(c_0)^a
             \overline{(c_0/h)_3}(Nc_0)^{-w}.
 \end{split}
 \tag{D7}
\]

In the inner sum, the primes of \(h\) are already excluded by the cubic
symbol. Exclude the remaining primes using
\(\mathbf1_{(c_0,r/h)=1}=\sum_{e\mid(c_0,r/h)}\mu_E(e)\).
Set \(c_0=et\). Terms with \((e,t)\ne1\) vanish on both sides of
twisted multiplicativity, and

\[
 \widetilde g(h)\widetilde g(e)
       \overline{(e/h)_3}=\widetilde g(he),\qquad
 \overline{(t/e)_3}\,\overline{(t/h)_3}
       =\overline{(t/he)_3}.
 \tag{D8}
\]

Group by \(k=he\mid r\). The residual \(t\)-sum is exactly
\(\mathcal G_{k,\kappa}(w;a)\), with all the primes of \(k\) excluded.
For each prime of \(k\), the choice \(\mathfrak p\mid h\) contributes
\(q-1\), whereas the choice \(\mathfrak p\mid e\) contributes
\(-(-1+qz_{\mathfrak p})\). Their sum is

\[
 (q-1)-(-1+qz_{\mathfrak p})=q(1-z_{\mathfrak p}).
 \tag{D9}
\]

Therefore the coefficient of \(\mathcal G_{k,\kappa}\) is

\[
 \widetilde g(k)\kappa(k)\alpha(k)^a(Nk)^{1-w}
 Z_{1,\kappa}(w;a)
 \prod_{\mathfrak p\mid k}(1-z_{\mathfrak p})
 \prod_{\mathfrak p\mid r/k}(qz_{\mathfrak p}-1).
 \tag{D10}
\]

The first product converts \(Z_{1,\kappa}\) to \(Z_{k,\kappa}\).
This proves (D5). In particular, omitting the deleted Euler factors would
destroy the exact cancellation (D9).

## 3. Consequence to the right of the half-line

If \(\Re w\ge1/2+\delta\), \(\delta>0\), then
\(|qz_{\mathfrak p}|\le q^{-3\delta}\). For every \(\epsilon>0\),

\[
 \prod_{\mathfrak p\mid r}(1+q^{-3\delta})
   \ll_{\delta,\epsilon}R^\epsilon.
 \tag{D11}
\]

One proof chooses \(q_0(\delta,\epsilon)\) such that
\(1+q^{-3\delta}\le q^\epsilon\) for \(q\ge q_0\); the product over
the finitely many smaller primes is an absolute constant. Consequently,
whenever the continued identity is available,

\[
 |\mathscr D_{r,\kappa}(w;a)|
 \ll_{\delta,\epsilon}R^\epsilon
       \sum_{k\mid r}(Nk)^{1-\Re w}|Q_{k,\kappa}(w;a)|.
 \tag{D12}
\]

This inequality is uniform in the fixed finite list of profiles and in
the imaginary part of \(w\). It does not assert a mean-value bound.

## 4. Exact original and dual angular orientations

The original series in DR Proposition 5.2 has angular factor
\(\alpha(c)^\ell\). Its reflected raw theta series has angular factor
\(\alpha(\mu)^{-\ell}\). Thus **the substitution in (D1)--(D12) is
\(a=-\ell\), \(w=1-s\)**. In particular the reflected cube Euler factor
contains \(\alpha(d)^{-3\ell}\), and the reflected cubic character
remains the conjugate symbol \(\overline{(c/k)_3}\).

The coefficient identity comes from \(a^*(\mu)\) in DR (5.73)--(5.74).
Because those formulas conjugate \(\tau,\tau_1,\tau_2\), their squarefree
coefficients involve \(g(c)\), rather than \(\overline{g(c)}\).
That is why (D8) has the stated orientation.

For the trivial original profile, write
\(\mu=\lambda^j\zeta c d^3\), \(j\ge-4\). The source formulas express
its raw coefficient as

\[
 a^*(\mu)=C_{j,\zeta}\widetilde g(c)\kappa_{j,\zeta}(c)(Nd)^{1/2},
 \qquad |C_{j,\zeta}|\ll3^{j/6},
 \tag{D13}
\]

on their stated support. All absent source cases have \(C_{j,\zeta}=0\).
The profile \(\kappa_{j,\zeta}\) is cubic, so
\(\kappa_{j,\zeta}(cd^3)=\kappa_{j,\zeta}(c)\).
The ramified scale and angle contribute
\(3^{-jw}\alpha(\lambda^j\zeta)^{-\ell}\).
Thus each ramified component is exactly a scalar multiple of (D4),
with \(a=-\ell\), after a fixed unit change of the Ramanujan argument.
Such a unit change does not affect \(c_r\).

Grouping the nonzero \(j\)'s into their finitely many residue classes
produces convergent geometric scalar factors for \(\Re w>1/6\).
The meromorphic identity (D5) can therefore be applied component by
component wherever the corresponding profile series continue.

## 5. The initial finite cubic profiles are explicit

By DR (1.5), a primary \(c\) has unique coordinates

\[
 c\equiv1+\alpha_2\lambda^2+\alpha_3\lambda^3\pmod9,
 \quad\alpha_2,\alpha_3\in\mathbb F_3,
 \qquad
 (\omega/c)_3=\omega^{\alpha_2},\quad
 (\lambda/c)_3=\omega^{-\alpha_3}.
 \tag{D14}
\]

The nine characters of this group are
\(\kappa_{a,b}(c)=\omega^{a\alpha_2+b\alpha_3}\).
The coordinates add under multiplication because the cross term is
divisible by \(\lambda^4=9\).

For \(t=0,1,2\), the change of variable in the primitive cubic Gauss sum
gives

\[
 \frac{g(\omega^t\lambda^2,c)}{\sqrt{Nc}}
   =\widetilde g(c)\,\kappa_{-t,-1}(c).
 \tag{D15}
\]

The exceptional \(j=-4\) term has an additive factor
\(\check e(\lambda^{-4}\zeta cd^3)\).
Every primary \(d\) satisfies \(d^3\equiv1\pmod9\). After removing the
fixed scalar \(\check e(\lambda^{-4}\zeta)\), this factor is

\[
 \check e\bigl(\lambda^{-4}\zeta(c-1)\bigr)
 =\omega^{-\alpha_2\operatorname{Tr}_{E/\mathbb Q}\zeta}
 =\kappa_{-\operatorname{Tr}\zeta,0}(c).
 \tag{D16}
\]

Indeed \(\operatorname{Tr}(\zeta\lambda)\) is divisible by 3 for every
Eisenstein unit. This proves that the initial profiles in (D13) lie in
\(\{\kappa_{0,0}\}\cup\{\kappa_{a,-1}:a\in\mathbb F_3\}\).
This is a profile list for the *first* reflected series only. Proving
closure under repeated reflection requires the separate finite-profile
argument; (D14)--(D16) alone do not establish it.

## 6. Finite verification and its scope

The companion checker verifies the nine-element group and (D16) using
exact integer arithmetic in \(\mathbb Z[\omega]/9\).
It also checks the truncated two-prime formal-series identity (D5)
with nontrivial cubic reciprocity phases, signed Ramanujan factors,
cube coefficients, and zero extensions. This checks algebra and catches
sign or Euler-factor omissions. It does not verify automorphy, analytic
continuation, contour shifts, finite-profile closure, or any infinite
mean-value theorem.
