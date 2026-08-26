# L-106093 — Mellin polarization places the least-discrepancy anchor inside one amplified family moment

Claim ID: `L-106093`  
Programme aliases: `LFAM1.ANCHOR_AMPLIFIED_ROUGH_TAIL`, `LFAM2.MELLIN_GAUSS_INDIVIDUALIZATION`, `STRESS.FIRST_DIFFERENCE_HYBRID_MOMENT`  
Status: **PROVED EXACT MELLIN/GAUSS NORMAL FORM AND PRINCIPAL EMBEDDING**  
Created: 2026-08-25  
Depends on: `L-106090--L-106092`; `L-106020`, `L-106027`; parent `L-102959`, `T-106030`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The fixed-anchor Cauchy route duplicates one opposite rough tail for every
compatible anchor.  This lemma keeps the anchor inside the amplifier before
any square is taken.

Work in one frozen physical shell of the coprime two-sided current.  Fix:

\[
g\ge1,\qquad
\ell\ {\rm prime},\qquad
Q\ {\rm an\ opposite\ semiprime\ owner\ product},
\qquad
\sigma=\kappa_\ell(Qg^2)\in\{\pm1\}.
\tag{L-106093.1}
\]

The clean source guarantees \((gQ,\ell)=1\).

Let \(\alpha\) range over all left anchors with this common core \(g\) and
least-discrepancy prime \(\ell\).  Write \(A_\alpha(t)\) for the complete
Mellin amplitude of the anchor, including its Boolean coefficient, canonical
equal-pair share, owner product, shell, carrier, marked-prime and renewal
labels.

Let \(\mathcal T_{\alpha;g,Q,\sigma}\) be the opposite atoms with this fixed
\(g,Q,\sigma\) and satisfying

\[
P^-(d)>\ell,\qquad(d,c_\alpha)=1.
\tag{L-106093.2}
\]

Put

\[
B_{\alpha;g,Q,\sigma,h}(t)
=
\sum_{\beta\in\mathcal T_{\alpha;g,Q,\sigma}}
b_\beta(t)e_\ell(-hM_\beta),
\qquad
0\le h<\ell,
\tag{L-106093.3}
\]

where \(M_\beta=Qg^2d^2\) is the literal opposite physical integer.

## 1. Anchor amplification before squaring

Define

\[
\boxed{
Z_{g,\ell,Q,\sigma,h}(t)
=
\sum_{\substack{\alpha\\
g_\alpha=g,\ \ell_\alpha=\ell}}
\overline{A_\alpha(t)}\,
B_{\alpha;g,Q,\sigma,h}(t).
}
\tag{L-106093.4}
\]

The anchor-dependent coprimality and incidence masks remain inside the
opposite packet.  No tail is placed in an orthogonal anchor copy after
physical observation.

Mellin--Plancherel and the exact Ramanujan identity of `L-106090` give

\[
\boxed{
\mathcal C_{\rm 2s}
=
2\operatorname{Re}\,
\frac1{2\pi}
\int_{\mathbf R}
|\widehat\kappa(t)|^2
\sum_{g,\ell,Q}\sum_{\sigma=\pm1}
Z_{g,\ell,Q,\sigma,0}(t)\,dt .
}
\tag{L-106093.5}
\]

Every unordered interaction occurs once by its unique least-discrepancy
orientation.

## 2. Exact amplified even-character family

For an even character \(\eta\bmod\ell\), let
\(B_{\alpha;g,Q,\sigma,\eta}(t)\) be the multiplicative transform of
(L-106093.3), with the two square roots of \(\eta\) combined inside the fixed
owner quadratic class \(\sigma\), as in `L-106027`.  Define

\[
Z_{g,\ell,Q,\sigma,\eta}(t)
=
\sum_{\substack{\alpha\\g_\alpha=g,\ \ell_\alpha=\ell}}
\overline{A_\alpha(t)}
B_{\alpha;g,Q,\sigma,\eta}(t).
\tag{L-106093.6}
\]

Linearity of the Gauss transform in the tail and then in the anchor yields

\[
\boxed{
\sum_{h=1}^{\ell-1}
|Z_{g,\ell,Q,\sigma,h}(t)|^2
=
\frac{\ell+1}{\ell-1}
|Z_{g,\ell,Q,\sigma,1}(t)|^2
+
\frac{2\ell}{\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|Z_{g,\ell,Q,\sigma,\eta}(t)|^2.
}
\tag{L-106093.7}
\]

Here the subscript \(1\) denotes the principal even character, equivalently

\[
Z_{g,\ell,Q,\sigma,1}(t)
=
Z_{g,\ell,Q,\sigma,0}(t).
\tag{L-106093.8}
\]

The family square is therefore taken only after the full left-anchor
amplifier has been assembled.

## 3. Natural source-dual moment

Define

\[
\boxed{
\begin{aligned}
\mathfrak M_{\rm LDRT}(Y)
={1\over2\pi}
\sum_{g,\ell,Q}
g^2\ell Q
\sum_{\sigma=\pm1}
\int_{\mathbf R}
|\widehat\kappa(t)|^2
\Bigg[
&{\ell+1\over\ell-1}
|Z_{g,\ell,Q,\sigma,1}(t)|^2\\
&+{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|Z_{g,\ell,Q,\sigma,\eta}(t)|^2
\Bigg]dt .
\end{aligned}
}
\tag{L-106093.9}
\]

The weight

\[
g^2\ell Q
\tag{L-106093.10}
\]

is the dual of the literal common-core, selected-core-prime and opposite-owner
weights in the physical coefficient.  It is not a freely inserted amplifier.

For the principal amplitudes,

\[
\begin{aligned}
\left|
\sum_{g,\ell,Q,\sigma}
Z_{g,\ell,Q,\sigma,1}(t)
\right|^2
\le{}&
2
\left(
\sum_{g,\ell,Q}{1\over g^2\ell Q}
\right)\\
&\times
\left(
\sum_{g,\ell,Q,\sigma}
g^2\ell Q
|Z_{g,\ell,Q,\sigma,1}(t)|^2
\right).
\end{aligned}
\tag{L-106093.11}
\]

On a finite horizon,

\[
\sum_g{1\over g^2}<\infty,\qquad
\sum_\ell{1\over\ell}\ll\log\log Y,\qquad
\sum_{Q=pq}{1\over Q}\ll(\log\log Y)^2.
\tag{L-106093.12}
\]

Cauchy in \(t\) and (L-106093.5) consequently give

\[
\boxed{
\mathfrak M_{\rm LDRT}(Y)=Y^{o(1)}
\Longrightarrow
|\mathcal C_{\rm 2s}(Y)|=Y^{o(1)}.
}
\tag{L-106093.13}
\]

This is an absolute bound and hence stronger than `BCI102990`.

## 4. Principal/nonprincipal split

Since every summand in (L-106093.9) is nonnegative,

\[
\mathfrak M_{\rm LDRT}
=
\mathfrak M_{\rm LDRT}^{\rm prin}
+
\mathfrak M_{\rm LDRT}^{\rm nonprin}.
\tag{L-106093.14}
\]

The first term is the anchor-amplified untwisted rough-tail moment.  The
second is a genuine moment over new even Dirichlet-L channels.  Neither
may be inferred from the other without an individualization theorem.

## Scope

The lemma repairs the main weakness of the fixed-anchor Cauchy normal form:
the opposite tail is not duplicated before the family square.  It does not
estimate (L-106093.9).  Its diagonal anchor part is closed in `L-106094`; the
remaining cross-anchor moment is the live theorem in `T-106090`.
