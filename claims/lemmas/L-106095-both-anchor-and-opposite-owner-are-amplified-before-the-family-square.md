# L-106095 — Both anchor and opposite owner are amplified before the rough-tail family square

Claim ID: `L-106095`  
Programme aliases: `LFAM1.FULLY_AMPLIFIED_ROUGH_TAIL`, `LFAM2.OWNER_ANCHOR_MELLIN_GAUSS`, `STRESS.CORRECTED_SOURCE_DUAL_MOMENT`  
Status: **PROVED EXACT CORRECTED MELLIN/GAUSS NORMAL FORM**  
Created: 2026-08-25  
Depends on: `L-106090--L-106093`, `R-106095`; `L-106020`, `L-106027`; parent `L-102959`, `T-106030`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix only

\[
g\ge1,\qquad
\ell\ {\rm prime},\qquad
\sigma\in\{\pm1\}.
\tag{L-106095.1}
\]

Let \(\alpha\) range over every left anchor with common core \(g\) and least
discrepancy prime \(\ell\).

For one anchor, let \(\mathcal T_{\alpha;g,\ell,\sigma}\) contain **all**
opposite atoms

\[
\beta=(Q,d,\text{owner, Boolean, shell, carrier and renewal labels})
\]

such that

\[
P^-(d)>\ell,\qquad(d,c_\alpha)=1,\qquad
\kappa_\ell(Qg^2)=\sigma.
\tag{L-106095.2}
\]

Define

\[
B_{\alpha;g,\ell,\sigma,h}(t)
=
\sum_{\beta\in\mathcal T_{\alpha;g,\ell,\sigma}}
b_\beta(t)e_\ell(-hQg^2d^2),
\qquad 0\le h<\ell.
\tag{L-106095.3}
\]

Thus the opposite owner product \(Q\) is summed inside the field.

## 1. Fully amplified phase member

Put

\[
\boxed{
\widetilde Z_{g,\ell,\sigma,h}(t)
=
\sum_{\substack{\alpha\\g_\alpha=g,\ell_\alpha=\ell}}
\overline{A_\alpha(t)}
B_{\alpha;g,\ell,\sigma,h}(t).
}
\tag{L-106095.4}
\]

Both coherent dimensions are now assembled before squaring:

```text
left anchor:
  c, P and all anchor labels;

opposite tail:
  Q, d and all opposite labels.
```

Mellin--Plancherel gives the exact current

\[
\boxed{
\mathcal C_{\rm 2s}
=
2\operatorname{Re}{1\over2\pi}
\int_{\mathbf R}
|\widehat\kappa(t)|^2
\sum_{g,\ell}\sum_{\sigma=\pm1}
\widetilde Z_{g,\ell,\sigma,0}(t)\,dt.
}
\tag{L-106095.5}
\]

## 2. Exact even-character transform with varying \(Q\)

Inside one \(\sigma\)-sector, choose a fixed representative
\(u_\sigma\in\mathbf F_\ell^\times\).  For every \(Q\) in the sector there is
\(r_Q\in\mathbf F_\ell^\times\) such that

\[
Qg^2\equiv u_\sigma r_Q^2\pmod\ell.
\tag{L-106095.6}
\]

Therefore

\[
e_\ell(-hQg^2d^2)
=
e_\ell(-hu_\sigma(r_Qd)^2).
\]

The multiplicative transform sees the combined variable \(r_Qd\).  Let
\(\widetilde Z_{g,\ell,\sigma,\eta}(t)\) be the result of replacing every
additive phase by the even character \(\eta(r_Qd)\), with the two square roots
combined as in `L-106027`.

Linearity gives

\[
\boxed{
\sum_{h=1}^{\ell-1}
|\widetilde Z_{g,\ell,\sigma,h}(t)|^2
=
{\ell+1\over\ell-1}
|\widetilde Z_{g,\ell,\sigma,1}(t)|^2
+
{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\widetilde Z_{g,\ell,\sigma,\eta}(t)|^2.
}
\tag{L-106095.7}
\]

Here

\[
\widetilde Z_{g,\ell,\sigma,1}
=
\widetilde Z_{g,\ell,\sigma,0}.
\tag{L-106095.8}
\]

## 3. Correct source-dual moment

Define

\[
\boxed{
\begin{aligned}
\widetilde{\mathfrak M}_{\rm LDRT}(Y)
={1\over2\pi}
\sum_{g,\ell}g^2\ell
\sum_{\sigma=\pm1}
\int |\widehat\kappa(t)|^2
\Bigg[
&{\ell+1\over\ell-1}
|\widetilde Z_{g,\ell,\sigma,1}(t)|^2\\
&+{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\widetilde Z_{g,\ell,\sigma,\eta}(t)|^2
\Bigg]dt .
\end{aligned}
}
\tag{L-106095.9}
\]

There is no separate \(Q\)-weight: its reciprocal source coefficient remains
inside the fully amplified family member.

The dual index sum is now genuinely subpower:

\[
\sum_{g,\ell}{1\over g^2\ell}
\ll\log\log Y.
\tag{L-106095.10}
\]

Consequently,

\[
\boxed{
\widetilde{\mathfrak M}_{\rm LDRT}(Y)=Y^{o(1)}
\Longrightarrow
|\mathcal C_{\rm 2s}(Y)|=Y^{o(1)}.
}
\tag{L-106095.11}
\]

## 4. Positive split

Write

\[
\widetilde{\mathfrak M}_{\rm LDRT}
=
\widetilde{\mathfrak M}_{\rm prin}
+
\widetilde{\mathfrak M}_{\rm nonprin}.
\tag{L-106095.12}
\]

The principal member contains the native anchor/opposite-owner amplifier.  The
nonprincipal members are new even L-channels in which both owner and core
variables remain literal.

## Scope

This lemma repairs the \(Q\)-dimension error without using an orthogonal owner
coordinate.  It does not estimate the corrected moment.  `L-106096` pays its
literal atomic diagonal; the remaining cross-incidence moment is stated in
`T-106100`.
