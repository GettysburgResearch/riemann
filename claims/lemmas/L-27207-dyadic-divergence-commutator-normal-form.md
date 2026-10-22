# L-27207 — Exact dyadic divergence commutator normal form

Claim ID: `L-27207`  
Title: The complete carry target at endpoint \(2Y\) is an exact half-scale lift plus one bottom charge and one odd-node adjacent-tree commutator  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26205`, `L-27204`; elementary Möbius inversion  
Scope: arbitrary finite targets with exact even-column scaling; no RH assumption

## 1. Target divergence

Let \(Y\ge2\), \(X=2Y\), and let \(\alpha>0\). Suppose finite targets \(w_Y(2),\ldots,w_Y(Y)\) and \(w_X(2),\ldots,w_X(X)\) satisfy

\[
\boxed{w_X(2q)=\alpha\,w_Y(q)\qquad(2\le q\le Y).}
\tag{L-27207.1}
\]

The bottom column \(w_X(2)\) and every odd column of \(w_X\) are otherwise arbitrary.

For an endpoint \(Z\) and target \(w_Z\), define

\[
u_Z(m)=\sum_{k\le Z/m}\mu(k)w_Z(mk),\qquad 2\le m\le Z,
\tag{L-27207.2}
\]

put \(u_Z(Z+1)=0\), and set

\[
r_Z(m)=u_Z(m)-u_Z(m+1)\qquad(2\le m\le Z),
\tag{L-27207.3}
\]

\[
r_Z(1)=-\sum_{m=2}^{Z}m\,r_Z(m).
\tag{L-27207.4}
\]

By `L-26205`, \(r_Z\) is the unique size-zero node divergence whose carry columns are \(w_Z\).

Let \(\mathcal D_2\) denote node dilation:

\[
(\mathcal D_2r)(2m)=r(m),\qquad(\mathcal D_2r)(2m+1)=0.
\tag{L-27207.5}
\]

## 2. Pair identity away from the bottom

For every \(a\ge2\), (L-27207.1) gives

\[
u_X(2a)=\alpha u_Y(a),\qquad u_X(2a+2)=\alpha u_Y(a+1).
\tag{L-27207.6}
\]

Therefore

\[
\boxed{r_X(2a)+r_X(2a+1)=\alpha r_Y(a)\qquad(2\le a\le Y).}
\tag{L-27207.7}
\]

Thus, after subtracting the dilated lower divergence, every pair \((2a,2a+1)\), \(a\ge2\), is exactly the dipole

\[
r_X(2a+1)(e_{2a+1}-e_{2a}).
\tag{L-27207.8}
\]

The only unmatched pair is the bottom pair \((2,3)\).

## 3. Central trees and adjacent commutators

Retain the canonical central trees of `L-27204`:

\[
T_1=0,\qquad T_n=[n,\lfloor n/2\rfloor]+T_{\lfloor n/2\rfloor}+T_{\lceil n/2\rceil}.
\tag{L-27207.9}
\]

They satisfy

\[
\partial T_n=e_n-ne_1.
\tag{L-27207.10}
\]

Define the adjacent-tree commutator

\[
\boxed{E_n=T_{n+1}-T_n.}
\tag{L-27207.11}
\]

Then

\[
\boxed{\partial E_n=e_{n+1}-e_n-e_1.}
\tag{L-27207.12}
\]

The commutators have the sparse binary recursions

\[
\boxed{E_{2m}=[2m+1,m]-[2m,m]+E_m,}
\tag{L-27207.13}
\]

\[
\boxed{E_{2m+1}=[2m+2,m+1]-[2m+1,m]+E_m,}
\tag{L-27207.14}
\]

with \(E_1=T_2=[2,1]\). Hence

\[
\boxed{\|E_n\|_1\le2\lfloor\log_2n\rfloor+1.}
\tag{L-27207.15}
\]

Every edge occurring in \(E_n\) is \(1/4\)-balanced. The commutator is therefore a legal sparse cycle/deformation object in the balanced fragmentation space used on this branch.

## 4. The exact bottom coefficient

Put

\[
c_X=r_X(2)-\alpha r_Y(1)+r_X(3).
\tag{L-27207.16}
\]

The definition of \(r_Y(1)\) and telescoping of (L-27207.3) give

\[
c_X=u_X(2)+\sum_{m=2}^{Y}u_X(2m)=\sum_{m=1}^{Y}u_X(2m).
\tag{L-27207.17}
\]

Expanding \(u_X\) and grouping by \(\ell=mk\),

\[
\begin{aligned}
\sum_{m=1}^{Y}u_X(2m)
&=\sum_{\ell\le Y}w_X(2\ell)\sum_{k\mid\ell}\mu(k)\\
&=w_X(2).
\end{aligned}
\tag{L-27207.18}
\]

Thus the unmatched bottom dipole is not an error term:

\[
\boxed{c_X=w_X(2).}
\tag{L-27207.19}
\]

It is the exact logarithmic/bottom carry charge.

## 5. Exact divergence identity

Combining (L-27207.7), (L-27207.12), and (L-27207.19) gives

\[
\boxed{
r_X=\alpha\,\mathcal D_2r_Y+w_X(2)\,\partial T_2+\sum_{a=1}^{Y-1}r_X(2a+1)\,\partial E_{2a}.
}
\tag{L-27207.20}
\]

No asymptotic estimate, positivity assertion, or zeta-zero hypothesis enters this identity.

The three terms are respectively:

1. the exact lower-scale divergence;
2. the immutable bottom logarithmic charge;
3. the complete odd-node commutator.

There is no remaining diffuse same-scale source.

## 6. Exact flow lift

For a split flow \(d\), let

\[
(\mathcal L_2d)_{(2n,2j)}=d_{(n,j)}
\tag{L-27207.21}
\]

and set all other coefficients to zero. If \(d_Y\) is any exact balanced signed flow with

\[
\partial d_Y=r_Y,
\tag{L-27207.22}
\]

define

\[
\boxed{
d_X^{\mathrm{com}}(d_Y)=\alpha\mathcal L_2d_Y+w_X(2)T_2+\sum_{a=1}^{Y-1}r_X(2a+1)E_{2a}.
}
\tag{L-27207.23}
\]

Then

\[
\boxed{\partial d_X^{\mathrm{com}}(d_Y)=r_X.}
\tag{L-27207.24}
\]

By the exact divergence/carry equivalence in `L-26205`,

\[
\boxed{\sum_e d_X^{\mathrm{com}}(e)\chi_e(q)=w_X(q)\qquad(2\le q\le X).}
\tag{L-27207.25}
\]

Thus (L-27207.23) is a complete exact producer, not merely a node-level formal identity.

## 7. Capacity splitting and the true half contraction

Use the source-adapted capacity weight of `L-27205`:

\[
\omega_{n,j}=\sum_{q=2}^{n}\frac{\chi_{n,j}(q)}{\sqrt q}.
\tag{L-27207.26}
\]

For a doubled edge \(\widetilde e=(2n,2j)\), define its odd-column part

\[
\omega_{\mathrm{odd}}(\widetilde e)=\sum_{\substack{3\le q\le2n\\q\ {\rm odd}}}\frac{\chi_{2n,2j}(q)}{\sqrt q}.
\tag{L-27207.27}
\]

The even columns give the exact decomposition

\[
\boxed{\omega_{\widetilde e}=2^{-1/2}\omega_e+\omega_{\mathrm{odd}}(\widetilde e).}
\tag{L-27207.28}
\]

For the RH target, \(\alpha=2^{-1/2}\). Therefore the negative capacity debt of the lifted part is exactly

\[
\boxed{
\mathcal N_\omega(2^{-1/2}\mathcal L_2d)=\frac12\mathcal N_\omega(d)+2^{-1/2}\sum_{d_e<0}(-d_e)\omega_{\mathrm{odd}}(2e).
}
\tag{L-27207.29}
\]

This is the first genuine contraction in the Cycle Debt metric. The factor \(1/2\) is exact. Its sole obstruction is the odd-column leakage, which must be combined with—not estimated separately from—the adjacent-tree commutator in (L-27207.23).

## 8. Paired odd-commutator excess

Write

\[
Q_Y=\sum_{a=1}^{Y-1}r_X(2a+1)E_{2a}.
\tag{L-27207.30}
\]

Adding the positive bottom coefficient \(w_X(2)T_2\) cannot increase negative capacity debt. Define the source-complete paired excess

\[
\boxed{
\mathfrak E_Y(d)=\left[\mathcal N_\omega\left(2^{-1/2}\mathcal L_2d+Q_Y\right)-\frac12\mathcal N_\omega(d)\right]_+.
}
\tag{L-27207.31}
\]

Then every exact lower flow gives the rigorous upper bound

\[
\boxed{\mathfrak N_\eta(2Y)\le\frac12\mathcal N_\omega(d)+\mathfrak E_Y(d),}
\tag{L-27207.32}
\]

where \(\mathfrak N_\eta\) is the optimized Cycle Debt of `L-27205`.

The definition (L-27207.31) keeps every cancellation between lifted odd-column leakage and the Möbius commutator. Replacing it by separate absolute values would discard the coherent source and return to the invalid unsigned surrogates rejected elsewhere in the repository.

## 9. Proof boundary

Closed exactly here:

- even-column scaling of the Möbius divergence;
- the complete bottom-charge coefficient;
- sparse adjacent-tree commutator normal form;
- exact flow and carry-column replay;
- the exact factor-\(1/2\) capacity contraction;
- localization of all remaining debt to the paired odd commutator.

Open:

- a subpower or polylogarithmic bound for \(\mathfrak E_Y(d)\) on a compatible cofinal family of lower flows;
- Cycle Debt;
- RH.
